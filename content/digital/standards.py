#!/usr/bin/env python3
"""Adds a short 'Standards we follow' line, with authoritative sources, to the /digital service pages.
Placed at the end of the section it belongs to. Idempotent. Usage: python3 content/digital/standards.py"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
L = {
    "seo": ("Google Search Central: SEO Starter Guide", "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"),
    "cwv": ("web.dev: Core Web Vitals", "https://web.dev/articles/vitals"),
    "wcag": ("W3C: Web Content Accessibility Guidelines", "https://www.w3.org/WAI/standards-guidelines/wcag/"),
    "ecom": ("Google Search Central: Ecommerce guidance", "https://developers.google.com/search/docs/specialty/ecommerce"),
    "owasp": ("OWASP Top Ten", "https://owasp.org/www-project-top-ten/"),
    "gbp": ("Google Business Profile Help", "https://support.google.com/business/"),
    "pknic": ("PKNIC: .pk domain fees", "https://pknic.net.pk/how-to-pay.html"),
}
PAGES = {
    "digital/business-websites.html": ("Built to a Real Standard", ["seo", "cwv", "wcag"], "Standards we build to"),
    "digital/ecommerce-development.html": ("Built for Mobile Shoppers First", ["ecom", "cwv"], "Guidance we follow"),
    "digital/web-app-development.html": ("Data and Security, Handled Properly", ["owasp", "wcag"], "Standards we build to"),
    "digital/web-development-lahore.html": ("What We Build", ["gbp", "seo"], "Guidance we follow"),
    "digital/pricing.html": ("What Can Change the Final Price", ["pknic"], "Third-party fees are paid at official rates"),
}


def main():
    os.chdir(ROOT)
    for f, (h2, keys, label) in PAGES.items():
        t = open(f, encoding="utf-8").read()
        if 'class="standards-line"' in t:
            continue
        m = re.search(r"<h2[^>]*>\s*" + re.escape(h2), t)
        assert m, (f, h2)
        nxt = [x for x in (t.find("<h2", m.end()), t.find("</section>", m.end())) if x > 0]
        end = min(nxt)
        seg = t[m.end():end]
        last = max(seg.rfind(x) + len(x) for x in ("</p>", "</ul>", "</ol>", "</table>") if seg.rfind(x) >= 0)
        links = " &middot; ".join(f'<a href="{L[k][1]}" rel="noopener" target="_blank">{L[k][0]}</a>' for k in keys)
        line = f'<p class="standards-line" style="font-size:.88rem;color:#64748b;margin-top:14px"><strong>{label}:</strong> {links}.</p>'
        pos = m.end() + last
        t = t[:pos] + line + t[pos:]
        open(f, "w", encoding="utf-8").write(t)
        print("added", f)


if __name__ == "__main__":
    main()
