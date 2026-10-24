#!/usr/bin/env python3
"""Strips shared filler sections from topic pages and inserts page-specific content.

A section (an <h2> and everything up to the next <h2> inside <article>) counts as filler when at
least half of its 6-word shingles also appear in 3+ other pages. Filler sections are removed;
new sections and FAQs from data_*.py are inserted in their place, the FAQPage JSON-LD is rebuilt
from the visible FAQ, and table-of-contents links to removed sections are dropped.
Usage: python3 content/topic-fix/fix.py --dry [file ...] | python3 content/topic-fix/fix.py [file ...]
"""
import atexit
import glob
import html as H
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "content", "lahore-areas"))
from build import render_body, inline, strip_tags  # noqa: E402
from check import shingles  # noqa: E402

MODIFIED = "2026-10-24"
BASE = "c29e728"  # last commit before the topic-page rewrite
_BASE_DIR = None
STYLE = ("<style id=\"tf-style\">.tf-sec table{width:100%;border-collapse:collapse;margin:16px 0}"
         ".tf-sec th,.tf-sec td{padding:9px 12px;border-bottom:1px solid #E2E8F0;text-align:left;font-size:.9rem}"
         ".tf-sec th{background:#0F172A;color:#fff}.tf-sec .ib{background:rgba(20,184,166,.07);border-left:4px solid #14B8A6;"
         "border-radius:0 10px 10px 0;padding:14px 18px;margin:18px 0}.tf-sec .ib i{display:none}"
         ".tf-faq details{border:1px solid #E2E8F0;border-radius:10px;margin:0 0 10px;padding:12px 16px;background:#F8FAFC}"
         ".tf-faq summary{font-weight:600;cursor:pointer}.tf-faq details p{margin:10px 0 0}"
         "@media(max-width:768px){html,body{overflow-x:hidden}main,article,.layout>*,.article-wrap>*{min-width:0;max-width:100%}"
         ".topbar{overflow:hidden}article ul,article ol{max-width:calc(100% - 20px)}"
         "article p,article li{overflow-wrap:break-word}article table{display:block;overflow-x:auto;max-width:100%}}</style>")


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"&[a-z#0-9]+;", " ", s))).strip().lower()


def split_article(h):
    m = re.search(r"(<article[^>]*>)([\s\S]*?)(</article>)", h)
    if not m:
        return None
    parts = re.split(r"(?=<h2[\s>])", m.group(2))
    # a wrapper opened right before an h2 (<section class="extra-content"><h2>) belongs to that h2's part
    for i in range(len(parts) - 1):
        w = re.search(r"<section\b[^>]*>\s*$", parts[i])
        if w:
            parts[i + 1] = parts[i][w.start():] + parts[i + 1]
            parts[i] = parts[i][: w.start()]
    return m, parts


def heading(part):
    hm = re.match(r"\s*(?:<section\b[^>]*>\s*)?<h2[^>]*>([\s\S]*?)</h2>", part)
    return norm(hm.group(1)) if hm else "__intro__"


def build_freq(exclude=()):
    freq = Counter()
    base = base_tree()
    for f in glob.glob(os.path.join(base, "*.html")) + glob.glob(os.path.join(base, "blogs", "*.html")):
        if os.path.relpath(f, base) in exclude:
            continue
        r = split_article(open(f, encoding="utf-8-sig", errors="ignore").read())
        if not r:
            continue
        s = set()
        for p in r[1]:
            s |= shingles(norm(p))
        freq.update(s)
    return freq


def is_filler(part, freq):
    s = shingles(norm(part))
    if not s:
        return False
    # the page itself contributes 1 to each count, so >=4 means 3+ other pages
    return sum(1 for x in s if freq[x] >= 4) / len(s) >= 0.5


def salvage_faq(part, freq):
    pairs = []
    for q, a in re.findall(r'class="(?:faq-q|fq-q)"[^>]*>([\s\S]*?)</div>\s*<div[^>]*class="(?:faq-a|fq-a)"[^>]*>([\s\S]*?)</div>', part):
        q, a = strip_tags(q).strip(), strip_tags(a).strip()
        if q and a and not is_filler(q + " " + a, freq):
            pairs.append((H.unescape(q), H.unescape(a)))
    return pairs


def extract_cta(part):
    """Returns the first complete cta-box/article-cta div in a part, matched by div depth."""
    m = re.search(r'<div class="(?:cta-box|article-cta)[^"]*"', part)
    if not m:
        return ""
    depth = 0
    for t in re.finditer(r"<(/?)div\b[^>]*>", part[m.start():]):
        depth += -1 if t.group(1) else 1
        if depth == 0:
            return part[m.start(): m.start() + t.end()]
    return ""


def excess_closers(part):
    """Closing tags a section carries for containers opened before it (e.g. the .article div)."""
    out = ""
    for tag in ("div", "section"):
        n = len(re.findall(rf"</{tag}>", part)) - len(re.findall(rf"<{tag}\b", part))
        out += f"</{tag}>" * max(0, n)
    return out


def base_tree():
    """Checkout of the pages as they were before this rewrite (BASE), so the filler test and the
    source of each page do not change as pages get fixed and re-runs stay idempotent."""
    global _BASE_DIR
    if _BASE_DIR is None:
        _BASE_DIR = tempfile.mkdtemp(prefix="topic-fix-base-")
        atexit.register(shutil.rmtree, _BASE_DIR, True)
        arc = subprocess.run(["git", "archive", BASE, "--", "*.html"], cwd=ROOT, capture_output=True, check=True).stdout
        subprocess.run(["tar", "-x", "-C", _BASE_DIR], input=arc, check=True)
    return _BASE_DIR


def source_html(rel):
    return open(os.path.join(base_tree(), rel), encoding="utf-8-sig").read()


def load_data():
    data = {}
    for p in sorted(glob.glob(os.path.join(HERE, "data_*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(p)[:-3], p)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for rel, page in mod.PAGES.items():
            cur = data.setdefault(rel, {})
            for k, v in page.items():
                cur[k] = cur.get(k, []) + v if isinstance(v, list) and k in cur else v
    return data


def rebuild_jsonld(h, faq):
    def fix(obj):
        if isinstance(obj, list):
            return [fix(o) for o in obj if not (isinstance(o, dict) and o.get("@type") == "FAQPage")]
        if isinstance(obj, dict):
            if obj.get("@type") in ("BlogPosting", "Article", "NewsArticle"):
                obj["dateModified"] = MODIFIED
            if "@graph" in obj:
                obj["@graph"] = fix(obj["@graph"])
        return obj

    def repl(m):
        try:
            obj = json.loads(m.group(2))
        except ValueError:
            return m.group(0)
        if isinstance(obj, dict) and obj.get("@type") == "FAQPage":
            return ""
        return m.group(1) + json.dumps(fix(obj), ensure_ascii=False) + m.group(3)

    h = re.sub(r'(<script type="application/ld\+json">)([\s\S]*?)(</script>)', repl, h)
    if not faq:
        return h
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(inline(a))}} for q, a in faq]}
    return h.replace("</head>", f'<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>\n</head>', 1)


def fix_page(rel, page, freq, dry):
    path = os.path.join(ROOT, rel)
    h = source_html(rel)
    r = split_article(h)
    if not r:
        return None
    m, parts = r
    kept, removed, salvaged, drop_parts = [], [], [], []
    for p in parts:
        hd = heading(p)
        faq_sec = "frequently asked" in hd or hd.startswith("faq")
        if hd == "__intro__":
            kept.append(p)
        elif faq_sec:
            salvaged += salvage_faq(p, freq)
            removed.append(hd)
            drop_parts.append(p)
        elif hd in page.get("keep", []) or not is_filler(p, freq):
            if hd in page.get("drop", []):
                removed.append(hd)
                drop_parts.append(p)
            else:
                kept.append(p)
        else:
            removed.append(hd)
            drop_parts.append(p)
    if dry:
        return kept, removed, salvaged
    body_html, _ = render_body(page["body"])
    salvaged = [x for x in salvaged if x[0] not in page.get("faq_skip", [])]
    for old_s, new_s in page.get("replace", []):
        salvaged = [(q, a.replace(H.unescape(old_s), H.unescape(new_s))) for q, a in salvaged]
    faq = page["faq"] + [x for x in salvaged if x[0] not in {q for q, _ in page["faq"]}][: max(0, 6 - len(page["faq"]))]
    faq_html = "".join(f"<details><summary>{H.escape(q)}</summary><p>{inline(a)}</p></details>" for q, a in faq)
    new = f'<div class="tf-sec">\n{body_html}\n</div>\n' if page["body"].strip() else ""
    if faq:
        new += f'<h2 id="faqs">{H.escape(page.get("faq_heading", "Frequently Asked Questions"))}</h2>\n<div class="tf-faq">{faq_html}</div>\n'
    # page-specific sections go after the kept content, before any closing CTA div
    article = "".join(kept)
    tail = "".join(excess_closers(p) for p in drop_parts)
    cta = re.search(r'<div class="(?:cta-box|article-cta)', article)
    if cta:
        article = article[: cta.start()] + new + article[cta.start():]
    else:
        saved = next((c for c in map(extract_cta, drop_parts) if c), "")
        # kept content may end with closers of the .article wrapper; new content goes inside it
        n = len(re.findall(r"</div>", article)) - len(re.findall(r"<div\b", article))
        m_end = re.search(r"((?:\s*</div>){%d}\s*)$" % n, article) if n > 0 else None
        if m_end:
            article = article[: m_end.start()] + new + saved + article[m_end.start():]
        else:
            article = article + new + saved
    article += tail
    for old, new_text in page.get("replace", []):
        if old in article:
            article = article.replace(old, new_text)
        elif old not in h:
            raise SystemExit(f"{rel}: replace target not found: {old[:60]}")
    if page.get("lead"):
        article = re.sub(r'(<p class="lead">)[\s\S]*?(</p>)', lambda x: x.group(1) + inline(page["lead"]) + x.group(2), article, count=1)
    h = h[: m.start(2)] + article + h[m.end(2):]
    # the same wrong figure is often repeated in meta tags and JSON-LD outside <article>
    for old, new_text in page.get("replace", []):
        h = h.replace(old, new_text)
    if page.get("desc"):
        d = H.escape(page["desc"], quote=True)
        h = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda x: x.group(1) + d + x.group(2), h, count=1)
        h = re.sub(r'(<meta property="og:description" content=")[^"]*(")', lambda x: x.group(1) + d + x.group(2), h, count=1)
    ids = set(re.findall(r'id="([^"]+)"', h))
    h = re.sub(r'<a href="#([^"]+)"[^>]*>[\s\S]*?</a>', lambda x: x.group(0) if x.group(1) in ids else "", h)
    h = rebuild_jsonld(h, faq)
    h = re.sub(r'<style id="tf-style">[\s\S]*?</style>\n?', "", h)
    h = h.replace("</head>", STYLE + "\n</head>", 1)
    # regex fixes run last so they also reach salvaged FAQs and the rebuilt FAQPage JSON-LD
    for pat, repl in page.get("regex", []):
        h = re.sub(pat, repl, h)
    open(path, "w", encoding="utf-8").write(h)
    return kept, removed, salvaged


def main():
    dry = "--dry" in sys.argv
    files = [a for a in sys.argv[1:] if not a.startswith("--")]
    data = load_data()
    targets = files or sorted(data)
    freq = build_freq()
    for rel in targets:
        page = data.get(rel, {"body": "", "faq": []})
        if not dry and rel not in data:
            print("no data for", rel)
            continue
        res = fix_page(rel, page, freq, dry)
        if res is None:
            print(f"== {rel}\n   NO-ARTICLE")
            continue
        kept, removed, salv = res
        if dry:
            print(f"== {rel}")
            for p in kept:
                print(f"   KEEP {heading(p)[:70]} ({len(strip_tags(p).split())}w)")
            for r in removed:
                print(f"   DROP {r[:70]}")
            for q, a in salv:
                print(f"   FAQ? {q[:90]}")
        else:
            print("fixed", rel, "dropped", len(removed))


if __name__ == "__main__":
    main()
