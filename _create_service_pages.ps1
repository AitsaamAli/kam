
$base = "c:\Users\786\Desktop\kam"

# Reusable navbar and footer
$COMMON_HEAD = @'
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta name="robots" content="index, follow"/>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/>
'@

$CSS = @'
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700&family=DM+Sans:wght@400;500;600&family=Cinzel:wght@600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-2ZLVR968Y8"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-2ZLVR968Y8');</script>
<link rel="icon" type="image/jpeg" href="/images/logo.jpg"/>
<style>
:root{--navy:#0F172A;--teal:#14B8A6;--teal-mid:#0D9488;--gold-light:#D4AF37;--font-display:'Cinzel',serif;--font-serif:'Cormorant Garamond',Georgia,serif;--font-body:'DM Sans',system-ui,sans-serif;--max-w:1200px;--radius:12px;--radius-lg:20px}
[data-theme="light"]{--bg:#FFFFFF;--bg-2:#F8F9FA;--bg-3:#F1F3F5;--surface:#FFFFFF;--border:#E2E8F0;--text:#0F172A;--text-2:#334155;--text-3:#64748B;--text-4:#94A3B8;--nav-bg:rgba(255,255,255,0.97);--nav-border:#E2E8F0;--shadow:0 1px 3px rgba(0,0,0,0.08),0 4px 16px rgba(0,0,0,0.06);--shadow-lg:0 8px 32px rgba(0,0,0,0.1);--teal-bg:rgba(20,184,166,0.06)}
[data-theme="dark"]{--bg:#0A0F1E;--bg-2:#0F172A;--bg-3:#1E293B;--surface:#0F172A;--border:rgba(255,255,255,0.08);--text:#F1F5F9;--text-2:#CBD5E1;--text-3:#64748B;--nav-bg:rgba(10,15,30,0.97);--nav-border:rgba(255,255,255,0.06);--shadow:0 1px 3px rgba(0,0,0,0.4),0 4px 16px rgba(0,0,0,0.3);--shadow-lg:0 8px 32px rgba(0,0,0,0.5);--teal-bg:rgba(20,184,166,0.1)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}body{font-family:var(--font-body);background:var(--bg);color:var(--text);line-height:1.65;overflow-x:hidden}a{text-decoration:none;color:inherit}ul{list-style:none}img{max-width:100%;display:block}
::-webkit-scrollbar{width:5px}::-webkit-scrollbar-thumb{background:#14B8A6;border-radius:4px}
.container{max-width:var(--max-w);margin:0 auto;padding:0 24px}
.topbar{background:#0F172A;padding:9px 0}.topbar .container{display:flex;align-items:center}.topbar-left{flex:1;overflow:hidden;white-space:nowrap}.topbar-promo-wrap{display:inline-flex;animation:kascroll 28s linear infinite}.topbar-promo{font-size:.68rem;letter-spacing:.04em;color:rgba(148,163,184,.9);white-space:nowrap;flex-shrink:0}@keyframes kascroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.navbar{position:sticky;top:0;z-index:1000;background:var(--nav-bg);backdrop-filter:blur(20px);border-bottom:1px solid var(--nav-border)}.navbar .container{display:flex;align-items:center;justify-content:space-between;height:68px}
.logo{display:flex;align-items:center;gap:12px}.logo-name{font-family:var(--font-display);font-size:.92rem;font-weight:700;letter-spacing:.07em;line-height:1.2}.logo-sub{font-size:.56rem;letter-spacing:.18em;color:var(--gold-light);text-transform:uppercase}
.nav-links{display:flex;align-items:center;gap:4px}.nav-links>li{position:relative;list-style:none}.nav-links>li>a{font-size:.84rem;font-weight:500;color:#1E293B;display:flex;align-items:center;gap:4px;padding:8px 14px;border-radius:8px;transition:all .2s;white-space:nowrap}.nav-links>li>a:hover{color:#14B8A6;background:#F0FDFA}
.nav-drop{position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%) translateY(-6px);z-index:2000;min-width:220px;background:#fff;border:1px solid #E2E8F0;border-radius:12px;box-shadow:0 8px 32px rgba(15,23,42,.12);padding:8px;opacity:0;visibility:hidden;pointer-events:none;transition:all .2s}.nav-links>li:hover .nav-drop{opacity:1;visibility:visible;pointer-events:auto;transform:translateX(-50%) translateY(0)}.nav-links>li:last-child .nav-drop{left:auto;right:0;transform:translateY(-6px)}.nav-links>li:last-child:hover .nav-drop{transform:translateY(0)}.nav-drop a{display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:8px;font-size:.82rem;color:#1E293B;transition:all .15s}.nav-drop a:hover{background:#F0FDFA;color:#14B8A6}.nav-drop a i{width:16px;text-align:center;color:#14B8A6;font-size:.78rem}
.nav-actions{display:flex;align-items:center;gap:10px}.nav-phone{font-size:.8rem;color:#64748B;display:flex;align-items:center;gap:6px}.nav-phone i{color:#14B8A6}.nav-phone a{color:#1E293B;font-weight:500}.nav-cta{background:#0F172A;color:#fff!important;padding:8px 18px!important;border-radius:8px!important;font-size:.82rem!important;font-weight:600!important;transition:all .2s!important}.nav-cta:hover{background:#14B8A6!important}
.hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;background:none;border:none;padding:4px}.hamburger span{width:22px;height:2px;background:#64748B;border-radius:2px;display:block}
.mobile-nav{display:none;flex-direction:column;position:fixed;top:68px;left:0;right:0;z-index:999;background:#fff;border-bottom:3px solid #14B8A6;box-shadow:0 12px 40px rgba(0,0,0,.15);max-height:calc(100vh - 68px);overflow-y:auto}.mobile-nav.open{display:flex}.mobile-nav a{padding:14px 24px;border-bottom:1px solid #F1F5F9;font-size:.9rem;color:#64748B}
.page-hero{background:var(--bg-2);border-bottom:1px solid var(--border);padding:72px 0 60px;position:relative;overflow:hidden}.page-hero::before{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(20,184,166,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(20,184,166,.04) 1px,transparent 1px);background-size:52px 52px}.page-hero::after{content:'';position:absolute;inset:0;background:radial-gradient(circle at 70% 30%,rgba(20,184,166,.06) 0%,transparent 50%)}.page-hero .container{position:relative;z-index:2}.page-hero h1{font-family:var(--font-serif);font-size:clamp(2rem,4vw,3rem);font-weight:700;color:var(--text);line-height:1.12;margin-bottom:18px;max-width:820px}.page-hero p{font-family:var(--font-serif);font-size:1.1rem;color:var(--text-2);line-height:1.8;max-width:680px;margin-bottom:32px}.hero-badge{display:inline-flex;align-items:center;gap:6px;background:rgba(20,184,166,.07);border:1px solid rgba(20,184,166,.2);border-radius:100px;padding:5px 16px;font-size:.7rem;color:#14B8A6;letter-spacing:.1em;text-transform:uppercase;font-family:var(--font-display);margin-bottom:20px}.hero-btns{display:flex;gap:12px;flex-wrap:wrap}.btn-wa{display:inline-flex;align-items:center;gap:8px;background:#25D366;color:#fff;padding:13px 28px;border-radius:8px;font-weight:600;font-size:.92rem;transition:all .2s}.btn-wa:hover{background:#1da851;transform:translateY(-2px)}.btn-outline{display:inline-flex;align-items:center;gap:8px;color:#0F172A;padding:12px 28px;border-radius:8px;font-size:.92rem;border:1.5px solid var(--border);transition:all .2s}.btn-outline:hover{border-color:#14B8A6;color:#14B8A6}
.stats-bar{background:var(--surface);border-bottom:1px solid var(--border);padding:22px 0}.stats-row{display:flex;justify-content:center;gap:48px;flex-wrap:wrap}.stat-item{text-align:center}.stat-num{font-family:var(--font-display);font-size:1.5rem;font-weight:700;color:#14B8A6}.stat-lbl{font-size:.75rem;color:#64748B;margin-top:2px}
.section{padding:80px 0}.section-alt{padding:80px 0;background:var(--bg-2)}.section-label{font-family:var(--font-display);font-size:.65rem;letter-spacing:.2em;text-transform:uppercase;color:#14B8A6;margin-bottom:12px}.section-title{font-family:var(--font-serif);font-size:clamp(1.7rem,3vw,2.4rem);font-weight:700;color:var(--text);margin-bottom:16px;line-height:1.2}.section-sub{font-size:.97rem;color:var(--text-3);max-width:640px;line-height:1.7}
.services-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:48px}.svc-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:32px;transition:all .3s}.svc-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg);border-color:rgba(20,184,166,.3)}.svc-icon{width:52px;height:52px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.3rem;margin-bottom:18px}.svc-icon-teal{background:rgba(20,184,166,.1);color:#14B8A6}.svc-icon-navy{background:rgba(15,23,42,.08);color:#0F172A}.svc-icon-gold{background:rgba(212,175,55,.1);color:#D4AF37}.svc-card h3{font-family:var(--font-serif);font-size:1.1rem;font-weight:700;margin-bottom:10px}.svc-card p{font-size:.88rem;color:var(--text-3);line-height:1.7}
.steps-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px;margin-top:48px}.step-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:36px 28px;text-align:center}.step-num{width:56px;height:56px;background:linear-gradient(135deg,#14B8A6,#0D9488);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.5rem;font-weight:800;margin:0 auto 20px;box-shadow:0 8px 20px rgba(20,184,166,.25)}.step-card h3{font-weight:700;font-size:1rem;margin-bottom:8px;color:var(--text)}.step-card p{font-size:.87rem;color:var(--text-3);line-height:1.65}
.pricing-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:24px;margin-top:48px}.price-card{background:var(--surface);border:2px solid var(--border);border-radius:var(--radius-lg);padding:36px 32px;transition:all .3s}.price-card.featured{border-color:#14B8A6;box-shadow:0 12px 40px rgba(20,184,166,.15)}.price-card h3{font-size:.9rem;color:var(--text-3);text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px}.price-amount{font-family:var(--font-display);font-size:2rem;font-weight:700;color:#14B8A6;margin:12px 0 4px}.price-period{font-size:.8rem;color:var(--text-3)}.price-divider{height:1px;background:var(--border);margin:20px 0}.price-features{display:flex;flex-direction:column;gap:10px}.price-feature{display:flex;align-items:center;gap:10px;font-size:.88rem;color:var(--text-2)}.price-feature i{color:#14B8A6;width:14px;flex-shrink:0}.price-cta{display:flex;align-items:center;justify-content:center;gap:8px;background:#0F172A;color:#fff;padding:12px 24px;border-radius:8px;font-weight:600;font-size:.88rem;margin-top:24px;transition:all .2s;width:100%;border:none;cursor:pointer}.price-cta:hover{background:#14B8A6}
.docs-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin-top:32px}.doc-item{display:flex;align-items:center;gap:12px;background:var(--bg-2);border:1px solid var(--border);border-radius:10px;padding:14px 16px;font-size:.88rem;color:var(--text-2)}.doc-item i{color:#14B8A6;width:18px;flex-shrink:0}
.faq-list{display:flex;flex-direction:column;gap:12px;margin-top:36px}.faq-item{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden}.faq-q{padding:16px 20px;font-weight:600;font-size:.92rem;cursor:pointer;display:flex;justify-content:space-between;align-items:center;color:var(--text)}.faq-q:hover{color:#14B8A6}.faq-q i{color:#14B8A6;transition:transform .3s;flex-shrink:0}.faq-item.open .faq-q i{transform:rotate(45deg)}.faq-a{display:none;padding:0 20px 16px;font-size:.88rem;color:var(--text-3);line-height:1.75}.faq-item.open .faq-a{display:block}
.cta-strip{background:linear-gradient(135deg,#0F172A,#14B8A6);padding:72px 0;text-align:center}.cta-strip h2{font-family:var(--font-serif);font-size:2rem;color:#fff;margin-bottom:14px}.cta-strip p{color:rgba(203,213,225,.9);max-width:580px;margin:0 auto 32px;font-size:.97rem;line-height:1.7}.cta-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}.btn-white{display:inline-flex;align-items:center;gap:8px;background:#fff;color:#0F172A;padding:13px 28px;border-radius:8px;font-weight:600;font-size:.92rem;transition:all .2s}.btn-white:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.2)}.btn-ghost-white{display:inline-flex;align-items:center;gap:8px;color:#fff;padding:12px 28px;border-radius:8px;font-size:.92rem;border:1.5px solid rgba(255,255,255,.4);transition:all .2s}.btn-ghost-white:hover{background:rgba(255,255,255,.1)}
footer{background:#0F172A;border-top:1px solid rgba(255,255,255,.06);padding:40px 0;text-align:center}.footer-logo{font-family:var(--font-display);font-size:1rem;color:var(--gold-light);letter-spacing:.1em;margin-bottom:14px}.footer-links{display:flex;justify-content:center;gap:24px;margin:16px 0;flex-wrap:wrap}.footer-links a{color:#64748B;font-size:.84rem;transition:color .2s}.footer-links a:hover{color:var(--gold-light)}.footer-copy{font-size:.76rem;color:#475569;margin-top:10px}
.wa-float{position:fixed;bottom:28px;right:28px;z-index:999;width:58px;height:58px;background:#25D366;border-radius:50%;display:grid;place-items:center;color:#fff;font-size:1.7rem;box-shadow:0 8px 28px rgba(37,211,102,.4);transition:transform .25s}.wa-float:hover{transform:scale(1.1)}
@media(max-width:900px){.nav-links,.nav-phone,.nav-cta{display:none}.hamburger{display:flex}.stats-row{gap:24px}}
@media(max-width:600px){.page-hero{padding:48px 0 40px}.section,.section-alt{padding:56px 0}.pricing-grid{grid-template-columns:1fr}}
</style>
'@

$NAV_BODY = @'

<div class="topbar"><div class="container"><div class="topbar-left"><div class="topbar-promo-wrap"><span class="topbar-promo">FBR NOTICE? CALL KAMBOH ASSOCIATES NOW &nbsp;&bull;&nbsp; 0328-4675162 &nbsp;&bull;&nbsp; EXPERT NOTICE RESPONSE &nbsp;&bull;&nbsp; FBR NOTICE DEFENSE &nbsp;&bull;&nbsp; DON'T IGNORE &mdash; CALL NOW 0328-4675162 &nbsp;&bull;&nbsp;</span><span class="topbar-promo" aria-hidden="true">FBR NOTICE? CALL KAMBOH ASSOCIATES NOW &nbsp;&bull;&nbsp; 0328-4675162 &nbsp;&bull;&nbsp; EXPERT NOTICE RESPONSE &nbsp;&bull;&nbsp; FBR NOTICE DEFENSE &nbsp;&bull;&nbsp; DON'T IGNORE &mdash; CALL NOW 0328-4675162 &nbsp;&bull;&nbsp;</span></div></div></div></div>
<nav class="navbar" id="navbar">
  <div class="container">
    <a href="/" class="logo">
      <div><img src="/images/logo.jpg" alt="Kamboh Associates" width="48" height="48" style="border-radius:50%;object-fit:cover"/></div>
      <div><div class="logo-name">KAMBOH ASSOCIATES</div><div class="logo-sub">Tax &amp; Regulatory Excellence</div></div>
    </a>
    <ul class="nav-links">
      <li><a href="/">Home</a></li>
      <li><a href="/income-tax-filing">Services <i class="fas fa-chevron-down" style="font-size:.6rem;opacity:.6"></i></a>
        <div class="nav-drop">
          <a href="/income-tax-filing"><i class="fas fa-file-invoice-dollar"></i> Income Tax Filing</a>
          <a href="/ntn-registration"><i class="fas fa-id-card"></i> NTN Registration</a>
          <a href="/sales-tax-registration"><i class="fas fa-percent"></i> Sales Tax Registration</a>
          <a href="/sales-tax-return"><i class="fas fa-file-alt"></i> Sales Tax Return</a>
          <a href="/corporate-tax-return"><i class="fas fa-building"></i> Corporate Tax Return</a>
          <a href="/fbr-notice-defense"><i class="fas fa-shield-alt"></i> FBR Notice Defense</a>
          <a href="/wealth-statement"><i class="fas fa-wallet"></i> Wealth Statement</a>
          <a href="/withholding-tax"><i class="fas fa-hand-holding-usd"></i> Withholding Tax</a>
          <a href="/eobi-registration"><i class="fas fa-users"></i> EOBI Registration</a>
          <a href="/secp-vs-sole-proprietorship-pakistan"><i class="fas fa-building-columns"></i> SECP Registration</a>
          <a href="/business-advisory"><i class="fas fa-chart-line"></i> Business Advisory</a>
          <a href="/pricing"><i class="fas fa-tags"></i> Pricing &amp; Fees</a>
        </div>
      </li>
      <li><a href="/#tools">Tools <i class="fas fa-chevron-down" style="font-size:.6rem;opacity:.6"></i></a>
        <div class="nav-drop">
          <a href="/tax-calculator"><i class="fas fa-calculator"></i> Tax Calculator</a>
          <a href="/salary-calculator"><i class="fas fa-user-tie"></i> Salary Calculator</a>
          <a href="/gst-calculator"><i class="fas fa-percent"></i> GST Calculator</a>
          <a href="/income-estimator"><i class="fas fa-chart-bar"></i> Income Estimator</a>
        </div>
      </li>
      <li><a href="/#deadlines">Deadlines</a></li>
      <li><a href="/pricing">Pricing</a></li>
      <li><a href="/contact">Contact</a></li>
      <li><a href="/blogs">Blog <i class="fas fa-chevron-down" style="font-size:.6rem;opacity:.6"></i></a>
        <div class="nav-drop">
          <a href="/blogs"><i class="fas fa-landmark"></i> FBR &amp; Tax Guides</a>
          <a href="/blogs"><i class="fas fa-user-clock"></i> Freelancer Tax</a>
          <a href="/blogs"><i class="fas fa-store"></i> E-Commerce Tax</a>
          <a href="/blogs"><i class="fas fa-building"></i> Business &amp; SECP</a>
        </div>
      </li>
    </ul>
    <div class="nav-actions">
      <span class="nav-phone"><i class="fas fa-phone"></i><a href="tel:03284675162">0328-4675162</a></span>
      <a href="/contact" class="nav-cta">Get Started</a>
      <button class="hamburger" id="hamburger" onclick="this.classList.toggle('open');document.getElementById('mobileNav').classList.toggle('open')" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
  <div class="mobile-nav" id="mobileNav">
    <a href="/">Home</a>
    <a href="/income-tax-filing">Income Tax Filing</a>
    <a href="/ntn-registration">NTN Registration</a>
    <a href="/sales-tax-registration">Sales Tax Registration</a>
    <a href="/sales-tax-return">Sales Tax Return</a>
    <a href="/corporate-tax-return">Corporate Tax Return</a>
    <a href="/fbr-notice-defense">FBR Notice Defense</a>
    <a href="/wealth-statement">Wealth Statement</a>
    <a href="/withholding-tax">Withholding Tax</a>
    <a href="/eobi-registration">EOBI Registration</a>
    <a href="/secp-vs-sole-proprietorship-pakistan">SECP Registration</a>
    <a href="/pricing">Pricing &amp; Fees</a>
    <a href="/blogs">Blog</a>
    <a href="/contact">Contact</a>
    <a href="https://wa.me/923284675162" target="_blank" style="color:#25D366"><i class="fab fa-whatsapp" style="margin-right:8px"></i>WhatsApp Advisory</a>
  </div>
</nav>
'@

$FOOTER = @'
<footer>
  <div class="container">
    <div class="footer-logo">KAMBOH ASSOCIATES</div>
    <p style="font-size:.84rem;color:#64748B;margin-bottom:12px">Pakistan's Trusted Tax Consultant &mdash; FBR Certified Since 2008</p>
    <div class="footer-links">
      <a href="/">Home</a><a href="/income-tax-filing">Income Tax</a><a href="/ntn-registration">NTN</a><a href="/sales-tax-registration">Sales Tax</a><a href="/corporate-tax-return">Corporate Tax</a><a href="/fbr-notice-defense">FBR Notice</a><a href="/wealth-statement">Wealth Statement</a><a href="/withholding-tax">WHT</a><a href="/eobi-registration">EOBI</a><a href="/pricing">Pricing</a><a href="/blogs">Blog</a><a href="/contact">Contact</a>
    </div>
    <div class="footer-copy">&copy; 2026 Kamboh Associates. All rights reserved. | 0328-4675162 | Lahore, Pakistan</div>
  </div>
</footer>
<a href="https://wa.me/923284675162" class="wa-float" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
<script>document.querySelectorAll('.faq-q').forEach(q=>{q.addEventListener('click',()=>{q.parentElement.classList.toggle('open')})});</script>
'@

# Helper: Assemble full page
function MkSvcPage($slug, $titleTag, $metaDesc, $canonSlug, $heroBody, $mainBody) {
  $path = "$base\$slug.html"
  if (Test-Path $path) { Write-Host "SKIP: $slug"; return }
  $content = $COMMON_HEAD + "`n<title>$titleTag</title>`n<meta name=`"description`" content=`"$metaDesc`"/>`n<link rel=`"canonical`" href=`"https://kambohassociates.com/$canonSlug`"/>`n" + $CSS + "`n</head><body>`n" + $NAV_BODY + $heroBody + $mainBody + $FOOTER + "`n</body></html>"
  [System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
  Write-Host "CREATED: $slug"
}

# ══════════════════════════════════════════
# 1. FBR NOTICE DEFENSE
# ══════════════════════════════════════════
$hero1 = @'
<section class="page-hero">
  <div class="container">
    <div class="hero-badge"><i class="fas fa-shield-alt"></i> &nbsp; FBR Certified Notice Experts</div>
    <h1>FBR Notice Defense &amp; Response Service Pakistan</h1>
    <p>Received an FBR notice? Don't ignore it. Our expert tax consultants handle Section 111, 114, 122, 177 audit notices with proper legal response filed on FBR IRIS within your deadline.</p>
    <div class="hero-btns">
      <a href="https://wa.me/923284675162" class="btn-wa"><i class="fab fa-whatsapp"></i> WhatsApp Notice Now</a>
      <a href="tel:03284675162" class="btn-outline"><i class="fas fa-phone"></i> Call 0328-4675162</a>
    </div>
  </div>
</section>
<div class="stats-bar"><div class="container"><div class="stats-row">
  <div class="stat-item"><div class="stat-num">500+</div><div class="stat-lbl">Notices Handled</div></div>
  <div class="stat-item"><div class="stat-num">24hr</div><div class="stat-lbl">Response Time</div></div>
  <div class="stat-item"><div class="stat-num">100%</div><div class="stat-lbl">Legal Compliance</div></div>
  <div class="stat-item"><div class="stat-num">2008</div><div class="stat-lbl">Est. Since</div></div>
</div></div></div>
'@

$main1 = @'
<section class="section">
  <div class="container">
    <div class="section-label">Notice Types We Handle</div>
    <h2 class="section-title">All FBR Notice Types — Expert Response</h2>
    <p class="section-sub">Every type of FBR notice requires a specific legal response strategy. Wrong response can make your situation worse. We know exactly what each notice requires.</p>
    <div class="services-grid">
      <div class="svc-card"><div class="svc-icon svc-icon-teal"><i class="fas fa-file-shield"></i></div><h3>Section 111 — Unexplained Income</h3><p>Unexplained assets or bank credits? We prepare a complete explanation with supporting documents to satisfy FBR demand.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-navy"><i class="fas fa-file-circle-exclamation"></i></div><h3>Section 114 — Non-Filing Notice</h3><p>Received notice for not filing returns? We file all pending returns AND respond to the notice to avoid penalties.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-gold"><i class="fas fa-balance-scale"></i></div><h3>Section 122 — Amendment Notice</h3><p>FBR wants to amend your assessment? We prepare legal objections and represent you before the tax officer.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-teal"><i class="fas fa-search-dollar"></i></div><h3>Section 177 — Tax Audit</h3><p>Audit notice received? We compile all required records, prepare audit response, and attend audit proceedings on your behalf.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-navy"><i class="fas fa-gavel"></i></div><h3>Appeal Filing — CIR / ATIR</h3><p>Disagree with FBR assessment? We file appeal before Commissioner Inland Revenue (Appeals) or Appellate Tribunal.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-gold"><i class="fas fa-clock-rotate-left"></i></div><h3>Penalty Remission</h3><p>Facing FBR penalties? We apply for penalty remission with proper legal grounds and documentation.</p></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">How It Works</div>
    <h2 class="section-title">Notice Response in 3 Steps</h2>
    <div class="steps-grid">
      <div class="step-card"><div class="step-num">1</div><h3>Share the Notice</h3><p>WhatsApp us a photo of the FBR notice. We review the notice type, applicable section, and response deadline — free of charge.</p></div>
      <div class="step-card"><div class="step-num">2</div><h3>We Prepare Response</h3><p>Our expert prepares a legally sound written response with supporting documents within 24-48 hours.</p></div>
      <div class="step-card"><div class="step-num">3</div><h3>Filed on FBR IRIS</h3><p>Response submitted through FBR IRIS portal with proper acknowledgment. We monitor FBR's next action and keep you informed.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-label">Pricing</div>
    <h2 class="section-title">Notice Response Charges</h2>
    <div class="pricing-grid">
      <div class="price-card"><h3>Basic Notice</h3><div class="price-amount">Rs. 5,000</div><div class="price-period">per notice</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Section 114 non-filing</li><li class="price-feature"><i class="fas fa-check"></i>Simple clarification notices</li><li class="price-feature"><i class="fas fa-check"></i>Written response on IRIS</li><li class="price-feature"><i class="fas fa-check"></i>48-hour turnaround</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
      <div class="price-card featured"><h3>Complex Notice</h3><div class="price-amount">Rs. 12,000</div><div class="price-period">per notice</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Section 111 / 122</li><li class="price-feature"><i class="fas fa-check"></i>Full documentation support</li><li class="price-feature"><i class="fas fa-check"></i>Legal grounds preparation</li><li class="price-feature"><i class="fas fa-check"></i>IRIS submission + followup</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
      <div class="price-card"><h3>Audit Defense</h3><div class="price-amount">Rs. 25,000</div><div class="price-period">onwards</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Section 177 audit</li><li class="price-feature"><i class="fas fa-check"></i>Full record compilation</li><li class="price-feature"><i class="fas fa-check"></i>Audit attendance</li><li class="price-feature"><i class="fas fa-check"></i>Appeal if needed</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">FAQ</div>
    <h2 class="section-title">FBR Notice Questions</h2>
    <div class="faq-list">
      <div class="faq-item"><div class="faq-q">What happens if I ignore an FBR notice? <i class="fas fa-plus"></i></div><div class="faq-a">Ignoring an FBR notice leads to ex-parte assessment, heavy penalties, bank account freeze, and legal prosecution. Always respond before the deadline.</div></div>
      <div class="faq-item"><div class="faq-q">How much time do I have to respond? <i class="fas fa-plus"></i></div><div class="faq-a">Most notices give 15-30 days. Section 111 and 122 notices usually give 30 days. Check the deadline printed on your notice and contact us immediately.</div></div>
      <div class="faq-item"><div class="faq-q">Can you get the notice cancelled? <i class="fas fa-plus"></i></div><div class="faq-a">Depending on the grounds, many notices can be resolved by proper explanation. For Section 111 notices with genuine income sources, we prepare explanation letters that satisfy FBR. For legally invalid notices, we object on legal grounds.</div></div>
      <div class="faq-item"><div class="faq-q">Do you handle notices for companies too? <i class="fas fa-plus"></i></div><div class="faq-a">Yes. We handle FBR notices for individuals, sole proprietors, AOPs, private limited companies, and public companies across all cities in Pakistan.</div></div>
    </div>
  </div>
</section>
<section class="cta-strip">
  <div class="container">
    <h2>Got an FBR Notice? Act Today.</h2>
    <p>Every day of delay increases your risk. WhatsApp us the notice and get free expert advice within 2 hours.</p>
    <div class="cta-btns"><a href="https://wa.me/923284675162" class="btn-white"><i class="fab fa-whatsapp"></i> WhatsApp Now &mdash; Free Review</a><a href="tel:03284675162" class="btn-ghost-white"><i class="fas fa-phone"></i> 0328-4675162</a></div>
  </div>
</section>
'@

MkSvcPage "fbr-notice-defense" "FBR Notice Defense Service Pakistan 2026 | Kamboh Associates" "Expert FBR notice response. Section 111, 114, 122, 177 audit defense. 24-hour legal response on FBR IRIS. WhatsApp 0328-4675162 for free review." "fbr-notice-defense" $hero1 $main1

# ══════════════════════════════════════════
# 2. WEALTH STATEMENT
# ══════════════════════════════════════════
$hero2 = @'
<section class="page-hero">
  <div class="container">
    <div class="hero-badge"><i class="fas fa-wallet"></i> &nbsp; FBR Wealth Statement Experts</div>
    <h1>Wealth Statement Filing &mdash; Accurate &amp; FBR-Compliant</h1>
    <p>Every active taxpayer must file a wealth statement with their income tax return. A wrong wealth statement is the #1 cause of Section 111 FBR notices. We file it correctly the first time.</p>
    <div class="hero-btns">
      <a href="https://wa.me/923284675162" class="btn-wa"><i class="fab fa-whatsapp"></i> WhatsApp Now</a>
      <a href="tel:03284675162" class="btn-outline"><i class="fas fa-phone"></i> Call 0328-4675162</a>
    </div>
  </div>
</section>
<div class="stats-bar"><div class="container"><div class="stats-row">
  <div class="stat-item"><div class="stat-num">5000+</div><div class="stat-lbl">Wealth Statements Filed</div></div>
  <div class="stat-item"><div class="stat-num">0</div><div class="stat-lbl">FBR Notices Triggered</div></div>
  <div class="stat-item"><div class="stat-num">24hr</div><div class="stat-lbl">Filing Time</div></div>
  <div class="stat-item"><div class="stat-num">100%</div><div class="stat-lbl">FBR Compliant</div></div>
</div></div></div>
'@

$main2 = @'
<section class="section">
  <div class="container">
    <div class="section-label">What We Declare</div>
    <h2 class="section-title">Complete Wealth Statement Filing</h2>
    <p class="section-sub">Your wealth statement must include all assets and liabilities — property, vehicles, gold, bank accounts, investments, and foreign assets. Miss anything and FBR will notice.</p>
    <div class="services-grid">
      <div class="svc-card"><div class="svc-icon svc-icon-teal"><i class="fas fa-home"></i></div><h3>Property &amp; Real Estate</h3><p>All immovable properties — house, plot, commercial — declared at FBR-compliant valuations to avoid Section 111 notice.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-navy"><i class="fas fa-car"></i></div><h3>Vehicles &amp; Movable Assets</h3><p>Vehicles, gold, jewelry, furniture declared at correct values per FBR schedule to prevent unexplained assets notices.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-gold"><i class="fas fa-university"></i></div><h3>Bank Accounts &amp; Investments</h3><p>All savings, fixed deposits, shares, mutual funds, and prize bonds reconciled with actual bank statements.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-teal"><i class="fas fa-globe"></i></div><h3>Foreign Assets Declaration</h3><p>Foreign bank accounts, properties, investments reported per Section 116A — essential for FATF compliance.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-navy"><i class="fas fa-business-time"></i></div><h3>Business Capital</h3><p>Business assets, stock-in-trade, debtors, and capital balances reconciled with your accounts.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-gold"><i class="fas fa-hand-holding-dollar"></i></div><h3>Liabilities Reconciliation</h3><p>Loans, mortgages, and liabilities declared properly to reduce net wealth and minimize tax exposure.</p></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">Process</div>
    <h2 class="section-title">How We File Your Wealth Statement</h2>
    <div class="steps-grid">
      <div class="step-card"><div class="step-num">1</div><h3>Asset Checklist</h3><p>Share all assets and liabilities via WhatsApp. We provide a simple checklist to ensure nothing is missed or overstated.</p></div>
      <div class="step-card"><div class="step-num">2</div><h3>Reconciliation</h3><p>We reconcile all assets with your income sources — ensuring no unexplained additions that could trigger FBR notices.</p></div>
      <div class="step-card"><div class="step-num">3</div><h3>Filed on IRIS</h3><p>Wealth statement filed on FBR IRIS with income tax return. Confirmation sent to you within 24 hours.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-label">Pricing</div>
    <h2 class="section-title">Wealth Statement Charges</h2>
    <div class="pricing-grid">
      <div class="price-card"><h3>Salaried Individual</h3><div class="price-amount">Rs. 4,000</div><div class="price-period">with tax return</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Basic assets declaration</li><li class="price-feature"><i class="fas fa-check"></i>Bank balance reconciliation</li><li class="price-feature"><i class="fas fa-check"></i>Property &amp; vehicle</li><li class="price-feature"><i class="fas fa-check"></i>Liabilities declaration</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
      <div class="price-card featured"><h3>Business Owner</h3><div class="price-amount">Rs. 8,000</div><div class="price-period">with tax return</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Business capital included</li><li class="price-feature"><i class="fas fa-check"></i>Multiple properties</li><li class="price-feature"><i class="fas fa-check"></i>Investments &amp; shares</li><li class="price-feature"><i class="fas fa-check"></i>Full reconciliation report</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
      <div class="price-card"><h3>Foreign Assets</h3><div class="price-amount">Rs. 15,000</div><div class="price-period">onwards</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Foreign bank accounts</li><li class="price-feature"><i class="fas fa-check"></i>Overseas properties</li><li class="price-feature"><i class="fas fa-check"></i>Section 116A compliance</li><li class="price-feature"><i class="fas fa-check"></i>FATF-compliant filing</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">FAQ</div>
    <h2 class="section-title">Wealth Statement FAQ</h2>
    <div class="faq-list">
      <div class="faq-item"><div class="faq-q">Is wealth statement mandatory? <i class="fas fa-plus"></i></div><div class="faq-a">Yes. Under Section 116 of Income Tax Ordinance 2001, every person required to file an income tax return must also submit a Wealth Statement showing all assets and liabilities as of June 30.</div></div>
      <div class="faq-item"><div class="faq-q">What if my assets increased but income is low? <i class="fas fa-plus"></i></div><div class="faq-a">This is the most common cause of Section 111 (unexplained income) notices. We carefully reconcile asset additions with all income sources — gifts, inheritance, loans — to prepare a clean, defensible wealth statement.</div></div>
      <div class="faq-item"><div class="faq-q">Do I need to declare gold and jewelry? <i class="fas fa-plus"></i></div><div class="faq-a">Yes. Gold, jewelry, and household items are declared at their current market value. We help you calculate fair values per FBR guidelines so you stay compliant without overpaying.</div></div>
    </div>
  </div>
</section>
<section class="cta-strip">
  <div class="container">
    <h2>File Your Wealth Statement Correctly</h2>
    <p>A wrong wealth statement is the #1 trigger for FBR notices. Let our experts file it right, the first time.</p>
    <div class="cta-btns"><a href="https://wa.me/923284675162" class="btn-white"><i class="fab fa-whatsapp"></i> WhatsApp Now</a><a href="tel:03284675162" class="btn-ghost-white"><i class="fas fa-phone"></i> 0328-4675162</a></div>
  </div>
</section>
'@

MkSvcPage "wealth-statement" "Wealth Statement Filing Service Pakistan 2026 | Kamboh Associates" "Accurate wealth statement filing with income tax return. All assets, liabilities, foreign assets declared correctly. Prevents Section 111 FBR notices. From Rs. 4,000. WhatsApp 0328-4675162." "wealth-statement" $hero2 $main2

# ══════════════════════════════════════════
# 3. WITHHOLDING TAX
# ══════════════════════════════════════════
$hero3 = @'
<section class="page-hero">
  <div class="container">
    <div class="hero-badge"><i class="fas fa-hand-holding-usd"></i> &nbsp; WHT Compliance Experts</div>
    <h1>Withholding Tax Compliance &amp; Monthly Filing Pakistan</h1>
    <p>Every employer and registered business must deduct and deposit withholding tax monthly. Missing the 20th deadline means Rs. 2,500 per day penalty. We handle your complete WHT compliance.</p>
    <div class="hero-btns">
      <a href="https://wa.me/923284675162" class="btn-wa"><i class="fab fa-whatsapp"></i> WhatsApp Now</a>
      <a href="tel:03284675162" class="btn-outline"><i class="fas fa-phone"></i> Call 0328-4675162</a>
    </div>
  </div>
</section>
<div class="stats-bar"><div class="container"><div class="stats-row">
  <div class="stat-item"><div class="stat-num">1200+</div><div class="stat-lbl">Monthly Filings Done</div></div>
  <div class="stat-item"><div class="stat-num">20th</div><div class="stat-lbl">Monthly Deadline</div></div>
  <div class="stat-item"><div class="stat-num">Rs. 0</div><div class="stat-lbl">Penalties for Clients</div></div>
  <div class="stat-item"><div class="stat-num">2008</div><div class="stat-lbl">Est. Since</div></div>
</div></div></div>
'@

$main3 = @'
<section class="section">
  <div class="container">
    <div class="section-label">WHT Services</div>
    <h2 class="section-title">Complete Withholding Tax Management</h2>
    <p class="section-sub">From salary deductions to contractor payments, import tax to rent WHT — we calculate, deposit, and file monthly statements for every WHT category your business needs.</p>
    <div class="services-grid">
      <div class="svc-card"><div class="svc-icon svc-icon-teal"><i class="fas fa-user-tie"></i></div><h3>Salary WHT — Section 149</h3><p>Monthly income tax deduction from employee salaries. We calculate correct deduction per slab and prepare Salary Register.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-navy"><i class="fas fa-file-invoice"></i></div><h3>Contractor Payments — Section 153</h3><p>WHT on payments to contractors at 7% (filer) or 14% (non-filer). Monthly statements filed on FBR IRIS.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-gold"><i class="fas fa-home"></i></div><h3>Rent WHT — Section 155</h3><p>15% WHT on commercial rent to non-ATL landlords. Monthly deduction, deposit, and statements managed.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-teal"><i class="fas fa-calendar-alt"></i></div><h3>Monthly WHT Statements</h3><p>Monthly withholding statements filed on FBR IRIS by 20th of following month. Avoid Rs. 2,500/day penalty.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-navy"><i class="fas fa-percent"></i></div><h3>Import WHT — Section 148</h3><p>Advance tax on imports calculated and reconciled with customs payments. Annual adjustable tax treatment handled.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-gold"><i class="fas fa-file-export"></i></div><h3>Annual WHT Reconciliation</h3><p>Year-end reconciliation of all WHT deducted, deposited, and declared. Clean reconciliation prevents audit triggers.</p></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">Process</div>
    <h2 class="section-title">Monthly WHT Compliance Process</h2>
    <div class="steps-grid">
      <div class="step-card"><div class="step-num">1</div><h3>Share Payment Data</h3><p>Send monthly salary register, contractor invoices, and other payments. We extract all WHT data automatically.</p></div>
      <div class="step-card"><div class="step-num">2</div><h3>Calculate &amp; Deposit</h3><p>We calculate correct WHT per section, prepare CPR challans, and guide payment through banking channel.</p></div>
      <div class="step-card"><div class="step-num">3</div><h3>File Monthly Statement</h3><p>WHT statement filed on FBR IRIS by the 20th. Acknowledgment and filed statement sent to you.</p></div>
      <div class="step-card"><div class="step-num">4</div><h3>Annual Reconciliation</h3><p>Year-end reconciliation with annual return. WHT certificates issued to all payees.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-label">Pricing</div>
    <h2 class="section-title">WHT Compliance Charges</h2>
    <div class="pricing-grid">
      <div class="price-card"><h3>Small Business</h3><div class="price-amount">Rs. 3,000</div><div class="price-period">per month</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Up to 10 employees</li><li class="price-feature"><i class="fas fa-check"></i>Salary WHT</li><li class="price-feature"><i class="fas fa-check"></i>Monthly statement</li><li class="price-feature"><i class="fas fa-check"></i>WHT certificates</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
      <div class="price-card featured"><h3>Medium Business</h3><div class="price-amount">Rs. 6,000</div><div class="price-period">per month</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Up to 50 employees</li><li class="price-feature"><i class="fas fa-check"></i>All WHT sections</li><li class="price-feature"><i class="fas fa-check"></i>Contractor WHT</li><li class="price-feature"><i class="fas fa-check"></i>Annual reconciliation</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
      <div class="price-card"><h3>Large Business</h3><div class="price-amount">Custom</div><div class="price-period">contact us</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>50+ employees</li><li class="price-feature"><i class="fas fa-check"></i>All WHT categories</li><li class="price-feature"><i class="fas fa-check"></i>Import WHT</li><li class="price-feature"><i class="fas fa-check"></i>Dedicated consultant</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">FAQ</div>
    <h2 class="section-title">WHT FAQ</h2>
    <div class="faq-list">
      <div class="faq-item"><div class="faq-q">What is the penalty for not filing monthly WHT statement? <i class="fas fa-plus"></i></div><div class="faq-a">Under Section 182 of ITO 2001, failure to file WHT statement attracts Rs. 2,500 per day of default, plus 25% surcharge on late tax. This can accumulate to lakhs quickly.</div></div>
      <div class="faq-item"><div class="faq-q">Who must deduct withholding tax? <i class="fas fa-plus"></i></div><div class="faq-a">All registered companies, AOPs registered for income or sales tax, government departments, and e-enrolled withholding agents must deduct and file WHT statements.</div></div>
      <div class="faq-item"><div class="faq-q">What is the WHT rate on contractor payments? <i class="fas fa-plus"></i></div><div class="faq-a">Section 153 rates: 7% for filers on services, 14% for non-filers. For supply of goods: 4.5% filers, 9% non-filers. Rates vary by payment type and ATL status of payee.</div></div>
    </div>
  </div>
</section>
<section class="cta-strip">
  <div class="container">
    <h2>Stay WHT Compliant &mdash; Avoid Penalties</h2>
    <p>One missed WHT filing = Rs. 2,500 per day. Let us handle your monthly filings so you never miss a deadline.</p>
    <div class="cta-btns"><a href="https://wa.me/923284675162" class="btn-white"><i class="fab fa-whatsapp"></i> WhatsApp Now</a><a href="tel:03284675162" class="btn-ghost-white"><i class="fas fa-phone"></i> 0328-4675162</a></div>
  </div>
</section>
'@

MkSvcPage "withholding-tax" "Withholding Tax Compliance Service Pakistan 2026 | Kamboh Associates" "Monthly WHT statements, salary WHT, contractor WHT filing by 20th each month. Avoid Rs. 2,500/day penalty. From Rs. 3,000/month. WhatsApp 0328-4675162." "withholding-tax" $hero3 $main3

# ══════════════════════════════════════════
# 4. CORPORATE TAX RETURN
# ══════════════════════════════════════════
$hero4 = @'
<section class="page-hero">
  <div class="container">
    <div class="hero-badge"><i class="fas fa-building"></i> &nbsp; Corporate Tax Filing Experts</div>
    <h1>Corporate Tax Return Filing &mdash; Pvt Ltd, AOP &amp; Partnership</h1>
    <p>Private limited companies and AOPs must file annual corporate tax returns with FBR. Late filing means Rs. 40,000 minimum penalty. We handle complete corporate tax compliance including SECP filings.</p>
    <div class="hero-btns">
      <a href="https://wa.me/923284675162" class="btn-wa"><i class="fab fa-whatsapp"></i> WhatsApp Now</a>
      <a href="tel:03284675162" class="btn-outline"><i class="fas fa-phone"></i> Call 0328-4675162</a>
    </div>
  </div>
</section>
<div class="stats-bar"><div class="container"><div class="stats-row">
  <div class="stat-item"><div class="stat-num">300+</div><div class="stat-lbl">Companies Filed</div></div>
  <div class="stat-item"><div class="stat-num">29%</div><div class="stat-lbl">Corporate Tax Rate</div></div>
  <div class="stat-item"><div class="stat-num">Rs. 0</div><div class="stat-lbl">Late Penalties</div></div>
  <div class="stat-item"><div class="stat-num">2008</div><div class="stat-lbl">Est. Since</div></div>
</div></div></div>
'@

$main4 = @'
<section class="section">
  <div class="container">
    <div class="section-label">Services Included</div>
    <h2 class="section-title">Complete Corporate Tax Compliance</h2>
    <p class="section-sub">From tax computation to SECP filings, we handle every aspect of your company's annual tax obligations — so you can focus on running your business.</p>
    <div class="services-grid">
      <div class="svc-card"><div class="svc-icon svc-icon-teal"><i class="fas fa-building"></i></div><h3>Pvt Ltd Company Return</h3><p>Annual income tax return for Private Limited companies including balance sheet, P&amp;L, and tax computation at 29% corporate rate.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-navy"><i class="fas fa-handshake"></i></div><h3>AOP / Partnership Return</h3><p>Association of Persons and partnership firm tax returns. Each partner's share income declared separately on FBR IRIS.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-gold"><i class="fas fa-file-contract"></i></div><h3>Tax Computation Preparation</h3><p>Detailed tax computation showing gross profit, deductible expenses, taxable income, and final tax liability.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-teal"><i class="fas fa-chart-pie"></i></div><h3>Minimum Tax — Section 113</h3><p>Calculation of minimum tax at 1.25% of turnover where applicable. Section 113 compliance and reconciliation.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-navy"><i class="fas fa-coins"></i></div><h3>Advance Tax Management</h3><p>Quarterly advance tax calculation, deposit, and reconciliation with annual liability to minimize year-end payments.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-gold"><i class="fas fa-file-circle-check"></i></div><h3>SECP Annual Filing</h3><p>Form A (Annual Return) and Form 29 (Directors) filed with SECP alongside tax return for full compliance.</p></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">Process</div>
    <h2 class="section-title">Corporate Tax Filing Process</h2>
    <div class="steps-grid">
      <div class="step-card"><div class="step-num">1</div><h3>Share Accounts</h3><p>Share your annual accounts, bank statements, and FBR challans via WhatsApp or email. We handle the rest.</p></div>
      <div class="step-card"><div class="step-num">2</div><h3>Tax Computation</h3><p>We prepare detailed tax computation, reconcile WHT credits, and calculate final tax payable or refundable.</p></div>
      <div class="step-card"><div class="step-num">3</div><h3>Return Filing</h3><p>Corporate tax return filed on FBR IRIS with all annexures. SECP annual return filed simultaneously.</p></div>
      <div class="step-card"><div class="step-num">4</div><h3>Payment &amp; Confirmation</h3><p>Tax challan prepared, payment deposited, filed return with payment receipt sent to you within 48 hours.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-label">Pricing</div>
    <h2 class="section-title">Corporate Tax Return Charges</h2>
    <div class="pricing-grid">
      <div class="price-card"><h3>Small Company</h3><div class="price-amount">Rs. 18,000</div><div class="price-period">per year</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Turnover up to Rs. 10M</li><li class="price-feature"><i class="fas fa-check"></i>Tax computation</li><li class="price-feature"><i class="fas fa-check"></i>FBR annual return</li><li class="price-feature"><i class="fas fa-check"></i>SECP Form A</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
      <div class="price-card featured"><h3>Medium Company</h3><div class="price-amount">Rs. 35,000</div><div class="price-period">per year</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Turnover up to Rs. 50M</li><li class="price-feature"><i class="fas fa-check"></i>Full tax computation</li><li class="price-feature"><i class="fas fa-check"></i>WHT reconciliation</li><li class="price-feature"><i class="fas fa-check"></i>SECP + FBR filing</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
      <div class="price-card"><h3>Large Company</h3><div class="price-amount">Custom</div><div class="price-period">contact us</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Turnover Rs. 50M+</li><li class="price-feature"><i class="fas fa-check"></i>Audit liaison</li><li class="price-feature"><i class="fas fa-check"></i>Transfer pricing</li><li class="price-feature"><i class="fas fa-check"></i>Dedicated team</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">FAQ</div>
    <h2 class="section-title">Corporate Tax FAQ</h2>
    <div class="faq-list">
      <div class="faq-item"><div class="faq-q">What is the corporate tax rate in Pakistan 2026? <i class="fas fa-plus"></i></div><div class="faq-a">Standard corporate tax rate is 29% of taxable income. Small companies with turnover under Rs. 250M may qualify for reduced rates. Minimum tax under Section 113 is 1.25% of gross turnover where regular tax is lower.</div></div>
      <div class="faq-item"><div class="faq-q">When is the corporate tax return deadline? <i class="fas fa-plus"></i></div><div class="faq-a">For companies with fiscal year ending June 30, the deadline is December 31. For December year-end, deadline is June 30. Late filing penalty is Rs. 40,000 or 0.1% of tax payable — whichever is higher.</div></div>
      <div class="faq-item"><div class="faq-q">Does my Pvt Ltd company need an audit? <i class="fas fa-plus"></i></div><div class="faq-a">Companies with paid-up capital over Rs. 1 million or annual turnover exceeding Rs. 25 million must get accounts audited by a chartered accountant. We can coordinate audit through our CA network.</div></div>
    </div>
  </div>
</section>
<section class="cta-strip">
  <div class="container">
    <h2>File Your Company Tax Return On Time</h2>
    <p>Late corporate tax filing costs Rs. 40,000 minimum. Get your return filed correctly and on time — every year.</p>
    <div class="cta-btns"><a href="https://wa.me/923284675162" class="btn-white"><i class="fab fa-whatsapp"></i> WhatsApp Now</a><a href="tel:03284675162" class="btn-ghost-white"><i class="fas fa-phone"></i> 0328-4675162</a></div>
  </div>
</section>
'@

MkSvcPage "corporate-tax-return" "Corporate Tax Return Filing Pakistan 2026 | Pvt Ltd and AOP | Kamboh Associates" "Annual corporate tax return for private limited companies and AOPs. Tax computation, WHT reconciliation, SECP filing. From Rs. 18,000. WhatsApp 0328-4675162." "corporate-tax-return" $hero4 $main4

# ══════════════════════════════════════════
# 5. SALES TAX RETURN
# ══════════════════════════════════════════
$hero5 = @'
<section class="page-hero">
  <div class="container">
    <div class="hero-badge"><i class="fas fa-file-alt"></i> &nbsp; Sales Tax Return Experts</div>
    <h1>Monthly Sales Tax Return Filing &mdash; Never Miss the 18th</h1>
    <p>STRN-registered businesses must file monthly sales tax returns by the 18th. Late filing means Rs. 10,000 fine + 1.5% monthly surcharge. We file on time, every month — guaranteed.</p>
    <div class="hero-btns">
      <a href="https://wa.me/923284675162" class="btn-wa"><i class="fab fa-whatsapp"></i> WhatsApp Now</a>
      <a href="tel:03284675162" class="btn-outline"><i class="fas fa-phone"></i> Call 0328-4675162</a>
    </div>
  </div>
</section>
<div class="stats-bar"><div class="container"><div class="stats-row">
  <div class="stat-item"><div class="stat-num">800+</div><div class="stat-lbl">Monthly Returns Filed</div></div>
  <div class="stat-item"><div class="stat-num">18th</div><div class="stat-lbl">Monthly Deadline</div></div>
  <div class="stat-item"><div class="stat-num">Rs. 0</div><div class="stat-lbl">Missed Deadlines</div></div>
  <div class="stat-item"><div class="stat-num">2008</div><div class="stat-lbl">Est. Since</div></div>
</div></div></div>
'@

$main5 = @'
<section class="section">
  <div class="container">
    <div class="section-label">What We File</div>
    <h2 class="section-title">Complete Sales Tax Return Service</h2>
    <p class="section-sub">From output tax calculation to input tax reconciliation and FBR POS reporting — we handle your complete monthly sales tax compliance so you can focus on business.</p>
    <div class="services-grid">
      <div class="svc-card"><div class="svc-icon svc-icon-teal"><i class="fas fa-receipt"></i></div><h3>Monthly Return Filing</h3><p>Sales tax return filed on FBR IRIS by 18th each month. Output vs input tax calculated accurately for minimum tax liability.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-navy"><i class="fas fa-file-invoice-dollar"></i></div><h3>Input Tax Reconciliation</h3><p>All input tax claims cross-checked with FBR purchase data. Maximum legitimate input tax claimed to reduce liability.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-gold"><i class="fas fa-qrcode"></i></div><h3>FBR POS Reporting</h3><p>FBR-integrated POS businesses get daily invoice reporting and monthly return filed in compliance with POS system.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-teal"><i class="fas fa-boxes-stacked"></i></div><h3>Manufacturer Returns</h3><p>Special returns for manufacturers including Section 8B restrictions and minimum 60% input tax claim management.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-navy"><i class="fas fa-file-excel"></i></div><h3>Nil Return Filing</h3><p>Even with no sales, a nil return must be filed. We include nil return filing in every monthly package — no extra charge.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-gold"><i class="fas fa-plane-departure"></i></div><h3>Export Refund Claims</h3><p>Zero-rated export refund claims filed on FBR with all supporting documents for fast-track refund processing.</p></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">Process</div>
    <h2 class="section-title">Monthly Filing Process</h2>
    <div class="steps-grid">
      <div class="step-card"><div class="step-num">1</div><h3>Share Monthly Data</h3><p>Send us your monthly sales invoices and purchase invoices. We extract output and input tax data automatically.</p></div>
      <div class="step-card"><div class="step-num">2</div><h3>Reconciliation</h3><p>Output tax vs input tax reconciled. FBR purchase ledger cross-checked to validate all input claims.</p></div>
      <div class="step-card"><div class="step-num">3</div><h3>Filed by 18th</h3><p>Sales tax return filed before the 18th. Tax challan prepared and payment deposited with acknowledgment sent to you.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-label">Pricing</div>
    <h2 class="section-title">Sales Tax Return Charges</h2>
    <div class="pricing-grid">
      <div class="price-card"><h3>Small Trader</h3><div class="price-amount">Rs. 2,500</div><div class="price-period">per month</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Up to 50 invoices/month</li><li class="price-feature"><i class="fas fa-check"></i>Input tax reconciliation</li><li class="price-feature"><i class="fas fa-check"></i>Monthly return filing</li><li class="price-feature"><i class="fas fa-check"></i>Nil return included</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
      <div class="price-card featured"><h3>Medium Business</h3><div class="price-amount">Rs. 5,000</div><div class="price-period">per month</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Unlimited invoices</li><li class="price-feature"><i class="fas fa-check"></i>POS reporting</li><li class="price-feature"><i class="fas fa-check"></i>Full reconciliation</li><li class="price-feature"><i class="fas fa-check"></i>Annual return</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
      <div class="price-card"><h3>Manufacturer/Exporter</h3><div class="price-amount">Rs. 10,000</div><div class="price-period">per month</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Complex returns</li><li class="price-feature"><i class="fas fa-check"></i>Export refund claims</li><li class="price-feature"><i class="fas fa-check"></i>Section 8B compliance</li><li class="price-feature"><i class="fas fa-check"></i>Provincial tax coordination</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">FAQ</div>
    <h2 class="section-title">Sales Tax Return FAQ</h2>
    <div class="faq-list">
      <div class="faq-item"><div class="faq-q">What is the monthly sales tax return deadline? <i class="fas fa-plus"></i></div><div class="faq-a">The monthly sales tax return must be filed by the 18th of the following month. For example, January return must be filed by February 18. Late filing attracts Rs. 10,000 fine plus 1.5% per month default surcharge on outstanding tax.</div></div>
      <div class="faq-item"><div class="faq-q">What if I have no sales this month? <i class="fas fa-plus"></i></div><div class="faq-a">You must still file a Nil return by the 18th. Failure to file even a nil return attracts the same Rs. 10,000 penalty. We include nil return filing in every monthly package at no extra charge.</div></div>
      <div class="faq-item"><div class="faq-q">Can I claim input tax on all purchases? <i class="fas fa-plus"></i></div><div class="faq-a">Input tax can only be claimed on purchases from STRN-registered suppliers with valid FBR invoices. Section 8B restricts input to 60% of output tax for some categories. We ensure maximum legitimate input is claimed.</div></div>
    </div>
  </div>
</section>
<section class="cta-strip">
  <div class="container">
    <h2>Never Miss the 18th Deadline Again</h2>
    <p>We file your sales tax return every month before the deadline. Zero penalties, zero stress, full compliance.</p>
    <div class="cta-btns"><a href="https://wa.me/923284675162" class="btn-white"><i class="fab fa-whatsapp"></i> WhatsApp Now</a><a href="tel:03284675162" class="btn-ghost-white"><i class="fas fa-phone"></i> 0328-4675162</a></div>
  </div>
</section>
'@

MkSvcPage "sales-tax-return" "Monthly Sales Tax Return Filing Service Pakistan 2026 | Kamboh Associates" "Monthly sales tax return filing on FBR IRIS before 18th deadline. Input tax reconciliation, POS reporting, nil returns included. From Rs. 2,500/month. WhatsApp 0328-4675162." "sales-tax-return" $hero5 $main5

# ══════════════════════════════════════════
# 6. EOBI REGISTRATION
# ══════════════════════════════════════════
$hero6 = @'
<section class="page-hero">
  <div class="container">
    <div class="hero-badge"><i class="fas fa-users"></i> &nbsp; EOBI and Labour Law Experts</div>
    <h1>EOBI Registration &amp; Monthly Compliance Service</h1>
    <p>5 or more employees? EOBI registration is mandatory by law. Monthly contributions of 6% must be filed on time. We register your business with EOBI and manage ongoing monthly compliance.</p>
    <div class="hero-btns">
      <a href="https://wa.me/923284675162" class="btn-wa"><i class="fab fa-whatsapp"></i> WhatsApp Now</a>
      <a href="tel:03284675162" class="btn-outline"><i class="fas fa-phone"></i> Call 0328-4675162</a>
    </div>
  </div>
</section>
<div class="stats-bar"><div class="container"><div class="stats-row">
  <div class="stat-item"><div class="stat-num">400+</div><div class="stat-lbl">Employers Registered</div></div>
  <div class="stat-item"><div class="stat-num">7-14</div><div class="stat-lbl">Days to Register</div></div>
  <div class="stat-item"><div class="stat-num">100%</div><div class="stat-lbl">Compliance Rate</div></div>
  <div class="stat-item"><div class="stat-num">2008</div><div class="stat-lbl">Est. Since</div></div>
</div></div></div>
'@

$main6 = @'
<section class="section">
  <div class="container">
    <div class="section-label">Services Included</div>
    <h2 class="section-title">Complete EOBI &amp; Labour Compliance</h2>
    <p class="section-sub">From initial employer registration to monthly contribution filing and employee enrollment — we handle every aspect of your EOBI and social security compliance.</p>
    <div class="services-grid">
      <div class="svc-card"><div class="svc-icon svc-icon-teal"><i class="fas fa-user-plus"></i></div><h3>Employer EOBI Registration</h3><p>Register your business with EOBI online. Employer registration number issued within 7-14 working days.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-navy"><i class="fas fa-users"></i></div><h3>Employee Enrollment</h3><p>All employees enrolled on EOBI system with individual insurance numbers. EOBI cards facilitated for each employee.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-gold"><i class="fas fa-calendar-check"></i></div><h3>Monthly Contribution Filing</h3><p>5% employer + 1% employee EOBI contribution calculated, submitted, and payment receipt maintained monthly.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-teal"><i class="fas fa-id-badge"></i></div><h3>PESSI Registration — Punjab</h3><p>Punjab Employees Social Security Institution registration and monthly contribution filing for Punjab employers.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-navy"><i class="fas fa-file-medical"></i></div><h3>WWF Compliance</h3><p>Workers Welfare Fund registration and annual levy payment for employers with assessable income above Rs. 500,000.</p></div>
      <div class="svc-card"><div class="svc-icon svc-icon-gold"><i class="fas fa-clock"></i></div><h3>Back-Period Regularization</h3><p>Previously non-compliant? We regularize past EOBI dues with penalty negotiation and installment arrangements.</p></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">Process</div>
    <h2 class="section-title">EOBI Registration Process</h2>
    <div class="steps-grid">
      <div class="step-card"><div class="step-num">1</div><h3>Business Documents</h3><p>Share NTN, CNIC of owner/directors, business registration, and employee list via WhatsApp.</p></div>
      <div class="step-card"><div class="step-num">2</div><h3>Online Application</h3><p>We submit employer registration on EOBI portal with all documents. Application tracked daily.</p></div>
      <div class="step-card"><div class="step-num">3</div><h3>Registration Number</h3><p>EOBI employer number received within 7-14 days. All employees enrolled on system immediately.</p></div>
      <div class="step-card"><div class="step-num">4</div><h3>Monthly Compliance</h3><p>Ongoing monthly contributions calculated and filed. We manage EOBI so you focus on your business.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-label">Pricing</div>
    <h2 class="section-title">EOBI Service Charges</h2>
    <div class="pricing-grid">
      <div class="price-card"><h3>Registration Only</h3><div class="price-amount">Rs. 8,000</div><div class="price-period">one-time</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>EOBI employer registration</li><li class="price-feature"><i class="fas fa-check"></i>Up to 20 employees enrolled</li><li class="price-feature"><i class="fas fa-check"></i>Registration certificate</li><li class="price-feature"><i class="fas fa-check"></i>First month setup</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
      <div class="price-card featured"><h3>Registration + Monthly</h3><div class="price-amount">Rs. 2,000</div><div class="price-period">per month (after reg)</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Monthly contribution filing</li><li class="price-feature"><i class="fas fa-check"></i>New employee enrollment</li><li class="price-feature"><i class="fas fa-check"></i>Payment receipts maintained</li><li class="price-feature"><i class="fas fa-check"></i>PESSI if applicable</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
      <div class="price-card"><h3>Regularization</h3><div class="price-amount">Custom</div><div class="price-period">contact us</div><div class="price-divider"></div><ul class="price-features"><li class="price-feature"><i class="fas fa-check"></i>Back period calculation</li><li class="price-feature"><i class="fas fa-check"></i>Penalty negotiation</li><li class="price-feature"><i class="fas fa-check"></i>EOBI compliance audit</li><li class="price-feature"><i class="fas fa-check"></i>Full regularization</li></ul><a href="https://wa.me/923284675162" class="price-cta"><i class="fab fa-whatsapp"></i> Get Started</a></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">FAQ</div>
    <h2 class="section-title">EOBI FAQ</h2>
    <div class="faq-list">
      <div class="faq-item"><div class="faq-q">Is EOBI registration mandatory? <i class="fas fa-plus"></i></div><div class="faq-a">Yes. Under the EOBI Act 1976, every employer with 5 or more workers must register with EOBI within 30 days of reaching 5 employees. Non-compliance attracts prosecution and arrears with 10% annual surcharge.</div></div>
      <div class="faq-item"><div class="faq-q">What is the EOBI contribution amount? <i class="fas fa-plus"></i></div><div class="faq-a">Employer contributes 5% of minimum wage (Rs. 37,000 from July 2025) = Rs. 1,850 per employee per month. Employee contributes 1% = Rs. 370 per month. Total Rs. 2,220 per employee deposited with EOBI monthly.</div></div>
      <div class="faq-item"><div class="faq-q">What benefits do employees get from EOBI? <i class="fas fa-plus"></i></div><div class="faq-a">EOBI provides old-age pension, invalidity pension, survivors' pension, and old-age grant. Employees become entitled after 15 years of contribution and reaching 60 years of age (55 for women).</div></div>
    </div>
  </div>
</section>
<section class="cta-strip">
  <div class="container">
    <h2>Get EOBI Registered Today</h2>
    <p>5 or more employees? EOBI registration is legally required. We complete the process in 7-14 days.</p>
    <div class="cta-btns"><a href="https://wa.me/923284675162" class="btn-white"><i class="fab fa-whatsapp"></i> WhatsApp Now</a><a href="tel:03284675162" class="btn-ghost-white"><i class="fas fa-phone"></i> 0328-4675162</a></div>
  </div>
</section>
'@

MkSvcPage "eobi-registration" "EOBI Registration Service Pakistan 2026 | Employer Compliance | Kamboh Associates" "EOBI employer registration and monthly contribution filing. Punjab PESSI, WWF compliance. From Rs. 8,000 one-time registration. WhatsApp 0328-4675162. All cities Pakistan." "eobi-registration" $hero6 $main6

Write-Host "`nAll service pages done!"
