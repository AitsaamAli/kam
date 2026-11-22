"""Parts 8-10, second pass (owner asked for the best solution, 22 Nov 2026).
1. FBR value: Lahore area pages that match a row of FBR's Lahore valuation table (S.R.O. 1722(I)/2024, s.68 ITO; rows 1330-1363
   were amended by S.R.O. 876(I)/2026 and are not used) get a 'FBR Value of Property' section: per-marla residential / commercial
   values and worked 236K / 236C figures at those values. Unique official numbers per area. Data: fbr_lahore_valuation_2024.json,
   mapping: fbr_lahore_map.json. Pages without the Local Tax Facts block get it (Short answer + FAQs) through part2.apply.
2. Merge: block/sector sub-pages (FBR values them at the parent area's rate, so they could only repeat it) and 'near <landmark>'
   pages 301 to their parent area page / the Lahore hub (lahore_merges.json). Files kept, as with earlier redirects.
Idempotent (markers ka-fmv, ka-local)."""
import glob, html, json, os, re, sys
sys.path.insert(0, "/home/user/kam/content/city-expand")
import part2 as P

ROOT = P.ROOT
E = html.escape
L = 'style="color:#0D9488"'
SRO = "https://download1.fbr.gov.pk/SROs/20241030Lahore1722.pdf"
ITO = "https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf"
T = {r[0]: r for r in json.load(open(ROOT + "content/city-expand/fbr_lahore_valuation_2024.json"))}
MAP = json.load(open(ROOT + "content/city-expand/fbr_lahore_map.json"))
MERGES = json.load(open(ROOT + "content/city-expand/lahore_merges.json"))
NEAR = ["near-airport", "near-doctors-hospital", "near-ganga-ram", "near-high-court", "near-jinnah-hospital", "near-lums",
        "near-mayo-hospital", "near-pu", "near-services-hospital", "near-ucp", "near-uet"]
for n in NEAR:
    p = f"blogs/tax-consultant-{n}-lahore.html"
    if os.path.exists(ROOT + p):
        MERGES[p] = "tax-consultant-lahore.html"


def url(p):
    return "/" + p[:-5]


def num(x):
    x = str(x).replace(",", "").strip()
    return int(x) if x.isdigit() else None


def k236(v):
    return 0.105 if v <= 50_000_000 else 0.145 if v <= 100_000_000 else 0.185


def merge():
    vj = json.load(open(ROOT + "vercel.json"))
    have = {r["source"] for r in vj["redirects"]}
    for kid, par in MERGES.items():
        if url(kid) not in have:
            vj["redirects"].append({"source": url(kid), "destination": url(par), "permanent": True})
    json.dump(vj, open(ROOT + "vercel.json", "w"), indent=2)
    sm = open(ROOT + "sitemap.xml", encoding="utf-8").read()
    bl = open(ROOT + "blogs.html", encoding="utf-8").read()
    for kid in MERGES:
        u = url(kid)
        sm = re.sub(r"\s*<url>\s*<loc>https://kambohassociates\.com" + re.escape(u) + r"</loc>.*?</url>", "", sm, flags=re.S)
        slug = u.split("/")[-1]
        bl = re.sub(r'\n  \{\n    id: "' + re.escape(slug) + r'",.*?\n  \},', "", bl, flags=re.S)
        bl = re.sub(r'      <a href="' + re.escape(u) + r'"[^\n]*\n', "", bl)
    open(ROOT + "sitemap.xml", "w", encoding="utf-8").write(sm)
    open(ROOT + "blogs.html", "w", encoding="utf-8").write(bl)
    rep = {f'href="{url(k)}"': f'href="{url(p)}"' for k, p in MERGES.items()}
    for f in glob.glob(ROOT + "**/*.html", recursive=True):
        rel = f[len(ROOT):]
        if rel.startswith(("content/", "node_modules/")) or rel in MERGES:
            continue
        t = open(f, encoding="utf-8").read()
        o = t
        for a, b in rep.items():
            t = t.replace(a, b)
        if t != o:
            open(f, "w", encoding="utf-8").write(t)


def name_of(slug):
    return {"mm-alam-road": "MM Alam Road", "pcsir": "PCSIR Housing", "nespak-housing": "NESPAK Housing", "wapda-town": "WAPDA Town",
            "dha-raya": "DHA Raya", "askari-10": "Askari X"}.get(slug) or slug.replace("-", " ").title()


def fmv_block(slug):
    nm = name_of(slug)
    rows, ex = [], []
    for k in MAP[slug]:
        r = T[k]
        area, rp, cp = r[2], num(r[3]), num(r[5])
        rows.append(f"<tr><td>{E(nm)}: {E(area)} (S.No. {k})</td><td>{('Rs ' + format(rp, ',')) if rp else 'not valued'}</td>"
                    f"<td>{('Rs ' + format(cp, ',')) if cp else 'not valued'}</td></tr>")
        if not ex:
            base, kind = (rp, "residential") if rp else (cp, "commercial")
            for marla, label in ((5, "5 marla"), (20, "1 kanal")):
                v = base * marla
                ex.append(f"<tr><td>{E(nm)} {label} {kind} plot</td><td>Rs {v:,}</td><td>Rs {round(v * 0.0125):,}</td>"
                          f"<td>Rs {round(v * k236(v)):,}</td><td>Rs {round(v * 0.0275):,}</td><td>Rs {round(v * 0.115):,}</td></tr>")
    return (f'<div class="ka-fmv">\n<h2 id="fbr-value">FBR Value of Property in {E(nm)}</h2>\n'
            f'<p>FBR fixes the value of immovable property in {E(nm)} under section 68 of the Income Tax Ordinance, through '
            f'<a href="{SRO}" {L} target="_blank" rel="noopener">S.R.O. 1722(I)/2024</a> (29 October 2024). The {E(nm)} rows of that table:</p>\n'
            f'<div style="overflow-x:auto"><table><thead><tr><th>{E(nm)} entry</th><th>Residential plot, per marla</th><th>Commercial plot, per marla</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div>\n'
            f'<p>Advance tax at the {E(nm)} FBR value: 236K on the buyer is charged on fair market value; 236C on the seller is charged on the sale price, '
            f'so the 236C figures below apply only if the {E(nm)} plot sells at the FBR value. Rates: ATL 1.25% / 2.75%; off the ATL 236K 10.5% to Rs 50m, '
            f'14.5% to Rs 100m, 18.5% above, and 236C 11.5% (<a href="{ITO}" {L} target="_blank" rel="noopener">ITO 2001, Tenth Schedule</a>).</p>\n'
            f'<div style="overflow-x:auto"><table><thead><tr><th>{E(nm)} example</th><th>FBR value</th><th>236K, ATL buyer</th><th>236K, off-ATL buyer</th>'
            f'<th>236C, ATL seller</th><th>236C, off-ATL seller</th></tr></thead><tbody>{"".join(ex)}</tbody></table></div>\n</div>\n')


def facts_fmv(slug):
    return dict(name=name_of(slug), dist="Lahore", slug=slug, rto="Lahore", tehsil=False)


def short_fmv(_s, f):
    slug = f["slug"]
    r = T[MAP[slug][0]]
    rp, cp = num(r[3]), num(r[5])
    v = f"Rs {rp:,} a marla (residential)" if rp else f"Rs {cp:,} a marla (commercial)"
    return (f"FBR values {f['name']} property at {v} under S.R.O. 1722(I)/2024, so a {f['name']} buyer on the ATL pays 236K of 1.25% of that value. "
            f"{f['name']} filers see their FBR office in IRIS; {f['name']} services register with PRA free. We serve {f['name']} from Awan Town, Lahore.")


def section_fmv(_s, f):
    nm = f["name"]
    rows = [(f"{nm} FBR office", "see IRIS; Lahore's RTO is at Tax House, Nabha Road", f'<a href="{P.S_FBR}" {L} target="_blank" rel="noopener">{E(nm)}: FBR offices</a>'),
            (f"{nm} DNFBPs", "Director (DNFBPs) Lahore for Lahore RTOs", f'<a href="{P.S_SRO}" {L} target="_blank" rel="noopener">{E(nm)}: S.R.O. 1497</a>'),
            (f"{nm} services tax", f"PRA; {nm} registration free", f'<a href="{P.S_PRA}" {L} target="_blank" rel="noopener">{E(nm)}: PRA s.25, r.15</a>')]
    trs = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{c}</td></tr>" for a, b, c in rows)
    return (f'<h2 id="local-tax-facts">Local Tax Facts for {E(nm)}</h2>\n<p>{E(nm)} facts checked {P.DLONG}.</p>\n'
            f'<div style="overflow-x:auto"><table><thead><tr><th>{E(nm)}</th><th>Fact</th><th>Source</th></tr></thead><tbody>{trs}</tbody></table></div>\n')


def faqs_fmv(_s, f):
    nm, slug = f["name"], f["slug"]
    r = T[MAP[slug][0]]
    rp, cp = num(r[3]), num(r[5])
    v = rp or cp
    return [(f"{nm}: what is the FBR value of a plot?", f"S.R.O. 1722(I)/2024 values {nm} ({r[2]}) at Rs {v:,} a marla; a 5 marla {nm} plot is Rs {v * 5:,}."),
            (f"{nm}: how much 236K does a buyer pay?", f"At the {nm} FBR value, an ATL buyer pays 1.25%: Rs {round(v * 5 * 0.0125):,} on 5 marla.")]


def main():
    merge()
    P.MERGE = {}
    P.facts, P.short_answer, P.section, P.faqs = facts_fmv, short_fmv, section_fmv, faqs_fmv
    done = 0
    for slug in MAP:
        stem = f"{slug}-lahore"
        p = ROOT + f"blogs/tax-consultant-{stem}.html"
        if not os.path.exists(p) or f"blogs/tax-consultant-{stem}.html" in MERGES:
            continue
        P.T = {stem: None}
        f = facts_fmv(slug)
        P.facts = lambda _s, f=f: f
        P.apply(stem)  # adds Short answer, Local Tax Facts, FAQs when the page has none yet
        t = open(p, encoding="utf-8").read()
        if 'class="ka-fmv"' in t:
            continue
        m = re.search(r'</table></div>\n', t[t.find('id="local-tax-facts"'):]) if 'id="local-tax-facts"' in t else None
        k = (t.find('id="local-tax-facts"') + m.end()) if m else t.find("<h2", t.find("<article"))
        t = t[:k] + fmv_block(slug) + t[k:]
        t = re.sub(r'<details class="ka-toc".*?</details>\n?', "", t, count=1, flags=re.S)
        open(p, "w", encoding="utf-8").write(t)
        done += 1
    print("merged", len(MERGES), "fbr value sections", done)


if __name__ == "__main__":
    main()
