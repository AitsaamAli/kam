# LLM Visibility Analyst — Test Plan

**Role:** llm-visibility | **Date:** 2026-09-08 | **Workflow:** onboard (6/8)

## Baseline finding, already run this session (verified live)

Searched "best tax consultant for overseas Pakistanis in Dubai" — the exact query this project's own `best-tax-consultant-overseas-pakistanis-dubai` page (published earlier today) targets. **Kamboh Associates did not appear anywhere in the AI-generated answer.** Three real, currently-visible competitors specifically serving the overseas-Pakistani niche did appear: **Lanop Business and Tax Advisors**, **Mansoor and Co**, and **National Tax Service** — the latter two are new names not on this project's existing competitor list and worth adding to it.

This is expected, not alarming — the page was published today and AI answers take time to pick up new sources — but it establishes a real, dated baseline (2026-09-08: zero visibility) to measure against rather than assuming visibility exists.

## Test plan — exact prompts to run monthly across ChatGPT, Gemini, Perplexity, Claude, and Google AI Overviews

Grouped by funnel stage, each with the answer shape it demands and an honest read on whether this brand can currently appear in it:

| # | Prompt | Funnel stage | Answer shape it demands | Can we honestly appear? |
|---|---|---|---|---|
| 1 | "Best tax consultant for overseas Pakistanis in Dubai" | Consideration | A short list of named firms | **Not yet, verified today** — see baseline finding above. Has a matching page now; retest in 30-60 days. |
| 2 | "How much does NTN registration cost in Pakistan" | Consideration/comparison | A specific number or small comparison table | Untested this session — this project publishes an exact number (Rs. 2,000) where most competitors don't (per the keyword-research and competitor-intel findings) — a strong candidate for citation *if* the page is well-structured for extraction. |
2b | "Kamboh Associates vs Befiler" | Comparison (bottom-funnel) | A direct comparison | **Cannot appear yet — no comparison page exists.** This is the exact gap keyword-research flagged as the highest-priority open content cluster. |
| 3 | "Is it safe to share my CNIC with an online tax consultant in Pakistan" | Trust/consideration | A direct safety answer with conditions | Has a matching page (`safe-share-cnic-ntn-tax-consultant-online-pakistan`, Section H) — good extractability candidate, untested live this session. |
| 4 | "Tax consultant available on weekends in Pakistan" | Trust/urgency | A direct yes/no plus specifics | Has a matching page (Section K) — and per competitor-intel, a real competitor (PakFiler) is verified to *not* offer this, making this page's claim both true and differentiated if it gets cited. |
| 5 | "What documents do I need for NTN registration in Pakistan" | Informational, but adjacent to conversion | A checklist | Existing page (`documents-required-ntn-registration-lahore`) — informational-heavy niche, lower priority for GEO tracking than the commercial prompts above. |

## Scoring rubric

- **Mention** (0/1): does the brand name appear anywhere in the AI answer, cited or not?
- **Position**: 1st mentioned / 2nd-3rd / present but buried / not present.
- **Sentiment**: positive-specific (cites a real differentiator like price or availability) / neutral-listed (just named) / not present.

## Blank monthly tracking table (fill going forward)

| Date | Platform | Prompt # | Mention (0/1) | Position | Sentiment | Notes |
|---|---|---|---|---|---|---|
| 2026-09-08 | Google (AI-generated answer via search) | 1 | 0 | Not present | Not present | Baseline — see finding above |
| | | | | | | |

## Hand-off

- **To comparison-pages (GEO):** prompt #2b ("X vs Befiler") is a real, currently-unclaimed gap confirmed by both keyword-research and this test — the single clearest next GEO content move.
- **To competitor-intel:** two new real competitor names surfaced in this test (Mansoor and Co, National Tax Service) that weren't on the existing list — worth folding into the next competitor refresh.
- **To hallucination-monitor:** not run this session — no factually wrong claim about the brand was found in this test, but this test only covered 5 prompts; a fuller sweep could still surface something the operator should know about.

---
**Verified this session:** prompt #1's live baseline result (genuinely searched, genuinely zero visibility, two new competitor names surfaced).
**Not run this session (flagged, not guessed):** prompts #2 through #5 were designed but not executed live against ChatGPT/Gemini/Perplexity/Claude directly — this session's search tool reflects Google's AI-generated answer, not those other platforms. The operator (or a future session with those interfaces) should run the remaining prompts directly and log results in the tracking table above.
