# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary: researchers and recruits — scientists, clinician-scientists, collaborators, students, residents and postdocs who want to judge the lab's science and decide whether to work with or join it. When needs conflict, the site serves them first (home page leads with the science).

Secondary, each with a dedicated page: people with ALS, SBMA and other motor neuron diseases and their families (clinic access, trials; English and Italian), and trial sponsors/CROs (trial track record, facilities).

## Product Purpose

The public website of the NeuroMuscle Lab, Department of Neuroscience, Università degli Studi di Padova, linked to the Motor Neuron Disease Centre (Centro Malattie del Motoneurone) of Azienda Ospedale Università Padova. It shows what the lab studies, who is in it, what it publishes, which trials it runs, and how to get in touch or apply. Success: a visiting researcher understands the lab's research lines and people within a minute, and a prospective student or postdoc finds how to apply.

## Positioning

A clinical-and-bench group that follows motor neuron disease along the whole motor unit, from the motor neuron to the muscle fibre: long-term clinical cohorts and trials in ALS and SBMA (coordinating centre of the clenbuterol SBMA trial), muscle and neuromuscular-junction pathology, fluid and imaging biomarkers, TDP-43 cryptic splicing (with UCL Queen Square), and population genetics of repeat expansions.

## Operating Context

- Quarto static site in the `lab-website` repo, rendered to `docs/` and served by GitHub Pages; target domain neuromusclelab.org.
- Publications feed generated weekly from PubMed by `scripts/update_publications.py` (GitHub Action), also triggerable from the Lab Agent.
- Contact/"Work with us" form posts to Formspree (`xvkavpqz`); privacy policy follows iubenda structure, data controller Prof. Gianni Sorarù.
- Content is edited by lab members in plain `.qmd`/JSON files, so structures must stay simple to maintain.

## Capabilities and Constraints

- Pages: home, research, lab, trials, team, publications, news (+ posts, RSS), patients (EN) / pazienti (IT), contact, privacy.
- Principal investigator and contact: Prof. Gianni Sorarù. Prof. Elena Pegoraro (Head of Neuromuscular Laboratory) sits next to him in the team's top row and in the publications feed.
- Planned content blocks the user will supply (never fabricate): techniques & methods (Claude may draft from the lab's papers for the user to check), funders & partners, collaborators & alumni, open positions.
- No search; no CMS; no tracking beyond what the privacy policy covers.

## Brand Commitments

- Name: "NeuroMuscle Lab" (capital M).
- Tagline: "From motor neuron to muscle fibre."
- Mark and motor-unit illustration (axon branching onto striated fibres) in `images/mark.svg` and the home hero.
- University of Padova and Azienda Ospedale Università Padova logos in the footer.
- Reference: symmune.org (sister lab site) for overall feel — full-bleed hero, page chaining with "Keep scrolling to…" links, "Get in touch" with Information / Work with us tabs. Reference for content types: frattalab.org.

## Evidence on Hand

- Team photos for 11 of 14 members (`images/team/`); none for Pegoraro, Vianello, Marcato.
- Real trials list 2022–2026 and trial facilities (Drive doc "TRICALS / WEBSITE").
- Real publications (PubMed), four news posts, conference "Skeletal Muscle in ALS" (25–26 Sept 2026).
- No lab photographs; no funder list, collaborator list, alumni list or open positions yet (user will supply).

## Product Principles

1. Science first: lead with what the lab discovers and how, backed by real papers.
2. Truthful by construction: every person, trial, paper, funder and claim is real and sourced; empty is better than invented.
3. Easy for the lab to keep current: content lives in plain files; automation (PubMed feed) over manual lists.
4. Patients get a calm, plain-language path that never mixes with recruitment or sponsor messaging.

## Accessibility & Inclusion

Bilingual patient information (English/Italian). Visitors include people with motor disability: keyboard-operable, large hit targets, reduced-motion respected, good contrast on the dark theme.
