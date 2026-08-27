# Competitor Landscape & Keyword Research Method

## Known competitors (confirmed via live research across multiple sessions)

### General Pakistani tax-filing/FBR-consultant competitors
Found via live web search when researching the informational 100-topic content-gap plan:
- **Befiler** (befiler.com)
- **Pak Tax Services**
- **JZARR Filers**
- **TaxIt.pk**
- **TaxFlow.com.pk**
- **Difbr.pk**
- **Oscar.pk**
- **Switcher Techno**
- **Tenco Consulting**

### Visa/overseas-Pakistani-tax competitors specifically
Found via live SERP research when planning the UK visa-cluster content:
- **countrytaxcalc.com** — owns the "post-arrival" angle (DTA/PAYE/Skilled Worker tax mechanics after you've already moved). This is the specific gap the "Moving to [Country]" post in the country-cluster structure is designed to close — bring that same audience back to a Pakistani consultant instead of losing them to a UK-side generic tax site.
- **opaige.com**
- **swiftpassimmigration.com**
- **trips.pk**
- All four of these publish only **one generic, visa-type-agnostic post** per country (e.g. one "UK visa tax documents" post, not split by student/skilled-worker/business/visitor). That's the structural gap the 5-post country-cluster strategy exploits — see `06-content-strategy-projects.md`.

### General Pakistani business/finance press (used for sourcing new law changes, not as direct competitors)
Dawn, Profit/Pakistan Today, ProPakistani, VATupdate — checked for coverage of new Finance Act provisions (SEP tax, digital invoicing SROs, etc.) before those provisions had consultant-content written about them anywhere yet.

## How competitor research is actually done on this project (repeatable method)

This is the process used for the two major gap-analysis projects (`06-content-strategy-projects.md` Projects A and C) — reuse it for any future "what should we write next" question:

1. **Establish the local baseline first.** Extract all existing blog titles/topics from this site (`ls blogs/*.html` + read titles, or grep for `<title>`) so you know what's already covered and can immediately rule out cannibalization risk before proposing anything "new."
2. **Live-search the named competitors above** for their blog/content sections — look specifically at (a) what topics they've built into full content hubs (multiple linked posts, not just one), (b) what they call "the most important" or lead with prominently, and (c) what visa-type/service-type splits they use vs. one generic catch-all post.
3. **Live-search general business press** for recent regulatory changes (new SROs, Finance Act provisions, new bilateral agreements) that are too new for competitors to have written about yet — this is where genuine first-mover content opportunities come from (e.g. the FBR digital-invoicing rollout, the SEP/Section 6A digital-economy tax law, and the Italy bilateral labor-migration MOU were all found this way).
4. **Score each candidate topic** on: (a) genuine current search/user demand, (b) thin-to-zero competitor coverage OR zero coverage on this site specifically, (c) a real, non-generic angle achievable without fabricating figures, (d) natural fit for FAQ/TL;DR/AEO-citable structure.
5. **For visa/country content specifically**, also pull real migration-volume and visa-approval-rate data (student visa counts, approval-rate trends) to rank countries/topics by actual opportunity size, not just gut feel — see the Tier 1/2/3 country ranking table in `06-content-strategy-projects.md` for the exact method and sourcing (ApplyBoard student mobility analysis, British Council/UKVI data, BEOE overseas-worker statistics, Gulf News UAE employment reporting, MOFA Pakistan press releases).

## "How do we take a lead from them" — the actual playbook used

This project's competitive strategy is **not** "copy what they rank for" — it's specifically finding what they *haven't* built yet and building it first, or building a *more segmented/deeper* version of what they have:

- **If a competitor has one generic post on a topic** → split it into a segmented cluster (the country-cluster 5-post pattern: by visa type/persona rather than one catch-all).
- **If a competitor has zero coverage of a real, searched topic** → write it first (the gig-economy, digital-invoicing, and SEP-tax content gaps were all "nobody has this yet" findings).
- **If a competitor has built a full content hub around something** → treat that as strong evidence of real demand, and make sure this site has at least equal-depth coverage, differentiated by this firm's actual services and real numbers (never copy their numbers — verify independently).
- **Never fabricate a statistic to look more authoritative than a competitor** — the content-integrity rule (see `09-verified-facts-and-figures.md` and `11-working-norms-and-user-preferences.md`) applies here specifically: hedge explicitly where sourcing is thin rather than inventing a precise-sounding number, even if a competitor's page presents one confidently.

## Keyword research approach in practice
This project has not run a dedicated keyword-volume tool (no DataForSEO/Ahrefs data captured in this history) — keyword decisions have been made by:
- Direct topic-title matching to how competitors and search behavior phrase things (e.g. "UK Visa Ke Liye Pakistan FBR Tax Return", matching the actual bilingual Roman-Urdu/English search pattern this audience uses).
- Following what competitors have already validated by ranking/building hubs for.
- City/service-name combinatorics for local-intent commercial pages (Project B in `06-content-strategy-projects.md`) — "Best Tax Consultant in [City]", "[Service] Consultant [City]".
- If DataForSEO or another live keyword-data source is available in a future session (check for `mcp__dataforseo__*` tools or the `seo-dataforseo`/`seo-google` skills), prefer real volume/difficulty data over title-pattern guessing — this hasn't been done yet on this project and would meaningfully improve topic prioritization.

## Where to look for the source deliverables
- `content-gap-100-new-blog-topics.md` (project root) — the full informational-topic competitor research writeup.
- `commercial-local-100-blog-topics.md` (project root) — the commercial/local-intent plan.
- The "Visa Country Priority Report" reasoning is reproduced in full in `06-content-strategy-projects.md` since the original was a Claude Artifact that may not remain accessible to a future session.
