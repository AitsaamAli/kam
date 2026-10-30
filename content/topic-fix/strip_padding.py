#!/usr/bin/env python3
"""Removes the generic padding section (grey box, blue left border) from service pages without an <article>.

The box repeats the same 300-800 words across pages and carries wrong facts (ACCA claim, a Johar Town office,
old fees and rates). Its two FAQ answers are also dropped from the page's FAQPage JSON-LD.
Usage: python3 content/topic-fix/strip_padding.py file ...
"""
import json
import re
import sys

STY = '<section style="margin:2rem 0;padding:1.5rem;background:#f8f9fa;border-radius:8px;border-left:4px solid #1a73e8">'
# other boxes repeated word for word across service pages; the "About" box stays on about.html only
BOXES = [
    ('<section style="margin:2rem 0;padding:1.5rem;background:#fff8e1;border-radius:8px;border-left:4px solid #f9a825">',
     "<h2>Pakistan Tax Calendar 2026-27", None),
    ('<section style="margin:2rem 0;padding:1.5rem;background:#e8f4f8;border-radius:8px;border:1px solid #b8d4f0">',
     "<h2>About Kamboh Associates — Pakistan Tax Experts Since 2008", "about.html"),
]
BOX_QUESTIONS = {"What is the process to hire Kamboh Associates for tax filing?",
                 "Does Kamboh Associates serve clients outside Lahore?"}


def strip_faq(obj):
    if isinstance(obj, list):
        return [strip_faq(o) for o in obj]
    if isinstance(obj, dict):
        if obj.get("@type") == "FAQPage":
            obj["mainEntity"] = [q for q in obj.get("mainEntity", []) if q.get("name") not in BOX_QUESTIONS]
        if "@graph" in obj:
            obj["@graph"] = strip_faq(obj["@graph"])
    return obj


def main():
    for f in sys.argv[1:]:
        h = open(f, encoding="utf-8-sig").read()
        n = len(re.findall(re.escape(STY), h))
        h = re.sub(r"\s*" + re.escape(STY) + r"[\s\S]*?</section>", "", h)
        for sty, head, keep_on in BOXES:
            if f != keep_on:
                n += len(re.findall(re.escape(sty) + r"\s*" + re.escape(head), h))
                h = re.sub(r"\s*" + re.escape(sty) + r"\s*" + re.escape(head) + r"[\s\S]*?</section>", "", h)

        def repl(m):
            if not any(q in m.group(2) for q in BOX_QUESTIONS):
                return m.group(0)
            return m.group(1) + json.dumps(strip_faq(json.loads(m.group(2))), ensure_ascii=False) + m.group(3)

        h = re.sub(r'(<script type="application/ld\+json">)([\s\S]*?)(</script>)', repl, h)
        open(f, "w", encoding="utf-8").write(h)
        print(f, "removed", n)


if __name__ == "__main__":
    main()
