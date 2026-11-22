"""Parts 8-10 (Lahore areas), group-wise official facts (owner chose this route, 22 Nov 2026).
Groups with verified official facts:
- DHA: dhalahore.org transfer page (DHA Transfer Branch processes regular transfer, NDC, hiba, legal heirs, SPA; NDC needs the
  property tax receipt and clearance from Walton / Lahore Cantt Board).
- Walled City gates: walledcitylahore.gop.pk (Punjab Walled Cities & Heritage Areas Authority, set up by the Government of Punjab in
  2012; its gates page lists the gates of Old Lahore).
- Industrial estates: pie.com.pk (PIEDMC head office at Sundar Industrial Estate, Raiwind Road; city office at Quaid-e-Azam
  Industrial Estate, Kot Lakhpat).
- Census tehsils of Lahore district: Raiwind, Shalimar, Lahore Cantt (PBS Census 2023 Table 1, Punjab).
- Housing societies: ITO 2001 s.236C/236K Explanation (housing authorities, housing societies and co-operative societies that
  record transfers collect the advance tax), Division X / XVIII and Tenth Schedule rates.
Every group also gets RTO Lahore (FBR field offices), Director (DNFBPs) Lahore (S.R.O. 1497(I)/2026) and PRA (Act s.25, rule 15).
Pages that fit no verified group (LDA schemes, cantonment-only areas, roads, markets, landmark 'near' pages and block/sector
sub-pages) are left for the owner's decision. Idempotent via part2.apply (marker ka-local)."""
import hashlib, html, json, re, sys
sys.path.insert(0, "/home/user/kam/content/city-expand")
import part2 as P

ROOT = P.ROOT
E = html.escape
L = 'style="color:#0D9488"'
S_DHA = "https://dhalahore.org/dha-facilities/transfer/"
S_WCLA = "https://walledcitylahore.gop.pk/gates/"
S_PIE = "https://pie.com.pk/"
S_ITO = "https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf"
GATES = {"akbari-gate": "Akbari", "bhatti-gate": "Bhatti", "delhi-gate": "Delhi", "lohari-gate": "Lohari", "mochi-gate": "Mochi",
         "mori-gate": "Mori", "sheranwala-gate": "Sheranwala", "taxali-gate": "Taxali", "yakki-gate": "Zakki (Yakki)"}
INDUSTRIAL = {"sundar-industrial": ("Sundar Industrial Estate", "PIEDMC's head office is at Sundar Industrial Estate, Raiwind Road"),
              "kot-lakhpat-industrial": ("Quaid-e-Azam Industrial Estate, Kot Lakhpat", "PIEDMC's city office is at Quaid-e-Azam Industrial Estate, Kot Lakhpat")}
TEHSIL = {"raiwind": "RAIWIND TEHSIL", "shalimar": "SHALIMAR TEHSIL", "lahore-cantt": "LAHORE CANTT TEHSIL"}
SOC = ["valencia", "wapda-town", "lake-city", "paragon-city", "eden-city", "eden-garden", "eden-residencia", "eden-abad", "al-kabir-town",
       "al-noor-town", "airport-housing-society", "engineers-town", "medical-housing-society", "nespak-housing", "pcsir",
       "punjab-govt-employees", "revenue-society", "sui-gas-society", "uet-housing-society", "state-life-housing", "green-city",
       "river-garden", "sa-gardens", "safari-garden", "central-park", "bahria-town", "bahria-orchard", "bahria-nasheman",
       "bahria-education-city", "bahria-rafi-block"]
DHA = ["dha", "dha-rahbar", "dha-raya"]
PILOT = ["dha-rahbar", "dha-raya", "mochi-gate", "bhatti-gate", "sundar-industrial", "kot-lakhpat-industrial", "raiwind", "bahria-orchard", "valencia", "wapda-town"]


def disp(slug):
    special = {"dha": "DHA Lahore", "dha-rahbar": "DHA Rahbar", "dha-raya": "DHA Raya", "pcsir": "PCSIR Housing", "sa-gardens": "SA Gardens",
               "uet-housing-society": "UET Housing Society", "nespak-housing": "NESPAK Housing", "wapda-town": "WAPDA Town",
               "punjab-govt-employees": "Punjab Govt Employees Society", "lahore-cantt": "Lahore Cantt"}
    return special.get(slug) or slug.replace("-", " ").title()


def group(slug):
    if slug in DHA:
        return "dha"
    if slug in GATES:
        return "gate"
    if slug in INDUSTRIAL:
        return "ind"
    if slug in TEHSIL:
        return "tehsil"
    if slug in SOC:
        return "soc"
    return None


def facts(slug):
    return dict(name=disp(slug), dist="Lahore", group=group(slug), slug=slug, rto="Lahore", tehsil=False)


def short_answer(slug, f):
    slug = f["slug"]
    nm, g = f["name"], f["group"]
    if g == "dha":
        a = f"In {nm}, DHA Lahore's own Transfer Branch processes transfers, and an NDC needs the Walton or Lahore Cantt Board property tax receipt."
    elif g == "gate":
        a = f"{nm} is in Old Lahore, whose heritage the Punjab Walled Cities & Heritage Areas Authority (set up in 2012) looks after."
    elif g == "ind":
        a = f"{INDUSTRIAL[slug][0]} is listed among PIEDMC's projects, and {INDUSTRIAL[slug][1].split(' is at ')[0]} is there."
    elif g == "tehsil":
        c = P.CENSUS[TEHSIL[slug]]
        a = f"{nm} tehsil had {P.n(c['pop']):,} people at Census 2023 ({P.n(c['pop2017']):,} in 2017)."
    else:
        a = f"Where the {nm} society office records a transfer, it collects 236C from the seller and 236K from the buyer."
    return f"{a} {nm} filers see their FBR office in IRIS (Lahore's RTO is on Nabha Road); {nm} services register with PRA free. We serve {nm} from Awan Town, Lahore."


def section(slug, f):
    slug = f["slug"]
    nm, g = f["name"], f["group"]
    rows = []
    if g == "dha":
        rows += [(f"{nm} transfers", f"DHA Lahore Transfer Branch: regular transfer, NDC, hiba, legal heirs, SPA", f'<a href="{S_DHA}" {L} target="_blank" rel="noopener">{E(nm)}: DHA transfers</a>'),
                 (f"{nm} NDC", f"Walton / Lahore Cantt Board property tax receipt and clearance", f'<a href="{S_DHA}" {L} target="_blank" rel="noopener">{E(nm)}: DHA NDC</a>'),
                 (f"{nm} advance tax", f"housing authority recording a {nm} transfer collects 236C (seller) and 236K (buyer)", f'<a href="{S_ITO}" {L} target="_blank" rel="noopener">{E(nm)}: ITO s.236C, 236K</a>')]
        lead = f"{nm} property moves through DHA Lahore's own office, not the district sub-registrar, so the paperwork below is specific to {nm}."
    elif g == "gate":
        rows += [(f"{nm} heritage body", f"Punjab Walled Cities & Heritage Areas Authority (Government of Punjab, 2012)", f'<a href="{S_WCLA}" {L} target="_blank" rel="noopener">{E(nm)}: PWCA gates</a>'),
                 (f"{nm} on PWCA list", f"{GATES[slug]} Gate is one of Old Lahore's listed gates", f'<a href="{S_WCLA}" {L} target="_blank" rel="noopener">{E(nm)}: gates page</a>')]
        lead = f"{nm} sits inside Old Lahore, so {nm} traders work in a heritage area listed by PWCA."
    elif g == "ind":
        est, off = INDUSTRIAL[slug]
        rows += [(f"{nm} estate body", f"PIEDMC (Punjab Industrial Estates Development and Management Company)", f'<a href="{S_PIE}" {L} target="_blank" rel="noopener">{E(nm)}: PIEDMC</a>'),
                 (f"{nm} PIEDMC office", off, f'<a href="{S_PIE}" {L} target="_blank" rel="noopener">{E(nm)}: PIEDMC offices</a>'),
                 (f"{nm} goods sales tax", f"FBR sales tax registration (STRN) for {nm} manufacturers", '<a href="/sales-tax-registration" ' + L + f'>{E(nm)}: STRN</a>')]
        lead = f"{est} is one of PIEDMC's projects, so {nm} units deal with an estate company as well as FBR and PRA."
    elif g == "tehsil":
        c = P.CENSUS[TEHSIL[slug]]
        pop, p17 = P.n(c["pop"]), P.n(c["pop2017"])
        pbs = f'<a href="{P.S_PBS}" {L} target="_blank" rel="noopener">{E(nm)}: PBS Table 1</a>'
        rows += [(f"{nm} population", f"{pop:,} (2023), {p17:,} (2017)", pbs), (f"{nm} households", f"{c['hh']} per {nm} household", pbs)]
        lead = f"{nm} tehsil grew {round((pop - p17) / p17 * 100, 1)}% between the 2017 and 2023 censuses, {pop - p17:,} more people."
    else:
        rows += [(f"{nm} transfer tax", f"society recording a {nm} transfer collects 236C 2.75% (seller, ATL) and 236K 1.25% (buyer, ATL)", f'<a href="{S_ITO}" {L} target="_blank" rel="noopener">{E(nm)}: ITO s.236C, 236K</a>'),
                 (f"{nm} off the ATL", f"{nm} seller 11.5%; {nm} buyer 10.5% to Rs 50m", f'<a href="{S_ITO}" {L} target="_blank" rel="noopener">{E(nm)}: Tenth Schedule</a>')]
        lead = f"Section 236C and 236K name housing and co-operative societies among those who collect advance tax when they record a transfer, which is why {nm} sellers and buyers meet it at the {nm} office."
    rows += [(f"{nm} FBR office", f"see IRIS; Lahore's RTO is at Tax House, Nabha Road", f'<a href="{P.S_FBR}" {L} target="_blank" rel="noopener">{E(nm)}: FBR offices</a>'),
             (f"{nm} DNFBPs", f"Director (DNFBPs) Lahore for Lahore RTOs", f'<a href="{P.S_SRO}" {L} target="_blank" rel="noopener">{E(nm)}: S.R.O. 1497</a>'),
             (f"{nm} services tax", f"PRA; {nm} registration free", f'<a href="{P.S_PRA}" {L} target="_blank" rel="noopener">{E(nm)}: PRA s.25, r.15</a>')]
    trs = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{c}</td></tr>" for a, b, c in rows)
    return (f'<h2 id="local-tax-facts">Local Tax Facts for {E(nm)}</h2>\n<p>{E(lead)} {E(nm)} facts checked {P.DLONG}.</p>\n'
            f'<div style="overflow-x:auto"><table><thead><tr><th>{E(nm)}</th><th>Fact</th><th>Source</th></tr></thead><tbody>{trs}</tbody></table></div>\n')


def faqs(slug, f):
    slug = f["slug"]
    nm, g = f["name"], f["group"]
    q1 = {"dha": (f"{nm}: who processes a property transfer?", f"DHA Lahore's Transfer Branch handles {nm} transfers; the {nm} NDC needs the cantonment board property tax receipt."),
          "gate": (f"{nm}: is it a heritage area?", f"Yes. {nm} is on the gates list of the Punjab Walled Cities & Heritage Areas Authority."),
          "ind": (f"{nm}: who runs the estate?", f"PIEDMC, the Punjab industrial estates company, lists {INDUSTRIAL.get(slug, ('',''))[0]} among its projects."),
          "tehsil": (f"{nm}: how many people live in the tehsil?", f"{nm} tehsil had {P.n(P.CENSUS[TEHSIL.get(slug, 'RAIWIND TEHSIL')]['pop']):,} people at Census 2023."),
          "soc": (f"{nm}: who collects tax on a transfer?", f"When the {nm} society records a transfer it collects 236C from the {nm} seller and 236K from the {nm} buyer.")}[g]
    q2 = (f"{nm}: which FBR office handles income tax?", f"{nm} filers find their office in IRIS; FBR lists Lahore's RTO at Tax House, Nabha Road.")
    return [q1, q2]


def main(only=None):
    d = json.load(open(ROOT + "content/city-expand/batches.json"))
    pages = [x.replace("tax-consultant-", "").replace("-lahore", "") for n in (7, 8, 9) for x in d["parts"][n]["pages"]]
    todo = [s for s in pages if group(s) and (only is None or s in only)]
    P.T = {s: None for s in todo}
    P.MERGE = {}
    P.facts, P.short_answer, P.section, P.faqs = facts, short_answer, section, faqs
    orig = P.apply

    def apply_lahore(s):
        import os
        real = None
        for c in (f"blogs/tax-consultant-{s}-lahore.html", f"tax-consultant-{s}-lahore.html", f"blogs/tax-consultant-{s}.html"):
            if os.path.exists(ROOT + c):
                real = c
                break
        if not real:
            return False
        # part2.apply reads blogs/tax-consultant-<slug>.html; pass the real stem
        stem = real.split("tax-consultant-")[1][:-5]
        if not real.startswith("blogs/"):
            return False
        return orig(stem)

    done = []
    for s in todo:
        stem = s + "-lahore"
        P.T[stem] = None
        f = facts(s)
        P.facts = lambda _st, f=f: f
        if apply_lahore(s):
            done.append(s)
    print("pages updated", len(done), sorted(done))


if __name__ == "__main__":
    main(set(PILOT) if "--pilot" in sys.argv else None)
