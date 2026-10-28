#!/usr/bin/env python3
"""Builds /digital/blog posts and the blog index from content/digital/posts/*.py.

Each post module defines POST = dict(slug, title, h1, description, keyword, published, updated,
category, answer, takeaways, body, faqs, sources, method, related). The page shell (top bar, menu,
footer) is copied from an existing /digital page and then normalised by shell.py.
Usage: python3 content/digital/blog_build.py && python3 content/digital/shell.py
"""
import glob
import html as H
import importlib.util
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://kambohassociates.com"
ORG = SITE + "/digital#organization"
TEMPLATE = os.path.join(ROOT, "digital", "business-websites.html")
WA = "https://wa.me/923284675162?text="

EXTRA_CSS = """<style id="dg-blog">
.answer-box{background:#F0FDFA;border:1px solid rgba(20,184,166,.35);border-left:4px solid #14B8A6;border-radius:12px;padding:18px 22px;margin:0 0 24px}
.answer-box .lbl{font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:#0F766E;font-weight:700;margin-bottom:6px}
.answer-box p{margin:0!important;color:#0F172A!important;font-size:1rem!important}
.takeaways{background:var(--bg-2);border:1px solid var(--border);border-radius:12px;padding:18px 22px 6px;margin:0 0 26px}
.takeaways h2{font-size:1.1rem!important;margin:0 0 10px!important}.takeaways h2::before{display:none!important}
.toc{border:1px solid var(--border);border-radius:12px;padding:16px 22px;margin:0 0 30px}
.toc .lbl{font-weight:700;font-size:.85rem;margin-bottom:8px;color:var(--text)}
.toc ol{margin:0 0 0 18px!important}.toc a{border:none!important}
.eeat{border-top:1px solid var(--border);margin-top:36px;padding-top:24px}
.eeat h2{font-size:1.25rem!important}
.author-box{display:flex;gap:14px;align-items:flex-start;background:var(--bg-2);border:1px solid var(--border);border-radius:12px;padding:18px 20px;margin:18px 0}
.author-box .av{width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,#0F172A,#14B8A6);color:#fff;display:grid;place-items:center;font-weight:700;flex-shrink:0}
.author-box p{margin:0 0 6px!important;font-size:.9rem!important}
.sources li{font-size:.86rem!important}
.related{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:12px 0 0}
.related a{display:block;border:1px solid var(--border)!important;border-radius:10px;padding:12px 14px;font-weight:600;color:var(--text)!important}
.post-card{display:block;border:1px solid var(--border);border-radius:14px;padding:20px 22px;margin:0 0 16px;background:var(--surface)}
.post-card h2{font-size:1.2rem!important;margin:0 0 8px!important}.post-card h2::before{display:none!important}
.post-card p{margin:0!important}
@media(max-width:600px){.article-body table{display:block;overflow-x:auto}}
</style>
"""


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", H.unescape(re.sub(r"<[^>]+>", "", t)).lower()).strip("-")[:60]


def load_posts():
    posts = []
    for f in sorted(glob.glob(os.path.join(HERE, "posts", "*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        posts.append(m.POST)
    return posts


def esc(s):
    return H.escape(s, quote=True)


def head_and_shell():
    t = open(TEMPLATE, encoding="utf-8").read()
    head_end = t.index("</head>")
    head = t[:head_end]
    # keep only the generic head (charset, viewport, fonts, styles, analytics); drop page-specific tags
    head = re.sub(r"<title>[^<]*</title>", "<title>@@TITLE@@</title>", head, count=1)
    head = re.sub(r'<meta name="description" content="[^"]*"\s*/?>', '<meta name="description" content="@@DESC@@"/>', head, count=1)
    head = re.sub(r'<link rel="canonical" href="[^"]*"\s*/?>', '<link rel="canonical" href="@@URL@@"/>', head, count=1)
    head = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>\s*', "", head)
    head = re.sub(r'<meta (?:property|name)="(?:og|twitter):[^"]*" content="[^"]*"\s*/?>\s*', "", head)
    head = head.replace('<style id="dg-nav">', '<style id="dg-nav">', 1)
    body_start = t.index("<!-- HERO -->")
    shell_top = t[head_end:body_start]
    foot = t[t.index("</aside>") + len("</aside>"):]
    return head, shell_top, foot


def og(title, desc, url, kind):
    return (f'<meta property="og:locale" content="en_US"/><meta property="og:type" content="{kind}"/>\n'
            f'<meta property="og:title" content="{esc(title)}"/>\n<meta property="og:description" content="{esc(desc)}"/>\n'
            f'<meta property="og:url" content="{url}"/>\n<meta property="og:image" content="{SITE}/images/og-default.jpg"/>\n'
            '<meta property="og:image:width" content="1200"/>\n<meta property="og:image:height" content="630"/>\n'
            '<meta property="og:site_name" content="Kamboh Associates Digital"/>\n'
            f'<meta name="twitter:card" content="summary_large_image"/>\n<meta name="twitter:title" content="{esc(title)}"/>\n'
            f'<meta name="twitter:description" content="{esc(desc)}"/>\n<meta name="twitter:image" content="{SITE}/images/og-default.jpg"/>\n')


def ld(obj):
    return '<script type="application/ld+json">%s</script>\n' % json.dumps(obj, ensure_ascii=False)


SIDEBAR = """<aside class="sidebar">
<div class="consult-card"><h3>Free Consultation</h3><p>A real quote within one business day</p><a href="{wa}"><i class="fab fa-whatsapp"></i> WhatsApp Now</a></div>
<div class="sidebar-card"><div class="sidebar-title"><i class="fas fa-globe"></i> Web Development</div>
<a href="/digital/business-websites" style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--border);color:var(--text-3);font-size:.87rem"><i class="fas fa-display" style="color:var(--gold-light)"></i> Business Websites</a>
<a href="/digital/ecommerce-development" style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--border);color:var(--text-3);font-size:.87rem"><i class="fas fa-cart-shopping" style="color:var(--gold-light)"></i> E-commerce Development</a>
<a href="/digital/web-app-development" style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--border);color:var(--text-3);font-size:.87rem"><i class="fas fa-code" style="color:var(--gold-light)"></i> Web App Development</a>
<a href="/digital/pricing" style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--border);color:var(--text-3);font-size:.87rem"><i class="fas fa-tags" style="color:var(--gold-light)"></i> Pricing</a>
<a href="/digital/blog" style="display:flex;align-items:center;gap:10px;padding:10px 0;color:var(--text-3);font-size:.87rem"><i class="fas fa-book-open" style="color:var(--gold-light)"></i> All Guides</a>
</div>
<div class="sidebar-card"><div class="sidebar-title"><i class="fas fa-building"></i> About Us</div><p style="font-size:.85rem;color:var(--text-3);line-height:1.7">A Lahore-based team building business websites, online stores and web applications for clients in Pakistan and abroad. Fixed starting prices, milestone payments, and you own your domain and code.</p><a href="/digital/contact" style="display:block;text-align:center;color:#14B8A6;font-size:.85rem;font-weight:600;margin-top:12px"><i class="fas fa-arrow-right"></i> Get a Quote</a></div>
</aside>
</div>
"""

AUTHOR = """<aside class="author-box"><div class="av">KA</div><div>
<p><strong>Written and fact-checked by the Kamboh Associates Digital team</strong>, Lahore.</p>
<p>We build business websites, online stores and web applications for clients in Pakistan and abroad. Kamboh Associates has run from the same Awan Town, Lahore office since 2008, and publishes its web development prices openly on its <a href="/digital/pricing">pricing page</a>.</p>
<p>Questions or corrections: WhatsApp <a href="https://wa.me/923284675162">0328-4675162</a> or email <a href="mailto:info@kambohassociates.com">info@kambohassociates.com</a>.</p>
</div></aside>"""


def render_post(p, head, shell_top, foot, all_posts):
    url = f"{SITE}/digital/blog/{p['slug']}"
    body = p["body"]
    h2s = re.findall(r'<h2 id="([^"]+)">([\s\S]*?)</h2>', body)
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in h2s)
    faq_html = "".join(
        f'<div class="faq-item"><div class="faq-q">{esc(q)} <i class="fas fa-plus"></i></div><div class="faq-a">{a}</div></div>'
        for q, a in p["faqs"])
    src_html = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{esc(t)}</a></li>' for t, u in p["sources"])
    by_slug = {x["slug"]: x for x in all_posts}
    rel = [(f"/digital/blog/{s}", by_slug[s]["h1"]) for s in p["related"] if s in by_slug]
    rel += p.get("service_links", [])
    rel_html = "".join(f'<a href="{u}">{esc(t)}</a>' for u, t in rel)
    alltext = " ".join([body, p["answer"], " ".join(p["takeaways"]), p["method"]] + [q + " " + a for q, a in p["faqs"]])
    words = len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", alltext)))
    mins = max(4, round(words / 220))
    wa = WA + p.get("wa", "Hi%2C%20I%20read%20your%20guide%20and%20need%20a%20website%20quote")
    takeaways = "".join(f"<li>{t}</li>" for t in p["takeaways"])

    blog = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["h1"], "description": p["description"],
            "datePublished": p["published"], "dateModified": p["updated"], "inLanguage": "en",
            "author": {"@type": "Organization", "@id": ORG, "name": "Kamboh Associates Digital", "url": SITE + "/digital"},
            "publisher": {"@type": "Organization", "@id": ORG, "name": "Kamboh Associates Digital",
                          "logo": {"@type": "ImageObject", "url": SITE + "/android-chrome-512x512.png", "width": 512, "height": 512}},
            "mainEntityOfPage": {"@type": "WebPage", "@id": url}, "url": url,
            "image": {"@type": "ImageObject", "url": SITE + "/images/og-default.jpg", "width": 1200, "height": 630},
            "keywords": ", ".join([p["keyword"]] + p.get("cluster", [])), "articleSection": p["category"],
            "wordCount": words, "citation": [u for _, u in p["sources"]]}
    faqld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in p["faqs"]]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Web Development", "item": SITE + "/digital"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/digital/blog"},
        {"@type": "ListItem", "position": 3, "name": p["h1"], "item": url}]}

    h = head.replace("@@TITLE@@", esc(p["title"])).replace("@@DESC@@", esc(p["description"])).replace("@@URL@@", url)
    h += og(p["title"], p["description"], url, "article")
    h += f'<meta property="article:published_time" content="{p["published"]}"/>\n<meta property="article:modified_time" content="{p["updated"]}"/>\n'
    h += ld(blog) + ld(faqld) + ld(crumbs) + EXTRA_CSS
    hero = f"""<!-- HERO -->
<section class="blog-post-hero"><div class="container">
<nav class="breadcrumb"><a href="/digital">Web Development</a><i class="fas fa-chevron-right"></i><a href="/digital/blog">Blog</a><i class="fas fa-chevron-right"></i><span>{esc(p['crumb'])}</span></nav>
<div class="blog-meta-tag"><i class="fas fa-tags"></i> {esc(p['category'])}</div>
<h1>{esc(p['h1'])}</h1>
<div class="blog-hero-meta"><div class="blog-meta-item"><i class="fas fa-user-check"></i> Kamboh Associates Digital team</div><div class="blog-meta-item"><i class="far fa-calendar-check"></i> Updated <time datetime="{p['updated']}">{p['updated_h']}</time></div><div class="blog-meta-item"><i class="far fa-clock"></i> {mins} min read</div></div>
</div></section>

<div class="blog-layout container">
<article class="article-body">
<div class="answer-box"><div class="lbl">Short answer</div><p>{p['answer']}</p></div>
<div class="takeaways"><h2 id="key-takeaways">Key Takeaways</h2><ul>{takeaways}</ul></div>
<nav class="toc" aria-label="Contents"><div class="lbl">In this guide</div><ol>{toc}<li><a href="#faqs">Frequently asked questions</a></li></ol></nav>
{body}
<h2 id="faqs">Frequently Asked Questions</h2>
<div class="faq-list">{faq_html}</div>
<section class="eeat">
<h2 id="how-we-researched">How We Researched This Guide</h2>
<p>{p['method']}</p>
<h2 id="sources">Sources</h2>
<ol class="sources">{src_html}</ol>
<p style="font-size:.85rem;color:var(--text-3)"><strong>Disclosure:</strong> Kamboh Associates sells the web development services discussed here. Other providers' prices are quoted from their own public pages on the dates shown and may have changed. We correct errors as soon as they are reported. First published <time datetime="{p['published']}">{p['published_h']}</time>; last reviewed <time datetime="{p['updated']}">{p['updated_h']}</time>.</p>
{AUTHOR}
<h2 id="keep-reading">Keep Reading</h2>
<div class="related">{rel_html}</div>
</section>
<div class="info-box"><i class="fas fa-circle-info"></i><p><strong>{p['cta']}</strong> WhatsApp <a href="{wa}">0328-4675162</a> with a short description of your project and we'll reply within one business day with a fixed price and timeline.</p></div>
</article>
"""
    return h + shell_top.replace("<!-- HERO -->", "") + hero + SIDEBAR.format(wa=wa) + foot


def render_index(posts, head, shell_top, foot):
    url = SITE + "/digital/blog"
    title = "Web Development Blog: Website Costs and Guides"
    desc = "Plain-language guides for Pakistani and overseas businesses on website prices, platforms, online stores and hiring a developer, with real PKR figures."
    cards = "".join(
        f'<a class="post-card" href="/digital/blog/{p["slug"]}"><h2>{esc(p["h1"])}</h2><p>{esc(p["description"])}</p></a>'
        for p in sorted(posts, key=lambda x: x["order"]))
    items = {"@context": "https://schema.org", "@type": "CollectionPage", "name": title, "url": url, "description": desc,
             "publisher": {"@id": ORG},
             "mainEntity": {"@type": "ItemList", "itemListElement": [
                 {"@type": "ListItem", "position": n, "url": f"{SITE}/digital/blog/{p['slug']}", "name": p["h1"]}
                 for n, p in enumerate(sorted(posts, key=lambda x: x["order"]), 1)]}}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Web Development", "item": SITE + "/digital"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": url}]}
    h = head.replace("@@TITLE@@", esc(title)).replace("@@DESC@@", esc(desc)).replace("@@URL@@", url)
    h += og(title, desc, url, "website") + ld(items) + ld(crumbs) + EXTRA_CSS
    hero = f"""<!-- HERO -->
<section class="blog-post-hero"><div class="container">
<nav class="breadcrumb"><a href="/digital">Web Development</a><i class="fas fa-chevron-right"></i><span>Blog</span></nav>
<div class="blog-meta-tag"><i class="fas fa-book-open"></i> Guides</div>
<h1>Website Costs, Platforms and Practical Guides</h1>
<div class="blog-hero-meta"><div class="blog-meta-item"><i class="fas fa-info-circle"></i> Written by our Lahore web team for business owners in Pakistan and abroad. Every price we quote matches our published price list.</div></div>
</div></section>

<div class="blog-layout container">
<article class="article-body">
<p>These guides answer the questions business owners ask us before they commit to a website: what it should cost, which platform suits them, what an online store needs in Pakistan, and how to compare quotes. Each guide lists its sources and the date it was last checked.</p>
{cards}
</article>
"""
    return h + shell_top.replace("<!-- HERO -->", "") + hero + SIDEBAR.format(wa=WA + "Hi%2C%20I%20need%20a%20website%20quote") + foot


def main():
    posts = load_posts()
    head, shell_top, foot = head_and_shell()
    os.makedirs(os.path.join(ROOT, "digital", "blog"), exist_ok=True)
    for p in posts:
        open(os.path.join(ROOT, "digital", "blog", p["slug"] + ".html"), "w", encoding="utf-8").write(
            render_post(p, head, shell_top, foot, posts))
    open(os.path.join(ROOT, "digital", "blog", "index.html"), "w", encoding="utf-8").write(render_index(posts, head, shell_top, foot))
    print("built %d posts + index" % len(posts))


if __name__ == "__main__":
    main()
