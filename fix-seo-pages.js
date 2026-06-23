const fs = require('fs');
const path = require('path');

// ─── 1. PRICING PAGE: add SEO content section before footer ─────────────────
(function fixPricing() {
  const fp = path.join(__dirname, 'pricing.html');
  let c = fs.readFileSync(fp, 'utf8');

  const seoSection = `
<!-- SEO CONTENT SECTION -->
<section style="background:#F8FAFC;padding:72px 0">
  <div class="container" style="max-width:860px;margin:0 auto;padding:0 24px">
    <h2 style="font-family:'Cormorant Garamond',serif;font-size:2rem;color:#0F172A;text-align:center;margin-bottom:16px">Tax Consultant Fees in Pakistan — What You Should Know</h2>
    <p style="color:#64748B;text-align:center;margin-bottom:40px;font-size:.95rem">Transparent, affordable pricing with no hidden charges</p>
    <p style="color:#1E293B;line-height:1.8;margin-bottom:18px;font-size:.96rem">Tax consultant fees in Pakistan vary widely depending on the service, complexity, and the firm you choose. At Kamboh Associates, we follow a simple principle: <strong>fixed fees quoted upfront, payment only after work is done</strong>. No hidden charges, no surprises.</p>
    <p style="color:#1E293B;line-height:1.8;margin-bottom:18px;font-size:.96rem">For a <strong>salaried individual income tax return</strong>, our fee starts at Rs. 3,500 — this covers IRIS filing, wealth statement, withholding tax reconciliation, and the final acknowledgment receipt. Most salaried returns are completed same day.</p>
    <p style="color:#1E293B;line-height:1.8;margin-bottom:18px;font-size:.96rem">For <strong>freelancers and small business owners</strong>, fees start from Rs. 5,000 and depend on the volume of transactions, number of income sources, and whether accounts need to be prepared from raw bank statements.</p>
    <p style="color:#1E293B;line-height:1.8;margin-bottom:32px;font-size:.96rem"><strong>Company registration fees</strong> in Pakistan through Kamboh Associates start from Rs. 15,000, covering SECP incorporation, NTN registration, and bank account assistance. We are FBR-registered tax consultants serving clients across Pakistan — 100% online via WhatsApp.</p>

    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px;margin-bottom:40px">
      <div style="background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:20px;text-align:center">
        <div style="font-size:1.6rem;font-weight:700;color:#14B8A6;font-family:'Cormorant Garamond',serif">Rs. 3,500</div>
        <div style="font-size:.85rem;color:#64748B;margin-top:4px">Individual Tax Return</div>
      </div>
      <div style="background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:20px;text-align:center">
        <div style="font-size:1.6rem;font-weight:700;color:#14B8A6;font-family:'Cormorant Garamond',serif">Rs. 2,000</div>
        <div style="font-size:.85rem;color:#64748B;margin-top:4px">NTN Registration</div>
      </div>
      <div style="background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:20px;text-align:center">
        <div style="font-size:1.6rem;font-weight:700;color:#14B8A6;font-family:'Cormorant Garamond',serif">Rs. 15,000</div>
        <div style="font-size:.85rem;color:#64748B;margin-top:4px">Company Registration</div>
      </div>
      <div style="background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:20px;text-align:center">
        <div style="font-size:1.6rem;font-weight:700;color:#14B8A6;font-family:'Cormorant Garamond',serif">18+ Years</div>
        <div style="font-size:.85rem;color:#64748B;margin-top:4px">Experience Since 2008</div>
      </div>
    </div>

    <div style="background:linear-gradient(135deg,#0F172A,#1E3A5F);border-radius:16px;padding:28px 32px;text-align:center">
      <h3 style="font-family:'Cormorant Garamond',serif;color:#fff;font-size:1.35rem;margin-bottom:8px">Get an Exact Quote in 15 Minutes</h3>
      <p style="color:#94A3B8;font-size:.9rem;margin-bottom:18px">WhatsApp your requirement — we quote a fixed fee and start immediately.</p>
      <a href="https://wa.me/923284675162?text=I+need+a+quote+for+tax+services" style="display:inline-flex;align-items:center;gap:8px;background:#25D366;color:#fff;padding:12px 28px;border-radius:100px;font-weight:600;font-size:.92rem"><i class="fab fa-whatsapp"></i> WhatsApp 0328-4675162</a>
    </div>
  </div>
</section>

<!-- FOOTER -->`;

  c = c.replace('<!-- FOOTER -->', seoSection);
  fs.writeFileSync(fp, c, 'utf8');
  console.log('OK: pricing.html');
})();

// ─── 2. SECP PAGE: add company registration steps section ────────────────────
(function fixSecp() {
  const fp = path.join(__dirname, 'secp-vs-sole-proprietorship-pakistan.html');
  let c = fs.readFileSync(fp, 'utf8');

  const newSection = `
        <h2 id="company-registration-pakistan">Company Registration in Pakistan — Step by Step</h2>
        <p>Agar aap Private Limited Company register karna chahte hain, yeh 6-step process hai. Kamboh Associates pura process handle karta hai — aapko sirf documents dene hain.</p>
        <table class="big-compare-table">
          <thead><tr><th>Step</th><th>Action</th><th>Time</th></tr></thead>
          <tbody>
            <tr><td>1</td><td>Company name search on SECP eServices portal — check availability</td><td>Same day</td></tr>
            <tr><td>2</td><td>Draft Memorandum &amp; Articles of Association (MOA/AOA)</td><td>1–2 days</td></tr>
            <tr><td>3</td><td>Submit Form 1 online on SECP eServices — pay SECP fee</td><td>1 day</td></tr>
            <tr><td>4</td><td>SECP issues Certificate of Incorporation</td><td>3–7 working days</td></tr>
            <tr><td>5</td><td>Register company NTN on FBR IRIS</td><td>1–2 days</td></tr>
            <tr><td>6</td><td>Open corporate bank account with Certificate + NTN</td><td>3–5 working days</td></tr>
          </tbody>
        </table>
        <div class="info-box">
          <i class="fas fa-file-alt"></i>
          <p><strong>Documents required:</strong> CNIC copies of all shareholders and directors, proposed company name (3 options), registered office address, shareholding percentage of each shareholder, and initial paid-up capital amount (minimum Rs. 100,000 recommended).</p>
        </div>

        <h2 id="secp-costs">SECP Registration Costs 2026</h2>
        <table class="big-compare-table">
          <thead><tr><th>Fee Type</th><th>Amount</th></tr></thead>
          <tbody>
            <tr><td>SECP official filing fee (up to Rs. 1M capital)</td><td>Rs. 1,000 – 3,500</td></tr>
            <tr><td>Kamboh Associates professional fee</td><td>From Rs. 15,000</td></tr>
            <tr><td>NTN registration (included)</td><td>Included</td></tr>
            <tr><td>Bank account assistance (included)</td><td>Included</td></tr>
            <tr><td>Total (approx.)</td><td><strong>Rs. 16,000 – 20,000</strong></td></tr>
          </tbody>
        </table>
`;

  // Insert before the article-cta div
  c = c.replace('<div class="article-cta">', newSection + '\n        <div class="article-cta">');
  fs.writeFileSync(fp, c, 'utf8');
  console.log('OK: secp-vs-sole-proprietorship-pakistan.html');
})();

console.log('\nDone! Now run: node create-new-pages.js');
