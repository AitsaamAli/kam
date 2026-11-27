"""Fact fix, 27 Nov 2026 (owner: fix wrong facts before the December 2026 core update).
Rates checked in the Income Tax Ordinance as amended to 30 June 2026 (FBR PDF):
- 236C: 2.75% of consideration (First Schedule Part IV Division X, as substituted by Finance Act 2026); off the ATL 11.5% (Tenth Schedule).
- 236K: 1.25% of fair market value (Division XVIII); off the ATL 10.5% to Rs 50m, 14.5% to Rs 100m, 18.5% above (Tenth Schedule proviso).
Pages stating the off-ATL rates as 5.5% (236C) or 2.5% (236K) are corrected in context. Not touched: the owner-pending page
property-transfer-tax-2026-27-pakistan-236c-236k (and its blogs.html excerpt), the 7E page's before/after table, s.148 import rates,
and the pre-2026 slab history (4.5% / 5% / 5.5%). Run with --apply to write; without it, prints the changes."""
import glob, json, re, sys
R = "/home/user/kam/"
APPLY = "--apply" in sys.argv
red = {r["source"] for r in json.load(open(R + "vercel.json"))["redirects"]}
EX = ("content", "outreach", "reports", "seo_output", "searchops-team", "project-history", "schema", "content-batches", "digital")
SKIP = {"blogs/property-transfer-tax-2026-27-pakistan-236c-236k.html", "blogs/section-7e-abolished-fcc-ruling-2026-pakistan.html"}
SELL = re.compile(r"236C|sale WHT|property sale|Property sale|[Ss]ell|[Ss]eller|bech|[Ff]arokht|Jaidad ki farokht|selling", re.I)
BUY = re.compile(r"236K|[Pp]urchase|[Bb]uy|[Bb]uyer|khareed|Khareed", re.I)
NOT = re.compile(r"\b148\b|[Ii]mport|old-rate|halved|[Bb]udget 2026|reduced from|slab table|4\.5%, 5%|236H|236G|Finance Act", re.I)
K_PROSE = "10.5% (to Rs 50m; 14.5% to Rs 100m, 18.5% above)"
K_CELL = "10.5%&ndash;18.5%"


def fix(t):
    out, n, notes = [], 0, []
    i = 0
    for m in re.finditer(r"(?<![\d.])(5\.5|2\.5)\s?%", t):
        pre = t[max(0, m.start() - 170):m.start()]
        near = t[max(0, m.start() - 70):m.end() + 40]
        if NOT.search(near):
            continue
        rate = m.group(1)
        if rate == "5.5" and SELL.search(pre) and "2.75%" in t[max(0, m.start() - 140):m.end() + 60]:
            new = "11.5%"
        elif rate == "2.5" and BUY.search(pre) and "1.25%" in t[max(0, m.start() - 140):m.end() + 60]:
            cell = t[m.start() - 4:m.start()].endswith("<td>") or t[m.start()-1] == ">"
            new = K_CELL if cell else K_PROSE
            inj = t[m.start() - 220:m.start()]
            if '"text":' in inj[-200:] or "content=\"" in inj[-200:]:
                new = "10.5% to 18.5%"
        else:
            continue
        out.append(t[i:m.start()]); out.append(new); i = m.end(); n += 1
        notes.append(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t[max(0, m.start() - 60):m.end() + 50])))
    out.append(t[i:])
    return "".join(out), n, notes


tot = 0
for f in sorted(glob.glob(R + "**/*.html", recursive=True)):
    rel = f[len(R):]
    if rel.startswith(EX) or rel in SKIP or "/" + rel[:-5] in red:
        continue
    t = open(f, encoding="utf-8").read()
    new, n, notes = fix(t)
    if n:
        tot += n
        print("==", rel, n)
        if not APPLY:
            for x in notes[:4]:
                print("    ", x[:150])
        else:
            open(f, "w", encoding="utf-8").write(new)
print("total", tot)
