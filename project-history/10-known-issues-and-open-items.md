# Known Issues & Open Items

These are things that have been found and flagged but **not yet resolved** — a future session should know about them rather than rediscover them, and should ask the user before acting rather than assuming a decision.

## 1. Spain/Greece/Portugal pillar pages have real content overlap (unresolved)
`spain-visa-fbr-tax-return-pakistan-2026.html`, `greece-visa-fbr-tax-return-pakistan-2026.html`, `portugal-visa-fbr-tax-return-pakistan-2026.html` overlap with each other well above the 15% uniqueness threshold used everywhere else on this project:
- Spain vs Greece: **36.0%**
- Greece vs Portugal: **25.9%**
- Spain vs Portugal: **17.5%**

**Flagged to the user during the UK/Australia cluster work, no decision or action taken yet.** If picking up Tier 3 country work (Italy/Spain/Greece/Portugal — see `06-content-strategy-projects.md`), this should probably be fixed as part of that work rather than adding more content on top of already-overlapping pages. Confirm with the user before rewriting these three, since they're existing live pages (see the "don't touch existing blogs without being asked" rule in `11-working-norms-and-user-preferences.md` — but this is exactly the kind of case where flagging and asking is the right move, since it's a real known defect, not an unprompted edit).

## 2. GSC "Not found (404)" / "Page with redirect" counts — may still show stale numbers in Search Console
The root cause (a 6-week-stale cached `sitemap.xml`) was found and fixed 2026-08-19 (see `04-seo-technical-history.md` Wave 5), and the live sitemap was verified to match the repo's actual URL count immediately after the fix. However, **Google Search Console itself can take days-to-weeks to re-crawl and reflect this in its Coverage report** — if a future session is shown a GSC screenshot still showing high "Not indexed" numbers, don't assume the fix didn't work; re-verify the *live site* state first (`curl` the sitemap, check headers, diff URL counts) before concluding there's a new problem. The GSC "Validate Fix" button can be used to prompt faster re-crawl if genuinely needed.

## 3. ~798 near-duplicate city pages — deliberately not rewritten
`income-tax-filing-<city>.html` (×90) and `ntn-registration-<city>.html` (×122) are thin (400-799 words) but were explicitly excluded from the rewrite queue because mechanically padding hundreds of city-name-swapped pages risks Google's "scaled content abuse" policy (see `04-seo-technical-history.md`). This is a **deliberate deferral, not an oversight** — if ever revisited, it needs a genuinely differentiated angle per city (real local content: local FBR RTO office details, local business sector context, etc.), not a template fill. Don't batch-process these without a real content plan.

## 4. Color contrast (WCAG AA failures) — needs a user design decision
~200+ files have footer text and sidebar teal labels below WCAG AA's 4.5:1 contrast ratio. Fixing means changing colors that are part of the established brand palette used everywhere (buttons/links/icons) — this is a real brand/visual decision, not a mechanical fix. Flagged in the 2026-08-07 claude-seo audit, still open. Ask the user before touching brand colors for this reason.

## 5. CLS (layout shift) — systemic, needs real engineering work
The worst-sampled page scored 0.256 (Google's "Poor" range), caused by the shared async Google Fonts loading pattern present on every single page (`font-display:swap` reflowing content when the web font replaces the fallback). Proper fix is metric-matched fallback `@font-face` overrides or `font-display:optional` (with its own tradeoffs) — real engineering work across the shared font-loading snippet, not a one-line change. Not started.

## 6. Meta descriptions >165 characters (419 files, low priority)
Not broken (nothing is truncated/cut off), just suboptimal length for Google's ~155-160 char display cutoff. Fixing properly means a genuinely shorter, compelling rewrite per file (not blind truncation, which would recreate the exact truncation bug fixed elsewhere — see `04-seo-technical-history.md` Wave 2). Needs its own project if the user wants it prioritized; not started.

## 7. Commercial/local-intent 100-topic plan — 74/100 topics remaining
See `06-content-strategy-projects.md` Project B. Sections C-K not started. This is an *in-progress* project, not a bug, but worth listing here as the single largest known "unfinished work" item on the site.

## 8. Country-cluster expansion — 4+ countries still pending
Germany (next recommended pick) and Italy, then USA/Ireland at lower priority. See `06-content-strategy-projects.md` Project C for the full ranking and reasoning. Canada is deliberately de-prioritized (collapsed approval rate).

## 9. Phase 2.5 of the original "Master Prompt" optimization — never completed
Per `OPTIMIZATION-REPORT.md`: duplicate-content similarity clustering, further thin-content deepening, and a formal keyword-cannibalization map were flagged as "Phase 2.5 remaining" back in 2026-06-26 and never explicitly revisited as a named phase (though much of its practical intent has been achieved piecemeal through the later rewrite/uniqueness-check work). Not urgent, but if a formal cannibalization audit is ever requested, this is the origin of that ask.

## 10. No live keyword-volume/SEO-data tool has been used yet
All topic/keyword decisions to date have been made via competitor-pattern-matching and manual research (see `07-competitor-landscape-and-keyword-research.md`), not real search-volume data. If DataForSEO, Google Search Console API access, or similar becomes available in a session, it would meaningfully improve prioritization — flagged as an opportunity, not a defect.
