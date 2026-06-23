const fs = require('fs');
const path = require('path');

// Shared head/nav/footer from existing blog template
const HEAD = (title, desc, keywords, canonical, schema) => `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><title>${title}</title><meta name="description" content="${desc}"/><meta name="keywords" content="${keywords}"/><link rel="canonical" href="${canonical}"/><link rel="preconnect" href="https://fonts.googleapis.com"/><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700&family=DM+Sans:wght@400;500;600&family=Cinzel:wght@600;700&display=swap" rel="stylesheet"/><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/><style>:root{--navy:#0F172A;--teal:#14B8A6;--gold-light:#D4AF37;--font-display:'Cinzel',serif;--font-serif:'Cormorant Garamond',Georgia,serif;--font-body:'DM Sans',system-ui,sans-serif;--max-w:1200px}*{box-sizing:border-box;margin:0;padding:0}body{font-family:var(--font-body);background:#fff;color:#0F172A;line-height:1.65;overflow-x:hidden}a{text-decoration:none;color:inherit}ul{list-style:none}.container{max-width:var(--max-w);margin:0 auto;padding:0 24px}.topbar{background:#0F172A;padding:8px 0}.topbar .container{display:flex;justify-content:center;overflow:hidden}.topbar-promo-wrap{display:inline-flex;animation:kascroll 28s linear infinite}.topbar-promo{font-size:.73rem;color:rgba(148,163,184,.9);white-space:nowrap;flex-shrink:0}@keyframes kascroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}.navbar{position:sticky;top:0;z-index:1000;background:rgba(255,255,255,.97);backdrop-filter:blur(20px);border-bottom:1px solid #E2E8F0}.navbar .container{display:flex;align-items:center;justify-content:space-between;height:68px}.logo{display:flex;align-items:center;gap:12px}.logo-name{font-family:var(--font-display);font-size:.92rem;font-weight:700;letter-spacing:.07em;line-height:1.2}.logo-sub{font-size:.56rem;letter-spacing:.18em;color:var(--gold-light);text-transform:uppercase}.nav-links{display:flex;align-items:center;gap:4px}.nav-links>li{position:relative;list-style:none}.nav-links>li>a{font-size:.84rem;font-weight:500;color:#1E293B;display:flex;align-items:center;gap:4px;padding:8px 14px;border-radius:8px;transition:all .2s}.nav-links>li>a:hover{color:#14B8A6;background:#F0FDFA}.nav-chevron{font-size:.6rem;opacity:.6}.nav-drop{position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%) translateY(-6px);min-width:200px;background:#fff;border:1px solid #E2E8F0;border-radius:12px;box-shadow:0 8px 32px rgba(15,23,42,.12);padding:8px;opacity:0;visibility:hidden;pointer-events:none;transition:all .2s}.nav-links>li:hover .nav-drop{opacity:1;visibility:visible;pointer-events:auto;transform:translateX(-50%) translateY(0)}.nav-links>li:last-child .nav-drop{left:auto;right:0;transform:translateY(-6px)}.nav-links>li:last-child:hover .nav-drop{transform:translateY(0)}.nav-drop a{display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:8px;font-size:.82rem;color:#1E293B;transition:all .15s}.nav-drop a:hover{background:#F0FDFA;color:#14B8A6}.nav-drop a i{width:16px;text-align:center;color:#14B8A6}.nav-drop-divider{height:1px;background:#E2E8F0;margin:4px 8px}.nav-actions{display:flex;align-items:center;gap:10px}.nav-phone{font-size:.8rem;color:#64748B;display:flex;align-items:center;gap:6px}.nav-phone i{color:#14B8A6}.nav-phone a{color:#1E293B;font-weight:500}.nav-cta{background:#0F172A;color:#fff!important;padding:8px 18px!important;border-radius:8px!important;font-size:.82rem!important;font-weight:600!important;transition:all .2s!important}.nav-cta:hover{background:#14B8A6!important}.hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;background:none;border:none;padding:4px}.hamburger span{width:22px;height:2px;background:#64748B;border-radius:2px;display:block}.mobile-nav{display:none;flex-direction:column;position:fixed;top:68px;left:0;right:0;z-index:999;background:#fff;border-bottom:3px solid #14B8A6;box-shadow:0 12px 40px rgba(0,0,0,.15)}.mobile-nav.open{display:flex}.mobile-nav a{padding:14px 24px;border-bottom:1px solid #F1F5F9;font-size:.9rem;color:#64748B}.blog-hero{background:linear-gradient(135deg,#0F172A 0%,#1E3A5F 60%,#0F4C5C 100%);padding:64px 0 52px;position:relative;overflow:hidden}.blog-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 70% 30%,rgba(20,184,166,.1) 0%,transparent 60%)}.blog-hero .container{position:relative;z-index:1}.breadcrumb{display:flex;align-items:center;gap:8px;font-size:.78rem;color:rgba(148,163,184,.7);margin-bottom:20px;flex-wrap:wrap}.breadcrumb a{color:rgba(148,163,184,.7)}.breadcrumb a:hover{color:#14B8A6}.breadcrumb i{font-size:.55rem}.blog-cat{display:inline-flex;align-items:center;gap:5px;background:rgba(20,184,166,.15);border:1px solid rgba(20,184,166,.3);border-radius:100px;padding:4px 14px;font-size:.68rem;color:#14B8A6;font-family:var(--font-display);letter-spacing:.1em;text-transform:uppercase;margin-bottom:14px}.blog-hero h1{font-family:var(--font-serif);font-size:clamp(1.9rem,4vw,3rem);font-weight:700;color:#F1F5F9;line-height:1.15;margin-bottom:16px;max-width:800px}.blog-meta{display:flex;flex-wrap:wrap;gap:18px;font-size:.8rem;color:rgba(148,163,184,.8)}.blog-meta span{display:flex;align-items:center;gap:5px}.blog-meta i{color:#14B8A6}.blog-layout{display:grid;grid-template-columns:1fr 300px;gap:48px;padding:56px 0 80px;align-items:start}.article-body{background:#fff;border:1px solid #E2E8F0;border-radius:20px;padding:40px 44px;box-shadow:0 1px 3px rgba(15,23,42,.08)}.article-lead{font-family:var(--font-serif);font-size:1.15rem;color:#1E293B;line-height:1.8;margin-bottom:32px;padding-bottom:24px;border-bottom:1px solid #E2E8F0}.article-body h2{font-family:var(--font-serif);font-size:1.5rem;font-weight:600;color:#0F172A;margin:36px 0 14px;display:flex;align-items:center;gap:10px}.article-body h2::before{content:'';width:4px;height:24px;background:linear-gradient(135deg,#14B8A6,#0D9488);border-radius:2px;flex-shrink:0}.article-body p{font-size:.96rem;color:#1E293B;line-height:1.82;margin-bottom:16px}.article-body ul{margin:8px 0 16px 20px;display:flex;flex-direction:column;gap:6px}.article-body ul li{font-size:.94rem;color:#1E293B;list-style:disc;line-height:1.7}.article-body table{width:100%;border-collapse:collapse;margin:16px 0}.article-body th{background:#0F172A;color:#fff;padding:10px 14px;font-size:.84rem;text-align:left}.article-body td{padding:10px 14px;border-bottom:1px solid #E2E8F0;font-size:.88rem}.article-body tr:nth-child(even) td{background:#F8FAFC}.highlight-box{background:rgba(20,184,166,.07);border-left:4px solid #14B8A6;border-radius:0 12px 12px 0;padding:16px 20px;margin:20px 0}.highlight-box p{margin:0;font-size:.93rem}.faq-item{border:1px solid #E2E8F0;border-radius:12px;margin-bottom:10px;overflow:hidden}.faq-q{padding:15px 20px;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-size:.92rem;background:#F8FAFC}.faq-q:hover{color:#14B8A6}.faq-q i{transition:transform .3s;color:#14B8A6}.faq-a{display:none;padding:14px 20px;border-top:1px solid #E2E8F0;font-size:.88rem;line-height:1.7}.faq-item.open .faq-a{display:block}.faq-item.open .faq-q i{transform:rotate(180deg)}.sidebar-card{background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:22px;margin-bottom:20px}.sidebar-card h4{font-family:var(--font-serif);font-size:1rem;font-weight:700;margin-bottom:12px;padding-bottom:10px;border-bottom:2px solid #E2E8F0}.consult-card{background:linear-gradient(135deg,#0F172A,#1E3A5F);border-radius:12px;padding:24px;color:#fff;text-align:center;margin-bottom:20px}.consult-card h4{font-family:var(--font-serif);font-size:1.1rem;margin-bottom:8px}.consult-card p{font-size:.83rem;color:#94A3B8;margin-bottom:16px}.wa-btn{display:inline-flex;align-items:center;gap:8px;background:#25D366;color:#fff;padding:11px 22px;border-radius:100px;font-weight:600;font-size:.88rem;width:100%;justify-content:center}.price-badge{background:linear-gradient(135deg,#14B8A6,#0D9488);color:#fff;border-radius:12px;padding:18px;text-align:center;margin-bottom:12px}.price-badge .amount{font-family:var(--font-serif);font-size:1.8rem;font-weight:700}.price-badge .from{font-size:.78rem;opacity:.8}.service-list li{padding:7px 0;border-bottom:1px solid #E2E8F0;font-size:.86rem;display:flex;align-items:center;gap:8px}.service-list li:last-child{border-bottom:none}.service-list li i{color:#14B8A6;width:14px}@media(max-width:900px){.blog-layout{grid-template-columns:1fr}.nav-links,.nav-phone{display:none}.hamburger{display:flex}}@media(max-width:600px){.article-body{padding:24px 20px}.blog-hero{padding:44px 0 36px}}</style>
<script type="application/ld+json">${schema}</script>
<meta property="og:locale" content="en_PK"/><meta property="og:type" content="article"/><meta property="og:title" content="${title}"/><meta property="og:description" content="${desc}"/><meta property="og:url" content="${canonical}"/><meta property="og:site_name" content="Kamboh Associates"/><meta name="twitter:card" content="summary"/><meta name="twitter:title" content="${title}"/><meta name="twitter:description" content="${desc}"/>
</head>`;

const NAV = `<body>
<div class="topbar"><div class="container"><div class="topbar-promo-wrap"><span class="topbar-promo">FBR NOTICE? CALL KAMBOH ASSOCIATES NOW &nbsp;&bull;&nbsp; 0328-4675162 &nbsp;&bull;&nbsp; EXPERT NOTICE RESPONSE &nbsp;&bull;&nbsp; FBR NOTICE DEFENSE &nbsp;&bull;&nbsp; DON'T IGNORE &mdash; CALL NOW 0328-4675162 &nbsp;&bull;&nbsp;</span></div></div></div>
<nav class="navbar"><div class="container"><a href="/" class="logo"><div><svg width="44" height="44" viewBox="0 0 46 46" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1a3a1a"/><stop offset="100%" stop-color="#0d2a0d"/></linearGradient><linearGradient id="g2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#F0CF6B"/><stop offset="100%" stop-color="#D4AF37"/></linearGradient></defs><circle cx="23" cy="23" r="23" fill="url(#g1)"/><circle cx="23" cy="23" r="21" fill="none" stroke="url(#g2)" stroke-width="1.5"/><text x="23" y="27" font-family="Cinzel,serif" font-size="13" font-weight="700" fill="url(#g2)" text-anchor="middle" letter-spacing="1">KA</text><path id="cp" d="M 23,23 m -17,0 a 17,17 0 1,1 34,0 a 17,17 0 1,1 -34,0" fill="none"/><text font-family="Cinzel,serif" font-size="3.8" fill="#D4AF37" letter-spacing="1.8"><textPath href="#cp" startOffset="3%">KAMBOH ASSOCIATES &bull; TAX CONSULTANT &bull;</textPath></text></svg></div><div><div class="logo-name">KAMBOH ASSOCIATES</div><div class="logo-sub">Tax &amp; Regulatory Excellence</div></div></a>
<ul class="nav-links"><li><a href="/">Home</a></li><li><a href="/income-tax-filing">Services <i class="fas fa-chevron-down nav-chevron"></i></a><div class="nav-drop"><a href="/income-tax-filing"><i class="fas fa-file-invoice-dollar"></i> Income Tax Filing</a><a href="/ntn-registration"><i class="fas fa-id-card"></i> NTN Registration</a><a href="/sales-tax-registration"><i class="fas fa-percent"></i> Sales Tax Registration</a><a href="/secp-vs-sole-proprietorship-pakistan"><i class="fas fa-building"></i> SECP Company Registration</a><div class="nav-drop-divider"></div><a href="/sales-tax-return"><i class="fas fa-file-alt"></i> Sales Tax Return</a><a href="/corporate-tax-return"><i class="fas fa-building"></i> Corporate Tax Return</a><a href="/fbr-notice-defense"><i class="fas fa-shield-alt"></i> FBR Notice Defense</a><a href="/wealth-statement"><i class="fas fa-wallet"></i> Wealth Statement</a><a href="/withholding-tax"><i class="fas fa-hand-holding-usd"></i> Withholding Tax</a><a href="/eobi-registration"><i class="fas fa-users"></i> EOBI Registration</a><a href="/aop-tax-return"><i class="fas fa-handshake"></i> AOP Tax Return</a><a href="/tax-exemption-certificate"><i class="fas fa-certificate"></i> Tax Exemption Cert</a><a href="/import-export-registration"><i class="fas fa-ship"></i> Import / Export</a><div class="nav-drop-divider"></div><a href="/pricing"><i class="fas fa-tags"></i> Pricing &amp; Fees</a></div></li><li><a href="/#tools">Tools <i class="fas fa-chevron-down nav-chevron"></i></a><div class="nav-drop"><a href="/tax-calculator"><i class="fas fa-calculator"></i> Tax Calculator</a><a href="/salary-calculator"><i class="fas fa-user-tie"></i> Salary Calculator</a><a href="/gst-calculator"><i class="fas fa-percent"></i> GST Calculator</a></div></li><li><a href="/pricing">Pricing</a></li><li><a href="/contact">Contact</a></li><li><a href="/blogs">Blog <i class="fas fa-chevron-down nav-chevron"></i></a><div class="nav-drop"><a href="/blogs"><i class="fas fa-landmark"></i> FBR &amp; Tax Guides</a><a href="/blogs"><i class="fas fa-user-clock"></i> Freelancer Tax</a></div></li></ul>
<div class="nav-actions"><span class="nav-phone"><i class="fas fa-phone"></i><a href="tel:03284675162">0328-4675162</a></span><a href="/contact" class="nav-cta">Get Started</a><button class="hamburger" id="hamburger" onclick="this.classList.toggle('open');document.getElementById('mobileNav').classList.toggle('open')" aria-label="Menu"><span></span><span></span><span></span></button></div></div></nav>
<div class="mobile-nav" id="mobileNav"><a href="/">Home</a><a href="/income-tax-filing">Services</a><a href="/pricing">Pricing</a><a href="/blogs">Blog</a><a href="/contact">Contact</a><a href="https://wa.me/923284675162" target="_blank" style="color:#25D366"><i class="fab fa-whatsapp" style="margin-right:8px"></i>WhatsApp Advisory</a></div>`;

const SIDEBAR = `<aside><div class="consult-card"><h4>Free Consultation</h4><p>Expert reply within 30 minutes</p><a href="https://wa.me/923284675162?text=I+need+tax+consultation" class="wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Now</a></div><div class="sidebar-card"><h4>Our Services</h4><ul class="service-list"><li><i class="fas fa-file-invoice-dollar"></i> Income Tax Return</li><li><i class="fas fa-id-card"></i> NTN Registration</li><li><i class="fas fa-building"></i> <a href="/secp-vs-sole-proprietorship-pakistan" style="color:#0D9488">Company Registration</a></li><li><i class="fas fa-percent"></i> Sales Tax (STRN)</li><li><i class="fas fa-shield-halved"></i> <a href="/fbr-notice-defense" style="color:#0D9488">FBR Notice</a> Response</li></ul></div><div class="sidebar-card"><div class="price-badge"><div class="from">Starting From</div><div class="amount">Rs. 3,500</div><div class="from">Income Tax Return</div></div><a href="/pricing" style="display:block;text-align:center;color:#14B8A6;font-size:.85rem;font-weight:600;margin-top:8px"><i class="fas fa-tags"></i> View All Pricing</a></div></aside>`;

const FOOTER = `<a href="https://wa.me/923284675162" target="_blank" aria-label="WhatsApp" style="position:fixed;bottom:24px;right:24px;z-index:9999;display:flex;align-items:center;justify-content:center;width:58px;height:58px;background:#25D366;border-radius:50%;box-shadow:0 4px 16px rgba(37,211,102,0.5);text-decoration:none"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="30" height="30" fill="#fff"><path d="M16 0C7.163 0 0 7.163 0 16c0 2.822.736 5.476 2.027 7.785L0 32l8.469-2.001A15.93 15.93 0 0016 32c8.837 0 16-7.163 16-16S24.837 0 16 0zm0 29.333a13.27 13.27 0 01-6.77-1.855l-.485-.288-5.024 1.188 1.228-4.893-.317-.502A13.267 13.267 0 012.667 16C2.667 8.636 8.636 2.667 16 2.667S29.333 8.636 29.333 16 23.364 29.333 16 29.333zm7.27-9.862c-.398-.199-2.354-1.162-2.72-1.294-.365-.133-.631-.199-.897.199-.265.398-1.029 1.294-1.261 1.56-.232.265-.465.299-.863.1-.398-.199-1.681-.619-3.202-1.977-1.183-1.057-1.981-2.362-2.213-2.76-.232-.398-.025-.613.175-.811.179-.179.398-.465.597-.698.199-.232.265-.398.398-.664.133-.265.066-.498-.033-.697-.1-.199-.897-2.163-1.229-2.96-.324-.777-.653-.672-.897-.684l-.764-.013c-.265 0-.697.1-1.062.498-.365.398-1.394 1.362-1.394 3.322s1.428 3.853 1.627 4.119c.199.265 2.808 4.287 6.804 6.014.951.411 1.693.656 2.271.84.954.304 1.823.261 2.509.158.765-.114 2.354-.962 2.686-1.891.333-.929.333-1.726.233-1.891-.1-.165-.365-.265-.764-.464z"/></svg></a>
<footer style="background:#0F172A;border-top:1px solid rgba(255,255,255,.06);padding:28px 0;text-align:center"><p style="font-size:.82rem;color:#64748B">&#169; 2026 Kamboh Associates &nbsp;|&nbsp;<a href="/contact" style="color:#14B8A6">Contact</a> &nbsp;|&nbsp;<a href="/pricing" style="color:#14B8A6">Pricing</a> &nbsp;|&nbsp;<a href="/blogs" style="color:#14B8A6">Blog</a></p></footer>
<script>document.querySelectorAll('.faq-q').forEach(q=>q.addEventListener('click',()=>q.parentElement.classList.toggle('open')))</script>
</body></html>`;

// ─── PAGE 1: Income Tax Slab 2026 Blog ───────────────────────────────────────
const slabSchema = JSON.stringify({
  "@context":"https://schema.org","@type":"BlogPosting",
  "headline":"Income Tax Slab Pakistan 2026 — Updated FBR Tax Rates",
  "datePublished":"2026-06-23","dateModified":"2026-06-23",
  "author":{"@type":"Organization","name":"Kamboh Associates","url":"https://kambohassociates.com"},
  "publisher":{"@type":"Organization","name":"Kamboh Associates","url":"https://kambohassociates.com","logo":{"@type":"ImageObject","url":"https://kambohassociates.com/logo.png"}},
  "mainEntityOfPage":{"@type":"WebPage","@id":"https://kambohassociates.com/blogs/income-tax-slab-pakistan-2026"}
});

const slabContent = `
<section class="blog-hero"><div class="container"><nav class="breadcrumb"><a href="/"><i class="fas fa-home"></i> Home</a><i class="fas fa-chevron-right"></i><a href="/blogs">Blog</a><i class="fas fa-chevron-right"></i><span>Income Tax Slab Pakistan 2026</span></nav><div class="blog-cat"><i class="fas fa-percent"></i> Tax Guides</div><h1>Income Tax Slab Pakistan 2026 — Updated FBR Tax Rates for Individuals</h1><div class="blog-meta"><span><i class="fas fa-calendar"></i> June 2026</span><span><i class="fas fa-user"></i> Kamboh Associates</span><span><i class="fas fa-clock"></i> 7 min read</span></div></div></section>
<div class="blog-layout container"><article class="article-body">
<p class="article-lead">FBR's income tax slabs for Tax Year 2026 (July 1, 2025 – June 30, 2026) determine how much income tax you owe on your salary, business income, or other earnings. This guide covers the complete slab table for salaried individuals, business persons, and AOPs — plus how to calculate your actual tax liability.</p>

<h2>Income Tax Slabs for Salaried Individuals — Tax Year 2026</h2>
<p>Salaried taxpayers have separate (more favorable) tax slabs compared to business individuals. These rates apply to salary income as defined under Section 12 of the Income Tax Ordinance 2001:</p>
<table class="data-table">
<tr><th>Annual Taxable Income (Rs.)</th><th>Tax Rate</th><th>Fixed Amount</th></tr>
<tr><td>Up to 600,000</td><td>0%</td><td>Nil</td></tr>
<tr><td>600,001 – 1,200,000</td><td>5%</td><td>Nil + 5% above Rs. 600,000</td></tr>
<tr><td>1,200,001 – 2,200,000</td><td>15%</td><td>Rs. 30,000 + 15% above Rs. 1,200,000</td></tr>
<tr><td>2,200,001 – 3,200,000</td><td>25%</td><td>Rs. 180,000 + 25% above Rs. 2,200,000</td></tr>
<tr><td>3,200,001 – 4,100,000</td><td>30%</td><td>Rs. 430,000 + 30% above Rs. 3,200,000</td></tr>
<tr><td>Above 4,100,000</td><td>35%</td><td>Rs. 700,000 + 35% above Rs. 4,100,000</td></tr>
</table>
<div class="highlight-box"><p><strong>Important:</strong> These slabs apply to <em>taxable income</em> — after deducting allowable expenses, allowances, and deductions. Your gross salary ≠ taxable income.</p></div>

<h2>Income Tax Slabs for Business Individuals &amp; AOPs — Tax Year 2026</h2>
<p>Non-salaried individuals (freelancers, sole proprietors, business owners) and Associations of Persons (AOPs) follow slightly different slabs:</p>
<table class="data-table">
<tr><th>Annual Taxable Income (Rs.)</th><th>Tax Rate</th><th>Fixed Amount</th></tr>
<tr><td>Up to 600,000</td><td>0%</td><td>Nil</td></tr>
<tr><td>600,001 – 1,200,000</td><td>15%</td><td>Nil + 15% above Rs. 600,000</td></tr>
<tr><td>1,200,001 – 1,600,000</td><td>20%</td><td>Rs. 90,000 + 20% above Rs. 1,200,000</td></tr>
<tr><td>1,600,001 – 3,200,000</td><td>30%</td><td>Rs. 170,000 + 30% above Rs. 1,600,000</td></tr>
<tr><td>3,200,001 – 5,600,000</td><td>40%</td><td>Rs. 650,000 + 40% above Rs. 3,200,000</td></tr>
<tr><td>Above 5,600,000</td><td>45%</td><td>Rs. 1,610,000 + 45% above Rs. 5,600,000</td></tr>
</table>

<h2>Corporate Tax Rate — Companies (Tax Year 2026)</h2>
<table class="data-table">
<tr><th>Entity Type</th><th>Tax Rate</th></tr>
<tr><td>Private Limited Company (Pvt. Ltd.)</td><td>29%</td></tr>
<tr><td>Public Listed Company</td><td>29%</td></tr>
<tr><td>Small Company (turnover below Rs. 250M)</td><td>20%</td></tr>
<tr><td>Banking Company</td><td>39%</td></tr>
</table>

<h2>How to Calculate Your Income Tax — Example</h2>
<p>Let's calculate tax for a salaried person with annual income of Rs. 2,500,000:</p>
<table class="data-table">
<tr><th>Step</th><th>Calculation</th><th>Amount (Rs.)</th></tr>
<tr><td>Gross annual salary</td><td>Given</td><td>2,500,000</td></tr>
<tr><td>Less: Medical allowance (10% of basic)</td><td>Deductible</td><td>(100,000)</td></tr>
<tr><td>Taxable income</td><td>2,500,000 – 100,000</td><td>2,400,000</td></tr>
<tr><td>Tax on first Rs. 2,200,000</td><td>Fixed from slab table</td><td>180,000</td></tr>
<tr><td>Tax on Rs. 200,000 (above 2.2M at 25%)</td><td>200,000 × 25%</td><td>50,000</td></tr>
<tr><td><strong>Total Tax Liability</strong></td><td></td><td><strong>230,000</strong></td></tr>
</table>
<div class="highlight-box"><p><strong>Effective rate:</strong> Rs. 230,000 ÷ Rs. 2,500,000 = 9.2%. Even though you fall in the 25% slab, your effective (average) rate is much lower because lower slabs are taxed at lower rates.</p></div>

<h2>Tax-Exempt Income — What is Not Taxable</h2>
<ul>
<li>Agricultural income (exempt under provincial laws)</li>
<li>Gratuity up to Rs. 300,000 (approved gratuity fund)</li>
<li>Provident fund contributions and withdrawals (approved funds)</li>
<li>Scholarships and education grants</li>
<li>Pension income from approved pension funds</li>
<li>Foreign remittances received in Pakistan (salary paid in foreign currency and remitted)</li>
</ul>

<h2>Reducing Your Tax — Legal Deductions</h2>
<table class="data-table">
<tr><th>Deduction</th><th>Section</th><th>Limit</th></tr>
<tr><td>Pension fund / annuity contribution</td><td>63</td><td>20–40% of taxable income (age-based)</td></tr>
<tr><td>Investment in listed shares / mutual funds</td><td>62</td><td>Tax credit 15% on up to Rs. 1.5M</td></tr>
<tr><td>Donation to approved institutions</td><td>61</td><td>30% of taxable income</td></tr>
<tr><td>Medical allowance</td><td>Schedule I</td><td>Up to 10% of basic salary (exempt)</td></tr>
</table>

<h2>Frequently Asked Questions</h2>
<div class="faq-list">
<div class="faq-item"><div class="faq-q">Are income tax slabs the same as last year? <i class="fas fa-chevron-down"></i></div><div class="faq-a">FBR revises slabs every year in the Federal Budget (June). For Tax Year 2026, the salaried slabs shown above are the current applicable rates under the Finance Act 2025-26. Always verify on iris.fbr.gov.pk or with a registered tax consultant before filing.</div></div>
<div class="faq-item"><div class="faq-q">If I have both salary and business income, which slabs apply? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Salary income is taxed under salaried slabs and business income is taxed under business slabs — they are not combined. You declare both separately in your IRIS return. IRIS auto-calculates the correct tax for each type of income.</div></div>
<div class="faq-item"><div class="faq-q">What is the minimum income to file a tax return in Pakistan? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Legally, if your income is below Rs. 600,000 (the zero-tax threshold), you are not required to file. However, filing even a nil return is strongly recommended — it makes you an active filer and saves 50% on WHT rates on property, banking, and vehicles.</div></div>
<div class="faq-item"><div class="faq-q">What tax slab applies to freelancers in Pakistan? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Freelancers are considered "business individuals" and are taxed under the business individual slabs (starting at 15% above Rs. 600,000). However, if freelance income comes from foreign clients remitted to a Pakistani bank, a concessional 1% tax rate may apply under SRO 1006. Consult a tax advisor to determine the most beneficial treatment for your specific situation.</div></div>
</div>

<div class="article-cta" style="background:linear-gradient(135deg,#0F172A,#1E3A5F);border-radius:16px;padding:28px 32px;margin-top:32px;text-align:center">
<h3 style="font-family:'Cormorant Garamond',serif;color:#fff;font-size:1.4rem;margin-bottom:8px">Calculate Your Exact Tax — Free Consultation</h3>
<p style="color:#94A3B8;font-size:.9rem;margin-bottom:18px">WhatsApp your income details. We calculate your exact liability and file your return same day.</p>
<a href="https://wa.me/923284675162?text=I+need+help+with+income+tax+slab+calculation" style="display:inline-flex;align-items:center;gap:8px;background:#25D366;color:#fff;padding:12px 28px;border-radius:100px;font-weight:600;font-size:.92rem"><i class="fab fa-whatsapp"></i> WhatsApp 0328-4675162</a>
</div>
</article>
${SIDEBAR}
</div>`;

fs.writeFileSync(
  path.join(__dirname, 'blogs', 'income-tax-slab-pakistan-2026.html'),
  HEAD('Income Tax Slab Pakistan 2026 — Updated FBR Tax Rates', 'Complete income tax slab table for Pakistan 2026. Salaried individuals, business owners, AOP, and corporate tax rates. Calculate your exact FBR tax liability.', 'income tax slab Pakistan 2026, FBR tax rates 2026, income tax rates Pakistan, tax slab salaried Pakistan 2026', 'https://kambohassociates.com/blogs/income-tax-slab-pakistan-2026', slabSchema) +
  NAV + slabContent + FOOTER,
  'utf8'
);
console.log('OK: blogs/income-tax-slab-pakistan-2026.html');

// ─── PAGE 2: Freelancer Tax Landing Page ─────────────────────────────────────
const freelancerContent = `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Freelancer Tax Filing Pakistan 2026 — FBR Return for Remote Workers</title>
<meta name="description" content="Complete guide to freelancer tax in Pakistan 2026. How to file FBR return, declare foreign income, pay minimum tax on remittances. Kamboh Associates — 0328-4675162."/>
<meta name="keywords" content="freelancer tax Pakistan 2026, FBR tax freelancer Pakistan, freelancer income tax return Pakistan, foreign income tax Pakistan, Upwork Fiverr Toptal tax Pakistan"/>
<link rel="canonical" href="https://kambohassociates.com/freelancer-tax-pakistan"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700&family=DM+Sans:wght@400;500;600&family=Cinzel:wght@600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","name":"Freelancer Tax Filing Pakistan 2026","description":"Complete guide to freelancer income tax filing in Pakistan, including FBR return, foreign remittance tax, and concessional rates.","url":"https://kambohassociates.com/freelancer-tax-pakistan","provider":{"@type":"Organization","name":"Kamboh Associates","telephone":"+923284675162"}}</script>
<meta property="og:type" content="website"/><meta property="og:title" content="Freelancer Tax Pakistan 2026 — Kamboh Associates"/><meta property="og:description" content="How to file your tax return as a Pakistani freelancer earning from Upwork, Fiverr, Toptal, or direct foreign clients. FBR rules, rates, and process explained."/><meta property="og:url" content="https://kambohassociates.com/freelancer-tax-pakistan"/>
<style>:root{--navy:#0F172A;--teal:#14B8A6;--gold:#D4AF37;--font-display:'Cinzel',serif;--font-serif:'Cormorant Garamond',serif;--font-body:'DM Sans',sans-serif;--max-w:1100px}*{box-sizing:border-box;margin:0;padding:0}body{font-family:var(--font-body);background:#fff;color:#0F172A;line-height:1.65;overflow-x:hidden}a{text-decoration:none;color:inherit}.container{max-width:var(--max-w);margin:0 auto;padding:0 24px}.topbar{background:#0F172A;padding:8px 0;text-align:center;font-size:.73rem;color:rgba(148,163,184,.9)}.navbar{position:sticky;top:0;z-index:1000;background:rgba(255,255,255,.97);backdrop-filter:blur(20px);border-bottom:1px solid #E2E8F0}.navbar .container{display:flex;align-items:center;justify-content:space-between;height:68px}.logo-name{font-family:var(--font-display);font-size:.92rem;font-weight:700;letter-spacing:.07em}.logo-sub{font-size:.56rem;letter-spacing:.18em;color:var(--gold);text-transform:uppercase}.nav-cta{background:#0F172A;color:#fff!important;padding:8px 18px;border-radius:8px;font-size:.82rem;font-weight:600}.hero{background:linear-gradient(135deg,#0F172A 0%,#1E3A5F 50%,#0F4C5C 100%);padding:80px 0 64px;text-align:center}.hero-label{display:inline-flex;align-items:center;gap:6px;background:rgba(20,184,166,.15);border:1px solid rgba(20,184,166,.3);border-radius:100px;padding:5px 16px;font-size:.7rem;color:#14B8A6;font-family:var(--font-display);letter-spacing:.12em;text-transform:uppercase;margin-bottom:20px}.hero h1{font-family:var(--font-serif);font-size:clamp(2rem,4.5vw,3.2rem);color:#F1F5F9;line-height:1.15;margin-bottom:18px;max-width:800px;margin-left:auto;margin-right:auto}.hero p{font-size:1.05rem;color:#94A3B8;max-width:600px;margin:0 auto 32px}.hero-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}.btn-teal{display:inline-flex;align-items:center;gap:8px;background:#14B8A6;color:#fff;padding:13px 28px;border-radius:8px;font-weight:600;font-size:.92rem}.btn-wa{display:inline-flex;align-items:center;gap:8px;background:#25D366;color:#fff;padding:13px 28px;border-radius:8px;font-weight:600;font-size:.92rem}.content-section{padding:72px 0}.content-section h2{font-family:var(--font-serif);font-size:1.7rem;color:#0F172A;margin-bottom:16px;display:flex;align-items:center;gap:10px}.content-section h2::before{content:'';width:4px;height:26px;background:linear-gradient(135deg,#14B8A6,#0D9488);border-radius:2px;flex-shrink:0}.content-section p{color:#1E293B;line-height:1.82;margin-bottom:16px;font-size:.96rem}.data-table{width:100%;border-collapse:collapse;margin:16px 0 28px}.data-table th{background:#0F172A;color:#fff;padding:10px 14px;font-size:.84rem;text-align:left}.data-table td{padding:10px 14px;border-bottom:1px solid #E2E8F0;font-size:.88rem}.data-table tr:nth-child(even) td{background:#F8FAFC}.highlight-box{background:rgba(20,184,166,.07);border-left:4px solid #14B8A6;border-radius:0 12px 12px 0;padding:16px 20px;margin:20px 0;font-size:.93rem}.steps-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px;margin:24px 0}.step-card{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:20px}.step-num{width:32px;height:32px;background:#0F172A;border-radius:8px;color:#D4AF37;font-family:var(--font-display);font-size:.8rem;font-weight:700;display:flex;align-items:center;justify-content:center;margin-bottom:10px}.step-card h4{font-size:.9rem;font-weight:600;margin-bottom:6px}.step-card p{font-size:.83rem;color:#64748B;margin:0}.faq-item{border:1px solid #E2E8F0;border-radius:12px;margin-bottom:10px;overflow:hidden}.faq-q{padding:15px 20px;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-size:.92rem;background:#F8FAFC}.faq-q i{transition:transform .3s;color:#14B8A6}.faq-a{display:none;padding:14px 20px;border-top:1px solid #E2E8F0;font-size:.88rem;line-height:1.7}.faq-item.open .faq-a{display:block}.faq-item.open .faq-q i{transform:rotate(180deg)}.cta-section{background:linear-gradient(135deg,#0F172A,#1E3A5F);padding:72px 0;text-align:center}.cta-section h2{font-family:var(--font-serif);color:#fff;font-size:2rem;margin-bottom:12px}.cta-section p{color:#94A3B8;max-width:520px;margin:0 auto 28px;font-size:.95rem}@media(max-width:768px){.hero{padding:56px 0 48px}}</style>
</head><body>
<div class="topbar">FBR TAX CONSULTANTS &bull; 0328-4675162 &bull; 100% ONLINE &bull; SAME DAY FILING &bull; FREELANCER TAX SPECIALISTS</div>
<nav class="navbar"><div class="container"><a href="/" style="display:flex;align-items:center;gap:12px"><svg width="40" height="40" viewBox="0 0 46 46" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1a3a1a"/><stop offset="100%" stop-color="#0d2a0d"/></linearGradient><linearGradient id="g2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#F0CF6B"/><stop offset="100%" stop-color="#D4AF37"/></linearGradient></defs><circle cx="23" cy="23" r="23" fill="url(#g1)"/><circle cx="23" cy="23" r="21" fill="none" stroke="url(#g2)" stroke-width="1.5"/><text x="23" y="27" font-family="Cinzel,serif" font-size="13" font-weight="700" fill="url(#g2)" text-anchor="middle">KA</text></svg><div><div class="logo-name">KAMBOH ASSOCIATES</div><div class="logo-sub">Tax &amp; Regulatory Excellence</div></div></a><a href="https://wa.me/923284675162" class="btn-wa" style="padding:9px 20px;font-size:.84rem"><i class="fab fa-whatsapp"></i> WhatsApp Now</a></div></nav>

<section class="hero">
  <div class="container">
    <div class="hero-label"><i class="fas fa-laptop-code"></i> Freelancer Tax Guide 2026</div>
    <h1>Freelancer Tax Filing in Pakistan — Complete FBR Guide 2026</h1>
    <p>Earning from Upwork, Fiverr, Toptal, or direct foreign clients? Here's everything you need to know about declaring your income and filing your FBR return.</p>
    <div class="hero-btns">
      <a href="https://wa.me/923284675162?text=I+am+a+freelancer+and+need+tax+help" class="btn-wa"><i class="fab fa-whatsapp"></i> File My Return Now</a>
      <a href="/income-tax-filing" class="btn-teal"><i class="fas fa-file-alt"></i> View Tax Services</a>
    </div>
  </div>
</section>

<section class="content-section">
  <div class="container">
    <h2>Do Freelancers Pay Tax in Pakistan?</h2>
    <p>Yes. Freelancers earning from foreign clients are taxable in Pakistan. Income earned by a Pakistani resident (anywhere in the world) must be declared in your annual FBR return. The good news: Pakistan offers <strong>special concessional tax rates for freelancers</strong> to encourage the digital economy.</p>
    <div class="highlight-box">FBR's SRO 1006(I)/2021 grants a <strong>1% minimum tax</strong> on foreign remittances received through banking channels by freelancers — instead of the normal 15–35% income tax slab rates. This is one of the most favorable tax treatments available.</div>

    <h2>Freelancer Tax Rates — 2026</h2>
    <table class="data-table">
      <tr><th>Income Type</th><th>Tax Rate</th><th>Condition</th></tr>
      <tr><td>Foreign remittances (through bank)</td><td>1% minimum tax</td><td>Registered with PSEB / freelance platform + bank receipt</td></tr>
      <tr><td>Local clients (PKR income)</td><td>Normal business slabs (0–45%)</td><td>Standard tax treatment</td></tr>
      <tr><td>Salary from foreign company (employed)</td><td>Salaried slabs (0–35%)</td><td>If you receive salary as employee</td></tr>
      <tr><td>Services to foreign companies (B2B)</td><td>0% sales tax (zero-rated)</td><td>Exported IT services under SRO 1012</td></tr>
    </table>

    <h2>How to File Your Tax Return as a Freelancer</h2>
    <div class="steps-grid">
      <div class="step-card"><div class="step-num">1</div><h4>Get NTN</h4><p>Register on IRIS (iris.fbr.gov.pk) with CNIC + mobile. NTN is issued instantly.</p></div>
      <div class="step-card"><div class="step-num">2</div><h4>Collect Bank Statements</h4><p>Download full year statement showing all Wise, Payoneer, or bank transfers from foreign clients.</p></div>
      <div class="step-card"><div class="step-num">3</div><h4>Calculate Gross Receipts</h4><p>Add up all foreign remittances received between July 1 – June 30. This is your gross income for the year.</p></div>
      <div class="step-card"><div class="step-num">4</div><h4>File Return on IRIS</h4><p>Login → Declaration → 114(I) → Income from Business → Enter gross receipts. Apply 1% minimum tax if eligible.</p></div>
      <div class="step-card"><div class="step-num">5</div><h4>File Wealth Statement</h4><p>Declare all assets (cash, property, vehicles) and liabilities (loans) as of June 30.</p></div>
      <div class="step-card"><div class="step-num">6</div><h4>Pay &amp; Submit</h4><p>Pay tax via PSID (generated in IRIS) through any bank. Then submit return and download acknowledgment.</p></div>
    </div>

    <h2>Wise / Payoneer — Are These Taxable?</h2>
    <p>Yes. Income received via Wise, Payoneer, or direct bank wire from a foreign client is all taxable. The key question is <em>how</em> it is taxed:</p>
    <table class="data-table">
      <tr><th>Platform</th><th>Tax Treatment</th><th>What to Declare</th></tr>
      <tr><td>Wise (remitted to PK bank)</td><td>1% minimum tax (if PSEB registered)</td><td>Total PKR equivalent received</td></tr>
      <tr><td>Payoneer (withdrawn to PK bank)</td><td>1% minimum tax</td><td>Amount withdrawn to Pakistan</td></tr>
      <tr><td>Payoneer (kept in USD, not withdrawn)</td><td>Declare in wealth statement as foreign asset</td><td>USD balance at June 30</td></tr>
      <tr><td>Upwork / Fiverr (via Payoneer)</td><td>1% on PKR value received</td><td>Annual withdrawal total</td></tr>
    </table>

    <h2>PSEB Registration — Do You Need It?</h2>
    <p>PSEB (Pakistan Software Export Board) registration is required to claim the 1% concessional tax rate. Without PSEB registration, you may be taxed at normal business income slab rates (up to 45%).</p>
    <ul style="margin:12px 0 16px 20px;display:flex;flex-direction:column;gap:6px">
      <li style="list-style:disc;font-size:.94rem;color:#1E293B">Register free at pseb.org.pk as an individual IT service exporter</li>
      <li style="list-style:disc;font-size:.94rem;color:#1E293B">Submit your CNIC, bank statement showing foreign remittances, and service description</li>
      <li style="list-style:disc;font-size:.94rem;color:#1E293B">Approval takes 2–4 weeks — apply early in the tax year</li>
      <li style="list-style:disc;font-size:.94rem;color:#1E293B">PSEB certificate attached to your tax return supports the 1% rate claim</li>
    </ul>

    <h2>Frequently Asked Questions</h2>
    <div class="faq-list">
      <div class="faq-item"><div class="faq-q">I earn from Fiverr. Do I need to file a tax return? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes. If you earn from any foreign platform and receive payment in Pakistan (bank or Payoneer/Wise), you must file a tax return. Even if your total income is below the taxable threshold, filing a nil or low-tax return maintains your active filer status which saves money on many daily transactions.</div></div>
      <div class="faq-item"><div class="faq-q">What if I never filed before — can I start now? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Yes. You can file for Tax Year 2026 (July 2025 – June 2026) and also retroactively for up to 5 previous years. Many freelancers regularize their tax position in one session. Kamboh Associates handles this process completely — WhatsApp us with your bank statements and we take care of the rest.</div></div>
      <div class="faq-item"><div class="faq-q">Do I need to pay GST / Sales Tax on my freelance services? <i class="fas fa-chevron-down"></i></div><div class="faq-a">No. IT services exported to foreign clients are zero-rated for Sales Tax under SRO 1012. This means no GST is charged on your invoices to foreign clients. You may register for STRN voluntarily for documentation purposes but you do not need to collect GST from your foreign clients.</div></div>
      <div class="faq-item"><div class="faq-q">I earn from local clients in PKR as well. How does that affect my tax? <i class="fas fa-chevron-down"></i></div><div class="faq-a">Local PKR income is taxed under normal business slabs (starting at 15% above Rs. 600,000). You declare foreign and local income separately in your IRIS return. The 1% concessional rate only applies to foreign remittances — local income follows standard rates.</div></div>
    </div>
  </div>
</section>

<section class="cta-section">
  <div class="container">
    <h2>Freelancer Tax Filing — Done for You</h2>
    <p>Send your bank statement on WhatsApp. We handle NTN, PSEB guidance, IRIS filing, and wealth statement. Most freelancer returns filed same day.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <a href="https://wa.me/923284675162?text=I+am+a+freelancer+and+need+tax+filing+help" class="btn-wa"><i class="fab fa-whatsapp"></i> WhatsApp 0328-4675162</a>
      <a href="/pricing" class="btn-teal"><i class="fas fa-tags"></i> View Pricing</a>
    </div>
  </div>
</section>

<a href="https://wa.me/923284675162" target="_blank" style="position:fixed;bottom:24px;right:24px;z-index:9999;display:flex;align-items:center;justify-content:center;width:58px;height:58px;background:#25D366;border-radius:50%;box-shadow:0 4px 16px rgba(37,211,102,0.5)"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="30" height="30" fill="#fff"><path d="M16 0C7.163 0 0 7.163 0 16c0 2.822.736 5.476 2.027 7.785L0 32l8.469-2.001A15.93 15.93 0 0016 32c8.837 0 16-7.163 16-16S24.837 0 16 0zm0 29.333a13.27 13.27 0 01-6.77-1.855l-.485-.288-5.024 1.188 1.228-4.893-.317-.502A13.267 13.267 0 012.667 16C2.667 8.636 8.636 2.667 16 2.667S29.333 8.636 29.333 16 23.364 29.333 16 29.333zm7.27-9.862c-.398-.199-2.354-1.162-2.72-1.294-.365-.133-.631-.199-.897.199-.265.398-1.029 1.294-1.261 1.56-.232.265-.465.299-.863.1-.398-.199-1.681-.619-3.202-1.977-1.183-1.057-1.981-2.362-2.213-2.76-.232-.398-.025-.613.175-.811.179-.179.398-.465.597-.698.199-.232.265-.398.398-.664.133-.265.066-.498-.033-.697-.1-.199-.897-2.163-1.229-2.96-.324-.777-.653-.672-.897-.684l-.764-.013c-.265 0-.697.1-1.062.498-.365.398-1.394 1.362-1.394 3.322s1.428 3.853 1.627 4.119c.199.265 2.808 4.287 6.804 6.014.951.411 1.693.656 2.271.84.954.304 1.823.261 2.509.158.765-.114 2.354-.962 2.686-1.891.333-.929.333-1.726.233-1.891-.1-.165-.365-.265-.764-.464z"/></svg></a>
<footer style="background:#0F172A;padding:28px 0;text-align:center"><p style="font-size:.82rem;color:#64748B">&#169; 2026 Kamboh Associates &nbsp;|&nbsp;<a href="/contact" style="color:#14B8A6">Contact</a> &nbsp;|&nbsp;<a href="/pricing" style="color:#14B8A6">Pricing</a> &nbsp;|&nbsp;<a href="/blogs" style="color:#14B8A6">Blog</a></p></footer>
<script>document.querySelectorAll('.faq-q').forEach(q=>q.addEventListener('click',()=>q.parentElement.classList.toggle('open')))</script>
</body></html>`;

fs.writeFileSync(path.join(__dirname, 'freelancer-tax-pakistan.html'), freelancerContent, 'utf8');
console.log('OK: freelancer-tax-pakistan.html');
console.log('\nAll done!');
