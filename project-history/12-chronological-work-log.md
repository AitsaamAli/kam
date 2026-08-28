# Chronological Work Log

550+ commits since the initial commit. This groups them thematically by month for orientation — for full commit-level detail, run `git log --oneline` or `git log --grep="<keyword>"` in the repo. Commits-per-month at time of writing: May 124, June 191, July 51, August 185 (through 2026-08-27).

## 2026-05-19 — Initial commit
Site and blog system created (`dec5a116`), first SEO-optimized FBR Filer Guide blog added, initial layout/structure work.

## 2026-05 through mid-2026-06 — Foundation building
Service pages, homepage sections, pricing page, blog system scaffolding, initial batch of blog content. (124 commits in May, 191 in June — the bulk of the original site build-out.)

## 2026-06-26 — "Master Prompt v3/v4" full-site optimization (Wave 1)
5-phase mechanical + judgment SEO pass across 1,761 pages — titles, schema, AEO/GEO (llms.txt), 1,931 internal links, full verification. See `04-seo-technical-history.md` Wave 1 and root `OPTIMIZATION-REPORT.md`/`SITE-AUDIT-REPORT.md`/`CHANGELOG-seo.md`.

## 2026-07-15 — Overseas Pakistani FBR blog series (original 8 + 2 more July 23)
10 new visa/FBR hub-and-spoke blogs written (UK, Canada, Italy, Spain, Germany, Australia, non-resident 182-day rule, Section 8 clearance, pending returns, pillar) — see `05-blog-content-inventory-and-rewrite-method.md` and `06-content-strategy-projects.md`. Same day: 2 budget/tax-law blogs (Section 7E abolition, 236C/236K property transfer changes).

## 2026-07-23 — 10 more blogs, staggered release (then pushed immediately)
New batch (FBR new return form, WHT rate card, ATL status checker, SMC registration, rent reporting rules, IT export exemption, NPO/trust registration, benami transaction law, Greece + Portugal visa guides completing the abroad series). Originally scheduled via Windows Task Scheduler to go live one every 3 hours; user cancelled the stagger partway through and had everything pushed immediately.

## Late July / early August 2026 — Thin-blog rewrite marathon begins
Individual "fix: rewrite X to N words" / "fix: expand X with..." commits start appearing in volume — this is the long-running effort to bring the corpus from under-2000-word thin content up to standard. Continues in bursts across multiple sessions through mid-August. See `05-blog-content-inventory-and-rewrite-method.md` for the methodology and the recurring "generic filler" bug pattern discovered during this work.

## 2026-08-01 — Site-wide bug sweep + growth/internal-linking push (Waves 2 & 3)
Same-day: (a) a custom-script scan across 1,138 blogs found and fixed truncated titles/descriptions, broken JSON-LD, mojibake, mismatched FAQ schema (Wave 2); (b) llms.txt expansion + 5 new topic-cluster pillar pages built at site root, nav-dropdown internal linking extended to 1,263/1,279 pages (Wave 3). See `04-seo-technical-history.md`.

## 2026-08-06/07 — GSC deindexing investigation round 1 + claude-seo Lighthouse audit
Root cause found: 723 broken links from a `blogs.html` city-page href bug + 299 matching `vercel.json` redirect rules, fixed. `site-health-check.js` built. Separately, the claude-seo plugin installed and run — homepage-specific fixes (aria-labels, dead `javascript:void(0)` links, a JS TypeError), sitemap BOM stripped. Contrast and CLS issues found and flagged (still open). See `04-seo-technical-history.md` Waves 4 & 5.

## 2026-08-08/09 — Thin-blog rewrite marathon, heavy volume
Multiple full-day continuous sessions working through the priority tier (1300-1999 word files) — `rewrite-apply.js` built to mechanize the generic-template cases; dozens of files rewritten with careful per-cluster differentiation (crypto, overseas-Pakistani, IRIS-portal, consultant/location pages, etc.). See `05-blog-content-inventory-and-rewrite-method.md`.

## 2026-08-13 through 08-17 — Informational 100-topic competitor-gap project
Full competitor research (`content-gap-100-new-blog-topics.md`), then Sections A through N written and pushed across several days — **100/100 topics complete by 2026-08-17**. See `06-content-strategy-projects.md` Project A for the full section-by-section breakdown.

## 2026-08-19 — GSC deindexing round 2 + the real root cause found
Health-check re-run found it had crept back to 74 issues (new-batch relatedHref bug, stale footer links, a newly-discovered root-vs-`/blogs/`-path pattern) — fixed to 0. Separately, while verifying an external "technical SEO audit" a user shared, discovered the actual biggest root cause of the whole multi-week saga: a 6-week-stale cached `sitemap.xml` (Vercel edge cache, 24h Cache-Control never actually expiring due to a caching quirk). Fixed by shortening cache TTL + a manual Vercel redeploy; verified resolved. See `04-seo-technical-history.md` Wave 5 for the full blow-by-blow — this was the single most consequential fix on the project.

## 2026-08-19 (later same day) — Commercial/local-intent 100-topic plan started
New, distinct 100-topic plan (`commercial-local-100-blog-topics.md`) targeting commercial/local search intent rather than more informational content. Sections A (10 city pages) and B (16 service-consultant pages) completed same/next day = 26/100. See `06-content-strategy-projects.md` Project B.

## Mid-to-late August 2026 — Visual/design overhaul
Template-consistency audit found 5 distinct CSS template families (`02-site-architecture-and-templates.md`); dark-mode support removed sitewide per explicit user instruction (681 files); a sitewide CSS-specificity contrast bug fixed (1,420 files); logo/favicon inconsistencies fixed (raster→SVG, invisible-favicon-glyph bug); a "bold gold-foil premium" visual redesign designed via Artifact mockups, approved, then applied sitewide to CTA boxes/buttons (1,267 files across all 4 template families) and FAQ accordion icons (1,267 files). See `03-design-system-and-branding.md`.

## 2026-08-20 through 08-27 — Visa/overseas country-cluster expansion (most recent, active work)
User requested a full country-by-country visa/tax-document opportunity analysis before committing to any one country; a comparative "Visa Country Priority Report" was built and published (reasoning fully reproduced in `06-content-strategy-projects.md` Project C). UK selected as #1 priority: existing thin pillar page rewritten to 2000+ words (938→2128, later bug-fixed for an accidentally-duplicated section), then a 5-post cluster written (student/skilled-worker/business-investor/visitor/post-move-tax-status), each ~1900-2000 words, uniqueness-checked, wired in. Same pattern immediately repeated for Australia (#2 priority): pillar rewritten 929→1936 words, 5-post cluster written — with a real lesson learned mid-project that the first Australia draft copied too much UK-cluster phrasing (17-38% overlap), requiring a substantial rewrite pass before it passed the uniqueness threshold. **This history folder (`project-history/`) was created 2026-08-27** as the next step, per explicit user request, to preserve all of the above for continuity into future sessions.

## 2026-08-28 — Germany, Italy, USA visa clusters (content drafted externally, verified and published here)
User provided three zip files (`germany-cluster-content.zip`, `italy-cluster-content.zip`, `usa-cluster-content.zip`) containing pre-drafted content — `.js` data files matching this project's generator format, each package with a detailed README — produced by an external "Claude Cowork" session that had read this project-history folder and followed its documented process. Work done this session: extracted and read every file, independently re-verified word counts/tag-balance/JSON-LD (all matched the packages' own claims closely), ran the actual uniqueness-check script against the UK/Australia clusters and existing overseas-Pakistani sibling pages (all clean, well under 15%), built a parameterized `country-cluster-generator.js` (replacing the one-off UK/Australia/Germany-specific generators with a single reusable one taking `countryName`/`pillarSlug`), and published all three:
- **Germany**: pillar rewritten (919→2,595 words) + 4-post cluster (student/Blue Card/Opportunity Card/after-moving). Commit `87bff701`.
- **Italy**: pillar **re-platformed** onto the MINIFIED template (it had been on an older, different CSS family) and a real factual error fixed — the old pillar wrongly claimed FBR documents are required for Italy's Decreto Flussi work-visa route, which fresh research confirmed is false (that route is employer-sponsored with no proof-of-funds step at all) + 4-post cluster (quota news-hook, seasonal work/182-day rule, moving-to-Italy, remittance/property). Commit `e390b9d8`.
- **USA**: brand-new pillar (first USA coverage on the site) + full 5-post cluster (F-1, H-1B, EB-5, B1/B2, after-moving). Commit `a45268e1`.

**One real audit finding, not silently trusted:** the USA package's README claimed its uniqueness check had been run against a "Canada cluster" file that doesn't exist anywhere in the repo or any delivered zip — flagged as unverifiable in the commit message and in `13-remaining-countries-blog-titles.md`, rather than either accepting the claim or quietly deleting it. Everything independently checkable came back clean regardless.

Also folded in a companion competitor/keyword research document (`Kamboh_Associates_Keyword_Cluster_Strategy.md`, prepared 2026-08-19 by a separate Claude session, found in Downloads) into `07-competitor-landscape-and-keyword-research.md` — 18-query live SERP research identifying ranking competitors and keyword-cluster tiers distinct from the earlier informational-content-gap competitor list.

## What's actively next (as of 2026-08-28)
1. Fix the Spain/Greece/Portugal content-overlap issue (`10-known-issues-and-open-items.md` item #1) before any further Tier 3 work.
2. Canada full cluster, then Ireland (new pillar + cluster) — see `13-remaining-countries-blog-titles.md`.
3. Continue the commercial/local-intent 100-topic plan (Sections C-K, 74 topics remaining).
3. Whatever the user directs next — check `10-known-issues-and-open-items.md` for what's flagged-but-unresolved if no new direction is given.
