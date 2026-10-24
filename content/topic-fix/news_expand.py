#!/usr/bin/env python3
"""Adds topic-specific sections to the five short news posts and lists all of them on /news.

The posts were 120-245 words each, two pairs covered the same subject, and three were not linked from
anywhere. Each post gets its own angle; figures are limited to those confirmed for 2026-27.
Usage: python3 content/topic-fix/news_expand.py   (idempotent: skips posts already expanded)
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MARK = '<div class="news-more">'
MARK2 = '<div class="news-more2">'

ADD = {
"finance-act-2026-passed": """
<h2>How the Finance Act Becomes Law</h2>
<p>The budget is presented as a Finance Bill in June. The National Assembly debates it, may amend it, and passes it before the new fiscal year; the Senate makes recommendations, and once assented the bill becomes the Finance Act. Its income tax provisions generally apply from 1 July, the first day of the new tax year. Changes made during the debate mean that figures quoted on budget day are not always the figures that become law, which is why we wait for the enacted text before updating calculators and guides.</p>
<h2>Dates That Follow the Act</h2>
<ul><li><strong>1 July 2026:</strong> new withholding rates start applying to payments and transfers.</li>
<li><strong>July:</strong> FBR issues explanatory circulars and its Withholding Tax Regime Card for the year.</li>
<li><strong>From 1 July 2026:</strong> property buyers pay advance tax under section 236K at 1.25% (on the Active Taxpayers List) or 2.5% (others); sellers pay 2.75% or 5.5% under section 236C.</li></ul>
<h2>What Employers Should Do First</h2>
<p>Payroll teams should load the new salaried slabs from the July payroll, re-estimate each employee's annual tax, and spread any difference over the remaining months. Employees can ask HR for the revised monthly deduction in writing.</p>
""",
"finance-act-2026-key-changes": """
<h2>Who Should Act on the Changes</h2>
<ul><li><strong>Salaried employees:</strong> check that July payslips use the new slabs; claim any over-deduction in your return.</li>
<li><strong>Property buyers and sellers:</strong> for transfers from 1 July 2026, advance tax is 1.25% or 2.5% for buyers and 2.75% or 5.5% for sellers, depending on Active Taxpayers List status.</li>
<li><strong>Online sellers:</strong> tax collected on digital payments (1%) and cash-on-delivery orders (2%) is an advance payment you can claim only by filing.</li>
<li><strong>Non-filers:</strong> the gap on everyday transactions keeps widening, so filing this year is the cheapest fix.</li></ul>
<h2>Capital Gains: Acquisition Date Matters</h2>
<p>Gains on property bought from 1 July 2024 are generally taxed at a flat rate for active filers regardless of holding period, while older purchases follow earlier holding-period rules. Check the acquisition date on your deed before estimating the tax on a sale.</p>
<h2>Questions We Are Hearing</h2>
<p>Most questions this season are about whether a deal registered in early July falls under the new property rates (it generally follows the registration date) and whether last year's slabs still apply to the return due on 30 September 2026 (they do not; that return is for tax year 2026).</p>
""",
"income-tax-return-deadline-2026": """
<h2>Deadline by Taxpayer Type</h2>
<table><thead><tr><th>Taxpayer</th><th>Return for tax year 2026 due</th></tr></thead><tbody>
<tr><td>Salaried individuals</td><td>30 September 2026</td></tr>
<tr><td>Business individuals and AOPs</td><td>30 September 2026</td></tr>
<tr><td>Companies with a 30 June year end</td><td>31 December 2026</td></tr>
<tr><td>Companies with a special tax year</td><td>Within the period set in section 118 after their year end</td></tr></tbody></table>
<h2>If You Cannot Make It</h2>
<p>An individual extension can be requested from your Commissioner under section 119, but the application must be made before the due date. A general extension, when FBR grants one, is announced by an official notification; rumours on social media are not enough to rely on. After the deadline, a late return still puts you back on the Active Taxpayers List once the ATL surcharge is paid.</p>
""",
"return-filing-season-2026": """
<h2>A Four-Week Filing Plan</h2>
<ol><li><strong>Week 1:</strong> download salary certificates, bank tax deduction certificates and property or vehicle tax receipts for 1 July 2025 &ndash; 30 June 2026.</li>
<li><strong>Week 2:</strong> list your assets and liabilities at 30 June 2026 and note any purchase, sale or gift during the year.</li>
<li><strong>Week 3:</strong> prepare the return and wealth statement on IRIS, or send the documents to your consultant.</li>
<li><strong>Week 4:</strong> review, submit with the PIN, pay any balance through a PSID and download the acknowledgement.</li></ol>
<h2>Common First-Week Problems</h2>
<p>Forgotten IRIS passwords, a mobile number that no longer works, and salary certificates that employers have not yet issued are the most common reasons people end up filing in the last week. Fix the login first: password resets need access to the registered mobile number and email.</p>
<p>Our salaried return service is Rs 3,500 and NTN registration Rs 2,000, as listed on the <a href="/pricing">pricing page</a>.</p>
""",
"active-taxpayer-list-atl-update-2026": """
<h2>When the List Changes</h2>
<p>The Active Taxpayers List for income tax is published each year on 1 March, based on returns filed for the previous tax year. People who file late are added after paying the ATL surcharge, so their names can appear between annual updates. Sales tax has its own separate active list based on monthly returns.</p>
<h2>What Changes for You Once Listed</h2>
<table><thead><tr><th>Transaction</th><th>On the list</th><th>Not on the list</th></tr></thead><tbody>
<tr><td>Buying property (236K, from 1 July 2026)</td><td>1.25%</td><td>2.5%</td></tr>
<tr><td>Selling property (236C, from 1 July 2026)</td><td>2.75%</td><td>5.5%</td></tr>
<tr><td>Prize bond winnings</td><td>15%</td><td>30%</td></tr></tbody></table>
<p>Before a large transaction, check your status on the day and keep a screenshot, because banks and registrars check the list on the transaction date.</p>
""",
}

MORE = {'finance-act-2026-passed': "<h2>Reading Budget Coverage Carefully</h2>\n<p>Budget-day headlines often mix proposals that were later dropped with measures that survived. Three checks help: confirm the measure appears in the enacted Finance Act, note its start date, and look for FBR's explanatory circular, which usually follows within weeks. Until then, treat figures shared on WhatsApp groups as unconfirmed. Our guides are updated only after the enacted text and circulars are available, and each one shows the date it was last reviewed so you can see whether it reflects the final law.</p>\n<p>If a change affects a transaction you are about to make, such as a property transfer or a large bank withdrawal, check the rate that applies on the transaction date rather than the date you agreed the deal.</p>\n", 'finance-act-2026-key-changes': '<h2>A Simple Checklist for July</h2>\n<ul><li>Confirm your name on the Active Taxpayers List before any large purchase.</li><li>Ask your employer for the revised monthly tax deduction.</li><li>Save courier and payment-gateway statements if you sell online.</li><li>Note acquisition dates of any property you may sell this year.</li></ul>\n', 'income-tax-return-deadline-2026': '<h2>What the Return for Tax Year 2026 Covers</h2>\n<p>The return due on 30 September 2026 covers income earned from 1 July 2025 to 30 June 2026, together with the wealth statement showing assets and liabilities on 30 June 2026. Salary certificates, bank tax certificates and property documents should all relate to that period. Mixing up tax years is one of the most common reasons returns are rejected or amended later.</p>\n', 'return-filing-season-2026': "<h2>Documents Checklist</h2>\n<table><thead><tr><th>If you have</th><th>Keep ready</th></tr></thead><tbody>\n<tr><td>Salary</td><td>Employer's salary and tax deduction certificate</td></tr>\n<tr><td>Bank accounts</td><td>Profit and tax deduction certificates, statements for 30 June</td></tr>\n<tr><td>Property</td><td>Registry or allotment papers, advance tax receipts, rent agreements</td></tr>\n<tr><td>Vehicle</td><td>Registration book and token tax receipts</td></tr>\n<tr><td>Freelance or business income</td><td>Platform statements, invoices and expense records</td></tr></tbody></table>\n<p>Filing early also gives time to fix problems, such as a missing certificate or a wrong CNIC on a bank record, before the deadline.</p>\n", 'active-taxpayer-list-atl-update-2026': "<h2>If Your Name Is Missing</h2>\n<p>If you filed but cannot find your name, check that the return was submitted (not saved as a draft), that it was for the correct tax year, and, for a late return, that the ATL surcharge was paid. Then raise the issue through FBR's facilitation channel with your acknowledgement and payment receipt.</p>\n"}

FIX = [("From Rs. 2,500.", "From Rs. 2,000 for NTN registration."), ("Filing from Rs. 2,500.", "Filing from Rs. 3,500."),
       ("FBR-certified consultants.", "Experienced tax consultants."),
       ("plus capital gains tax that tapers with holding period", "plus capital gains tax whose rate depends on when the property was acquired")]

CARDS = [("active-taxpayer-list-atl-update-2026", "ATL", "Active Taxpayer List 2026: Check and Stay Listed",
          "How the list is updated and what changes once your name appears.", "15 June 2026"),
         ("finance-act-2026-key-changes", "Finance Act", "Finance Act 2026: Who Should Act",
          "Practical changes for employees, property buyers, online sellers and non-filers.", "18 June 2026"),
         ("income-tax-return-deadline-2026", "Deadline", "Return Deadlines for Tax Year 2026",
          "Due dates by taxpayer type and what to do if you cannot make them.", "20 June 2026")]


def main():
    for slug, html in ADD.items():
        f = os.path.join(ROOT, "news", slug + ".html")
        h = open(f, encoding="utf-8-sig").read()
        for a, b in FIX:
            h = h.replace(a, b)
        if MARK2 not in h and MARK in h:
            h = h.replace(MARK, MARK + '<div class="news-more2"></div>' + MORE[slug], 1)
        if MARK not in h:
            i = h.index("</article>")
            et = h.rfind('<div class="expert-take">', 0, i)
            at = et if et != -1 else i
            h = h[:at] + MARK + '<div class="news-more2"></div>' + MORE[slug] + html + "</div>" + h[at:]
        open(f, "w", encoding="utf-8").write(h)
        print("expanded", slug)
    f = os.path.join(ROOT, "news", "index.html")
    h = open(f, encoding="utf-8-sig").read()
    for slug, tag, title, desc, date in CARDS:
        if f"/news/{slug}" in h:
            continue
        card = (f'<div class="news-card"><span class="news-tag"><i class="fas fa-bolt"></i> {tag}</span>'
                f'<h3><a href="/news/{slug}" style="color:inherit">{title}</a></h3><p>{desc}</p>'
                f'<div style="font-size:.78rem;color:var(--text-4)"><i class="fas fa-calendar"></i> {date}</div>'
                f'<a href="/news/{slug}" style="display:inline-block;margin-top:14px;color:#14B8A6;font-weight:600;font-size:.85rem">'
                f'Read more <i class="fas fa-arrow-right"></i></a></div>')
        h = re.sub(r'(<div class="news-grid">)', lambda m: m.group(1) + card, h, count=1)
    open(f, "w", encoding="utf-8").write(h)


if __name__ == "__main__":
    main()
