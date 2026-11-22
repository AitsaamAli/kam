"""Parts 4 and 5 of the city pages programme (owner, 22 Nov 2026): Sindh, Balochistan and Khyber Pakhtunkhwa towns.
Same method as part2.py (whose apply() is reused), with province facts:
- PBS Census 2023 Table 1 for Sindh, KP and Balochistan (parsed into census_other_2023.json).
- FBR field offices page: RTO-I/II Karachi, Hyderabad, Sukkur, Quetta, Peshawar, Abbottabad (addresses as written).
- S.R.O. 1497(I)/2026: Karachi directorate = RTOs Karachi I & II, Hyderabad, Sukkur; Quetta directorate = RTO Quetta;
  Khyber Pakhtunkhwa directorate = RTOs Peshawar and Abbottabad.
- Services authority: KPRA (its own site: set up under the KP Finance Act 2013 to administer sales tax on services);
  SRB and BRA named on FBR's page (their own sites returned 503, so nothing more is claimed about them).
AJK (7 pages) and Gilgit-Baltistan (4 pages) are left out: the 2023 census tables and FBR's office list do not cover them,
so fewer than four official local facts exist. Sadiqabad (Punjab) is done with the Punjab data."""
import hashlib, html, json, sys
sys.path.insert(0, "/home/user/kam/content/city-expand")
import part2 as P

ROOT = P.ROOT
E = html.escape
O = json.load(open(ROOT + "content/city-expand/census_other_2023.json"))
S_PBS = {"sindh": "https://www.pbs.gov.pk/wp-content/uploads/census_tables/tables/table_1_sindh_districts.pdf",
         "kp": "https://www.pbs.gov.pk/wp-content/uploads/census_tables/tables/table_1_kp_districts.pdf",
         "balochistan": "https://www.pbs.gov.pk/wp-content/uploads/census_tables/tables/table_1_balochistan_districts.pdf"}
AUTH = {"sindh": ("Sindh Revenue Board (SRB)", "http://www.srb.gos.pk/"),
        "kp": ("Khyber Pakhtunkhwa Revenue Authority (KPRA)", "https://kpra.gov.pk/"),
        "balochistan": ("Balochistan Revenue Authority (BRA)", "https://bra.gob.pk/")}
DIRECT = {"sindh": "Karachi", "kp": "Khyber Pakhtunkhwa", "balochistan": "Quetta"}
RTO = {"Karachi": "RTO-I (Shahra-e-Kamal Ataturk) and RTO-II (Gulistan-e-Jauhar), Karachi", "Hyderabad": "A-49, S.I.T.E Area",
       "Sukkur": "Main Income Tax Building, Queens Road", "Quetta": "Spinny Road", "Peshawar": "Tax House, Jamrud Road",
       "Abbottabad": "opposite Cantt Garden, Mansehra Road"}
RTO_DIST = {"HYDERABAD": "Hyderabad", "SUKKUR": "Sukkur", "QUETTA": "Quetta", "PESHAWAR": "Peshawar", "ABBOTTABAD": "Abbottabad"}

# slug -> (province, census row, display name)
T = {
 "awaran": ("balochistan", "AWARAN SUB-DIVISION", "Awaran"), "badin": ("sindh", "BADIN TALUKA", "Badin"),
 "chaman": ("balochistan", "CHAMAN DISTRICT", "Chaman"), "dadu": ("sindh", "DADU TALUKA", "Dadu"),
 "dera-bugti": ("balochistan", "DERA BUGTI DISTRICT", "Dera Bugti"), "ghotki": ("sindh", "GHOTKI TALUKA", "Ghotki"),
 "gwadar": ("balochistan", "GWADAR SUB-DIVISION", "Gwadar"), "harnai": ("balochistan", "HARNAI SUB-DIVISION", "Harnai"),
 "hub": ("balochistan", "HUB SUB-DIVISION", "Hub"), "hyderabad": ("sindh", "HYDERABAD CITY TALUKA", "Hyderabad"),
 "jacobabad": ("sindh", "JACOBABAD TALUKA", "Jacobabad"), "jaffarabad-balochistan": ("balochistan", "JAFFARABAD DISTRICT", "Jaffarabad"),
 "jamshoro": ("sindh", "JAMSHORO DISTRICT", "Jamshoro"), "kalat": ("balochistan", "KALAT SUB-DIVISION", "Kalat"),
 "kandhkot": ("sindh", "KANDHKOT TALUKA", "Kandhkot"), "kashmor": ("sindh", "KASHMORE TALUKA", "Kashmore"),
 "khairpur": ("sindh", "KHAIRPUR TALUKA", "Khairpur"), "khuzdar": ("balochistan", "KHUZDAR SUB-DIVISION", "Khuzdar"),
 "kotri": ("sindh", "KOTRI TALUKA", "Kotri"), "larkana": ("sindh", "LARKANA TALUKA", "Larkana"),
 "lasbela": ("balochistan", "LASBELA DISTRICT", "Lasbela"), "mastung": ("balochistan", "MASTUNG SUB-DIVISION", "Mastung"),
 "matiari": ("sindh", "MATIARI TALUKA", "Matiari"), "mehrabpur": ("sindh", "MEHRABPUR TALUKA", "Mehrabpur"),
 "mirpurkhas": ("sindh", "MIRPUR KHAS TALUKA", "Mirpurkhas"), "moro": ("sindh", "MORO TALUKA", "Moro"),
 "nawabshah": ("sindh", "NAWABSHAH TALUKA", "Nawabshah"), "nushki": ("balochistan", "NUSHKI SUB-DIVISION", "Nushki"),
 "panjgur": ("balochistan", "PANJGUR SUB-DIVISION", "Panjgur"), "qila-abdullah": ("balochistan", "KILLA ABDULLAH DISTRICT", "Qila Abdullah"),
 "qila-saifullah": ("balochistan", "KILLA SAIFULLAH DISTRICT", "Qila Saifullah"), "quetta": ("balochistan", "QUETTA DISTRICT", "Quetta"),
 "rohri": ("sindh", "ROHRI TALUKA", "Rohri"), "sanghar": ("sindh", "SANGHAR TALUKA", "Sanghar"),
 "sehwan": ("sindh", "SEHWAN TALUKA", "Sehwan"), "shikarpur": ("sindh", "SHIKARPUR TALUKA", "Shikarpur"),
 "sibi": ("balochistan", "SIBI SUB-DIVISION", "Sibi"), "sukkur": ("sindh", "SUKKUR CITY TALUKA", "Sukkur"),
 "tando-allahyar": ("sindh", "TANDO AHYAR TALUKA", "Tando Allahyar"), "tharparkar": ("sindh", "THARPARKAR DISTRICT", "Tharparkar"),
 "thatta": ("sindh", "THATTA TALUKA", "Thatta"), "turbat": ("balochistan", "TURBAT SUB-DIVISION", "Turbat"),
 "umerkot": ("sindh", "UMER KOT TALUKA", "Umerkot"), "tando-adam": ("sindh", "TANDO ADAM TALUKA", "Tando Adam"),
 "loralai": ("balochistan", "LORALAI DISTRICT", "Loralai"), "zhob": ("balochistan", "ZHOB SUB-DIVISION", "Zhob"),
 "abbottabad": ("kp", "ABBOTTABAD TEHSIL", "Abbottabad"), "bannu": ("kp", "BANNU TEHSIL", "Bannu"), "buner": ("kp", "BUNER DISTRICT", "Buner"),
 "charsadda": ("kp", "CHARSADDA TEHSIL", "Charsadda"), "dera-ismail-khan": ("kp", "DERA ISMAIL KHAN TEHSIL", "Dera Ismail Khan"),
 "haripur": ("kp", "HARIPUR TEHSIL", "Haripur"), "havelian": ("kp", "HAVELIAN TEHSIL", "Havelian"), "karak": ("kp", "KARAK TEHSIL", "Karak"),
 "kohat": ("kp", "KOHAT TEHSIL", "Kohat"), "lakki-marwat": ("kp", "LAKKI MARWAT TEHSIL", "Lakki Marwat"),
 "malakand": ("kp", "MALAKAND DISTRICT", "Malakand"), "mardan": ("kp", "MARDAN TEHSIL", "Mardan"), "mingora-swat": ("kp", "BABUZAI TEHSIL", "Mingora"),
 "nowshera": ("kp", "NOWSHERA TEHSIL", "Nowshera"), "peshawar": ("kp", "PESHAWAR TEHSIL", "Peshawar"), "shangla": ("kp", "SHANGLA DISTRICT", "Shangla"),
 "swabi": ("kp", "SWABI TEHSIL", "Swabi"), "swat": ("kp", "SWAT DISTRICT", "Swat"), "tank": ("kp", "TANK TEHSIL", "Tank"), "topi": ("kp", "TOPI TEHSIL", "Topi"),
 "battagram": ("kp", "BATAGRAM DISTRICT", "Battagram"), "chitral": ("kp", "LOWER CHITRAL DISTRICT", "Chitral"), "hangu": ("kp", "HANGU TEHSIL", "Hangu"),
 "lower-dir": ("kp", "LOWER DIR DISTRICT", "Lower Dir"), "mansehra": ("kp", "MANSEHRA TEHSIL", "Mansehra"), "timergara": ("kp", "LOWER DIR DISTRICT", "Timergara"),
 "upper-dir": ("kp", "UPPER DIR DISTRICT", "Upper Dir"),
}
UNIT = {"TALUKA": "taluka", "TEHSIL": "tehsil", "SUB-DIVISION": "sub-division", "DISTRICT": "district"}


def n(x):
    return int(str(x).replace(",", ""))


def facts(slug):
    prov, row, name = T[slug]
    c = O[prov][row]
    kind = row.rsplit(" ", 1)[1]
    dist = c["district"]
    dc = O[prov].get(dist + " DISTRICT", c)
    distname = dist.title().replace("Killa", "Qila").replace("Umer Kot", "Umerkot").replace("Tando Ahyar", "Tando Allahyar")
    rto = "Karachi" if dist.startswith("KARACHI") else RTO_DIST.get(dist)
    is_unit = kind != "DISTRICT"
    pop = n(c["pop"])
    p17 = n(c["pop2017"]) if c.get("pop2017") else None
    un = row.rsplit(" ", 1)[0].title()
    for a, b in (("Tando Ahyar", "Tando Allahyar"), ("Killa", "Qila"), ("Umer Kot", "Umerkot"), ("Mirpur Khas", "Mirpurkhas")):
        un = un.replace(a, b)
    return dict(prov=prov, name=name, dist=distname, unit=UNIT[kind], unitname=un, tehsil=is_unit, pop=pop, p17=p17,
                grow=round((pop - p17) / p17 * 100, 1) if p17 else None, urb=c["urban"], hh=c["hh"], dpop=n(dc["pop"]), rto=rto,
                district_row=(kind == "DISTRICT"))


def short_answer(slug, f):
    nm, d = f["name"], f["dist"]
    auth = AUTH[f["prov"]][0].split(" (")[1].rstrip(")")
    if f["district_row"]:
        head = f"{nm} ({d} district) had {f['pop']:,} people at Census 2023."
    else:
        head = f"{nm} ({d} district) had {f['pop']:,} people in {f['unitname']} {f['unit']} at Census 2023."
    office = (f"{d} has FBR's RTO {f['rto']}; {nm} filers confirm their office in IRIS." if f["rto"]
              else f"{d} has no FBR RTO listed, so {nm} filers find their tax office in IRIS.")
    return f"{head} {office} {nm} sales tax on services: {auth}. We handle {nm} work online from Lahore."


def section(slug, f):
    nm, d, prov = f["name"], f["dist"], f["prov"]
    L = 'style="color:#0D9488"'
    pbs = f'<a href="{S_PBS[prov]}" {L} target="_blank" rel="noopener">{E(nm)}: PBS Table 1</a>'
    rows = []
    where = f"{d} district" if f["district_row"] else f"{f['unitname']} {f['unit']}"
    rows.append((f"{nm} population", f"{f['pop']:,} in {where} (2023)" + (f", {f['p17']:,} (2017)" if f["p17"] else ""), pbs))
    rows.append((f"{nm} urban share", f"{f['urb']}% urban, {f['hh']} per {nm} household", pbs))
    rows.append((f"{nm} FBR office", (f"RTO {f['rto']}, {RTO[f['rto']]}" if f["rto"] else f"none in {d}; {nm} NTNs: see IRIS"),
                 f'<a href="{P.S_FBR}" {L} target="_blank" rel="noopener">{E(nm)}: FBR offices</a>'))
    rows.append((f"{nm} DNFBPs", f"Director (DNFBPs) {DIRECT[prov]}" + (f" via RTO {f['rto']}" if f["rto"] else f" for {nm}'s provincial RTOs"),
                 f'<a href="{P.S_SRO}" {L} target="_blank" rel="noopener">{E(nm)}: S.R.O. 1497</a>'))
    an, au = AUTH[prov]
    rows.append((f"{nm} services tax", f"{an}", f'<a href="{au}" {L} target="_blank" rel="noopener">{E(nm)}: {E(an.split(" (")[1].rstrip(")"))}</a>'))
    trs = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{c}</td></tr>" for a, b, c in rows)
    if f["p17"] and not f["district_row"]:
        u = f"{f['unitname']} {f['unit']}"
        opts = [f"{u} ({nm}) added {f['pop'] - f['p17']:,} people from 2017 to 2023 ({f['grow']}%).",
                f"From 2017 to 2023 {u} ({nm}) grew {f['grow']}%, or {f['pop'] - f['p17']:,} people.",
                f"{u} ({nm}) had {f['grow']}% more people in 2023 than 2017: {f['pop'] - f['p17']:,}."]
        lead = opts[int(hashlib.md5(slug.encode()).hexdigest(), 16) % 3]
    elif f["p17"]:
        lead = f"{d} district grew from {f['p17']:,} (2017) to {f['pop']:,} (2023), {f['grow']}% for {nm}'s district."
    else:
        lead = f"{nm} sits in {d} district."
    return (f'<h2 id="local-tax-facts">Local Tax Facts for {E(nm)}</h2>\n<p>{E(lead)} {E(nm)} facts checked {P.DLONG}.</p>\n'
            f'<div style="overflow-x:auto"><table><thead><tr><th>{E(nm)}</th><th>Fact</th><th>Source</th></tr></thead><tbody>{trs}</tbody></table></div>\n')


def faqs(slug, f):
    nm, d, prov = f["name"], f["dist"], f["prov"]
    auth = AUTH[prov][0]
    q1 = (f"{nm}: which FBR office handles income tax?",
          (f"{nm} is in {d} district, home of RTO {f['rto']}; {nm} filers confirm theirs in IRIS." if f["rto"]
           else f"{nm} filers: FBR lists no RTO in {d}; {nm} NTNs show theirs in IRIS."))
    q2 = (f"{nm}: who collects sales tax on services?", f"For {nm}, the provincial authority is the {auth}; FBR handles sales tax on goods.")
    return [q1, q2]


def main():
    P.T = {s: None for s in T}
    P.MERGE = {}
    P.facts, P.short_answer, P.section, P.faqs = facts, short_answer, section, faqs
    done = [s for s in T if P.apply(s)]
    # Sadiqabad is in Punjab: Punjab data and functions
    import importlib
    importlib.reload(P)
    P.MERGE = {}
    P.T = {"sadiqabad": ("SADIQABAD TEHSIL", "Rahim Yar Khan", "Sadiqabad")}
    if "SADIQABAD TEHSIL" in P.CENSUS and P.apply("sadiqabad"):
        done.append("sadiqabad")
    print("pages updated", len(done))


if __name__ == "__main__":
    main()
