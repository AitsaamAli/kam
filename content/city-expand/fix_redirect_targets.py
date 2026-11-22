"""Fix after part 2 / Lahore merges (22 Nov 2026): some targets already had older redirects.
1. Flatten every redirect chain in vercel.json to its final destination.
2. Undo kamonke -> kamoke: /blogs/tax-consultant-kamoke already redirected to /income-tax-filing, so kamonke (the live Kamoke page)
   stays live; its links are restored and it gets the part 2 facts.
3. Five Lahore areas live at root URLs (/tax-consultant-<area>-lahore); the FBR value section goes there too.
Idempotent."""
import glob, json, os, re, sys
sys.path.insert(0, "/home/user/kam/content/city-expand")
ROOT = "/home/user/kam/"

vj = json.load(open(ROOT + "vercel.json"))
vj["redirects"] = [r for r in vj["redirects"] if r["source"] != "/blogs/tax-consultant-kamonke"]
dest = {r["source"]: r["destination"] for r in vj["redirects"]}
for r in vj["redirects"]:
    d, seen = r["destination"], set()
    while d in dest and d not in seen:
        seen.add(d)
        d = dest[d]
    r["destination"] = d
json.dump(vj, open(ROOT + "vercel.json", "w"), indent=2)

sm = open(ROOT + "sitemap.xml", encoding="utf-8").read()
if "/blogs/tax-consultant-kamonke</loc>" not in sm:
    sm = sm.replace("</urlset>", "  <url>\n    <loc>https://kambohassociates.com/blogs/tax-consultant-kamonke</loc>\n    <lastmod>2026-11-22</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n</urlset>", 1)
    open(ROOT + "sitemap.xml", "w", encoding="utf-8").write(sm)
for f in glob.glob(ROOT + "**/*.html", recursive=True):
    if "/content/" in f or f.endswith("tax-consultant-kamonke.html"):
        continue
    t = open(f, encoding="utf-8").read()
    if 'href="/blogs/tax-consultant-kamoke"' in t:
        open(f, "w", encoding="utf-8").write(t.replace('href="/blogs/tax-consultant-kamoke"', 'href="/blogs/tax-consultant-kamonke"'))

import part2 as P
P.MERGE = {}
P.T = {"kamonke": ("KAMOKE TEHSIL", "Gujranwala", "Kamoke")}
P.apply("kamonke")

import lahore_fmv as F
for slug in ["johar-town", "model-town", "wapda-town", "gulshan-ravi", "shadman"]:
    p = ROOT + f"tax-consultant-{slug}-lahore.html"
    if not os.path.exists(p):
        continue
    t = open(p, encoding="utf-8").read()
    if 'class="ka-fmv"' in t:
        continue
    k = t.find("</article>")
    t = t[:k] + F.fmv_block(slug) + t[k:]
    t = re.sub(r'<details class="ka-toc".*?</details>\n?', "", t, count=1, flags=re.S)
    open(p, "w", encoding="utf-8").write(t)
print("done")
