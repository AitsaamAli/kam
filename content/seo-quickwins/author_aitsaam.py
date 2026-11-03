#!/usr/bin/env python3
"""Attribute tax articles to Aitsaam Ali (approved by the owner on 4 November 2026).

For every tax-site article (BlogPosting/Article/NewsArticle) whose author is still the organisation:
- schema: the "author" object becomes a Person linked to /authors/aitsaam-ali (publisher stays the organisation)
- visible byline: "Kamboh Associates" next to the user icon in the hero becomes a link to the author page
Skips /digital (team-authored), the blog index and pages that already name a Person.
Usage: python3 content/seo-quickwins/author_aitsaam.py
"""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PERSON = {"@type": "Person", "name": "Aitsaam Ali", "url": "https://kambohassociates.com/authors/aitsaam-ali",
          "@id": "https://kambohassociates.com/authors/aitsaam-ali#person",
          "jobTitle": "Author", "worksFor": {"@id": "https://kambohassociates.com/#organization"}}
LINK = '<a href="/authors/aitsaam-ali" style="color:inherit;text-decoration:underline">Aitsaam Ali</a>'
AUTHOR_ORG = re.compile(r'"author":\s*\{(?:[^{}]|\{[^{}]*\})*"@type":\s*"Organization"(?:[^{}]|\{[^{}]*\})*\}')
BYLINES = [('<i class="fas fa-user-tie"></i> Kamboh Associates</div>', f'<i class="fas fa-user-tie"></i> {LINK}</div>'),
           ('<span><i class="fas fa-user"></i> Kamboh Associates</span>', f'<span><i class="fas fa-user"></i> {LINK}</span>')]


def main():
    os.chdir(ROOT)
    done, no_byline = 0, []
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith(("content/", "digital/")) or f == "blogs.html":
            continue
        t = open(f, encoding="utf-8").read()
        if re.search(r'"@type":\s*"Person"', t) or not re.search(r'"@type":\s*"(BlogPosting|Article|NewsArticle)"', t):
            continue
        n = AUTHOR_ORG.sub('"author": ' + json.dumps(PERSON), t)
        hit = False
        for a, b in BYLINES:
            if a in n:
                n = n.replace(a, b, 1)
                hit = True
                break
        if not hit:
            no_byline.append(f)
        for j in re.findall(r'<script type="application/ld\+json">(.*?)</script>', n, re.S):
            json.loads(j)
        if n != t:
            open(f, "w", encoding="utf-8").write(n)
            done += 1
    print("articles updated:", done, "| without a visible byline to update:", no_byline or "NONE")


if __name__ == "__main__":
    main()
