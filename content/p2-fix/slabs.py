#!/usr/bin/env python3
"""P2 fix (6 Nov 2026): replace outdated or wrong income tax slab tables site-wide.

Found: pages labelled 2026 or 2026-27 showed Tax Year 2025 salaried rates (5/15/25/30/35), some showed Tax Year 2024
rates (2.5/12.5/22.5/27.5), a business page showed salaried slabs, one table had blank rates, worked examples used old
rates, and /tools/income-tax-calculator used wrong non-salaried slabs (max 35% instead of 45%).

Correct rates:
  Salaried TY2027 (Finance Act 2026): 0 / 1% / 6,000+11% / 116,000+20% / 316,000+25% / 541,000+29% / 976,000+32% / 1,424,000+35% (above 7m)
  Salaried TY2026 (Finance Act 2025): 0 / 1% / 6,000+11% / 116,000+23% / 346,000+30% / 616,000+35% (above 4.1m)
  Non-salaried TY2026 and TY2027 (unchanged): 0 / 15% / 90,000+20% / 170,000+30% / 650,000+40% / 1,610,000+45% (above 5.6m),
  plus a 10% surcharge on tax where taxable income exceeds Rs 10 million.
Usage: python3 content/p2-fix/slabs.py
"""
import html
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SAL27 = [(600000, 0, 0), (1200000, 0, .01), (2200000, 6000, .11), (3200000, 116000, .20), (4100000, 316000, .25),
         (5600000, 541000, .29), (7000000, 976000, .32), (None, 1424000, .35)]
SAL26 = [(600000, 0, 0), (1200000, 0, .01), (2200000, 6000, .11), (3200000, 116000, .23), (4100000, 346000, .30), (None, 616000, .35)]
BUS = [(600000, 0, 0), (1200000, 0, .15), (1600000, 90000, .20), (3200000, 170000, .30), (5600000, 650000, .40), (None, 1610000, .45)]


def tax(x, S):
    lo = 0
    for hi, fixed, rate in S:
        if hi is None or x <= hi:
            return fixed + (x - lo) * rate
        lo = hi
    return 0


def f(n):
    return f"{n:,.0f}"


def desc(S, x_lo):
    lo = 0
    for hi, fixed, rate in S:
        if hi is None or x_lo < hi:
            if rate == 0:
                return "0%"
            return (f"Rs {f(fixed)} + " if fixed else "") + f"{rate * 100:.0f}% above Rs {f(lo)}"
        lo = hi


def sal_table_compact():
    rows, lo = [], 0
    for hi, _, _ in SAL27:
        rng = (f"Up to Rs {f(hi)}" if lo == 0 else (f"Rs {f(lo + 1)} to {f(hi)}" if hi else f"Above Rs {f(lo)}"))
        rows.append(f"<tr><td>{rng}</td><td>{desc(SAL27, lo)}</td></tr>")
        lo = hi or lo
    return ('<table class="data-table"><thead><tr><th>Salary per year</th><th>Employer withholds (Section 149)</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table><p>Employers spread this annual tax over the months of the tax year when deducting salary tax.</p>')


def sal_table(urdu=False):
    rows, lo = [], 0
    for hi, _, _ in SAL27:
        rng = (f"Up to Rs {f(hi)}" if lo == 0 else (f"Rs {f(lo + 1)} to {f(hi)}" if hi else f"Above Rs {f(lo)}"))
        rows.append(f"<tr><td>{rng}</td><td>{desc(SAL27, lo)}</td><td>{desc(SAL26, lo)}</td></tr>")
        lo = hi or lo
    if urdu:
        head = "<tr><th>سالانہ قابلِ ٹیکس تنخواہ</th><th>ٹیکس سال 2027 (یکم جولائی 2026 سے)</th><th>ٹیکس سال 2026</th></tr>"
        note = "<p>تنخواہ دار افراد کی شرحیں، فنانس ایکٹ 2026 اور 2025 کے مطابق۔ ٹیکس سال 2027 میں 9 فیصد سرچارج ختم کر دیا گیا۔</p>"
    else:
        head = "<tr><th>Annual taxable salary</th><th>Tax Year 2027 (from 1 July 2026)</th><th>Tax Year 2026</th></tr>"
        note = ("<p>Salaried slabs under the Finance Act 2026 (Tax Year 2027) and Finance Act 2025 (Tax Year 2026). The 9% surcharge on salaried "
                "income above Rs 10 million was abolished for Tax Year 2027. Source: <a href=\"https://www.fbr.gov.pk/\" rel=\"noopener\">FBR</a>.</p>")
    return f'<table class="slab-table data-table"><thead>{head}</thead><tbody>{"".join(rows)}</tbody></table>{note}'


def bus_table():
    rows, lo = [], 0
    for hi, _, _ in BUS:
        rng = (f"Up to Rs {f(hi)}" if lo == 0 else (f"Rs {f(lo + 1)} to {f(hi)}" if hi else f"Above Rs {f(lo)}"))
        rows.append(f"<tr><td>{rng}</td><td>{desc(BUS, lo)}</td></tr>")
        lo = hi or lo
    return ('<table class="slab-table data-table"><thead><tr><th>Annual taxable business income</th><th>Tax Year 2026 and 2027</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table><p>Non-salaried individuals and AOPs; the Finance Act 2026 left these slabs unchanged. '
            'A 10% surcharge on tax applies where taxable income exceeds Rs 10 million.</p>')


def example_table(monthly):
    rows = "".join(f"<tr><td>Rs {f(m)}</td><td>Rs {f(m * 12)}</td><td>Rs {f(tax(m * 12, SAL27))}</td><td>Rs {f(tax(m * 12, SAL27) / 12)}</td></tr>" for m in monthly)
    return ('<table class="data-table"><thead><tr><th>Monthly salary</th><th>Annual salary</th><th>Annual tax (TY2027)</th><th>Monthly deduction</th></tr></thead>'
            f"<tbody>{rows}</tbody></table>")


def cells(tb):
    return " ".join(re.sub(r"<[^>]+>", " ", html.unescape(c)) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", tb, re.S))


def classify(tb):
    c = re.sub(r"(?<=\d),(?=\d)", "", cells(tb))
    c = re.sub(r"(\d)L\b", r"\g<1>00000", c)
    c = re.sub(r"Rs\s*600K", "600000", c)
    c = re.sub(r"(\d+(?:\.\d+)?)M\b", lambda m: str(int(float(m.group(1)) * 1000000)), c)
    if "600000" not in c or "1200000" not in c:
        return None
    if re.search(r"Monthly Salary", c, re.I) and re.search(r"Annual Tax", c, re.I):
        return "example"
    if "1610000" in c and "45%" in c:
        return None  # correct non-salaried table
    if "29%" in c and "32%" in c and re.search(r"1200000\s*\S*\s*1%", c):
        return None  # already correct
    if re.search(r"\b(5|2\.5)%", c) or "Check Finance Act" in c or re.search(r"\b15%", c):
        return "salaried"
    return None


FILES = ["blogs/business-income-tax-pakistan-2026.html", "blogs/income-tax-on-salary-pakistan-2026.html", "blogs/income-tax-slab-pakistan-2026.html",
         "blogs/section-149-salary-tax-pakistan-2026.html", "blogs/tax-on-salary-pakistan-2026.html", "guides/finance-act-2026-pakistan-summary.html",
         "amazon-seller-tax-pakistan.html", "blogs/how-to-file-income-tax-return-pakistan-2026.html", "blogs/salary-person-tax-return-pakistan.html",
         "payoneer-tax-pakistan.html", "upwork-income-tax-pakistan.html", "blogs/budget-2026-27-salary-tax-slabs-pakistan.html",
         "blogs/finance-act-2026-pakistan-tax-changes.html", "ur/guides/finance-act-2026-pakistan-summary.html", "tools/income-tax-calculator-pakistan.html",
         "salaried-person-tax-return-pakistan.html", "blogs/salary-tax-calculator-pakistan-2026.html", "tax-filing-doctors-pakistan.html", "blogs/wht-rate-card-2026-27-pakistan.html"]
BUSINESS_PAGES = {"blogs/business-income-tax-pakistan-2026.html"}
TEXT = [(r"Income Tax Slabs for Salaried Individuals — Tax Year 2025 Rates", "Income Tax Slabs for Salaried Individuals — Tax Year 2027 and 2026 Rates")]


def budget_table():
    rows, lo = [], 0
    for hi, _, _ in SAL27:
        rng = (f"Up to {f(hi)}" if lo == 0 else (f"{f(lo + 1)} to {f(hi)}" if hi else f"Above {f(lo)}"))
        a, b = desc(SAL26, lo), desc(SAL27, lo)
        rows.append(f"<tr><td>{rng}</td><td>{a}</td><td>{b}</td></tr>")
        lo = hi or lo
    return ('<table class="data-table"><thead><tr><th>Annual income (Rs)</th><th>Tax Year 2026</th><th>Tax Year 2027</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table><p>The biggest cuts are in the Rs 2.2 million to Rs 7 million bands, and the top 35% rate now starts above Rs 7 million instead of Rs 4.1 million. Source: <a href="https://www.fbr.gov.pk/" rel="noopener">FBR</a>, Finance Act 2026.</p>')


def main():
    os.chdir(ROOT)
    changed = []
    for fn in FILES:
        t = open(fn, encoding="utf-8").read()
        n = t

        def rep(m):
            tb = m.group(0)
            k = classify(tb)
            if fn.endswith("budget-2026-27-salary-tax-slabs-pakistan.html") and "TY2027" in cells(tb):
                return budget_table()
            if k == "example":
                if "(TY2027)" in tb:
                    return tb
                monthly = []
                for r in re.findall(r"<tr.*?</tr>", tb, re.S):
                    m1 = re.search(r"<td[^>]*>\s*(?:Rs\.?|PKR)?\s*([\d,]+)\s*</td>", r)
                    if m1:
                        monthly.append(int(m1.group(1).replace(",", "")))
                return example_table(monthly) if monthly else tb
            if k == "salaried":
                if fn.endswith("wht-rate-card-2026-27-pakistan.html"):
                    return sal_table_compact()
                return bus_table() if fn in BUSINESS_PAGES else sal_table(urdu=fn.startswith("ur/"))
            return tb
        n = re.sub(r"<table.*?</table>", rep, n, flags=re.S)
        if fn == "tools/income-tax-calculator-pakistan.html":
            n = re.sub(r"BUSINESS_SLABS:\s*\[.*?\]", "BUSINESS_SLABS: [ {min:0, max:600000, fixed:0, rate:0}, {min:600001, max:1200000, fixed:0, rate:0.15}, "
                       "{min:1200001, max:1600000, fixed:90000, rate:0.20}, {min:1600001, max:3200000, fixed:170000, rate:0.30}, "
                       "{min:3200001, max:5600000, fixed:650000, rate:0.40}, {min:5600001, max:Infinity, fixed:1610000, rate:0.45} ]", n, count=1, flags=re.S)
            n = n.replace("calcSlabs(normalIncome,TAX_CONFIG.SALARIED_SLABS)", "calcSlabs(normalIncome,TAX_CONFIG.BUSINESS_SLABS)")
            if "SURCHARGE_10M" not in n:
                n = n.replace("result=calcSlabs(income,slabs);\n", "result=calcSlabs(income,slabs); if(type!=='salaried'&&income>10000000){result.tax*=1.10; /*SURCHARGE_10M*/ result.rows.push({range:'Surcharge (income above Rs 10m)',taxable:'',rate:'10% of tax',tax:fmt(result.tax/11)});}\n", 1)
        for a, b in TEXT:
            n = re.sub(a, b, n)
        if n != t:
            open(fn, "w", encoding="utf-8").write(n)
            changed.append(fn)
    print("changed", len(changed), changed)


if __name__ == "__main__":
    main()
