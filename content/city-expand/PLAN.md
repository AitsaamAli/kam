# City pages programme (owner request, 22 Nov 2026)

653 `blogs/tax-consultant-*` pages have under 800 words of article text (median 458). Goal: take each to **1,000+ words of real, local content** (aim 1,250 where the facts support it), add a **Short answer** box, and lift them out of thin / duplicate / doorway territory **without any penalty or de-indexing**.

The pages are split into 10 parts in `batches.json`. Do **one part per session**, in order, and wait **7 days** between parts while watching Search Console.

## The parts

| Part | Pages | What | Method |
|---|---|---|---|
| 1 | 41 | 19 duplicate pairs (e.g. `dg-khan` / `dera-ghazi-khan`, `jhelum` / `jhelum-city`) and 3 odd pages | merge |
| 2 | 44 | Punjab towns A–K | expand |
| 3 | 46 | Punjab towns L–Z | expand |
| 4 | 45 | Sindh and Balochistan towns | expand |
| 5 | 29 | KP, Gilgit-Baltistan and AJK towns | expand |
| 6 | 67 | Islamabad sectors and Rawalpindi areas | area (pilot 10 first) |
| 7 | 99 | Karachi, Faisalabad, Peshawar, Multan, Quetta, Hyderabad areas | area |
| 8–10 | 95 / 95 / 93 | Lahore areas | area |

Towns first because each town has its own official facts (district, FBR office, provincial authority). Neighbourhood ("area") pages last, because most share one city's facts and are the main doorway risk.

## Methods

**merge (part 1).** The pairs target the same place twice, which is duplicate content in itself. Keep the main URL (the shorter slug), move any unique facts into it, expand it as for "expand", and 301 the second URL to it in `vercel.json`. A 301 keeps the link value and is not a penalty. **Needs the owner's OK for each pair** (the owner said no de-indexing; a 301 replaces one URL with another rather than removing the place).

**expand (parts 2–5).** Add, per town, only facts from official sources, each linked with the date checked:
- District and province, and the provincial sales tax authority (PRA, SRB, KPRA, BRA; AJK and GB have their own regimes): provincial authority sites.
- Which FBR Regional Tax Office / IR zone covers the town: FBR jurisdiction notifications.
- Which FBR DNFBP directorate covers it: S.R.O. 1497(I)/2026.
- Population: Pakistan Bureau of Statistics, Census 2023 district tables.
- Where property transfers are registered and who collects property tax (district registrar, provincial Excise, cantonment board where relevant): provincial sites.
- The existing local economy text stays; rewrite it only to correct it.
Then: Short answer box at the top (local, one paragraph), a "How we help from Lahore" service section (published fees only), 4–6 local FAQs, Related links to the district/province hub.

**area (parts 6–10).** Neighbourhoods inside one city share most facts, so 1,000 words each must come from what is genuinely different about the area:
- The body that runs it (DHA, Bahria, CDA sector, cantonment board, LDA/KDA scheme, housing society), with its official site.
- Who registers property transfers there (society transfer office or sub-registrar), so who collects 236C/236K (s.236C/236K Explanation).
- Who collects property tax (cantonment board vs provincial Excise).
- Commercial zone or market rules that change which registrations apply (PRA/SRB for services, DNFBP for property dealers).
- City-wide facts appear once in a short linked paragraph, not repeated.
**Pilot first:** do 10 pages of part 6, run the overlap check, and only continue if every page is under 15% overlap with all other city pages. A page that cannot reach 1,000 words of real content is **not padded**. It goes on a list for the owner: keep as is, or merge into the city hub with a 301.

## Penalty-safety rules (every part)

1. Do not change URL, title, H1, canonical or robots tags (CLAUDE.md standing rule). Only the body, the Short answer box and FAQs change.
2. Every new fact has an official source link and a "checked" date. No market prices, no unverifiable claims, no review numbers, never "24/7".
3. No padding, no spun text, no city-name swapping. Each page must say something no other page says.
4. Overlap: run `python3 content/topic-fix/gate.py` (must end "680/680 clean") **and** an 8-gram check of the part against all city pages; every page under 15%.
5. Shared blocks (service section, how it works) stay short and are worded differently per province, so they do not dominate the overlap.
6. Update `dateModified` only on pages that really changed.
7. One part per deploy, 7 days apart. Ping IndexNow for the changed URLs after the deploy is live.
8. Before parts 6–10, get the Search Console export: pages with impressions are expanded first and most carefully; zero-impression pages are the merge candidates the owner decides on.
9. Stop and report if Search Console shows a drop in impressions for the changed pages after a part.

## Ready-to-paste prompt for each session

> Read `content/city-expand/PLAN.md` and do **part N** from `content/city-expand/batches.json`. Follow the method for that part and the penalty-safety rules. Facts only from official sources with links and dates. Show me the overlap and word counts before the PR, then follow the PR flow.

## Progress

| Part | Status | PR | Date |
|---|---|---|---|
| 1 | not started | | |
| 2 | not started | | |
| 3 | not started | | |
| 4 | not started | | |
| 5 | not started | | |
| 6 | not started | | |
| 7 | not started | | |
| 8 | not started | | |
| 9 | not started | | |
| 10 | not started | | |
