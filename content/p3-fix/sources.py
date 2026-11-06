#!/usr/bin/env python3
"""P3 fix (6 Nov 2026): add a short, topic-matched 'Official sources' line to tax-site articles that cite no
official website by link. Sources are chosen from the page's URL, title and H1: FBR always, plus IRIS, SECP,
provincial revenue authorities, Excise, IPO or EOBI/PESSI where the topic needs them. Inserted once, before the
FAQ heading (or at the end of the article). Idempotent. Usage: python3 content/p3-fix/sources.py
"""
import glob
import html
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = {
    "fbr": ("Federal Board of Revenue", "https://www.fbr.gov.pk/"),
    "iris": ("FBR IRIS portal", "https://iris.fbr.gov.pk/"),
    "secp": ("SECP", "https://www.secp.gov.pk/"),
    "pra": ("Punjab Revenue Authority", "https://pra.punjab.gov.pk/"),
    "srb": ("Sindh Revenue Board", "https://www.srb.gos.pk/"),
    "kpra": ("Khyber Pakhtunkhwa Revenue Authority", "https://kpra.gov.pk/"),
    "excise": ("Punjab Excise, Taxation and Narcotics Control", "https://excise.punjab.gov.pk/"),
    "ipo": ("IPO-Pakistan", "https://ipo.gov.pk/"),
    "eobi": ("EOBI", "https://www.eobi.gov.pk/"),
    "pessi": ("PESSI", "https://pessi.punjab.gov.pk/"),
}
RULES = [
    (r"professional[- ]tax|token[- ]tax|motor vehicle|vehicle tax|property tax|urban immovable|excise", ["excise"]),
    (r"secp|company|companies|llp|incorporat|annual return|smc|private limited", ["secp"]),
    (r"\bpra\b|punjab sales tax|services tax|restaurant|salon|beauty", ["pra"]),
    (r"\bsrb\b|sindh sales tax|karachi.*(services|restaurant)", ["srb"]),
    (r"kpra|khyber.*sales tax", ["kpra"]),
    (r"trademark|trade mark|logo|brand|copyright|patent", ["ipo"]),
    (r"eobi|old[- ]age", ["eobi"]),
    (r"social security|pessi", ["pessi"]),
    (r"return|filing|file|ntn|registration|atl|active taxpayer|wealth statement|iris|filer|refund|notice|deadline", ["iris"]),
]
MARK = 'class="official-sources"'
OFFICIAL = re.compile(r'href="https?://(?:www\.)?(?:fbr\.gov\.pk|iris\.fbr\.gov\.pk|secp\.gov\.pk|pra\.punjab\.gov\.pk|srb\.gos\.pk|kpra\.gov\.pk|excise\.punjab\.gov\.pk|ipo\.gov\.pk|eobi\.gov\.pk|pessi\.punjab\.gov\.pk|sbp\.org\.pk)')


def pick(text):
    keys = ["fbr"]
    for pat, ks in RULES:
        if re.search(pat, text, re.I):
            for k in ks:
                if k not in keys:
                    keys.append(k)
    return keys[:3]


def line(keys, urdu=False):
    links = " &middot; ".join(f'<a href="{SRC[k][1]}" rel="noopener" target="_blank">{html.escape(SRC[k][0])}</a>' for k in keys)
    if urdu:
        return f'<p {MARK} style="font-size:.88rem;color:#64748b;margin:22px 0 10px">سرکاری ذرائع: {links}۔ فائل کرنے سے پہلے شرحیں اور تاریخیں ان سائٹس پر تصدیق کریں۔</p>'
    return (f'<p {MARK} style="font-size:.88rem;color:#64748b;margin:22px 0 10px"><strong>Official sources:</strong> {links}. '
            "Confirm current rates and dates on these sites before you file or pay.</p>")


def main():
    os.chdir(ROOT)
    added = 0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith(("content/", "node_modules/", "digital/")) or f in ("404.html",):
            continue
        t = open(f, encoding="utf-8").read()
        if MARK in t or OFFICIAL.search(t) or "<article" not in t:
            continue
        a = t.find("<article")
        e = t.find("</article>", a)
        if e < 0:
            continue
        m = re.compile(r"<h2[^>]*>[^<]*(?:Frequently Asked|FAQ|اکثر پوچھے)", re.I).search(t, a, e)
        pos = m.start() if m else e
        title = " ".join([f, (re.search(r"<title>(.*?)</title>", t, re.S) or [None, ""])[1],
                          (re.search(r"<h1[^>]*>(.*?)</h1>", t, re.S) or [None, ""])[1]])
        t = t[:pos] + line(pick(title), urdu=f.startswith("ur/")) + t[pos:]
        open(f, "w", encoding="utf-8").write(t)
        added += 1
    print("sources added", added)


if __name__ == "__main__":
    main()
