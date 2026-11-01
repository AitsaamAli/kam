#!/usr/bin/env python3
"""Replace outdated late-filing penalty, ATL surcharge and fee figures on tax pages (checked 1 November 2026).

Current position used everywhere:
- Section 182 (entry 1, as published on fbr.gov.pk): 0.1% of tax payable per day of default, max 50% of tax payable,
  minimum Rs 40,000 (also when no tax is payable); minimum Rs 5,000 where at least 75% of income is salary and
  salary income is below Rs 5 million.
- Section 182A ATL surcharge (Finance Act 2026, from 1 July 2026): individual Rs 25,000, AOP Rs 50,000, company Rs 100,000.
- Our fees as published on /pricing: business/freelancer return Rs 5,000, AOP Rs 8,000, company from Rs 18,000.
Usage: python3 content/penalty-fix-2026/fix_penalties.py   (prints files changed and leftover suspicious phrases)
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EN = "a Section 182 penalty of 0.1% of tax payable per day (minimum Rs. 40,000, or Rs. 5,000 for most salaried individuals)"
EN_SHORT = "0.1% of tax payable per day (min. Rs. 40,000; Rs. 5,000 for most salaried)"
RU = "Section 182 penalty: 0.1% of tax payable per day (kam az kam Rs 40,000, zyada tar salaried ke liye Rs 5,000)"
SUR = "the Section 182A ATL surcharge (Rs. 25,000 for individuals, Rs. 50,000 for AOPs, Rs. 100,000 for companies)"

PAIRS = [
    # ── templated area / service pages ──
    ("Late filing attracts a penalty of Rs.1,000 per month for individuals.", f"Late filing can attract {EN}."),
    ("Late filing attracts a penalty of Rs.1,000 per month.", f"Late filing can attract {EN}."),
    ("— Rs.1,000 per month for individuals; Rs.10,000 per month for companies<", f"— {EN_SHORT}, plus Rs.25,000 ATL surcharge for individuals<"),
    ("Non-compliance attracts a penalty of Rs.1,000/month for individuals or Rs.10,000/month for companies, plus 0.1% of tax due per day.",
     f"Late filing can attract {EN}, and {SUR} to get back on the ATL."),
    ("Rs.1,000/month + 0.1% of tax<", f"{EN_SHORT}<"),
    ("Rs.10,000/month + 0.1% of tax<", "0.1% of tax payable per day (min. Rs. 40,000)<"),
    ("Filing after these dates attracts a monthly penalty of Rs.1,000 (individuals) or Rs.10,000 (companies).",
     f"Filing after these dates can attract {EN}."),
    ("Rs.1,000 per month penalty + ATL surcharge (Rs.25,000 individual)", "Section 182 penalty (0.1% of tax payable per day, kam az kam Rs.40,000; zyada tar salaried ke liye Rs.5,000) + ATL surcharge (Rs.25,000 individual)"),
    ("Rs. 1,000 per month penalty aur ATL surcharge lag sakti hai.", f"{RU} aur ATL surcharge (Rs 25,000) lag sakta hai."),
    ("Late filing penalty: Rs. 1,000/month + 0.1% of tax payable<", f"Late filing penalty: {EN_SHORT}<"),
    ("You face a penalty of Rs. 1,000 per month of delay (individuals) plus a 0.1% daily surcharge on tax payable, and you drop off the Active Taxpayer List until the surcharge is cleared and ATL inclusion is processed.",
     f"You can face {EN}, and you stay off the Active Taxpayer List until you pay {SUR}."),
    ("Late filing costs Rs. 1,000/month (individuals) plus 0.1% of tax per day, and drops you off ATL until the surcharge is paid",
     "Late filing can cost a Section 182 penalty of 0.1% of tax payable per day (minimum Rs. 40,000, or Rs. 5,000 for most salaried), and keeps you off the ATL until the Rs. 25,000 surcharge is paid"),
    ("Rs. 1,000/month penalty<", "Section 182 penalty (0.1%/day, kam az kam Rs. 40,000; salaried Rs. 5,000) + Rs. 25,000 ATL surcharge<"),
    ("Rs. 1,000/day + ATL exclusion<", "0.1% of tax payable/day (min. Rs. 40,000) + ATL exclusion<"),
    ("Rs. 1,000/day (min. Rs. 10,000)", EN_SHORT),
    # ── blog posts ──
    ("Late filing penalty: Rs 1,000/day (maximum 50% of tax payable)", "Late filing penalty: 0.1% of tax payable per day (maximum 50% of tax payable; kam az kam Rs 40,000, zyada tar salaried ke liye Rs 5,000)"),
    ("A late return also attracts a penalty of Rs. 1,000 per day under Section 182.", f"A late return can also attract {EN}."),
    ("A return filed after 30 September attracts a minimum penalty of Rs. 1,000 per day under Section 182, and the taxpayer is immediately removed from ATL until a fresh ATL is published.",
     f"A return filed after the due date can attract {EN}, and the taxpayer stays off the ATL until {SUR} is paid."),
    ("Late penalty: Rs. 1,000/day<", "Late penalty: 0.1% of tax/day (min. Rs. 5,000 for most salaried)<"),
    ("Penalties: late return Rs 1,000 per month + potential 35% income tax + 10% surcharge.", f"Penalties: late return par {RU}, aur ATL ke liye Rs 25,000 surcharge."),
    ("Late filing par FBR penalty lagti hai — Rs 1,000/day ya minimum Rs 10,000.", f"Late filing par FBR {RU} laga sakta hai."),
    ("Rs 1,000/day (minimum Rs 10,000)<", "0.1% of tax/day (min. Rs 40,000; salaried Rs 5,000)<"),
    ("Late filing par penalty Rs 1,000 per day aur minimum Rs 10,000 lagti hai.", f"Late filing par {RU} lag sakti hai."),
    ("Late filing penalty: Rs 1,000/day, minimum Rs 10,000.", f"Late filing penalty: 0.1% of tax payable per day, kam az kam Rs 40,000 (zyada tar salaried ke liye Rs 5,000)."),
    ("Penalty Rs. 1,000/month + non-filer rates<", "Section 182 penalty (min. Rs. 40,000) + non-filer rates<"),
    ("a Section 182 penalty of Rs. 1,000 per month, and a possible Section 205 surcharge or Section 114A penalty depending on your situation",
     f"{EN}, and default surcharge under Section 205 on any tax paid late"),
    ("accruing a Section 182 penalty of Rs. 1,000 per month or part of a month the return remains outstanding.",
     "exposed to a Section 182 penalty of 0.1% of tax payable for every day the return remains outstanding (minimum Rs. 40,000, or Rs. 5,000 for most salaried individuals)."),
    ("If tax is also payable, Section 205 applies the higher of that figure or 0.1% of the tax payable per week, and FBR can levy up to Rs. 50,000 under Section 114A if you've received a formal notice.",
     "If tax is also unpaid, default surcharge under Section 205 applies to it, and a formal Section 114(4) notice can follow if you still do not file."),
    ("Miss that second date and the normal penalties (Section 182, Section 205, loss of Active Taxpayer List status, possible Section 114A notice) begin applying from 16 October.",
     "Miss that second date and the normal consequences (Section 182 penalty, Section 205 default surcharge on unpaid tax, loss of Active Taxpayer List status, a possible Section 114(4) notice) begin applying."),
    ("and the Section 114A penalty provision (up to Rs. 50,000) becomes more directly relevant than it would be for someone",
     "and ignoring it can lead to an assessment based on the information FBR already holds, which is more serious than it would be for someone"),
    ("Late filing attracts a penalty of Rs. 1,000 per day under Section 182(1) from 1 October onwards, in addition to any default surcharge on unpaid tax.",
     f"Late filing can attract {EN}, in addition to any default surcharge on unpaid tax."),
    ("Haan — late returns file ho sakti hain penalty ke saath (Rs 1,000/year minimum).", f"Haan — late returns file ho sakti hain; har saal ki late return par {RU}."),
    ("Penalty lagti hai (Rs 1,000/year minimum) lekin", f"Har saal ki late return par {RU}, lekin"),
    ("a Section 182 penalty of Rs. 1,000 per month or part thereof, a possible Section 205 surcharge if tax is payable, and up to Rs. 50,000 under Section 114A if FBR has issued a notice.",
     f"{EN}, and default surcharge under Section 205 if tax is unpaid."),
    ("A penalty under Section 182 — Rs. 1,000 per month or part of a month the return is late — begins accruing, and if tax is also payable, Section 205 applies the higher of that Rs. 1,000 figure or 0.1% of the tax payable per week. FBR can also levy up to Rs. 50,000 under Section 114A for non-filers who've been formally notified.",
     "A Section 182 penalty becomes possible: 0.1% of tax payable for each day of delay, minimum Rs. 40,000 (Rs. 5,000 for most salaried individuals). Unpaid tax also attracts default surcharge under Section 205, and to rejoin the ATL a late filer pays the Rs. 25,000 Section 182A surcharge."),
    ("Late filing penalty calculate karo (Rs 1,000/day ya 0.1% of tax whichever higher).", "Late filing penalty calculate karo (0.1% of tax payable per day, kam az kam Rs 40,000; zyada tar salaried ke liye Rs 5,000)."),
    ("Late filing penalty: Rs 1,000 per day ya 0.1% of tax payable per week — jo bhi zyada ho.", f"Late filing penalty: {RU}."),
    ("Rs 1,000 per year minimum<", "Kam az kam Rs 5,000 (salaried) ya Rs 40,000 per year<"),
    ("Rs 1,000 per year — bohot kam<", "Rs 5,000 per year (salaried) ya Rs 40,000 (baqi)<"),
    ("Rs 1,000/day OR 0.1%/week of tax — whichever higher<", "0.1% of tax per day (max 50% of tax)<"),
    ("Agar taxable income zero tha (salary below Rs 600,000 zyada tar saalon mein) toh penalty sirf Rs 1,000 per year hai.",
     "Agar tax zero tha to bhi Section 182 ka kam az kam penalty lag sakta hai: zyada tar salaried ke liye Rs 5,000 per year, baqi ke liye Rs 40,000."),
    ("Agar tax banta tha toh Rs 1,000/day ya 0.1% per week — whichever higher — maximum 50% of tax due.", "Agar tax banta tha toh 0.1% of tax payable per day — maximum 50% of tax due."),
    ("Penalty per year: Rs 1,000 (minimum)<", "Penalty per year: Rs 5,000 (salaried minimum)<"),
    ("5 saal ki total penalty: Rs 5,000<", "5 saal ki total penalty: Rs 25,000 (salaried minimum ke hisaab se)<"),
    ("5 saal ka total Rs 5,000.", "5 saal ka total kam az kam Rs 25,000 (salaried)."),
    ("and a Section 182 penalty of Rs. 1,000 per month begins accruing.", f"and {EN} can be imposed."),
    ("A late filing penalty applies — typically Rs. 1,000 per month or 0.1% of tax due, whichever is higher — but filing late is far better than not filing.",
     "A Section 182 penalty can apply (0.1% of tax payable per day, minimum Rs. 40,000, or Rs. 5,000 for most salaried individuals), but filing late is far better than not filing."),
    ("A late filing penalty applies &mdash; typically Rs. 1,000 per month or 0.1% of tax due, whichever is higher &mdash; but filing late is far better than not filing.",
     "A Section 182 penalty can apply (0.1% of tax payable per day, minimum Rs. 40,000, or Rs. 5,000 for most salaried individuals), but filing late is far better than not filing."),
    ("Late filing typically attracts a penalty of Rs. 1,000 per day (subject to minimum limits set in the Finance Act).", f"Late filing can attract {EN}."),
    ("Filing after the deadline attracts a penalty of Rs. 1,000 per day (minimum Rs. 10,000 for first-time late filers).", f"Filing after the deadline can attract {EN}."),
    ("The Rs. 1,000/month penalty stops accruing once you file.", "The daily Section 182 penalty count stops once you file."),
    ("Under Section 182, the penalty is Rs. 1,000 per month (or part thereof) for each month the return is late. If tax was also due, the higher of Rs. 1,000/month or 0.1% of tax payable per week applies under Section 205. FBR can also impose up to Rs. 50,000 under Section 114A for complete non-filers who receive notices.",
     "Under Section 182, the penalty is 0.1% of tax payable for each day the return is late, capped at 50% of tax payable, with a minimum of Rs. 40,000 (Rs. 5,000 where at least 75% of income is salary below Rs. 5 million). Unpaid tax also attracts default surcharge under Section 205, and to rejoin the ATL a late filer pays the Section 182A surcharge (Rs. 25,000 for individuals)."),
    ("Late filing costs Rs. 1,000/month penalty plus loss of Active Taxpayer List status, which doubles your WHT rates on bank profit and property.",
     "Late filing can cost a Section 182 penalty (minimum Rs. 40,000, or Rs. 5,000 for most salaried) plus loss of Active Taxpayer List status, which doubles your WHT rates on bank profit and property."),
    ("Rs. 1,000 per month for each month or part thereof<", "0.1% of tax payable per day; minimum Rs. 40,000 (Rs. 5,000 for most salaried)<"),
    ("Higher of: Rs. 1,000/month OR 0.1% of tax payable per week<", "0.1% of tax payable per day, max 50% of tax; plus Section 205 default surcharge on unpaid tax<"),
    ("The Rs. 1,000/month is not the real penalty.", "Even the penalty is not the main cost."),
    ("Failed to file at all (notified)</td><td>Section 114A</td><td>FBR can impose up to Rs. 50,000 penalty + ex-parte assessment",
     "Failed to file at all (notified)</td><td>Section 114(4) and 121</td><td>Best-judgment assessment on FBR's data, plus the Section 182 penalty"),
    ("Section 114A notice may arrive requiring you to file with a penalty<", "Section 114(4) notice may arrive requiring you to file<"),
    ("FBR has sent you a filing notice (Section 114A)<", "FBR has sent you a filing notice (Section 114(4))<"),
    ("Source: Sections 182, 205, 114A, Income Tax Ordinance 2001", "Source: Sections 114, 182, 182A and 205, Income Tax Ordinance 2001"),
    ("late filing attracts a Rs. 1,000/month penalty.<", "late filing can attract a Section 182 penalty (minimum Rs. 40,000, or Rs. 5,000 for most salaried).<"),
    ("A late filing penalty of Rs. 1,000 per month applies under Section 182.", f"Late filing can attract {EN}."),
    ("pay the separate ATL surcharge under Section 182A (Rs. 1,000 for individuals, Rs. 10,000 for AOPs, Rs. 20,000 for companies)",
     "pay the separate ATL surcharge under Section 182A (Rs. 25,000 for individuals, Rs. 50,000 for AOPs, Rs. 100,000 for companies)"),
    ("0.1% of tax payable per week; penalties under ITO<", "0.1% of tax payable per day (min. Rs. 40,000); penalties under ITO<"),
    ("a Section 182 penalty of Rs. 1,000 per month, and potentially a Section 205 surcharge or Section 114A penalty",
     f"{EN}, and default surcharge under Section 205 on any tax paid late"),
    ("Late filing penalty: Rs. 1,000 per month (minimum) under Section 182<", "Late filing penalty: 0.1% of tax payable per day under Section 182 (minimum Rs. 40,000; Rs. 5,000 for most salaried)<"),
    ("FBR levies Rs 1,000 per month late filing penalty for individuals (Section 182). If tax is also owed, the penalty is the higher of Rs 1,000/month or 0.1% of tax payable per week.",
     "Section 182 allows a late filing penalty of 0.1% of tax payable per day, capped at 50% of tax payable, with a minimum of Rs 40,000 (Rs 5,000 for most salaried individuals)."),
    ("Under Section 182, late filing attracts a penalty of Rs. 1,000 per month (minimum) if your tax liability is nil, or 0.1% of tax payable per month if you have tax due.",
     "Under Section 182, late filing can attract a penalty of 0.1% of tax payable per day, capped at 50% of tax payable, with a minimum of Rs. 40,000 even when no tax is payable."),
    ("Under Section 182, late filing attracts a penalty of Rs. 1,000 per month if your tax liability is nil, or 0.1% of tax payable per month if you have tax due.",
     "Under Section 182, late filing can attract a penalty of 0.1% of tax payable per day, capped at 50% of tax payable, with a minimum of Rs. 40,000 even when no tax is payable."),
    ("Rs 1,000/month ya 0.1% of tax — whichever higher<", "0.1% of tax/day (kam az kam Rs 40,000; salaried Rs 5,000)<"),
    ("Missing this date results in a Rs. 1,000/month late filing penalty under Section 182 and removal from the Active Taxpayer List.",
     "Missing the due date can result in a Section 182 penalty (minimum Rs. 5,000 for most salaried individuals) and removal from the Active Taxpayer List until the Rs. 25,000 surcharge is paid."),
    ("Rs. 1,000/month minimum<", "Section 182: min. Rs. 40,000<"),
    ("Rs. 1,000 per day of default, up to a maximum of 50 per cent of the tax payable for the year.",
     "0.1% of the tax payable for each day of default, up to a maximum of 50 per cent of the tax payable for the year, with a minimum of Rs. 40,000 (Rs. 5,000 for most salaried individuals)."),
    ("Rs. 1,000/month or 0.1% of tax, whichever is higher<", "0.1% of tax/day (min. Rs. 40,000; salaried Rs. 5,000)<"),
    ("Rs. 5,000/month minimum<", "0.1% of tax/day (min. Rs. 40,000)<"),
    ("Rs. 10,000/month or 0.1% of tax/day<", "0.1% of tax/day (min. Rs. 40,000)<"),
    ("Late filing penalty under Section 182: Rs. 1,000/day for individuals (max Rs. 50,000 for salaried), Rs. 2,500/day for companies",
     "Late filing penalty under Section 182: 0.1% of tax payable per day, max 50% of tax payable, minimum Rs. 40,000 (Rs. 5,000 for most salaried individuals)"),
    ("Rs. 1,000/day (individual) up to Rs. 50,000", "0.1% of tax payable/day, max 50% of tax; min. Rs. 40,000 (Rs. 5,000 for most salaried)"),
    ("under Section 182 (Rs. 1,000 per year if return is nil;", "under Section 182 (minimum Rs. 40,000, or Rs. 5,000 for most salaried, even if the return is nil;"),
    ("you'll face a penalty of Rs. 1,000 per day (up to 50% of tax payable)", "you can face a Section 182 penalty of 0.1% of tax payable per day (up to 50% of tax payable, minimum Rs. 40,000 or Rs. 5,000 for most salaried)"),
    ("From 1 October onwards, a penalty of Rs. 1,000 per day accrues on your account for every day you have not filed.",
     "From the day after the due date, the Section 182 formula counts 0.1% of tax payable for every day you have not filed."),
    ("and a Rs. 1,000 per day penalty begins accruing the moment the deadline passes.", "and a Section 182 penalty based on 0.1% of tax payable per day becomes possible the moment the deadline passes."),
    ("A late-filed return with a Rs. 1,000 per day penalty (capped at 50% of tax due)", "A late-filed return with a Section 182 penalty (capped at 50% of tax due)"),
    ("The total penalty owed is Rs. 1,000 per day from 1 October to the date of filing, capped at 50% of tax payable",
     "The Section 182 penalty is 0.1% of tax payable for each day from the due date to the date of filing, capped at 50% of tax payable"),
    ("triggers Rs. 1,000 per day penalty under Section 182", "can trigger a Section 182 penalty of 0.1% of tax payable per day"),
]
REGEX = [
    # our fee tables: business/freelancer return Rs 5,000 (pricing page), company from Rs 18,000
    (r"(Income Tax Return \((?:Business|Business/Freelancer)\)</td>\s*<td[^>]*>)Rs\.7,000", r"\1Rs.5,000"),
    (r"Income Tax Return \(Company/AOP\)(</td>\s*<td[^>]*>)Rs\.20,000", r"Income Tax Return (Company)\1Rs.18,000+"),
    (r"Rs\.3,500 for a basic salaried individual income tax return, Rs\.7,000 for business or freelancer returns",
     "Rs.3,500 for a basic salaried individual income tax return, Rs.5,000 for business or freelancer returns"),
    (r"(Company Late Return \+ ATL Surcharge</td><td>)Rs\.20,000 \+", r"\1Rs.18,000+ +"),
    (r"Private Limited Company ke liye Rs\. 20,000 se Rs\. 50,000\+ tak hoti hai", "Private Limited Company ke liye Rs. 18,000 se shuru hoti hai"),
    # ATL surcharge table on the ATL guide (old amounts shown as current)
    (r"(Individual</td>\s*<td[^>]*>)Rs\.1,000(</td>)", r"\1Rs.25,000\2"),
    (r"(AOP / Partnership</td>\s*<td[^>]*>)Rs\.10,000(</td>)", r"\1Rs.50,000\2"),
    (r"(Company</td>\s*<td[^>]*>)Rs\.20,000(</td>)", r"\1Rs.100,000\2"),
]
SKIP = ("digital/", "node_modules/")
NEW = ("tax-return-deadline-passed-31-october-2026", "late-filer-atl-surcharge-or-form-atl-u", "guzar-gayi-ab-kya-karein")


def main():
    os.chdir(ROOT)
    changed = []
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith(SKIP) or any(n in f for n in NEW):
            continue
        t = open(f, encoding="utf-8").read()
        n = t
        for old, new in PAIRS:
            n = n.replace(old, new)
            # same sentence inside JSON-LD with escaped quotes
            if '"' in old:
                n = n.replace(old.replace('"', '\\"'), new.replace('"', '\\"'))
        for pat, rep in REGEX:
            n = re.sub(pat, rep, n)
        if n != t:
            open(f, "w", encoding="utf-8").write(n)
            changed.append(f)
    print("files changed:", len(changed))
    R = r"Rs\.?\s?"
    left = [R + r"1,000\s*(?:per|a|/)\s*(?:month|day|year)", r"monthly penalty of " + R + "1,000", r"0\.1%[^<.]{0,40}per week",
            r"114A\b[^<]{0,40}(?:penalty|50,000|notice)", R + r"1,000 for individuals", R + r"1,000\s*\(minimum\)", r"Rs\.7,000<"]
    for f in sorted(glob.glob("**/*.html", recursive=True)):
        if f.startswith(SKIP):
            continue
        t = open(f, encoding="utf-8").read()
        for p in left:
            for m in re.finditer(p, t, re.I):
                print("LEFT", f, "::", re.sub(r"\s+", " ", t[max(0, m.start() - 90):m.end() + 50]))


if __name__ == "__main__":
    main()
