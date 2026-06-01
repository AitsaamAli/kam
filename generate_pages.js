const fs = require('fs');

// ─── SHARED TEMPLATE PARTS ───
const HEAD = (title, desc, slug) => `<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>${title} | Kamboh Associates</title>
<meta name="description" content="${desc}"/>
<link rel="canonical" href="https://kambohassociates.com/${slug}"/>
<meta property="og:title" content="${title} | Kamboh Associates"/>
<meta property="og:description" content="${desc}"/>
<meta property="og:url" content="https://kambohassociates.com/${slug}"/>
<meta property="og:type" content="website"/>
<meta name="geo.region" content="PK-PB"/>
<meta name="geo.placename" content="Lahore, Punjab, Pakistan"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="preconnect" href="https://cdnjs.cloudflare.com"/>
<link href="https://fonts.googleapis.com/css2?display=swap&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=DM+Sans:wght@400;500;600&family=Cinzel:wght@600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-2ZLVR968Y8"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-2ZLVR968Y8');</script>
<style>
:root{--navy:#0F172A;--navy-2:#1E293B;--teal:#14B8A6;--teal-mid:#0D9488;--teal-pale:#F0FDFA;--gold:#B8960C;--gold-light:#D4AF37;--gold-pale:#FFFBEE;--green:#10B981;--red:#EF4444;--font-display:'Cinzel',serif;--font-serif:'Cormorant Garamond',Georgia,serif;--font-body:'DM Sans',system-ui,sans-serif;--max-w:1200px;--ease:cubic-bezier(0.4,0,0.2,1);--radius:12px;--radius-lg:20px;}
[data-theme="light"]{--bg:#FFFFFF;--bg-2:#F8FAFC;--bg-3:#F1F5F9;--surface:#FFFFFF;--border:#E2E8F0;--border-teal:rgba(20,184,166,.2);--text:#0F172A;--text-2:#1E293B;--text-3:#64748B;--text-4:#94A3B8;--topbar-bg:#0F172A;--nav-bg:rgba(255,255,255,.97);--shadow:0 1px 3px rgba(15,23,42,.08),0 4px 16px rgba(15,23,42,.06);--shadow-lg:0 8px 32px rgba(15,23,42,.10);--teal-bg:rgba(20,184,166,.07);--gold-bg:rgba(212,175,55,.06);}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;font-size:16px}
body{font-family:var(--font-body);background:var(--bg);color:var(--text);line-height:1.65;overflow-x:hidden}
a{text-decoration:none;color:inherit}
img{max-width:100%;display:block}
ul{list-style:none}
::-webkit-scrollbar{width:5px}::-webkit-scrollbar-thumb{background:#14B8A6;border-radius:4px}
.container{max-width:var(--max-w);margin:0 auto;padding:0 24px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 26px;border-radius:8px;font-family:var(--font-body);font-size:.855rem;font-weight:500;cursor:pointer;border:none;transition:all .25s var(--ease);white-space:nowrap}
.btn-teal{background:#14B8A6;color:#fff;box-shadow:0 4px 16px rgba(20,184,166,.3)}
.btn-teal:hover{transform:translateY(-2px);background:#0D9488}
.btn-navy{background:#0F172A;color:#fff;box-shadow:0 4px 16px rgba(15,23,42,.2)}
.btn-navy:hover{transform:translateY(-2px);background:#1E293B}
.btn-outline{background:transparent;border:1.5px solid #0F172A;color:#0F172A}
.btn-outline:hover{background:#0F172A;color:#fff;transform:translateY(-2px)}
/* TOPBAR */
.topbar{background:#0F172A;border-bottom:1px solid rgba(255,255,255,.06);padding:8px 0;font-size:.75rem}
.topbar .container{display:flex;justify-content:center}
.topbar-promo-wrap{display:inline-flex;animation:kascroll 28s linear infinite;overflow:hidden}
.topbar-promo{font-family:var(--font-body);font-size:.73rem;color:rgba(148,163,184,.9);white-space:nowrap;flex-shrink:0;padding:0 20px}
@keyframes kascroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
/* NAVBAR */
.navbar{position:sticky;top:0;z-index:1000;background:rgba(255,255,255,.97);backdrop-filter:blur(24px);border-bottom:1px solid #E2E8F0;transition:box-shadow .3s}
.navbar.scrolled{box-shadow:0 4px 24px rgba(15,23,42,.08);border-bottom-color:rgba(20,184,166,.25)}
.navbar .container{display:flex;align-items:center;justify-content:space-between;height:68px}
.logo{display:flex;align-items:center;gap:12px}
.logo-name{font-family:var(--font-display);font-size:.92rem;font-weight:700;color:var(--text);letter-spacing:.07em;line-height:1.2}
.logo-sub{font-size:.56rem;letter-spacing:.18em;color:#D4AF37;text-transform:uppercase}
.nav-links{display:flex;align-items:center;gap:4px}
.nav-links>li{position:relative;list-style:none}
.nav-links>li>a{font-size:.84rem;font-weight:500;color:#1E293B;display:flex;align-items:center;gap:4px;padding:8px 14px;border-radius:8px;transition:all .2s}
.nav-links>li>a:hover{color:#14B8A6;background:#F0FDFA}
.nav-links>li>a.active{color:#14B8A6}
.nav-drop{position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%) translateY(-6px);min-width:220px;background:#fff;border:1px solid #E2E8F0;border-radius:12px;box-shadow:0 8px 32px rgba(15,23,42,.12);padding:8px;opacity:0;visibility:hidden;pointer-events:none;transition:all .2s}
.nav-links>li:hover .nav-drop{opacity:1;visibility:visible;pointer-events:auto;transform:translateX(-50%) translateY(0)}
.nav-drop a{display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:8px;font-size:.82rem;color:#1E293B;transition:all .15s}
.nav-drop a:hover{background:#F0FDFA;color:#14B8A6}
.nav-drop a i{width:16px;text-align:center;color:#14B8A6;font-size:.78rem}
.nav-drop-divider{height:1px;background:#E2E8F0;margin:4px 8px}
.nav-actions{display:flex;align-items:center;gap:10px}
.nav-phone{font-size:.8rem;display:flex;align-items:center;gap:6px}
.nav-phone i{color:#14B8A6}
.nav-phone a{color:#1E293B;font-weight:500;transition:color .2s}
.nav-phone a:hover{color:#14B8A6}
.nav-cta{background:#0F172A;color:#fff!important;padding:8px 18px!important;border-radius:8px!important;font-size:.82rem!important;font-weight:600!important;transition:all .2s!important}
.nav-cta:hover{background:#14B8A6!important}
.hamburger{display:none;flex-direction:column;gap:6px;cursor:pointer;padding:6px;background:none;border:none;width:40px;height:40px;justify-content:center;align-items:center;border-radius:8px}
.hamburger span{width:24px;height:2.5px;background:#0F172A;border-radius:3px;transition:all .35s;display:block}
.hamburger.open span:nth-child(1){transform:rotate(45deg) translate(0,8.5px)}
.hamburger.open span:nth-child(2){opacity:0}
.hamburger.open span:nth-child(3){transform:rotate(-45deg) translate(0,-8.5px)}
.mobile-nav{display:none;flex-direction:column;background:#fff;border-bottom:2px solid rgba(20,184,166,.2);box-shadow:0 8px 32px rgba(15,23,42,.1)}
.mobile-nav.open{display:flex}
.mobile-nav a{padding:14px 24px;border-bottom:1px solid #E2E8F0;font-size:.9rem;color:#64748B;transition:all .2s}
.mobile-nav a:hover{color:#14B8A6;background:#F0FDFA;padding-left:32px}
/* PAGE HERO */
.page-hero{background:linear-gradient(135deg,#0F172A 0%,#1E293B 60%,#0F766E 100%);padding:80px 0 70px;color:#fff}
.page-hero .eyebrow{font-family:var(--font-display);font-size:.58rem;letter-spacing:.3em;text-transform:uppercase;color:#14B8A6;display:block;margin-bottom:14px}
.page-hero h1{font-family:var(--font-serif);font-size:clamp(2rem,4vw,3.2rem);font-weight:700;line-height:1.1;margin-bottom:18px}
.page-hero p{font-size:1rem;color:rgba(255,255,255,.7);max-width:560px;line-height:1.8;margin-bottom:32px}
.page-hero .hero-btns{display:flex;gap:12px;flex-wrap:wrap}
/* SECTIONS */
.section{padding:80px 0}
.section-alt{padding:80px 0;background:#F8FAFC}
.section-teal{padding:80px 0;background:linear-gradient(135deg,#0F172A,#0F766E);color:#fff}
.eyebrow-sm{font-family:var(--font-display);font-size:.58rem;letter-spacing:.3em;text-transform:uppercase;color:#14B8A6;display:block;margin-bottom:10px}
.section-title{font-family:var(--font-serif);font-size:clamp(1.8rem,3vw,2.6rem);font-weight:700;line-height:1.15;color:#0F172A;margin-bottom:14px}
.section-title.light{color:#fff}
.section-sub{font-size:.95rem;color:#64748B;line-height:1.8;max-width:520px}
/* CARDS */
.cards-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px}
.card{background:#fff;border:1px solid #E2E8F0;border-radius:var(--radius-lg);padding:28px;transition:all .3s;position:relative}
.card:hover{box-shadow:var(--shadow-lg);transform:translateY(-4px);border-color:rgba(20,184,166,.3)}
.card-icon{width:48px;height:48px;background:#F0FDFA;border:1px solid rgba(20,184,166,.2);border-radius:12px;display:flex;align-items:center;justify-content:center;color:#14B8A6;font-size:1.1rem;margin-bottom:18px}
.card h3{font-family:var(--font-serif);font-size:1.15rem;font-weight:700;color:#0F172A;margin-bottom:8px}
.card p{font-size:.88rem;color:#64748B;line-height:1.7}
/* STEPS */
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:48px;position:relative}
.steps::before{content:'';position:absolute;top:28px;left:10%;right:10%;height:2px;background:linear-gradient(90deg,#14B8A6,rgba(20,184,166,.1));z-index:0}
.step{text-align:center;position:relative;z-index:1}
.step-num{width:56px;height:56px;background:linear-gradient(135deg,#14B8A6,#0D9488);border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:var(--font-display);font-size:1rem;font-weight:700;color:#fff;margin:0 auto 16px;box-shadow:0 4px 16px rgba(20,184,166,.35)}
.step h4{font-family:var(--font-serif);font-size:1rem;font-weight:700;color:#0F172A;margin-bottom:6px}
.step p{font-size:.82rem;color:#64748B;line-height:1.6}
/* PRICING */
.pricing-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px}
.price-card{background:#fff;border:2px solid #E2E8F0;border-radius:var(--radius-lg);padding:32px;text-align:center;transition:all .3s;position:relative}
.price-card.featured{border-color:#14B8A6;box-shadow:0 8px 32px rgba(20,184,166,.15)}
.price-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:#14B8A6;color:#fff;font-size:.7rem;font-weight:600;padding:4px 16px;border-radius:100px;letter-spacing:.05em;text-transform:uppercase}
.price-card h3{font-family:var(--font-serif);font-size:1.2rem;font-weight:700;color:#0F172A;margin-bottom:6px}
.price-card .price{font-family:var(--font-serif);font-size:2.4rem;font-weight:700;color:#14B8A6;margin:16px 0}
.price-card .price span{font-size:.9rem;color:#64748B;font-family:var(--font-body)}
.price-card ul{text-align:left;margin:20px 0;display:flex;flex-direction:column;gap:10px}
.price-card ul li{font-size:.85rem;color:#334155;display:flex;align-items:center;gap:8px}
.price-card ul li::before{content:'\f00c';font-family:'Font Awesome 6 Free';font-weight:900;color:#14B8A6;font-size:.75rem;flex-shrink:0}
/* FAQ */
.faq-list{margin-top:40px;display:flex;flex-direction:column;gap:12px}
.faq-item{background:#fff;border:1px solid #E2E8F0;border-radius:var(--radius);overflow:hidden;transition:all .2s}
.faq-item.open{border-color:rgba(20,184,166,.3)}
.faq-q{display:flex;align-items:center;justify-content:space-between;padding:18px 22px;cursor:pointer;font-weight:500;color:#0F172A;gap:16px}
.faq-q i{color:#14B8A6;transition:transform .3s;flex-shrink:0}
.faq-item.open .faq-q i{transform:rotate(180deg)}
.faq-a{max-height:0;overflow:hidden;transition:max-height .4s ease,padding .3s}
.faq-a-inner{padding:0 22px 18px;font-size:.9rem;color:#475569;line-height:1.8}
.faq-item.open .faq-a{max-height:300px}
/* DOCS LIST */
.docs-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:32px}
.doc-item{display:flex;align-items:flex-start;gap:12px;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:var(--radius);padding:14px 18px}
.doc-item i{color:#14B8A6;margin-top:2px;flex-shrink:0}
.doc-item span{font-size:.88rem;color:#334155;line-height:1.5}
/* CTA STRIP */
.cta-strip{background:linear-gradient(135deg,#0F172A,#0F766E);padding:64px 0;text-align:center;color:#fff}
.cta-strip h2{font-family:var(--font-serif);font-size:clamp(1.8rem,3vw,2.6rem);font-weight:700;margin-bottom:12px}
.cta-strip p{color:rgba(255,255,255,.7);margin-bottom:32px;font-size:.95rem}
.cta-strip .btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
/* RELATED LINKS */
.related-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:40px}
.related-card{display:flex;align-items:center;gap:14px;background:#fff;border:1px solid #E2E8F0;border-radius:var(--radius);padding:18px 20px;transition:all .2s}
.related-card:hover{border-color:rgba(20,184,166,.3);background:#F0FDFA;transform:translateX(4px)}
.related-card i{color:#14B8A6;font-size:1.1rem;flex-shrink:0}
.related-card span{font-size:.88rem;color:#1E293B;font-weight:500}
/* FOOTER */
footer{background:#0F172A;color:rgba(255,255,255,.65);padding:60px 0 0}
.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:48px;padding-bottom:48px}
.footer-logo-name{font-family:var(--font-display);font-size:.9rem;color:#D4AF37;letter-spacing:.1em;margin-bottom:10px}
.footer-desc{font-size:.82rem;line-height:1.8;color:rgba(255,255,255,.5);margin-bottom:20px}
.footer-head{font-family:var(--font-display);font-size:.6rem;letter-spacing:.24em;text-transform:uppercase;color:#14B8A6;margin-bottom:16px}
.footer-links li{margin-bottom:10px}
.footer-links a{font-size:.82rem;color:rgba(255,255,255,.55);transition:color .2s}
.footer-links a:hover{color:#14B8A6}
.footer-bottom{border-top:1px solid rgba(255,255,255,.08);padding:20px 0;display:flex;justify-content:space-between;font-size:.75rem;color:rgba(255,255,255,.35)}
/* WA BUTTON */
.wa-btn{position:fixed;bottom:28px;right:28px;width:56px;height:56px;background:#25D366;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.4rem;box-shadow:0 4px 20px rgba(37,211,102,.45);z-index:999;transition:transform .3s}
.wa-btn:hover{transform:scale(1.1)}
/* CALCULATOR SPECIFIC */
.calc-card{background:#fff;border:1px solid #E2E8F0;border-radius:var(--radius-lg);padding:36px;box-shadow:var(--shadow)}
.calc-input{width:100%;padding:12px 16px;border:1.5px solid #E2E8F0;border-radius:8px;font-family:var(--font-body);font-size:.9rem;color:#0F172A;background:#F8FAFC;transition:border .2s;outline:none;margin-top:6px}
.calc-input:focus{border-color:#14B8A6;background:#fff}
.calc-label{font-size:.82rem;font-weight:600;color:#334155;letter-spacing:.02em}
.calc-field{margin-bottom:20px}
.calc-btn{width:100%;padding:14px;background:#14B8A6;color:#fff;border:none;border-radius:8px;font-size:.9rem;font-weight:600;cursor:pointer;transition:all .2s;margin-top:8px}
.calc-btn:hover{background:#0D9488;transform:translateY(-1px)}
.calc-result{background:#F0FDFA;border:1.5px solid rgba(20,184,166,.25);border-radius:12px;padding:24px;margin-top:24px;display:none}
.calc-result.show{display:block}
.result-row{display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid rgba(20,184,166,.1);font-size:.88rem}
.result-row:last-child{border-bottom:none;font-weight:700;font-size:1rem;color:#0D9488;padding-top:14px}
.result-label{color:#475569}
.result-value{color:#0F172A;font-weight:600}
/* RESPONSIVE */
@media(max-width:768px){
  .nav-links,.nav-phone,.nav-cta{display:none}
  .hamburger{display:flex}
  .cards-grid,.steps,.pricing-grid,.related-grid{grid-template-columns:1fr}
  .docs-grid{grid-template-columns:1fr}
  .footer-grid{grid-template-columns:1fr 1fr}
  .footer-bottom{flex-direction:column;gap:8px;text-align:center}
  .page-hero{padding:56px 0 48px}
  .steps::before{display:none}
}
@media(max-width:480px){
  .footer-grid{grid-template-columns:1fr}
  .pricing-grid{grid-template-columns:1fr}
}
</style>`;

const NAVBAR = () => `
<div class="topbar"><div class="container"><div class="topbar-promo-wrap">
  <span class="topbar-promo">Pakistan's #1 Tax Consultancy Since 2008 &nbsp;•&nbsp; FBR Registered &nbsp;•&nbsp; 5,000+ Clients Served &nbsp;•&nbsp; Same-Day Service Available &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
  <span class="topbar-promo" aria-hidden="true">Pakistan's #1 Tax Consultancy Since 2008 &nbsp;•&nbsp; FBR Registered &nbsp;•&nbsp; 5,000+ Clients Served &nbsp;•&nbsp; Same-Day Service Available &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
</div></div></div>
<nav class="navbar" id="navbar">
  <div class="container">
    <a href="/" class="logo">
      <div>
        <div class="logo-name">KAMBOH ASSOCIATES</div>
        <div class="logo-sub">Tax &amp; Regulatory Excellence</div>
      </div>
    </a>
    <ul class="nav-links">
      <li><a href="/">Home</a></li>
      <li>
        <a href="/#services">Services <i class="fas fa-chevron-down" style="font-size:.6rem;opacity:.6"></i></a>
        <div class="nav-drop">
          <a href="/income-tax-filing"><i class="fas fa-file-invoice-dollar"></i> Income Tax Filing</a>
          <a href="/fbr-ntn-registration-guide"><i class="fas fa-id-card"></i> NTN Registration</a>
          <a href="/sales-tax-registration"><i class="fas fa-percent"></i> Sales Tax Registration</a>
          <a href="/secp-vs-sole-proprietorship-pakistan"><i class="fas fa-building"></i> SECP Registration</a>
          <div class="nav-drop-divider"></div>
          <a href="/business-advisory"><i class="fas fa-chart-line"></i> Business Advisory</a>
        </div>
      </li>
      <li>
        <a href="/#tools">Tools <i class="fas fa-chevron-down" style="font-size:.6rem;opacity:.6"></i></a>
        <div class="nav-drop">
          <a href="/tax-calculator"><i class="fas fa-calculator"></i> Tax Calculator</a>
          <a href="/salary-calculator"><i class="fas fa-user-tie"></i> Salary Calculator</a>
          <a href="/gst-calculator"><i class="fas fa-percent"></i> GST Calculator</a>
          <a href="/income-estimator"><i class="fas fa-chart-bar"></i> Income Estimator</a>
        </div>
      </li>
      <li><a href="/#deadlines">Deadlines</a></li>
      <li>
        <a href="/blogs">Blog <i class="fas fa-chevron-down" style="font-size:.6rem;opacity:.6"></i></a>
        <div class="nav-drop">
          <a href="/blogs"><i class="fas fa-landmark"></i> FBR &amp; Tax Guides</a>
          <a href="/blogs"><i class="fas fa-user-clock"></i> Freelancer Tax</a>
          <a href="/blogs"><i class="fas fa-store"></i> E-Commerce Tax</a>
          <a href="/blogs"><i class="fas fa-building"></i> Business &amp; SECP</a>
        </div>
      </li>
      <li><a href="/#contact">Contact</a></li>
    </ul>
    <div class="nav-actions">
      <span class="nav-phone"><i class="fas fa-phone"></i><a href="tel:03284675162">0328-4675162</a></span>
      <a href="/#contact" class="nav-cta">Get Started</a>
      <button class="hamburger" id="hamburger" onclick="toggleMobileNav()" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
  <div class="mobile-nav" id="mobileNav">
    <a href="/" onclick="closeMobileNav()">Home</a>
    <a href="/income-tax-filing" onclick="closeMobileNav()">Income Tax Filing</a>
    <a href="/fbr-ntn-registration-guide" onclick="closeMobileNav()">NTN Registration</a>
    <a href="/sales-tax-registration" onclick="closeMobileNav()">Sales Tax Registration</a>
    <a href="/secp-vs-sole-proprietorship-pakistan" onclick="closeMobileNav()">SECP Registration</a>
    <a href="/business-advisory" onclick="closeMobileNav()">Business Advisory</a>
    <a href="/tax-calculator" onclick="closeMobileNav()">Tax Calculator</a>
    <a href="/salary-calculator" onclick="closeMobileNav()">Salary Calculator</a>
    <a href="/gst-calculator" onclick="closeMobileNav()">GST Calculator</a>
    <a href="/blogs" onclick="closeMobileNav()">Blog</a>
    <a href="/#contact" onclick="closeMobileNav()">Contact</a>
  </div>
</nav>`;

const FOOTER = () => `
<footer>
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo-name">KAMBOH ASSOCIATES</div>
        <div class="footer-desc">Pakistan's trusted tax consultancy since 2008. Expert FBR income tax return filing, NTN registration, SECP company formation &amp; regulatory compliance.</div>
        <div style="font-size:.8rem;color:rgba(255,255,255,.4)">📍 Lahore, Pakistan &nbsp;|&nbsp; 📞 0328-4675162</div>
      </div>
      <div>
        <div class="footer-head">Services</div>
        <ul class="footer-links">
          <li><a href="/income-tax-filing">Income Tax Filing</a></li>
          <li><a href="/fbr-ntn-registration-guide">NTN Registration</a></li>
          <li><a href="/sales-tax-registration">Sales Tax Registration</a></li>
          <li><a href="/secp-vs-sole-proprietorship-pakistan">SECP Registration</a></li>
          <li><a href="/business-advisory">Business Advisory</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-head">Tools</div>
        <ul class="footer-links">
          <li><a href="/tax-calculator">Tax Calculator</a></li>
          <li><a href="/salary-calculator">Salary Calculator</a></li>
          <li><a href="/gst-calculator">GST Calculator</a></li>
          <li><a href="/income-estimator">Income Estimator</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-head">Resources</div>
        <ul class="footer-links">
          <li><a href="/blogs">All Tax Guides</a></li>
          <li><a href="/filer-vs-nonfiler-pakistan">Filer vs Non-Filer</a></li>
          <li><a href="/freelancer-filer-pakistan">Freelancer Tax</a></li>
          <li><a href="/income-tax-return-pakistan">Who Must File?</a></li>
          <li><a href="/#contact">Contact Us</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Kamboh Associates. All rights reserved.</span>
      <span>FBR Registered | SECP Compliant | Since 2008</span>
    </div>
  </div>
</footer>
<a href="https://wa.me/923284675162" class="wa-btn" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
<script>
function toggleMobileNav(){document.getElementById('hamburger').classList.toggle('open');document.getElementById('mobileNav').classList.toggle('open')}
function closeMobileNav(){document.getElementById('hamburger').classList.remove('open');document.getElementById('mobileNav').classList.remove('open')}
window.addEventListener('scroll',()=>{document.getElementById('navbar').classList.toggle('scrolled',window.scrollY>40)});
document.querySelectorAll('.faq-q').forEach(q=>{q.addEventListener('click',()=>{const item=q.parentElement;item.classList.toggle('open')})});
</script>`;

const RELATED_SERVICES = (exclude) => {
  const links = [
    {href:'/income-tax-filing',icon:'fa-file-invoice-dollar',text:'Income Tax Filing'},
    {href:'/fbr-ntn-registration-guide',icon:'fa-id-card',text:'NTN Registration'},
    {href:'/sales-tax-registration',icon:'fa-percent',text:'Sales Tax Registration'},
    {href:'/secp-vs-sole-proprietorship-pakistan',icon:'fa-building',text:'SECP Registration'},
    {href:'/business-advisory',icon:'fa-chart-line',text:'Business Advisory'},
    {href:'/tax-calculator',icon:'fa-calculator',text:'Tax Calculator'},
    {href:'/salary-calculator',icon:'fa-user-tie',text:'Salary Calculator'},
  ].filter(l => l.href !== exclude);
  return `<div class="related-grid">${links.slice(0,6).map(l=>`<a href="${l.href}" class="related-card"><i class="fas ${l.icon}"></i><span>${l.text}</span></a>`).join('')}</div>`;
};

// ═══════════════════════════════════════════
// PAGE 1: INCOME TAX FILING
// ═══════════════════════════════════════════
fs.writeFileSync('income-tax-filing.html', HEAD(
  'Income Tax Return Filing Pakistan 2025',
  'Professional FBR income tax return filing service in Pakistan. Salaried, freelancer, business owners. Same-day filing by Kamboh Associates Lahore.',
  'income-tax-filing'
) + `</head><body>
${NAVBAR()}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">FBR Registered Service</span>
    <h1>Income Tax Return<br>Filing Pakistan 2025</h1>
    <p>Pakistan's most trusted income tax return filing service. Salaried employees, freelancers, business owners — we file accurately within 24 hours.</p>
    <div class="hero-btns">
      <a href="https://wa.me/923284675162" class="btn btn-teal"><i class="fab fa-whatsapp"></i> File Now — WhatsApp</a>
      <a href="tel:03284675162" class="btn btn-outline" style="border-color:rgba(255,255,255,.4);color:#fff"><i class="fas fa-phone"></i> 0328-4675162</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow-sm">Who Should File</span>
    <h2 class="section-title">Who Must File Income Tax in Pakistan?</h2>
    <p class="section-sub">Under FBR rules, the following persons must file an annual income tax return by September 30.</p>
    <div class="cards-grid">
      <div class="card"><div class="card-icon"><i class="fas fa-user-tie"></i></div><h3>Salaried Employees</h3><p>Any salaried person earning more than PKR 600,000/year must file an income tax return — even if tax is deducted by employer.</p></div>
      <div class="card"><div class="card-icon"><i class="fas fa-laptop-code"></i></div><h3>Freelancers & Digital Workers</h3><p>Fiverr, Upwork, YouTube, TikTok creators and all online earners receiving foreign income must be FBR registered and file annually.</p></div>
      <div class="card"><div class="card-icon"><i class="fas fa-store"></i></div><h3>Business Owners</h3><p>Sole proprietors, AOP members, e-commerce sellers (Amazon, Shopify) and all business income earners must file income tax return.</p></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <span class="eyebrow-sm">Our Process</span>
    <h2 class="section-title">How We File Your Tax Return</h2>
    <p class="section-sub">Simple 5-step process. No office visit required. 100% remote service across Pakistan.</p>
    <div class="steps">
      <div class="step"><div class="step-num">1</div><h4>Send Documents</h4><p>WhatsApp your CNIC, salary slips or bank statement</p></div>
      <div class="step"><div class="step-num">2</div><h4>We Prepare</h4><p>Our team prepares your complete tax return</p></div>
      <div class="step"><div class="step-num">3</div><h4>Your Approval</h4><p>We send you a preview for review and approval</p></div>
      <div class="step"><div class="step-num">4</div><h4>We File</h4><p>Filed directly on FBR Iris portal same day</p></div>
      <div class="step"><div class="step-num">5</div><h4>Acknowledgment</h4><p>You receive official FBR acknowledgment receipt</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow-sm">Documents Required</span>
    <h2 class="section-title">What Documents Do You Need?</h2>
    <div class="docs-grid">
      <div class="doc-item"><i class="fas fa-id-card"></i><span>CNIC copy (front & back)</span></div>
      <div class="doc-item"><i class="fas fa-file-alt"></i><span>Salary slips (last 12 months) — for salaried</span></div>
      <div class="doc-item"><i class="fas fa-university"></i><span>Bank statement (July–June)</span></div>
      <div class="doc-item"><i class="fas fa-home"></i><span>Property details (if any owned)</span></div>
      <div class="doc-item"><i class="fas fa-car"></i><span>Vehicle registration details</span></div>
      <div class="doc-item"><i class="fas fa-money-bill-wave"></i><span>Business income records (for business owners)</span></div>
      <div class="doc-item"><i class="fas fa-globe"></i><span>Foreign income proof (for freelancers)</span></div>
      <div class="doc-item"><i class="fas fa-piggy-bank"></i><span>Investment details (NSS, shares, mutual funds)</span></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <span class="eyebrow-sm">Transparent Pricing</span>
    <h2 class="section-title">Tax Filing Packages 2025</h2>
    <div class="pricing-grid">
      <div class="price-card">
        <h3>Salaried Basic</h3>
        <div class="price">PKR 2,500 <span>/ return</span></div>
        <ul>
          <li>Single salary income</li>
          <li>Wealth statement included</li>
          <li>FBR Iris filing</li>
          <li>Acknowledgment receipt</li>
          <li>ATL status update</li>
        </ul>
        <a href="https://wa.me/923284675162" class="btn btn-teal" style="width:100%;justify-content:center">Get Started</a>
      </div>
      <div class="price-card featured">
        <div class="price-badge">Most Popular</div>
        <h3>Professional</h3>
        <div class="price">PKR 4,500 <span>/ return</span></div>
        <ul>
          <li>Multiple income sources</li>
          <li>Business or freelance income</li>
          <li>Wealth statement included</li>
          <li>Tax planning advice</li>
          <li>Priority 24-hour service</li>
        </ul>
        <a href="https://wa.me/923284675162" class="btn btn-teal" style="width:100%;justify-content:center">Get Started</a>
      </div>
      <div class="price-card">
        <h3>Business / AOP</h3>
        <div class="price">PKR 8,000 <span>+</span></div>
        <ul>
          <li>Business accounts filing</li>
          <li>AOP / partnership returns</li>
          <li>Withholding statements</li>
          <li>Full compliance review</li>
          <li>FBR notice handling</li>
        </ul>
        <a href="https://wa.me/923284675162" class="btn btn-teal" style="width:100%;justify-content:center">Get Quote</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:760px">
    <span class="eyebrow-sm">FAQ</span>
    <h2 class="section-title">Frequently Asked Questions</h2>
    <div class="faq-list">
      <div class="faq-item"><div class="faq-q">What is the FBR income tax deadline for 2025?<i class="fas fa-chevron-down"></i></div><div class="faq-a"><div class="faq-a-inner">The FBR income tax return deadline for individuals and AOPs is September 30, 2025 (for Tax Year 2025). For companies, it is December 31, 2025. Late filing attracts a PKR 1,000/month penalty and removal from the Active Taxpayer List.</div></div></div>
      <div class="faq-item"><div class="faq-q">Do I need NTN before filing a tax return?<i class="fas fa-chevron-down"></i></div><div class="faq-a"><div class="faq-a-inner">Yes. You need an active NTN registered on FBR Iris before you can file an income tax return. Kamboh Associates can register your NTN same day and then immediately file your return.</div></div></div>
      <div class="faq-item"><div class="faq-q">Can you file my return remotely from any city?<i class="fas fa-chevron-down"></i></div><div class="faq-a"><div class="faq-a-inner">Yes. We provide fully remote income tax return filing for clients in Lahore, Karachi, Islamabad, Faisalabad, Rawalpindi, Multan, and all cities across Pakistan. Send documents on WhatsApp — receive FBR acknowledgment same day.</div></div></div>
      <div class="faq-item"><div class="faq-q">What is a wealth statement and do I need to file it?<i class="fas fa-chevron-down"></i></div><div class="faq-a"><div class="faq-a-inner">Yes. A Wealth Statement (assets & liabilities declaration) is mandatory for every person filing an income tax return in Pakistan. It includes your property, vehicles, bank accounts, cash, jewelry, and investments. Kamboh Associates prepares and files your wealth statement as part of the return.</div></div></div>
      <div class="faq-item"><div class="faq-q">What are the benefits of being a tax filer?<i class="fas fa-chevron-down"></i></div><div class="faq-a"><div class="faq-a-inner">As an active filer, you pay significantly lower withholding tax on banking transactions, property purchases, vehicle registration, and prize money. Non-filers pay 2-4x more tax on these transactions. Filing also protects you from FBR notices and penalties.</div></div></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <span class="eyebrow-sm">Related Services</span>
    <h2 class="section-title">Explore More Services & Tools</h2>
    ${RELATED_SERVICES('/income-tax-filing')}
  </div>
</section>

<section class="cta-strip">
  <div class="container">
    <h2>File Your Income Tax Return Today</h2>
    <p>Don't miss the September 30 deadline. Get your return filed in 24 hours.</p>
    <div class="btns">
      <a href="https://wa.me/923284675162" class="btn btn-teal"><i class="fab fa-whatsapp"></i> WhatsApp Now</a>
      <a href="tel:03284675162" class="btn btn-outline" style="border-color:rgba(255,255,255,.35);color:#fff"><i class="fas fa-phone"></i> Call 0328-4675162</a>
    </div>
  </div>
</section>
${FOOTER()}
</body></html>`);

// ═══════════════════════════════════════════
// PAGE 2: SALES TAX REGISTRATION
// ═══════════════════════════════════════════
fs.writeFileSync('sales-tax-registration.html', HEAD(
  'Sales Tax STRN Registration Pakistan 2025',
  'FBR Sales Tax Registration Number (STRN) registration service in Pakistan. Get your GST number registered by Kamboh Associates Lahore.',
  'sales-tax-registration'
) + `</head><body>
${NAVBAR()}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">FBR Sales Tax Service</span>
    <h1>Sales Tax (STRN)<br>Registration Pakistan 2025</h1>
    <p>Get your FBR Sales Tax Registration Number (STRN) quickly and correctly. Required for all businesses supplying taxable goods or services in Pakistan.</p>
    <div class="hero-btns">
      <a href="https://wa.me/923284675162" class="btn btn-teal"><i class="fab fa-whatsapp"></i> Register Now</a>
      <a href="tel:03284675162" class="btn btn-outline" style="border-color:rgba(255,255,255,.4);color:#fff"><i class="fas fa-phone"></i> 0328-4675162</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow-sm">Who Needs STRN</span>
    <h2 class="section-title">Who Must Register for Sales Tax?</h2>
    <div class="cards-grid">
      <div class="card"><div class="card-icon"><i class="fas fa-industry"></i></div><h3>Manufacturers</h3><p>Any business manufacturing taxable goods must register for sales tax with FBR, regardless of turnover.</p></div>
      <div class="card"><div class="card-icon"><i class="fas fa-store"></i></div><h3>Retailers & Wholesalers</h3><p>Registered retailers and tier-1 retailers must register for sales tax under FBR's retail tax scheme.</p></div>
      <div class="card"><div class="card-icon"><i class="fas fa-laptop"></i></div><h3>Service Providers</h3><p>IT, digital marketing agencies, e-commerce platforms, and various service businesses may require STRN for B2B contracts.</p></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <span class="eyebrow-sm">Process</span>
    <h2 class="section-title">STRN Registration Process</h2>
    <div class="steps">
      <div class="step"><div class="step-num">1</div><h4>NTN Required</h4><p>Active NTN must exist before STRN registration</p></div>
      <div class="step"><div class="step-num">2</div><h4>Documents</h4><p>Gather CNIC, business proof, address documents</p></div>
      <div class="step"><div class="step-num">3</div><h4>FBR Application</h4><p>We apply on FBR's IRIS portal for STRN</p></div>
      <div class="step"><div class="step-num">4</div><h4>Verification</h4><p>FBR verifies and issues STRN certificate</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow-sm">Documents Required</span>
    <h2 class="section-title">Required Documents for STRN</h2>
    <div class="docs-grid">
      <div class="doc-item"><i class="fas fa-id-card"></i><span>CNIC of business owner / directors</span></div>
      <div class="doc-item"><i class="fas fa-file-alt"></i><span>Active NTN registration certificate</span></div>
      <div class="doc-item"><i class="fas fa-map-marker-alt"></i><span>Business address proof (utility bill / lease)</span></div>
      <div class="doc-item"><i class="fas fa-building"></i><span>SECP registration (if private limited company)</span></div>
      <div class="doc-item"><i class="fas fa-university"></i><span>Business bank account details</span></div>
      <div class="doc-item"><i class="fas fa-file-invoice"></i><span>Nature of business / products description</span></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <h2 class="section-title">Monthly STRN Filing Obligations</h2>
    <p class="section-sub">Once registered, STRN holders must file monthly sales tax returns. Missing returns attract penalties.</p>
    <div class="cards-grid" style="margin-top:32px">
      <div class="card"><div class="card-icon"><i class="fas fa-calendar-alt"></i></div><h3>Monthly Return</h3><p>Sales tax return must be filed by the 15th of each month for the previous month's transactions.</p></div>
      <div class="card"><div class="card-icon"><i class="fas fa-file-invoice-dollar"></i></div><h3>Tax Payment</h3><p>Sales tax collected from customers must be deposited with FBR minus input tax adjustments (purchases).</p></div>
      <div class="card"><div class="card-icon"><i class="fas fa-shield-alt"></i></div><h3>Kamboh Monthly Service</h3><p>We handle your monthly STRN filings so you can focus on your business. Starting from PKR 3,000/month.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:760px">
    <span class="eyebrow-sm">FAQ</span>
    <h2 class="section-title">Sales Tax FAQs</h2>
    <div class="faq-list">
      <div class="faq-item"><div class="faq-q">What is the difference between NTN and STRN?<i class="fas fa-chevron-down"></i></div><div class="faq-a"><div class="faq-a-inner">NTN (National Tax Number) is for income tax registration — everyone must have it. STRN (Sales Tax Registration Number) is for businesses that supply taxable goods or services and need to charge/collect GST from customers. Both are registered on FBR IRIS.</div></div></div>
      <div class="faq-item"><div class="faq-q">What is the sales tax rate in Pakistan?<i class="fas fa-chevron-down"></i></div><div class="faq-a"><div class="faq-a-inner">The standard sales tax rate in Pakistan is 18% (FY 2025-26). However, various goods and services have reduced rates or exemptions. Provincial sales tax on services ranges from 13-16% depending on the province.</div></div></div>
      <div class="faq-item"><div class="faq-q">Do freelancers need STRN?<i class="fas fa-chevron-down"></i></div><div class="faq-a"><div class="faq-a-inner">Most individual freelancers do not need STRN for foreign clients (exports are zero-rated). However, if you provide services to Pakistani businesses and your annual turnover exceeds the threshold, registration may be required.</div></div></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <span class="eyebrow-sm">Related</span>
    <h2 class="section-title">Explore Related Services</h2>
    ${RELATED_SERVICES('/sales-tax-registration')}
  </div>
</section>

<section class="cta-strip">
  <div class="container">
    <h2>Get Your STRN Registered Today</h2>
    <p>Quick, accurate sales tax registration by FBR-certified consultants.</p>
    <div class="btns">
      <a href="https://wa.me/923284675162" class="btn btn-teal"><i class="fab fa-whatsapp"></i> WhatsApp Now</a>
      <a href="tel:03284675162" class="btn btn-outline" style="border-color:rgba(255,255,255,.35);color:#fff"><i class="fas fa-phone"></i> Call Us</a>
    </div>
  </div>
</section>
${FOOTER()}
</body></html>`);

// ═══════════════════════════════════════════
// PAGE 3: BUSINESS ADVISORY
// ═══════════════════════════════════════════
fs.writeFileSync('business-advisory.html', HEAD(
  'Business Advisory Services Pakistan — Tax & Compliance',
  'Expert business advisory, tax planning, FBR compliance, and corporate regulatory services by Kamboh Associates Lahore. Serving SMEs since 2008.',
  'business-advisory'
) + `</head><body>
${NAVBAR()}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Strategic Advisory</span>
    <h1>Business Advisory<br>& Tax Planning Pakistan</h1>
    <p>Expert business advisory services for SMEs, startups, and corporates. Tax planning, FBR compliance, corporate restructuring, and regulatory guidance since 2008.</p>
    <div class="hero-btns">
      <a href="https://wa.me/923284675162" class="btn btn-teal"><i class="fab fa-whatsapp"></i> Get Free Consultation</a>
      <a href="tel:03284675162" class="btn btn-outline" style="border-color:rgba(255,255,255,.4);color:#fff"><i class="fas fa-phone"></i> 0328-4675162</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow-sm">Our Advisory Services</span>
    <h2 class="section-title">Comprehensive Business Advisory</h2>
    <div class="cards-grid">
      <div class="card"><div class="card-icon"><i class="fas fa-chart-line"></i></div><h3>Tax Planning & Optimization</h3><p>Strategic tax planning to minimize your tax liability legally. Advance tax management, deductions optimization, and FY planning.</p></div>
      <div class="card"><div class="card-icon"><i class="fas fa-building"></i></div><h3>Business Structure Advisory</h3><p>Guidance on choosing between sole proprietorship, AOP, or SECP private limited company — based on your business size and goals.</p></div>
      <div class="card"><div class="card-icon"><i class="fas fa-shield-alt"></i></div><h3>FBR Compliance Management</h3><p>Ongoing FBR compliance — income tax, sales tax, withholding tax, and annual return management for businesses.</p></div>
      <div class="card"><div class="card-icon"><i class="fas fa-exclamation-triangle"></i></div><h3>FBR Notice Handling</h3><p>Expert handling of FBR audit notices, 111 notices, wealth explanations, and penalty removal applications.</p></div>
      <div class="card"><div class="card-icon"><i class="fas fa-handshake"></i></div><h3>Business Setup Advisory</h3><p>End-to-end guidance for new businesses: NTN, STRN, SECP registration, bank account opening, and initial compliance.</p></div>
      <div class="card"><div class="card-icon"><i class="fas fa-file-contract"></i></div><h3>Regulatory Compliance</h3><p>SECP annual filings, Form-A submissions, company annual returns, and corporate governance advisory.</p></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <span class="eyebrow-sm">Industries We Serve</span>
    <h2 class="section-title">Business Advisory Across Industries</h2>
    <div class="cards-grid">
      <div class="card"><div class="card-icon"><i class="fas fa-laptop-code"></i></div><h3>IT & Software Houses</h3><p>Tax exemptions, PSEB registration, IT export benefits, and software house compliance in Pakistan.</p></div>
      <div class="card"><div class="card-icon"><i class="fas fa-bullhorn"></i></div><h3>Digital Marketing Agencies</h3><p>Agency tax structure, client billing compliance, WHT management, and SECP vs sole proprietorship guidance.</p></div>
      <div class="card"><div class="card-icon"><i class="fas fa-shopping-cart"></i></div><h3>E-Commerce Businesses</h3><p>Amazon, Shopify, and local e-commerce tax compliance, import duty planning, and marketplace seller registration.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:760px">
    <span class="eyebrow-sm">FAQ</span>
    <h2 class="section-title">Business Advisory FAQs</h2>
    <div class="faq-list">
      <div class="faq-item"><div class="faq-q">What business structure is best for a startup in Pakistan?<i class="fas fa-chevron-down"></i></div><div class="faq-a"><div class="faq-a-inner">For most startups, a sole proprietorship is the simplest and cheapest to set up. However, if you want to raise investment, have multiple partners, or need limited liability protection, a SECP private limited company is better. Our advisors analyze your specific situation and recommend the optimal structure.</div></div></div>
      <div class="faq-item"><div class="faq-q">How do I handle a FBR 111 notice?<i class="fas fa-chevron-down"></i></div><div class="faq-a"><div class="faq-a-inner">A Section 111 notice from FBR requires you to explain unexplained income or assets. You typically have 30 days to respond. Kamboh Associates handles all FBR notice responses, prepares proper explanations, and represents you before FBR to resolve the matter without penalties.</div></div></div>
      <div class="faq-item"><div class="faq-q">Do software houses in Pakistan get tax exemption?<i class="fas fa-chevron-down"></i></div><div class="faq-a"><div class="faq-a-inner">Yes. PSEB-registered IT companies exporting software and IT services are eligible for significant tax exemptions under Pakistan's IT export incentive policy. Kamboh Associates handles PSEB registration and ensures your company qualifies for maximum tax benefits.</div></div></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <span class="eyebrow-sm">Related Services</span>
    <h2 class="section-title">Explore More</h2>
    ${RELATED_SERVICES('/business-advisory')}
  </div>
</section>

<section class="cta-strip">
  <div class="container">
    <h2>Get Expert Business Advisory</h2>
    <p>Free consultation for your business tax and compliance needs.</p>
    <div class="btns">
      <a href="https://wa.me/923284675162" class="btn btn-teal"><i class="fab fa-whatsapp"></i> Free Consultation</a>
      <a href="tel:03284675162" class="btn btn-outline" style="border-color:rgba(255,255,255,.35);color:#fff"><i class="fas fa-phone"></i> Call Us</a>
    </div>
  </div>
</section>
${FOOTER()}
</body></html>`);

console.log('Service pages created: income-tax-filing, sales-tax-registration, business-advisory');
