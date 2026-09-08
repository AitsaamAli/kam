# Client Strategy Director — 90-Day Roadmap

**Role:** strategy-director | **Date:** 2026-09-08 | **Workflow:** onboard (2/8)
**Built on:** head-search direction (measurement first, fix the stub defect, hold on new content until measured)

| Phase | Workstream | Owner | Dependency | Success measure |
|---|---|---|---|---|
| Weeks 1-2 | Wire GA4 + Search Console + a WhatsApp-click event | analytics-engineer | **PENDING — needs the operator's own Google account.** Claude cannot create a GA4 property or verify Search Console ownership without operator-side account access. See the standalone pending list saved to `briefs/current.md` and the operator's own chat for the exact steps. | GA4 property live, GSC verified, WhatsApp float-button clicks firing as a real GA4 event across at least the top 20 commercial pages |
| Weeks 1-2 | Audit and fix the 719 stale `blogPosts` stub entries | tech-auditor → web-dev | **DONE 2026-09-08** — commit `a69bdeec`. 485 dead stubs deleted, 234 repaired with real extracted data, plus 609 real files that had zero array entry at all backfilled, plus 65 pre-existing HTML-entity typos fixed as found. `blogPosts` now has exactly 1,403 entries matching the real file count, zero duplicates, zero stale stubs, zero missing files. | Verified live: 0 remaining stubs, 0 duplicates, 0 missing entries — met in full |
| Weeks 1-3 | Re-verify the two open design-call items (contrast, font-load CLS) from the last Lighthouse audit | cwv-engineer | **DONE 2026-09-08.** Contrast: already fixed sitewide per commit `26014a9b` (1,362 files, 2,609+ fixes), predates this session. Font-load CLS: verified live this session — `preconnect` + `preload as="style"` async-swap pattern with `display=swap` is already applied sitewide (confirmed on homepage, blogs.html, pricing.html, and new blog pages), which is the standard mitigation; no further action identified without a bigger self-hosted-font overhaul, which isn't warranted at this project's stage. | Both confirmed resolved, no fix plan needed |
| Weeks 3-4 | Competitor re-check against the 2026-08-13 named list (Befiler, TaxIt.pk, TaxFlow.com.pk, Difbr.pk, Oscar.pk, JZARR Filers, Pak Tax Services, Switcher Techno, Tenco Consulting) | competitor-intel | Live search/fetch access | Fresh teardown confirming which named gaps are now closed (e.g. digital invoicing, SEP tax) and which competitors have moved since the last check |
| Weeks 4-8 | Let the tracked cohort of ~15 highest-intent commercial pages (pricing, near-me, hire-for-persona, trust/how-to-choose) run under real measurement | data-analyst (reporting only, no new content) | GA4/GSC live from Phase 1 | A real dashboard view showing sessions → WhatsApp-click rate per page, even if the absolute numbers are still small |
| Week 8 | Results review — decide what content (if any) comes next based on which commercial pages actually converted | head-search + content-strategist | Weeks 4-8 tracked data | A written decision: "these 3-5 page types converted best, do more of exactly that" or "conversion signal too thin yet, extend the measurement window" — not a default "write 50 more" |
| Weeks 9-12 (conditional) | If Phase 1-2 data supports it: a small, targeted content extension (not another 90-topic batch) aimed specifically at the highest-converting page type found | content-strategist → brief-writer → writer-longform | Week 8 decision | New pages match the proven-converting pattern exactly, sized to real evidence rather than a topic-count target |

## Explicit sequencing note

Content production is deliberately the *last* phase, not the first — this reverses the pattern of the last three months (three large content batches with no measurement in between). Every phase before Week 9 either fixes a known defect or builds the measurement this project has never had. This is the direct implementation of head-search's "measurement before more content" bet.

## What this roadmap assumes

- **Assumption:** the operator can add a GA4/GTM snippet to the static HTML template without a build step (true for a plain `<script>` tag in a static site — no framework blocker exists here).
- **Assumption:** the operator wants the Week 8 review to genuinely gate Phase 3, not just be a formality before writing more content anyway — confirm this with the operator, since it's a real behavior change from the last three months' pattern.
- **Estimated, not measured:** the "~15 highest-intent commercial pages" selection is a reasoned pick from the recently-completed commercial-local-100 batch's own topic list (pricing, near-me, hire-for-persona categories), not a data-driven shortlist — it becomes data-driven only once Phase 1's measurement is live.

---
**Unverified/estimated in this deliverable:** every timeline (weeks) is a reasoned estimate for a one-operator team, not a committed date. No GSC/GA4 baseline exists yet to size "success" numerically — Phase 1 exists specifically to produce that baseline.
