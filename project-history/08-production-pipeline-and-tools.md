# Production Pipeline & Reusable Tools

## Important: the scratchpad is ephemeral — tools listed here get deleted between sessions
Every script below has been found **deleted from the Claude Code scratchpad directory multiple times across different sessions** (the scratchpad gets pruned). None of them exist anywhere permanent in the repo right now. **Treat every script below as "recreate from this spec," not "go find the file."** If a future session wants one of these tools, rewrite it from the description here rather than searching for a file that probably doesn't exist anymore. (If you want them to stop disappearing, the fix is to commit them into the repo, e.g. under a `tools/` directory — that hasn't been done yet as of this writing.)

## The standard per-blog production workflow
For **any** new blog or full rewrite, follow this sequence:

1. **Draft the content** — real, topic-specific, in the site's Roman-Urdu/English voice (see `01-business-overview.md`), grounded only in verified facts (`09-verified-facts-and-figures.md`).
2. **Generate/write the HTML** — reuse the correct template family's CSS shell exactly (`02-site-architecture-and-templates.md`); don't hand-roll new CSS per page.
3. **Word-count check** — 2000+ words (script in `05-blog-content-inventory-and-rewrite-method.md`).
4. **Uniqueness check** — 6-word shingle overlap against every other topically-related existing page (script below). Flag ≥15% as HIGH OVERLAP and rewrite the overlapping sentences with genuinely different phrasing — don't just dilute with more words.
5. **Wire into `blogs.html`** — both the JS `blogPosts` array AND the static alphabetical `<a href>` list (see `02-site-architecture-and-templates.md` — easy to forget the second one).
6. **Wire into `sitemap.xml`** — insert a `<url>` block in a sensible position (near topically-related entries).
7. **Validate JSON-LD** — must parse as valid JSON, `FAQPage` Q&A must match the visible FAQ content (not generic boilerplate).
8. **Tag-balance check** — `div`/`table`/`ul`/`li`/`article`/`h2` open-count must equal close-count (catches accidental duplicated sections from multi-step edits — this exact bug happened during the UK pillar rewrite, see `04-seo-technical-history.md` Wave 6).
9. **Run the broken-link health check** (script below) before committing.
10. **Commit + push** — one logical commit per batch/file, descriptive message.

## Tool specs (rebuild these each session if not present in scratchpad)

### `uniqueness-check.js` — 6-word shingle overlap detector
Purpose: flag near-duplicate content between two HTML files before publishing.
```js
const fs = require('fs');
function extractText(html) {
  const artMatch = html.match(/<article[^>]*>([\s\S]*?)<\/article>/);
  const src = artMatch ? artMatch[1] : html;
  return src.replace(/<script[\s\S]*?<\/script>/g, ' ')
    .replace(/<[^>]+>/g, ' ').replace(/&[a-z]+;/g, ' ')
    .replace(/\s+/g, ' ').trim().toLowerCase();
}
function shingles(text, n) {
  const words = text.split(' ').filter(Boolean);
  const set = new Set();
  for (let i = 0; i + n <= words.length; i++) set.add(words.slice(i, i + n).join(' '));
  return set;
}
function overlapPct(setA, setB) {
  if (setA.size === 0) return 0;
  let common = 0;
  for (const s of setA) if (setB.has(s)) common++;
  return (common / setA.size) * 100;
}
function compare(fileA, fileB) {
  const shA = shingles(extractText(fs.readFileSync(fileA,'utf8')), 6);
  const shB = shingles(extractText(fs.readFileSync(fileB,'utf8')), 6);
  return Math.max(overlapPct(shA, shB), overlapPct(shB, shA));
}
// CLI: node uniqueness-check.js file1.html file2.html [file3.html ...] — compares every pair, flags >=15% as HIGH OVERLAP
```
**Threshold: ≥15% = HIGH OVERLAP, must be fixed before publishing.** This threshold has caught real problems every time it's been run (e.g. the Spain/Greece/Portugal pages sit at 17.5-36% with each other — a known, still-unfixed issue, see `10-known-issues-and-open-items.md`; the first-draft Australia visa cluster hit 17-38% against the UK cluster before being rewritten).

### `site-health-check.js` — broken internal link scanner
Purpose: catch broken `href="/..."` links sitewide before they cause GSC indexing problems (this exact bug class caused the biggest deindexing incident on the project — see `04-seo-technical-history.md` Wave 5).
```js
const fs = require('fs'); const path = require('path');
const ROOT = 'C:/Users/786/Desktop/kam';
const BLOGS_DIR = path.join(ROOT, 'blogs');
function collectExistingPaths() {
  const paths = new Set();
  fs.readdirSync(ROOT).forEach(f => { if (f.endsWith('.html')) {
    const base = f.replace(/\.html$/, ''); paths.add('/' + base); paths.add('/' + f);
    if (base === 'index') paths.add('/');
  }});
  fs.readdirSync(BLOGS_DIR).forEach(f => { if (f.endsWith('.html')) {
    const base = f.replace(/\.html$/, ''); paths.add('/blogs/' + base); paths.add('/blogs/' + f);
  }});
  paths.add('/blogs');
  return paths;
}
function checkFile(file, existingPaths) {
  const html = fs.readFileSync(file, 'utf8');
  const hrefRe = /href="(\/[^"#?]*)(#[^"]*)?"/g;
  const issues = []; let m;
  while ((m = hrefRe.exec(html))) {
    const p = m[1];
    if (/\.(svg|css|js|xml|png|jpg|ico)$/.test(p) || p.startsWith('/wp-') || p.startsWith('/images/')) continue;
    if (!existingPaths.has(p)) issues.push(p);
  }
  return issues;
}
// Iterate all files in ROOT + BLOGS_DIR, call checkFile, print per-file issues + total count.
// KNOWN CAVEAT: a target page's real path may be at site ROOT (no /blogs/ prefix) even if it "feels" like
// a blog — always check the target file's own <link rel="canonical"> before assuming its path pattern.
// This exact wrong-assumption bug has caused real broken-link regressions before (Wave 5, round 2).
```

### `new-blog-generator.js` / country-cluster generator pattern
Purpose: template-fill a full HTML page from a small JS data object, instead of hand-writing boilerplate each time.
Data shape used for the country-cluster posts: `{slug, title, description, ogTitle, ogDescription, headline, breadcrumbName, h1, datePublished, dateModified, dateLabel, readTime, faqHeading, lead, tldr, bodyHtml, faqQA:[{q,a}], ctaHeading, ctaText, ctaWhatsapp, ctaBtnLabel, ctaSecondaryHref, ctaSecondaryLabel, toc:[{id,label}], sidebarCtaHeading, sidebarCtaText, related:[{href,label}]}`.
The generator function interpolates this into the full MINIFIED-family CSS shell (`02-site-architecture-and-templates.md`), including the JSON-LD `Article`+`FAQPage`+`BreadcrumbList` blocks, nav/topbar, sidebar TOC/related/WhatsApp card, and footer. **For a new country cluster, copy this pattern and just swap the nav ticker text + breadcrumb pillar link to the new country** — don't rewrite the whole CSS shell by hand.

### Word-count script
See `05-blog-content-inventory-and-rewrite-method.md` — full script reproduced there.

### `rewrite-apply.js` (older tool, thin-blog-rewrite-specific)
Mechanizes the boilerplate part of rewriting a file matching the **fully-generic filler template** (signature string: `"How can Kamboh Associates help with this?"` in the FAQ JSON-LD — see `05-blog-content-inventory-and-rewrite-method.md` for what this template looks like). Given a blog file + a small data object (`{faqQA, lead, tldr, bodyHtml, relatedHref, relatedText}`), it replaces the generic FAQ JSON-LD, the lead+TL;DR block, and everything from the Overview H2 through `</article>`. **Safety design: errors out loudly if an expected anchor string isn't found, rather than silently corrupting a file that doesn't match the generic template** (some files have genuine topic-specific content mixed in and need hand-editing instead — the script correctly refuses to touch these).

### `bold-redesign-utils.js` (CSS-rule editing utility, for sitewide visual changes)
Two functions: `findRule(css, selectorText)` (brace-matching CSS rule locator, returns `{start, end, body}`) and `replaceOrInsertAfter(html, selectorText, newBody, anchorSelectorText)` (replaces an existing rule's body if the selector exists, or inserts a brand-new rule right after an anchor rule if it doesn't). Used for the sitewide gold-foil redesign (`03-design-system-and-branding.md`) — reuse this exact pattern for any future sitewide CSS-rule change across hundreds of files, rather than fragile string search/replace.

## General discipline notes that apply across all tooling
- **Always dry-run and diff a sitewide destructive script before applying it** — a regex-based script deletion once accidentally destroyed 216 lines of unrelated shared JS on `index.html` (see `03-design-system-and-branding.md`).
- **Re-verify word count as the literal last step before commit**, not from an earlier check in the same session (`11-working-norms-and-user-preferences.md`).
- **Re-run the broken-link health check after every batch**, not just at the end of a big project.
- When a script "isn't found" in the scratchpad, that's expected (see the note at the top of this file) — recreate it from the spec here rather than assuming something is broken.
