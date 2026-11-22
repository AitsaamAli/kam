"""Part 1: merge the 19 duplicate city-page pairs (owner approved, 22 Nov 2026).
Main = the slug that is the full place name (e.g. dera-ghazi-khan over dg-khan, jhelum over jhelum-city). The other URL gets a 301 in vercel.json (file kept, as with earlier redirects), leaves sitemap.xml and the
blogs.html list, and every internal link to it is pointed at the main page so there is no redirect chain. Idempotent."""
import collections, glob, json, re

ROOT = "/home/user/kam/"
ALIAS = {"dg-khan": "dera-ghazi-khan", "fatehjang": "fateh-jang", "dir-lower": "lower-dir"}


def base(s):
    b = s[len("tax-consultant-"):]
    b = re.sub(r"-(city-centre|city|district|area)$", "", b)
    return ALIAS.get(b, b)


def pairs():
    m = collections.defaultdict(list)
    for f in glob.glob(ROOT + "blogs/tax-consultant-*.html"):
        s = f.split("/")[-1][:-5]
        m[base(s)].append(s)
    out = []
    for v in m.values():
        if len(v) == 2:
            # main = the slug that is the place's full name (not an alias like dg-khan, not a -city/-district variant)
            main = next((x for x in v if x[len("tax-consultant-"):] == base(x)), sorted(v, key=lambda x: (len(x), x))[0])
            sec = next(x for x in v if x != main)
            out.append((main, sec))
    return sorted(out)


def main():
    P = pairs()
    vj = json.load(open(ROOT + "vercel.json"))
    have = {r["source"] for r in vj["redirects"]}
    for main_, sec in P:
        src = f"/blogs/{sec}"
        if src not in have:
            vj["redirects"].append({"source": src, "destination": f"/blogs/{main_}", "permanent": True})
    json.dump(vj, open(ROOT + "vercel.json", "w"), indent=2)
    sm = open(ROOT + "sitemap.xml", encoding="utf-8").read()
    for _, sec in P:
        sm = re.sub(r"\s*<url>\s*<loc>https://kambohassociates\.com/blogs/" + re.escape(sec) + r"</loc>.*?</url>", "", sm, flags=re.S)
    open(ROOT + "sitemap.xml", "w", encoding="utf-8").write(sm)
    bl = open(ROOT + "blogs.html", encoding="utf-8").read()
    for _, sec in P:
        bl = re.sub(r'\n  \{\n    id: "' + re.escape(sec) + r'",.*?\n  \},', "", bl, flags=re.S)
        bl = re.sub(r'      <a href="/blogs/' + re.escape(sec) + r'"[^\n]*\n', "", bl)
    open(ROOT + "blogs.html", "w", encoding="utf-8").write(bl)
    rep = {f'href="/blogs/{sec}"': f'href="/blogs/{m}"' for m, sec in P}
    n = 0
    for f in glob.glob(ROOT + "**/*.html", recursive=True):
        if "/content/" in f or "/node_modules/" in f or any(f.endswith(f"/blogs/{s}.html") for _, s in P):
            continue
        t = open(f, encoding="utf-8").read()
        o = t
        for a, b in rep.items():
            t = t.replace(a, b)
        if t != o:
            open(f, "w", encoding="utf-8").write(t)
            n += 1
    print("pairs", len(P), "files relinked", n)
    for m, s in P:
        print(" ", s, "->", m)


if __name__ == "__main__":
    main()
