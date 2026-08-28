# Kamboh Associates — Project History (Read This First)

This folder is a deep-dive project history for **kambohassociates.com**, written so that a *fresh* Claude session (no prior conversation context) can read it and immediately continue SEO/blog work without re-discovering everything from scratch.

**Repo:** `C:\Users\786\Desktop\kam` (GitHub: `github.com/AitsaamAli/kam`, branch `main`, Vercel auto-deploy on push)
**Site:** kambohassociates.com — Pakistani tax consultancy (FBR/NTN filing, SECP company registration, sales tax, overseas Pakistani tax compliance), based in Lahore, founded 2008.
**Scale as of 2026-08-28:** 1,296 files in `blogs/`, 141 root-level HTML pages, 1,453 URLs in `sitemap.xml`, 555+ git commits since the 2026-05-19 initial commit.

## How to use this folder

Read files in this order depending on your task:

| If you're about to... | Read first |
|---|---|
| Write a new blog post | `05-blog-content-inventory-and-rewrite-method.md`, `08-production-pipeline-and-tools.md`, `09-verified-facts-and-figures.md` |
| Fix an SEO/indexing issue | `04-seo-technical-history.md` |
| Do competitor research / keyword planning | `07-competitor-landscape-and-keyword-research.md` |
| Touch CSS/design on existing pages | `02-site-architecture-and-templates.md`, `03-design-system-and-branding.md` |
| Start any content project | `11-working-norms-and-user-preferences.md` (read this one regardless — it's the rules the user has already corrected me on) |
| Understand what's already been written | `05-blog-content-inventory-and-rewrite-method.md`, `06-content-strategy-projects.md` |

## Files in this folder

1. `01-business-overview.md` — who Kamboh Associates is, services, contact, real fee schedule
2. `02-site-architecture-and-templates.md` — tech stack, the 4-5 distinct CSS template families, file layout
3. `03-design-system-and-branding.md` — the bold gold-foil visual redesign, dark-mode removal, favicon/logo history
4. `04-seo-technical-history.md` — every major SEO audit/fix wave, the GSC deindexing investigation, Master Prompt phases
5. `05-blog-content-inventory-and-rewrite-method.md` — what's done, what's thin/remaining, the generic-template bug pattern and how it's fixed
6. `06-content-strategy-projects.md` — the big planned content pushes (100-topic informational, 100-topic commercial/local, visa/overseas country clusters)
7. `07-competitor-landscape-and-keyword-research.md` — who the competitors are, how they're found, what keywords/gaps they reveal
8. `08-production-pipeline-and-tools.md` — the reusable scripts and the standard per-page production/validation workflow
9. `09-verified-facts-and-figures.md` — the numbers that are real and safe to reuse (fees, tax rates, stats) — **never invent a number not in this list**
10. `10-known-issues-and-open-items.md` — unresolved/deferred items a future session should know about
11. `11-working-norms-and-user-preferences.md` — corrections and confirmed preferences from the user, i.e. don't repeat these mistakes
12. `12-chronological-work-log.md` — month-by-month timeline of what happened, for orientation
13. `13-remaining-countries-blog-titles.md` — finalized blog **titles** for every country cluster not yet written (Germany, Canada, USA, Ireland, Gulf, Italy/Spain/Greece/Portugal) — titles/plan only, none of this content exists yet

## Critical ground rules (do not skip)

1. **Never fabricate a tax rate, fee, or statistic.** Only use numbers listed in `09-verified-facts-and-figures.md`, or numbers you've freshly verified via WebSearch/WebFetch and can cite. If unsure, hedge in the text rather than inventing a precise figure.
2. **Never touch an existing blog file when the task is "write a new blog"** — only create new files, unless the user explicitly asks for an edit to a specific existing file. (`11-working-norms-and-user-preferences.md`)
3. **Every new/rewritten blog must hit 2000+ words**, have valid JSON-LD, and be uniqueness-checked (6-word shingle overlap, flag ≥15%) against every topically-related existing page before being committed. (`08-production-pipeline-and-tools.md`)
4. **Run the broken-link health-check after every batch** before committing — this project has a documented history of link-rot bugs causing real GSC deindexing pain. (`04-seo-technical-history.md`)
5. **This folder itself may go stale.** It was compiled 2026-08-27. Before trusting a specific number (blog count, sitemap count, "current" review count), re-verify against the live repo — grep the file, don't just trust this doc. Treat everything here as a snapshot, not live state.

## What this folder is NOT

It is not a replacement for reading the actual code when doing precise work — it's an orientation layer. It's also not exhaustive of every one of the 550+ commits; `12-chronological-work-log.md` groups them thematically. For full commit-level detail, run `git log --oneline` in the repo.
