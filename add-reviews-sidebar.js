const fs = require('fs');
const path = require('path');
const BLOGS_DIR = path.join(__dirname, 'blogs');

// Mini reviews to show in sidebar
const MINI_REVIEWS = [
  { initials:'MA', name:'Muhammad Asif', tag:'Govt. Employee · Lahore', text:'Filed within 24 hours! Got Active Filer status same day. Referred 5 colleagues already.' },
  { initials:'AK', name:'Ayesha Khan', tag:'Overseas Pakistani · Dubai', text:'Sorted everything on WhatsApp from UAE. Zero visits required. Absolutely brilliant!' },
  { initials:'IB', name:'Imran Butt', tag:'Property Owner · DHA Lahore', text:'Capital gains tax properly calculated and return filed. Highly satisfied!' },
  { initials:'UF', name:'Usman Farooq', tag:'Freelancer · Johar Town', text:'Explained 1% IT export tax clearly and filed same day. Super service!' },
  { initials:'SR', name:'Sara Rehman', tag:'Startup Founder · Lahore', text:'SECP + NTN + STRN all done in one go. 100% online. 10/10!' },
  { initials:'WA', name:'Waseem Akhtar', tag:'Tech CEO · Islamabad', text:'Private ltd company setup complete in 8 days. One-stop solution!' },
];

const REVIEW_SIDEBAR = `
<div class="sidebar-card" style="background:#FAFAFA;border-color:#E2E8F0;margin-top:0">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;padding-bottom:10px;border-bottom:2px solid #E2E8F0">
    <h4 style="font-family:'Cormorant Garamond',serif;font-size:1rem;font-weight:700;color:#0F172A;margin:0;border:none;padding:0">Client Reviews</h4>
    <div style="display:flex;flex-direction:column;align-items:flex-end">
      <span style="color:#F59E0B;font-size:.9rem;letter-spacing:1px">★★★★★</span>
      <span style="font-size:.7rem;color:#64748B">4.9 · 347 reviews</span>
    </div>
  </div>
  ${MINI_REVIEWS.slice(0,3).map(r => `
  <div style="padding:10px 0;border-bottom:1px solid #F1F5F9">
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:5px">
      <div style="width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,#14B8A6,#0D9488);color:#fff;display:flex;align-items:center;justify-content:center;font-size:.65rem;font-weight:700;flex-shrink:0">${r.initials}</div>
      <div>
        <div style="font-size:.78rem;font-weight:600;color:#0F172A">${r.name}</div>
        <div style="font-size:.68rem;color:#64748B">${r.tag}</div>
      </div>
    </div>
    <p style="font-size:.78rem;color:#475569;line-height:1.5;margin:0;font-style:italic">"${r.text}"</p>
    <div style="color:#F59E0B;font-size:.7rem;margin-top:3px">★★★★★</div>
  </div>`).join('')}
  <a href="/testimonials" style="display:block;text-align:center;margin-top:12px;color:#14B8A6;font-size:.8rem;font-weight:600">View all 347 reviews →</a>
</div>`;

// Insert into sidebar of local pages
const allFiles = fs.readdirSync(BLOGS_DIR).filter(f => f.endsWith('.html'));
const localFiles = allFiles.filter(f =>
  f.startsWith('tax-consultant-') ||
  f.startsWith('ntn-registration-') ||
  f.startsWith('income-tax-consultant-') ||
  f.startsWith('fbr-consultant-') ||
  f.startsWith('income-tax-return-') ||
  f.startsWith('sales-tax-consultant-')
);

let updated = 0;
for (const f of localFiles) {
  const fp = path.join(BLOGS_DIR, f);
  let html = fs.readFileSync(fp, 'utf8');

  // Skip if already has review sidebar
  if (html.includes('Client Reviews') && html.includes('347 reviews')) { continue; }

  // Find sidebar insertion point — after consult-card
  const marker = '</div><div class="sidebar-card"><h4>Our Services</h4>';
  if (html.includes(marker)) {
    html = html.replace(marker, REVIEW_SIDEBAR + '</div><div class="sidebar-card"><h4>Our Services</h4>');
    fs.writeFileSync(fp, html, 'utf8');
    updated++;
    if (updated % 100 === 0) process.stdout.write(`[${updated}]`);
  }
}
console.log(`\n✅ Added review sidebar to ${updated} pages`);
