const fs = require('fs');
const path = require('path');
const BLOGS_DIR = path.join(__dirname, 'blogs');

// ── MAIN SERVICE PAGES ──────────────────────────────────────────────────────
const SERVICE_LINKS = [
  { href: '/income-tax-filing', icon: 'fas fa-file-invoice-dollar', label: 'Income Tax Return Filing' },
  { href: '/ntn-registration', icon: 'fas fa-id-card', label: 'NTN Registration' },
  { href: '/secp-vs-sole-proprietorship-pakistan', icon: 'fas fa-building', label: 'Company Registration (SECP)' },
  { href: '/sales-tax-registration', icon: 'fas fa-percent', label: 'Sales Tax Registration (STRN)' },
  { href: '/fbr-notice-defense', icon: 'fas fa-shield-alt', label: 'FBR Notice Defense' },
  { href: '/wealth-statement', icon: 'fas fa-wallet', label: 'Wealth Statement' },
  { href: '/pricing', icon: 'fas fa-tags', label: 'Tax Consultant Fees & Pricing' },
  { href: '/freelancer-tax-pakistan', icon: 'fas fa-laptop-code', label: 'Freelancer Tax Pakistan' },
];

// ── POPULAR BLOG LINKS ──────────────────────────────────────────────────────
const POPULAR_BLOGS = [
  { href: '/blogs/income-tax-slab-pakistan-2026', label: 'Income Tax Slab Pakistan 2026' },
  { href: '/blogs/filer-vs-nonfiler-pakistan', label: 'Filer vs Non-Filer Pakistan 2026' },
  { href: '/blogs/tax-saving-tips-pakistan-2026', label: 'Tax Saving Tips Pakistan 2026' },
  { href: '/blogs/fbr-income-tax-return-deadline-2026-pakistan', label: 'FBR Tax Return Deadline 2026' },
  { href: '/blogs/online-income-tax-return-filing-pakistan-2026', label: 'Online Tax Return Filing Guide' },
  { href: '/blogs/tax-on-bank-profit-pakistan-2026', label: 'Tax on Bank Profit Pakistan' },
  { href: '/blogs/tax-for-property-investors-pakistan-2026', label: 'Property Investor Tax Guide' },
  { href: '/blogs/tax-for-stock-investors-pakistan-2026', label: 'Stock Investor Tax Pakistan' },
];

// ── AREA GROUPS for contextual linking ─────────────────────────────────────
const GROUPS = {
  dha: {
    label: 'DHA Lahore',
    slugs: ['tax-consultant-dha-lahore','tax-consultant-dha-phase-1-lahore','tax-consultant-dha-phase-2-lahore','tax-consultant-dha-phase-3-lahore','tax-consultant-dha-phase-4-lahore','tax-consultant-dha-phase-5-lahore','tax-consultant-dha-phase-6-lahore','tax-consultant-dha-phase-7-lahore','tax-consultant-dha-phase-8-lahore','tax-consultant-dha-phase-9-lahore','tax-consultant-dha-phase-9-prism-lahore','tax-consultant-dha-phase-9-town-lahore','tax-consultant-dha-phase-10-lahore','tax-consultant-dha-rahbar-lahore','tax-consultant-dha-raya-lahore','tax-consultant-dha-y-block-lahore','tax-consultant-dha-q-block-lahore'],
  },
  bahria: {
    label: 'Bahria Town Lahore',
    slugs: ['tax-consultant-bahria-town-lahore','tax-consultant-bahria-orchard-lahore','tax-consultant-bahria-nasheman-lahore','tax-consultant-bahria-education-city-lahore','tax-consultant-bahria-rafi-block-lahore','tax-consultant-bahria-umer-block-lahore','tax-consultant-bahria-usman-block-lahore','tax-consultant-bahria-nishtar-block-lahore','tax-consultant-sector-c-bahria-lahore','tax-consultant-sector-e-bahria-lahore','tax-consultant-sector-f-bahria-lahore','tax-consultant-tauheed-block-bahria-lahore','tax-consultant-tulip-block-bahria-lahore','tax-consultant-jasmine-block-bahria-lahore'],
  },
  gulberg: {
    label: 'Gulberg Lahore',
    slugs: ['tax-consultant-gulberg-lahore','tax-consultant-gulberg-1-lahore','tax-consultant-gulberg-2-lahore','tax-consultant-gulberg-3-lahore','tax-consultant-gulberg-4-lahore','tax-consultant-gulberg-5-lahore','tax-consultant-gulberg-iii-lahore','tax-consultant-gulberg-v-lahore','tax-consultant-gulberg-main-market-lahore','tax-consultant-gulberg-green-lahore','tax-consultant-mm-alam-road-lahore','tax-consultant-main-boulevard-gulberg-lahore','tax-consultant-ghalib-market-lahore'],
  },
  model_town: {
    label: 'Model Town Lahore',
    slugs: ['tax-consultant-model-town-lahore','tax-consultant-model-town-a-lahore','tax-consultant-model-town-b-lahore','tax-consultant-model-town-c-lahore','tax-consultant-model-town-block-d-lahore','tax-consultant-model-town-block-e-lahore','tax-consultant-model-town-block-f-lahore','tax-consultant-model-town-block-g-lahore','tax-consultant-model-town-block-h-lahore','tax-consultant-model-town-block-i-lahore','tax-consultant-model-town-block-j-lahore','tax-consultant-model-town-block-k-lahore','tax-consultant-model-town-block-l-lahore','tax-consultant-model-town-extension-lahore','tax-consultant-model-town-commercial-lahore'],
  },
  johar: {
    label: 'Johar Town Lahore',
    slugs: ['tax-consultant-johar-town-lahore','tax-consultant-johar-town-phase-1-lahore','tax-consultant-johar-town-phase-2-lahore','tax-consultant-johar-town-phase-3-lahore','tax-consultant-johar-town-block-a-lahore','tax-consultant-johar-town-block-b-lahore','tax-consultant-johar-town-block-c-lahore','tax-consultant-johar-town-block-d-lahore','tax-consultant-johar-town-block-e1-lahore','tax-consultant-johar-town-block-e2-lahore','tax-consultant-johar-town-block-g-lahore','tax-consultant-johar-town-block-k-lahore','tax-consultant-johar-town-block-l-lahore','tax-consultant-johar-town-h1-lahore','tax-consultant-johar-town-h2-lahore','tax-consultant-johar-town-h3-lahore','tax-consultant-johar-town-h4-lahore','tax-consultant-johar-town-j1-lahore','tax-consultant-johar-town-j2-lahore','tax-consultant-johar-town-j3-lahore','tax-consultant-johar-town-j4-lahore','tax-consultant-johar-town-j5-lahore'],
  },
  askari: {
    label: 'Askari Lahore',
    slugs: ['tax-consultant-askari-lahore','tax-consultant-askari-1-lahore','tax-consultant-askari-2-lahore','tax-consultant-askari-3-lahore','tax-consultant-askari-4-lahore','tax-consultant-askari-5-lahore','tax-consultant-askari-6-lahore','tax-consultant-askari-7-lahore','tax-consultant-askari-8-lahore','tax-consultant-askari-9-lahore','tax-consultant-askari-10-lahore','tax-consultant-askari-11-lahore','tax-consultant-askari-13-lahore','tax-consultant-askari-14-lahore'],
  },
  allama_iqbal: {
    label: 'Allama Iqbal Town / Iqbal Town',
    slugs: ['tax-consultant-allama-iqbal-town-lahore','tax-consultant-ait-block-a-lahore','tax-consultant-ait-block-b-lahore','tax-consultant-ait-block-c-lahore','tax-consultant-ait-block-d-lahore','tax-consultant-ait-block-e-lahore','tax-consultant-ait-block-f-lahore','tax-consultant-ait-block-g-lahore','tax-consultant-ait-block-h-lahore','tax-consultant-iqbal-town-lahore','tax-consultant-iqbal-town-block-a-lahore','tax-consultant-iqbal-town-block-b-lahore','tax-consultant-iqbal-town-block-c-lahore','tax-consultant-iqbal-town-block-j-lahore'],
  },
};

// ── HELPER: get group for a slug ───────────────────────────────────────────
function getGroup(slug) {
  for (const [key, group] of Object.entries(GROUPS)) {
    if (group.slugs.includes(slug)) return { key, ...group };
  }
  return null;
}

// ── HELPER: get 6 related Lahore slugs ────────────────────────────────────
function getRelated(slug, allSlugs) {
  const group = getGroup(slug);
  let pool = [];
  if (group) {
    pool = group.slugs.filter(s => s !== slug && fs.existsSync(path.join(BLOGS_DIR, s + '.html')));
    if (pool.length > 4) pool = pool.slice(0, 4);
  }
  // fill with other popular Lahore pages
  const fallback = [
    'tax-consultant-lahore','tax-consultant-dha-lahore','tax-consultant-gulberg-lahore',
    'tax-consultant-model-town-lahore','tax-consultant-johar-town-lahore','tax-consultant-bahria-town-lahore',
    'tax-consultant-allama-iqbal-town-lahore','tax-consultant-lahore-cantt',
    'income-tax-return-filing-lahore','ntn-registration-lahore','sales-tax-consultant-lahore',
  ];
  for (const f of fallback) {
    if (!pool.includes(f) && f !== slug && fs.existsSync(path.join(BLOGS_DIR, f + '.html'))) {
      pool.push(f);
      if (pool.length >= 6) break;
    }
  }
  return pool.slice(0, 6);
}

function slugToLabel(slug) {
  return slug
    .replace(/^(tax-consultant-|income-tax-return-filing-|ntn-registration-|sales-tax-consultant-)/, '')
    .replace(/-lahore$/, '')
    .replace(/-/g, ' ')
    .replace(/\b\w/g, c => c.toUpperCase())
    + ' — Tax Consultant Lahore';
}

// ── INTERNAL LINKS HTML BLOCK ──────────────────────────────────────────────
function buildLinksBlock(slug, allSlugs) {
  const related = getRelated(slug, allSlugs);

  const relatedHtml = related.map(s => {
    const label = slugToLabel(s);
    return `<a href="/blogs/${s}" style="display:flex;align-items:center;gap:8px;padding:9px 14px;border:1px solid #E2E8F0;border-radius:8px;font-size:.83rem;color:#1E293B;transition:all .2s;text-decoration:none" onmouseover="this.style.borderColor='#14B8A6';this.style.color='#14B8A6'" onmouseout="this.style.borderColor='#E2E8F0';this.style.color='#1E293B'"><i class="fas fa-map-marker-alt" style="color:#14B8A6;width:14px;flex-shrink:0"></i><span>${label}</span></a>`;
  }).join('\n      ');

  const serviceHtml = SERVICE_LINKS.map(s =>
    `<a href="${s.href}" style="display:flex;align-items:center;gap:8px;padding:9px 14px;border:1px solid #E2E8F0;border-radius:8px;font-size:.83rem;color:#1E293B;transition:all .2s;text-decoration:none" onmouseover="this.style.borderColor='#14B8A6';this.style.color='#14B8A6'" onmouseout="this.style.borderColor='#E2E8F0';this.style.color='#1E293B'"><i class="${s.icon}" style="color:#14B8A6;width:14px;flex-shrink:0"></i><span>${s.label}</span></a>`
  ).join('\n      ');

  const popularHtml = POPULAR_BLOGS.map(b =>
    `<a href="${b.href}" style="display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid #F1F5F9;font-size:.83rem;color:#1E293B;text-decoration:none;transition:color .15s" onmouseover="this.style.color='#14B8A6'" onmouseout="this.style.color='#1E293B'"><i class="fas fa-chevron-right" style="color:#14B8A6;font-size:.65rem;width:10px"></i> ${b.label}</a>`
  ).join('\n      ');

  return `
<div style="margin-top:32px" class="internal-links">
  <h2 style="font-family:'Cormorant Garamond',serif;font-size:1.35rem;color:#0F172A;margin-bottom:16px;display:flex;align-items:center;gap:10px"><span style="width:4px;height:22px;background:linear-gradient(135deg,#14B8A6,#0D9488);border-radius:2px;display:inline-block;flex-shrink:0"></span>Tax Consultant — Other Lahore Areas</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:8px">
    ${relatedHtml}
  </div>
</div>

<div style="margin-top:28px">
  <h2 style="font-family:'Cormorant Garamond',serif;font-size:1.35rem;color:#0F172A;margin-bottom:16px;display:flex;align-items:center;gap:10px"><span style="width:4px;height:22px;background:linear-gradient(135deg,#14B8A6,#0D9488);border-radius:2px;display:inline-block;flex-shrink:0"></span>Our Tax Services in Lahore</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:8px">
    ${serviceHtml}
  </div>
</div>

<div style="margin-top:28px;background:#F8FAFC;border-radius:12px;padding:20px">
  <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;color:#0F172A;margin-bottom:14px"><i class="fas fa-book-open" style="color:#14B8A6;margin-right:8px"></i>Popular Tax Guides — Pakistan 2026</h3>
  <div style="display:flex;flex-direction:column">
    ${popularHtml}
  </div>
</div>`;
}

// ── MAIN: process all Lahore local pages ──────────────────────────────────
const allFiles = fs.readdirSync(BLOGS_DIR).filter(f => f.endsWith('.html'));
const lahoreSlugs = allFiles
  .filter(f => f.includes('lahore') || f.includes('lahori') || f.includes('lahore'))
  .map(f => f.replace('.html', ''));

let updated = 0, skipped = 0;

for (const slug of lahoreSlugs) {
  const fp = path.join(BLOGS_DIR, slug + '.html');
  let html = fs.readFileSync(fp, 'utf8');

  // Skip if already has internal links block
  if (html.includes('internal-links') || html.includes('Other Lahore Areas')) { skipped++; continue; }

  // Find insertion point: just before </article>
  const marker = '</article>';
  const pos = html.lastIndexOf(marker);
  if (pos === -1) { skipped++; continue; }

  const block = buildLinksBlock(slug, lahoreSlugs);
  html = html.slice(0, pos) + block + '\n' + html.slice(pos);
  fs.writeFileSync(fp, html, 'utf8');
  updated++;
  if (updated % 50 === 0) process.stdout.write(`[${updated}]`);
}

console.log(`\n✅ Updated ${updated} pages with internal links`);
console.log(`   Skipped ${skipped} (already had links or no marker)`);

// ── Also update non-Lahore local pages with service links ─────────────────
const otherLocalSlugs = allFiles
  .filter(f => {
    const s = f.replace('.html','');
    return !f.includes('lahore') && (s.startsWith('tax-consultant-') || s.startsWith('ntn-registration-') || s.startsWith('income-tax-consultant-') || s.startsWith('fbr-consultant-'));
  })
  .map(f => f.replace('.html', ''));

let updated2 = 0;
for (const slug of otherLocalSlugs) {
  const fp = path.join(BLOGS_DIR, slug + '.html');
  let html = fs.readFileSync(fp, 'utf8');
  if (html.includes('internal-links') || html.includes('Our Tax Services')) { continue; }
  const marker = '</article>';
  const pos = html.lastIndexOf(marker);
  if (pos === -1) continue;

  const serviceHtml = SERVICE_LINKS.map(s =>
    `<a href="${s.href}" style="display:flex;align-items:center;gap:8px;padding:9px 14px;border:1px solid #E2E8F0;border-radius:8px;font-size:.83rem;color:#1E293B;transition:all .2s;text-decoration:none" onmouseover="this.style.borderColor='#14B8A6';this.style.color='#14B8A6'" onmouseout="this.style.borderColor='#E2E8F0';this.style.color='#1E293B'"><i class="${s.icon}" style="color:#14B8A6;width:14px;flex-shrink:0"></i><span>${s.label}</span></a>`
  ).join('\n      ');

  const popularHtml = POPULAR_BLOGS.map(b =>
    `<a href="${b.href}" style="display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid #F1F5F9;font-size:.83rem;color:#1E293B;text-decoration:none;transition:color .15s" onmouseover="this.style.color='#14B8A6'" onmouseout="this.style.color='#1E293B'"><i class="fas fa-chevron-right" style="color:#14B8A6;font-size:.65rem;width:10px"></i> ${b.label}</a>`
  ).join('\n      ');

  const block = `
<div style="margin-top:28px" class="internal-links">
  <h2 style="font-family:'Cormorant Garamond',serif;font-size:1.35rem;color:#0F172A;margin-bottom:16px;display:flex;align-items:center;gap:10px"><span style="width:4px;height:22px;background:linear-gradient(135deg,#14B8A6,#0D9488);border-radius:2px;display:inline-block;flex-shrink:0"></span>Our Tax Services</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:8px">
    ${serviceHtml}
  </div>
</div>
<div style="margin-top:24px;background:#F8FAFC;border-radius:12px;padding:20px">
  <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;color:#0F172A;margin-bottom:14px"><i class="fas fa-book-open" style="color:#14B8A6;margin-right:8px"></i>Popular Tax Guides — Pakistan 2026</h3>
  <div style="display:flex;flex-direction:column">
    ${popularHtml}
  </div>
</div>`;

  html = html.slice(0, pos) + block + '\n' + html.slice(pos);
  fs.writeFileSync(fp, html, 'utf8');
  updated2++;
}
console.log(`✅ Updated ${updated2} other local pages with service links`);
console.log(`\n📊 TOTAL UPDATED: ${updated + updated2} pages`);
