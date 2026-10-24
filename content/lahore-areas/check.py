#!/usr/bin/env python3
"""Pre-commit gate for the Lahore area pages: uniqueness, length, JSON-LD, tag balance, links.

Uniqueness uses the project's standard 6-word-shingle overlap (project-history/08), checked
against every page in the tax-consultant-*-lahore family plus the root area pages.
Usage: python3 content/lahore-areas/check.py [slug ...]   (default: every page in data_*.py)
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import ROOT, load_pages  # noqa: E402

LIMIT = 15.0
MIN_WORDS = 550


def text_of(html):
    m = re.search(r"<article[^>]*>([\s\S]*?)</article>", html)
    src = m.group(1) if m else html
    src = re.sub(r"<script[\s\S]*?</script>", " ", src)
    src = re.sub(r"<[^>]+>", " ", src)
    src = re.sub(r"&[a-z#0-9]+;", " ", src)
    return re.sub(r"\s+", " ", src).strip().lower()


def shingles(text, n=6):
    w = text.split(" ")
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def existing_paths():
    paths = {"/", "/blogs"}
    for f in glob.glob(os.path.join(ROOT, "*.html")):
        paths.add("/" + os.path.basename(f)[:-5])
    for f in glob.glob(os.path.join(ROOT, "blogs", "*.html")):
        paths.add("/blogs/" + os.path.basename(f)[:-5])
    for f in glob.glob(os.path.join(ROOT, "*", "index.html")):
        paths.add("/" + os.path.basename(os.path.dirname(f)))
    for f in glob.glob(os.path.join(ROOT, "tools", "*.html")):
        paths.add("/tools/" + os.path.basename(f)[:-5])
    return paths


def main():
    pages, _ = load_pages()
    only = set(sys.argv[1:]) or {p["slug"] for p in pages}
    family = glob.glob(os.path.join(ROOT, "blogs", "tax-consultant-*-lahore.html")) + glob.glob(
        os.path.join(ROOT, "tax-consultant-*lahore*.html"))
    sh = {f: shingles(text_of(open(f, encoding="utf-8-sig").read())) for f in family}
    paths = existing_paths()
    bad = 0
    titles, descs = {}, {}
    for p in pages:
        titles.setdefault(p["title"], []).append(p["slug"])
        descs.setdefault(p["desc"], []).append(p["slug"])
    for s, v in list(titles.items()) + list(descs.items()):
        if len(v) > 1:
            print("DUPLICATE title/desc:", v)
            bad += 1
    for slug in sorted(only):
        f = os.path.join(ROOT, "blogs", f"tax-consultant-{slug}-lahore.html")
        html = open(f, encoding="utf-8").read()
        issues = []
        words = len(text_of(html).split())
        if words < MIN_WORDS:
            issues.append(f"{words} words")
        a = sh[f]
        worst = (0, "")
        for g, b in sh.items():
            if g == f or not a or not b:
                continue
            pct = max(len(a & b) / len(a), len(a & b) / len(b)) * 100
            if pct > worst[0]:
                worst = (pct, os.path.basename(g))
        if worst[0] >= LIMIT:
            issues.append(f"overlap {worst[0]:.1f}% with {worst[1]}")
        for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            try:
                json.loads(blob)
            except ValueError as e:
                issues.append(f"bad JSON-LD: {e}")
        for tag in ("div", "table", "ul", "ol", "li", "article", "h2", "p", "aside", "section"):
            o = len(re.findall(rf"<{tag}[\s>]", html))
            c = len(re.findall(rf"</{tag}>", html))
            if o != c:
                issues.append(f"<{tag}> {o}/{c}")
        for href in re.findall(r'href="(/[^"#?]*)', html):
            if not re.search(r"\.(css|js|png|ico|svg|xml)$", href) and href.rstrip("/") not in paths and href != "/":
                issues.append(f"broken link {href}")
        t = re.search(r"<title>(.*?)</title>", html).group(1)
        d = re.search(r'name="description" content="([^"]*)"', html).group(1)
        if len(t) > 70 or len(d) > 165 or len(d) < 110:
            issues.append(f"title {len(t)} / desc {len(d)} chars")
        status = "OK " if not issues else "FAIL"
        bad += bool(issues)
        print(f"{status} {slug:40s} {words:5d}w  max-overlap {worst[0]:4.1f}% ({worst[1]})", "; ".join(issues))
    print(f"\n{len(only) - bad if bad <= len(only) else 0}/{len(only)} clean")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
