#!/usr/bin/env python3
"""Describe Aitsaam Ali only as the author of the pages (owner's instruction, 4 November 2026).

He must not be presented as a tax consultant, specialist, filer or credential holder. Everywhere on the site:
- JSON-LD Person "Aitsaam Ali": jobTitle "Author"; hasCredential, identifier, address and the consultant
  description are removed
- visible bylines: the role text after his name becomes "Author", with a note that figures come from FBR's website
- the author page and the llms builder are rewritten in the same spirit
The firm (Kamboh Associates) is still described as it was; only the person changes.
Usage: python3 content/seo-quickwins/author_role.py
"""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NAME = "Aitsaam Ali"
DESC = ("Aitsaam Ali writes and maintains the guides on this website for Kamboh Associates. "
        "Tax rates, deadlines and rules in these guides are taken from the Federal Board of Revenue's official website and publications.")
DROP = ("hasCredential", "identifier", "address", "award", "alumniOf", "memberOf", "honorificSuffix")
ROLE = re.compile(r"consult|specialist|filer|registered|practition|expert|advocate|licen", re.I)
NOTE = "Author &middot; Figures from FBR&rsquo;s official website"


def fix_person(o):
    if isinstance(o, dict):
        if o.get("@type") == "Person" and o.get("name") == NAME:
            o["jobTitle"] = "Author"
            for k in DROP:
                o.pop(k, None)
            if "description" in o:
                o["description"] = DESC
        for v in o.values():
            fix_person(v)
    elif isinstance(o, list):
        for v in o:
            fix_person(v)


def fix_ld(t):
    def one(m):
        raw = m.group(1)
        if NAME not in raw:
            return m.group(0)
        d = json.loads(raw)
        fix_person(d)
        return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>"
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', one, t, flags=re.S)


BYLINE = re.compile(r"(Aitsaam Ali(?:</a>|</strong>))((?:[^<]|<strong[^>]*>|</strong>)*?)(?=</span>|</div>|<i )")


def fix_byline(m):
    name, rest = m.group(1), m.group(2)
    if not ROLE.search(rest):
        return m.group(0)
    keep = ""
    fc = re.search(r"(Facts checked [^<]*)", rest)
    if fc:
        keep = " &middot; " + fc.group(1).strip()
    if re.search(r"&middot;\s*$", rest.strip()) or rest.strip().endswith("&middot;"):
        return name + " &middot; Author &middot; "
    return name + ", " + NOTE + keep


def fix_visible(t):
    t = BYLINE.sub(fix_byline, t)
    t = t.replace(f"{NAME} — Tax Consultant</span>", f"{NAME} — Author</span>")
    return t


def author_page(t):
    t = re.sub(r"<title>[^<]*</title>", "<title>Aitsaam Ali — Author | Kamboh Associates</title>", t, count=1)
    t = t.replace("Aitsaam Ali — Tax Consultant | NTN • SECP • Sales Tax Specialist", "Aitsaam Ali — Author, Kamboh Associates")
    t = t.replace("Tax Consultant | NTN &bull; SECP &bull; Sales Tax Specialist", "Author, Kamboh Associates")
    t = re.sub(r"(<p[^>]*>)Aitsaam Ali is a Lahore-based tax consultant[^<]*", lambda m: m.group(1) + DESC + " Each guide shows when it was last checked.", t)
    t = re.sub(r'<meta name="description" content="[^"]*"', '<meta name="description" content="' + DESC.replace('"', "&quot;") + '"', t, count=1)
    t = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + DESC, t, count=1)
    t = t.replace("CONSULT AITSAAM ALI", "CONTACT KAMBOH ASSOCIATES")
    t = t.replace("Free 30-minute consultation via WhatsApp. Income tax, NTN, SECP, sales tax — all Pakistan.",
                  "Questions about a guide or our services? Message Kamboh Associates on WhatsApp.")
    return t


def main():
    os.chdir(ROOT)
    changed = 0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith(("content/", "node_modules/")):
            continue
        t = open(f, encoding="utf-8").read()
        if NAME not in t:
            continue
        n = fix_ld(t)
        n = fix_visible(n)
        if f == "authors/aitsaam-ali.html":
            n = author_page(n)
        if n != t:
            open(f, "w", encoding="utf-8").write(n)
            changed += 1
    print("files changed:", changed)
    # leftovers: his name within 80 characters of a role word, in visible text or schema
    left = []
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith(("content/", "node_modules/")):
            continue
        t = open(f, encoding="utf-8").read()
        for m in re.finditer(r"Aitsaam Ali.{0,80}", t):
            seg = re.sub(r"https?://\S+", "", m.group(0))
            if ROLE.search(seg):
                left.append((f, seg[:120]))
    print("leftovers:", len(left))
    for x in left[:40]:
        print("  ", x)


if __name__ == "__main__":
    main()
