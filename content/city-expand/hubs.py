"""Hub links for city pages (owner request, 22 Nov 2026). Idempotent.
Each tax-consultant-* page links up to its city hub (neighbourhoods) or its province guide / division city (towns), and each hub lists
the pages under it that it does not already link to. Redirected pages and noindex pages are skipped."""
import collections, glob, html, json, re

ROOT = "/home/user/kam/"
RED = {r["source"] for r in json.load(open(ROOT + "vercel.json"))["redirects"]}
CITY_HUB = {"lahore": "/tax-consultant-lahore"}
for c in ["karachi", "islamabad", "rawalpindi", "faisalabad", "peshawar", "multan", "quetta", "hyderabad", "gujranwala", "sargodha", "sialkot"]:
    CITY_HUB[c] = f"/blogs/tax-consultant-{c}"
PROV_HUB = {"Sindh": "/blogs/sindh-income-tax-guide-2026", "Balochistan": "/blogs/balochistan-income-tax-guide-2026",
            "KP": "/blogs/kpk-income-tax-guide-2026", "GB": "/blogs/gilgit-baltistan-tax-guide-2026", "AJK": "/blogs/azad-kashmir-tax-guide-2026"}
PUNJAB_DIV = ["faisalabad", "multan", "gujranwala", "sargodha", "sialkot", "rawalpindi", "bahawalpur", "sahiwal", "dera-ghazi-khan"]
KW = {"punjab": "Punjab", "sindh": "Sindh", "khyber": "KP", "pakhtunkhwa": "KP", "kpk": "KP", "balochistan": "Balochistan",
      "gilgit": "GB", "baltistan": "GB", "azad": "AJK", "ajk": "AJK", "kashmir": "AJK"}
KP = set("battagram chitral lower-dir hangu haripur havelian mansehra malakand mingora-swat buner charsadda topi shangla tank bannu abbottabad kohat mardan swabi nowshera swat karak lakki-marwat dera-ismail-khan".split())
GB = set("hunza gilgit skardu chilas".split())


def text(t):
    m = re.search(r"<article\b.*?</article>", t, re.S) or re.search(r"<main\b.*?</main>", t, re.S)
    b = re.sub(r"<(script|style)\b.*?</\1>", " ", m.group(0) if m else t, flags=re.S)
    return " " + re.sub(r"[^a-z]+", " ", html.unescape(re.sub(r"<[^>]+>", " ", b)).lower()) + " "


def title(t):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", t, re.S) or re.search(r"<title>(.*?)</title>", t, re.S)
    return re.split(r"\s+[|:—–-]\s+", html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip())[0]


def hub_for(slug, tx):
    b = slug[len("tax-consultant-"):]
    for c, h in CITY_HUB.items():
        if b.endswith("-" + c) or b.startswith(c + "-"):
            return h
    if b in CITY_HUB or b.endswith("-pakistan") or "los-angeles" in b:
        return None
    if b in GB:
        return PROV_HUB["GB"]
    if b in KP:
        return PROV_HUB["KP"]
    c = collections.Counter(KW[w] for w in tx.split() if w in KW)
    prov = c.most_common(1)[0][0] if c else "Punjab"
    if prov in PROV_HUB:
        return PROV_HUB[prov]
    best = max(PUNJAB_DIV, key=lambda d: tx.count(" " + d.replace("-", " ") + " "))
    if tx.count(" " + best.replace("-", " ") + " ") and best != b and f"/blogs/tax-consultant-{best}" not in RED:
        return f"/blogs/tax-consultant-{best}"
    return CITY_HUB["lahore"]


def path_of(u):
    return ROOT + u.lstrip("/") + ".html"


def main():
    pages = {}
    for f in glob.glob(ROOT + "blogs/tax-consultant-*.html"):
        s = f.split("/")[-1][:-5]
        if f"/blogs/{s}" in RED:
            continue
        t = open(f, encoding="utf-8").read()
        if re.search(r'<meta name="robots"[^>]*noindex', t):
            continue
        pages[s] = t
    kids = collections.defaultdict(list)
    up = 0
    for s, t in pages.items():
        h = hub_for(s, text(t))
        if not h or not __import__("os").path.exists(path_of(h)):
            continue
        kids[h].append(s)
        if 'class="ka-hub"' in t:
            continue
        ht = title(open(path_of(h), encoding="utf-8").read())
        line = (f'<p class="ka-hub" style="margin:20px 0 0;font-size:.92rem">Wider area: <a href="{h}" '
                f'style="color:#0D9488;font-weight:600">{html.escape(ht)}</a></p>\n')
        # after the first paragraph of the article: its neighbours are unique page text, so the line adds no shared 8-grams
        a = t.find("<article")
        k = t.find("</p>", a) if a > -1 else -1
        if k < 0:
            continue
        k += 4
        open(ROOT + f"blogs/{s}.html", "w", encoding="utf-8").write(t[:k] + "\n" + line.rstrip("\n") + t[k:])
        up += 1
    down = 0
    for h, ss in kids.items():
        p = path_of(h)
        t = open(p, encoding="utf-8").read()
        body = re.sub(r"<nav\b.*?</nav>|<footer\b.*?</footer>", " ", t, flags=re.S)
        have = set(re.findall(r'href="(/[^"#?]*)"', body))
        miss = sorted(s for s in ss if f"/blogs/{s}" not in have)
        if not miss:
            continue
        lis = "".join(f'<li><a href="/blogs/{s}">{html.escape(title(pages[s]))}</a></li>' for s in miss)
        if '<ul class="ka-hub-list">' in t:
            t = t.replace('<ul class="ka-hub-list">', '<ul class="ka-hub-list">' + lis, 1)
        else:
            box = ('<section class="ka-related" aria-label="Areas and towns we cover"><p class="ka-related-h">Areas and towns we cover</p>'
                   f'<ul class="ka-hub-list ka-related-list">{lis}</ul></section>\n')
            k = t.find('<aside class="ka-exp"')
            if k < 0:
                k = t.find("</article>")
            if k < 0:
                k = t.find('<footer class="ka-footer"')
            if k < 0:
                continue
            t = t[:k] + box + t[k:]
        open(p, "w", encoding="utf-8").write(t)
        down += len(miss)
    print("pages linked up", up, "hub links added", down)
    for h, ss in sorted(kids.items(), key=lambda x: -len(x[1])):
        print(" ", h, len(ss))


if __name__ == "__main__":
    main()
