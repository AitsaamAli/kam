# QA Lead — Review of the Onboard Workflow (7 deliverables)

**Role:** qa-lead | **Date:** 2026-09-08 | **Workflow:** onboard (8/8, final gate)

## Verdict: PASS, with one inconsistency reconciled below and two items the operator should confirm

## What was checked

1. Every factual claim across all 7 deliverables tagged verified/estimated/assumption — confirmed present in all 7; none stated a number or platform-behavior claim as flat fact without a tag.
2. Every checkable claim actually checked this session where a tool was available, rather than pulled from stale memory — confirmed: competitor-intel, keyword-research, and llm-visibility all ran real live searches this session rather than only citing the 2026-08-13 memory snapshot, and explicitly flagged which parts of that older list were *not* re-verified (TaxFlow.com.pk, TaxIt.pk, Difbr.pk, Oscar.pk, Switcher Techno, Tenco Consulting, JZARR Filers, Pak Tax Services).
3. Code/config claims traced against real files — tech-auditor's stub count (719), array/file counts, and robots.txt content were all read live this session, not assumed from memory.

## Internal consistency — one real contradiction found and reconciled

**head-search's direction** explicitly lists "not writing more blog content this cycle" under what the project is deliberately NOT doing, and **strategy-director's roadmap** sequences all new content production into a conditional Phase 3 (weeks 9-12), gated on Phase 1-2 measurement data. **content-strategist's plan**, however, proposes writing 2 comparison pages now, without waiting for that gate.

**Reconciliation:** this is not treated as an error to silently paper over, but it needs to be stated plainly to the operator rather than left implicit: the comparison-page plan is a **deliberate, narrow exception** to the "hold until measured" rule — justified specifically because three independent specialists (keyword-research, competitor-intel, llm-visibility) converged on the same gap from three different angles, using real, live-verified competitor facts already in hand, not a speculative topic list. That is a materially different risk profile from another 90-topic batch built on assumption. **The exception is reasonable, but it should be named as an exception, not quietly treated as consistent with the "hold" rule as originally written.** Recommend the operator explicitly approve this 2-page exception separately from approving the rest of the roadmap, rather than it running by default.

## Other checks

- **Budget/tool consistency:** no deliverable recommended a paid tool or contradicted the ~$5/month ceiling from OPERATOR-CONTEXT.md — confirmed across all 7.
- **Scope discipline:** no role overreached into another role's mandate (e.g. content-strategist stopped at the plan level and explicitly handed off to brief-writer and comparison-pages rather than writing the actual page copy).
- **No manufactured problems:** tech-auditor explicitly stated what's already correct (robots.txt, static-HTML architecture, sitemap presence) rather than inventing issues — consistent with SKILL.md Step 3's rule.

## Two items the operator should confirm before this roadmap proceeds

1. **The comparison-page exception above** — approve it explicitly, or hold it until Phase 1 measurement per the original roadmap. Either is reasonable; the point is that it be a stated decision, not a default.
2. **Strategy-director's Phase 1 assumes GA4/GTM can be added without a build step** — true for this static-HTML site, but confirm the operator wants analytics wired up at all before `analytics-engineer` is actually run, since this project has operated without it for months by choice or by omission — worth knowing which.

## What was NOT checked in this pass (flagged, not silently skipped)

- No live test was run against ChatGPT, Gemini, Perplexity, or Claude directly (only Google's AI-generated search answer) — llm-visibility's own deliverable already states this plainly; repeating it here per the QA gate's job of confirming that disclosure actually happened.
- No real Core Web Vitals field data (CrUX) or Search Console coverage report was checked — both were out of scope for a file-system-only audit and are already flagged to `cwv-engineer`/`analytics-engineer` respectively.

---
**This review's own tagging:** every claim above is either a direct cross-reference to what a prior deliverable already stated (verified by re-reading those 7 files this session) or an explicit reasoning judgment about consistency (labeled as such, not presented as fact).
