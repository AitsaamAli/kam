const fs = require('fs');
const path = require('path');

const REVIEWS_LINK = `<li><a href="/testimonials" style="display:flex;align-items:center;gap:5px">Reviews <span style="background:#14B8A6;color:#fff;font-size:.58rem;padding:1px 5px;border-radius:8px;font-weight:700;line-height:1.4">4.9★</span></a></li>`;

// Patterns to find and replace in different nav styles
const REPLACEMENTS = [
  // index.html style (with badge already added — skip re-adding)
  // Root pages: "<li><a href="/pricing">Pricing</a></li>\n      <li><a href="/contact">"
  {
    find: `<li><a href="/pricing">Pricing</a></li>\n      <li><a href="/contact">Contact</a></li>`,
    replace: `<li><a href="/pricing">Pricing</a></li>\n      ${REVIEWS_LINK}\n      <li><a href="/contact">Contact</a></li>`,
  },
  // Blog local pages nav style: "Pricing</a></li><li><a href="/contact">Contact</a></li><li><a href="/blogs">Blog</a></li>"
  {
    find: `<li><a href="/pricing">Pricing</a></li><li><a href="/contact">Contact</a></li><li><a href="/blogs">Blog</a></li>`,
    replace: `<li><a href="/pricing">Pricing</a></li><li><a href="/testimonials" style="display:flex;align-items:center;gap:5px">Reviews <span style="background:#14B8A6;color:#fff;font-size:.58rem;padding:1px 5px;border-radius:8px;font-weight:700;line-height:1.4">4.9★</span></a></li><li><a href="/contact">Contact</a></li><li><a href="/blogs">Blog</a></li>`,
  },
  // Mobile nav — root pages
  {
    find: `<a href="/contact">Contact</a>\n      <a href="/about">About</a>`,
    replace: `<a href="/testimonials">Reviews ★4.9</a>\n      <a href="/contact">Contact</a>\n      <a href="/about">About</a>`,
  },
  // Mobile nav — blog pages
  {
    find: `<a href="/blogs">Blog</a>\n<a href="/contact">Contact</a>`,
    replace: `<a href="/blogs">Blog</a>\n<a href="/testimonials">Reviews ★4.9</a>\n<a href="/contact">Contact</a>`,
  },
];

// Also handle mobile nav in local blog pages
const MOBILE_NAV_BLOG_FIND = `<a href="/">Home</a><a href="/income-tax-filing">Services</a><a href="/pricing">Pricing</a><a href="/blogs">Blog</a><a href="/contact">Contact</a>`;
const MOBILE_NAV_BLOG_REPLACE = `<a href="/">Home</a><a href="/income-tax-filing">Services</a><a href="/pricing">Pricing</a><a href="/testimonials">Reviews ★4.9</a><a href="/blogs">Blog</a><a href="/contact">Contact</a>`;

let updated = 0;
let skipped = 0;

function processFile(fp) {
  let html = fs.readFileSync(fp, 'utf8');

  // Skip if already has reviews link in nav
  if (html.includes('href="/testimonials"')) { skipped++; return; }

  let changed = false;

  // Try each replacement pattern
  for (const { find, replace } of REPLACEMENTS) {
    if (html.includes(find)) {
      html = html.split(find).join(replace);
      changed = true;
    }
  }

  // Mobile nav for blog local pages
  if (html.includes(MOBILE_NAV_BLOG_FIND)) {
    html = html.split(MOBILE_NAV_BLOG_FIND).join(MOBILE_NAV_BLOG_REPLACE);
    changed = true;
  }

  if (changed) {
    fs.writeFileSync(fp, html, 'utf8');
    updated++;
  } else {
    skipped++;
  }
}

// Process root HTML files
const rootFiles = fs.readdirSync(__dirname).filter(f => f.endsWith('.html'));
for (const f of rootFiles) {
  processFile(path.join(__dirname, f));
}

// Process blogs directory
const blogsDir = path.join(__dirname, 'blogs');
const blogFiles = fs.readdirSync(blogsDir).filter(f => f.endsWith('.html'));
for (const f of blogFiles) {
  processFile(path.join(blogsDir, f));
  if (updated % 200 === 0 && updated > 0) process.stdout.write(`[${updated}]`);
}

console.log(`\n✅ Updated: ${updated} files`);
console.log(`   Skipped (already had link or no match): ${skipped}`);
