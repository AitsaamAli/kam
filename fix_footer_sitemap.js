/**
 * Fix footer href="#" links + regenerate sitemap
 * Run: node fix_footer_sitemap.js
 */
const fs = require('fs');
const path = require('path');

// ── 1. Fix footer dead links in all HTML files ──────────────────────────────
const REPLACEMENTS = [
  ['href="#">Privacy</a>',    'href="/privacy">Privacy</a>'],
  ['href="#">Terms</a>',      'href="/terms">Terms</a>'],
  ['href="#">Disclaimer</a>', 'href="/disclaimer">Disclaimer</a>'],
];

const allFiles = [
  ...fs.readdirSync('.').filter(f => f.endsWith('.html')),
  ...fs.readdirSync('blogs').filter(f => f.endsWith('.html')).map(f => 'blogs/' + f)
];

let footerFixed = 0;
for (const fpath of allFiles) {
  let html = fs.readFileSync(fpath, 'utf8');
  let changed = false;
  for (const [from, to] of REPLACEMENTS) {
    if (html.includes(from)) { html = html.split(from).join(to); changed = true; }
  }
  if (changed) { fs.writeFileSync(fpath, html, 'utf8'); footerFixed++; }
}
console.log('Footer links fixed:', footerFixed, 'files');

// ── 2. Regenerate sitemap.xml (drop 41 deleted blog duplicates) ─────────────
const DUP_BLOG_SLUGS = new Set([
  'annual-company-filing-guide-pakistan','atl-registration-lahore',
  'brand-name-registration-guide-pakistan','business-compliance-checklist-pakistan',
  'company-registration-consultant-lahore','corporate-tax-consultant-lahore',
  'eobi-registration-guide-pakistan','fbr-consultant-near-me-lahore',
  'fbr-notice-after-tax-return-pakistan','gst-registration-lahore',
  'how-to-check-atl-status-pakistan','how-to-respond-to-tax-notices-pakistan',
  'income-tax-consultant-dha-lahore','income-tax-return-filing-lahore',
  'kpra-registration-guide-pakistan','logo-registration-process-pakistan',
  'ntn-registration-gulberg-lahore','ntn-registration-lahore',
  'pra-registration-guide-pakistan','rental-income-tax-calculator-pakistan',
  'sales-tax-consultant-lahore','social-security-registration-pakistan',
  'srb-registration-guide-pakistan','tax-audit-preparation-checklist',
  'tax-consultant-allama-iqbal-town-lahore','tax-consultant-cavalry-ground-lahore',
  'tax-consultant-faisal-town-lahore','tax-consultant-garden-town-lahore',
  'tax-consultant-gulshan-ravi-lahore','tax-consultant-johar-town-lahore',
  'tax-consultant-lahore-cantt','tax-consultant-model-town-lahore',
  'tax-consultant-shadman-lahore','tax-consultant-township-lahore',
  'tax-consultant-wapda-town-lahore','tax-filing-bahria-town-lahore',
  'tax-on-agricultural-income-pakistan','tax-on-commercial-property-pakistan',
  'tax-penalties-in-pakistan','trademark-registration-cost-pakistan',
  'wealth-statement-consultant-lahore'
]);

const BASE = 'https://kambohassociates.com';
const TODAY = '2026-06-23';
const urls = [];

// Root HTML files
fs.readdirSync('.').filter(f => f.endsWith('.html')).forEach(f => {
  const slug = f === 'index.html' ? '' : f.replace('.html','');
  const url = BASE + (slug ? '/' + slug : '/');
  const priority = slug === '' ? '1.0' : ['about','contact','pricing','testimonials','blogs'].includes(slug) ? '0.8' : '0.6';
  urls.push({ url, priority, freq: 'monthly' });
});

// New pages
['privacy','terms','disclaimer'].forEach(s => {
  if (!urls.find(u => u.url.includes('/'+s))) {
    urls.push({ url: BASE+'/'+s, priority: '0.4', freq: 'yearly' });
  }
});
urls.push({ url: BASE+'/authors/aitsaam-ali', priority: '0.7', freq: 'monthly' });

// Blog files (excluding deleted duplicates)
const blogFiles = fs.readdirSync('blogs').filter(f => f.endsWith('.html'));
blogFiles.forEach(f => {
  const slug = f.replace('.html','');
  if (!DUP_BLOG_SLUGS.has(slug)) {
    urls.push({ url: BASE+'/blogs/'+slug, priority: '0.5', freq: 'monthly' });
  }
});

const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map(u => `  <url>
    <loc>${u.url}</loc>
    <lastmod>${TODAY}</lastmod>
    <changefreq>${u.freq}</changefreq>
    <priority>${u.priority}</priority>
  </url>`).join('\n')}
</urlset>`;

fs.writeFileSync('sitemap.xml', xml, 'utf8');
console.log('Sitemap regenerated:', urls.length, 'URLs (removed 41 duplicate blog entries)');
console.log('Done.');
