#!/usr/bin/env python3
"""Correct withholding-statement penalties and the Section 205 default surcharge rate on tax pages (checked 4 November 2026).

Section 182, entry 1A (fbr.gov.pk): statement under 165/165A/165B not filed by the due date -> Rs 5,000 if the tax was
already paid and the statement is filed within 90 days; otherwise Rs 2,500 per day of default, minimum Rs 10,000.
Section 205 (Finance Act 2024): default surcharge at 12% a year or KIBOR + 3%, whichever is higher.
Usage: python3 content/penalty-fix-2026/fix_statements_surcharge.py
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DS = "12% a year or KIBOR + 3%, whichever is higher"
STMT = "Rs. 2,500 per day (minimum Rs. 10,000), or Rs. 5,000 if the tax was paid and the statement is filed within 90 days"

PAIRS = [
    # withholding statements
    ("Late WHT statement</strong> — 0.1% per day of outstanding WHT amount", f"Late WHT statement</strong> — {STMT}"),
    ('<td style="padding:8px">Monthly WHT Statement</td><td style="padding:8px">15th of each month</td><td style="padding:8px">0.1% per day</td>',
     '<td style="padding:8px">Monthly WHT Statement</td><td style="padding:8px">15th of each month</td><td style="padding:8px">Rs.2,500/day (min. Rs.10,000)</td>'),
    ("failure to file WHT statement attracts Rs. 2,500 per day of default, plus 25% surcharge on late tax. This can accumulate to lakhs quickly.",
     f"failure to file a WHT statement attracts {STMT}. Tax deposited late also attracts default surcharge under Section 205."),
    ("Non-filing attracts PKR 2,500/day penalty.", "Non-filing attracts PKR 2,500 per day of default (minimum PKR 10,000), or PKR 5,000 if the tax was paid and the statement is filed within 90 days."),
    ("Late filing attracts a penalty of PKR 2,500 per day from the due date.", "Late filing attracts a penalty of PKR 2,500 per day from the due date, with a minimum of PKR 10,000 (PKR 5,000 if the tax was paid and the statement is filed within 90 days)."),
    ("<td>Late monthly WHT statement</td><td class=\"bad\">PKR 2,500 per day from due date</td>",
     "<td>Late monthly WHT statement</td><td class=\"bad\">PKR 2,500 per day from due date (min. PKR 10,000)</td>"),
    ("the penalty under Section 182(2) is Rs. 2,500 per day from the due date until the statement is filed. A statement that is 30 days late costs Rs. 75,000 in penalties alone.",
     "the penalty under Section 182 is Rs. 2,500 per day from the due date until the statement is filed, with a minimum of Rs. 10,000, or Rs. 5,000 if the tax was already paid and the statement is filed within 90 days. Where the tax was not paid on time, a statement that is 30 days late can cost Rs. 75,000 in penalties alone."),
    ("Failure to file monthly WHT statements: Rs. 2,500 per day default penalty", "Failure to file monthly WHT statements: Rs. 2,500 per day (minimum Rs. 10,000)"),
    ("Rs. 2,500 per day for each day the statement remains unfiled beyond the due date.",
     "Rs. 2,500 per day for each day the statement remains unfiled beyond the due date, with a minimum of Rs. 10,000 (Rs. 5,000 if the tax was paid and the statement is filed within 90 days)."),
    # late return row with an outdated method
    ('<td class="bad">PKR 1,000/month (first 2 months) + PKR 2,000/month + loss of ATL filer status</td>',
     '<td class="bad">0.1% of tax payable per day (min. PKR 40,000; PKR 5,000 for most salaried) + PKR 25,000 ATL surcharge for individuals</td>'),
    ('<td class="bad">12% annual default surcharge + PKR 25,000 minimum penalty</td>',
     f'<td class="bad">Default surcharge ({DS}), plus penalty under Section 182</td>'),
]
REGEX = [
    # specific phrases first, generic ones last
    (r"approximately 12% annual markup rate shortfall amount par", "shortfall amount par 12% saalana ya KIBOR + 3% (jo zyada ho) ki rate se"),
    (r"approximately <strong>12% annual markup rate</strong> ka default surcharge", "<strong>12% saalana ya KIBOR + 3% (jo zyada ho)</strong> ki rate se default surcharge"),
    (r"approximately 12% annual markup rate ka default surcharge", "12% saalana ya KIBOR + 3% (jo zyada ho) ki rate se default surcharge"),
    (r"Underpayment par 12% annual markup surcharge lagta hai", "Underpayment par default surcharge lagta hai (12% saalana ya KIBOR + 3%, jo zyada ho)"),
    (r"penalty aur 12% default surcharge dono", "penalty aur default surcharge (12% saalana ya KIBOR + 3%, jo zyada ho) dono"),
    (r"Penalty \+ 12% default surcharge on unpaid tax", "Penalty + default surcharge (12% saalana ya KIBOR + 3%, jo zyada ho) on unpaid tax"),
    (r"Failure to pay results in 12% annual markup on the shortfall", f"Failure to pay results in default surcharge ({DS}) on the shortfall"),
    (r"12% per annum markup on unpaid tax", f"default surcharge ({DS}) on unpaid tax"),
    (r"12% annual markup on shortfall", f"Default surcharge ({DS})"),
    (r"a 12% annual default surcharge on the outstanding amount", f"default surcharge ({DS}) on the outstanding amount"),
    (r"the 12% default surcharge", "default surcharge under Section 205"),
    (r"default surcharge of 12% per annum on the outstanding amount", f"default surcharge ({DS}) on the outstanding amount"),
    (r"Default surcharge on unpaid tax: 12% per annum", f"Default surcharge on unpaid tax: {DS}"),
    (r"default surcharge at 12% per annum on the unpaid amount", f"default surcharge ({DS}) on the unpaid amount"),
    (r"default surcharge at 12% per annum on unpaid tax", f"default surcharge ({DS}) on unpaid tax"),
    (r"Default surcharge is 12% per annum on shortfall", f"Default surcharge is {DS}, on the shortfall"),
    (r"Default surcharge at 12% per annum on unpaid GST", "Default surcharge on unpaid sales tax under Section 34 of the Sales Tax Act"),
    (r"12% annual markup", f"Default surcharge ({DS})"),
]


def main():
    os.chdir(ROOT)
    changed = []
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith(("content/", "digital/")):
            continue
        t = open(f, encoding="utf-8").read()
        n = t
        for a, b in PAIRS:
            n = n.replace(a, b)
            if '"' in a:
                n = n.replace(a.replace('"', '\\"'), b.replace('"', '\\"'))
        for p, r in REGEX:
            n = re.sub(p, r, n)
        if n != t:
            open(f, "w", encoding="utf-8").write(n)
            changed.append(f)
    print("files changed:", len(changed))
    left = re.compile(r"12\s?%\s*(per annum|annual|p\.a\.)[^<]{0,40}(markup|surcharge)|0\.1% per day of outstanding WHT|25% surcharge on late tax|PKR 1,000/month \(first", re.I)
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith(("content/", "digital/")):
            continue
        for m in left.finditer(open(f, encoding="utf-8").read()):
            print("LEFT", f, m.group(0))


if __name__ == "__main__":
    main()
