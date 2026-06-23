const fs = require('fs');
let html = fs.readFileSync('blogs.html', 'utf8');

// Replace the entire category-list div using start/end markers
const START = '<div class="category-list">';
const END   = '</div>\n      </div>\n\n      <div class="sidebar-card">\n        <div class="sidebar-title"><i class="fas fa-clock"></i> Recent Posts</div>';

const idx1 = html.indexOf(START);
const idx2 = html.indexOf(END);

if (idx1 === -1 || idx2 === -1) {
  console.log('markers not found idx1='+idx1+' idx2='+idx2);
  process.exit(1);
}

const NEW_LIST = `<div class="category-list">
          <div class="cat-item" onclick="filterPosts('all',null)"><i class="fas fa-border-all" style="color:var(--gold-light);width:16px"></i> All Articles <span class="cat-count">1,373</span></div>
          <div class="cat-item" onclick="filterPosts('Lahore Local',null)"><i class="fas fa-map-pin" style="color:var(--gold-light);width:16px"></i> Lahore Local <span class="cat-count">415</span></div>
          <div class="cat-item" onclick="filterPosts('Other Cities',null)"><i class="fas fa-city" style="color:var(--gold-light);width:16px"></i> Other Cities <span class="cat-count">155</span></div>
          <div class="cat-item" onclick="filterPosts('Tax Guides',null)"><i class="fas fa-book" style="color:var(--gold-light);width:16px"></i> Tax Guides <span class="cat-count">107</span></div>
          <div class="cat-item" onclick="filterPosts('Tax Filing',null)"><i class="fas fa-file-invoice-dollar" style="color:var(--gold-light);width:16px"></i> Tax Filing 2026 <span class="cat-count">104</span></div>
          <div class="cat-item" onclick="filterPosts('FBR',null)"><i class="fas fa-landmark" style="color:var(--gold-light);width:16px"></i> FBR &amp; Tax <span class="cat-count">139</span></div>
          <div class="cat-item" onclick="filterPosts('Karachi Local',null)"><i class="fas fa-map-pin" style="color:var(--gold-light);width:16px"></i> Karachi Local <span class="cat-count">86</span></div>
          <div class="cat-item" onclick="filterPosts('Islamabad Local',null)"><i class="fas fa-map-pin" style="color:var(--gold-light);width:16px"></i> Islamabad Local <span class="cat-count">84</span></div>
          <div class="cat-item" onclick="filterPosts('Overseas Pakistanis',null)"><i class="fas fa-globe-asia" style="color:var(--gold-light);width:16px"></i> Overseas Pakistanis <span class="cat-count">39</span></div>
          <div class="cat-item" onclick="filterPosts('Peshawar Local',null)"><i class="fas fa-map-pin" style="color:var(--gold-light);width:16px"></i> Peshawar Local <span class="cat-count">37</span></div>
          <div class="cat-item" onclick="filterPosts('Pakistan Local',null)"><i class="fas fa-map-marker-alt" style="color:var(--gold-light);width:16px"></i> All Cities <span class="cat-count">29</span></div>
          <div class="cat-item" onclick="filterPosts('Hyderabad Local',null)"><i class="fas fa-map-pin" style="color:var(--gold-light);width:16px"></i> Hyderabad Local <span class="cat-count">29</span></div>
          <div class="cat-item" onclick="filterPosts('Quetta Local',null)"><i class="fas fa-map-pin" style="color:var(--gold-light);width:16px"></i> Quetta Local <span class="cat-count">24</span></div>
          <div class="cat-item" onclick="filterPosts('Faisalabad Local',null)"><i class="fas fa-map-pin" style="color:var(--gold-light);width:16px"></i> Faisalabad Local <span class="cat-count">21</span></div>
          <div class="cat-item" onclick="filterPosts('Multan Local',null)"><i class="fas fa-map-pin" style="color:var(--gold-light);width:16px"></i> Multan Local <span class="cat-count">19</span></div>
          <div class="cat-item" onclick="filterPosts('Gujranwala Local',null)"><i class="fas fa-map-pin" style="color:var(--gold-light);width:16px"></i> Gujranwala Local <span class="cat-count">19</span></div>
          <div class="cat-item" onclick="filterPosts('Business',null)"><i class="fas fa-briefcase" style="color:var(--gold-light);width:16px"></i> Business Tax <span class="cat-count">9</span></div>
          <div class="cat-item" onclick="filterPosts('Digital Business Tax',null)"><i class="fas fa-globe" style="color:var(--gold-light);width:16px"></i> Digital Business <span class="cat-count">9</span></div>
          <div class="cat-item" onclick="filterPosts('Freelancer Tax',null)"><i class="fas fa-laptop-code" style="color:var(--gold-light);width:16px"></i> Freelancer Tax <span class="cat-count">8</span></div>
          <div class="cat-item" onclick="filterPosts('Sialkot Local',null)"><i class="fas fa-map-pin" style="color:var(--gold-light);width:16px"></i> Sialkot Local <span class="cat-count">8</span></div>
          <div class="cat-item" onclick="filterPosts('FBR Notices',null)"><i class="fas fa-bell" style="color:var(--gold-light);width:16px"></i> FBR Notices <span class="cat-count">6</span></div>
          <div class="cat-item" onclick="filterPosts('Tax Year 2026',null)"><i class="fas fa-calendar-check" style="color:var(--gold-light);width:16px"></i> Tax Year 2026 <span class="cat-count">6</span></div>
          <div class="cat-item" onclick="filterPosts('E-Commerce Tax',null)"><i class="fas fa-shopping-cart" style="color:var(--gold-light);width:16px"></i> E-Commerce Tax <span class="cat-count">3</span></div>
          <div class="cat-item" onclick="filterPosts('Creator Tax',null)"><i class="fas fa-star" style="color:var(--gold-light);width:16px"></i> Creator Tax <span class="cat-count">3</span></div>
        </div>`;

html = html.slice(0, idx1) + NEW_LIST + html.slice(idx2);
fs.writeFileSync('blogs.html', html, 'utf8');
console.log('✅ Sidebar category list replaced');
