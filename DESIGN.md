---
name: NeuroMuscle Lab
description: From motor neuron to muscle fibre. A deep-teal anatomical world drawn in nerve blue and muscle green.
colors:
  ground: "#0B2530"
  panel: "#12394A"
  soma: "#163646"
  rule: "#2A5563"
  edge: "#5C7F88"
  text: "#E6F0F1"
  nav-text: "#CFE0E3"
  body: "#C4D7DB"
  muted: "#A3BEC4"
  placeholder: "#7C9AA1"
  nerve: "#6DB9EA"
  link: "#8FCBEF"
  link-hover: "#B9E0F6"
  muscle: "#78D3A6"
  muscle-light: "#9BE0BD"
  field-ink: "#0E3340"
typography:
  display:
    fontFamily: "Anybody, Arial Narrow, sans-serif"
    fontSize: "clamp(3rem, 7vw, 6rem)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: "-0.03em"
    fontVariation: "'wdth' 112"
  page-title:
    fontFamily: "Anybody, Arial Narrow, sans-serif"
    fontSize: "clamp(3.2rem, 7.5vw, 6.5rem)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: "-0.02em"
    fontVariation: "'wdth' 120"
  headline:
    fontFamily: "Anybody, Arial Narrow, sans-serif"
    fontSize: "clamp(2.2rem, 4vw, 3.5rem)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.02em"
    fontVariation: "'wdth' 110"
  title:
    fontFamily: "Anybody, Arial Narrow, sans-serif"
    fontSize: "1.75rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
    fontVariation: "'wdth' 105"
  numeral:
    fontFamily: "Anybody, Arial Narrow, sans-serif"
    fontSize: "1.75rem"
    fontWeight: 700
    lineHeight: 1.2
    fontVariation: "'wdth' 105"
  lede:
    fontFamily: "Schibsted Grotesk, system-ui, sans-serif"
    fontSize: "1.15rem"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Schibsted Grotesk, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
  item-title:
    fontFamily: "Schibsted Grotesk, system-ui, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 600
    lineHeight: 1.35
  label:
    fontFamily: "Schibsted Grotesk, system-ui, sans-serif"
    fontSize: "0.8rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.12em"
rounded:
  field: "12px"
  tile: "14px"
  card: "20px"
  panel: "24px"
  pill: "999px"
spacing:
  gutter: "clamp(20px, 6.6vw, 96px)"
  max-width: "1440px"
  row: "28px"
  grid-tight: "32px"
  grid: "48px"
  section: "clamp(64px, 8vw, 120px)"
  section-home: "clamp(88px, 10vw, 150px)"
components:
  button-primary:
    backgroundColor: "{colors.muscle}"
    textColor: "{colors.ground}"
    typography: "{typography.item-title}"
    rounded: "{rounded.pill}"
    padding: "0 28px"
    height: "52px"
  button-primary-hover:
    backgroundColor: "{colors.muscle-light}"
    textColor: "{colors.ground}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    rounded: "{rounded.pill}"
    padding: "0 28px"
    height: "52px"
  button-ink:
    backgroundColor: "{colors.ground}"
    textColor: "{colors.text}"
    rounded: "{rounded.pill}"
    padding: "0 28px"
    height: "52px"
  button-ink-hover:
    backgroundColor: "{colors.panel}"
  nav-contact:
    backgroundColor: "transparent"
    textColor: "{colors.nerve}"
    rounded: "{rounded.pill}"
    padding: "0.6rem 1.35rem"
  input-field:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.text}"
    rounded: "{rounded.field}"
    height: "52px"
  station-paper:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    rounded: "{rounded.tile}"
    padding: "16px 20px"
  trial-card:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.body}"
    rounded: "{rounded.card}"
    padding: "28px 30px"
  join-field:
    backgroundColor: "{colors.muscle}"
    textColor: "{colors.ground}"
    padding: "clamp(64px, 8vw, 112px) 0"
---

# Design System: NeuroMuscle Lab

## Overview

**Creative North Star: "The Motor Unit, Read Top to Bottom"**

The site is a dark anatomical plate. A deep teal ground (the colour of tissue under a fluorescence scope) carries two signal colours that are never decorative: nerve blue marks everything that belongs to the neuron side (axon, nodes, dates, the active tab), muscle green marks everything that belongs to the fibre side (roles, the active nav item, the primary action, the one drenched field). The motor-unit illustration in the hero, the striated texture on placeholder frames, and the home page's gutter spine all draw from the same small anatomy kit: a 3px axon, dashed myelin, round nodes, a five-bouton endplate, horizontal or vertical striations.

Density is editorial and calm. Content runs in a 1440px column with a fluid gutter; sections are separated by generous vertical air and 1px hairline rules, not by boxes. Lists of real things (papers, news, techniques, collaborators, trials by year) are hairline-ruled rows with a nerve-blue Anybody date or number on the left. Panels are rare and reserved for things that are truly objects (a trial, a map, a form field). Headlines are wide and heavy; reading text is plain, unhurried Schibsted Grotesk.

Motion is physiological rather than decorative: an action potential runs down the hero axon every 4.2s, the home spine draws itself station by station with a clip-path as you scroll, nodes light when their section arrives, and the page chain fills a conic ring as you keep scrolling past the end. Everything stops or resolves to its final state under reduced motion.

**Key Characteristics:**
- Deep teal ground with tonal panels; no light mode.
- Two semantic accents: nerve blue (neuron side, data, navigation) and muscle green (fibre side, action, people).
- Anybody at heavy weight and wide stretch for display; Schibsted Grotesk for everything read.
- Hairline-ruled rows over cards; pills for every control.
- Anatomy as the only ornament: axon, myelin, node, endplate, striation.
- Every page ends in a "Keep scrolling to..." chain to the next page.

## Colors

A cold, low-light teal field where blue and green are anatomical signals, not brand decoration.

### Primary
- **Muscle Green** (`muscle`): the primary action colour (Join the lab, Work with us, Send request), the active navbar item, team roles, research "lines", the focus ring, text selection, checked checkboxes, the striation texture, and the home page's drenched Join field. Hover lifts to **Pale Muscle** (`muscle-light`).

### Secondary
- **Nerve Blue** (`nerve`): the neuron side of the anatomy (axon, myelin, nodes, endplate, cell body outline), the Contact pill in the navbar, the active contact tab, callout edges, list markers, and every Anybody date, year or index number in a ruled list.
- **Signal Link** (`link`): inline links and the hover colour of titles inside rows; hover lifts to **Pale Signal** (`link-hover`).

### Neutral
- **Deep Tissue Teal** (`ground`): page background, navbar, text on muscle and nerve fills, the ink button on the drenched field. Also the browser `theme-color`.
- **Panel Teal** (`panel`): the one raised tone: trial cards, form fields, map frame, photo placeholders, the default Join card on inner pages.
- **Soma Teal** (`soma`): fill of the cell-body shape on the home spine only.
- **Hairline** (`rule`): every 1px divider between rows, cards, footer zones and stations.
- **Edge** (`edge`): 1.5px outlines on ghost buttons, language switches, inputs and the navbar toggler; scrollbar thumb.
- **Bright Text** (`text`): headings, names, row titles, button text on dark.
- **Nav Text** (`nav-text`): resting navbar and tab labels.
- **Body Text** (`body`): running text.
- **Muted Text** (`muted`): ledes, meta lines, journal and date captions, footer.
- **Placeholder** (`placeholder`): input placeholders only.
- **Field Ink** (`field-ink`): body text set on the muscle-green field.

### Named Rules
**The Two Sides Rule.** Blue belongs to the nerve and green to the muscle. Data that indexes (years, dates, numbers, markers) is nerve blue; things a person does or is (actions, roles, active state) are muscle green. Never swap them for variety.

**The One Drenched Field Rule.** Muscle green fills at most one full-bleed area per page (the Join field on home). Elsewhere green appears only as text, a line, a ring or a button.

## Typography

**Display Font:** Anybody (variable, weight 100 to 900, width 50% to 150%), with Arial Narrow fallback
**Body Font:** Schibsted Grotesk (variable, 400 to 900, with italic), with system-ui fallback

Both are self-hosted woff2 under the SIL OFL; no third-party font requests.

**Character:** Anybody is pushed wide (105% to 130% stretch) and heavy (700 to 800) with tight negative tracking, so headlines read as a confident, slightly technical specimen label. Schibsted Grotesk is a sober newspaper grotesk that keeps long research text and patient information plain.

### Hierarchy
- **Display** (800, `clamp(3rem, 7vw, 6rem)`, 0.92, width 112%): the home hero statement only, balanced, max about 9.5em wide.
- **Page title** (800, `clamp(3.2rem, 7.5vw, 6.5rem)`, 0.92, width 120%): inner page heads and article titles. Drops to `clamp(2.1rem, 10.5vw, 3rem)` at 104% below 480px.
- **Headline** (800, `clamp(2.2rem, 4vw, 3.5rem)`, 1.0): section heads. The drenched Join head scales to 6rem at 115%.
- **Title** (700, 1.5 to 1.75rem, width 105%): card, trial, technique and member titles; home station titles run larger (`clamp(1.9rem, 3.4vw, 3rem)`).
- **Numeral** (Anybody 700 to 800, 1.1 to 1.75rem, nerve blue): years, dates, research line numbers, trial years, trial stats, initials.
- **Lede** (400, 1.1 to 1.3rem, muted): the paragraph that sits beside or under a page or section head, max 520 to 560px.
- **Body** (400, 1.0625rem, 1.6): running text, held to about 62ch in research and station copy.
- **Item title** (600, 1.2 to 1.35rem): paper titles, news titles, names. Bright text, link colour on hover.
- **Label** (600, 0.8rem, 0.12em tracking, uppercase): anatomy names on the home spine (Nucleus, Cell body, Axon, Junction, Fibre) and news categories. Article h3s switch to Schibsted 600 at 1.25rem.

### Named Rules
**The Wide Heavy Rule.** Anybody is only ever used heavy (700+) and stretched (105%+). It never sets running text, and Schibsted never sets a display head.

**The Label Beside Rule.** An uppercase label sits beside its anchor (next to the spine node, or with the date in a news row), never stacked above a heading.

## Layout

One centred column: max width 1440px, horizontal gutter `clamp(20px, 6.6vw, 96px)`, applied identically to navbar, sections and footer so all left edges align. Section rhythm is `clamp(64px, 8vw, 120px)` on inner pages and `clamp(88px, 10vw, 150px)` between home sections; the home Join field sits further off at `clamp(96px, 11vw, 160px)`.

Inner pages open with a split page head: a huge title left, a muted lede right, bottom-aligned, wrapping on narrow screens. Content then runs as ruled rows or asymmetric two-column grids: research topics at 440px / fluid with a 96px gap, trials at 200px year / fluid, papers at 140px year / fluid, news at 230px date / fluid. Card grids use three columns at 48px gaps or two at 32px; the team uses four columns (three below 1100px, two below 800px) of 4:5 portraits.

The home page replaces the card grid with a station list: a 220px mark column holding the spine and anatomy label, and a 7:5 text-and-paper body. Below 900px the mark column shrinks to 56px, the spine moves to 14px, and labels turn vertical down the axon.

Breakpoints are content-led: 480, 600, 700, 800, 900, 1100, 1200 (navbar collapses below), 1400 (navbar tightens between 1200 and 1399). Most two-column structures collapse to one at 900px.

Every page ends with a page-chain link ("Keep scrolling to...") right-aligned on a hairline, followed by the footer (institution logos, address, PI, privacy link).

## Elevation & Depth

Flat. Depth comes from tone (ground to panel), from hairlines, and from the anatomy drawn on top of the ground. There are no ambient drop shadows anywhere in the system. The only `box-shadow` uses are rings: a 1.5px inset muscle ring that marks the trial the lab coordinates, an inset ground ring inside the lit nucleus node, and a soft 7px nerve halo around a lit axon node.

### Shadow Vocabulary
- **Lead ring** (`box-shadow: inset 0 0 0 1.5px #78D3A6`): the one trial card the lab coordinates.
- **Node halo** (`box-shadow: 0 0 0 7px rgba(109, 185, 234, 0.18)`): a lit node of Ranvier on the home spine.

### Named Rules
**The Tone Not Shadow Rule.** To lift something, move it from ground to panel teal; to separate things, draw a 1px hairline. Never float a surface with a blurred shadow.

## Shapes

Controls are pills (999px): buttons, the navbar Contact link, the navbar toggler, contact tabs and their track, language switches, news category chips. Objects get soft large corners: 24px for panels and the map, 20px for trial cards and portraits, 14px for small tiles (station paper links, home faces), 12px for form fields. Circles are reserved for anatomy (nodes, boutons) and member avatars. Strokes are 1px for dividers and 1.5px for interactive outlines.

The striation texture (2px muscle-green stripes at 10% opacity every 13px, on panel teal) is the system's one fill pattern; it stands in for missing photographs and initials-only portraits.

## Components

### Buttons
Confident, round, tactile.
- **Shape:** full pill, 52px minimum height, 0 28px padding, Schibsted 600 at 1.05rem, 1.5px border.
- **Primary (muscle):** muscle green with ground text; hover to pale muscle. The default call to action across the site.
- **Ghost:** transparent with an edge outline and bright text; hover brightens the outline to text colour. Always paired after a primary.
- **Ink:** ground fill with bright text, used only on the muscle-green field; hover to panel teal.
- **Press:** every button scales to 0.97 on `:active` over 160ms with the ease-out curve.
- **Focus:** 2px muscle outline at 3px offset site-wide; ground outline on the green field.

### Arrow link
Semibold bright text followed by a 22px x 2px muscle-green bar that grows to 36px on hover (200ms ease-out). Used for "Meet the team", "All publications", "All news".

### Ruled rows (papers, news, techniques, collaborators)
- **Divider:** 1px hairline above each row, closing hairline below the last.
- **Lead column:** an Anybody 700 date, year or number in nerve blue.
- **Content:** bright item title, muted meta line; lab members' names in author lists are muscle green.
- **Hover:** title shifts to link blue; nothing else moves.

### Cards / Containers
- **Default card:** not a box. A 1px hairline on top, 28px above the content, title in Anybody 700.
- **Trial card:** panel teal, 20px radius, 28px x 30px padding; a muscle uppercase tag, an Anybody title, a hairline then stats with Anybody numerals. The coordinated trial carries the lead ring.
- **Station paper:** 1px hairline outline, 14px radius, 16px x 20px; title bright, journal and year muted. Hover turns the outline nerve blue and tints the fill panel teal.

### Inputs / Fields
- **Style:** panel teal fill, 1.5px edge border, 12px radius, 52px minimum height (160px for text areas), bright text, placeholder colour for hints; labels in Schibsted 600 above.
- **Focus:** border turns nerve blue, plus the global muscle focus ring.
- **Checkbox:** 22px, muscle green when checked.

### Tabs (contact)
A pill track with a 1.5px hairline border and 6px inset holding pill tabs (52px tall, nav-text, 600). The active tab fills nerve blue with ground text.

### Navigation
- **Bar:** ground background, no border, no shadow, 88px tall (72px collapsed), gutter-aligned. Mark plus wordmark in Anybody 800 at 125% stretch.
- **Links:** nav-text at 1rem; hover to bright text; active is muscle green with a 2px underline 8px below.
- **Contact:** a nerve-blue outlined pill; filled nerve blue when active.
- **Mobile:** below 1200px a 44px circular toggler; links stack.

### Page chain
A right-aligned link on a hairline with a 44px circular muscle-outline button carrying a down arrow. Scrolling past the page end fills a conic muscle sweep inside the ring and moves to the next page at the threshold. "Back to the start" variants rotate the arrow up.

### Motor-unit spine (home signature)
The research lines are an ordered list of stations along one motor unit. Each station draws its own spine segment and the material changes along it: a soma-teal cell body with a translucent nerve outline (nucleus node, then cell-body node), an axon of a 3px nerve line inside 34px myelin dashes broken by a node of Ranvier, a five-bouton endplate, then a striated muscle-green fibre that runs to the end. Each segment reveals with `clip-path` as it crosses 62% of the viewport; its node lights (fills nerve blue, or the endplate boutons scale 1.15) when the station arrives. Under reduced motion every station is drawn and lit.

### Motor-unit illustration
The hero art: one myelinated axon branching onto four of six horizontal striated fibres, with endplate halos; inactive fibres sit at roughly half the opacity of active ones. An action potential (a short pale-blue dash) travels the axon and branches on a 4.2s loop, and disappears under reduced motion.

### Join field (home)
A full-bleed muscle-green band: a 6rem Anybody head in ground on one side, a field-ink paragraph and an ink button on the other. Text selection inverts to ground with muscle text.

### Team portraits
4:5 frames at 20px radius on panel teal; name in bright 600, role in muscle, focus in muted. Members without a photo get the striated frame with large muscle initials. The home faces strip shows the same photos smaller (14px radius) in greyscale.

## Do's and Don'ts

### Do:
- **Do** keep nerve blue for the neuron side and indexing data, and muscle green for the fibre side, actions and people (The Two Sides Rule).
- **Do** list real items as hairline-ruled rows with a nerve-blue Anybody date or number in the lead column.
- **Do** use a full pill (999px) at 52px height for every button and switch, with the 0.97 press scale.
- **Do** lift with panel teal and separate with a 1px hairline (The Tone Not Shadow Rule).
- **Do** set every display head in Anybody 700 to 800 at 105% stretch or wider, with negative tracking.
- **Do** end every page with a "Keep scrolling to..." page-chain link.
- **Do** resolve every animation to its final, fully drawn state under `prefers-reduced-motion`.
- **Do** use the striated panel as the stand-in for any missing photograph.

### Don't:
- **Don't** add a light theme or a white surface; the ground is always deep teal.
- **Don't** use blurred drop shadows; the only shadows are inset rings and the node halo.
- **Don't** fill more than one full-bleed area with muscle green on a page.
- **Don't** put a muscle-green button on the muscle-green field; use the ink button there.
- **Don't** stack an uppercase label above a heading; labels sit beside their node or with the date.
- **Don't** set running text in Anybody or headlines in Schibsted Grotesk.
- **Don't** add icon glyphs or decorative illustration outside the anatomy kit (axon, myelin, node, endplate, striation).
- **Don't** load fonts or assets from third-party hosts; fonts are self-hosted.
