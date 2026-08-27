# Design System & Branding History

## Current design language: "Bold Gold-Foil Premium" (applied August 2026)

**Colors:**
- Navy: `#0F172A` → `#1E3A5F` → `#06110E` (radial gradient backgrounds for dark elements)
- Gold: `#E4C158` / `#B8860C` / `#D4AF37` / `#C9A227` (foil accents, buttons, borders)
- Teal: `#14B8A6` / `#0D9488` (secondary accent, links, icons — this is the site's original/base brand color)

**Signature treatments:**
- Dark CTA boxes: `radial-gradient(120% 140% at 15% -10%, #1E3A5F 0%, #0F172A 46%, #06110E 100%)` with layered gold/teal glow via `::before` radial gradients and gold-tinted `box-shadow`.
- Primary buttons: gold gradient (`linear-gradient(135deg,#E4C158,#B8860C)`), dark text (`#1A1305`), gold-tinted shadow, lift-on-hover.
- Ghost/secondary buttons: transparent with white border.
- FAQ accordion icon: navy→teal gradient circle badge, flips to gold gradient + rotates on `.open`.

**How this happened:** User asked for a visual upgrade recommendation ("website ka design ko thora upgrade karna chah raha ho"), was shown mockups (published as Claude Artifacts), rejected the first version as "Bohat plain/simple lag raha hai," a bolder version was built and approved ("YA OK KARO IMPLEMENT KARO"), then applied sitewide per template family (see `02-site-architecture-and-templates.md` for the family list) — CTA boxes/buttons first (1267 files across all 4 families), then FAQ accordion icons (also 1267 files). User explicitly declined extending the redesign to service cards ("Yahin ruk jao, CTA+FAQ kaafi hai").

**Implementation pattern:** a small reusable JS utility pair — `findRule(css, selectorText)` (brace-matching CSS rule locator) and `replaceOrInsertAfter(html, selectorText, newBody, anchorSelectorText)` (replaces an existing rule's body, or inserts a brand-new rule right after an anchor rule if it doesn't exist yet, e.g. adding a `:hover` or `::before` rule that wasn't there before) — applied per-family with a small per-family config script. If this needs extending to a 5th visual element or a template family gets a new variant, rebuild this same two-function pattern rather than hand-editing hundreds of files with search/replace.

## Dark mode — REMOVED, do not re-add
The site briefly had partial dark-mode support (a `data-theme` JS toggle + `prefers-color-scheme` CSS) on ~540 of 1,272 blog files. User explicitly ordered it removed sitewide ("NIGHT MODE SUPPORT NAHI BI NAHI CHIA HA MUJA PURI WEBSITE MA USKO REMOVE KARO") — done across 681 files. **Do not reintroduce dark-mode CSS/JS** unless the user explicitly asks again. Watch out if templating new pages from an old file that might still carry the theme-detect script — check for it and strip it out.

**Bug during this removal (learn from it):** a first-pass regex-based `<script>`-tag deletion script accidentally deleted ~216 lines of unrelated shared JS (mobile nav, modals, calculators) on `index.html`, because the theme-detect IIFE was embedded inside one large shared `<script>` tag rather than its own. Fixed by switching to exact literal-string matching of the known theme-script text variants instead of any tag-boundary/regex heuristic. **Lesson: always dry-run and diff a sitewide destructive script before applying it, especially anything touching shared `<script>` blocks.**

## Contrast bug (fixed, but the pattern can recur — know the fix)
A real, sitewide CSS-specificity bug caused text to visually merge into its background on gradient CTA boxes and ghost buttons across ~1,420 files: a component relying on an *inherited* `color:#fff` from a parent container was silently overridden by a wrapper's own `p{}`/`a{}` rule at equal-or-higher specificity (e.g. `.article p{color:#334155}` beating an inherited white). **Fix pattern:** force `color:#fff!important` on the specific losing selectors — this is why you'll see `color:#fff!important` scattered through several CTA/button rules in the CSS; it's deliberate, not accidental duplication. If you ever see faint/invisible text on a dark box while editing, suspect this exact pattern first.

## Logo & favicon history
- Logo: an inline SVG monogram (navy circle, gold ring, "KA" text) used in the navbar — replaced an older raster `logo.jpg` on 83 root pages, and added to 39 pages that had text-only navbar branding with no icon at all.
- **Favicon bug (subtle, two-stage fix):** the SVG favicon existed but was invisible in the browser tab. Root cause: `font-family="Cinzel,serif"` (a Google Font, unavailable in the isolated context browsers use to rasterize favicons) combined with a gradient `fill` on the SVG `<text>` — browsers rendered only the background circle, no glyph. Fixed by switching to a system font stack (`Arial,Helvetica,sans-serif`) with a solid fill color and larger font-size, applied across 1,436 pages, plus a second pass catching 8 files with a differently-colored gradient variant of the same bug. **If a favicon or any other tiny rasterized SVG text ever looks blank, suspect a webfont-in-an-isolated-render-context issue first.**
- The current favicon SVG string is short and self-contained — grep any recently-created page's `<head>` for `<link rel="icon" type="image/svg+xml"` to get the exact current markup to reuse in new pages.

## GEO/AEO signals (already in place, don't re-add)
- `llms.txt` and `llms-full.txt` exist at site root, listing key pages for AI crawlers (ChatGPT, Perplexity, Claude, Gemini).
- `robots.txt` explicitly allows `GPTBot`, `Google-Extended`, `ClaudeBot`, `PerplexityBot`.
- Every blog has `FAQPage` JSON-LD with real (not generic) Q&A, and a visible TL;DR box — both are AI-citation-friendly structures already standard practice, not something to newly propose.
