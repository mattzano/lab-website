#!/usr/bin/env python3
"""Build the Publications page feed for the NeuroMuscle Lab website.

What it does
  1. For every member in data/members.json, searches PubMed (NCBI E-utilities)
     and downloads the matching records.
  2. Keeps a paper for a member only if that member really is an author: surname,
     first name and (optionally) the author's own affiliation must match. This drops
     homonyms such as a different "Cavallo F".
  3. Adds citation counts from OpenAlex (used to pick "key" papers).
  4. Saves everything to data/publications.json (a cache, so the page still builds
     offline) and writes _publications/feed.md, which publications.qmd includes:
       - "Latest": the most recent papers across the whole lab, newest first;
       - "Key papers by member": up to N papers per member from the last K years.
         Pinned key_pmids win; otherwise papers where the member is first or last
         author are preferred, then the most cited, then the newest.

Usage (from the repo root)
  python3 scripts/update_publications.py            # fetch from PubMed/OpenAlex, then build
  python3 scripts/update_publications.py --offline  # rebuild the feed from the cache only
  python3 scripts/update_publications.py --no-citations

Only the Python standard library is used. No API key is needed; set NCBI_API_KEY
(or settings.ncbi_api_key) to raise PubMed's rate limit.
"""
import argparse
import datetime as dt
import html
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMBERS = os.path.join(ROOT, "data", "members.json")
CACHE = os.path.join(ROOT, "data", "publications.json")
FEED = os.path.join(ROOT, "_publications", "feed.md")

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
OPENALEX = "https://api.openalex.org/works"
UA = "neuromusclelab.org publications updater (python-urllib)"
MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


# ----------------------------------------------------------------------------- helpers

def fold(s):
    """Lower-case, strip accents and punctuation, for name comparison."""
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z ]", "", s.lower()).strip()


def http_get(url, params, tries=4):
    q = urllib.parse.urlencode(params, safe=":/|,")
    req = urllib.request.Request(url + "?" + q, headers={"User-Agent": UA})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:  # network hiccups, 429s
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))
            print(f"  retrying ({e})", file=sys.stderr)


def parse_month(m):
    if not m:
        return 1
    m = m.strip()
    if m.isdigit():
        return max(1, min(12, int(m)))
    return MONTHS.get(m[:3].lower(), 1)


# ----------------------------------------------------------------------------- PubMed

def pubmed_search(query, mindate, settings):
    params = {"db": "pubmed", "term": query, "retmax": 1000, "retmode": "json",
              "datetype": "pdat", "mindate": mindate, "maxdate": "3000", "tool": "neuromusclelab"}
    key = os.environ.get("NCBI_API_KEY") or settings.get("ncbi_api_key")
    if key:
        params["api_key"] = key
    if settings.get("contact_email"):
        params["email"] = settings["contact_email"]
    data = json.loads(http_get(EUTILS + "esearch.fcgi", params))
    return data.get("esearchresult", {}).get("idlist", [])


def text_of(el):
    return "".join(el.itertext()).strip() if el is not None else ""


def parse_article(art):
    mc = art.find("MedlineCitation")
    a = mc.find("Article")
    pmid = text_of(mc.find("PMID"))
    journal = a.find("Journal")
    iso = text_of(journal.find("ISOAbbreviation")) if journal is not None else ""
    jtitle = text_of(journal.find("Title")) if journal is not None else ""
    pd = journal.find("JournalIssue/PubDate") if journal is not None else None
    year = text_of(pd.find("Year")) if pd is not None else ""
    month = text_of(pd.find("Month")) if pd is not None else ""
    day = text_of(pd.find("Day")) if pd is not None else ""
    if not year and pd is not None:
        md = text_of(pd.find("MedlineDate"))
        m = re.search(r"(\d{4})\s*([A-Za-z]{3})?", md)
        if m:
            year, month = m.group(1), m.group(2) or ""
    epub = a.find("ArticleDate")
    edate = None
    if epub is not None and text_of(epub.find("Year")):
        edate = {"year": text_of(epub.find("Year")), "month": text_of(epub.find("Month")),
                 "day": text_of(epub.find("Day"))}
    authors = []
    for au in a.findall("AuthorList/Author"):
        if au.find("CollectiveName") is not None:
            continue
        authors.append({
            "last": text_of(au.find("LastName")),
            "fore": text_of(au.find("ForeName")),
            "initials": text_of(au.find("Initials")),
            "affs": [text_of(x) for x in au.findall("AffiliationInfo/Affiliation")],
        })
    doi = ""
    for aid in art.findall("PubmedData/ArticleIdList/ArticleId"):
        if aid.get("IdType") == "doi":
            doi = text_of(aid)
    if not doi:
        for el in a.findall("ELocationID"):
            if el.get("EIdType") == "doi":
                doi = text_of(el)
    types = [text_of(t) for t in a.findall("PublicationTypeList/PublicationType")]
    return {
        "pmid": pmid, "doi": doi, "title": text_of(a.find("ArticleTitle")),
        "journal": jtitle, "journal_abbrev": iso,
        "pubdate": {"year": year, "month": month, "day": day}, "epubdate": edate,
        "authors": authors, "types": types,
    }


def pubmed_fetch(pmids, settings):
    out = []
    for i in range(0, len(pmids), 150):
        batch = pmids[i:i + 150]
        params = {"db": "pubmed", "id": ",".join(batch), "retmode": "xml", "tool": "neuromusclelab"}
        key = os.environ.get("NCBI_API_KEY") or settings.get("ncbi_api_key")
        if key:
            params["api_key"] = key
        root = ET.fromstring(http_get(EUTILS + "efetch.fcgi", params))
        out += [parse_article(x) for x in root.findall("PubmedArticle")]
        time.sleep(0.4)
    return out


# ----------------------------------------------------------------------------- OpenAlex

def openalex_citations(dois):
    cites = {}
    dois = [d for d in dois if d]
    for i in range(0, len(dois), 40):
        batch = dois[i:i + 40]
        flt = "doi:" + "|".join("https://doi.org/" + d for d in batch)
        try:
            data = json.loads(http_get(OPENALEX, {"filter": flt, "per-page": 50,
                                                  "select": "doi,cited_by_count"}))
        except Exception as e:
            print(f"  OpenAlex failed for a batch ({e}); citations skipped", file=sys.stderr)
            continue
        for w in data.get("results", []):
            d = (w.get("doi") or "").replace("https://doi.org/", "").lower()
            cites[d] = w.get("cited_by_count", 0)
        time.sleep(0.2)
    return cites


# ----------------------------------------------------------------------------- matching

def author_index(rec, m):
    """Position of member m in rec's author list, or None if not a real match."""
    lasts = {fold(x) for x in m["last_names"]}
    firsts = [fold(x) for x in m.get("first_names", [])]
    affs = [a.lower() for a in m.get("affiliations", [])]
    any_aff = any(k in aff.lower() for au in rec["authors"] for aff in au["affs"] for k in affs) if affs else True
    for i, au in enumerate(rec["authors"]):
        if fold(au["last"]) not in lasts:
            continue
        fore = fold(au["fore"])
        if len(fore.replace(" ", "")) > 2:            # full first name available
            if firsts and not any(fore.startswith(f) for f in firsts):
                continue
        else:                                         # only initials in the record
            if m.get("initials") and not fold(au["initials"]).startswith(fold(m["initials"])[:1]):
                continue
        if affs:
            own = " ".join(au["affs"]).lower()
            if own and not any(k in own for k in affs):
                continue
            if not own and not any_aff:
                continue
        return i
    return None


def rec_date(rec):
    d = rec.get("epubdate") or rec["pubdate"]
    try:
        y = int(d.get("year") or rec["pubdate"].get("year"))
    except (TypeError, ValueError):
        return dt.date(1900, 1, 1)
    mo = parse_month(d.get("month"))
    try:
        da = int(d.get("day") or 1)
    except ValueError:
        da = 1
    try:
        return dt.date(y, mo, da)
    except ValueError:
        return dt.date(y, mo, 1)


# ----------------------------------------------------------------------------- rendering

def esc(s):
    return html.escape(s or "", quote=True)


def clean_title(t):
    t = re.sub(r"\s+", " ", t or "").strip()
    return t[:-1] if t.endswith(".") else t


def author_html(rec, member_positions):
    names = [f"{a['last']} {a['initials']}".strip() for a in rec["authors"]]
    n = len(names)
    if n == 0:
        return ""
    show = set(range(n)) if n <= 6 else ({0, 1, 2, n - 1} | set(member_positions))
    parts, prev = [], -1
    for i in sorted(show):
        if i - prev > 1:
            parts.append("…")
        nm = esc(names[i])
        parts.append(f"<strong>{nm}</strong>" if i in member_positions else nm)
        prev = i
    return ", ".join(parts)


def link_for(rec):
    if rec.get("doi"):
        return "https://doi.org/" + rec["doi"]
    return f"https://pubmed.ncbi.nlm.nih.gov/{rec['pmid']}/"


def month_year(rec):
    d = rec_date(rec)
    return f"{MONTH_NAMES[d.month - 1]} {d.year}"


def render(cfg, records, matches, cites, generated):
    s = cfg["settings"]
    members = cfg["members"]
    by_pmid = {r["pmid"]: r for r in records}
    excl_types = set(s.get("exclude_types", []))

    def ok(r):
        return not (set(r.get("types", [])) & excl_types)

    pos = {}  # pmid -> set of author indices that are lab members
    for mid, items in matches.items():
        for pmid, idx in items.items():
            pos.setdefault(pmid, set()).add(idx)

    # Latest across the lab
    lab = [by_pmid[p] for p in pos if p in by_pmid and ok(by_pmid[p])]
    lab.sort(key=lambda r: (rec_date(r), r["pmid"]), reverse=True)
    latest = lab[: int(s.get("latest_count", 12))]

    out = ["```{=html}", '<section class="nm-pubs-latest" aria-labelledby="pubs-latest">',
           '<h2 id="pubs-latest">Latest publications</h2>',
           f'<p class="nm-pubs-updated">From PubMed · updated {esc(generated)}</p>', '<div class="nm-publist">']
    for r in latest:
        out.append(pub_row(r, pos.get(r["pmid"], set()), show_year=True))
    out += ["</div>", "</section>"]

    # Key papers per member
    cutoff = dt.date.today().replace(year=dt.date.today().year - int(s.get("key_years", 5)))
    k = int(s.get("key_count", 5))
    out += ['<section class="nm-pubs-members" aria-labelledby="pubs-members">',
            f'<h2 id="pubs-members">Key papers by lab member</h2>',
            f'<p class="nm-pubs-updated">Up to {k} papers per person from the last {s.get("key_years", 5)} years.</p>',
            '<div class="nm-member-pubs-grid">']
    for m in members:
        mine = matches.get(m["id"], {})
        key_excl = set(s.get("key_exclude_types", []))
        cands = [by_pmid[p] for p in mine if p in by_pmid and ok(by_pmid[p])
                 and not (set(by_pmid[p].get("types", [])) & key_excl)
                 and p not in m.get("exclude_pmids", []) and rec_date(by_pmid[p]) >= cutoff]
        if not cands:
            continue
        pinned = [by_pmid[p] for p in m.get("key_pmids", []) if p in by_pmid]
        if pinned:
            keys = pinned[:k]
        else:
            def score(r):
                i, n = mine[r["pmid"]], len(r["authors"])
                lead = 2 if (i == 0 or i == n - 1) else (1 if i in (1, n - 2) else 0)
                return (lead, cites.get((r.get("doi") or "").lower(), -1), rec_date(r))
            keys = sorted(cands, key=score, reverse=True)[:k]
            keys.sort(key=rec_date, reverse=True)
        photo = m.get("photo")
        face = f'<img src="{esc(photo)}" alt="" loading="lazy">' if photo else ""
        pm_link = "https://pubmed.ncbi.nlm.nih.gov/?term=" + urllib.parse.quote(m["pubmed_query"]) + "&sort=date"
        out.append('<article class="nm-member-pubs">')
        out.append(f'<header>{face}<div><h3>{esc(m["name"])}</h3><span class="nm-role">{esc(m.get("role", ""))}</span></div></header>')
        out.append("<ol>")
        for r in keys:
            out.append(
                f'<li><a href="{esc(link_for(r))}">{esc(clean_title(r["title"]))}</a>'
                f'<span class="nm-meta"><em>{esc(r.get("journal_abbrev") or r.get("journal"))}</em>, {rec_date(r).year}</span></li>')
        out.append("</ol>")
        out.append(f'<a class="nm-member-all" href="{esc(pm_link)}">All papers on PubMed</a>')
        out.append("</article>")
    out += ["</div>", "</section>", "```", ""]
    return "\n".join(out)


def pub_row(r, positions, show_year=True):
    return (f'<div class="nm-pubrow"><span class="nm-year">{rec_date(r).year}</span><div>'
            f'<a href="{esc(link_for(r))}">{esc(clean_title(r["title"]))}</a>'
            f'<span class="nm-authors">{author_html(r, positions)}</span>'
            f'<span class="nm-meta"><em>{esc(r.get("journal_abbrev") or r.get("journal"))}</em> · {month_year(r)}</span>'
            f"</div></div>")


# ----------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--offline", action="store_true", help="do not fetch; rebuild from data/publications.json")
    ap.add_argument("--no-citations", action="store_true", help="skip OpenAlex citation counts")
    ap.add_argument("--years", type=int, default=None, help="how far back to search (default: key_years + 1)")
    args = ap.parse_args()

    cfg = json.load(open(MEMBERS, encoding="utf-8"))
    # "publications": false keeps a member on the team page but out of the feed
    cfg["members"] = [m for m in cfg["members"] if m.get("publications", True)]
    s = cfg["settings"]
    cache = {"records": [], "citations": {}}
    if os.path.exists(CACHE):
        cache = json.load(open(CACHE, encoding="utf-8"))
    records = {r["pmid"]: r for r in cache.get("records", [])}
    cites = cache.get("citations", {})

    if not args.offline:
        years = args.years or int(s.get("key_years", 5)) + 1
        mindate = f"{dt.date.today().year - years}/01/01"
        wanted = set()
        for m in cfg["members"]:
            try:
                ids = pubmed_search(m["pubmed_query"], mindate, s)
                print(f"{m['name']}: {len(ids)} PubMed hits")
                wanted |= set(ids) | set(m.get("key_pmids", []))
            except Exception as e:
                print(f"{m['name']}: search failed ({e}); keeping cached papers", file=sys.stderr)
            time.sleep(0.4)
        missing = sorted(p for p in wanted if p not in records)
        if missing:
            print(f"Fetching {len(missing)} new records")
            for r in pubmed_fetch(missing, s):
                records[r["pmid"]] = r
        if not args.no_citations:
            print("Fetching citation counts from OpenAlex")
            cites.update(openalex_citations([r.get("doi", "").lower() for r in records.values()]))

    matches = {}
    for m in cfg["members"]:
        mm = {}
        for p, r in records.items():
            if p in m.get("exclude_pmids", []):
                continue
            i = author_index(r, m)
            if i is not None:
                mm[p] = i
        matches[m["id"]] = mm
        print(f"  {m['name']}: {len(mm)} papers confirmed")

    generated = dt.date.today().strftime("%-d %B %Y") if os.name != "nt" else dt.date.today().isoformat()
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    keep = sorted({p for mm in matches.values() for p in mm})  # drop homonym-only records from the cache
    json.dump({"generated": dt.date.today().isoformat(),
               "records": [records[p] for p in keep],
               "citations": {k: v for k, v in cites.items() if k},
               "matches": matches},
              open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    os.makedirs(os.path.dirname(FEED), exist_ok=True)
    with open(FEED, "w", encoding="utf-8") as f:
        f.write(render(cfg, [records[p] for p in keep], matches, cites, generated))
    print(f"Wrote {os.path.relpath(FEED, ROOT)} and {os.path.relpath(CACHE, ROOT)}")


if __name__ == "__main__":
    main()
