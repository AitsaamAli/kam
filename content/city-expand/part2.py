"""Part 2 of the city pages programme (owner, 22 Nov 2026): Punjab towns A-K.
Adds to each page a Short answer box, a 'Local tax facts' section with 4-5 official facts, two local FAQs (visible and in FAQPage
schema), official source links with the date checked, and points the hub link at the district page. Idempotent (marker: ka-local).
Facts:
- PBS, 7th Population and Housing Census 2023, Table 1, Punjab (district and tehsil rows): population 2023 and 2017, urban share,
  household size.
- FBR field offices page: Regional Tax Offices in Punjab and their addresses (no district list is published there, so the page only
  says where an RTO sits, and that the IRIS profile shows the office for each NTN).
- S.R.O. 1497(I)/2026: DNFBPs within the RTOs of Lahore, Sialkot, Gujranwala, Faisalabad, Sargodha, Multan, Sahiwal and Bahawalpur ->
  Director (DNFBPs) Lahore; RTO Rawalpindi -> Director (DNFBPs) Islamabad.
- Punjab Sales Tax on Services Act 2012 s.25 and PRA Registration Rules 2012 rule 15.
Also merges two duplicates found in part 2: kamonke -> kamoke (content moved), khanpur-ryk -> khanpur."""
import hashlib, html, json, re

ROOT = "/home/user/kam/"
CENSUS = json.load(open(ROOT + "content/city-expand/census_punjab_2023.json"))  # parsed from the PBS Table 1 Punjab PDF
DATE, DLONG = "2026-11-22", "22 November 2026"
S_PBS = "https://www.pbs.gov.pk/wp-content/uploads/census_tables/tables/table_1_punjab_districts.pdf"
S_FBR = "https://fbr.gov.pk/regional-tax-offices/524"
S_SRO = "https://download1.fbr.gov.pk/Docs/2026916149312406SRO1497-2026JurisdictionofDNFBPAuthorities.pdf"
S_PRA = "https://reg.pra.punjab.gov.pk/PTMS/SOP/Download/SalesTaxAct2012/Chapter%204-%20REGISTRATION.pdf"
RTO = {"Lahore": "Tax House, Nabha Road", "Gujranwala": "G-T Road", "Faisalabad": "opposite Allied Hospital, Jail Road",
       "Sialkot": "Kutchery Road", "Bahawalpur": "21-A Sarwar Shaheed Road, Model Town-A", "Sargodha": "Shahi Palace, Chatha Town, Lahore Road",
       "Sahiwal": "Canal Colony", "Multan": "LMQ Road, Nawan Shehr", "Rawalpindi": "12 Mayo Road"}

# slug -> (census row, district, display name)
T = {
 "ahmadpur-east": ("AHMADPUR EAST TEHSIL", "Bahawalpur", "Ahmadpur East"), "arifwala": ("ARIF WALA TEHSIL", "Pakpattan", "Arifwala"),
 "attock": ("ATTOCK TEHSIL", "Attock", "Attock"), "bahawalpur": ("BAHAWALPUR CITY TEHSIL", "Bahawalpur", "Bahawalpur"),
 "bhakkar": ("BHAKKAR TEHSIL", "Bhakkar", "Bhakkar"), "bhalwal": ("BHALWAL TEHSIL", "Sargodha", "Bhalwal"),
 "bhawalnagar": ("BAHAWALNAGAR TEHSIL", "Bahawalnagar", "Bahawalnagar"), "burewala": ("BUREWALA TEHSIL", "Vehari", "Burewala"),
 "chakwal": ("CHAKWAL TEHSIL", "Chakwal", "Chakwal"), "chichawatni": ("CHICHAWATNI TEHSIL", "Sahiwal", "Chichawatni"),
 "chiniot": ("CHINIOT TEHSIL", "Chiniot", "Chiniot"), "choa-saidan-shah": ("CHOA SAIDAN SHAH TEHSIL", "Chakwal", "Choa Saidan Shah"),
 "chunian": ("CHUNIAN TEHSIL", "Kasur", "Chunian"), "darya-khan": ("DARYA KHAN TEHSIL", "Bhakkar", "Darya Khan"),
 "dina": ("DINA TEHSIL", "Jhelum", "Dina"), "ferozewala": ("FEROZEWALA TEHSIL", "Sheikhupura", "Ferozewala"),
 "gojra": ("GOJRA TEHSIL", "Toba Tek Singh", "Gojra"), "gujar-khan": ("GUJAR KHAN TEHSIL", "Rawalpindi", "Gujar Khan"),
 "gujranwala": ("GUJRANWALA CITY TEHSIL", "Gujranwala", "Gujranwala"), "hafizabad": ("HAFIZABAD TEHSIL", "Hafizabad", "Hafizabad"),
 "hazro": ("HAZRO TEHSIL", "Attock", "Hazro"), "isa-khel": ("ISAKHEL TEHSIL", "Mianwali", "Isa Khel"),
 "jalalpur-pirwala": ("JALALPUR PIRWALA TEHSIL", "Multan", "Jalalpur Pirwala"), "jaranwala": ("JARANWALA TEHSIL", "Faisalabad", "Jaranwala"),
 "jhang": ("JHANG TEHSIL", "Jhang", "Jhang"), "joharabad": ("KHUSHAB DISTRICT", "Khushab", "Joharabad"),
 "kabirwala": ("KABIRWALA TEHSIL", "Khanewal", "Kabirwala"), "kalur-kot": ("KALUR KOT TEHSIL", "Bhakkar", "Kalur Kot"),
 "kamalia": ("KAMALIA TEHSIL", "Toba Tek Singh", "Kamalia"), "kamoke": ("KAMOKE TEHSIL", "Gujranwala", "Kamoke"),
 "kasur": ("KASUR TEHSIL", "Kasur", "Kasur"), "khanewal": ("KHANEWAL TEHSIL", "Khanewal", "Khanewal"),
 "khanpur": ("KHANPUR TEHSIL", "Rahim Yar Khan", "Khanpur"), "kharian": ("KHARIAN TEHSIL", "Gujrat", "Kharian"),
 "khushab": ("KHUSHAB TEHSIL", "Khushab", "Khushab"), "kot-addu": ("KOT ADDU TEHSIL", "Muzaffargarh", "Kot Addu"),
 "kot-momin": ("KOT MOMIN TEHSIL", "Sargodha", "Kot Momin"), "kot-radha-kishan": ("KOT RADHA KISHAN TEHSIL", "Kasur", "Kot Radha Kishan"),
 "kunjah": ("GUJRAT DISTRICT", "Gujrat", "Kunjah"), "lalamusa": ("GUJRAT DISTRICT", "Gujrat", "Lalamusa"),
 "liaquatpur": ("LIAQUAT PUR TEHSIL", "Rahim Yar Khan", "Liaquatpur"), "daska": ("DASKA TEHSIL", "Sialkot", "Daska"),
 "dera-ghazi-khan": ("DERA GHAZI KHAN TEHSIL", "Dera Ghazi Khan", "Dera Ghazi Khan"),
 "faisalabad": ("FAISALABAD CITY TEHSIL", "Faisalabad", "Faisalabad"), "fateh-jang": ("FATEH JANG TEHSIL", "Attock", "Fateh Jang"),
 "gujrat": ("GUJRAT TEHSIL", "Gujrat", "Gujrat"), "jhelum": ("JHELUM TEHSIL", "Jhelum", "Jhelum"),
}
MERGE = {"kamonke": "kamoke", "khanpur-ryk": "khanpur"}
LAHORE_DIR = {"Lahore", "Sialkot", "Gujranwala", "Faisalabad", "Sargodha", "Multan", "Sahiwal", "Bahawalpur"}
E = html.escape


def n(x):
    return int(str(x).replace(",", ""))


def pick(slug, k, options):
    return options[int(hashlib.md5((slug + k).encode()).hexdigest(), 16) % len(options)]


def facts(slug):
    row, dist, name = T[slug]
    c = CENSUS[row]
    dc = CENSUS[dist.upper() + " DISTRICT"]
    tehsil = row.endswith("TEHSIL")
    unit = row.rsplit(" ", 1)[0].title().replace("Arif Wala", "Arif Wala").replace("Liaquat Pur", "Liaquat Pur")
    pop, p17, urb, hh = n(c["pop"]), n(c["pop2017"]), c["urban"], c["hh"]
    grow = round((pop - p17) / p17 * 100, 1)
    rto_city = dist if dist in RTO else None
    return dict(name=name, dist=dist, tehsil=tehsil, unit=unit, pop=pop, p17=p17, grow=grow, urb=urb, hh=hh,
                dpop=n(dc["pop"]), rto=rto_city)


def short_answer(slug, f):
    nm, d = f["name"], f["dist"]
    if f["tehsil"]:
        head = f"{nm} ({d} district) had {f['pop']:,} people in {nm} tehsil at Census 2023."
    else:
        head = f"{nm} is in {d} district, which had {f['dpop']:,} people at Census 2023."
    if f["rto"]:
        office = f"{d} has FBR's RTO {f['rto']}; {nm} filers confirm their office in IRIS."
    else:
        office = f"{d} has no FBR RTO listed, so {nm} filers find their tax office in IRIS."
    return f"{head} {office} {nm} service businesses register with PRA (free); we handle {nm} work online from Lahore."


def section(slug, f):
    nm, d = f["name"], f["dist"]
    L = 'style="color:#0D9488"'
    pbs = f'<a href="{S_PBS}" {L} target="_blank" rel="noopener">{E(nm)}: PBS Table 1</a>'
    rows = []
    if f["tehsil"]:
        rows.append((f"{nm} population", f"{f['pop']:,} (2023), {f['p17']:,} (2017)", pbs))
        rows.append((f"{nm} urban share", f"{f['urb']}% urban, {f['hh']} per {nm} household", pbs))
    else:
        rows.append((f"{nm} population", f"{d} district {f['dpop']:,}; {nm} not counted separately", pbs))
    rows.append((f"{nm} FBR office", (f"RTO {f['rto']}, {RTO[f['rto']]}" if f["rto"] else f"none in {d}; {nm} NTNs: see IRIS"),
                 f'<a href="{S_FBR}" {L} target="_blank" rel="noopener">{E(nm)}: FBR offices</a>'))
    dn = ("Lahore" if f["rto"] in LAHORE_DIR else "Islamabad") if f["rto"] else None
    rows.append((f"{nm} DNFBPs", (f"Director (DNFBPs) {dn} via RTO {f['rto']}" if dn else f"{nm}: Lahore or Islamabad, by RTO"),
                 f'<a href="{S_SRO}" {L} target="_blank" rel="noopener">{E(nm)}: S.R.O. 1497</a>'))
    rows.append((f"{nm} services tax", f"PRA; {nm} registration free",
                 f'<a href="{S_PRA}" {L} target="_blank" rel="noopener">{E(nm)}: PRA s.25, r.15</a>'))
    trs = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{c}</td></tr>" for a, b, c in rows)
    if f["tehsil"]:
        lead = pick(slug, "p", [
            f"{nm} tehsil added {f['pop'] - f['p17']:,} people from 2017 to 2023 ({f['grow']}%).",
            f"From 2017 to 2023 {nm} tehsil grew {f['grow']}%, or {f['pop'] - f['p17']:,} people.",
            f"{nm} tehsil had {f['grow']}% more people in 2023 than 2017: {f['pop'] - f['p17']:,}.",
        ])
    else:
        lead = f"{nm} lies in {d} district; {nm} has no separate census line."
    return (f'<h2 id="local-tax-facts">Local Tax Facts for {E(nm)}</h2>\n<p>{E(lead)} {E(nm)} facts checked {DLONG}.</p>\n'
            f'<div style="overflow-x:auto"><table><thead><tr><th>{E(nm)}</th><th>Fact</th><th>Source</th></tr></thead><tbody>{trs}</tbody></table></div>\n')


def faqs(slug, f):
    nm, d = f["name"], f["dist"]
    q1 = (f"{nm}: which FBR office handles income tax?",
          (f"{nm} is in {d} district, home of RTO {f['rto']}; {nm} filers confirm theirs in IRIS." if f["rto"]
           else f"{nm} filers: FBR lists no RTO in {d}; {nm} NTNs show theirs in IRIS."))
    q2 = (f"{nm} service firms: PRA registration?", f"Yes: {nm} taxable services register with PRA; {nm} registration is free (rule 15).")
    return [q1, q2]


def sources_line():
    return ""


def merge_duplicates():
    vj = json.load(open(ROOT + "vercel.json"))
    have = {r["source"] for r in vj["redirects"]}
    for sec, main in MERGE.items():
        src = f"/blogs/tax-consultant-{sec}"
        if src in have:
            continue
        if sec == "kamonke":
            a = open(ROOT + f"blogs/tax-consultant-{sec}.html", encoding="utf-8").read()
            b = open(ROOT + f"blogs/tax-consultant-{main}.html", encoding="utf-8").read()
            ma, mb = re.search(r"<article\b.*?</article>", a, re.S), re.search(r"<article\b.*?</article>", b, re.S)
            body = ma.group(0).replace(f"/blogs/tax-consultant-{sec}", f"/blogs/tax-consultant-{main}")
            b = b[:mb.start()] + body + b[mb.end():]
            open(ROOT + f"blogs/tax-consultant-{main}.html", "w", encoding="utf-8").write(b)
        vj["redirects"].append({"source": src, "destination": f"/blogs/tax-consultant-{main}", "permanent": True})
    json.dump(vj, open(ROOT + "vercel.json", "w"), indent=2)
    sm = open(ROOT + "sitemap.xml", encoding="utf-8").read()
    bl = open(ROOT + "blogs.html", encoding="utf-8").read()
    for sec in MERGE:
        sm = re.sub(r"\s*<url>\s*<loc>https://kambohassociates\.com/blogs/tax-consultant-" + sec + r"</loc>.*?</url>", "", sm, flags=re.S)
        bl = re.sub(r'\n  \{\n    id: "tax-consultant-' + sec + r'",.*?\n  \},', "", bl, flags=re.S)
        bl = re.sub(r'      <a href="/blogs/tax-consultant-' + sec + r'"[^\n]*\n', "", bl)
    open(ROOT + "sitemap.xml", "w", encoding="utf-8").write(sm)
    open(ROOT + "blogs.html", "w", encoding="utf-8").write(bl)
    import glob
    for p in glob.glob(ROOT + "**/*.html", recursive=True):
        if "/content/" in p or any(p.endswith(f"tax-consultant-{s}.html") for s in MERGE):
            continue
        t = open(p, encoding="utf-8").read()
        o = t
        for sec, main in MERGE.items():
            t = t.replace(f'href="/blogs/tax-consultant-{sec}"', f'href="/blogs/tax-consultant-{main}"')
        if t != o:
            open(p, "w", encoding="utf-8").write(t)


def apply(slug):
    p = ROOT + f"blogs/tax-consultant-{slug}.html"
    t = open(p, encoding="utf-8").read()
    if 'class="ka-local ' in t:
        return False
    f = facts(slug)
    box = ('<div class="ka-local tldr-box" style="background:linear-gradient(135deg,rgba(20,184,166,.08),rgba(20,184,166,.04));border:1.5px solid '
           'rgba(20,184,166,.35);border-radius:12px;padding:16px 20px;margin:18px 0 24px;display:flex;gap:12px;align-items:flex-start">'
           '<div style="background:#14B8A6;color:#fff;border-radius:6px;padding:3px 9px;font-size:.68rem;font-weight:700;letter-spacing:.08em;'
           'flex-shrink:0;margin-top:2px">Short answer</div><p style="margin:0;font-size:.93rem;color:#1E293B;line-height:1.7">'
           + E(short_answer(slug, f)) + "</p></div>\n")
    # after the hub line (or the first paragraph)
    m = re.search(r'<p class="ka-hub"[^>]*>.*?</p>', t)
    k = m.end() if m else t.find("</p>", t.find("<article")) + 4
    t = t[:k] + "\n" + box + t[k:]
    # local section before the first existing H2 of the body
    sec = section(slug, f)
    h = re.search(r"<details class=\"ka-toc\".*?</details>\n?", t, re.S)
    if h:
        t = t[:h.start()] + t[h.end():]  # TOC is rebuilt by apply.py with the new section included
    j = t.find("<h2", k)
    t = t[:j] + sec + t[j:]
    # sources
    s = t.find('<p class="official-sources"')
    t = (t[:s] + sources_line() + t[s:]) if s > -1 else t.replace('<aside class="ka-exp"', sources_line() + '<aside class="ka-exp"', 1)
    # FAQs: visible + schema
    qa = faqs(slug, f)
    vis = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in qa)
    if '<div class="tf-faq">' in t:
        t = t.replace('<div class="tf-faq">', '<div class="tf-faq">' + vis, 1)
    def addq(mm):
        d = json.loads(mm.group(1))
        names = {q["name"] for q in d["mainEntity"]}
        d["mainEntity"] = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa if q not in names] + d["mainEntity"]
        return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>"
    t = re.sub(r'<script type="application/ld\+json">(\{"@context": "https://schema.org", "@type": "FAQPage".*?)</script>', addq, t, count=1, flags=re.S)
    t = re.sub(r'"dateModified": "[^"]*"', f'"dateModified": "{DATE}"', t, count=1)
    # hub: district page if it exists
    dslug = "tax-consultant-" + f["dist"].lower().replace(" ", "-")
    import os
    if dslug != f"tax-consultant-{slug}" and os.path.exists(ROOT + f"blogs/{dslug}.html"):
        dt = open(ROOT + f"blogs/{dslug}.html", encoding="utf-8").read()
        title = re.split(r"\s+[|:—–-]\s+", html.unescape(re.sub(r"<[^>]+>", "", re.search(r"<h1[^>]*>(.*?)</h1>", dt, re.S).group(1))).strip())[0]
        t = re.sub(r'(<p class="ka-hub"[^>]*>Wider area: <a href=")[^"]*("[^>]*>)[^<]*(</a>)', lambda mm: mm.group(1) + f"/blogs/{dslug}" + mm.group(2) + E(title) + mm.group(3), t, count=1)
    open(p, "w", encoding="utf-8").write(t)
    return True


def main():
    merge_duplicates()
    done = [s for s in T if apply(s)]
    print("pages updated", len(done))


if __name__ == "__main__":
    main()
