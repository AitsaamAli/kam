"""Builds the 2026 calculator pages from tools/late-filing-penalty-calculator.html (head, nav, footer reused).
Facts checked 19 November 2026 against the Income Tax Ordinance 2001 amended up to 30.06.2026 (FBR PDF)."""
import html, json, os, re, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from calcs import CALCS

ROOT = "/home/user/kam"
BASE = "https://kambohassociates.com"
ITO = "https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf"
TPL = open(f"{ROOT}/tools/late-filing-penalty-calculator.html", encoding="utf-8").read()
E = html.escape
L = 'style="color:#0D9488;font-weight:600"'
WA = "https://wa.me/923284675162"

PRELUDE = r"""function rs(n){return 'Rs. '+Math.round(n).toLocaleString('en-PK');}
function $(id){return document.getElementById(id);}
function num(id){var v=$(id).value;return v===''?NaN:parseFloat(v);}
function pad(n){return (n<10?'0':'')+n;}
function iso(d){return d.getUTCFullYear()+'-'+pad(d.getUTCMonth()+1)+'-'+pad(d.getUTCDate());}
function nice(d){return d.toLocaleDateString('en-GB',{day:'numeric',month:'long',year:'numeric',timeZone:'UTC'});}
function parseD(s){return new Date(Date.UTC(+s.slice(0,4),+s.slice(5,7)-1,+s.slice(8,10)));}
function addM(d,m){var y=d.getUTCFullYear(),mo=d.getUTCMonth()+m,dd=d.getUTCDate();y+=Math.floor(mo/12);mo=((mo%12)+12)%12;var last=new Date(Date.UTC(y,mo+1,0)).getUTCDate();return new Date(Date.UTC(y,mo,Math.min(dd,last)));}
function addD(d,n){return new Date(d.getTime()+n*86400000);}
function today(){var t=new Date();return new Date(Date.UTC(t.getFullYear(),t.getMonth(),t.getDate()));}
function show(id){$(id).classList.add('show');}
"""


def field(f):
    k = f[0]
    if k == "num":
        _, i, lab, ph, hlp = (list(f) + [""])[:5]
        h = f'<p style="font-size:.8rem;color:var(--text-3);margin-top:6px">{hlp}</p>' if hlp else ""
        return f'<div class="calc-section"><label class="calc-label" for="{i}">{lab}</label><input type="number" class="calc-input" id="{i}" placeholder="{E(ph)}" min="0" step="any" inputmode="decimal"/>{h}</div>'
    if k == "date":
        _, i, lab, val = f
        return f'<div class="calc-section"><label class="calc-label" for="{i}">{lab}</label><input type="date" class="calc-input" id="{i}" value="{val}"/></div>'
    if k == "sel":
        _, i, lab, opts = f
        o = "".join(f'<option value="{v}">{E(t)}</option>' for v, t in opts)
        return f'<div class="calc-section" id="{i}Row"><label class="calc-label" for="{i}">{lab}</label><select class="calc-input" id="{i}">{o}</select></div>'
    raise ValueError(k)


def card(c):
    i, lab, col = (list(c) + [""])[:3]
    st = f' style="border-top:3px solid {col}"' if col else ""
    vs = f' style="color:{col}"' if col else ""
    return f'<div class="result-card"{st}><div class="result-label">{lab}</div><div class="result-value"{vs} id="{i}">-</div><div class="result-note" id="{i}N"></div></div>'


def short(x):
    return f'<p class="direct-answer" style="margin:0 0 12px;padding:10px 14px;background:#F0FDFA;border-left:3px solid #0D9488;border-radius:0 8px 8px 0;color:#0F172A"><strong>Short answer:</strong> {x}</p>'


def page(c):
    url = f"{BASE}/tools/{c['slug']}"
    t = TPL
    title = c["title"] + " | Kamboh Associates"
    t = re.sub(r"<title>.*?</title>", f"<title>{E(title)}</title>", t, 1)
    t = re.sub(r'<meta name="description" content="[^"]*"/>', f'<meta name="description" content="{E(c["desc"])}"/>', t, 1)
    t = re.sub(r'<link rel="canonical" href="[^"]*"/>', f'<link rel="canonical" href="{url}"/>', t, 1)
    for prop, val in (("og:title", title), ("og:description", c["desc"]), ("og:url", url)):
        t = re.sub(rf'<meta property="{prop}" content="[^"]*"/>', f'<meta property="{prop}" content="{E(val)}"/>', t, 1)
    t = re.sub(r'<meta name="twitter:title" content="[^"]*"/>', f'<meta name="twitter:title" content="{E(title)}"/>', t, 1)
    t = re.sub(r'<meta name="twitter:description" content="[^"]*"/>', f'<meta name="twitter:description" content="{E(c["desc"])}"/>', t, 1)
    app = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": c["h1"], "applicationCategory": "FinanceApplication",
           "operatingSystem": "Web", "description": c["desc"], "url": url, "dateModified": "2026-11-19", "inLanguage": "en-PK",
           "offers": {"@type": "Offer", "price": "0", "priceCurrency": "PKR"},
           "creator": {"@id": f"{BASE}/#organization", "@type": "Organization", "name": "Kamboh Associates", "url": BASE},
           "citation": [u for _, u in c["sources"]]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in c["faqs"]]}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"}, {"@type": "ListItem", "position": 2, "name": "Calculators", "item": f"{BASE}/tools"},
        {"@type": "ListItem", "position": 3, "name": c["crumb"], "item": url}]}
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in (app, faq, bc))
    t = re.sub(r'(<script type="application/ld\+json">.*?</script>\s*){3}', lambda m: lds, t, 1, flags=re.S)
    # hero + body
    s = t.index('<section class="blog-post-hero">'); e = t.index('<section class="cta-strip">')
    rules = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{d}</td></tr>" for a, b, d in c["rules"])
    how = "".join(f'<h2 style="margin:24px 0 6px">{h}</h2>{short(sa)}{body}' for h, sa, body in c["sections"])
    faqh = "".join(f'<div class="faq-item"><h3 style="font-size:1rem;margin:14px 0 6px">{q}</h3><p>{a}</p></div>' for q, a in c["faqs"])
    rel = " &middot; ".join(f'<a href="{h}" {L}>{E(x)}</a>' for h, x in c["related"])
    srcs = "; ".join(f'<a href="{u}" target="_blank" rel="noopener">{E(n)}</a>' for n, u in c["sources"])
    body = f'''<section class="blog-post-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a><i class="fas fa-chevron-right"></i><a href="/tools">Calculators</a><i class="fas fa-chevron-right"></i><span>{E(c["crumb"])}</span></div>
    <h1>{E(c["h1"])}</h1>
    <div class="blog-hero-meta">
      <span class="blog-meta-tag"><i class="fas fa-calculator"></i> {E(c["tag"])}</span>
      <span class="blog-meta-item"><i class="fas fa-check-circle" style="color:#10B981"></i> Rules checked 19 November 2026</span>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="quick-answer" style="border-left:4px solid #0D9488;background:#F0FDFA;border-radius:10px;padding:16px 20px;margin:0 0 20px"><p style="margin:0 0 6px;font-weight:700;color:#0F172A">Quick answer</p><p style="margin:0;color:#334155">{c["quick"]}</p></div>
    <div class="warn-box"><i class="fas fa-info-circle"></i><p>{c["warn"]} Rules from the <a href="{ITO}" target="_blank" rel="noopener" {L}>Income Tax Ordinance, 2001 (FBR, amended up to 30.06.2026)</a>. This is an estimate, not advice for your case.</p></div>
    <div class="calc-wrap">
      <h2 style="font-family:var(--font-serif);font-size:1.5rem;margin-bottom:6px;color:var(--text)">{c["calc_h"]}</h2>
      <p style="font-size:.87rem;color:var(--text-3);margin-bottom:28px">{c["calc_p"]}</p>
      {"".join(field(f) for f in c["fields"])}
      <p id="cErr" style="color:#B91C1C;font-size:.88rem;margin:-6px 0 14px" role="alert"></p>
      <button class="calc-btn" id="cBtn" type="button"><i class="fas fa-calculator"></i> &nbsp;Calculate</button>
      <div class="calc-result" id="cRes" aria-live="polite">
        <h3 style="font-family:var(--font-serif);font-size:1.3rem;color:var(--text);margin-bottom:18px">{c["res_h"]}</h3>
        <div class="result-grid">{"".join(card(x) for x in c["cards"])}</div>
        <p id="cExp" style="font-size:.88rem;color:var(--text-2);margin-top:16px"></p>
        <div class="verify-note"><i class="fas fa-exclamation-triangle"></i> {c["verify"]}</div>
      </div>
    </div>
    <div style="margin-top:48px">
      <h2 style="font-family:var(--font-serif);font-size:1.6rem;color:var(--text);margin-bottom:6px">Rules the Calculator Uses</h2>
      {short(c["rules_short"])}
      <table class="data-table"><thead><tr><th>Item</th><th>Rule</th><th>Source</th></tr></thead><tbody>{rules}</tbody></table>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0"><div class="container" style="max-width:820px">
{how}
<h2 style="margin:24px 0 12px">Frequently Asked Questions</h2>
{faqh}
<p style="margin-top:20px"><strong>Related:</strong> {rel}</p>
<p style="font-size:.85rem;color:var(--text-3);margin-top:12px">Sources: {srcs}. Checked 19 November 2026.</p>
</div></section>
'''
    t = t[:s] + body + t[e:]
    # CTA strip
    cs = t.index('<section class="cta-strip">'); ce = t.index('</section>', cs) + len('</section>')
    wa = f"{WA}?text={urllib.parse.quote(c['cta'][2])}"
    t = t[:cs] + f'''<section class="cta-strip">
  <div class="container">
    <h2>{E(c["cta"][0])}</h2>
    <p>{E(c["cta"][1])}</p>
    <div class="btns">
      <a href="{E(wa)}" class="btn-primary" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> {E(c["cta"][3])}</a>
      <a href="/pricing" class="btn-ghost">See Published Fees</a>
    </div>
  </div>
</section>''' + t[ce:]
    # calculator script
    js0 = t.index('<script>\n(function(){'); js1 = t.index('})();\n</script>', js0) + len('})();\n</script>')
    t = t[:js0] + "<script>\n(function(){\n" + PRELUDE + c["js"] + "\n})();\n</script>" + t[js1:]
    return t


def main():
    sm = open(f"{ROOT}/sitemap.xml", encoding="utf-8").read()
    for c in CALCS:
        out = page(c)
        open(f"{ROOT}/tools/{c['slug']}.html", "w", encoding="utf-8").write(out)
        print(c["slug"], len(c["title"]), len(c["desc"]))
        loc = f"{BASE}/tools/{c['slug']}"
        if f"<loc>{loc}</loc>" not in sm:
            sm = sm.replace("</urlset>", f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>2026-11-19</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n</urlset>", 1)
    open(f"{ROOT}/sitemap.xml", "w", encoding="utf-8").write(sm)


if __name__ == "__main__":
    main()
