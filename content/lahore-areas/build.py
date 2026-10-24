#!/usr/bin/env python3
"""Builds the /blogs/tax-consultant-<area>-lahore pages from per-area data.

Each page is written individually in data_*.py (lead, body, FAQs); this script
only supplies the shared chrome, schema and link blocks, so the article text
itself stays unique per URL. Usage: python3 content/lahore-areas/build.py [slug ...]
"""
import glob
import html
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SITE = "https://kambohassociates.com"
MODIFIED = "2026-10-24"
HUB_HREF = "/tax-consultant-lahore"
HUB_LABEL = "Tax Consultant Lahore — All Areas"

# Fees mirror pricing.html (the sitewide fee source); link targets are existing pages.
SERVICES = {
    "salaried": ("Salaried / pensioner income tax return", "Rs. 3,500", "/income-tax-filing"),
    "freelancer": ("Freelancer / remote-worker return", "Rs. 5,000", "/freelancer-tax-pakistan"),
    "soleprop": ("Sole proprietor / shop return", "Rs. 5,000", "/income-tax-filing"),
    "ntn": ("NTN registration (incl. ATL)", "Rs. 2,000", "/ntn-registration"),
    "wealth": ("Wealth statement (Section 116)", "Rs. 2,000", "/wealth-statement"),
    "aop": ("AOP / partnership return", "Rs. 8,000", "/aop-tax-return"),
    "strn": ("Sales tax registration (STRN)", "Rs. 3,000", "/sales-tax-registration"),
    "strmonthly": ("Monthly sales tax return", "Rs. 3,000 / month", "/sales-tax-return"),
    "pvtltd": ("Pvt Ltd company registration", "Rs. 15,000+", "/secp-company-registration-guide-2026"),
    "notice": ("FBR notice response", "Rs. 5,000+", "/fbr-notice-defense"),
    "overseas": ("Overseas Pakistani return", "Rs. 6,000", "/freelancer-overseas-tax-guide-pakistan"),
    "wht": ("Withholding tax statement", "Rs. 2,500 / month", "/withholding-tax"),
    "corporate": ("Company income tax return", "Rs. 18,000+", "/corporate-tax-return"),
    "eobi": ("EOBI employer registration", "Rs. 8,000", "/eobi-registration"),
    "impexp": ("Import / export registration", "Rs. 10,000+", "/import-export-registration"),
    "exempt": ("Tax exemption certificate", "Rs. 5,000+", "/tax-exemption-certificate"),
}

CTA = [
    ("Send your documents, get a fixed quote", "WhatsApp a photo of your CNIC and whatever paperwork you have. We reply with the exact fee before any work starts."),
    ("Talk to a Lahore tax consultant today", "Share your situation on WhatsApp — salary slip, rent agreement, notice, anything — and we tell you what is actually needed."),
    ("Not sure what you need to file?", "Message us first. A short WhatsApp chat usually settles whether you need a return, a wealth statement, or nothing at all."),
    ("File without taking a day off", "Our team works online from our Awan Town office, so you never have to visit or queue. Documents on WhatsApp, receipt back on WhatsApp."),
    ("Got a deadline or a notice?", "Tell us the date on the notice or the deadline you are facing — we prioritise time-bound work the same day."),
]


def load_pages():
    pages, clusters, extras = [], {}, {}
    for path in sorted(glob.glob(os.path.join(HERE, "data_*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        clusters.update(getattr(mod, "CLUSTERS", {}))
        extras.update(getattr(mod, "EXTRA", {}))
        for p in mod.PAGES:
            p["_file"] = os.path.basename(path)
            pages.append(p)
    for p in pages:
        if p["slug"] in extras:
            p["body"] = p["body"].rstrip() + "\n" + extras[p["slug"]]
    return pages, clusters


def inline(text):
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:48]


def render_body(src):
    """Tiny markup: ## h2, ### h3, - ul, 1. ol, | table |, > info box, blank-line paragraphs."""
    out, toc, block, kind = [], [], [], None

    def flush():
        nonlocal block, kind
        if not block:
            return
        if kind == "p":
            out.append("<p>" + inline(" ".join(block)) + "</p>")
        elif kind == "ul":
            out.append("<ul>" + "".join("<li>" + inline(b) + "</li>" for b in block) + "</ul>")
        elif kind == "ol":
            out.append("<ol>" + "".join("<li>" + inline(b) + "</li>" for b in block) + "</ol>")
        elif kind == "ib":
            out.append('<div class="ib"><i class="fas fa-lightbulb"></i><p>' + inline(" ".join(block)) + "</p></div>")
        elif kind == "table":
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in block]
            head = "".join("<th>" + inline(c) + "</th>" for c in rows[0])
            body = "".join("<tr>" + "".join("<td>" + inline(c) + "</td>" for c in r) + "</tr>" for r in rows[1:])
            out.append('<table class="dt"><thead><tr>' + head + "</tr></thead><tbody>" + body + "</tbody></table>")
        block, kind = [], None

    for raw in src.strip().split("\n"):
        line = raw.strip()
        if not line:
            flush()
            continue
        if line.startswith("## "):
            flush()
            title = line[3:].strip()
            hid = slugify(title)
            toc.append((hid, title))
            out.append(f'<h2 id="{hid}">{inline(title)}</h2>')
            continue
        if line.startswith("### "):
            flush()
            out.append("<h3>" + inline(line[4:].strip()) + "</h3>")
            continue
        for k, pat in (("ul", r"^- "), ("ol", r"^\d+\. "), ("table", r"^\|"), ("ib", r"^> ")):
            if re.match(pat, line):
                if kind != k:
                    flush()
                    kind = k
                block.append(line if k == "table" else re.sub(pat, "", line))
                break
        else:
            if kind != "p":
                flush()
                kind = "p"
            block.append(line)
    flush()
    return "\n  ".join(out), toc


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def old_published(slug):
    try:
        h = open(os.path.join(ROOT, "blogs", f"tax-consultant-{slug}-lahore.html"), encoding="utf-8-sig").read()
        m = re.search(r'"datePublished":"(\d{4}-\d{2}-\d{2})"', h)
        return m.group(1) if m else "2026-07-17"
    except FileNotFoundError:
        return MODIFIED


def nearby(page, pages_by_slug, clusters):
    cl = clusters[page["cluster"]]
    picks = page.get("near")
    if not picks:
        members = [p["slug"] for p in pages_by_slug.values() if p["cluster"] == page["cluster"] and p["slug"] != page["slug"]]
        members.sort()
        i = sum(map(ord, page["slug"])) % max(len(members), 1)
        picks = (members[i:] + members[:i])[:4]
    links = []
    for s in picks:
        name = pages_by_slug[s]["name"] if s in pages_by_slug else s.replace("-", " ").title()
        links.append((f"/blogs/tax-consultant-{s}-lahore", f"Tax consultant in {name}"))
    return cl, links


def build_page(page, pages_by_slug, clusters, shell):
    slug, name = page["slug"], page["name"]
    url = f"{SITE}/blogs/tax-consultant-{slug}-lahore"
    body_html, toc = render_body(page["body"])
    cl, near_links = nearby(page, pages_by_slug, clusters)

    svc_rows = "".join(
        f'<tr><td><a href="{SERVICES[k][2]}">{SERVICES[k][0]}</a></td><td>{SERVICES[k][1]}</td></tr>' for k in page["services"]
    )
    svc_heading = page.get("services_heading", f"Fees for the work {name} clients ask for most")
    toc.append(("fees", svc_heading))
    fees = (
        f'<h2 id="fees">{svc_heading}</h2>\n  '
        f'<table class="dt"><thead><tr><th>Service</th><th>Starting fee</th></tr></thead><tbody>{svc_rows}</tbody></table>\n  '
        f'<p>Full fee schedule: <a href="/pricing">pricing</a>. The quote you get on WhatsApp is final.</p>'
    )

    near_heading = page.get("near_heading", f"Areas next to {name}")
    toc.append(("nearby", near_heading))
    parent = f'<a href="{cl["parent_href"]}">{cl["parent_label"]}</a>'
    near_items = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in near_links)
    near = (
        f'<h2 id="nearby">{near_heading}</h2>\n  '
        f'<p>{page.get("near_intro", "Main area guide: " + parent + ". Pages for neighbouring localities:")}</p>\n  '
        f"<ul>{near_items}<li><a href=\"{HUB_HREF}\">All Lahore areas we cover</a></li></ul>"
    )

    toc.insert(len(toc) - 2, ("faqs", "FAQs"))
    faq_html = "".join(
        f'<div class="fi"><div class="fq-q">{html.escape(q)} <i class="fas fa-plus"></i></div><div class="fq-a">{inline(a)}</div></div>'
        for q, a in page["faq"]
    )
    faq = f'<h2 id="faqs">{page.get("faq_heading", name + " — questions we get asked")}</h2>\n  <div class="fq">{faq_html}</div>'

    cta_h, cta_p = CTA[sum(map(ord, slug)) % len(CTA)]
    wa_text = html.escape(f"Hi, I am in {name}, Lahore and need tax help.").replace(" ", "+")
    cta = (
        f'<div class="cta-box"><h3>{cta_h}</h3><p>{cta_p}</p><div class="cta-btns">'
        f'<a href="https://wa.me/923284675162?text={wa_text}" class="btn-w" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> WhatsApp 0328-4675162</a>'
        f'<a href="tel:03284675162" class="btn-g"><i class="fas fa-phone"></i> Call</a></div></div>'
    )

    article = f'<p class="lead">{inline(page["lead"])}</p>\n  {body_html}\n  {faq}\n  {cta}'
    modules = f'{fees}\n  {near}'


    breadcrumb_items = [("Home", f"{SITE}/"), ("Tax Consultant Lahore", f"{SITE}{HUB_HREF}")]
    if cl["parent_href"] != HUB_HREF:
        breadcrumb_items.append((cl["parent_label"], SITE + cl["parent_href"]))
    breadcrumb_items.append((name, url))

    schema = [
        {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": page["h1"][:110],
            "description": page["desc"],
            "datePublished": old_published(slug),
            "dateModified": MODIFIED,
            "inLanguage": "en-PK",
            "author": {"@type": "Organization", "name": "Kamboh Associates", "url": SITE},
            "publisher": {"@type": "Organization", "name": "Kamboh Associates", "url": SITE,
                          "logo": {"@type": "ImageObject", "url": f"{SITE}/android-chrome-512x512.png"}},
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "about": {"@type": "Place", "name": f"{name}, {page.get('locality', 'Lahore')}",
                      "containedInPlace": {"@type": "City", "name": page.get("locality", "Lahore")}},
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(breadcrumb_items)
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(inline(a))}}
                for q, a in page["faq"]
            ],
        },
    ]

    meta = (
        '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large"/>\n'
        f"<title>{html.escape(page['title'])}</title>\n"
        f'<meta name="description" content="{html.escape(page["desc"])}"/>\n'
        f'<link rel="canonical" href="{url}"/>\n'
        f'<meta property="og:type" content="article"/><meta property="og:title" content="{html.escape(page["title"])}"/>'
        f'<meta property="og:description" content="{html.escape(page["desc"])}"/><meta property="og:url" content="{url}"/>\n'
        f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>\n'
    )
    head = shell["head"].replace('<link rel="preconnect"', meta + '<link rel="preconnect"', 1)
    head = head.replace("<style>", "<style>\n.article h3{font-family:var(--fs);font-size:1.25rem;font-weight:600;color:#0F172A;margin:26px 0 10px}.article .cta-box h3{color:#fff;font-size:1.6rem;margin:0 0 10px}", 1)

    crumbs = '<a href="/"><i class="fas fa-home"></i> Home</a><i class="fas fa-chevron-right"></i>'
    crumbs += f'<a href="{HUB_HREF}">Lahore</a><i class="fas fa-chevron-right"></i>'
    if cl["parent_href"] != HUB_HREF:
        crumbs += f'<a href="{cl["parent_href"]}">{cl["short"]}</a><i class="fas fa-chevron-right"></i>'
    crumbs += f"<span>{html.escape(name)}</span>"
    words = len(strip_tags(article).split())
    hero = (
        '<section class="hero"><div class="container">\n'
        f'  <div class="breadcrumb">{crumbs}</div>\n'
        f'  <div class="badge"><i class="fas fa-map-marker-alt"></i> {html.escape(page.get("badge", cl["short"] + " — Local Tax Guide"))}</div>\n'
        f'  <h1>{html.escape(page["h1"])}</h1>\n'
        '  <div class="hero-meta"><div class="meta-item"><i class="far fa-calendar-alt"></i> Updated October 2026</div>'
        '<div class="meta-item"><i class="fas fa-user-tie"></i> Kamboh Associates</div>'
        f'<div class="meta-item"><i class="far fa-clock"></i> {max(3, round(words / 220))} min read</div>'
        f'<div class="meta-item"><i class="fas fa-map-pin"></i> {html.escape(name)}</div></div>\n'
        "</div></section>"
    )
    toc_links = "".join(f'<a href="#{i}"><i class="fas fa-circle"></i> {html.escape(strip_tags(t))[:46]}</a>' for i, t in toc)
    aside = (
        '<aside class="sidebar">\n'
        f'  <div class="sc reveal"><div class="st"><i class="fas fa-list"></i> Contents</div><nav class="rl">{toc_links}</nav></div>\n'
        f'  <div class="sc cc reveal"><h3>Based in {html.escape(name)}?</h3><p>We work online from Awan Town, Lahore — no visit needed.</p>'
        '<a href="https://wa.me/923284675162" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> WhatsApp Now</a></div>\n'
        f'  <div class="sc reveal"><div class="st"><i class="fas fa-map"></i> {html.escape(cl["short"])}</div><nav class="rl">'
        f'<a href="{cl["parent_href"]}"><i class="fas fa-circle"></i> {html.escape(cl["parent_label"])}</a>'
        f'<a href="{HUB_HREF}"><i class="fas fa-circle"></i> {HUB_LABEL}</a>'
        '<a href="/pricing"><i class="fas fa-circle"></i> Pricing</a></nav></div>\n'
        "</aside>"
    )
    return (
        head + "\n" + shell["nav"] + "\n" + hero + '\n<div class="container"><div class="layout">\n'
        f'<div><article><div class="article reveal">\n  {article}\n</div></article>\n'
        f'<section class="article reveal" style="margin-top:24px" aria-label="Fees and nearby areas">\n  {modules}\n</section></div>\n' + aside + "\n</div></div>\n"
        + shell["foot"] + "\n</body></html>\n"
    )


TOPIC_PAGES = {"high-net-worth-individuals", "it-software-companies", "multinational-foreign-companies",
               "real-estate-agents", "vs-chartered-accountant", "doctors"}


def legacy_area_slugs(done):
    """Area pages not yet rewritten, so the hub still links every live area URL."""
    redirected = {r["source"] for r in json.load(open(os.path.join(ROOT, "vercel.json")))["redirects"]}
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "blogs", "tax-consultant-*-lahore.html"))):
        slug = os.path.basename(f)[len("tax-consultant-"):-len("-lahore.html")]
        if slug in done or slug in TOPIC_PAGES or f"/blogs/tax-consultant-{slug}-lahore" in redirected:
            continue
        out.append(slug)
    return out


def build_hub(pages, clusters, shell):
    spec = importlib.util.spec_from_file_location("hub", os.path.join(HERE, "hub.py"))
    hub = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hub)
    H = hub.HUB
    url = SITE + HUB_HREF
    body_html, toc = render_body(H["body"])
    groups = []
    for key, cl in clusters.items():
        members = sorted((p for p in pages if p["cluster"] == key), key=lambda p: p["name"])
        if not members:
            continue
        items = "".join(
            f'<li><a href="/blogs/tax-consultant-{p["slug"]}-lahore">{html.escape(p["name"])}</a> — {html.escape(p["title"].split(":", 1)[-1].strip())}</li>'
            for p in members)
        main = "" if cl["parent_href"] == HUB_HREF else f'<p>Main guide: <a href="{cl["parent_href"]}">{html.escape(cl["parent_label"])}</a></p>'
        hid = "z-" + key
        toc.append((hid, cl["short"]))
        groups.append(f'<h2 id="{hid}">{html.escape(cl["short"])}</h2>{main}<ul>{items}</ul>')
    legacy = legacy_area_slugs({p["slug"] for p in pages})
    if legacy:
        toc.append(("z-more", "More Lahore localities"))
        items = "".join(f'<li><a href="/blogs/tax-consultant-{s}-lahore">{s.replace("-", " ").title()}</a></li>' for s in legacy)
        groups.append(f'<h2 id="z-more">More Lahore localities</h2><ul>{items}</ul>')
    toc.append(("faqs", "FAQs"))
    faq_html = "".join(
        f'<div class="fi"><div class="fq-q">{html.escape(q)} <i class="fas fa-plus"></i></div><div class="fq-a">{inline(a)}</div></div>'
        for q, a in H["faq"])
    article = (f'<p class="lead">{inline(H["lead"])}</p>\n  {body_html}\n  ' + "\n  ".join(groups)
               + f'\n  <h2 id="faqs">Questions about our Lahore service</h2>\n  <div class="fq">{faq_html}</div>')
    schema = [
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": H["h1"], "description": H["desc"],
         "url": url, "dateModified": MODIFIED, "inLanguage": "en-PK"},
        {"@context": "https://schema.org", "@type": "AccountingService", "name": "Kamboh Associates", "url": SITE,
         "telephone": "+923284675162", "priceRange": "Rs 2,000+",
         "address": {"@type": "PostalAddress", "streetAddress": "Shop No 34 Rizwan Block Market, opposite Rizwan Park, Awan Town",
                     "addressLocality": "Lahore", "addressRegion": "Punjab", "addressCountry": "PK"},
         "areaServed": {"@type": "City", "name": "Lahore"}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Tax Consultant Lahore", "item": url}]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(inline(a))}}
            for q, a in H["faq"]]},
    ]
    meta = (
        '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large"/>\n'
        f"<title>{html.escape(H['title'])}</title>\n"
        f'<meta name="description" content="{html.escape(H["desc"])}"/>\n'
        f'<link rel="canonical" href="{url}"/>\n'
        f'<meta property="og:type" content="website"/><meta property="og:title" content="{html.escape(H["title"])}"/>'
        f'<meta property="og:description" content="{html.escape(H["desc"])}"/><meta property="og:url" content="{url}"/>\n'
        f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>\n'
    )
    head = shell["head"].replace('<link rel="preconnect"', meta + '<link rel="preconnect"', 1)
    hero = (
        '<section class="hero"><div class="container">\n'
        '  <div class="breadcrumb"><a href="/"><i class="fas fa-home"></i> Home</a><i class="fas fa-chevron-right"></i><span>Tax Consultant Lahore</span></div>\n'
        '  <div class="badge"><i class="fas fa-map-marker-alt"></i> Lahore — All Areas</div>\n'
        f'  <h1>{html.escape(H["h1"])}</h1>\n'
        '  <div class="hero-meta"><div class="meta-item"><i class="far fa-calendar-alt"></i> Updated October 2026</div>'
        '<div class="meta-item"><i class="fas fa-map-pin"></i> Awan Town, Lahore</div></div>\n</div></section>'
    )
    toc_links = "".join(f'<a href="#{i}"><i class="fas fa-circle"></i> {html.escape(t)[:46]}</a>' for i, t in toc)
    aside = (
        '<aside class="sidebar">\n'
        f'  <div class="sc reveal"><div class="st"><i class="fas fa-list"></i> Areas</div><nav class="rl">{toc_links}</nav></div>\n'
        '  <div class="sc cc reveal"><h3>Anywhere in Lahore</h3><p>One WhatsApp message gets you a fixed quote.</p>'
        '<a href="https://wa.me/923284675162" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> WhatsApp Now</a></div>\n'
        "</aside>"
    )
    out = (head + "\n" + shell["nav"] + "\n" + hero + '\n<div class="container"><div class="layout">\n'
           f'<article><div class="article reveal">\n  {article}\n</div></article>\n' + aside + "\n</div></div>\n"
           + shell["foot"] + "\n</body></html>\n")
    with open(os.path.join(ROOT, HUB_HREF.strip("/") + ".html"), "w", encoding="utf-8") as f:
        f.write(out)


def update_sitemap(pages):
    path = os.path.join(ROOT, "sitemap.xml")
    xml = open(path, encoding="utf-8").read()
    for p in pages:
        loc = re.escape(f"{SITE}/blogs/tax-consultant-{p['slug']}-lahore</loc>")
        xml = re.sub(loc + r"(\s*)<lastmod>[^<]*</lastmod>", lambda m: m.group(0)[: m.group(0).rfind("<lastmod>")] + f"<lastmod>{MODIFIED}</lastmod>", xml)
    hub = f"{SITE}{HUB_HREF}</loc>"
    if hub not in xml:
        entry = (f"  <url>\n    <loc>{SITE}{HUB_HREF}</loc>\n    <lastmod>{MODIFIED}</lastmod>\n"
                 "    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n")
        xml = xml.replace("</urlset>", entry + "</urlset>")
    else:
        xml = re.sub(re.escape(hub) + r"(\s*)<lastmod>[^<]*</lastmod>", hub + r"\1" + f"<lastmod>{MODIFIED}</lastmod>", xml)
    open(path, "w", encoding="utf-8").write(xml)


def main():
    shell = {k: open(os.path.join(HERE, f"shell_{k}.html"), encoding="utf-8").read() for k in ("head", "nav", "foot")}
    pages, clusters = load_pages()
    by_slug = {p["slug"]: p for p in pages}
    only = set(sys.argv[1:])
    for p in pages:
        if only and p["slug"] not in only:
            continue
        out = build_page(p, by_slug, clusters, shell)
        with open(os.path.join(ROOT, "blogs", f"tax-consultant-{p['slug']}-lahore.html"), "w", encoding="utf-8") as f:
            f.write(out)
    build_hub(pages, clusters, shell)
    update_sitemap(pages)
    print(f"built {len(only) or len(pages)} page(s) + hub")


if __name__ == "__main__":
    main()
