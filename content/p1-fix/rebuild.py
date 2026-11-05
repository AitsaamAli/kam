#!/usr/bin/env python3
"""P1 fix (5 Nov 2026): replace the shared template body of doorway pages with page-specific content.

Only the article body after the first H2 is replaced; head tags (title, description, canonical, robots) stay
unchanged so URLs and rankings are not disturbed. FAQPage JSON-LD is rebuilt from the new visible FAQs and
dateModified is updated. Lahore area parents become hubs for their block guides (data from content/lahore-areas).
Usage: python3 content/p1-fix/rebuild.py
"""
import collections
import glob
import html
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from topics import DEADLINE, INTRO, T  # noqa: E402

DATE = "2026-11-05"
SERVICE_NAMES = {"wealth": "wealth statements", "ntn": "NTN registration", "salaried": "salaried returns", "notice": "FBR notices",
                 "property": "property tax", "rental": "rental income", "business": "business returns", "sales": "sales tax",
                 "freelancer": "freelancer income", "overseas": "overseas Pakistanis", "company": "company registration", "atl": "ATL status"}


def load_area_data():
    sys.path.insert(0, os.path.join(ROOT, "content", "lahore-areas"))
    spec = importlib.util.spec_from_file_location("clusters", os.path.join(ROOT, "content", "lahore-areas", "data_00_clusters.py"))
    cm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cm)
    pages = []
    for f in sorted(glob.glob(os.path.join(ROOT, "content", "lahore-areas", "data_[0-9][0-9]_*.py"))):
        s = importlib.util.spec_from_file_location("m" + os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(s)
        s.loader.exec_module(m)
        for v in vars(m).values():
            if isinstance(v, list) and v and isinstance(v[0], dict) and "slug" in v[0]:
                pages += v
    return cm.CLUSTERS, pages


def faq_html(faqs, toggle):
    if toggle:
        items = "".join(f'<div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">{html.escape(q)}<i class="fas fa-chevron-down"></i></div>'
                        f'<div class="faq-a"><p>{html.escape(a)}</p></div></div>' for q, a in faqs)
        return f'<h2 id="faqs">Frequently Asked Questions</h2><div class="faq-list">{items}</div>'
    return '<h2 id="faqs">Frequently Asked Questions</h2>' + "".join(f"<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>" for q, a in faqs)


def sources_html(src):
    links = "; ".join(f'<a href="{u}" rel="noopener">{html.escape(n)}</a>' for n, u in src)
    return (f'<p class="sources" style="font-size:.88rem;color:#64748b;margin-top:18px">Sources: {links}. Figures checked on 5 November 2026; '
            'confirm on the official website before acting, as rates and dates can change.</p>')


def topic_content(slug, toggle):
    d = T[slug]
    body = "".join(f'<h2 id="s{i}">{html.escape(h)}</h2>{c}' for i, (h, c) in enumerate(d["sections"], 1))
    return body + faq_html(d["faqs"], toggle) + sources_html(d["sources"]), d["faqs"]


def hub_content(cluster, info, blocks, toggle):
    short = info["short"]
    rows = "".join(f'<tr><td><a href="/blogs/tax-consultant-{b["slug"]}-lahore">{html.escape(b["name"])}</a></td><td>{html.escape(b["desc"])}</td></tr>' for b in blocks)
    svc = collections.Counter()
    for b in blocks:
        try:
            svc.update(eval(b["services"]) if isinstance(b["services"], str) else b["services"])
        except Exception:
            pass
    top = [SERVICE_NAMES.get(k, k) for k, _ in svc.most_common(4)]
    faqs = []
    for b in blocks:
        try:
            fq = eval(b["faq"]) if isinstance(b["faq"], str) else b["faq"]
        except Exception:
            fq = []
        if fq:
            q, a = fq[0]
            faqs.append((q, a))
        if len(faqs) == 4:
            break
    body = (f'<h2 id="area">Tax help in {html.escape(short)}, block by block</h2><p>{html.escape(INTRO.get(cluster, ""))}</p>'
            f'<p>We have written {len(blocks)} guides for specific parts of {html.escape(short)}, each answering the question residents there ask us most.</p>'
            f'<table><tr><th>Area</th><th>What the guide covers</th></tr>{rows}</table>'
            + (f'<h2 id="needs">What {html.escape(short)} residents ask about most</h2><p>Across these guides, the most frequent needs are '
               + ", ".join(top[:-1]) + (" and " + top[-1] if len(top) > 1 else (top[0] if top else "")) + ".</p>" if top else "")
            + f'<h2 id="deadline">Filing status for Tax Year 2026</h2><p>{DEADLINE}</p>'
            + f'<h2 id="visit">Working with us from {html.escape(short)}</h2><p>Our office is at Shop No 34, Rizwan Block Market, Awan Town, Lahore, open Monday to Saturday from 9:00 AM to 6:00 PM and on Friday until 12:30 PM. Most clients in {html.escape(short)} share documents on WhatsApp and never need to visit. For all areas, see our <a href="/tax-consultant-lahore">Lahore area guide</a>.</p>')
    srcs = [("Federal Board of Revenue", "https://www.fbr.gov.pk/"), ("FBR IRIS portal", "https://iris.fbr.gov.pk/")]
    return body + faq_html(faqs, toggle) + sources_html(srcs), faqs


TAG = re.compile(r"<(/?)(div|section|article|ul|ol|table|aside)\b[^>]*>", re.I)


def unmatched_closers(seg):
    stack, out = [], []
    for m in TAG.finditer(seg):
        name = m.group(2).lower()
        if m.group(1):
            if stack and stack[-1] == name:
                stack.pop()
            else:
                out.append(f"</{name}>")
        else:
            stack.append(name)
    return "".join(out)


def replace_body(t, new):
    a = t.find('class="article-body')
    if a < 0:
        a = t.find("<article")
    start = t.find("<h2", a)
    ends = [x for x in (t.find("</article>", start), t.find('<aside class="sidebar', start)) if x > 0] or [t.find("<footer", start)]
    end = min(ends)
    seg = t[start:end]
    return t[:start] + new + unmatched_closers(seg) + t[end:]


def update_ld(t, faqs):
    def fix(o):
        if isinstance(o, dict):
            ty = o.get("@type")
            if ty == "FAQPage":
                o["mainEntity"] = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]
            if "dateModified" in o:
                o["dateModified"] = DATE
            for v in o.values():
                fix(v)
        elif isinstance(o, list):
            for v in o:
                fix(v)
        return o

    def one(m):
        try:
            d = json.loads(m.group(1))
        except Exception:
            return m.group(0)
        return '<script type="application/ld+json">' + json.dumps(fix(d), ensure_ascii=False) + "</script>"
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', one, t, flags=re.S)


def main():
    os.chdir(ROOT)
    clusters, apages = load_area_data()
    parents = {v["parent_href"].strip("/"): k for k, v in clusters.items() if v["parent_href"] != "/tax-consultant-lahore"}
    done = []
    for slug in list(T) + [p for p in parents if p not in T]:
        f = slug + ".html"
        t = open(f, encoding="utf-8").read()
        toggle = "function toggleFAQ" in t
        if slug in T:
            new, faqs = topic_content(slug, toggle)
        else:
            c = parents[slug]
            blocks = [p for p in apages if p["cluster"] == c]
            new, faqs = hub_content(c, clusters[c], blocks, toggle)
        t2 = update_ld(replace_body(t, new), faqs)
        t2 = re.sub(r"<div[^>]*itemscope[^>]*itemtype=\"https://schema.org/FAQPage\"[^>]*>", "<div>", t2)
        open(f, "w", encoding="utf-8").write(t2)
        done.append(slug)
    print("rebuilt", len(done))


if __name__ == "__main__":
    main()
