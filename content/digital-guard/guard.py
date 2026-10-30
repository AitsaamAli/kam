#!/usr/bin/env python3
"""Isolation guard for the /digital (web development) section.

Run before every commit that touches web-development work:
    python3 content/digital-guard/guard.py            # compare against origin/main
    python3 content/digital-guard/guard.py --base X   # compare against another ref

The tax site must stay exactly as it is. The guard fails if web-development work
changes any tax page, adds links between the two sections, targets tax keywords,
or leaves the /digital pages in a state that could send Google mixed signals.

Checks
  G1  Tax freeze      - no file outside the digital allowlist changed (tax HTML, shared CSS/JS,
                        vercel.json, llms files, main sitemap content)
  G2  Main sitemap    - sitemap.xml lists exactly the same non-digital URLs as the base
  G3  Tax -> digital  - no tax page links to /digital beyond the frozen baseline
  G4  Digital -> tax  - /digital pages link only to /digital, external sites, assets and legal pages
  G5  Keyword fence   - /digital titles and H1s do not target tax keywords
  G6  Unique meta     - /digital titles and descriptions are unique across the whole site
  G7  Schema          - valid JSON-LD; provider is the digital entity; FAQPage matches visible FAQ
  G8  Overlap         - /digital body text overlaps < 15% with any other page (6-word shingles)
  G9  Indexing        - self canonical, no noindex, listed in sitemap-digital.xml and not in sitemap.xml
  G10 Shell           - no tax promo bar, tax navigation or tax footer on /digital pages
  G11 Links           - every /digital link points to an existing /digital page
"""
import argparse
import glob
import html as H
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://kambohassociates.com"
DIGITAL_ORG = SITE + "/digital#organization"

# Files web-development work may change. Everything else belongs to the tax site.
ALLOW = [
    re.compile(r"^digital/"),
    re.compile(r"^content/digital[^/]*/"),
    re.compile(r"^sitemap-digital\.xml$"),
    re.compile(r"^sitemap\.xml$"),   # only to move /digital URLs out; G2 checks the rest is identical
    re.compile(r"^robots\.txt$"),    # only to add the sitemap-digital line; checked below
]
LEGAL = {"/privacy", "/terms", "/disclaimer"}
ASSET = re.compile(r"^/(images/|android-chrome|favicon|apple-touch|site\.webmanifest|mobile-fixes\.css)")
TAX_TERMS = re.compile(
    r"\b(tax|ntn|strn|fbr|filer|atl|secp|wealth statement|withholding|sales tax|income tax|"
    r"return filing|iris|gst)\b", re.I)
TAX_SHELL = re.compile(r"File Your Taxes|Tax &amp; Regulatory Excellence|/income-tax-filing\"|/ntn-registration\"")

fails = []


def fail(check, msg):
    fails.append((check, msg))


def sh(*args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True).stdout


def read(p):
    return open(os.path.join(ROOT, p), encoding="utf-8", errors="replace").read()


def text_of(h):
    b = re.search(r"<main[\s\S]*</main>", h) or re.search(r"<body[\s\S]*</body>", h)
    b = b.group(0) if b else h
    b = re.sub(r"<(script|style|nav|footer|header|aside)\b[\s\S]*?</\1>", " ", b)
    b = re.sub(r'<div class="topbar">[\s\S]*?</div>\s*</div>\s*</div>', " ", b)
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", b))).strip().lower()


def shingles(t, n=6):
    w = re.findall(r"[a-z0-9]+", t)
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


def links(h):
    return re.findall(r'href="(?:https?://(?:www\.)?kambohassociates\.com)?(/[^"#?]*)', h)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="origin/main")
    a = ap.parse_args()
    base = a.base

    # ---- G1 tax freeze -------------------------------------------------------------
    changed = set(sh("git", "diff", "--name-only", base).split()) | set(
        sh("git", "ls-files", "--others", "--exclude-standard").split())
    for f in sorted(changed):
        if not any(r.search(f) for r in ALLOW):
            fail("G1", "file outside the web-development area changed: " + f)
    if "robots.txt" in changed:
        old = sh("git", "show", base + ":robots.txt").splitlines()
        new = read("robots.txt").splitlines()
        added = [l for l in new if l not in old]
        removed = [l for l in old if l not in new]
        if removed or any(l.strip() and l.strip() != "Sitemap: %s/sitemap-digital.xml" % SITE for l in added):
            fail("G1", "robots.txt may only gain the sitemap-digital line")

    # ---- G2 main sitemap identical for tax URLs ----------------------------------------
    loc = re.compile(r"<loc>([^<]+)</loc>")
    old_tax = {u for u in loc.findall(sh("git", "show", base + ":sitemap.xml")) if "/digital" not in u.split(".com", 1)[-1][:8]}
    new_all = loc.findall(read("sitemap.xml"))
    new_tax = {u for u in new_all if "/digital" not in u.split(".com", 1)[-1][:8]}
    if old_tax != new_tax:
        fail("G2", "sitemap.xml tax URLs differ from base (+%d / -%d)" % (len(new_tax - old_tax), len(old_tax - new_tax)))

    # ---- collect pages ----------------------------------------------------------------
    digital = sorted(glob.glob(os.path.join(ROOT, "digital", "**", "*.html"), recursive=True))
    digital = [os.path.relpath(p, ROOT) for p in digital]
    skip = ("content/", "project-history/", "reports/", "seo_output/", "outreach/", "searchops-team/",
            "content-batches/", "gsc_", "node_modules/", "schema/", "digital/")
    tax = [p for p in (os.path.relpath(x, ROOT) for x in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True))
           if not p.startswith(skip)]

    # ---- G3 tax -> digital links (frozen baseline) -------------------------------------
    baseline = set(json.load(open(os.path.join(HERE, "baseline.json")))["tax_pages_linking_to_digital"])
    for p in tax:
        if any(u == "/digital" or u.startswith("/digital/") for u in links(read(p))) and p not in baseline:
            fail("G3", "tax page links to /digital (not in frozen baseline): " + p)

    # ---- per digital page checks --------------------------------------------------------
    sm_digital = set(loc.findall(read("sitemap-digital.xml"))) if os.path.exists(os.path.join(ROOT, "sitemap-digital.xml")) else set()
    titles, descs = {}, {}
    for p in tax:
        h = read(p)
        t = re.search(r"<title>([^<]*)</title>", h)
        d = re.search(r'<meta name="description" content="([^"]*)"', h)
        if t: titles.setdefault(H.unescape(t.group(1)).strip().lower(), p)
        if d: descs.setdefault(H.unescape(d.group(1)).strip().lower(), p)

    texts = {}
    for p in digital:
        h = read(p)
        url = SITE + "/" + (p[:-len("/index.html")] if p.endswith("/index.html") else p[:-5])
        # G4
        for u in links(h):
            if u.startswith("/digital"):
                t = u.rstrip("/").lstrip("/")
                if not (os.path.exists(os.path.join(ROOT, t + ".html")) or os.path.exists(os.path.join(ROOT, t, "index.html"))):
                    fail("G11", "%s has a broken internal link: %s" % (p, u))
                continue
            if u in LEGAL or ASSET.search(u):
                continue
            fail("G4", "%s links into the tax site: %s" % (p, u))
        # G5
        t = re.search(r"<title>([^<]*)</title>", h)
        t = H.unescape(t.group(1)).strip() if t else ""
        h1 = re.search(r"<h1[^>]*>([\s\S]*?)</h1>", h)
        h1 = H.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip() if h1 else ""
        for label, val in (("title", t), ("H1", h1)):
            if TAX_TERMS.search(val):
                fail("G5", "%s %s targets a tax term: %r" % (p, label, val))
        if not t or len(t) > 60:
            fail("G6", "%s title missing or over 60 characters (%d)" % (p, len(t)))
        # G6
        d = re.search(r'<meta name="description" content="([^"]*)"', h)
        d = H.unescape(d.group(1)).strip() if d else ""
        if not 110 <= len(d) <= 165:
            fail("G6", "%s description length %d (110-165)" % (p, len(d)))
        for key, store, label in ((t.lower(), titles, "title"), (d.lower(), descs, "description")):
            if key in store and store[key] != p:
                fail("G6", "%s %s duplicates %s" % (p, label, store[key]))
            store.setdefault(key, p)
        if len(re.findall(r"<h1[\s>]", h)) != 1:
            fail("G6", p + " must have exactly one H1")
        # G7
        visible = text_of(h)
        for m in re.finditer(r'<script type="application/ld\+json">([\s\S]*?)</script>', h):
            try:
                data = json.loads(m.group(1))
            except ValueError as e:
                fail("G7", "%s invalid JSON-LD: %s" % (p, e))
                continue
            for o in (data if isinstance(data, list) else [data]):
                if not isinstance(o, dict):
                    continue
                if o.get("@type") == "LocalBusiness":
                    fail("G7", p + " uses LocalBusiness (address belongs to the tax entity)")
                prov = o.get("provider")
                if prov is not None and (not isinstance(prov, dict) or prov.get("@id") != DIGITAL_ORG):
                    fail("G7", p + " provider must be " + DIGITAL_ORG)
                if o.get("@type") == "FAQPage":
                    for q in o.get("mainEntity", []):
                        qn = re.sub(r"\s+", " ", q.get("name", "")).strip().lower()
                        if qn and qn not in visible:
                            fail("G7", "%s FAQ schema question not visible: %s" % (p, q.get("name")))
        # G9
        can = re.search(r'<link rel="canonical" href="([^"]+)"', h)
        if not can or can.group(1) != url:
            fail("G9", "%s canonical should be %s" % (p, url))
        if re.search(r'<meta name="robots" content="[^"]*noindex', h):
            fail("G9", p + " is noindex")
        if url not in sm_digital:
            fail("G9", p + " missing from sitemap-digital.xml")
        if url in new_all:
            fail("G9", p + " still listed in the main sitemap.xml")
        # G10
        if TAX_SHELL.search(h):
            fail("G10", p + " still carries tax promo / navigation / footer")
        texts[p] = shingles(text_of(h))

    # ---- G8 overlap -------------------------------------------------------------------
    pool = {}
    for p in tax:
        pool[p] = shingles(text_of(read(p)))
    pool.update(texts)
    df = {}
    for s in pool.values():
        for x in s:
            df[x] = df.get(x, 0) + 1
    common = {x for x, n in df.items() if n > 400}
    for p, s in texts.items():
        s = s - common
        if not s:
            continue
        for q, o in pool.items():
            if q == p:
                continue
            ov = len(s & o) / len(s)
            if ov >= 0.15:
                fail("G8", "%s overlaps %.1f%% with %s" % (p, ov * 100, q))

    if fails:
        for c, m in fails:
            print("FAIL %-4s %s" % (c, m))
        print("\n%d problem(s). Tax site protection: NOT clear to push." % len(fails))
        sys.exit(1)
    print("OK  %d /digital pages checked, %d tax pages untouched. Clear to push." % (len(digital), len(tax)))


if __name__ == "__main__":
    main()
