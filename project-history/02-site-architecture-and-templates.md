# Site Architecture & Template System

## Stack
- **Pure static HTML/CSS/JS** — no framework, no build step. Every page is a standalone `.html` file with inline `<style>` in `<head>` and a small inline `<script>` before `</body>`.
- **Hosting:** Vercel, auto-deploys on every push to `main`. Typical deploy lag observed: 15-30 minutes (don't assume a fix "didn't work" — `curl -sI <url>` and check `X-Vercel-Cache`/`Age` headers before concluding a code bug; see `04-seo-technical-history.md`).
- **Fonts:** Google Fonts `Cormorant Garamond` (serif, headings), `DM Sans` (sans, body), `Cinzel` (serif-display, eyebrow/label text) — loaded via `preload as="style"` + `onload` swap pattern, with `<noscript>` fallback.
- **Icons:** Font Awesome 6.5.0 via CDN.
- **`vercel.json`:** holds a ~640-entry `redirects` array (301/308) consolidating legacy neighborhood/city doorway pages into their real `/blogs/` equivalents.

## Directory layout
```
kam/
├── index.html, about.html, pricing.html, contact.html, testimonials.html, ...  (root-level service/trust pages, 141 files)
├── blogs.html          ← the blog index/listing page (see below — has TWO separate blog-link mechanisms)
├── blogs/               (1,282 .html files — every individual blog post)
├── sitemap.xml           (1,439 <url> entries)
├── robots.txt, llms.txt, llms-full.txt
├── vercel.json           (redirects)
├── project-history/      (this folder)
└── [several .md reports at root — see below]
```

### `blogs.html` has two independent blog-link mechanisms — **update both when adding a blog**
1. A JS `blogPosts` array (`{id, featured, link, title, excerpt, date, category, readTime, author, icon}` objects) — powers the dynamic/featured blog cards shown on the page.
2. A large **static, alphabetically-sorted-by-slug** `<a href="/blogs/...">` list further down the file — this is what makes every post Googlebot-crawlable even without JS. **This list must be inserted in alphabetical slug order** — find the neighboring entries and insert between them, don't just append.

Forgetting either one has caused real indexing bugs before (see `04-seo-technical-history.md`).

## Existing root-level `.md` reports (read, don't duplicate)
These predate this history folder and hold detailed data from earlier optimization phases — reference them rather than re-deriving:
- `OPTIMIZATION-REPORT.md` — the "Master Prompt v3/v4" 5-phase optimization run (2026-06-26): before/after metrics across 1,761 pages.
- `SITE-AUDIT-REPORT.md` — the full invariant-based scorecard from that same audit (21 checks, pass rates).
- `CHANGELOG-seo.md` — terse phase-by-phase commit log for that same optimization run.
- `content-gap-100-new-blog-topics.md` — the 100-topic informational competitor-gap plan (see `06-content-strategy-projects.md`).
- `commercial-local-100-blog-topics.md` — the 100-topic commercial/local-intent plan (in progress, see `06-content-strategy-projects.md`).
- `internal-links-map.md`, `DEPLOYMENT_GUIDE.md`, `GSC_QUICK_START_GUIDE.md`, `PROMOTION_CALENDAR_7DAYS.md` — supporting docs from the same era, less frequently needed.

## The 4-5 distinct CSS template families (important — don't assume one CSS structure)

A visual/template audit (2026-08-01 era) found the blog corpus is **not** on one shared template — pages were generated across different tool passes over time and split into distinct "families" by their actual class-naming convention. **Always check which family a file belongs to before doing sitewide CSS edits** — a selector that exists in one family doesn't exist in another.

| Family | Approx. file count | Signature classes | Notes |
|---|---|---|---|
| **OLD-hero** (`.hero`/full) | 427 | `.cta-box`, `.btn-w`, `.btn-g`, FAQ: `.fi`/`.fq-q i`/`.fi.open` (icon rotates 45°) | Older full-markup template |
| **blog-post-hero** | 105 (104 w/ CTA) | `.article-cta`, `.cta-btn-white`, `.cta-btn-ghost`, FAQ: `.faq-item`/`.faq-q i` (rotates 180°) | Only 52/105 have buttons |
| **MINIFIED** | 35 | Short classes: `.hr`, `.ar`, `.dt`, `.ib`, `.wb`, `.cl`/`.cli`, `.faq`/`.fi`/`.fq`/`.fa`, `.ct`/`.ctb`/`.bw`/`.bg`, `.sb`/`.sc`/`.st`/`.tc`/`.cc`/`.rl` | **This is the template used by the whole visa/overseas country series** (UK, Australia, Canada, Germany, Spain, Italy, Greece, Portugal pillar + cluster pages) — see `06-content-strategy-projects.md`. A reusable generator for this exact family exists in scratchpad history (`uk-cluster-generator.js` / `australia-cluster-generator.js` pattern — rebuild similarly for the next country). |
| **blog-hero** (`NEW-full`) | 701 | No class-based dark CTA box (inline-styled instead); sidebar `.consult-card`/`.wa-btn`; FAQ: `.faq-item`/`.faq-q i` (rotates 180°) | Largest family — most of the thin-blog-rewrite corpus lives here |
| **Consultant/location pages** | small set (`best-tax-consultant-*`, `affordable-tax-consultant-*`, etc.) | Multi-line formatted markup, NOT single-line minified | A **different genre** (service/location marketing, not educational blog) AND different HTML formatting — the `rewrite-apply.js` automation script fails on these; must hand-edit. |

**How to tell which family a file is in:** grep the file for one of the signature classes above, or just open it and look at whether the CSS block is single-line-minified or multi-line-formatted.

## The visa/overseas cluster's exact CSS block (MINIFIED family)
Because this family is actively being extended (new countries), its full CSS is preserved verbatim in the generator scripts referenced in `08-production-pipeline-and-tools.md`. Key selectors: `.hr` (hero section), `.ar` (article card), `.ld` (lead paragraph), `.ib`/`.wb` (info/warning callout boxes), `.cl`/`.cli` (checklist box), `.dt` (data table), `.faq`/`.fi`/`.fq`/`.fa` (FAQ accordion), `.ct`/`.ctb`/`.bw`/`.bg` (dark gradient CTA box + gold/ghost buttons), `.sb`/`.sc`/`.st`/`.tc`/`.cc`/`.rl` (sidebar: card, section title, table-of-contents, WhatsApp card, related-links).
