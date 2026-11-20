"""Blog listing hero redesign (owner request 20 Nov 2026). Replaces <section class="blog-hero">…</section> in blogs.html.
Keeps the H1 text, the #heroSearch input (used by setHeroSearch/searchPosts), every internal link and the WhatsApp/call/calculator actions.
Usage: python3 blog_hero.py [out_file]   (default writes blogs.html in place)"""
import re, sys

ROOT = '/home/user/kam/'
CSS = """<style id="kh-css">
.kh{--kh-navy:#0B1222;--kh-ink:#0F172A;--kh-teal:#14B8A6;--kh-teal-d:#0D9488;--kh-gold:#D4AF37;background:var(--kh-navy);color:#E2E8F0;text-align:left;padding:72px 0 0;position:relative;overflow:hidden}
.kh::before{content:"";position:absolute;inset:0;background:radial-gradient(60% 70% at 85% 10%,rgba(20,184,166,.20),transparent 60%),radial-gradient(45% 60% at 0% 100%,rgba(212,175,55,.10),transparent 60%);pointer-events:none}
.kh::after{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:44px 44px;-webkit-mask-image:linear-gradient(180deg,#000,transparent 85%);mask-image:linear-gradient(180deg,#000,transparent 85%);pointer-events:none}
.kh .container{position:relative;z-index:2}
.kh-main,.kh-card{min-width:0}
.kh-grid{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:48px;align-items:center}
.kh-eyebrow{display:inline-flex;align-items:center;gap:10px;font-family:var(--font-display,'Cinzel',serif);font-size:.66rem;letter-spacing:.24em;text-transform:uppercase;color:var(--kh-gold);margin-bottom:18px}
.kh-eyebrow::before{content:"";width:28px;height:1px;background:var(--kh-gold)}
.kh h1{font-family:var(--font-serif,'Cormorant Garamond',Georgia,serif);font-size:clamp(2.3rem,5vw,3.6rem);font-weight:700;line-height:1.04;color:#fff;margin:0 0 16px;letter-spacing:-.01em;text-wrap:balance}
.kh h1 span{font-style:italic;background:linear-gradient(120deg,#5EEAD4,#14B8A6);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.kh .kh-sub{font-size:1.04rem;line-height:1.7;color:#CBD5E1;max-width:560px;margin:0 0 28px}
.kh-search{display:flex;align-items:center;gap:8px;background:#fff;border-radius:16px;padding:7px 7px 7px 18px;max-width:620px;box-shadow:0 18px 50px rgba(0,0,0,.35);border:1px solid rgba(255,255,255,.6)}
.kh-search:focus-within{outline:3px solid rgba(20,184,166,.55);outline-offset:2px}
.kh-search>i{color:#64748B;font-size:1rem}
.kh-search input{flex:1;min-width:0;border:0;outline:0;background:transparent;font:inherit;font-size:.98rem;color:var(--kh-ink);padding:12px 4px}
.kh-search input::placeholder{color:#94A3B8}
.kh-search button{border:0;cursor:pointer;background:var(--kh-teal-d);color:#fff;font:inherit;font-weight:600;font-size:.9rem;padding:12px 20px;border-radius:11px;display:inline-flex;align-items:center;gap:8px;transition:background .2s}
.kh-search button:hover,.kh-search button:focus-visible{background:var(--kh-ink)}
.kh-topics{display:flex;align-items:center;gap:10px;margin-top:16px;max-width:660px}
.kh-label{font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;color:#94A3B8;font-weight:600;flex-shrink:0}
.kh-chips{display:flex;gap:8px;flex-wrap:wrap}
.kh-chips button{border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.06);color:#E2E8F0;font:inherit;font-size:.8rem;padding:7px 14px;border-radius:999px;cursor:pointer;white-space:nowrap;transition:all .2s}
.kh-chips button:hover,.kh-chips button:focus-visible{background:rgba(20,184,166,.18);border-color:var(--kh-teal);color:#fff}
.kh-card{background:#fff;color:var(--kh-ink);border-radius:20px;padding:26px 24px;box-shadow:0 24px 60px rgba(0,0,0,.35);position:relative}
.kh-card::before{content:"";position:absolute;left:24px;right:24px;top:0;height:3px;border-radius:0 0 3px 3px;background:linear-gradient(90deg,var(--kh-gold),var(--kh-teal))}
.kh-card-eyebrow{font-family:var(--font-display,'Cinzel',serif);font-size:.62rem;letter-spacing:.2em;text-transform:uppercase;color:var(--kh-teal-d);margin-bottom:8px}
.kh .kh-card .kh-card-title{font-family:var(--font-serif,'Cormorant Garamond',Georgia,serif);font-size:1.6rem;font-weight:700;line-height:1.1;margin:0 0 8px;color:var(--kh-ink)}
.kh .kh-card p{font-size:.86rem;color:#475569;line-height:1.6;margin:0 0 16px;max-width:none}
.kh-fees{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:0 0 16px}
.kh-fees div{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:9px 10px}
.kh-fees b{display:block;font-family:var(--font-serif,'Cormorant Garamond',Georgia,serif);font-size:1.2rem;color:var(--kh-teal-d);line-height:1.1}
.kh-fees span{font-size:.7rem;color:#64748B}
.kh-btns{display:grid;gap:8px}
.kh-btn{display:flex;align-items:center;justify-content:center;gap:8px;min-height:46px;border-radius:11px;font-weight:600;font-size:.9rem;text-decoration:none;transition:transform .15s,box-shadow .15s}
.kh-btn:hover{transform:translateY(-1px)}
.kh-btn.wa{background:#25D366;color:#fff;box-shadow:0 8px 20px rgba(37,211,102,.28)}
.kh-btn.call{background:var(--kh-ink);color:#fff}
.kh-btn:focus-visible{outline:3px solid var(--kh-teal);outline-offset:2px}
.kh-calc{display:block;text-align:center;margin-top:12px;font-size:.82rem;color:var(--kh-teal-d);font-weight:600;text-decoration:none}
.kh-trust{display:flex;flex-wrap:wrap;gap:6px 14px;margin-top:14px;padding-top:14px;border-top:1px solid #E2E8F0;font-size:.74rem;color:#475569}
.kh-trust span{display:inline-flex;align-items:center;gap:6px}
.kh-trust i{color:var(--kh-teal-d)}
.kh-start{margin-top:56px;border-top:1px solid rgba(255,255,255,.08);background:rgba(255,255,255,.025)}
.kh-start .container{display:flex;align-items:center;gap:18px;padding-top:18px;padding-bottom:18px}
.kh-start .kh-label{color:var(--kh-gold)}
.kh-guides{display:flex;gap:10px;flex-wrap:wrap}
.kh-guides a{display:inline-flex;align-items:center;gap:8px;color:#E2E8F0;text-decoration:none;font-size:.84rem;font-weight:500;padding:8px 14px;border-radius:10px;border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.04);white-space:nowrap;transition:all .2s}
.kh-guides a i{color:var(--kh-teal);font-size:.8rem}
.kh-guides a:hover,.kh-guides a:focus-visible{border-color:var(--kh-gold);color:#fff;background:rgba(212,175,55,.08)}
.kh .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media(max-width:960px){.kh-grid{grid-template-columns:minmax(0,1fr);gap:28px}.kh-card{max-width:620px}}
@media(max-width:640px){
 .kh{padding-top:40px}
 .kh h1{font-size:2.35rem}
 .kh-upd{display:none}
 .kh .kh-sub{font-size:.95rem;margin-bottom:20px}
 .kh-search{padding:5px 5px 5px 14px;border-radius:14px}
 .kh-search input{font-size:.92rem;padding:11px 2px}
 .kh-search button{padding:11px 14px}
 .kh-search button span{display:none}
 .kh-topics{flex-direction:column;align-items:flex-start;gap:8px}
 .kh-chips,.kh-guides{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;margin:0 -16px;padding:2px 16px;width:calc(100% + 32px);-webkit-mask-image:linear-gradient(90deg,#000 88%,transparent);mask-image:linear-gradient(90deg,#000 88%,transparent)}
 .kh-chips::-webkit-scrollbar,.kh-guides::-webkit-scrollbar{display:none}
 .kh-card{padding:22px 18px;border-radius:18px}
 .kh-btns{grid-template-columns:1fr 1fr}
 .kh-start{margin-top:36px}
 .kh-start .container{flex-direction:column;align-items:flex-start;gap:10px}
}
@media(prefers-reduced-motion:reduce){.kh *{transition:none!important}}
</style>
"""

CHIPS = [("income tax return", "Income tax return"), ("NTN registration", "NTN registration"), ("DNFBP", "DNFBP &amp; AML"),
         ("sole proprietor", "Sole proprietors"), ("freelancer", "Freelancers"), ("FBR notice", "FBR notices"),
         ("property tax", "Property tax"), ("company registration", "Company registration")]
GUIDES = [("/income-tax-return-pakistan", "fa-file-invoice", "Tax Return"), ("/ntn-registration", "fa-id-card", "NTN Registration"),
          ("/filer-vs-nonfiler-pakistan", "fa-scale-balanced", "Filer vs Non-Filer"), ("/secp-company-registration-guide-2026", "fa-building", "SECP Registration"),
          ("/wealth-statement-mistakes-pakistan", "fa-wallet", "Wealth Statement"), ("/tax-benefits-filer-pakistan", "fa-star", "Filer Benefits")]

chips = "".join(f'<button type="button" onclick="setHeroSearch(\'{q}\')">{t}</button>' for q, t in CHIPS)
guides = "".join(f'<a href="{h}"><i class="fas {i}" aria-hidden="true"></i>{t}</a>' for h, i, t in GUIDES)
HERO = f"""<section class="blog-hero kh">
  <div class="container">
    <div class="kh-grid">
      <div class="kh-main">
        <span class="kh-eyebrow">Knowledge Hub<span class="kh-upd">&nbsp;&middot; Updated November 2026</span></span>
        <h1>Tax &amp; Regulatory <span>Insights</span></h1>
        <p class="kh-sub">Clear guides to Pakistan's income tax, FBR compliance, DNFBP rules and business registration, checked against FBR's own texts.</p>
        <form class="kh-search" role="search" onsubmit="setHeroSearch(document.getElementById('heroSearch').value);return false">
          <label for="heroSearch" class="sr">Search our guides</label>
          <i class="fas fa-magnifying-glass" aria-hidden="true"></i>
          <input type="search" id="heroSearch" autocomplete="off" placeholder="Search 1,500+ guides: NTN, filer status, FBR notice&hellip;"
            oninput="document.getElementById('searchInput').value=this.value;searchPosts(this.value)">
          <button type="submit" aria-label="Search"><i class="fas fa-arrow-right" aria-hidden="true"></i><span>Search</span></button>
        </form>
        <div class="kh-topics"><span class="kh-label">Popular</span><div class="kh-chips">{chips}</div></div>
      </div>
      <aside class="kh-card" aria-label="Have it done for you">
        <div class="kh-card-eyebrow">Done for you</div>
        <p class="kh-card-title">Prefer we handle it?</p>
        <p>We file, register and reply to FBR for you, with the fee confirmed before work starts.</p>
        <div class="kh-fees"><div><b>Rs 3,500</b><span>Salaried return</span></div><div><b>Rs 2,000</b><span>NTN registration</span></div></div>
        <div class="kh-btns">
          <a class="kh-btn wa" href="https://wa.me/923284675162?text=Hi%2C%20tax%20filing%20mein%20help%20chahiye" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp" aria-hidden="true"></i> WhatsApp</a>
          <a class="kh-btn call" href="tel:+923284675162"><i class="fas fa-phone" aria-hidden="true"></i> 0328-4675162</a>
        </div>
        <a class="kh-calc" href="/tax-calculator"><i class="fas fa-calculator" aria-hidden="true"></i> Try the tax calculator</a>
        <div class="kh-trust"><span><i class="fas fa-circle-check" aria-hidden="true"></i>FBR Registered</span><span><i class="fas fa-circle-check" aria-hidden="true"></i>Since 2008</span><span><i class="fas fa-location-dot" aria-hidden="true"></i>Awan Town, Lahore</span></div>
      </aside>
    </div>
  </div>
  <div class="kh-start"><div class="container"><span class="kh-label">Start here</span><div class="kh-guides">{guides}</div></div></div>
</section>"""


def main(out):
    t = open(ROOT + 'blogs.html', encoding='utf-8').read()
    s = t.index('<section class="blog-hero')
    e = t.index('</section>', s) + len('</section>')
    t = t[:s] + HERO + t[e:]
    if 'id="kh-css"' not in t:
        t = t.replace('</head>', CSS + '</head>', 1)
    open(out, 'w', encoding='utf-8').write(t)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else ROOT + 'blogs.html')
