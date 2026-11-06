#!/usr/bin/env python3
"""P2 fix: worked examples and slab displays that used outdated rates (6 Nov 2026)."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slabs import bus_table, sal_table  # noqa: E402

FIX = {
    "blogs/business-income-tax-pakistan-2026.html": [(
        "Tax Calculation (Rs. 1,200,001 &ndash; Rs. 2,200,000 slab):<br>\nRs. 30,000 + 15% &times; (Rs. 2,000,000 &minus; Rs. 1,200,000)<br>\n= Rs. 30,000 + 15% &times; Rs. 800,000<br>\n= Rs. 30,000 + Rs. 120,000<br>\n<strong>= Rs. 150,000 gross income tax</strong><br><br>\nLess WHT credits (Section 153 from customers): Rs. (40,000)<br>\n<strong>Net tax payable: Rs. 110,000</strong>",
        "Tax Calculation (non-salaried slab Rs. 1,600,001 &ndash; Rs. 3,200,000, Tax Year 2027):<br>\nRs. 170,000 + 30% &times; (Rs. 2,000,000 &minus; Rs. 1,600,000)<br>\n= Rs. 170,000 + 30% &times; Rs. 400,000<br>\n= Rs. 170,000 + Rs. 120,000<br>\n<strong>= Rs. 290,000 gross income tax</strong><br><br>\nLess WHT credits (Section 153 from customers): Rs. (40,000)<br>\n<strong>Net tax payable: Rs. 250,000</strong>")],
    "blogs/section-149-salary-tax-pakistan-2026.html": [(
        "Annual tax: Rs. 30,000 + 15% &times; (Rs. 1,800,000 &minus; Rs. 1,200,000) = Rs. 30,000 + Rs. 90,000 = <strong>Rs. 120,000</strong><br>\nMonthly WHT deduction: Rs. 120,000 &divide; 12 = <strong>Rs. 10,000 per month</strong>",
        "Annual tax (Tax Year 2027): Rs. 6,000 + 11% &times; (Rs. 1,800,000 &minus; Rs. 1,200,000) = Rs. 6,000 + Rs. 66,000 = <strong>Rs. 72,000</strong><br>\nMonthly WHT deduction: Rs. 72,000 &divide; 12 = <strong>Rs. 6,000 per month</strong>")],
    "tax-filing-doctors-pakistan.html": [("Tax Slabs for Doctors (2025&ndash;26)", "Tax Slabs for Doctors (Tax Year 2027)"), ("Tax Slabs for Doctors (2025–26)", "Tax Slabs for Doctors (Tax Year 2027)")],
}
DOCTOR_GRID = re.compile(r'(<h2 id="tax-slabs">[^<]*</h2>\s*)<div class="info-grid">.*?</div>\s*</div>\s*(?=<h2)', re.S)
DOCTOR_NEW = (sal_table() + "<p>Salary from a hospital is taxed at the salaried slabs above when it is more than 75% of taxable income. "
              "Fees from a private practice are non-salaried income; if salary is 75% or less of total income, all income is taxed at the non-salaried slabs below.</p>"
              + bus_table())
BUSINESS_ROWS = ("<tr><td>Below 600,000</td><td>0%</td><td>29% of profit</td><td>Sole proprietor</td></tr>"
                 "<tr><td>600K &ndash; 1.2M</td><td>up to 7.5% effective</td><td>29%</td><td>Sole proprietor</td></tr>"
                 "<tr><td>1.2M &ndash; 2.4M</td><td>7.5% to 17.1% effective</td><td>29%</td><td>Sole proprietor</td></tr>"
                 "<tr><td>2.4M &ndash; 6M</td><td>17.1% to 29.8% effective</td><td>29%</td><td>Comparable near the top of the band</td></tr>"
                 "<tr><td>Above 6M</td><td>rises towards 45%, plus a 10% surcharge on tax above Rs 10m</td><td>29%, plus tax on dividends paid out</td><td>Company often lower if profits are retained</td></tr>")


def main():
    os.chdir(ROOT)
    for f, pairs in FIX.items():
        t = open(f, encoding="utf-8").read()
        n = t
        for a, b in pairs:
            n = n.replace(a, b)
        if f == "tax-filing-doctors-pakistan.html":
            n = DOCTOR_GRID.sub(lambda m: m.group(1) + DOCTOR_NEW, n, count=1)
        if n != t:
            open(f, "w", encoding="utf-8").write(n)
            print("fixed", f)
    f = "best-business-structure-pakistan.html"
    t = open(f, encoding="utf-8").read()
    i = t.find("Sole Proprietor Tax")
    a = t.rfind("<table", 0, i)
    e = t.find("</table>", i)
    tb = t[a:e]
    if "0&ndash;5%" in tb or "0–5%" in tb:
        head_end = tb.find("</tr>") + 5
        body = re.sub(r"<tbody>.*", "<tbody>" + BUSINESS_ROWS + "</tbody>", tb[head_end:], flags=re.S) if "<tbody>" in tb else BUSINESS_ROWS
        new = tb[:head_end] + body
        if "<tbody>" in tb[:head_end]:
            new = tb[:head_end] + BUSINESS_ROWS + "</tbody>"
        t = t[:a] + new + t[e:]
        t = t.replace("</table>", "</table><p>Sole proprietor figures are the effective rate at the edges of each band under the non-salaried slabs for Tax Year 2027; companies pay 29% on taxable profit, and dividends paid to owners are taxed separately.</p>", 1) if "effective rate at the edges" not in t else t
        open(f, "w", encoding="utf-8").write(t)
        print("fixed", f)


if __name__ == "__main__":
    main()
