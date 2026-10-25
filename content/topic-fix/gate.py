#!/usr/bin/env python3
"""Gate for pages rewritten by fix.py: overlap against every indexed page, length, JSON-LD, tags, links.

Overlap ignores shingles found on more than 400 pages (site-wide navigation and footer chrome), as in
the sitewide scan. Tag balance is compared with the committed version so pre-existing quirks are not
blamed on the rewrite.
Usage: python3 content/topic-fix/gate.py [file ...]   (default: every page in data_*.py)
"""
import collections
import glob
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "content", "lahore-areas"))

from check import text_of as article_text, shingles, existing_paths  # noqa: E402
sys.path.insert(0, HERE)
from fix import load_data  # noqa: E402

LIMIT = 15.0
MIN_WORDS = 480
TAGS = ("div", "table", "ul", "ol", "li", "article", "h2", "p", "section", "details")


def text_of(html):
    """Article text, or for pages without <article> the body minus scripts, styles and site chrome."""
    if re.search(r"<article[^>]*>", html):
        return article_text(html)
    m = re.search(r"<body[\s\S]*</body>", html)
    b = re.sub(r"<(script|style|nav|footer|header)\b[\s\S]*?</\1>", " ", m.group(0) if m else html)
    b = re.sub(r"<[^>]+>", " ", b)
    b = re.sub(r"&[a-z#0-9]+;", " ", b)
    return re.sub(r"\s+", " ", b).strip().lower()


def indexed_pages():
    redirects = {r["source"] for r in json.load(open(os.path.join(ROOT, "vercel.json")))["redirects"]}
    out = []
    for pat in ("*.html", "blogs/*.html", "guides/*.html", "news/*.html"):
        for f in glob.glob(os.path.join(ROOT, pat)):
            rel = os.path.relpath(f, ROOT)
            url = "/" + rel[:-5]
            if url in redirects or url + ".html" in redirects:
                continue
            h = open(f, encoding="utf-8-sig", errors="ignore").read()
            if re.search(r'<meta name="robots"[^>]*noindex', h):
                continue
            out.append((rel, h))
    return out


def balance(html):
    return {t: len(re.findall(rf"<{t}[\s>]", html)) - len(re.findall(rf"</{t}>", html)) for t in TAGS}


def main():
    targets = sys.argv[1:] or sorted(load_data())
    pages = indexed_pages()
    sh = {rel: shingles(text_of(h)) for rel, h in pages}
    count = collections.Counter(x for s in sh.values() for x in s)
    sh = {rel: {x for x in s if count[x] <= 400} for rel, s in sh.items()}
    idx = collections.defaultdict(list)
    for rel, s in sh.items():
        for x in s:
            idx[x].append(rel)
    paths = existing_paths() | {f"/{d}/" + os.path.basename(f)[:-5] for d in ("authors", "guides", "news") for f in glob.glob(os.path.join(ROOT, d, "*.html"))}
    bad = 0
    for rel in targets:
        html = open(os.path.join(ROOT, rel), encoding="utf-8-sig").read()
        issues = []
        words = len(text_of(html).split())
        # local service pages carry one city's facts, not a full topic guide; 300 unique words is the floor there
        floor = 300 if re.match(r"blogs/(tax-consultant|ntn-registration|income-tax-filing)-", rel) else MIN_WORDS
        if words < floor:
            issues.append(f"{words} words")
        a = sh.get(rel, set())
        hits = collections.Counter(g for x in a for g in idx[x] if g != rel)
        worst = (0.0, "")
        for g, c in hits.items():
            pct = max(c / len(a), c / max(1, len(sh[g]))) * 100
            if pct > worst[0]:
                worst = (pct, g)
        if worst[0] >= LIMIT:
            issues.append(f"overlap {worst[0]:.1f}% with {worst[1]}")
        for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            try:
                json.loads(blob)
            except ValueError as e:
                issues.append(f"bad JSON-LD: {e}")
        if html.count('"FAQPage"') > 1:
            issues.append("multiple FAQPage")
        try:
            old = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=ROOT, capture_output=True, text=True).stdout
        except OSError:
            old = ""
        b_new, b_old = balance(html), balance(old) if old else {t: 0 for t in TAGS}
        for t in TAGS:
            if b_new[t] != b_old[t]:
                issues.append(f"<{t}> balance {b_old[t]} -> {b_new[t]}")
        ids = re.findall(r'\sid="([^"]+)"', html)
        dup = {i for i in ids if ids.count(i) > 1}
        if dup:
            issues.append(f"duplicate ids {sorted(dup)[:4]}")
        for href in re.findall(r'href="(/[^"#?]*)', html):
            if not re.search(r"\.(css|js|png|ico|svg|xml|webp|jpg)$", href) and href.rstrip("/") not in paths and href != "/":
                issues.append(f"broken link {href}")
        d = re.search(r'name="description" content="([^"]*)"', html)
        if d and not 110 <= len(d.group(1)) <= 165:
            issues.append(f"desc {len(d.group(1))} chars")
        bad += bool(issues)
        print(f"{'OK ' if not issues else 'FAIL'} {rel:60s} {words:5d}w  {worst[0]:4.1f}% ({worst[1]})", "; ".join(issues))
    print(f"\n{len(targets) - bad}/{len(targets)} clean")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
