#!/usr/bin/env node
/**
 * validate.js — Kamboh Associates blog batch validator
 *
 * Usage:
 *   node validate.js batch-C1.js
 *   node validate.js batch-C1.js batch-C2.js batch-D1.js      <-- cross-batch overlap ke liye SAB ek sath dein
 *
 * Checks:
 *   1. Required fields + types (generator schema)
 *   2. Word count >= 2000 (lead + tldr + bodyHtml visible text + FAQ answers)
 *   3. HTML tag balance (div/table/tr/td/th/ul/li/p/h2/h3/strong/em/span)
 *   4. TOC anchor resolution (dono taraf: toc -> body, body -> toc)
 *   5. JSON serializability
 *   6. Non-ASCII scan (sirf allowlisted typographic chars ki ijazat)
 *   7. FAQ count >= 5, aur JSON-LD ke liye q/a non-empty
 *   8. Slug uniqueness + slug format
 *   9. WhatsApp number correctness
 *  10. Banned-phrase scan (e.g. "late filer" — Finance Act 2026 ke tehat withdraw)
 *  11. Pairwise 6-word shingle overlap, >=15% = HIGH OVERLAP
 */

const fs = require('fs');
const path = require('path');

const WORD_MIN = 2000;
const OVERLAP_FLAG = 15;
const WHATSAPP = '923284675162';
const SHINGLE_N = 6;

// Allowlisted non-ASCII: em dash, en dash, curly quotes, ellipsis, euro, pound, degree
const ALLOWED_NON_ASCII = new Set(['\u2014', '\u2013', '\u2018', '\u2019', '\u201C', '\u201D', '\u2026', '\u20AC', '\u00A3', '\u00B0']);

const BANNED_PHRASES = [
  { re: /late\s*filer/i, why: 'Finance Act 2026 ke tehat "late filer" category withdraw ho chuki hai' },
  { re: /\bog:image\b/i, why: 'Blog pages par images allowed nahi hain' },
  { re: /prefers-color-scheme|data-theme/i, why: 'Dark mode sitewide remove kiya ja chuka hai' }
];

const REQUIRED_STRING_FIELDS = [
  'slug', 'title', 'description', 'ogTitle', 'ogDescription', 'headline',
  'breadcrumbName', 'h1', 'datePublished', 'dateModified', 'dateLabel',
  'readTime', 'faqHeading', 'lead', 'tldr', 'bodyHtml', 'ctaHeading',
  'ctaText', 'ctaWhatsapp', 'ctaBtnLabel', 'ctaSecondaryHref',
  'ctaSecondaryLabel', 'sidebarCtaHeading', 'sidebarCtaText'
];

const PAIRED_TAGS = ['div', 'table', 'tr', 'td', 'th', 'ul', 'ol', 'li', 'p', 'h2', 'h3', 'h4', 'strong', 'em', 'span', 'a'];

let ERRORS = 0;
let WARNINGS = 0;

function err(slug, msg) { console.log(`  [FAIL] ${slug}: ${msg}`); ERRORS++; }
function warn(slug, msg) { console.log(`  [WARN] ${slug}: ${msg}`); WARNINGS++; }

function stripTags(html) {
  return html
    .replace(/<script[\s\S]*?<\/script>/gi, ' ')
    .replace(/<style[\s\S]*?<\/style>/gi, ' ')
    .replace(/<[^>]*>/g, ' ')
    .replace(/&[a-zA-Z#0-9]+;/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function countWords(post) {
  const parts = [post.lead || '', post.tldr || '', post.bodyHtml || ''];
  (post.faqQA || []).forEach(f => { parts.push(f.q || ''); parts.push(f.a || ''); });
  return stripTags(parts.join(' ')).split(/\s+/).filter(Boolean).length;
}

function checkTagBalance(slug, html) {
  const selfClosing = /^(br|hr|img|input|meta|link)$/i;
  for (const tag of PAIRED_TAGS) {
    if (selfClosing.test(tag)) continue;
    const open = (html.match(new RegExp(`<${tag}(\\s[^>]*)?>`, 'gi')) || []).length;
    const close = (html.match(new RegExp(`</${tag}\\s*>`, 'gi')) || []).length;
    if (open !== close) {
      err(slug, `tag balance <${tag}>: ${open} open vs ${close} close`);
    }
  }
}

function checkAnchors(slug, post) {
  const bodyIds = new Set();
  const re = /<h[23][^>]*\sid=["']([^"']+)["']/gi;
  let m;
  while ((m = re.exec(post.bodyHtml))) bodyIds.add(m[1]);

  const tocIds = (post.toc || []).map(t => t.id);
  if (!tocIds.length) err(slug, 'toc khali hai');

  tocIds.forEach(id => {
    if (!bodyIds.has(id)) err(slug, `TOC anchor "#${id}" body mein kisi heading par nahi mila`);
  });
  bodyIds.forEach(id => {
    if (!tocIds.includes(id)) warn(slug, `body heading id "${id}" TOC mein nahi hai`);
  });
  const dupes = tocIds.filter((id, i) => tocIds.indexOf(id) !== i);
  if (dupes.length) err(slug, `TOC mein duplicate id: ${[...new Set(dupes)].join(', ')}`);
}

function checkNonAscii(slug, post) {
  const blob = JSON.stringify(post);
  const bad = new Map();
  for (const ch of blob) {
    const code = ch.codePointAt(0);
    if (code > 127 && !ALLOWED_NON_ASCII.has(ch)) {
      bad.set(ch, (bad.get(ch) || 0) + 1);
    }
  }
  if (bad.size) {
    const list = [...bad.entries()]
      .map(([ch, n]) => `"${ch}" (U+${ch.codePointAt(0).toString(16).toUpperCase().padStart(4, '0')}) x${n}`)
      .join(', ');
    err(slug, `non-ASCII characters mile: ${list}`);
  }
}

function checkBanned(slug, post) {
  const blob = JSON.stringify(post);
  BANNED_PHRASES.forEach(({ re, why }) => {
    if (re.test(blob)) err(slug, `banned phrase ${re} — ${why}`);
  });
}

function checkSchema(slug, post) {
  REQUIRED_STRING_FIELDS.forEach(f => {
    if (typeof post[f] !== 'string' || !post[f].trim()) err(slug, `field "${f}" missing ya khali hai`);
  });
  if (!Array.isArray(post.faqQA) || post.faqQA.length < 5) {
    err(slug, `faqQA mein kam az kam 5 sawal chahiye (abhi ${(post.faqQA || []).length})`);
  }
  (post.faqQA || []).forEach((f, i) => {
    if (!f.q || !f.a) err(slug, `faqQA[${i}] adhoora hai`);
  });
  if (!Array.isArray(post.related) || post.related.length < 3) {
    warn(slug, `related links kam hain (${(post.related || []).length})`);
  }
  (post.related || []).forEach((r, i) => {
    if (!r.href || !r.href.startsWith('/')) err(slug, `related[${i}] href root-relative hona chahiye`);
  });
  if (post.ctaWhatsapp !== WHATSAPP) err(slug, `ctaWhatsapp ghalat hai: ${post.ctaWhatsapp} (chahiye ${WHATSAPP})`);
  if (!/^[a-z0-9-]+$/.test(post.slug || '')) err(slug, 'slug format ghalat (sirf lowercase, digits, hyphen)');
  if ((post.title || '').length > 65) warn(slug, `title lamba hai (${post.title.length} chars)`);
  if ((post.description || '').length > 165) warn(slug, `meta description >165 chars (${post.description.length})`);
  try { JSON.parse(JSON.stringify(post)); } catch (e) { err(slug, 'JSON serializable nahi: ' + e.message); }
}

function shingles(text) {
  const words = text.toLowerCase().split(/\s+/).filter(Boolean);
  const set = new Set();
  for (let i = 0; i + SHINGLE_N <= words.length; i++) set.add(words.slice(i, i + SHINGLE_N).join(' '));
  return set;
}

function overlapPct(a, b) {
  if (!a.size) return 0;
  let common = 0;
  for (const s of a) if (b.has(s)) common++;
  return (common / a.size) * 100;
}

// ---- main ----
const files = process.argv.slice(2);
if (!files.length) {
  console.error('Usage: node validate.js batch-C1.js [batch-C2.js ...]');
  process.exit(2);
}

let posts = [];
files.forEach(f => {
  const abs = path.resolve(f);
  const batch = require(abs);
  const arr = Array.isArray(batch) ? batch : [batch];
  arr.forEach(p => posts.push({ ...p, __file: path.basename(f) }));
});

console.log(`\n=== Kamboh blog validator — ${posts.length} posts from ${files.length} batch file(s) ===\n`);

// per-post checks
console.log('--- Per-post checks ---');
const wordCounts = {};
posts.forEach(post => {
  const slug = post.slug || '(no slug)';
  checkSchema(slug, post);
  checkTagBalance(slug, post.bodyHtml || '');
  checkAnchors(slug, post);
  checkNonAscii(slug, post);
  checkBanned(slug, post);
  const wc = countWords(post);
  wordCounts[slug] = wc;
  if (wc < WORD_MIN) err(slug, `word count ${wc} < ${WORD_MIN}`);
});

// slug uniqueness
const slugs = posts.map(p => p.slug);
const dupSlugs = slugs.filter((s, i) => slugs.indexOf(s) !== i);
if (dupSlugs.length) { console.log(`  [FAIL] duplicate slugs: ${[...new Set(dupSlugs)].join(', ')}`); ERRORS++; }

console.log('\n--- Word counts ---');
Object.entries(wordCounts).forEach(([s, w]) => {
  console.log(`  ${w >= WORD_MIN ? 'OK  ' : 'LOW '} ${String(w).padStart(5)}  ${s}`);
});

console.log('\n--- Pairwise 6-word shingle overlap ---');
const sh = posts.map(p => shingles(stripTags([p.lead, p.tldr, p.bodyHtml, (p.faqQA || []).map(f => f.q + ' ' + f.a).join(' ')].join(' '))));
let worst = 0, worstPair = '';
for (let i = 0; i < posts.length; i++) {
  for (let j = i + 1; j < posts.length; j++) {
    const pct = Math.max(overlapPct(sh[i], sh[j]), overlapPct(sh[j], sh[i]));
    if (pct > worst) { worst = pct; worstPair = `${posts[i].slug} <-> ${posts[j].slug}`; }
    if (pct >= OVERLAP_FLAG) {
      console.log(`  [HIGH OVERLAP ${pct.toFixed(1)}%] ${posts[i].slug} <-> ${posts[j].slug}`);
      ERRORS++;
    }
  }
}
console.log(`  Highest pair: ${worst.toFixed(1)}%  (${worstPair || 'n/a'})  — threshold ${OVERLAP_FLAG}%`);

console.log(`\n=== RESULT: ${ERRORS} error(s), ${WARNINGS} warning(s) ===\n`);
process.exit(ERRORS ? 1 : 0);
