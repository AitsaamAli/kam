#!/usr/bin/env node
/**
 * Sitemap Generator — kambohassociates.com
 * Run: node generate-sitemap.js
 * Run from the root of the project directory.
 * Zero external dependencies. Scans all .html files and rebuilds sitemap.xml.
 */

const fs = require('fs');
const path = require('path');

const BASE_URL = 'https://kambohassociates.com';
const TODAY = new Date().toISOString().split('T')[0];

// Pages excluded from sitemap (non-indexable / utility pages)
const EXCLUDE = new Set([
  'gst-calculator.html',
  'income-estimator.html',
  'salary-calculator.html',
  'tax-calculator.html',
  '404.html',
  'thank-you.html',
]);

// Known service pages get higher priority
const SERVICE_PAGES = new Set([
  'income-tax-filing.html',
  'ntn-registration.html',
  'sales-tax-registration.html',
  'sales-tax-return.html',
  'corporate-tax-return.html',
  'fbr-notice-defense.html',
  'wealth-statement.html',
  'withholding-tax.html',
  'eobi-registration.html',
  'aop-tax-return.html',
  'tax-exemption-certificate.html',
  'import-export-registration.html',
  'secp-vs-sole-proprietorship-pakistan.html',
  'business-advisory.html',
]);

const PRIORITY_MAP = {
  'index.html':  { priority: '1.0', changefreq: 'weekly' },
  'about.html':  { priority: '0.8', changefreq: 'monthly' },
  'contact.html':{ priority: '0.8', changefreq: 'monthly' },
  'pricing.html':{ priority: '0.8', changefreq: 'monthly' },
  'blogs.html':  { priority: '0.8', changefreq: 'weekly' },
};

const urls = [];

// ── Root pages ──────────────────────────────────────────────────
fs.readdirSync('.').filter(f => f.endsWith('.html')).forEach(f => {
  if (EXCLUDE.has(f)) return;
  const slug = f === 'index.html' ? '' : f.replace('.html', '');
  const loc  = slug ? `${BASE_URL}/${slug}` : `${BASE_URL}/`;
  const meta = PRIORITY_MAP[f] || (SERVICE_PAGES.has(f)
    ? { priority: '0.9', changefreq: 'monthly' }
    : { priority: '0.6', changefreq: 'monthly' });

  // Read lastmod from file mtime for accuracy
  const stat = fs.statSync(f);
  const lastmod = stat.mtime.toISOString().split('T')[0];

  urls.push({ loc, lastmod, ...meta });
});

// ── Blog posts ───────────────────────────────────────────────────
if (fs.existsSync('blogs')) {
  fs.readdirSync('blogs').filter(f => f.endsWith('.html')).forEach(f => {
    const slug = f.replace('.html', '');
    const loc  = `${BASE_URL}/blogs/${slug}`;
    const stat = fs.statSync(path.join('blogs', f));
    const lastmod = stat.mtime.toISOString().split('T')[0];
    urls.push({ loc, lastmod, changefreq: 'monthly', priority: '0.5' });
  });
}

// ── Build XML ────────────────────────────────────────────────────
let xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`;

urls.forEach(u => {
  xml += `  <url>\n    <loc>${u.loc}</loc>\n    <lastmod>${u.lastmod}</lastmod>\n    <changefreq>${u.changefreq}</changefreq>\n    <priority>${u.priority}</priority>\n  </url>\n`;
});

xml += `</urlset>\n`;

fs.writeFileSync('sitemap.xml', xml, 'utf8');
console.log(`✓ sitemap.xml regenerated — ${urls.length} URLs (${TODAY})`);
