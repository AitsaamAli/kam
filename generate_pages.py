#!/usr/bin/env python3
"""Generate all 427 missing GSC 404 pages for kambohassociates.com"""
import os, re

BLOGS_DIR = os.path.join(os.path.dirname(__file__), 'blogs')

NAV = '''<div class="topbar"><div class="container"><div class="topbar-left"><div class="topbar-promo-wrap"><span class="topbar-promo">File Your Taxes In Just 6 Minutes With Our Qualified Consultants! &nbsp;&nbsp;&bull;&nbsp;&nbsp; Now Available in Just Rs. 3,500/- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="topbar-promo" aria-hidden="true">File Your Taxes In Just 6 Minutes With Our Qualified Consultants! &nbsp;&nbsp;&bull;&nbsp;&nbsp; Now Available in Just Rs. 3,500/- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></div></div></div></div>
<nav class="navbar" id="navbar"><div class="container"><a href="/" class="logo"><div><svg width="44" height="44" viewBox="0 0 46 46" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1a3a1a"/><stop offset="100%" stop-color="#0d2a0d"/></linearGradient><linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#F0CF6B"/><stop offset="100%" stop-color="#D4AF37"/></linearGradient></defs><circle cx="23" cy="23" r="23" fill="url(#logoGrad)"/><circle cx="23" cy="23" r="21" fill="none" stroke="url(#goldGrad)" stroke-width="1.5"/><text x="23" y="27" font-family="Cinzel,serif" font-size="13" font-weight="700" fill="url(#goldGrad)" text-anchor="middle" letter-spacing="1">KA</text><path id="circle-path" d="M 23,23 m -17,0 a 17,17 0 1,1 34,0 a 17,17 0 1,1 -34,0" fill="none"/><text font-family="Cinzel,serif" font-size="3.8" fill="#D4AF37" letter-spacing="1.8"><textPath href="#circle-path" startOffset="3%">KAMBOH ASSOCIATES &bull; TAX CONSULTANT &bull;</textPath></text></svg></div><div><div class="logo-name">KAMBOH ASSOCIATES</div><div class="logo-sub">Tax &amp; Regulatory Excellence</div></div></a><ul class="nav-links"><li><a href="/">Home</a></li><li><a href="/income-tax-filing">Services <i class="fas fa-chevron-down"></i></a><div class="nav-drop"><a href="/income-tax-filing"><i class="fas fa-file-invoice-dollar"></i> Income Tax Filing</a><a href="/ntn-registration"><i class="fas fa-id-card"></i> NTN Registration</a><a href="/sales-tax-registration"><i class="fas fa-percent"></i> Sales Tax Registration</a><a href="/secp-vs-sole-proprietorship-pakistan"><i class="fas fa-building"></i> SECP Company Registration</a><a href="/fbr-notice-defense"><i class="fas fa-shield-alt"></i> FBR Notice Defense</a><a href="/wealth-statement"><i class="fas fa-wallet"></i> Wealth Statement</a><a href="/pricing"><i class="fas fa-tags"></i> Pricing &amp; Fees</a></div></li><li><a href="/pricing">Pricing</a></li><li><a href="/testimonials">Reviews <span style="background:#14B8A6;color:#fff;font-size:.58rem;padding:1px 5px;border-radius:8px;font-weight:700">4.9&#9733;</span></a></li><li><a href="/contact">Contact</a></li><li><a href="/blogs" class="active">Blog</a></li></ul><div class="nav-actions"><span class="nav-phone"><i class="fas fa-phone"></i><a href="tel:03284675162">0328-4675162</a></span><a href="/contact" class="nav-cta">Get Started</a><button class="hamburger" id="hamburger" onclick="this.classList.toggle('open');document.getElementById('mobileNav').classList.toggle('open')" aria-label="Menu"><span></span><span></span><span></span></button></div></div><div class="mobile-nav" id="mobileNav"><a href="/">Home</a><a href="/income-tax-filing">Services</a><a href="/pricing">Pricing</a><a href="/blogs">Blog</a><a href="/contact">Contact</a><a href="https://wa.me/923284675162" target="_blank" style="color:#25D366"><i class="fab fa-whatsapp" style="margin-right:8px"></i>WhatsApp</a></div></nav>'''

CSS = '''<style>
:root{--t:#14B8A6;--n:#0F172A;--g:#D4AF37;--fs:"Cormorant Garamond",Georgia,serif;--fb:"DM Sans",system-ui,sans-serif;--fd:"Cinzel",serif}
[data-theme="light"]{--bg:#fff;--bg2:#F8F9FA;--bg3:#F1F3F5;--bd:#E2E8F0;--tx:#0F172A;--tx2:#334155;--tx3:#64748B;--sh:0 1px 3px rgba(0,0,0,.08),0 4px 16px rgba(0,0,0,.06)}
[data-theme="dark"]{--bg:#0A0F1E;--bg2:#0F172A;--bg3:#1E293B;--bd:rgba(255,255,255,.08);--tx:#F1F5F9;--tx2:#CBD5E1;--tx3:#64748B;--sh:0 1px 3px rgba(0,0,0,.4),0 4px 16px rgba(0,0,0,.3)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}body{font-family:var(--fb);background:var(--bg);color:var(--tx);line-height:1.65;overflow-x:hidden}
a{text-decoration:none;color:inherit}img{max-width:100%;display:block}ul{list-style:none}
::-webkit-scrollbar{width:5px}::-webkit-scrollbar-thumb{background:#14B8A6;border-radius:4px}
.container{max-width:1200px;margin:0 auto;padding:0 24px}
.topbar{background:#0F172A;border-bottom:1px solid rgba(255,255,255,.2);padding:9px 0;font-size:.75rem}
.topbar .container{display:flex;align-items:center}
.topbar-left{flex:1;overflow:hidden;white-space:nowrap}.topbar-promo-wrap{display:inline-flex;animation:kascroll 26s linear infinite}.topbar-promo{font-family:var(--fd);font-size:.68rem;letter-spacing:.04em;color:rgba(148,163,184,.9);white-space:nowrap;flex-shrink:0}@keyframes kascroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.navbar{position:sticky;top:0;z-index:1000;background:rgba(255,255,255,.97);backdrop-filter:blur(20px);border-bottom:1px solid #E2E8F0}
.navbar.scrolled{box-shadow:0 4px 24px rgba(15,23,42,.08)}
.navbar .container{display:flex;align-items:center;justify-content:space-between;height:68px}
.logo{display:flex;align-items:center;gap:12px}
.logo-name{font-family:var(--fd);font-size:.92rem;font-weight:700;color:#0F172A;letter-spacing:.07em;line-height:1.2}
.logo-sub{font-size:.56rem;letter-spacing:.18em;color:#D4AF37;text-transform:uppercase}
.nav-links{display:flex;align-items:center;gap:4px;list-style:none}
.nav-links>li{position:relative}
.nav-links>li>a{font-size:.84rem;font-weight:500;color:#1E293B;display:flex;align-items:center;gap:4px;padding:8px 14px;border-radius:8px;transition:all .2s}
.nav-links>li>a:hover{color:#14B8A6;background:#F0FDFA}
.nav-drop{position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%) translateY(-6px);z-index:2000;min-width:200px;background:#fff;border:1px solid #E2E8F0;border-radius:12px;box-shadow:0 8px 32px rgba(15,23,42,.12);padding:8px;opacity:0;visibility:hidden;transition:all .2s}
.nav-links>li:hover .nav-drop{opacity:1;visibility:visible;transform:translateX(-50%) translateY(0)}
.nav-drop a{display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:8px;font-size:.82rem;color:#1E293B;transition:all .15s}
.nav-drop a:hover{background:#F0FDFA;color:#14B8A6}
.nav-drop a i{width:16px;text-align:center;color:#14B8A6;font-size:.78rem}
.nav-actions{display:flex;align-items:center;gap:10px}
.nav-phone{font-size:.8rem;color:#64748B;display:flex;align-items:center;gap:6px}
.nav-phone i{color:#14B8A6}.nav-phone a{color:#1E293B;font-weight:500}
.nav-cta{background:#0F172A;color:#fff!important;padding:8px 18px!important;border-radius:8px!important;font-size:.82rem!important;font-weight:600!important;transition:all .2s!important}
.nav-cta:hover{background:#14B8A6!important}
.hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:4px;background:none;border:none}
.hamburger span{width:22px;height:2px;background:#64748B;border-radius:2px;display:block}
.mobile-nav{display:none;flex-direction:column;position:fixed;left:0;right:0;z-index:999;background:#fff;border-bottom:3px solid #14B8A6;box-shadow:0 12px 40px rgba(0,0,0,.15);max-height:calc(100vh - 68px);overflow-y:auto}
.mobile-nav.open{display:flex}
.mobile-nav a{padding:16px 24px;border-bottom:1px solid #F1F5F9;font-size:.9rem;color:#64748B}
.hero{background:#F8F9FA;border-bottom:1px solid #E2E8F0;padding:56px 0 48px;position:relative;overflow:hidden}
.hero::before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(20,184,166,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(20,184,166,.04) 1px,transparent 1px);background-size:52px 52px}
.hero .container{position:relative;z-index:2}
.breadcrumb{display:flex;align-items:center;gap:8px;font-size:.78rem;color:#94A3B8;margin-bottom:24px;flex-wrap:wrap}
.breadcrumb a{color:#94A3B8;transition:color .2s}.breadcrumb a:hover{color:#14B8A6}.breadcrumb i{font-size:.55rem}
.badge{display:inline-flex;align-items:center;gap:5px;background:rgba(20,184,166,.07);border:1px solid rgba(20,184,166,.2);border-radius:100px;padding:4px 14px;font-size:.68rem;color:#14B8A6;font-family:var(--fd);letter-spacing:.1em;text-transform:uppercase;margin-bottom:16px}
.hero h1{font-family:var(--fs);font-size:clamp(1.9rem,4vw,3rem);font-weight:700;color:#0F172A;line-height:1.12;margin-bottom:18px;max-width:780px}
.hero-meta{display:flex;flex-wrap:wrap;gap:20px;align-items:center;margin-top:24px}
.meta-item{display:flex;align-items:center;gap:6px;font-size:.8rem;color:#64748B}
.meta-item i{color:#14B8A6;font-size:.8rem}
.layout{display:grid;grid-template-columns:1fr 320px;gap:56px;padding:60px 0 100px;align-items:start}
.article{background:#fff;border:1px solid #E2E8F0;border-radius:20px;padding:44px 48px;box-shadow:var(--sh)}
.article p.lead{font-family:var(--fs);font-size:1.2rem;color:#334155;line-height:1.8;margin-bottom:36px;padding-bottom:28px;border-bottom:1px solid #E2E8F0}
.article h2{font-family:var(--fs);font-size:1.65rem;font-weight:600;color:#0F172A;margin:40px 0 16px;line-height:1.2;display:flex;align-items:center;gap:12px}
.article h2::before{content:"";width:4px;height:28px;background:linear-gradient(135deg,#14B8A6,#0D9488);border-radius:2px;flex-shrink:0}
.article h3{font-family:var(--fs);font-size:1.2rem;font-weight:600;color:#0F172A;margin:28px 0 12px}
.article p{font-size:.97rem;color:#334155;line-height:1.82;margin-bottom:18px}
.article a{color:#14B8A6;border-bottom:1px solid rgba(20,184,166,.2)}
.article ul,.article ol{margin:10px 0 18px 20px;display:flex;flex-direction:column;gap:6px}
.article ul li{font-size:.95rem;color:#334155;list-style:disc;line-height:1.7}
.article ol li{font-size:.95rem;color:#334155;list-style:decimal;line-height:1.7}
table.dt{width:100%;border-collapse:collapse;margin:22px 0 32px;font-size:.87rem;border-radius:12px;overflow:hidden;border:1px solid #E2E8F0}
table.dt thead tr{background:linear-gradient(135deg,#0F766E,#14B8A6);color:#fff}
table.dt thead th{padding:14px 16px;text-align:left;font-family:var(--fd);font-size:.65rem;letter-spacing:.1em;text-transform:uppercase}
table.dt tbody tr{border-bottom:1px solid #E2E8F0}
table.dt td{padding:13px 16px;color:#334155;line-height:1.5}
table.dt td:first-child{font-weight:500;color:#0F172A}
.ib{display:flex;align-items:flex-start;gap:14px;background:rgba(20,184,166,.06);border:1px solid rgba(20,184,166,.2);border-radius:12px;padding:18px 20px;margin:20px 0 24px}
.ib i{color:#14B8A6;font-size:1.1rem;flex-shrink:0;margin-top:2px}
.ib p{font-size:.88rem;color:#334155;margin:0;line-height:1.7}
.ig{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:16px;margin:22px 0}
.ic{background:#F8F9FA;border:1px solid #E2E8F0;border-radius:12px;padding:18px;border-top:3px solid #14B8A6}
.ic .lb{font-size:.72rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:#0D9488;margin-bottom:6px}
.ic .vl{font-size:1rem;font-weight:700;color:#0F172A}
.ic .sb{font-size:.78rem;color:#64748B;margin-top:4px}
.fq{display:flex;flex-direction:column;gap:12px;margin:20px 0 28px}
.fi{background:#F8F9FA;border:1px solid #E2E8F0;border-radius:12px;overflow:hidden}
.fi:hover{border-color:rgba(20,184,166,.3)}
.fq-q{display:flex;justify-content:space-between;align-items:center;padding:16px 18px;cursor:pointer;font-weight:600;font-size:.9rem;color:#0F172A;gap:12px}
.fq-q i{color:#14B8A6;transition:transform .3s;flex-shrink:0;font-size:.8rem}
.fi.open .fq-q i{transform:rotate(45deg)}
.fq-a{display:none;padding:0 18px 16px;font-size:.87rem;color:#64748B;line-height:1.75}
.fi.open .fq-a{display:block}
.cta-box{background:linear-gradient(135deg,#0F766E,#14B8A6);border-radius:20px;padding:36px 40px;text-align:center;margin:40px 0 0;color:#fff}
.cta-box h3{font-family:var(--fs);font-size:1.6rem;margin-bottom:10px}
.cta-box p{font-size:.9rem;opacity:.9;margin-bottom:24px;line-height:1.7;max-width:480px;margin-left:auto;margin-right:auto}
.cta-btns{display:flex;gap:10px;justify-content:center;flex-wrap:wrap}
.btn-w{background:#fff;color:#0F766E;padding:12px 26px;border-radius:8px;font-weight:600;font-size:.88rem;display:inline-flex;align-items:center;gap:8px;transition:all .2s;text-decoration:none}
.btn-w:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.2)}
.btn-g{background:transparent;color:#fff;padding:11px 26px;border-radius:8px;font-size:.88rem;display:inline-flex;align-items:center;gap:8px;border:1.5px solid rgba(255,255,255,.4);transition:all .2s;text-decoration:none}
.sidebar{display:flex;flex-direction:column;gap:20px;position:sticky;top:90px}
.sc{background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:22px}
.st{font-family:var(--fd);font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;color:#14B8A6;margin-bottom:16px;display:flex;align-items:center;gap:8px}
.cc{background:linear-gradient(135deg,#0F766E,#14B8A6);border-radius:12px;padding:26px;text-align:center;color:#fff}
.cc h3{font-family:var(--fs);font-size:1.2rem;margin-bottom:8px}
.cc p{font-size:.83rem;opacity:.9;margin-bottom:18px;line-height:1.6}
.cc a{display:inline-flex;align-items:center;gap:7px;background:#fff;color:#0F766E;padding:10px 20px;border-radius:7px;font-weight:600;font-size:.83rem;text-decoration:none}
.rl{display:flex;flex-direction:column;gap:4px}
.rl a{display:flex;align-items:center;gap:8px;padding:8px 10px;border-radius:7px;font-size:.84rem;color:#64748B;transition:all .2s;border:none}
.rl a:hover{background:rgba(20,184,166,.07);color:#14B8A6}
.rl a i{color:#14B8A6;font-size:.65rem;flex-shrink:0}
footer{background:#0F172A;border-top:1px solid rgba(255,255,255,.06);padding:40px 0;text-align:center;color:#64748B}
.fl{font-family:var(--fd);font-size:1.1rem;color:#D4AF37;letter-spacing:.1em;margin-bottom:12px}
.flr{display:flex;justify-content:center;gap:28px;margin:16px 0;flex-wrap:wrap}
.flr a{color:#64748B;font-size:.85rem;transition:color .2s}
.flr a:hover{color:#D4AF37}
.fc{font-size:.78rem;margin-top:8px}
.wa-float{position:fixed;bottom:24px;right:24px;z-index:9999;display:flex;align-items:center;justify-content:center;width:58px;height:58px;background:#25D366;border-radius:50%;box-shadow:0 4px 16px rgba(37,211,102,.5);text-decoration:none;animation:waPulse 2s infinite}
@keyframes waPulse{0%,100%{box-shadow:0 4px 16px rgba(37,211,102,.5)}50%{box-shadow:0 4px 28px rgba(37,211,102,.85),0 0 0 8px rgba(37,211,102,.15)}}
.reveal{opacity:0;transform:translateY(24px);transition:opacity .6s,transform .6s}.reveal.visible{opacity:1;transform:none}
@media(max-width:1024px){.layout{grid-template-columns:1fr}.sidebar{position:static}}
@media(max-width:768px){.nav-links,.nav-phone,.nav-cta{display:none!important}.hamburger{display:flex!important}.layout{padding:36px 0 60px}.article{padding:26px 22px}}
@media(max-width:480px){.container{padding:0 16px}.hero{padding:36px 0 32px}}
</style>'''

JS = '''<script>
window.addEventListener('scroll',function(){var nb=document.getElementById('navbar');if(nb)nb.classList.toggle('scrolled',window.scrollY>60);});
document.querySelectorAll('.fq-q').forEach(q=>q.addEventListener('click',()=>{var fi=q.closest('.fi');var open=fi.classList.contains('open');document.querySelectorAll('.fi.open').forEach(i=>i.classList.remove('open'));if(!open)fi.classList.add('open');}));
var ro=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');ro.unobserve(e.target);}});},{threshold:0});
document.querySelectorAll('.reveal').forEach(function(el){var r=el.getBoundingClientRect();if(r.top<(window.innerHeight||document.documentElement.clientHeight)&&r.bottom>0){el.classList.add('visible');}else{ro.observe(el);}});
</script>'''

WA_BTN = '''<a href="https://wa.me/923284675162?text=Hello%20Kamboh%20Associates%2C%20I%20need%20tax%20consultation." target="_blank" rel="noopener noreferrer" aria-label="WhatsApp" class="wa-float"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" fill="#fff"><path d="M16 0C7.163 0 0 7.163 0 16c0 2.822.736 5.476 2.027 7.785L0 32l8.469-2.001A15.93 15.93 0 0016 32c8.837 0 16-7.163 16-16S24.837 0 16 0zm0 29.333a13.27 13.27 0 01-6.77-1.855l-.485-.288-5.024 1.188 1.228-4.893-.317-.502A13.267 13.267 0 012.667 16C2.667 8.636 8.636 2.667 16 2.667S29.333 8.636 29.333 16 23.364 29.333 16 29.333zm7.27-9.862c-.398-.199-2.354-1.162-2.72-1.294-.365-.133-.631-.199-.897.199-.265.398-1.029 1.294-1.261 1.56-.232.265-.465.299-.863.1-.398-.199-1.681-.619-3.202-1.977-1.183-1.057-1.981-2.362-2.213-2.76-.232-.398-.025-.613.175-.811.179-.179.398-.465.597-.698.199-.232.265-.398.398-.664.133-.265.066-.498-.033-.697-.1-.199-.897-2.163-1.229-2.96-.324-.777-.653-.672-.897-.684l-.764-.013c-.265 0-.697.1-1.062.498-.365.398-1.394 1.362-1.394 3.322s1.428 3.853 1.627 4.119c.199.265 2.808 4.287 6.804 6.014.951.411 1.693.656 2.271.84.954.304 1.823.261 2.509.158.765-.114 2.354-.962 2.686-1.891.333-.929.333-1.726.233-1.891-.1-.165-.365-.265-.764-.464z"/></svg></a>'''

FOOTER = '''<footer><div class="container"><div class="fl">KAMBOH ASSOCIATES</div><p style="font-size:.82rem;color:#64748B;margin-bottom:8px">Tax &amp; Regulatory Excellence &mdash; Serving Pakistan Nationwide</p><div class="flr"><a href="/">Home</a><a href="/#services">Services</a><a href="/blogs">Blog</a><a href="/tax-calculator">Tax Tools</a><a href="/contact">Contact</a><a href="https://wa.me/923284675162" target="_blank">WhatsApp</a></div><div class="fc">&copy; 2026 Kamboh Associates. All rights reserved. | <a href="tel:03284675162" style="color:#D4AF37">0328-4675162</a></div></div></footer>'''

HEAD_COMMON = '''<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?display=swap&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=DM+Sans:wght@400;500;600&family=Cinzel:wght@600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"/>
<link rel="icon" type="image/jpeg" href="/images/logo.jpg"/>
<link rel="stylesheet" href="/mobile-fixes.css"/>
<script>(function(){var t=localStorage.getItem('site-theme');if(t)document.documentElement.setAttribute('data-theme',t);else if(window.matchMedia('(prefers-color-scheme: dark)').matches)document.documentElement.setAttribute('data-theme','dark');})();</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-2ZLVR968Y8"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-2ZLVR968Y8');</script>'''


def slug_to_title(slug):
    return ' '.join(w.capitalize() for w in slug.split('-'))


def detect_city(slug, prefix):
    loc = slug[len(prefix):]
    parts = loc.split('-')
    city_words = ['lahore','islamabad','karachi','faisalabad','rawalpindi','multan',
                  'peshawar','quetta','sialkot','gujranwala','hyderabad','abbottabad','bahawalpur']
    for cw in city_words:
        if loc.endswith(cw):
            return cw.capitalize()
    return ' '.join(w.capitalize() for w in parts[-1:])


def make_tc_page(slug):
    loc_raw = slug[len('tax-consultant-'):]
    location = slug_to_title(loc_raw)
    parts = loc_raw.split('-')
    city = parts[-1].capitalize()
    url = f'https://kambohassociates.com/blogs/{slug}'
    title = f'Best Tax Consultant in {location} | Kamboh Associates'
    desc = f'Top tax consultant in {location}. NTN registration, income tax filing, FBR compliance — affordable, remote, expert service. WhatsApp: 0328-4675162.'
    wa_msg = f'Hi%2C+I+need+tax+help+in+{location.replace(" ","+")}'

    schema = f'''[
  {{"@context":"https://schema.org","@type":"Article","headline":"Best Tax Consultant in {location}","datePublished":"2026-07-17","author":{{"@type":"Organization","name":"Kamboh Associates"}}}},
  {{"@context":"https://schema.org","@type":"LocalBusiness","name":"Kamboh Associates","address":{{"@type":"PostalAddress","addressLocality":"{location}","addressCountry":"PK"}},"telephone":"+923284675162","url":"https://kambohassociates.com","areaServed":"{location}","priceRange":"Rs 3,500+"}},
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://kambohassociates.com/"}},{{"@type":"ListItem","position":2,"name":"Blog","item":"https://kambohassociates.com/blogs"}},{{"@type":"ListItem","position":3,"name":"Tax Consultant in {location}","item":"{url}"}}]}}
]'''

    content = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large"/>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="geo.placename" content="{location}"/>
<meta property="og:type" content="article"/>
<meta property="og:title" content="Best Tax Consultant in {location}"/>
<meta property="og:url" content="{url}"/>
<link rel="canonical" href="{url}"/>
{HEAD_COMMON}
<script type="application/ld+json">{schema}</script>
{CSS}
</head>
<body>
{NAV}
<section class="hero">
  <div class="container">
    <div class="breadcrumb"><a href="/"><i class="fas fa-home"></i> Home</a><i class="fas fa-chevron-right"></i><a href="/blogs">Blog</a><i class="fas fa-chevron-right"></i><span>Tax Consultant in {location}</span></div>
    <div class="badge"><i class="fas fa-map-marker-alt"></i> Local Tax Guide</div>
    <h1>Best Tax Consultant in {location}</h1>
    <div class="hero-meta">
      <div class="meta-item"><i class="far fa-calendar-alt"></i> July 2026</div>
      <div class="meta-item"><i class="fas fa-user-tie"></i> Kamboh Associates</div>
      <div class="meta-item"><i class="far fa-clock"></i> 6 min read</div>
      <div class="meta-item"><i class="fas fa-map-pin"></i> {location}</div>
    </div>
  </div>
</section>
<div class="container">
  <div class="layout">
    <article>
      <div class="article reveal">
        <p class="lead">Kamboh Associates provides expert FBR tax and compliance services to all residents and businesses in {location}. Whether you need <a href="/ntn-registration">NTN registration</a>, income tax filing, <a href="/wealth-statement">wealth statement</a>, or help responding to <a href="/fbr-notice-defense">FBR notices</a> — our qualified consultants handle everything remotely. No office visit required. WhatsApp your documents to 0328-4675162 and we begin immediately.</p>
        <h2 id="why">Why {location} Taxpayers Need a Tax Consultant in 2026</h2>
        <p>FBR now cross-references taxpayer data with banks, utility companies, property registries, vehicle registration databases, and telecom operators. If your declared income does not match this third-party data, FBR automatically generates notices. A qualified tax consultant ensures full compliance and helps you avoid costly penalties.</p>
        <div class="ib"><i class="fas fa-lightbulb"></i><p><strong>Key Benefit for {location} Residents:</strong> Being a tax filer saves significant money on every major financial transaction. Property purchases, vehicle registration, banking, and utilities all carry 50% lower withholding tax for ATL filers. Annual filing costs just Rs 3,500 — the annual savings can be Rs 50,000 to Rs 500,000+.</p></div>
        <h2 id="services">Our Services for {location} Clients</h2>
        <ul>
          <li><strong>NTN Registration</strong> — Get your tax number within 24–48 hours</li>
          <li><strong>Income Tax Return Filing</strong> — Annual FBR return from Rs 3,500</li>
          <li><strong>Sales Tax / GST Registration</strong> — FBR STRN and PRA registration</li>
          <li><strong>Wealth Statement Preparation</strong> — Accurate, FBR-defensible statements</li>
          <li><strong>FBR Notice Response</strong> — Professional replies to all notice types</li>
          <li><strong>Company Registration</strong> — SECP and District Administration</li>
          <li><strong>Corporate Tax Filing</strong> — Complete company tax compliance</li>
        </ul>
        <h2 id="filer-benefits">Benefits of Being a Tax Filer</h2>
        <div class="ig">
          <div class="ic"><div class="lb">Property Purchase</div><div class="vl">3% vs 6%</div><div class="sb">Filer vs non-filer WHT</div></div>
          <div class="ic"><div class="lb">Vehicle Registration</div><div class="vl">50% Less</div><div class="sb">Token tax for filers</div></div>
          <div class="ic"><div class="lb">Bank Profit Tax</div><div class="vl">15% vs 35%</div><div class="sb">Filer vs non-filer</div></div>
          <div class="ic"><div class="lb">Filing Cost</div><div class="vl">Rs 3,500</div><div class="sb">Starting price 2026</div></div>
        </div>
        <h2 id="process">How to Get Started — Step by Step</h2>
        <ol>
          <li><strong>WhatsApp your CNIC</strong> to 0328-4675162</li>
          <li><strong>We assess your situation</strong> and advise on what is required</li>
          <li><strong>NTN registration</strong> completed within 24–48 business hours</li>
          <li><strong>Share financial documents</strong> securely via WhatsApp</li>
          <li><strong>We prepare your complete return</strong> with all eligible deductions applied</li>
          <li><strong>We file on FBR IRIS</strong> and send you the official acknowledgment</li>
          <li><strong>ATL status activates</strong> within 3–7 days of filing</li>
        </ol>
        <h2 id="pricing">Transparent Pricing — No Hidden Charges</h2>
        <table class="dt">
          <thead><tr><th>Service</th><th>Starting Price</th><th>Timeline</th></tr></thead>
          <tbody>
            <tr><td>NTN Registration</td><td>Rs 1,500</td><td>24–48 hours</td></tr>
            <tr><td>Salaried Tax Return</td><td>Rs 3,500</td><td>Same day</td></tr>
            <tr><td>Business Tax Return</td><td>Rs 7,000</td><td>2–3 days</td></tr>
            <tr><td>Wealth Statement</td><td>Rs 5,000</td><td>2–3 days</td></tr>
            <tr><td>Sales Tax Registration</td><td>Rs 5,000</td><td>7–14 days</td></tr>
            <tr><td>Company Registration</td><td>Rs 8,000</td><td>5–10 days</td></tr>
            <tr><td>FBR Notice Response</td><td>Rs 5,000</td><td>24–48 hours</td></tr>
          </tbody>
        </table>
        <div class="cta-box">
          <h3>Get Expert Tax Help in {location} Today</h3>
          <p>Kamboh Associates serves all {location} clients remotely. Share your documents via WhatsApp and we handle everything — free first consultation.</p>
          <div class="cta-btns">
            <a href="https://wa.me/923284675162?text={wa_msg}" class="btn-w" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> Free Consultation</a>
            <a href="tel:03284675162" class="btn-g"><i class="fas fa-phone"></i> 0328-4675162</a>
          </div>
        </div>
        <h2 id="faqs">Frequently Asked Questions</h2>
        <div class="fq">
          <div class="fi"><div class="fq-q">Who needs to file income tax in {location}? <i class="fas fa-plus"></i></div><div class="fq-a">Any individual in {location} earning above Rs 600,000 per year from salary, business, rental income, or freelancing must file an annual income tax return with FBR by September 30 each year. NTN registration is the first step.</div></div>
          <div class="fi"><div class="fq-q">How much does tax filing cost? <i class="fas fa-plus"></i></div><div class="fq-a">Kamboh Associates pricing: Salaried individuals from Rs 3,500, Business owners from Rs 7,000, Property investors with wealth statement from Rs 8,000. All prices include FBR portal filing and official acknowledgment certificate.</div></div>
          <div class="fi"><div class="fq-q">Do I need to visit your office? <i class="fas fa-plus"></i></div><div class="fq-a">No. We serve all {location} clients completely remotely. Simply WhatsApp your documents to 0328-4675162 and we complete your entire tax filing online. No office visit is required at any stage.</div></div>
          <div class="fi"><div class="fq-q">What is the income tax return deadline in Pakistan? <i class="fas fa-plus"></i></div><div class="fq-a">The annual income tax return deadline is September 30 each year. Filing after this date attracts late filing penalties starting at 5% of tax payable. We recommend filing before August 31 to avoid last-minute issues.</div></div>
          <div class="fi"><div class="fq-q">How quickly can you register my NTN? <i class="fas fa-plus"></i></div><div class="fq-a">Kamboh Associates completes NTN registration within 24 to 48 business hours. WhatsApp your CNIC copy and basic details and we begin the FBR IRIS application immediately.</div></div>
        </div>
      </div>
      <div style="margin-top:32px">
        <h2 style="font-family:'Cormorant Garamond',serif;font-size:1.35rem;color:#0F172A;margin-bottom:16px;display:flex;align-items:center;gap:10px"><span style="width:4px;height:22px;background:linear-gradient(135deg,#14B8A6,#0D9488);border-radius:2px;display:inline-block;flex-shrink:0"></span>Our Tax Services</h2>
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:8px">
          <a href="/income-tax-filing" style="display:flex;align-items:center;gap:8px;padding:9px 14px;border:1px solid #E2E8F0;border-radius:8px;font-size:.83rem;color:#1E293B;transition:all .2s" onmouseover="this.style.borderColor='#14B8A6';this.style.color='#14B8A6'" onmouseout="this.style.borderColor='#E2E8F0';this.style.color='#1E293B'"><i class="fas fa-file-invoice-dollar" style="color:#14B8A6;width:14px"></i><span>Income Tax Return Filing</span></a>
          <a href="/ntn-registration" style="display:flex;align-items:center;gap:8px;padding:9px 14px;border:1px solid #E2E8F0;border-radius:8px;font-size:.83rem;color:#1E293B;transition:all .2s" onmouseover="this.style.borderColor='#14B8A6';this.style.color='#14B8A6'" onmouseout="this.style.borderColor='#E2E8F0';this.style.color='#1E293B'"><i class="fas fa-id-card" style="color:#14B8A6;width:14px"></i><span>NTN Registration</span></a>
          <a href="/secp-vs-sole-proprietorship-pakistan" style="display:flex;align-items:center;gap:8px;padding:9px 14px;border:1px solid #E2E8F0;border-radius:8px;font-size:.83rem;color:#1E293B;transition:all .2s" onmouseover="this.style.borderColor='#14B8A6';this.style.color='#14B8A6'" onmouseout="this.style.borderColor='#E2E8F0';this.style.color='#1E293B'"><i class="fas fa-building" style="color:#14B8A6;width:14px"></i><span>Company Registration (SECP)</span></a>
          <a href="/sales-tax-registration" style="display:flex;align-items:center;gap:8px;padding:9px 14px;border:1px solid #E2E8F0;border-radius:8px;font-size:.83rem;color:#1E293B;transition:all .2s" onmouseover="this.style.borderColor='#14B8A6';this.style.color='#14B8A6'" onmouseout="this.style.borderColor='#E2E8F0';this.style.color='#1E293B'"><i class="fas fa-percent" style="color:#14B8A6;width:14px"></i><span>Sales Tax Registration</span></a>
          <a href="/fbr-notice-defense" style="display:flex;align-items:center;gap:8px;padding:9px 14px;border:1px solid #E2E8F0;border-radius:8px;font-size:.83rem;color:#1E293B;transition:all .2s" onmouseover="this.style.borderColor='#14B8A6';this.style.color='#14B8A6'" onmouseout="this.style.borderColor='#E2E8F0';this.style.color='#1E293B'"><i class="fas fa-shield-alt" style="color:#14B8A6;width:14px"></i><span>FBR Notice Defense</span></a>
          <a href="/wealth-statement" style="display:flex;align-items:center;gap:8px;padding:9px 14px;border:1px solid #E2E8F0;border-radius:8px;font-size:.83rem;color:#1E293B;transition:all .2s" onmouseover="this.style.borderColor='#14B8A6';this.style.color='#14B8A6'" onmouseout="this.style.borderColor='#E2E8F0';this.style.color='#1E293B'"><i class="fas fa-wallet" style="color:#14B8A6;width:14px"></i><span>Wealth Statement</span></a>
          <a href="/pricing" style="display:flex;align-items:center;gap:8px;padding:9px 14px;border:1px solid #E2E8F0;border-radius:8px;font-size:.83rem;color:#1E293B;transition:all .2s" onmouseover="this.style.borderColor='#14B8A6';this.style.color='#14B8A6'" onmouseout="this.style.borderColor='#E2E8F0';this.style.color='#1E293B'"><i class="fas fa-tags" style="color:#14B8A6;width:14px"></i><span>Pricing &amp; Fees</span></a>
        </div>
      </div>
    </article>
    <aside class="sidebar">
      <div class="sc reveal"><div class="st"><i class="fas fa-list"></i> Contents</div><nav class="rl"><a href="#why"><i class="fas fa-circle"></i> Why It Matters</a><a href="#services"><i class="fas fa-circle"></i> Our Services</a><a href="#filer-benefits"><i class="fas fa-circle"></i> Filer Benefits</a><a href="#process"><i class="fas fa-circle"></i> How to Start</a><a href="#pricing"><i class="fas fa-circle"></i> Pricing</a><a href="#faqs"><i class="fas fa-circle"></i> FAQs</a></nav></div>
      <div class="sc cc reveal" style="transition-delay:.1s"><h3>Tax Help in {location}</h3><p>Expert FBR compliance from Kamboh Associates. First consultation free.</p><a href="https://wa.me/923284675162" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> WhatsApp Now</a></div>
      <div class="sc reveal" style="transition-delay:.2s"><div class="st"><i class="fas fa-phone"></i> Contact Now</div><p style="font-size:.85rem;color:#64748B;margin-bottom:12px">Free consultation available now</p><a href="tel:03284675162" style="display:flex;align-items:center;justify-content:center;gap:8px;background:#0F172A;color:#fff;padding:12px 16px;border-radius:8px;font-weight:600;font-size:.88rem;text-decoration:none;margin-bottom:8px"><i class="fas fa-phone"></i> 0328-4675162</a><a href="https://wa.me/923284675162" target="_blank" rel="noopener noreferrer" style="display:flex;align-items:center;justify-content:center;gap:8px;background:#25D366;color:#fff;padding:12px 16px;border-radius:8px;font-weight:600;font-size:.88rem;text-decoration:none"><i class="fab fa-whatsapp"></i> WhatsApp</a></div>
    </aside>
  </div>
</div>
{FOOTER}
{WA_BTN}
{JS}
</body>
</html>'''
    return content


def make_ntn_page(slug):
    city_raw = slug[len('ntn-registration-'):]
    city = slug_to_title(city_raw)
    url = f'https://kambohassociates.com/blogs/{slug}'
    title = f'NTN Registration in {city} | Online FBR | Kamboh Associates'
    desc = f'NTN registration in {city} — online, fast, just Rs 1,500. FBR IRIS application completed in 24-48 hours. WhatsApp 0328-4675162.'
    wa_msg = f'Hi%2C+I+need+NTN+registration+in+{city.replace(" ","+")}'

    schema = f'''[
  {{"@context":"https://schema.org","@type":"Article","headline":"NTN Registration in {city} | Online FBR","datePublished":"2026-07-17","author":{{"@type":"Organization","name":"Kamboh Associates"}}}},
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://kambohassociates.com/"}},{{"@type":"ListItem","position":2,"name":"Blog","item":"https://kambohassociates.com/blogs"}},{{"@type":"ListItem","position":3,"name":"NTN Registration in {city}","item":"{url}"}}]}}
]'''

    content = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large"/>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="geo.placename" content="{city}"/>
<meta property="og:type" content="article"/>
<meta property="og:title" content="NTN Registration in {city}"/>
<meta property="og:url" content="{url}"/>
<link rel="canonical" href="{url}"/>
{HEAD_COMMON}
<script type="application/ld+json">{schema}</script>
{CSS}
</head>
<body>
{NAV}
<section class="hero">
  <div class="container">
    <div class="breadcrumb"><a href="/"><i class="fas fa-home"></i> Home</a><i class="fas fa-chevron-right"></i><a href="/blogs">Blog</a><i class="fas fa-chevron-right"></i><span>NTN Registration in {city}</span></div>
    <div class="badge"><i class="fas fa-id-card"></i> NTN Registration Guide</div>
    <h1>NTN Registration in {city} — Online FBR 2026</h1>
    <div class="hero-meta">
      <div class="meta-item"><i class="far fa-calendar-alt"></i> July 2026</div>
      <div class="meta-item"><i class="fas fa-user-tie"></i> Kamboh Associates</div>
      <div class="meta-item"><i class="far fa-clock"></i> 5 min read</div>
      <div class="meta-item"><i class="fas fa-map-pin"></i> {city}</div>
    </div>
  </div>
</section>
<div class="container">
  <div class="layout">
    <article>
      <div class="article reveal">
        <p class="lead">Kamboh Associates completes NTN (National Tax Number) registration for all individuals and businesses in {city} within 24–48 hours — entirely online through FBR IRIS. No office visit required. Starting from just Rs 1,500, we handle the complete FBR application and send you your NTN certificate.</p>
        <h2 id="what">What is NTN and Why Do You Need It?</h2>
        <p>NTN (National Tax Number) is your unique FBR identification number required for all tax-related transactions in Pakistan. Without an NTN, you cannot file income tax returns, become a filer, or access ATL (Active Taxpayer List) benefits which reduce withholding tax rates by 50% on property, vehicles, banking, and more.</p>
        <div class="ib"><i class="fas fa-lightbulb"></i><p><strong>For {city} Residents:</strong> NTN registration is the first step to becoming a tax filer. Once registered, you can file your annual return and save Rs 50,000 to Rs 500,000+ annually through reduced withholding tax rates on every major financial transaction.</p></div>
        <h2 id="docs">Documents Required for NTN Registration</h2>
        <ul>
          <li><strong>CNIC copy</strong> — front and back (scanned or photo)</li>
          <li><strong>Phone number</strong> — registered on your CNIC</li>
          <li><strong>Email address</strong> — for FBR IRIS portal access</li>
          <li><strong>Business details</strong> — name, address, type (for businesses only)</li>
          <li><strong>Bank account details</strong> — for income source verification</li>
        </ul>
        <h2 id="process">NTN Registration Process — Step by Step</h2>
        <ol>
          <li><strong>WhatsApp your CNIC</strong> (front &amp; back) to 0328-4675162</li>
          <li><strong>We verify your data</strong> on FBR database immediately</li>
          <li><strong>Complete FBR IRIS application</strong> submitted by our team</li>
          <li><strong>OTP verification</strong> — we guide you through the 2-step process</li>
          <li><strong>NTN issued</strong> — you receive your number within 24–48 hours</li>
          <li><strong>Income tax return filing</strong> — we recommend filing immediately to get ATL status</li>
        </ol>
        <h2 id="pricing">NTN Registration Fees in {city}</h2>
        <table class="dt">
          <thead><tr><th>Service</th><th>Price</th><th>Timeline</th></tr></thead>
          <tbody>
            <tr><td>NTN Registration (Individual)</td><td>Rs 1,500</td><td>24–48 hours</td></tr>
            <tr><td>NTN Registration (Business/AOP)</td><td>Rs 2,500</td><td>24–48 hours</td></tr>
            <tr><td>NTN + First Tax Return</td><td>Rs 4,500</td><td>Same day filing</td></tr>
            <tr><td>NTN + Return + Wealth Statement</td><td>Rs 7,500</td><td>2–3 days</td></tr>
          </tbody>
        </table>
        <div class="cta-box">
          <h3>Get Your NTN Registered in {city} Today</h3>
          <p>WhatsApp your CNIC to 0328-4675162 and we complete your NTN registration within 24 hours. No office visit required.</p>
          <div class="cta-btns">
            <a href="https://wa.me/923284675162?text={wa_msg}" class="btn-w" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> WhatsApp Now</a>
            <a href="tel:03284675162" class="btn-g"><i class="fas fa-phone"></i> 0328-4675162</a>
          </div>
        </div>
        <h2 id="faqs">Frequently Asked Questions</h2>
        <div class="fq">
          <div class="fi"><div class="fq-q">How long does NTN registration take in {city}? <i class="fas fa-plus"></i></div><div class="fq-a">Kamboh Associates completes NTN registration for {city} clients within 24 to 48 business hours. Simply WhatsApp your CNIC copy and we begin the FBR IRIS application immediately.</div></div>
          <div class="fi"><div class="fq-q">What documents do I need for NTN registration? <i class="fas fa-plus"></i></div><div class="fq-a">You need your CNIC (front and back), a phone number registered on your CNIC, and an email address. For businesses, you also need the business name, address, and type of business.</div></div>
          <div class="fi"><div class="fq-q">Is NTN registration free in Pakistan? <i class="fas fa-plus"></i></div><div class="fq-a">FBR does not charge for NTN registration. The Rs 1,500 fee is for Kamboh Associates professional service — we handle the complete process, saving you time and errors on the FBR IRIS portal.</div></div>
          <div class="fi"><div class="fq-q">Can I get NTN registration online without visiting FBR office? <i class="fas fa-plus"></i></div><div class="fq-a">Yes. NTN registration is fully online through FBR IRIS. We complete the entire process remotely for {city} clients — no FBR office visit required at any stage.</div></div>
        </div>
      </div>
    </article>
    <aside class="sidebar">
      <div class="sc reveal"><div class="st"><i class="fas fa-list"></i> Contents</div><nav class="rl"><a href="#what"><i class="fas fa-circle"></i> What is NTN?</a><a href="#docs"><i class="fas fa-circle"></i> Documents Needed</a><a href="#process"><i class="fas fa-circle"></i> Registration Steps</a><a href="#pricing"><i class="fas fa-circle"></i> Fees</a><a href="#faqs"><i class="fas fa-circle"></i> FAQs</a></nav></div>
      <div class="sc cc reveal" style="transition-delay:.1s"><h3>NTN Registration {city}</h3><p>24–48 hour turnaround. Rs 1,500 only. Fully remote.</p><a href="https://wa.me/923284675162" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> WhatsApp Now</a></div>
      <div class="sc reveal" style="transition-delay:.2s"><div class="st"><i class="fas fa-phone"></i> Contact</div><a href="tel:03284675162" style="display:flex;align-items:center;justify-content:center;gap:8px;background:#0F172A;color:#fff;padding:12px 16px;border-radius:8px;font-weight:600;font-size:.88rem;text-decoration:none;margin-bottom:8px"><i class="fas fa-phone"></i> 0328-4675162</a><a href="https://wa.me/923284675162" target="_blank" rel="noopener noreferrer" style="display:flex;align-items:center;justify-content:center;gap:8px;background:#25D366;color:#fff;padding:12px 16px;border-radius:8px;font-weight:600;font-size:.88rem;text-decoration:none"><i class="fab fa-whatsapp"></i> WhatsApp</a></div>
    </aside>
  </div>
</div>
{FOOTER}
{WA_BTN}
{JS}
</body>
</html>'''
    return content


def make_itf_page(slug):
    city_raw = slug[len('income-tax-filing-'):]
    city = slug_to_title(city_raw)
    url = f'https://kambohassociates.com/blogs/{slug}'
    title = f'Income Tax Filing in {city} | FBR Return 2026 | Kamboh Associates'
    desc = f'Online income tax return filing in {city}. Expert FBR compliance from Rs 3,500. Salaried, business, freelancers — fully remote. WhatsApp 0328-4675162.'
    wa_msg = f'Hi%2C+I+need+income+tax+filing+in+{city.replace(" ","+")}'

    schema = f'''[
  {{"@context":"https://schema.org","@type":"Article","headline":"Income Tax Filing in {city}","datePublished":"2026-07-17","author":{{"@type":"Organization","name":"Kamboh Associates"}}}},
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://kambohassociates.com/"}},{{"@type":"ListItem","position":2,"name":"Blog","item":"https://kambohassociates.com/blogs"}},{{"@type":"ListItem","position":3,"name":"Income Tax Filing in {city}","item":"{url}"}}]}}
]'''

    content = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large"/>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="geo.placename" content="{city}"/>
<meta property="og:type" content="article"/>
<meta property="og:title" content="Income Tax Filing in {city}"/>
<meta property="og:url" content="{url}"/>
<link rel="canonical" href="{url}"/>
{HEAD_COMMON}
<script type="application/ld+json">{schema}</script>
{CSS}
</head>
<body>
{NAV}
<section class="hero">
  <div class="container">
    <div class="breadcrumb"><a href="/"><i class="fas fa-home"></i> Home</a><i class="fas fa-chevron-right"></i><a href="/blogs">Blog</a><i class="fas fa-chevron-right"></i><span>Income Tax Filing in {city}</span></div>
    <div class="badge"><i class="fas fa-file-invoice-dollar"></i> Income Tax Filing Guide</div>
    <h1>Income Tax Return Filing in {city} — FBR 2026</h1>
    <div class="hero-meta">
      <div class="meta-item"><i class="far fa-calendar-alt"></i> July 2026</div>
      <div class="meta-item"><i class="fas fa-user-tie"></i> Kamboh Associates</div>
      <div class="meta-item"><i class="far fa-clock"></i> 6 min read</div>
      <div class="meta-item"><i class="fas fa-map-pin"></i> {city}</div>
    </div>
  </div>
</section>
<div class="container">
  <div class="layout">
    <article>
      <div class="article reveal">
        <p class="lead">Kamboh Associates provides expert income tax return filing services for all residents and businesses in {city}. Salaried employees, business owners, freelancers, property investors — we file your complete FBR return from just Rs 3,500, entirely online. WhatsApp your documents to 0328-4675162 and we handle everything.</p>
        <h2 id="who">Who Must File Income Tax Return in {city}?</h2>
        <p>Under Pakistan's Income Tax Ordinance 2001, every individual earning above Rs 600,000 per year must file an annual income tax return with FBR. This includes salaried employees, business owners, freelancers, rental income earners, and property investors in {city}.</p>
        <div class="ib"><i class="fas fa-lightbulb"></i><p><strong>Deadline:</strong> The income tax return deadline is September 30 each year. Filing before this date avoids late filing penalties of 5% of tax payable per month. Kamboh Associates recommends filing before August 31 to ensure on-time submission.</p></div>
        <h2 id="benefits">Why File Income Tax Return in {city}?</h2>
        <div class="ig">
          <div class="ic"><div class="lb">Property WHT</div><div class="vl">3% vs 6%</div><div class="sb">Filer vs non-filer</div></div>
          <div class="ic"><div class="lb">Bank Profit Tax</div><div class="vl">15% vs 35%</div><div class="sb">Filer vs non-filer</div></div>
          <div class="ic"><div class="lb">Vehicle Token</div><div class="vl">50% Less</div><div class="sb">For ATL filers</div></div>
          <div class="ic"><div class="lb">Filing Cost</div><div class="vl">Rs 3,500</div><div class="sb">Starting price</div></div>
        </div>
        <h2 id="process">How to File Income Tax Return — Step by Step</h2>
        <ol>
          <li><strong>WhatsApp CNIC</strong> to 0328-4675162 — we check your FBR status</li>
          <li><strong>NTN registration</strong> if not already done (24 hours)</li>
          <li><strong>Share income documents</strong> — salary slips, bank statements, rental income proof</li>
          <li><strong>We calculate your tax</strong> and apply all eligible deductions</li>
          <li><strong>Review and approve</strong> the return before filing</li>
          <li><strong>Filed on FBR IRIS</strong> — you receive official acknowledgment</li>
          <li><strong>ATL active</strong> within 3–7 days — you are now a tax filer</li>
        </ol>
        <h2 id="pricing">Income Tax Filing Fees in {city}</h2>
        <table class="dt">
          <thead><tr><th>Category</th><th>Starting Price</th><th>Timeline</th></tr></thead>
          <tbody>
            <tr><td>Salaried Individual</td><td>Rs 3,500</td><td>Same day</td></tr>
            <tr><td>Business Owner / Self-Employed</td><td>Rs 7,000</td><td>2–3 days</td></tr>
            <tr><td>Freelancer / IT Professional</td><td>Rs 5,000</td><td>1–2 days</td></tr>
            <tr><td>Property Investor (with wealth statement)</td><td>Rs 8,000</td><td>2–3 days</td></tr>
            <tr><td>Company / AOP Return</td><td>Rs 15,000</td><td>3–5 days</td></tr>
          </tbody>
        </table>
        <div class="cta-box">
          <h3>File Your Income Tax Return in {city} Today</h3>
          <p>Same-day filing available. WhatsApp your CNIC and salary slip to 0328-4675162 — we begin immediately. Free consultation included.</p>
          <div class="cta-btns">
            <a href="https://wa.me/923284675162?text={wa_msg}" class="btn-w" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> WhatsApp Now</a>
            <a href="tel:03284675162" class="btn-g"><i class="fas fa-phone"></i> 0328-4675162</a>
          </div>
        </div>
        <h2 id="faqs">Frequently Asked Questions</h2>
        <div class="fq">
          <div class="fi"><div class="fq-q">What is the income tax return deadline? <i class="fas fa-plus"></i></div><div class="fq-a">The FBR income tax return deadline is September 30 each year for individuals, and December 31 for companies. Late filing attracts penalties of 5% of tax payable per month of delay.</div></div>
          <div class="fi"><div class="fq-q">What documents are needed to file tax return? <i class="fas fa-plus"></i></div><div class="fq-a">For salaried: salary slips or Form 16, CNIC. For business: accounts/bookkeeping, expenses record. For property: sale/purchase agreements, rental income proof. For overseas: remittance records.</div></div>
          <div class="fi"><div class="fq-q">Can I file tax return without visiting your office? <i class="fas fa-plus"></i></div><div class="fq-a">Yes — we serve all {city} clients fully remotely. Simply WhatsApp your documents to 0328-4675162 and we prepare and file your complete return online. No office visit needed.</div></div>
          <div class="fi"><div class="fq-q">What happens if I don't file income tax return? <i class="fas fa-plus"></i></div><div class="fq-a">Non-filers face higher withholding tax rates (double on property, vehicles, bank transactions), cannot purchase property above Rs 5 crore or vehicles above 1300cc, and may receive FBR Section 114 notices requiring filing under penalty.</div></div>
        </div>
      </div>
    </article>
    <aside class="sidebar">
      <div class="sc reveal"><div class="st"><i class="fas fa-list"></i> Contents</div><nav class="rl"><a href="#who"><i class="fas fa-circle"></i> Who Must File?</a><a href="#benefits"><i class="fas fa-circle"></i> Filer Benefits</a><a href="#process"><i class="fas fa-circle"></i> Filing Steps</a><a href="#pricing"><i class="fas fa-circle"></i> Pricing</a><a href="#faqs"><i class="fas fa-circle"></i> FAQs</a></nav></div>
      <div class="sc cc reveal" style="transition-delay:.1s"><h3>Tax Filing in {city}</h3><p>Expert FBR income tax return filing from Rs 3,500. Same-day service available.</p><a href="https://wa.me/923284675162" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> WhatsApp Now</a></div>
      <div class="sc reveal" style="transition-delay:.2s"><div class="st"><i class="fas fa-phone"></i> Contact</div><a href="tel:03284675162" style="display:flex;align-items:center;justify-content:center;gap:8px;background:#0F172A;color:#fff;padding:12px 16px;border-radius:8px;font-weight:600;font-size:.88rem;text-decoration:none;margin-bottom:8px"><i class="fas fa-phone"></i> 0328-4675162</a><a href="https://wa.me/923284675162" target="_blank" rel="noopener noreferrer" style="display:flex;align-items:center;justify-content:center;gap:8px;background:#25D366;color:#fff;padding:12px 16px;border-radius:8px;font-weight:600;font-size:.88rem;text-decoration:none"><i class="fab fa-whatsapp"></i> WhatsApp</a></div>
    </aside>
  </div>
</div>
{FOOTER}
{WA_BTN}
{JS}
</body>
</html>'''
    return content


def make_misc_page(slug):
    title_words = slug_to_title(slug.replace('-city','').replace('-karachi','').replace('-sialkot',''))
    if slug == 'it-export-income-tax-pakistan':
        page_title = 'IT Export Income Tax Pakistan 2026 | FBR Tax on Software Exports | Kamboh Associates'
        h1 = 'IT Export Income Tax in Pakistan — FBR Guide 2026'
        lead = 'Pakistan IT exports are subject to a preferential tax regime under FBR. Software exports, IT-enabled services, and freelance income earned in foreign currency qualify for special tax rates. Kamboh Associates helps IT companies and freelancers file their FBR returns correctly and claim all available exemptions. WhatsApp 0328-4675162 for free consultation.'
        badge = 'IT Export Tax Guide'
        badge_icon = 'fas fa-laptop-code'
        extra = '''<h2 id="rates">IT Export Tax Rates Pakistan 2026</h2>
        <table class="dt">
          <thead><tr><th>Category</th><th>Tax Rate</th><th>Condition</th></tr></thead>
          <tbody>
            <tr><td>Software Export (FBR certified)</td><td>0.25% FTR</td><td>On export receipts</td></tr>
            <tr><td>IT-Enabled Services</td><td>0.25% FTR</td><td>Foreign currency income</td></tr>
            <tr><td>Freelancer (Payoneer/Wise)</td><td>0.25% FTR</td><td>Foreign remittance</td></tr>
            <tr><td>Local IT Services</td><td>Normal slab rates</td><td>PKR income</td></tr>
          </tbody>
        </table>
        <h2 id="exemption">IT Export Exemption Certificate</h2>
        <p>IT companies can apply for an income tax exemption certificate from FBR under Section 65F of the Income Tax Ordinance. This provides full exemption on export income for certified IT companies. Kamboh Associates handles the complete exemption application process.</p>'''
    elif slug == 'tax-consultant-fees-pakistan':
        page_title = 'Tax Consultant Fees Pakistan 2026 | FBR Filing Cost | Kamboh Associates'
        h1 = 'Tax Consultant Fees in Pakistan 2026 — Complete Guide'
        lead = 'Tax consultant fees in Pakistan vary based on service type, complexity, and consultant experience. Kamboh Associates offers transparent, affordable pricing starting from Rs 1,500 for NTN registration to Rs 3,500 for income tax returns. All prices include FBR filing and official acknowledgment — no hidden charges.'
        badge = 'Tax Consultant Fees'
        badge_icon = 'fas fa-tags'
        extra = '''<h2 id="fees">Tax Consultant Fees — Market vs Kamboh Associates</h2>
        <table class="dt">
          <thead><tr><th>Service</th><th>Market Range</th><th>Kamboh Associates</th></tr></thead>
          <tbody>
            <tr><td>NTN Registration</td><td>Rs 1,500–5,000</td><td>Rs 1,500</td></tr>
            <tr><td>Salaried Tax Return</td><td>Rs 3,500–10,000</td><td>Rs 3,500</td></tr>
            <tr><td>Business Tax Return</td><td>Rs 7,000–25,000</td><td>Rs 7,000</td></tr>
            <tr><td>Wealth Statement</td><td>Rs 5,000–15,000</td><td>Rs 5,000</td></tr>
            <tr><td>Company Registration</td><td>Rs 8,000–30,000</td><td>Rs 8,000</td></tr>
            <tr><td>FBR Notice Response</td><td>Rs 5,000–20,000</td><td>Rs 5,000</td></tr>
          </tbody>
        </table>'''
    elif slug == 'tax-consultant-builders-developers-pakistan':
        page_title = 'Tax Consultant for Builders & Developers Pakistan 2026 | FBR | Kamboh Associates'
        h1 = 'Tax Consultant for Builders & Developers in Pakistan — FBR 2026'
        lead = 'Builders and property developers in Pakistan face complex FBR tax obligations including Section 7E, capital gains tax, advance tax under Section 236C/236K, and withholding tax compliance. Kamboh Associates provides specialized tax services for the real estate development sector across Pakistan.'
        badge = 'Builders & Developers Tax'
        badge_icon = 'fas fa-building'
        extra = '''<h2 id="taxes">Key Taxes for Builders & Developers</h2>
        <table class="dt">
          <thead><tr><th>Tax Type</th><th>Rate</th><th>Applicable On</th></tr></thead>
          <tbody>
            <tr><td>Section 236C (Seller WHT)</td><td>2.75% (filer) / 5.5% (non-filer)</td><td>Property sale proceeds</td></tr>
            <tr><td>Section 236K (Buyer WHT)</td><td>1.25% (filer) / 2.5% (non-filer)</td><td>Property purchase value</td></tr>
            <tr><td>Capital Gains Tax</td><td>15% (open plot) / varies</td><td>Gain on sale</td></tr>
            <tr><td>Section 7E (deemed income)</td><td>Abolished 2024-25</td><td>N/A — removed</td></tr>
          </tbody>
        </table>'''
    elif slug in ['tax-consultant-los-angeles-pakistanis', 'tax-consultant-new-jersey-pakistanis']:
        city_name = 'Los Angeles' if 'los-angeles' in slug else 'New Jersey'
        page_title = f'Tax Consultant for Overseas Pakistanis in {city_name} | FBR | Kamboh Associates'
        h1 = f'FBR Tax Services for Overseas Pakistanis in {city_name}'
        lead = f'Kamboh Associates provides complete FBR tax services for overseas Pakistanis living in {city_name}. Income tax return filing, NTN registration, wealth statement, Section 8 Tax Clearance Certificate — all handled remotely via WhatsApp. No Pakistan visit required.'
        badge = f'Overseas Pakistanis — {city_name}'
        badge_icon = 'fas fa-globe'
        extra = '''<h2 id="services">Services for Overseas Pakistanis</h2>
        <ul>
          <li><strong>Income Tax Return Filing</strong> — Annual FBR return even while abroad</li>
          <li><strong>NTN Registration</strong> — Get your Pakistan tax number remotely</li>
          <li><strong>Section 8 TCC</strong> — Tax Clearance Certificate for visa/NOC</li>
          <li><strong>Wealth Statement</strong> — Overseas assets declared properly</li>
          <li><strong>ATL Maintenance</strong> — Stay on Active Taxpayer List while abroad</li>
          <li><strong>Property Tax Filing</strong> — Manage Pakistan property tax obligations</li>
        </ul>'''
    else:
        city_name = slug_to_title(slug.replace('-city',''))
        page_title = f'Tax Consultant in {city_name} | FBR Services | Kamboh Associates'
        h1 = f'Expert Tax Consultant in {city_name} — FBR Services 2026'
        lead = f'Kamboh Associates provides complete FBR tax services to residents and businesses in {city_name}. Income tax return filing, NTN registration, wealth statement, FBR notice response — all handled remotely. WhatsApp 0328-4675162 for free consultation.'
        badge = f'{city_name} Tax Guide'
        badge_icon = 'fas fa-map-marker-alt'
        extra = '''<h2 id="services">Tax Services Available</h2>
        <ul>
          <li><strong>Income Tax Return Filing</strong> — From Rs 3,500, same-day filing</li>
          <li><strong>NTN Registration</strong> — 24–48 hours, Rs 1,500</li>
          <li><strong>Wealth Statement</strong> — Accurate FBR-defensible statements</li>
          <li><strong>FBR Notice Response</strong> — Professional, timely replies</li>
          <li><strong>Company Registration</strong> — SECP and District Administration</li>
          <li><strong>Sales Tax Registration</strong> — STRN and PRA registration</li>
        </ul>'''

    url = f'https://kambohassociates.com/blogs/{slug}'
    wa_msg = 'Hi%2C+I+need+tax+consultation'

    schema = f'''[
  {{"@context":"https://schema.org","@type":"Article","headline":"{h1}","datePublished":"2026-07-17","author":{{"@type":"Organization","name":"Kamboh Associates"}}}},
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://kambohassociates.com/"}},{{"@type":"ListItem","position":2,"name":"Blog","item":"https://kambohassociates.com/blogs"}},{{"@type":"ListItem","position":3,"name":"{h1}","item":"{url}"}}]}}
]'''

    content = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large"/>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{page_title}</title>
<meta name="description" content="{lead[:160]}"/>
<meta property="og:type" content="article"/>
<meta property="og:title" content="{h1}"/>
<meta property="og:url" content="{url}"/>
<link rel="canonical" href="{url}"/>
{HEAD_COMMON}
<script type="application/ld+json">{schema}</script>
{CSS}
</head>
<body>
{NAV}
<section class="hero">
  <div class="container">
    <div class="breadcrumb"><a href="/"><i class="fas fa-home"></i> Home</a><i class="fas fa-chevron-right"></i><a href="/blogs">Blog</a><i class="fas fa-chevron-right"></i><span>{h1}</span></div>
    <div class="badge"><i class="{badge_icon}"></i> {badge}</div>
    <h1>{h1}</h1>
    <div class="hero-meta">
      <div class="meta-item"><i class="far fa-calendar-alt"></i> July 2026</div>
      <div class="meta-item"><i class="fas fa-user-tie"></i> Kamboh Associates</div>
      <div class="meta-item"><i class="far fa-clock"></i> 5 min read</div>
    </div>
  </div>
</section>
<div class="container">
  <div class="layout">
    <article>
      <div class="article reveal">
        <p class="lead">{lead}</p>
        {extra}
        <div class="cta-box">
          <h3>Get Expert Tax Help Today</h3>
          <p>Kamboh Associates serves clients across Pakistan remotely. WhatsApp your documents and we handle everything — free first consultation.</p>
          <div class="cta-btns">
            <a href="https://wa.me/923284675162?text={wa_msg}" class="btn-w" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> Free Consultation</a>
            <a href="tel:03284675162" class="btn-g"><i class="fas fa-phone"></i> 0328-4675162</a>
          </div>
        </div>
        <h2 id="faqs">Frequently Asked Questions</h2>
        <div class="fq">
          <div class="fi"><div class="fq-q">How do I get started with Kamboh Associates? <i class="fas fa-plus"></i></div><div class="fq-a">Simply WhatsApp your CNIC copy to 0328-4675162. We assess your situation, advise on requirements, and begin your NTN registration or tax filing immediately. First consultation is free.</div></div>
          <div class="fi"><div class="fq-q">Do I need to visit your office? <i class="fas fa-plus"></i></div><div class="fq-a">No. Kamboh Associates provides fully remote services across Pakistan and overseas. All communication, document sharing, and tax filing is done online and via WhatsApp.</div></div>
          <div class="fi"><div class="fq-q">What is the income tax return deadline? <i class="fas fa-plus"></i></div><div class="fq-a">The annual income tax return deadline is September 30. Late filing attracts a penalty of 5% of tax payable per month. File by August 31 to avoid last-minute issues.</div></div>
        </div>
      </div>
    </article>
    <aside class="sidebar">
      <div class="sc cc reveal"><h3>Free Tax Consultation</h3><p>Expert FBR services from Kamboh Associates. WhatsApp now for immediate assistance.</p><a href="https://wa.me/923284675162" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> WhatsApp Now</a></div>
      <div class="sc reveal" style="transition-delay:.1s"><div class="st"><i class="fas fa-phone"></i> Contact</div><a href="tel:03284675162" style="display:flex;align-items:center;justify-content:center;gap:8px;background:#0F172A;color:#fff;padding:12px 16px;border-radius:8px;font-weight:600;font-size:.88rem;text-decoration:none;margin-bottom:8px"><i class="fas fa-phone"></i> 0328-4675162</a><a href="https://wa.me/923284675162" target="_blank" rel="noopener noreferrer" style="display:flex;align-items:center;justify-content:center;gap:8px;background:#25D366;color:#fff;padding:12px 16px;border-radius:8px;font-weight:600;font-size:.88rem;text-decoration:none"><i class="fab fa-whatsapp"></i> WhatsApp</a></div>
    </aside>
  </div>
</div>
{FOOTER}
{WA_BTN}
{JS}
</body>
</html>'''
    return content


def generate_all():
    created = 0
    skipped = 0

    with open('/tmp/gsc_404/tc_slugs.txt') as f:
        for line in f:
            slug = line.strip()
            if not slug:
                continue
            path = os.path.join(BLOGS_DIR, f'{slug}.html')
            if os.path.exists(path):
                skipped += 1
                continue
            with open(path, 'w', encoding='utf-8') as out:
                out.write(make_tc_page(slug))
            created += 1

    with open('/tmp/gsc_404/ntn_slugs.txt') as f:
        for line in f:
            slug = line.strip()
            if not slug:
                continue
            path = os.path.join(BLOGS_DIR, f'{slug}.html')
            if os.path.exists(path):
                skipped += 1
                continue
            with open(path, 'w', encoding='utf-8') as out:
                out.write(make_ntn_page(slug))
            created += 1

    with open('/tmp/gsc_404/itf_slugs.txt') as f:
        for line in f:
            slug = line.strip()
            if not slug:
                continue
            path = os.path.join(BLOGS_DIR, f'{slug}.html')
            if os.path.exists(path):
                skipped += 1
                continue
            with open(path, 'w', encoding='utf-8') as out:
                out.write(make_itf_page(slug))
            created += 1

    with open('/tmp/gsc_404/misc_slugs.txt') as f:
        for line in f:
            slug = line.strip()
            if not slug:
                continue
            path = os.path.join(BLOGS_DIR, f'{slug}.html')
            if os.path.exists(path):
                skipped += 1
                continue
            with open(path, 'w', encoding='utf-8') as out:
                out.write(make_misc_page(slug))
            created += 1

    print(f'Created: {created}, Skipped (already exist): {skipped}')


if __name__ == '__main__':
    generate_all()
