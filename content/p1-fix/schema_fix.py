#!/usr/bin/env python3
"""Search Console fixes (6 Nov 2026 export).
1. Unparsable structured data, 'Duplicate unique property': pages carried FAQPage twice (microdata and JSON-LD).
   Microdata FAQ attributes are removed where JSON-LD FAQPage exists; the visible FAQ text is unchanged.
2. Review snippets, 'Invalid object type for field <parent_node>': aggregateRating sat on Service/Organization,
   which Google does not support for review snippets. It is removed from those nodes."""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MICRO = re.compile(r'\s(itemscope(?:="[^"]*")?|itemprop="(?:mainEntity|acceptedAnswer|name|text)"|itemtype="https?://schema\.org/(?:FAQPage|Question|Answer)")')


def strip_rating(o):
    if isinstance(o, dict):
        ty = o.get("@type")
        if "aggregateRating" in o and ty in ("Service", "Organization"):
            del o["aggregateRating"]
        for v in o.values():
            strip_rating(v)
    elif isinstance(o, list):
        for v in o:
            strip_rating(v)
    return o


def main():
    os.chdir(ROOT)
    micro = rating = 0
    for f in [x for x in glob.glob("**/*.html", recursive=True) if not x.startswith(("content/", "node_modules/"))]:
        t = open(f, encoding="utf-8").read()
        n = t
        if '"FAQPage"' in n and re.search(r'itemtype="https?://schema\.org/FAQPage"', n) and not re.search(r'itemtype="https?://schema\.org/(?!FAQPage|Question|Answer)', n):
            n = MICRO.sub("", n)
            micro += 1
        if "aggregateRating" in n:
            def one(m):
                d = json.loads(m.group(1))
                return '<script type="application/ld+json">' + json.dumps(strip_rating(d), ensure_ascii=False) + "</script>"
            n2 = re.sub(r'<script type="application/ld\+json">(.*?)</script>', one, n, flags=re.S)
            rating += n2 != n
            n = n2
        if n != t:
            open(f, "w", encoding="utf-8").write(n)
    print("faq microdata removed", micro, "rating removed", rating)


if __name__ == "__main__":
    main()
