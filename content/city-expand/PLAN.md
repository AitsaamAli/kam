# City pages programme (owner request, 22 Nov 2026)

653 `blogs/tax-consultant-*` pages have under 800 words of article text (median 458). Goal (owner, 22 Nov 2026; the 1,000-word rule is dropped): give every page **4-5 official local facts**, a **Short answer** box and **unique content**, link it to its district/province hub, and lift it out of thin / duplicate / doorway territory **without any penalty, de-indexing or traffic drop**. Quality must be out-class; word count follows the facts, never padding.

The pages are split into 13 parts (11–13 added from the A7 audit) in `batches.json`. Do **one part per session**, in order, and wait **7 days** between parts while watching Search Console.

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
| 8–10 | 96 / 95 / 93 | Lahore areas | area |
| 11 | 90 | `income-tax-filing-<city>` (return-filing intent) | expand-intent |
| 12–13 | 59 / 58 | `ntn-registration-<area>` (registration intent) | expand-intent |

Towns first because each town has its own official facts (district, FBR office, provincial authority). Neighbourhood ("area") pages last, because most share one city's facts and are the main doorway risk.

## Methods

**merge (part 1).** The pairs target the same place twice, which is duplicate content in itself. Keep the main URL (the shorter slug), move any unique facts into it, expand it as for "expand", and 301 the second URL to it in `vercel.json`. A 301 keeps the link value and is not a penalty. **Needs the owner's OK for each pair** (the owner said no de-indexing; a 301 replaces one URL with another rather than removing the place).

**expand (parts 2–5).** Add, per town, 4-5 facts from official sources, each linked with the date checked:
- District and province, and the provincial sales tax authority (PRA, SRB, KPRA, BRA; AJK and GB have their own regimes): provincial authority sites.
- Which FBR Regional Tax Office / IR zone covers the town: FBR jurisdiction notifications.
- Which FBR DNFBP directorate covers it: S.R.O. 1497(I)/2026.
- Population: Pakistan Bureau of Statistics, Census 2023 district tables.
- Where property transfers are registered and who collects property tax (district registrar, provincial Excise, cantonment board where relevant): provincial sites.
- The existing local economy text stays; rewrite it only to correct it.
Then: Short answer box at the top (local, one paragraph), a "How we help from Lahore" service section (published fees only), 4–6 local FAQs, Related links to the district/province hub.

**area (parts 6–10).** Neighbourhoods inside one city share most facts, so the 4-5 facts must come from what is genuinely different about the area:
- The body that runs it (DHA, Bahria, CDA sector, cantonment board, LDA/KDA scheme, housing society), with its official site.
- Who registers property transfers there (society transfer office or sub-registrar), so who collects 236C/236K (s.236C/236K Explanation).
- Who collects property tax (cantonment board vs provincial Excise).
- Commercial zone or market rules that change which registrations apply (PRA/SRB for services, DNFBP for property dealers).
- City-wide facts appear once in a short linked paragraph, not repeated.
**Pilot first:** do 10 pages of part 6, run the overlap check, and only continue if every page is under 15% overlap with all other city pages. A page that cannot get 4 genuinely local facts is **not padded**. It goes on a list for the owner: keep as is, or merge into the city hub with a 301.

## Already done for all parts
- Hub links: every city page links to its city hub (areas) or province guide / division city (towns), and hubs list their pages (`hubs.py`, idempotent; run it after any new city page).
- Firm experience block on every guide (`content/ui-2026/experience.py`).

**expand-intent (parts 11–13).** These cities also have a `tax-consultant-` page, so each family must keep its own job and not compete: `income-tax-filing-` pages answer *how and where a return is filed for that place* (FBR RTO/zone, due date, local withholding situations), `ntn-registration-` pages answer *how to get an NTN there* (IRIS steps, documents, local cases). Add 4-5 official facts for that intent, a Short answer, and sideways links between the city's three pages (consultant ↔ filing ↔ NTN). Never repeat the consultant page's text.

## Lesson from part 2
Long shared sentences across 47 similar pages pushed the gate to 635/680 (32-38% overlap). What passes: a compact facts table where every cell carries the town's own name or numbers, short prose built around unique numbers, and FAQs that name the town. Reuse `part2.py` as the template for parts 3-5.

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
| 1 | done: 19 pairs 301-merged (`part1_merge.py`); hub links on 626 pages (`hubs.py`) | see git log | 22 Nov 2026 |
| 2 | done: 47 Punjab towns (`part2.py`, census data in `census_punjab_2023.json`); 2 more duplicates merged | see git log | 22 Nov 2026 |
| 3 | done: 45 Punjab towns (`part3.py`) | see git log | 22 Nov 2026 |
| 4 | done: Sindh + Balochistan towns, Sadiqabad (`part45.py`) | see git log | 22 Nov 2026 |
| 5 | done: KP towns (`part45.py`); 7 AJK + 4 GB pages wait for official data | see git log | 22 Nov 2026 |
| 6 | not started | | |
| 7 | not started | | |
| 8–10 | first pass: 47 Lahore areas with verified group facts (`lahore.py`: DHA, Walled City gates, PIEDMC estates, census tehsils, housing societies); 237 left (LDA schemes, cantonment-only, roads/markets, 87 block/sector and 11 'near' pages) for owner sources/decision | see git log | 22 Nov 2026 |
| 9 | not started | | |
| 10 | not started | | |
| 11 | not started | | |
| 12 | not started | | |
| 13 | not started | | |
