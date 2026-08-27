# SEO Technical History

Chronological summary of every major technical-SEO wave. See `12-chronological-work-log.md` for dates.

## Wave 1 — "Master Prompt v3/v4" full-site optimization (2026-06-26)
A 5-phase mechanical + judgment optimization pass across then-1,761 pages. Full detail in root `OPTIMIZATION-REPORT.md` and `SITE-AUDIT-REPORT.md`. Summary:
- Phase 0: audit (`seo-audit.csv`, `progress.json`)
- Phase 1: titles ≤60 chars, `BlogPosting` + `FAQPage` JSON-LD injected on all pages, canonicals verified
- Phase 2: 31 priority (GSC-indexed) pages got hand-tuned keyword-first titles, real 4-Q FAQs, TL;DR boxes
- Phase 3 (AEO/GEO): `llms.txt`/`llms-full.txt` written, `robots.txt` AI-crawler allowlist verified, `dateModified` updated
- Phase 4: 1,931 contextual internal links added across 1,234 pages, keyword→URL map, orphan fixes
- Phase 5: re-audit, 0 violations across 8 invariants
- **Note:** an older memory record claimed Phases 3-5 were still "pending" — that's stale/wrong. `CHANGELOG-seo.md` confirms all 5 phases completed and committed. Trust the changelog over any single memory snapshot.

## Wave 2 — site-wide bug sweep (2026-08-01)
Custom script scan across then-1,138 blog files, beyond what the earlier invariant-checker could catch:
- 92 files: truncated `<title>` tags ending in "…" — fixed from each page's own og:title/H1/BlogPosting headline
- 29 instances: truncated OG/Twitter description/title tags, 19 with the truncation baked into the meta description itself
- 1 file: broken JSON-LD (trailing comma) — zero structured data was being read from this page
- 1 file: a future-dated (2027) date in 3 places
- 3 files: mojibake-corrupted UTF-8 (â€"/â€¦/â€™ literal chars replacing em-dash/ellipsis/apostrophe)
- 178 files: standalone `FAQPage` JSON-LD containing generic boilerplate Q&A completely unrelated to the page topic — regenerated from each page's real visible FAQ
- **Still open (deliberately deferred):** 419 files have a meta description >165 chars — not broken, just suboptimal length; needs a real per-file rewrite project if ever prioritized.

## Wave 3 — growth/internal-linking push (2026-08-01, same day)
- Expanded `llms.txt` (Free Tools section, 6 more verified guides, STRN as its own line, sitemap pointer)
- Built 5 new topic-cluster **pillar pages at site root** (not `/blogs/`): `/income-tax-filing-guide-pakistan`, `/sales-tax-guide-pakistan`, `/property-tax-guide-pakistan`, `/fbr-notice-guide-pakistan`, `/freelancer-overseas-tax-guide-pakistan` — each 500-760 words of real synthesis + full schema, linking to 12-18 existing deep-dive guides.
- Replaced the generic repeated `/blogs` nav-dropdown link with real links to all 5 pillars, across every template variant found (4 distinct variants needed separate handling). **Final state: 1,263 of 1,279 pages link to all 5 pillars** (the 16 exceptions are legal pages + a handful of minimal local-SEO pages with no dropdown mechanism at all).
- **To add a 6th pillar later:** replicate the existing 5 pages' structure, then search any blog for the string `income-tax-filing-guide-pakistan` to find the repeated 5-link dropdown block and extend it, propagating the same string-replace across `blogs/*.html` and root `*.html`.

## Wave 4 — claude-seo plugin audit / Lighthouse (2026-08-07)
Installed the `claude-seo` Claude Code plugin, ran real Lighthouse against 32 sampled pages (avg: performance 91.7, accessibility 88.8, best-practices 99.9, SEO 99.2). Fixed:
- Homepage's specific SEO/best-practices issues: non-descriptive "Learn More" links (added `aria-label`), 5 `href="javascript:void(0)"` footer tool links (repointed to real calculator/checker pages), a recurring JS `TypeError` in dead dashboard-animation code.
- `sitemap.xml` had a UTF-8 BOM before the XML declaration — stripped (Google tolerated it, but strict validators didn't).
- 19 pages missing `aria-label` on the mobile hamburger button.

**Open, needs a design decision (not auto-fixed):**
1. Color-contrast failures on ~200+ files — footer text and sidebar teal labels compute below WCAG AA 4.5:1. Fixing means darkening backgrounds or changing colors that are part of the established brand palette (used in buttons/links/icons everywhere) — a real brand decision, flagged for the user.
2. CLS (layout shift) in Google's "Poor" range on the worst-sampled page (0.256) — systemic, caused by the async Google Fonts loading pattern (`font-display:swap` reflowing when the web font replaces the fallback). Real fix needs metric-matched fallback `@font-face` overrides or `font-display:optional` — not a one-line change.

**Tooling insight:** the plugin's per-file `content_quality.py` filler/repetition scorer only sees *within-document* quality — it can't detect *cross-page* near-duplicate boilerplate reused across dozens of files (which the manual sweeps above were specifically catching). A clean automated score does not mean no cross-page duplication problem.

## Wave 5 — GSC "Not indexed" deindexing investigation (2026-08-06 through 08-19, multi-round)
This was the single biggest technical-SEO saga on the project. Full blow-by-blow in the (now-consolidated-here) memory record; key findings, in the order they were discovered:

1. **Round 1 (632 "Not indexed" of ~1,842, 453 of them 404s):** root cause was `blogs.html`'s ~390 "Best Tax Consultant in `<city>`" entries all hardcoded to a wrong, non-existent URL pattern (`/income-tax-filing-<city>.html`) instead of the real `/blogs/income-tax-filing-<city>` — 723 broken links, plus 299 `vercel.json` redirect rules pointing at the same wrong target. Fixed (commit `4992a383`). A reusable `site-health-check.js` tool was built here — see `08-production-pipeline-and-tools.md`.
2. **Follow-on same round:** 4 files with corrupted meta-description tags, 55 more truncated titles on **root-level** pages (the earlier title-truncation fix had only covered `blogs/*.html`), 12 more mojibake instances.
3. **Round 2 (2026-08-19, GSC still showing 443/102):** re-ran the health check, found it had crept back to 74 issues — a new batch of pages (`commercial-local-100-topics` Section A/B) had a `relatedHref` missing its `/blogs/` prefix; ~90 older pages had static footer links to slugs that were never actually created; **discovered a new pattern: 19 pages live at site root but were being linked with an incorrect `/blogs/` prefix sitewide** — always check a target file's own `<link rel="canonical">` before assuming its path. Fixed down to 0 local issues.
4. **Important caveat documented here:** GSC's Coverage export gives counts only, not URL lists — its 404 count doesn't map 1:1 to what a local link-scan finds (some may be external backlinks to genuinely-removed old URLs, or simply not-yet-recrawled). Be upfront about this gap rather than implying an exact match.
5. **The real, much bigger root cause (found 2026-08-19 while verifying an external "technical SEO audit" doc a user shared):** live `sitemap.xml` was frozen at ~2026-07-02 content (632 URLs) against the repo's actual 1,421 URLs at the time — a **~6-week-stale Vercel edge cache**, caused by `vercel.json`'s `Cache-Control: public, max-age=86400` (24h) on `sitemap.xml`/`robots.txt`. This plausibly explains the *entire* multi-week "not indexed" saga — if Google was reading a 6-week-old sitemap the whole time, none of the intervening content pushes would ever have been discovered via sitemap at all. **Fix:** shortened Cache-Control to `max-age=300, must-revalidate` (commit `b9744dea`), user did a manual Vercel dashboard redeploy unchecking "Use existing Build Cache" to force-purge. **Verified resolved** — live sitemap matched repo count exactly afterward.
6. **How to diagnose this class of problem again:** `curl -sI https://kambohassociates.com/sitemap.xml` and check `Age`/`X-Vercel-Cache`/`Last-Modified` headers, diff the live sitemap URL count against the local repo count. A single page deploying correctly does NOT prove long-cached static assets (sitemap, robots.txt) are fresh — check them independently. Also: when someone hands you an external "audit" document, verify its specific claims via direct `curl`/WebFetch of raw HTML rather than trusting it or a markdown-converting fetch tool (which can miss `<head>`-only content like JSON-LD) — one shared audit round had both correct and incorrect claims mixed together.

## Wave 6 — pillar rewrite bug caught and fixed (2026-08-25/27, most recent)
While rewriting the UK visa pillar page to 2000+ words, an editing pass accidentally left a duplicated section (`h2 id="docs"` documents-checklist block appeared twice, identical). Caught via a routine post-edit tag-balance check before the next task started, fixed in a follow-up commit. **Lesson reinforced: always re-verify tag balance (`div`, `table`, `ul`, `li`, `h2` open/close counts match) and re-read the diff mentally before considering a multi-edit rewrite finished** — this class of bug is easy to introduce with multiple sequential `Edit` calls on the same file and easy to catch with a simple automated count.

## Reference: how Google crawling/indexing/deindexing actually works (verified from Google Search Central docs + Search Engine Journal, compiled 2026-08-19)

**Three-stage pipeline:** Crawling → Indexing → Serving. Google explicitly states no guarantee of crawling/indexing/ranking even with perfect compliance.

**Deindexing causes, most-to-least likely for a site like this:**
1. Self-inflicted: `noindex` meta/header, robots.txt disallow, password protection
2. Server-side: 5xx errors, soft-404s (200 status but "not found" content), redirect chains/loops, 401/403, slow rendering
3. Duplicate/canonicalization: GSC shows "Duplicate without user-selected canonical" — not a penalty, just a canonical pick
4. "Crawled – currently not indexed" / "Discovered – currently not indexed": **not penalties** — a quality/duplication judgment call or crawl-pacing issue. Resubmitting doesn't help; the underlying cause must be fixed.
5. Manual actions (real penalties, visible in GSC's Manual Actions report): cloaking, doorway pages, hacked content, keyword stuffing, link spam, **"scaled content abuse"** (explicitly includes "using generative AI tools to generate many pages without adding value for users" — directly relevant given this project bulk-produces AI-written pages; the per-page uniqueness-check discipline in `08-production-pipeline-and-tools.md` exists specifically to stay clear of this policy), thin affiliate content, sneaky redirects.
6. Crawl budget exhaustion on large sites: duplicate/low-value URLs starve crawl budget from real pages.

**What helps indexing:** XML sitemaps, internal linking (orphan pages are hard to discover), fast server response + 304 caching, correct HTTP status codes, consolidating duplicate URLs, unique/valuable content, GSC URL Inspection → Request Indexing (single-page only).

**Myths debunked:** IndexNow is NOT supported by Google (Bing/Yandex only). The Indexing API is officially restricted to JobPosting/BroadcastEvent content only.

**Diagnostic order:** GSC Page Indexing report → URL Inspection tool → Manual Actions report → Security Issues report → Crawl Stats report → robots.txt tester → check recent core/spam update dates before assuming technical failure.

## Reusable diagnostic checklist for any future indexing complaint
1. Is it a live-site problem, or a Google-cache/crawl-lag problem? `curl` the live URL directly — don't assume from a screenshot of Google search results (that reflects Google's crawl cache, which can be weeks old).
2. Check sitemap/robots.txt cache headers if the issue is sitewide/sudden.
3. Run `site-health-check.js` for broken internal links.
4. Check for truncated titles/meta, malformed JSON-LD, mojibake — the Wave 2 bug classes.
5. Reference the Google mechanics section above before assuming a novel cause.
