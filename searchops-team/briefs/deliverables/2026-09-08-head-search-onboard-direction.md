# Head of Search — Direction

**Role:** head-search | **Date:** 2026-09-08 | **Workflow:** onboard (1/8)

## The single biggest opportunity

This site has already solved the volume problem — 1,403 blog posts, 1,567 total pages, sitemap and robots.txt clean, all major AI crawlers allowed, `llms.txt` published. *(Verified: file counts and configs read directly from the project this session.)* What it has not solved is the **conversion mix**: the operator's own stated goal this month is that too much of that volume is informational-only, and a 100-topic commercial/local-intent project (89 pages: pricing pages, "hire a consultant for X persona," near-me pages, profession+city combos, trust/how-to-choose pages, urgency pages) was just completed specifically to fix this. *(Verified: from this project's own memory/commit history.)*

The biggest opportunity right now is **not more content** — it's making sure the commercial content that already exists actually converts and gets found, because a second 89-page commercial batch on top of an unmeasured first one is guesswork without knowing which pages are actually driving WhatsApp contacts. **This project has zero connected measurement** — no GSC, no GA4, no contact-source tracking pasted in or wired up. *(Verified: no analytics/tracking code or data file found in this project.)*

## Three bets for the next 90 days

1. **Wire up measurement before writing anything else.** GA4 + a simple WhatsApp-click event + Search Console verification is the precondition for every other bet — without it, "did the 89 commercial pages work" stays a guess forever. This is cheap (free tier) and is the one thing that makes every future content decision evidence-based instead of another round of intuition-based topic lists.
2. **Fix the 719 stale placeholder stub entries in `blogs.html`.** *(Verified: documented in this project's own prior session, one collision already caused a real duplicate-id bug.)* This is a real, quantified, already-diagnosed defect sitting in production right now — low effort, contained scope, no ambiguity about whether it's a problem.
3. **Turn the top 10-15 highest-intent commercial pages (pricing, near-me, hire-for-persona) into a tracked cohort** and watch them for 60-90 days once GA4 is live, rather than immediately producing a third wave of commercial content. Let real signal (which pages actually generate a WhatsApp click) decide what Section M/N/O would even be, instead of pattern-matching to "more of the same city/persona combos."

## What we are explicitly not doing, and why

- **Not writing more blog content this cycle.** Three consecutive 90-100 topic batches have been produced (competitor-gap, commercial-local-100, and this session's continuation) with zero measured feedback loop yet. Adding a fourth batch before measurement exists is the definition of the "junior mistake" this package's own knowledge base warns against — checklist completion over verified outcome. *(KNOWLEDGE.md: "a deliverable existing is not the same as it working.")*
- **Not recommending a framework migration or CMS.** The static-HTML approach is working for this project's actual scale and the operator's near-zero budget — 1,567 files is well under any real crawl-budget threshold (~10k+). This would be over-engineering for the stage this project is at.
- **Not recommending paid SEO tooling (Ahrefs/Semrush-class).** Per OPERATOR-CONTEXT.md's ~$5/month ceiling, free-tier GSC + manual PAA/Autocomplete sampling is the right toolset here, not a paid suite.

## The one risk that could sink this

**Scaled-content-abuse exposure.** Three back-to-back 90-100-topic AI-assisted content batches on one domain, however individually well-researched and de-duplicated, is exactly the pattern Google's 2024 scaled-content-abuse policy was written to catch if quality/uniqueness discipline ever slips even once. *(This project's own history shows the uniqueness-check discipline has been applied rigorously and consistently — that discipline is the only thing standing between "aggressive but legitimate publishing velocity" and "policy violation." It must not lapse on a future batch produced under time pressure.)* This is the reason bet #3 above says pause and measure rather than immediately writing more.

---
**Unverified/estimated in this deliverable:** the entire "conversion problem" framing is based on the operator's own stated goal, not measured data — there is no GSC/GA4 confirming which pages currently convert or don't. This is the exact gap bet #1 exists to close.
