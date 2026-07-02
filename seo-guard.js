#!/usr/bin/env node
/**
 * SEO Guard — kambohassociates.com
 * Run: node seo-guard.js
 * Exits with code 1 (FAIL) if ANY check fails. Exits 0 if all pass.
 * Add to pre-commit hook or GitHub Action to prevent broken pages going live.
 */

const fs   = require('fs');
const path = require('path');

// ── Config ────────────────────────────────────────────────────────
const BASE_URL = 'https://kambohassociates.com';

const NON_INDEXABLE = new Set([
  'gst-calculator.html', 'income-estimator.html',
  'salary-calculator.html', 'tax-calculator.html',
  '404.html', 'thank-you.html',
]);

const SERVICE_PAGES = new Set([
  'income-tax-filing.html', 'ntn-registration.html', 'sales-tax-registration.html',
  'sales-tax-return.html', 'corporate-tax-return.html', 'fbr-notice-defense.html',
  'wealth-statement.html', 'withholding-tax.html', 'eobi-registration.html',
  'aop-tax-return.html', 'tax-exemption-certificate.html', 'import-export-registration.html',
  'secp-vs-sole-proprietorship-pakistan.html', 'business-advisory.html',
]);

// ── Helpers ───────────────────────────────────────────────────────
const errors   = [];
const warnings = [];

function fail(msg)  { errors.push('  ✗ ' + msg); }
function warn(msg)  { warnings.push('  ⚠ ' + msg); }
function pass(msg)  { console.log('  ✓ ' + msg); }

// ── Collect all files ─────────────────────────────────────────────
const rootFiles = fs.readdirSync('.').filter(f => f.endsWith('.html'));
const blogFiles = fs.existsSync('blogs')
  ? fs.readdirSync('blogs').filter(f => f.endsWith('.html')).map(f => 'blogs/' + f)
  : [];

const allFiles      = [...rootFiles, ...blogFiles];
const indexableRoot = rootFiles.filter(f => !NON_INDEXABLE.has(f));
const indexable     = [...indexableRoot, ...blogFiles];

// ── Build link graph ──────────────────────────────────────────────
const slugMap = {};
allFiles.forEach(f => {
  const slug = f.replace(/\.html$/, '');
  slugMap[slug] = f;
  slugMap[slug + '/'] = f;
  slugMap[f] = f;
});

const inlinks = {};
allFiles.forEach(f => inlinks[f] = []);

allFiles.forEach(src => {
  const c = fs.readFileSync(src, 'utf8');
  const re = /href="([^"#?]+)"/g;
  let m;
  while ((m = re.exec(c)) !== null) {
    let href = m[1];
    if (href.startsWith('/'))   href = href.substring(1);
    if (href.startsWith(BASE_URL + '/')) href = href.replace(BASE_URL + '/', '');
    if (href.startsWith('http') || href.startsWith('mailto') || href.startsWith('tel')) continue;
    const target = slugMap[href];
    if (target && target !== src && !inlinks[target].includes(src)) {
      inlinks[target].push(src);
    }
  }
});

// ── CHECK 1: Orphan pages ─────────────────────────────────────────
console.log('\n[CHECK 1] Orphan pages (zero internal inlinks)');
const HOMEPAGE_EXEMPT = new Set(['index.html']);
const orphans = indexable.filter(f => !HOMEPAGE_EXEMPT.has(f) && inlinks[f].length === 0);
if (orphans.length === 0) {
  pass('No orphan pages found');
} else {
  orphans.forEach(o => fail(`ORPHAN: ${o}`));
}

// ── CHECK 2: JS-only critical links on /blogs page ────────────────
console.log('\n[CHECK 2] blogs.html — static <a href> links (not JS-only)');
if (fs.existsSync('blogs.html')) {
  const blogsHTML = fs.readFileSync('blogs.html', 'utf8');
  const staticLinks = (blogsHTML.match(/href="\/blogs\/[^"]+"/g) || []);
  if (staticLinks.length >= blogFiles.length * 0.95) {
    pass(`blogs.html has ${staticLinks.length} static blog links (expected ~${blogFiles.length})`);
  } else {
    fail(`blogs.html only has ${staticLinks.length} static links but ${blogFiles.length} blog files exist — Googlebot will miss posts`);
  }
}

// ── CHECK 3: Sitemap completeness ─────────────────────────────────
console.log('\n[CHECK 3] sitemap.xml completeness');
if (!fs.existsSync('sitemap.xml')) {
  fail('sitemap.xml does not exist');
} else {
  const sm = fs.readFileSync('sitemap.xml', 'utf8');
  const smLocs = new Set((sm.match(/<loc>([^<]+)<\/loc>/g) || []).map(l => l.replace(/<\/?loc>/g, '')));

  // Check every indexable page is in sitemap
  let missingFromSitemap = 0;
  indexable.forEach(f => {
    const slug = f.replace(/\.html$/, '');
    const expectedLoc = slug === 'index' ? BASE_URL + '/' : `${BASE_URL}/${slug}`;
    if (!smLocs.has(expectedLoc)) {
      fail(`Missing from sitemap: ${f} (expected ${expectedLoc})`);
      missingFromSitemap++;
    }
  });

  // Check for .html in locs
  const htmlLocs = (sm.match(/<loc>[^<]+\.html<\/loc>/g) || []);
  if (htmlLocs.length > 0) fail(`sitemap.xml has ${htmlLocs.length} URLs with .html extension`);

  if (missingFromSitemap === 0 && htmlLocs.length === 0) {
    pass(`sitemap.xml covers all ${smLocs.size} indexable pages — no .html extensions`);
  }
}

// ── CHECK 4: Missing canonical / title / meta description ─────────
console.log('\n[CHECK 4] Canonical, title, meta description on all pages');
let metaIssues = 0;
indexable.forEach(f => {
  const c = fs.readFileSync(f, 'utf8');
  if (!c.includes('rel="canonical"'))         { fail(`Missing canonical: ${f}`); metaIssues++; }
  if (!/<title>[^<]+<\/title>/.test(c))       { fail(`Missing <title>: ${f}`);  metaIssues++; }
  if (!c.includes('name="description"'))      { fail(`Missing meta description: ${f}`); metaIssues++; }
});
if (metaIssues === 0) pass(`All ${indexable.length} pages have canonical, title, and meta description`);

// ── CHECK 5: noindex / robots block ───────────────────────────────
console.log('\n[CHECK 5] Accidental noindex or robots block');
let noindexIssues = 0;
indexable.forEach(f => {
  const c = fs.readFileSync(f, 'utf8');
  if (/noindex/.test(c) && !NON_INDEXABLE.has(f)) {
    // Intentional dedup: noindex is fine when the canonical points to a different page
    const canon = c.match(/<link rel="canonical" href="([^"]+)"/);
    const selfUrl = BASE_URL + '/' + f.replace(/\.html$/, '');
    if (canon && canon[1].replace(/\/$/, '') !== selfUrl) return;
    fail(`Accidental noindex on: ${f}`);
    noindexIssues++;
  }
});
if (noindexIssues === 0) pass('No accidental noindex found on indexable pages');

// Check robots.txt
if (fs.existsSync('robots.txt')) {
  const rt = fs.readFileSync('robots.txt', 'utf8');
  if (rt.includes('Disallow: /')) {
    // Check it's not "Disallow: /" (blocks everything) vs "Allow: /"
    if (/^Disallow:\s*\/\s*$/m.test(rt)) fail('robots.txt has "Disallow: /" which blocks ALL crawling!');
    else pass('robots.txt — no full crawl block');
  } else {
    pass('robots.txt — no Disallow: / found');
  }
  if (!rt.includes('Sitemap:')) fail('robots.txt is missing Sitemap: directive');
  else pass('robots.txt has Sitemap: directive');
} else {
  fail('robots.txt does not exist');
}

// ── CHECK 6: Service pages with FAQ but no FAQPage schema ─────────
console.log('\n[CHECK 6] FAQPage schema on service pages with visible FAQs');
let faqIssues = 0;
SERVICE_PAGES.forEach(f => {
  if (!fs.existsSync(f)) return;
  const c = fs.readFileSync(f, 'utf8');
  // Only flag if FAQ content exists in the body (not just CSS), indicated by faq-q class or FAQ heading in HTML
  const bodyPart = c.substring(c.indexOf('<body') > 0 ? c.indexOf('<body') : 0);
  const hasFAQContent = /class="faq-q"|class="faq-item"[\s\S]{0,500}class="faq-a"|<h[23][^>]*>FAQ|Frequently Asked/i.test(bodyPart);
  if (hasFAQContent && !c.includes('FAQPage')) {
    fail(`Service page has FAQ content but no FAQPage schema: ${f}`);
    faqIssues++;
  }
});
if (faqIssues === 0) pass('All service pages with FAQ content have FAQPage schema');

// ── CHECK 7: Blog posts missing Article/BlogPosting schema ─────────
console.log('\n[CHECK 7] BlogPosting/Article schema on blog posts');
let schemaMissing = 0;
blogFiles.forEach(f => {
  const c = fs.readFileSync(f, 'utf8');
  if (!c.includes('BlogPosting') && !c.includes('"Article"')) {
    fail(`Missing Article schema: ${f}`);
    schemaMissing++;
    if (schemaMissing >= 5) return; // limit output
  }
});
if (schemaMissing === 0) {
  pass(`All ${blogFiles.length} blog posts have BlogPosting/Article schema`);
} else {
  fail(`${schemaMissing} blog posts missing Article schema (showing first 5)`);
}

// ── SUMMARY ───────────────────────────────────────────────────────
console.log('\n' + '═'.repeat(60));
if (errors.length === 0) {
  console.log('✅  ALL SEO CHECKS PASSED');
  console.log(`    ${indexable.length} pages checked, 0 issues found.`);
  process.exit(0);
} else {
  console.log(`❌  SEO GUARD FAILED — ${errors.length} issue(s) found:\n`);
  errors.forEach(e => console.log(e));
  if (warnings.length > 0) {
    console.log('\nWarnings:');
    warnings.forEach(w => console.log(w));
  }
  process.exit(1);
}
