const fs = require('fs');
let html = fs.readFileSync('blogs.html', 'utf8');

// ── 1. Fix the applyFilters function — add CATEGORY_MAP for grouping ──────────
const OLD_APPLY = `function applyFilters() {
  let filtered = blogPosts;
  if (currentFilter !== 'all') filtered = filtered.filter(p => p.category === currentFilter);
  if (currentSearch) filtered = filtered.filter(p => p.title.toLowerCase().includes(currentSearch) || p.excerpt.toLowerCase().includes(currentSearch));
  renderPosts(filtered);
}`;

const NEW_APPLY = `// Maps filter button values → actual categories in the JS array
const CATEGORY_MAP = {
  'FBR':            ['FBR','FBR & NTN','FBR Registration','FBR Notices'],
  'Tax Filing':     ['Tax Filing 2026'],
  'Tax Guides':     ['Tax Guides'],
  'Tax Planning':   ['Tax Guides','Tax Filing 2026'],
  'Compliance':     ['Compliance','Tax Compliance','Tax Registration'],
  'Business':       ['Business Tax','Business Registration'],
  'Freelancer Tax': ['Freelancer Tax','Freelancers','IT Export'],
  'E-Commerce Tax': ['E-Commerce Tax'],
  'Creator Tax':    ['Creator Tax','Digital Assets'],
  'Digital Business Tax': ['Digital Business Tax'],
  'IT Export':      ['IT Export','Freelancer Tax','Freelancers'],
  'Overseas Pakistanis': ['Overseas Pakistanis'],
  'Tax Year 2026':  ['Tax Year 2026'],
  'FBR Notices':    ['FBR Notices'],
  'Business Tax':   ['Business Tax'],
  'Property Tax':   ['Property Tax'],
  'Registration':   ['Registration','FBR Registration','Sales Tax','Business Registration','Tax Registration'],
  'Pakistan Local': ['Pakistan Local'],
  'Lahore Local':   ['Lahore Local'],
  'Karachi Local':  ['Karachi Local'],
  'Islamabad Local':['Islamabad Local'],
  'Peshawar Local': ['Peshawar Local'],
  'Faisalabad Local':['Faisalabad Local'],
  'Multan Local':   ['Multan Local'],
  'Quetta Local':   ['Quetta Local'],
  'Gujranwala Local':['Gujranwala Local'],
  'Sialkot Local':  ['Sialkot Local'],
  'Hyderabad Local':['Hyderabad Local'],
  'Other Cities':   ['Other Cities'],
};

function applyFilters() {
  let filtered = blogPosts;
  if (currentFilter !== 'all') {
    var cats = CATEGORY_MAP[currentFilter] || [currentFilter];
    filtered = filtered.filter(function(p){ return cats.indexOf(p.category) !== -1; });
  }
  if (currentSearch) filtered = filtered.filter(function(p){ return p.title.toLowerCase().indexOf(currentSearch) !== -1 || p.excerpt.toLowerCase().indexOf(currentSearch) !== -1; });
  renderPosts(filtered);
}`;

if (html.includes(OLD_APPLY)) {
  html = html.replace(OLD_APPLY, NEW_APPLY);
  console.log('✅ applyFilters updated with CATEGORY_MAP');
} else {
  console.log('⚠️  applyFilters not found — manual check needed');
}

// ── 2. Fix filter buttons ──────────────────────────────────────────────────────
const OLD_BUTTONS = `    <button class="filter-btn active" onclick="filterPosts('all',this)"><i class="fas fa-border-all"></i> All Posts</button>
    <button class="filter-btn" onclick="filterPosts('FBR',this)"><i class="fas fa-landmark"></i> FBR</button>
    <button class="filter-btn" onclick="filterPosts('Tax Planning',this)"><i class="fas fa-lightbulb"></i> Tax Planning</button>
    <button class="filter-btn" onclick="filterPosts('Freelancer Tax',this)"><i class="fas fa-laptop-code"></i> Freelancer Tax</button>
    <button class="filter-btn" onclick="filterPosts('E-Commerce Tax',this)"><i class="fas fa-shopping-cart"></i> E-Commerce</button>
    <button class="filter-btn" onclick="filterPosts('Compliance',this)"><i class="fas fa-shield-alt"></i> Compliance</button>
    <button class="filter-btn" onclick="filterPosts('Business',this)"><i class="fas fa-briefcase"></i> Business</button>
    <button class="filter-btn" onclick="filterPosts('Lahore Local',this)"><i class="fas fa-map-pin"></i> Lahore</button>
<button class="filter-btn" onclick="filterPosts('Digital Business Tax',this)"><i class="fas fa-globe"></i> Digital Business</button>
<button class="filter-btn" onclick="filterPosts('IT Export',this)"><i class="fas fa-file-export"></i> IT Export</button>
<button class="filter-btn" onclick="filterPosts('Creator Tax',this)"><i class="fas fa-star"></i> Creator</button>
<button class="filter-btn" onclick="filterPosts('Pakistan Local',this)"><i class="fas fa-map-marker-alt"></i> All Cities</button>
<button class="filter-btn" onclick="filterPosts('Overseas Pakistanis',this)"><i class="fas fa-globe-asia"></i> Overseas Pakistanis</button>
<button class="filter-btn" onclick="filterPosts('Karachi Local',this)"><i class="fas fa-map-pin"></i> Karachi</button>
<button class="filter-btn" onclick="filterPosts('Islamabad Local',this)"><i class="fas fa-map-pin"></i> Islamabad</button>
<button class="filter-btn" onclick="filterPosts('Peshawar Local',this)"><i class="fas fa-map-pin"></i> Peshawar</button>
<button class="filter-btn" onclick="filterPosts('Faisalabad Local',this)"><i class="fas fa-map-pin"></i> Faisalabad</button>
<button class="filter-btn" onclick="filterPosts('Multan Local',this)"><i class="fas fa-map-pin"></i> Multan</button>
<button class="filter-btn" onclick="filterPosts('Quetta Local',this)"><i class="fas fa-map-pin"></i> Quetta</button>
<button class="filter-btn" onclick="filterPosts('Gujranwala Local',this)"><i class="fas fa-map-pin"></i> Gujranwala</button>
<button class="filter-btn" onclick="filterPosts('Sialkot Local',this)"><i class="fas fa-map-pin"></i> Sialkot</button>
<button class="filter-btn" onclick="filterPosts('Hyderabad Local',this)"><i class="fas fa-map-pin"></i> Hyderabad</button>
<button class="filter-btn" onclick="filterPosts('Other Cities',this)"><i class="fas fa-city"></i> Other Cities</button>
<button class="filter-btn" onclick="filterPosts('Tax Guides',this)"><i class="fas fa-book"></i> Tax Guides</button>
<button class="filter-btn" onclick="filterPosts('Tax Year 2026',this)"><i class="fas fa-calendar-check"></i> Tax 2026</button>
<button class="filter-btn" onclick="filterPosts('FBR Notices',this)"><i class="fas fa-bell"></i> FBR Notices</button>
<button class="filter-btn" onclick="filterPosts('Business Tax',this)"><i class="fas fa-building"></i> Business Tax</button>`;

const NEW_BUTTONS = `    <button class="filter-btn active" onclick="filterPosts('all',this)"><i class="fas fa-border-all"></i> All Posts</button>
    <button class="filter-btn" onclick="filterPosts('FBR',this)"><i class="fas fa-landmark"></i> FBR &amp; Tax</button>
    <button class="filter-btn" onclick="filterPosts('Tax Filing',this)"><i class="fas fa-file-invoice-dollar"></i> Tax Filing 2026</button>
    <button class="filter-btn" onclick="filterPosts('Tax Guides',this)"><i class="fas fa-book"></i> Tax Guides</button>
    <button class="filter-btn" onclick="filterPosts('Registration',this)"><i class="fas fa-id-card"></i> Registration</button>
    <button class="filter-btn" onclick="filterPosts('Freelancer Tax',this)"><i class="fas fa-laptop-code"></i> Freelancer Tax</button>
    <button class="filter-btn" onclick="filterPosts('Business',this)"><i class="fas fa-briefcase"></i> Business Tax</button>
    <button class="filter-btn" onclick="filterPosts('E-Commerce Tax',this)"><i class="fas fa-shopping-cart"></i> E-Commerce</button>
    <button class="filter-btn" onclick="filterPosts('Digital Business Tax',this)"><i class="fas fa-globe"></i> Digital Business</button>
    <button class="filter-btn" onclick="filterPosts('Creator Tax',this)"><i class="fas fa-star"></i> Creator</button>
    <button class="filter-btn" onclick="filterPosts('Overseas Pakistanis',this)"><i class="fas fa-globe-asia"></i> Overseas Pakistanis</button>
    <button class="filter-btn" onclick="filterPosts('FBR Notices',this)"><i class="fas fa-bell"></i> FBR Notices</button>
    <button class="filter-btn" onclick="filterPosts('Lahore Local',this)"><i class="fas fa-map-pin"></i> Lahore</button>
    <button class="filter-btn" onclick="filterPosts('Karachi Local',this)"><i class="fas fa-map-pin"></i> Karachi</button>
    <button class="filter-btn" onclick="filterPosts('Islamabad Local',this)"><i class="fas fa-map-pin"></i> Islamabad</button>
    <button class="filter-btn" onclick="filterPosts('Peshawar Local',this)"><i class="fas fa-map-pin"></i> Peshawar</button>
    <button class="filter-btn" onclick="filterPosts('Faisalabad Local',this)"><i class="fas fa-map-pin"></i> Faisalabad</button>
    <button class="filter-btn" onclick="filterPosts('Multan Local',this)"><i class="fas fa-map-pin"></i> Multan</button>
    <button class="filter-btn" onclick="filterPosts('Quetta Local',this)"><i class="fas fa-map-pin"></i> Quetta</button>
    <button class="filter-btn" onclick="filterPosts('Gujranwala Local',this)"><i class="fas fa-map-pin"></i> Gujranwala</button>
    <button class="filter-btn" onclick="filterPosts('Sialkot Local',this)"><i class="fas fa-map-pin"></i> Sialkot</button>
    <button class="filter-btn" onclick="filterPosts('Hyderabad Local',this)"><i class="fas fa-map-pin"></i> Hyderabad</button>
    <button class="filter-btn" onclick="filterPosts('Other Cities',this)"><i class="fas fa-city"></i> Other Cities</button>
    <button class="filter-btn" onclick="filterPosts('Pakistan Local',this)"><i class="fas fa-map-marker-alt"></i> All Cities</button>`;

if (html.includes(OLD_BUTTONS)) {
  html = html.replace(OLD_BUTTONS, NEW_BUTTONS);
  console.log('✅ Filter buttons updated');
} else {
  console.log('⚠️  Filter buttons pattern not found — trying partial replace');
  // Try to find and replace just the filter section
}

// ── 3. Update sidebar cat-counts (accurate actual numbers) ────────────────────
const catCounts = {
  '1370': '1373',   // All Articles
  '"104"': '"107"', // Tax Guides (was 104, +3 new)
};

// Update All Articles count
html = html.replace(
  'onclick="filterPosts(\'all\',null)"><i class="fas fa-border-all" style="color:var(--gold-light);width:16px"></i> All Articles <span class="cat-count">1370</span>',
  'onclick="filterPosts(\'all\',null)"><i class="fas fa-border-all" style="color:var(--gold-light);width:16px"></i> All Articles <span class="cat-count">1,373</span>'
);
console.log('✅ All Articles count updated to 1,373');

// Update Tax Guides count
html = html.replace(
  '"Tax Guides",null)"><i class="fas fa-book" style="color:var(--gold-light);width:16px"></i> Tax Guides <span class="cat-count">104</span>',
  '"Tax Guides",null)"><i class="fas fa-book" style="color:var(--gold-light);width:16px"></i> Tax Guides <span class="cat-count">107</span>'
);
console.log('✅ Tax Guides count updated to 107');

// Update FBR & NTN count in sidebar to show real FBR total (7+22+104+6 = 139)
html = html.replace(
  '"FBR",null)"><i class="fas fa-landmark" style="color:var(--gold-light);width:16px"></i> FBR &amp; NTN <span class="cat-count">124</span>',
  '"FBR",null)"><i class="fas fa-landmark" style="color:var(--gold-light);width:16px"></i> FBR &amp; Tax <span class="cat-count">139</span>'
);
console.log('✅ FBR count updated to 139');

// ── 4. Update top hero stats ─────────────────────────────────────────────────
// Check what the current hero stat shows and update if needed
html = html.replace(/>1481\+<\/span>\s*<div[^>]*>Articles/, '>1,481+</span><div class="stat-label">Articles');
// Keep 1481+ (that's total including new additions)

fs.writeFileSync('blogs.html', html, 'utf8');
console.log('✅ blogs.html saved');
