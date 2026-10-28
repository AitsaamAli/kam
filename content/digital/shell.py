#!/usr/bin/env python3
"""Gives every /digital page its own web-development shell, separate from the tax site.

Replaces the shared tax top bar, navigation, footer, sidebar "about" card and breadcrumb root,
points schema at the digital entity, and writes sitemap-digital.xml. Safe to re-run.
Usage: python3 content/digital/shell.py
After running, check isolation with: python3 content/digital-guard/guard.py
"""
import glob
import html as H
import json
import os
import re
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://kambohassociates.com"
ORG_ID = SITE + "/digital#organization"
TODAY = date.today().isoformat()

# Prices come from digital/pricing.html; keep them in one place.
PRICES = {"starter": "Rs 40,500", "business": "Rs 85,500", "store": "Rs 157,500", "app": "Rs 360,000"}

DIGITAL_ORG = {
    "@type": "Organization",
    "@id": ORG_ID,
    "name": "Kamboh Associates Digital",
    "url": SITE + "/digital",
    "description": "The web development team of Kamboh Associates, Lahore: business websites, online stores and web applications for clients in Pakistan and abroad.",
    "parentOrganization": {"@id": SITE + "/#organization"},
    "telephone": "+923284675162",
    "email": "info@kambohassociates.com",
    "areaServed": ["Pakistan", "United Arab Emirates", "Saudi Arabia", "United Kingdom", "Canada", "United States"],
    "logo": {"@type": "ImageObject", "url": SITE + "/android-chrome-512x512.png", "width": 512, "height": 512},
}

# Starting prices used in Service schema (must match digital/pricing.html)
OFFERS = {"digital/business-websites.html": "40500", "digital/ecommerce-development.html": "157500",
          "digital/web-app-development.html": "360000", "digital/web-development-lahore.html": "40500"}

# Day-1 titles and descriptions (no tax terms; unique site-wide).
META = {
    "digital/index.html": ("Web Development Company in Pakistan | Kamboh Associates",
                           "Business websites from Rs 40,500, online stores from Rs 157,500 and web apps from Rs 360,000, built by a Lahore team for clients in Pakistan and abroad."),
    "digital/business-websites.html": ("Business Website Development in Pakistan, from Rs 40,500",
                                       "Fast, mobile-first business websites with fixed prices and clear timelines: 5–10 pages, CMS, WhatsApp and click-to-call, ready in two weeks."),
    "digital/ecommerce-development.html": ("E-commerce Website Development, from Rs 157,500",
                                           "Online stores built to sell: product catalogue, payment setup, courier and COD flow, WhatsApp ordering and a checkout that works on mobile."),
    "digital/web-app-development.html": ("Custom Web Application Development, from Rs 360,000",
                                         "Booking systems, client portals and internal tools for businesses that have outgrown a standard website. Scoped first, priced before we build."),
    "digital/web-development-lahore.html": ("Web Development Company in Lahore | Kamboh Associates",
                                            "A Lahore web development team you can meet in person: business websites, online stores and web apps with fixed prices and same-day replies."),
    "digital/pricing.html": ("Website Development Price in Pakistan 2026: Price List",
                             "Published PKR prices: websites from Rs 40,500, online stores from Rs 157,500, web apps from Rs 360,000, with milestones and market comparison."),
    "digital/contact.html": ("Get a Website Quote in One Business Day",
                             "Message us on WhatsApp with your project and get a real price and timeline within one business day, not a sales call. Lahore team, clients worldwide."),
}

LOGO_SVG = ('<svg width="{s}" height="{s}" viewBox="0 0 46 46" xmlns="http://www.w3.org/2000/svg"><defs>'
            '<linearGradient id="{p}g1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1E293B"/><stop offset="100%" stop-color="#0F172A"/></linearGradient>'
            '<linearGradient id="{p}g2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#5EEAD4"/><stop offset="100%" stop-color="#14B8A6"/></linearGradient></defs>'
            '<circle cx="23" cy="23" r="23" fill="url(#{p}g1)"/><circle cx="23" cy="23" r="21" fill="none" stroke="url(#{p}g2)" stroke-width="1.5"/>'
            '<text x="23" y="27" font-family="Cinzel,serif" font-size="12" font-weight="700" fill="url(#{p}g2)" text-anchor="middle" letter-spacing="1">KA</text></svg>')

NAV = [("/digital", "Home"), ("/digital/business-websites", "Business Websites"), ("/digital/ecommerce-development", "Online Stores"),
       ("/digital/web-app-development", "Web Apps"), ("/digital/pricing", "Pricing"), ("/digital/contact", "Contact")]


def header(active):
    promo = ("Business websites from {starter} &nbsp;&bull;&nbsp; Online stores from {store} &nbsp;&bull;&nbsp; "
             "Web apps from {app} &nbsp;&bull;&nbsp; A real quote within one business day").format(**PRICES)
    items = "".join('<li><a href="%s"%s>%s</a></li>' % (u, ' class="active"' if u == active else "", t) for u, t in NAV)
    mob = "".join('<a href="%s">%s</a>' % (u, t) for u, t in NAV)
    return f'''<div class="topbar">
  <div class="container">
    <div class="topbar-left"><div class="topbar-promo-wrap"><span class="topbar-promo">{promo} &nbsp;&nbsp;&nbsp;&nbsp;</span><span class="topbar-promo" aria-hidden="true">{promo} &nbsp;&nbsp;&nbsp;&nbsp;</span></div></div>
    <div class="topbar-right">
      <a href="https://wa.me/923284675162?text=Hi%2C%20I%20need%20a%20quote%20for%20a%20website" target="_blank" rel="noopener"><i class="fab fa-whatsapp"></i><span>WhatsApp 0328-4675162</span></a>
      <a href="mailto:info@kambohassociates.com"><i class="fas fa-envelope"></i><span>info@kambohassociates.com</span></a>
    </div>
  </div>
</div>

<!-- NAVBAR (web development) -->
<nav class="navbar" id="navbar">
  <div class="container">
    <a href="/digital" class="logo">
      <div class="logo-emblem">{LOGO_SVG.format(s=44, p="n")}</div>
      <div>
        <div class="logo-name">KAMBOH ASSOCIATES</div>
        <div class="logo-sub">Web Development</div>
      </div>
    </a>
    <ul class="nav-links">{items}</ul>
    <div class="nav-actions">
      <span class="nav-phone"><i class="fas fa-phone"></i><a href="tel:+923284675162">0328-4675162</a></span>
      <a href="/digital/contact" class="nav-cta">Get a Quote</a>
      <button class="hamburger" id="hamburger" onclick="toggleMobileNav()" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
  <div class="mobile-nav" id="mobileNav">
    {mob}
    <div class="mobile-nav-tools"><a href="https://wa.me/923284675162?text=Hi%2C%20I%20need%20a%20quote%20for%20a%20website" target="_blank" rel="noopener" style="color:#25D366;display:flex;align-items:center;gap:8px;padding:16px 24px"><i class="fab fa-whatsapp"></i>WhatsApp for a quote</a></div>
  </div>
</nav>'''


def footer():
    return f'''<footer>
  <div class="container">
    <div class="footer-grid">
      <div>
        <a href="/digital" class="logo" style="margin-bottom:0;display:inline-flex">
          {LOGO_SVG.format(s=36, p="f")}
          <div style="margin-left:10px">
            <div class="logo-name" style="color:#fff">KAMBOH ASSOCIATES</div>
            <div class="logo-sub">Web Development</div>
          </div>
        </a>
        <p class="footer-brand-desc">Business websites, online stores and web applications, built in Lahore for clients in Pakistan, the Gulf, the UK and North America.</p>
        <div class="footer-contact-row"><i class="fas fa-map-marker-alt"></i><span>Shop No 34 Rizwan Block Market, opposite Rizwan Park, Awan Town, Lahore 54660, Pakistan</span></div>
        <div class="footer-contact-row"><i class="fas fa-phone"></i><a href="tel:+923284675162">0328-4675162</a></div>
        <div class="footer-contact-row"><i class="fas fa-envelope"></i><a href="mailto:info@kambohassociates.com">info@kambohassociates.com</a></div>
      </div>
      <div>
        <div class="footer-col-head">What We Build</div>
        <ul class="footer-links">
          <li><a href="/digital/business-websites">Business Websites</a></li>
          <li><a href="/digital/ecommerce-development">E-commerce Stores</a></li>
          <li><a href="/digital/web-app-development">Web Applications</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-head">Company</div>
        <ul class="footer-links">
          <li><a href="/digital/web-development-lahore">Lahore Team</a></li>
          <li><a href="/digital/pricing">Pricing</a></li>
          <li><a href="/digital/contact">Get a Quote</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-head">Legal</div>
        <ul class="footer-links">
          <li><a href="/privacy">Privacy Policy</a></li>
          <li><a href="/terms">Terms of Service</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; {date.today().year} Kamboh Associates, Lahore. Established 2008.</span>
      <div class="footer-bottom-links"><a href="/privacy">Privacy</a><a href="/terms">Terms</a></div>
    </div>
  </div>
</footer>'''


ABOUT = ('<div class="sidebar-card"><div class="sidebar-title"><i class="fas fa-building"></i> About Us</div>'
         '<p style="font-size:.85rem;color:var(--text-3);line-height:1.7">A Lahore-based team building business websites, '
         'online stores and web applications for clients in Pakistan and abroad. Fixed starting prices, milestone payments, '
         'and you own your domain and code.</p><a href="/digital/contact" style="display:block;text-align:center;color:#14B8A6;'
         'font-size:.85rem;font-weight:600;margin-top:12px"><i class="fas fa-arrow-right"></i> Get a Quote</a></div>')


def url_of(p):
    return SITE + "/" + (p[:-len("/index.html")] if p.endswith("/index.html") else p[:-5])


def fix_schema(s, p):
    def one(m):
        data = json.loads(m.group(1))
        objs = data if isinstance(data, list) else [data]
        for o in objs:
            if not isinstance(o, dict):
                continue
            if "provider" in o:
                o["provider"] = DIGITAL_ORG
                if p in OFFERS:
                    o["offers"] = {"@type": "Offer", "price": OFFERS[p], "priceCurrency": "PKR",
                                   "url": SITE + "/digital/pricing", "description": "Starting price"}
            if o.get("@type") == "BreadcrumbList":
                items = [i for i in o["itemListElement"] if i.get("item") != SITE + "/"]
                for n, i in enumerate(items, 1):
                    i["position"] = n
                o["itemListElement"] = items
            if p in META and o.get("@type") in ("Service", "WebPage", "ContactPage"):
                o["description"] = META[p][1]
        return '<script type="application/ld+json">%s</script>' % json.dumps(data, ensure_ascii=False)
    return re.sub(r'<script type="application/ld\+json">([\s\S]*?)</script>', one, s)


def build(p):
    s = open(os.path.join(ROOT, p), encoding="utf-8").read()
    url = url_of(p)
    path = url[len(SITE):]
    a = s.index('<div class="topbar">')
    b = s.index("</nav>", s.index('<nav class="navbar"')) + len("</nav>")
    s = s[:a] + header(path) + s[b:]
    a = s.index("<footer>")
    b = s.index("</footer>") + len("</footer>")
    s = s[:a] + footer() + s[b:]
    s = re.sub(r'<div class="sidebar-card"><div class="sidebar-title"><i class="fas fa-building"></i> About [^<]*</div>[\s\S]*?</a></div>', ABOUT, s)
    # breadcrumb starts at the web-development home
    s = s.replace('<a href="/"><i class="fas fa-home"></i> Home</a><i class="fas fa-chevron-right"></i>', "", 1)
    s = s.replace('<!-- NAVBAR -->\n', "")
    if p in META:
        t, d = META[p]
        s = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % H.escape(t, quote=False), s, count=1)
        for pat in (r'(<meta name="description" content=")[^"]*(")', r'(<meta property="og:description" content=")[^"]*(")',
                    r'(<meta name="twitter:description" content=")[^"]*(")'):
            s = re.sub(pat, lambda m: m.group(1) + H.escape(d) + m.group(2), s)
        for pat in (r'(<meta property="og:title" content=")[^"]*(")', r'(<meta name="twitter:title" content=")[^"]*(")'):
            s = re.sub(pat, lambda m: m.group(1) + H.escape(t) + m.group(2), s)
        s = re.sub(r'(<meta property="og:site_name" content=")[^"]*(")', r"\1Kamboh Associates Digital\2", s)
    s = fix_schema(s, p)
    # the shared stylesheet hides the menu below 1500px for the long tax menu; ours is short
    if 'id="dg-nav"' not in s:
        s = s.replace("</head>", '<style id="dg-nav">@media(min-width:1025px){.nav-links,.nav-phone{display:flex!important}.hamburger{display:none!important}}</style>\n</head>', 1)
    open(os.path.join(ROOT, p), "w", encoding="utf-8").write(s)
    return url


def main():
    pages = sorted(os.path.relpath(x, ROOT) for x in glob.glob(os.path.join(ROOT, "digital", "**", "*.html"), recursive=True))
    urls = [build(p) for p in pages]
    body = "".join("  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n  </url>\n" % (u, TODAY) for u in urls)
    open(os.path.join(ROOT, "sitemap-digital.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>\n")
    # take /digital URLs out of the main sitemap; nothing else changes
    sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    sm = re.sub(r"\s*<url>\s*<loc>%s/digital(?:/[^<]*)?</loc>[\s\S]*?</url>" % re.escape(SITE), "", sm)
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sm)
    rb = open(os.path.join(ROOT, "robots.txt"), encoding="utf-8").read()
    line = "Sitemap: %s/sitemap-digital.xml" % SITE
    if line not in rb:
        open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(rb.rstrip("\n") + "\n" + line + "\n")
    print("rebuilt %d pages" % len(urls))


if __name__ == "__main__":
    main()
