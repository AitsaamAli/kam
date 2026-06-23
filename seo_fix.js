/**
 * SEO FIX SCRIPT — Kamboh Associates
 * One-pass bulk fix for all 1,617 HTML files
 * Run: node seo_fix.js          → dry-run (counts only)
 *      node seo_fix.js --apply  → real run
 */

const fs   = require('fs');
const path = require('path');

const DRY = !process.argv.includes('--apply');
if (DRY) console.log('=== DRY-RUN MODE (no files written) ===\n');
else     console.log('=== APPLY MODE ===\n');

// ─── INPUTS ─────────────────────────────────────────────────────────────────
const AUTHOR_NAME   = 'Aitsaam Ali';
const AUTHOR_TITLE  = 'Tax Consultant | NTN • SECP • Sales Tax Specialist';
const AUTHOR_SLUG   = 'aitsaam-ali';
const AUTHOR_CREDS  = 'FBR Active Filer | NTN • SECP • Sales Tax Specialist';
const AUTHOR_BIO    = 'Aitsaam Ali is a Lahore-based tax consultant with expertise in FBR income tax filing, NTN registration, SECP company formation, and sales tax compliance. He has helped thousands of individuals, freelancers, and businesses across Pakistan fulfil their FBR obligations accurately and on time.';
const AUTHOR_URL    = 'https://kambohassociates.com/authors/' + AUTHOR_SLUG;
const FBR_STATUS    = 'FBR Active Filer';
const FULL_ADDRESS  = 'Allama Iqbal Town, Opp. Shell Pump, Main Boulevard, Lahore, Punjab, Pakistan';
const PHONE         = '+923284675162';
const EMAIL         = 'info@kambohassociates.com';
const BRAND_NAME    = 'Kamboh Associates';
const REVIEWED_DATE = '2026-06-23';

// 41 duplicate filenames (exist in root/ AND blogs/)
const DUP_SLUGS = [
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
];
const DUP_SET = new Set(DUP_SLUGS);

// Service pages needing FAQPage schema check
const SERVICE_PAGES = new Set([
  'income-tax-filing.html','ntn-registration.html','sales-tax-registration.html',
  'corporate-tax-return.html','fbr-notice-defense.html','pricing.html',
  'wealth-statement.html','withholding-tax.html','aop-tax-return.html'
]);

// ─── COUNTERS ────────────────────────────────────────────────────────────────
const c = {
  authorFixed: 0, bylineAdded: 0, fontsFixed: 0,
  faqAdded: 0, metaFilled: 0, orgEnriched: 0,
  dupCanonicalized: 0, dateModifiedAdded: 0,
  keywordsRemoved: 0, faviconFixed: 0,
  filesProcessed: 0, filesSkipped: 0
};

// ─── HELPERS ─────────────────────────────────────────────────────────────────
function write(fpath, content) {
  if (!DRY) fs.writeFileSync(fpath, content, 'utf8');
}

function getSlug(fpath) {
  return path.basename(fpath, '.html');
}

function isBlogPost(fpath) {
  return fpath.startsWith('blogs');
}

function isRootPage(fpath) {
  return !fpath.startsWith('blogs');
}

// Build rich Person schema string
function personSchema() {
  return JSON.stringify({
    '@type': 'Person',
    name: AUTHOR_NAME,
    jobTitle: AUTHOR_TITLE,
    url: AUTHOR_URL,
    knowsAbout: ['Pakistan taxation','FBR income tax filing','NTN registration',
                 'SECP company registration','sales tax','FBR compliance']
  });
}

// Enrich Organization schema with full details
function enrichOrg(orgStr) {
  try {
    const org = JSON.parse(orgStr);
    org.legalName = BRAND_NAME;
    org.founder = { '@type': 'Person', name: AUTHOR_NAME, url: AUTHOR_URL };
    org.address = {
      '@type': 'PostalAddress',
      streetAddress: 'Allama Iqbal Town, Opp. Shell Pump, Main Boulevard',
      addressLocality: 'Lahore',
      addressRegion: 'Punjab',
      addressCountry: 'PK'
    };
    org.identifier = FBR_STATUS;
    org.telephone = PHONE;
    org.email = EMAIL;
    org.url = 'https://kambohassociates.com';
    // sameAs can be added later
    return JSON.stringify(org);
  } catch(e) { return orgStr; }
}

// Extract FAQ Q&A from HTML
function extractFAQs(html) {
  const faqs = [];
  // Pattern: common FAQ structures
  const qMatches = html.matchAll(/class="faq-q[^"]*"[^>]*>([\s\S]*?)<\/[^>]+>/g);
  const aMatches = [...html.matchAll(/class="faq-a[^"]*"[^>]*>([\s\S]*?)<\/[^>]+>/g)];
  let i = 0;
  for (const q of qMatches) {
    const qText = q[1].replace(/<[^>]+>/g,'').trim();
    const aText = aMatches[i] ? aMatches[i][1].replace(/<[^>]+>/g,'').trim() : '';
    if (qText && aText) faqs.push({ q: qText, a: aText });
    i++;
  }
  return faqs;
}

// Process a single HTML file
function processFile(fpath) {
  let html = fs.readFileSync(fpath, 'utf8');
  const slug = getSlug(fpath);
  const isBlog = isBlogPost(fpath);
  const isRoot = isRootPage(fpath);
  let changed = false;

  // ── A1: Author/Person schema in blog posts ───────────────────────────────
  if (isBlog && (html.includes('"@type":"Article"') || html.includes('"@type":"BlogPosting"') || html.includes('"@type":"WebPage"'))) {
    // Replace Organization author with Person in Article schema
    const oldOrg = /"author"\s*:\s*\{"@type"\s*:\s*"Organization"[^}]*\}/;
    const newPerson = `"author": ${personSchema()}`;
    if (oldOrg.test(html)) {
      html = html.replace(oldOrg, newPerson);
      c.authorFixed++;
      changed = true;
    }
    // Also handle array schema format ["@type":"Organization"]
    const oldOrg2 = /"author"\s*:\s*\{\s*"@type"\s*:\s*"Organization"\s*,\s*"name"\s*:\s*"[^"]*"\s*\}/;
    if (oldOrg2.test(html)) {
      html = html.replace(oldOrg2, newPerson);
      c.authorFixed++;
      changed = true;
    }

    // Add dateModified if missing
    if (!html.includes('"dateModified"')) {
      html = html.replace(/"datePublished"\s*:\s*"([^"]+)"/, `"datePublished":"$1","dateModified":"${REVIEWED_DATE}"`);
      c.dateModifiedAdded++;
      changed = true;
    }

    // Add publisher to Article schema if missing
    if (!html.includes('"publisher"')) {
      const publisherStr = `,"publisher":{"@type":"Organization","name":"${BRAND_NAME}","url":"https://kambohassociates.com"}`;
      html = html.replace(/("dateModified"\s*:\s*"[^"]*")/, `$1${publisherStr}`);
      changed = true;
    }
  }

  // ── A1b: Visible byline injection in blog posts ──────────────────────────
  if (isBlog && !html.includes('class="author-byline"')) {
    const bylineHTML = `\n<div class="author-byline" style="display:flex;align-items:center;gap:10px;margin:0 0 18px;padding:12px 16px;background:rgba(20,184,166,.07);border-left:3px solid #14B8A6;border-radius:0 8px 8px 0;font-size:.85rem;color:#334155"><i class="fas fa-user-tie" style="color:#14B8A6"></i><span>By <a href="/authors/${AUTHOR_SLUG}" style="color:#0D9488;font-weight:600">${AUTHOR_NAME}</a>, <strong>${AUTHOR_TITLE}</strong> &mdash; ${AUTHOR_CREDS}</span></div>\n`;

    // Try all known article body container variants
    const markers = [
      '<article class="article-body">',
      '<div class="article-body reveal">',
      '<div class="article-body">',
      '<div class="content-body">',
    ];
    let injected = false;
    for (const marker of markers) {
      if (html.includes(marker)) {
        html = html.replace(marker, marker + bylineHTML);
        c.bylineAdded++; changed = true; injected = true; break;
      }
    }
  }

  // ── A2: Canonical fix for root survivors of duplicate pairs ─────────────
  if (isRoot && DUP_SET.has(slug)) {
    const correctCanonical = `https://kambohassociates.com/${slug}`;
    // Ensure canonical points to root version
    const canonRx = /(<link\s+rel="canonical"\s+href=")[^"]*(")/;
    if (canonRx.test(html)) {
      const current = html.match(canonRx)[2-1]; // get href value
      html = html.replace(canonRx, `$1${correctCanonical}$2`);
      c.dupCanonicalized++;
      changed = true;
    }
  }

  // ── A3: Font loading optimization ────────────────────────────────────────
  // Convert blocking Google Fonts link to preload + async pattern
  const fontLinkRx = /(<link\s+href="(https:\/\/fonts\.googleapis\.com\/css2[^"]+)"\s+rel="stylesheet"\/>)/;
  if (fontLinkRx.test(html) && !html.includes('data-font-async')) {
    const match = html.match(fontLinkRx);
    const fontUrl = match[2];
    const asyncFont = `<link rel="preload" as="style" href="${fontUrl}" onload="this.onload=null;this.rel='stylesheet'" data-font-async="1"/>\n<noscript><link rel="stylesheet" href="${fontUrl}"/></noscript>`;
    html = html.replace(fontLinkRx, asyncFont);
    c.fontsFixed++;
    changed = true;
  }

  // Make Font Awesome async too
  const faLinkRx = /(<link\s+rel="stylesheet"\s+href="(https:\/\/cdnjs\.cloudflare\.com\/[^"]+font-awesome[^"]+)"(?:\s*\/)?>)/;
  if (faLinkRx.test(html) && !html.includes('data-fa-async')) {
    const match = html.match(faLinkRx);
    const faUrl = match[2];
    const asyncFA = `<link rel="preload" as="style" href="${faUrl}" onload="this.onload=null;this.rel='stylesheet'" data-fa-async="1"/>\n<noscript><link rel="stylesheet" href="${faUrl}"/></noscript>`;
    html = html.replace(faLinkRx, asyncFA);
    changed = true;
  }

  // ── A4: FAQPage schema on service pages ──────────────────────────────────
  const fname = path.basename(fpath);
  if (SERVICE_PAGES.has(fname) && !html.includes('FAQPage')) {
    const faqs = extractFAQs(html);
    if (faqs.length > 0) {
      const faqSchema = {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        mainEntity: faqs.map(f => ({
          '@type': 'Question',
          name: f.q,
          acceptedAnswer: { '@type': 'Answer', text: f.a }
        }))
      };
      const faqTag = `\n<script type="application/ld+json">${JSON.stringify(faqSchema)}</script>`;
      html = html.replace('</head>', faqTag + '\n</head>');
      c.faqAdded++;
      changed = true;
    }
  }

  // ── A5a: Fill missing meta description ───────────────────────────────────
  if (!html.includes('<meta name="description"')) {
    const h1Match = html.match(/<h1[^>]*>([^<]+)<\/h1>/);
    const h1Text = h1Match ? h1Match[1].replace(/<[^>]+>/g,'').trim() : '';
    const pMatch = html.match(/<p[^>]*>([^<]{40,})<\/p>/);
    const pText = pMatch ? pMatch[1].replace(/<[^>]+>/g,'').trim().substring(0,120) : '';
    if (h1Text) {
      const desc = (h1Text + (pText ? ' — ' + pText : '')).substring(0, 155);
      html = html.replace('<title>', `<meta name="description" content="${desc}"/>\n<title>`);
      c.metaFilled++;
      changed = true;
    }
  }

  // ── A5b: Remove bloated keywords meta (homepage only) ────────────────────
  if (fname === 'index.html' && html.includes('<meta name="keywords"')) {
    html = html.replace(/<meta\s+name="keywords"[^>]+\/>/,'');
    c.keywordsRemoved++;
    changed = true;
  }

  // ── A5c: Enrich Organization schema ──────────────────────────────────────
  if (html.includes('"AccountingService"') || html.includes('"LocalBusiness"')) {
    if (!html.includes('"legalName"')) {
      // Find and enrich the Organization/LocalBusiness schema
      const orgSchemaRx = /(\{"@context"\s*:\s*"https:\/\/schema\.org"\s*,\s*"@type"\s*:\s*\["AccountingService"[^}]*\}(?:[^}]*\})*)/;
      // Simpler approach: inject fields before closing of first schema block
      if (!html.includes('"legalName"') && html.includes('"telephone"')) {
        html = html.replace(
          /"telephone"\s*:\s*"\+923284675162"/,
          `"legalName":"${BRAND_NAME}","telephone":"${PHONE}","email":"${EMAIL}","identifier":"${FBR_STATUS}","address":{"@type":"PostalAddress","streetAddress":"Allama Iqbal Town, Opp. Shell Pump, Main Boulevard","addressLocality":"Lahore","addressRegion":"Punjab","addressCountry":"PK"},"founder":{"@type":"Person","name":"${AUTHOR_NAME}","url":"${AUTHOR_URL}"}`
        );
        c.orgEnriched++;
        changed = true;
      }
    }
  }

  // ── A5d: Fix favicon (add proper PNG sizes) ───────────────────────────────
  if (html.includes('rel="icon" type="image/jpeg"') && !html.includes('sizes="32x32"')) {
    html = html.replace(
      '<link rel="icon" type="image/jpeg" href="/images/logo.jpg"/>',
      '<link rel="icon" type="image/jpeg" href="/images/logo.jpg"/>\n<link rel="icon" type="image/png" sizes="32x32" href="/images/logo.jpg"/>\n<link rel="apple-touch-icon" href="/images/logo.jpg"/>'
    );
    c.faviconFixed++;
    changed = true;
  }

  if (changed) c.filesProcessed++;
  else c.filesSkipped++;

  return html;
}

// ─── MAIN WALK ───────────────────────────────────────────────────────────────
function walkAndFix() {
  const allFiles = [];

  // Root HTML files
  fs.readdirSync('.').filter(f => f.endsWith('.html')).forEach(f => allFiles.push(f));

  // Blog HTML files
  fs.readdirSync('blogs').filter(f => f.endsWith('.html'))
    .forEach(f => allFiles.push(path.join('blogs', f)));

  console.log(`Processing ${allFiles.length} files...`);

  for (const fpath of allFiles) {
    try {
      const newHtml = processFile(fpath);
      if (!DRY) write(fpath, newHtml);
    } catch(e) {
      console.error('ERROR on', fpath, e.message);
    }
  }
}

// ─── PHASE A2: Build vercel.json redirects for 41 duplicate blog→root ───────
function buildRedirects() {
  let vercel = {};
  if (fs.existsSync('vercel.json')) {
    try { vercel = JSON.parse(fs.readFileSync('vercel.json','utf8')); } catch(e) {}
  }

  const existingRedirects = vercel.redirects || [];
  const existingSrcs = new Set(existingRedirects.map(r => r.source));

  const newRedirects = DUP_SLUGS
    .filter(slug => !existingSrcs.has(`/blogs/${slug}`))
    .map(slug => ({
      source: `/blogs/${slug}`,
      destination: `/${slug}`,
      permanent: true
    }));

  vercel.redirects = [...existingRedirects, ...newRedirects];

  if (!DRY) {
    fs.writeFileSync('vercel.json', JSON.stringify(vercel, null, 2), 'utf8');
  }
  console.log(`Redirects: ${newRedirects.length} new 301s added to vercel.json`);
  return newRedirects.length;
}

// ─── PHASE A2b: Remove /blogs/ duplicate files (after redirects set) ────────
function removeBlogDuplicates() {
  let removed = 0;
  for (const slug of DUP_SLUGS) {
    const blogPath = path.join('blogs', slug + '.html');
    if (fs.existsSync(blogPath)) {
      if (!DRY) fs.unlinkSync(blogPath);
      removed++;
    }
  }
  console.log(`Duplicate blog files removed: ${removed}`);
  return removed;
}

// ─── RUN ────────────────────────────────────────────────────────────────────
walkAndFix();
const redirectCount = buildRedirects();
const removedCount  = removeBlogDuplicates();

console.log('\n═══ RESULTS ═══');
console.log(`Files processed (changed): ${c.filesProcessed}`);
console.log(`Files unchanged:           ${c.filesSkipped}`);
console.log(`A1 Author→Person schema:   ${c.authorFixed}`);
console.log(`A1 Visible byline added:   ${c.bylineAdded}`);
console.log(`A1 dateModified added:     ${c.dateModifiedAdded}`);
console.log(`A2 Duplicates canonicalized (root): ${c.dupCanonicalized}`);
console.log(`A2 301 redirects added:    ${redirectCount}`);
console.log(`A2 Duplicate files removed: ${removedCount}`);
console.log(`A3 Fonts made async:       ${c.fontsFixed}`);
console.log(`A4 FAQPage schema added:   ${c.faqAdded}`);
console.log(`A5 Meta descriptions filled: ${c.metaFilled}`);
console.log(`A5 Org schema enriched:    ${c.orgEnriched}`);
console.log(`A5 Keywords meta removed:  ${c.keywordsRemoved}`);
console.log(`A5 Favicon multi-size added: ${c.faviconFixed}`);
if (DRY) console.log('\n✅ DRY-RUN COMPLETE. Run with --apply to write changes.');
else     console.log('\n✅ APPLY COMPLETE.');
