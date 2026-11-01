import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from posts import POSTS, WA

ROOT = "/home/user/kam"
BASE = "https://kambohassociates.com"
TPL = open(f"{ROOT}/blogs/fbr-extends-tax-return-deadline-october-15-2026.html", encoding="utf-8").read()
DATE = "2026-11-01"
E = html.escape


def plain(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def page(p):
    url = f"{BASE}/blogs/{p['slug']}"
    t = TPL
    t = re.sub(r"<title>.*?</title>", f"<title>{E(p['title'])}</title>", t, 1)
    t = re.sub(r'<meta name="description" content="[^"]*"/>', f'<meta name="description" content="{E(p["description"])}"/>', t, 1)
    t = re.sub(r'<meta name="keywords" content="[^"]*"/>', f'<meta name="keywords" content="{E(p["keywords"])}"/>', t, 1)
    t = re.sub(r'<link rel="canonical" href="[^"]*"/>', f'<link rel="canonical" href="{url}"/>', t, 1)
    t = re.sub(r'<meta property="og:title" content="[^"]*"/>', f'<meta property="og:title" content="{E(p["title"])}"/>', t, 1)
    t = re.sub(r'<meta property="og:description" content="[^"]*"/>', f'<meta property="og:description" content="{E(p["description"])}"/>', t, 1)
    t = re.sub(r'<meta property="og:url" content="[^"]*"/>', f'<meta property="og:url" content="{url}"/>', t, 1)
    bp = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["h1"], "description": p["description"],
          "datePublished": DATE, "dateModified": DATE, "inLanguage": "en-PK",
          "author": {"@type": "Person", "name": "Aitsaam Ali", "url": f"{BASE}/authors/aitsaam-ali", "@id": f"{BASE}/authors/aitsaam-ali#person"},
          "publisher": {"@type": "Organization", "@id": f"{BASE}/#organization", "name": "Kamboh Associates", "url": BASE,
                        "logo": {"@type": "ImageObject", "url": f"{BASE}/android-chrome-512x512.png", "width": 512, "height": 512}},
          "mainEntityOfPage": {"@type": "WebPage", "@id": url},
          "image": {"@type": "ImageObject", "url": f"{BASE}/images/og-default.jpg", "width": 1200, "height": 630},
          "keywords": p["keywords"], "citation": [u for _, u in p["sources"]]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a_}} for q, a_ in p["faqs"]]}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
        {"@type": "ListItem", "position": 2, "name": "Tax Blog Pakistan", "item": f"{BASE}/blogs"},
        {"@type": "ListItem", "position": 3, "name": p["crumb"], "item": url}]}
    t = re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "BlogPosting".*?</script>', lambda m: ld(bp), t, 1, flags=re.S)
    t = re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "FAQPage".*?</script>', lambda m: ld(faq), t, 1, flags=re.S)
    t = re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "BreadcrumbList".*?</script>', lambda m: ld(bc), t, 1, flags=re.S)
    t = t.replace('<meta property="og:locale" content="en_PK"/><meta property="og:type" content="article"/>',
                  f'<meta property="og:locale" content="en_PK"/><meta property="og:type" content="article"/><meta property="article:published_time" content="{DATE}"/><meta property="article:modified_time" content="{DATE}"/>', 1)

    toc = "".join(f'<li><a href="#{i}" style="color:#0D9488">{plain(h)}</a></li>' for i, h in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', p["body"]))
    faqs = "".join(f'<div class="faq-item"><div class="faq-q">{E(q)} <i class="fas fa-chevron-down"></i></div><div class="faq-a">{E(a_)}</div></div>' for q, a_ in p["faqs"])
    srcs = "".join(f'<li><a href="{u}" target="_blank" rel="noopener" style="color:#0D9488">{E(n)}</a></li>' for n, u in p["sources"])
    rel = " &nbsp;|&nbsp; ".join(f'<a href="{h}">{E(n)} &rarr;</a>' for h, n in p["related"])
    words = len(plain(p["body"] + " ".join(q + " " + a_ for q, a_ in p["faqs"])).split())
    hero = f'''<section class="blog-hero"><div class="container"><nav class="breadcrumb"><a href="/"><i class="fas fa-home"></i> Home</a><i class="fas fa-chevron-right"></i><a href="/blogs">Blog</a><i class="fas fa-chevron-right"></i><span>{E(p["crumb"])}</span></nav><div class="blog-cat"><i class="fas fa-tags"></i> {E(p["category"])}</div>
<h1>{E(p["h1"])}</h1>
<div class="blog-meta"><span><i class="fas fa-calendar"></i> <time datetime="{DATE}">1 November 2026</time></span><span><i class="fas fa-user"></i> Kamboh Associates</span><span><i class="fas fa-clock"></i> {p["read"]}</span></div></div></section>
<div class="blog-layout container"><article class="article-body" style="min-width:0">
<div class="author-byline" style="display:flex;align-items:center;gap:10px;margin:0 0 18px;padding:12px 16px;background:rgba(20,184,166,.07);border-left:3px solid #14B8A6;border-radius:0 8px 8px 0;font-size:.85rem;color:#334155"><i class="fas fa-user-tie" style="color:#14B8A6"></i><span>By <a href="/authors/aitsaam-ali" style="color:#0D9488;font-weight:600">Aitsaam Ali</a>, <strong>Tax Consultant | NTN &amp; Compliance Specialist</strong> &middot; Facts checked 1 November 2026</span></div>
<div class="urgency-banner"><i class="fas fa-triangle-exclamation"></i><span>{E(p["banner"])}</span></div>
<p class="article-lead">{E(p["lead"])}</p>
<div class="tldr-box" style="background:linear-gradient(135deg,rgba(20,184,166,.08),rgba(20,184,166,.04));border:1.5px solid rgba(20,184,166,.35);border-radius:12px;padding:16px 20px;margin:0 0 24px;display:flex;gap:12px;align-items:flex-start"><div style="background:#14B8A6;color:#fff;border-radius:6px;padding:3px 9px;font-size:.68rem;font-weight:700;letter-spacing:.08em;flex-shrink:0;margin-top:2px">TL;DR</div><p style="margin:0;font-size:.93rem;color:#1E293B;line-height:1.7">{E(p["tldr"])}</p></div>
<nav class="toc-box" aria-label="Contents" style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:14px 18px;margin:0 0 24px"><strong style="font-size:.9rem">In this guide</strong><ol style="margin:8px 0 0 20px">{toc}</ol></nav>
{p["body"].strip()}

<h2 id="frequently-asked-questions">Frequently Asked Questions</h2>
<div class="faq-list">
{faqs}
</div>
<h2 id="sources">Sources</h2>
<ol>{srcs}</ol>
<p style="font-size:.85rem;color:#475569">This guide explains the law and FBR announcements as reported up to 1 November 2026. It is general information, not advice for your specific case. Rules and IRIS options can change, so confirm before you act.</p>
<div class="related-guide" style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:14px 18px;margin:20px 0"><strong>Related Guides:</strong> {rel}</div>
<div class="article-cta" style="background:linear-gradient(135deg,#0F172A,#1E3A5F);border-radius:16px;padding:28px 32px;margin-top:32px;text-align:center"><h3 style="font-family:'Cormorant Garamond',serif;color:#fff;font-size:1.4rem;margin-bottom:8px">{E(p["cta_h"])}</h3><p style="color:#94A3B8;font-size:.9rem;margin-bottom:18px">{E(p["cta_p"])}</p><a href="{WA}?text={E(__import__("urllib.parse").parse.quote(p["wa_text"]))}" style="display:inline-flex;align-items:center;gap:8px;background:#25D366;color:#fff;padding:12px 28px;border-radius:100px;font-weight:600;font-size:.92rem"><i class="fab fa-whatsapp"></i> WhatsApp 0328-4675162</a></div>
</article>
'''
    aside = '''<aside><div class="consult-card"><h4>Free Consultation</h4><p>Expert reply on WhatsApp</p><a href="https://wa.me/923284675162" class="wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp Now</a></div><div class="sidebar-card"><h4>Services</h4><ul class="service-list"><li><i class="fas fa-file-invoice-dollar"></i><a href="/income-tax-filing" style="color:#0D9488"> Income Tax Return</a></li><li><i class="fas fa-id-card"></i><a href="/ntn-registration" style="color:#0D9488"> NTN Registration</a></li><li><i class="fas fa-percent"></i><a href="/sales-tax-registration" style="color:#0D9488"> Sales Tax</a></li><li><i class="fas fa-shield-halved"></i><a href="/fbr-notice-defense" style="color:#0D9488"> FBR Notice</a></li></ul></div><div class="sidebar-card"><div class="price-badge"><div class="from">Individual Return From</div><div class="amount">Rs. 3,500</div><div class="from">Salaried, per tax year</div></div><a href="/pricing" style="display:block;text-align:center;color:#14B8A6;font-size:.85rem;font-weight:600;margin-top:8px"><i class="fas fa-tags"></i> View All Pricing</a></div></aside>'''
    s = t.index('<section class="blog-hero">')
    e = t.index("</aside>") + len("</aside>")
    t = t[:s] + hero + aside + t[e:]
    return t, words


def main():
    os.chdir(ROOT)
    bl = open("blogs.html", encoding="utf-8").read()
    sm = open("sitemap.xml", encoding="utf-8").read()
    for p in POSTS:
        out, words = page(p)
        open(f"blogs/{p['slug']}.html", "w", encoding="utf-8").write(out)
        print(p["slug"], "words:", words, "title len", len(p["title"]), "desc len", len(p["description"]))
        link = f"/blogs/{p['slug']}"
        if f'id: "{p["slug"]}"' not in bl:
            entry = ('\n  {\n' f'    id: "{p["slug"]}",\n' f'    title: {json.dumps(p["h1"], ensure_ascii=False)},\n'
                     f'    excerpt: {json.dumps(p["description"], ensure_ascii=False)},\n' f'    date: "{DATE}",\n'
                     f'    category: {json.dumps(p["category"], ensure_ascii=False)},\n' f'    readTime: "{p["read"]}",\n'
                     '    author: "Kamboh Associates",\n' f'    icon: "{p["icon"]}",\n' f'    link: "{link}"\n  }},')
            bl = bl.replace("const blogPosts = [", "const blogPosts = [" + entry, 1)
            # alphabetical "all guides" list
            items = list(re.finditer(r'      <a href="/blogs/([a-z0-9-]+)" style="display:block;padding:8px 0;font-size:\.83rem;[^\n]*\n', bl))
            tpl_line = items[0].group(0)
            new_line = re.sub(r'href="/blogs/[a-z0-9-]+"', f'href="{link}"', tpl_line)
            new_line = re.sub(r'>[^<>]*</a>\n$', f'>{E(p["h1"])}</a>\n', new_line)
            after = next((m for m in items if m.group(1) > p["slug"]), None)
            pos = after.start() if after else items[-1].end()
            bl = bl[:pos] + new_line + bl[pos:]
        if f"/blogs/{p['slug']}</loc>" not in sm:
            sm = sm.replace("</urlset>", f"  <url>\n    <loc>{BASE}/blogs/{p['slug']}</loc>\n    <lastmod>{DATE}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n</urlset>", 1)
    open("blogs.html", "w", encoding="utf-8").write(bl)
    open("sitemap.xml", "w", encoding="utf-8").write(sm)


main()
