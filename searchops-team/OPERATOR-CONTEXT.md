# Operator context

This is not a single project's brief — it's what's already known about how
this operator works, across projects. Every specialist should calibrate to
this by default unless the current project's own brief (`briefs/current.md`)
says otherwise. Read this once per session alongside Step 0/1.

## Budget reality
Projects run on tight, often near-zero recurring budgets. Default to
free-tier and near-free stacks unless the brief says otherwise:
- Hosting: Vercel free tier is the default assumption for web frontends.
- Database: Supabase free tier by default; **~$5/month is the real ceiling**
  for a paid upgrade — Supabase Pro at $25/month has already been flagged
  as too expensive for one project. Don't recommend $20-100+/month tooling
  (paid SEO suites, enterprise CDNs, premium plugin bundles) as a first
  option — lead with the free or near-free path, and only mention paid
  tools as a clearly-labeled upgrade path once the free path is exhausted.
- For SEO tooling specifically: assume no paid keyword/rank-tracking tool
  is available unless stated. Lean on free sources — Google Search
  Console, Google Autocomplete/People Also Ask sampled directly, Google
  Trends — and label paid-tool-only tactics as optional upgrades.

## Market and language
Projects are consistently built for the **Pakistani market**, frequently
selling to other Pakistani businesses (cafes, general stores). Default
assumptions unless told otherwise:
- Audience is price-sensitive Pakistani SMBs or their Pakistani customers.
- Content/UI may need Urdu and/or Roman Urdu — apply the Urdu/RTL section
  of KNOWLEDGE.md by default for consumer-facing copy, not just when asked.
- Local payment and trust patterns apply (see KNOWLEDGE.md international
  section) — cash-on-delivery / local payment methods, local case studies
  over foreign ones, local currency (PKR) throughout.
- The operator communicates in Roman Urdu mixed with English — match that
  register in your own commentary (per SKILL.md Step 2), regardless of
  what language the deliverable content itself is written in.

## Quality bar
Stated explicitly and repeatedly across projects: output must be fit for
**real commercial sale**, not a demo or student-project. A specific,
recurring instruction: work should not look or feel AI-generated — it
should read like it came from an experienced, professional team. Apply
this to SEO/content deliverables too: avoid generic AI-SEO-content tells
(formulaic headers, keyword-stuffed unnatural phrasing, filler
introductions) — see the frontend-design skill's AI-tell list for the
visual-design equivalent of this same standard.

## Known active projects (for context, not to assume relevance to a new one)
- **Cup Shup** — a cafe/restaurant POS and management web app (Johar Town),
  built for real commercial use, Vercel + Supabase stack.
- **General store / kiryana POS** — a retail management system planned for
  commercial sale in the Pakistani market, with a hard offline-capability
  requirement.
- **Tool website** — a small SEO-driven tool site, AdSense-monetized,
  targeting roughly $300/month, built with a near-zero budget.

If SearchOps work is being run on one of these, treat its own
`briefs/current.md` as authoritative for project-specific detail — this
file is background, not a substitute for that.

---
This file should be updated (not left stale) whenever the operator states a
new durable constraint or preference that would apply beyond a single
project — not for one-off project details, which belong in that project's
own brief.
