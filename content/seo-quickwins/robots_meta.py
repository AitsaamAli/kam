#!/usr/bin/env python3
"""Give every indexable page the same robots meta, allowing large image previews (Google Discover and Images).

- Rewrites the existing "index, follow" variants to ROBOTS.
- Adds ROBOTS after the canonical link on indexable pages that have no robots meta.
- Leaves noindex pages alone, and marks the unlinked news template page noindex.
- Skips /digital (its builder, content/digital/shell.py, applies the same tag) and content/ templates.
Usage: python3 content/seo-quickwins/robots_meta.py
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROBOTS = '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>'
VARIANT = re.compile(r'<meta name="robots" content="index,\s?follow(?:,\s?max-snippet:-1,\s?max-image-preview:large)?"\s*/?>')
NOINDEX = '<meta name="robots" content="noindex, follow"/>'


def main():
    os.chdir(ROOT)
    changed = added = 0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith(("content/", "digital/", "node_modules/")):
            continue
        t = open(f, encoding="utf-8").read()
        n = t
        if f == "news/_TEMPLATE.html":
            n = VARIANT.sub(NOINDEX, n)
        elif re.search(r'<meta name="robots"[^>]*noindex', n):
            continue
        elif VARIANT.search(n):
            n = VARIANT.sub(ROBOTS, n)
        elif 'name="robots"' not in n:
            m = re.search(r'<link rel="canonical"[^>]*>', n)
            if not m:
                continue
            n = n[:m.end()] + "\n" + ROBOTS + n[m.end():]
            added += 1
        if n != t:
            open(f, "w", encoding="utf-8").write(n)
            changed += 1
    print(f"files changed: {changed} (robots meta added to {added})")
    left = [f for f in glob.glob("**/*.html", recursive=True) if not f.startswith(("content/", "digital/"))
            and "noindex" not in open(f, encoding="utf-8").read() and "max-image-preview:large" not in open(f, encoding="utf-8").read()]
    print("indexable pages still without max-image-preview:", left or "NONE")


if __name__ == "__main__":
    main()
