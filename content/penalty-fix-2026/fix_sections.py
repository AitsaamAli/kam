#!/usr/bin/env python3
"""Rewrite the passages that teach a wrong late-filing penalty method (checked 1 November 2026). Each pair must match."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
S = 'style="padding:9px 14px;border:1px solid #E2E8F0"'

FIX = {
"blogs/late-income-tax-return-pakistan-2026.html": [
 ("Missing the 30 September deadline triggers Rs.&nbsp;1,000 per day penalty under Section 182 &mdash; penalties start accruing from 1 October",
  "Missing the due date exposes you to a Section 182 penalty of 0.1% of tax payable per day &mdash; minimum Rs.&nbsp;40,000, or Rs.&nbsp;5,000 for most salaried individuals"),
 ("and a Rs.&nbsp;1,000 per day penalty begins accruing the moment the deadline passes.",
  "and a Section 182 penalty, worked out at 0.1% of tax payable for each day of delay, becomes possible the moment the deadline passes."),
 ("<strong>Penalty under Section 182 starts immediately.</strong> From 1 October onwards, a penalty of Rs.&nbsp;1,000 per day accrues on your account for every day you have not filed. This is not a one-time flat penalty &mdash; it is a daily accumulating charge. The total penalty is capped at 50% of your total tax payable for the year (with a minimum of Rs.&nbsp;1,000 even for nil-tax returns). On a nil return with zero tax due, the minimum penalty is Rs.&nbsp;1,000. On a return with Rs.&nbsp;100,000 tax due, the maximum penalty is Rs.&nbsp;50,000 &mdash; reached after 50 days late.",
  "<strong>A Section 182 penalty becomes possible immediately.</strong> As published on FBR&rsquo;s website, the penalty for not filing by the due date is 0.1% of the tax payable for the year for each day of default, capped at 50% of the tax payable. If that works out below Rs.&nbsp;40,000, or no tax is payable at all, the penalty is Rs.&nbsp;40,000. Where at least 75% of your income is salary and the salary is below Rs.&nbsp;5 million, the minimum is Rs.&nbsp;5,000 instead. &ldquo;Tax payable&rdquo; means the tax chargeable for the year, not only the unpaid balance. The penalty is imposed by an order of the tax officer, normally after a notice that gives you a chance to explain."),
 ("The key difference is that IRIS will flag the return as late and in many cases automatically calculate the late filing penalty based on the number of days elapsed since the deadline. Here is the complete process:",
  "The difference is what follows: the return is recorded as late, a Section 182 penalty can be imposed later by order, and ATL inclusion needs the Section 182A surcharge. Here is the complete process:"),
 ("<strong>Step 4: IRIS calculates the penalty.</strong> In most cases, IRIS will automatically calculate the Section 182 late filing penalty based on the date of filing minus 30 September. Review this calculation carefully. For nil returns, the minimum Rs.&nbsp;1,000 penalty applies. For returns with tax due, confirm that the penalty displayed does not exceed 50% of your total tax liability.",
  "<strong>Step 4: Check the figures before you submit.</strong> Make sure income, tax deducted at source and the wealth statement reconcile. Pay any balance tax through a payment slip (PSID) before submitting. The Section 182 penalty is not a fee IRIS adds at submission; if it is imposed, it comes later through a notice and an order, which you can answer."),
 ("The system will generate separate PSIDs for: (a) any balance tax due, (b) the late filing penalty, and if applicable (c) the ATL surcharge. Pay all three through your bank, internet banking, or mobile banking app using the respective PSIDs.",
  "Pay any balance tax and, if you want ATL status, the Section 182A surcharge through PSIDs generated in IRIS, using your bank, internet banking or mobile banking app."),
 ("<tr><td>Nil return (no tax due)</td><td>30</td><td>Rs. 0</td><td>Minimum Rs. 1,000 flat</td><td>Rs. 1,000</td></tr>\n<tr><td>Small return (Rs. 20,000 tax)</td><td>45</td><td>Rs. 20,000</td><td>Rs. 1,000 &times; 45 = Rs. 45,000 &rarr; capped at 50% of Rs. 20,000 = Rs. 10,000</td><td>Rs. 10,000</td></tr>\n<tr><td>Medium return (Rs. 50,000 tax)</td><td>60</td><td>Rs. 50,000</td><td>Rs. 1,000 &times; 60 = Rs. 60,000 &rarr; capped at 50% of Rs. 50,000 = Rs. 25,000</td><td>Rs. 25,000</td></tr>\n<tr><td>Larger return (Rs. 200,000 tax)</td><td>90</td><td>Rs. 200,000</td><td>Rs. 1,000 &times; 90 = Rs. 90,000 &rarr; below 50% cap of Rs. 100,000</td><td>Rs. 90,000</td></tr>",
  "<tr><td>Salaried, nil tax (salary under Rs. 5 million)</td><td>30</td><td>Rs. 0</td><td>No tax payable &rarr; salaried minimum</td><td>Rs. 5,000</td></tr>\n<tr><td>Salaried (salary under Rs. 5 million)</td><td>60</td><td>Rs. 150,000</td><td>0.1% &times; 150,000 &times; 60 = Rs. 9,000</td><td>Rs. 9,000</td></tr>\n<tr><td>Shopkeeper or freelancer</td><td>45</td><td>Rs. 200,000</td><td>0.1% &times; 200,000 &times; 45 = Rs. 9,000 &rarr; below Rs. 40,000 minimum</td><td>Rs. 40,000</td></tr>\n<tr><td>Business with larger tax</td><td>90</td><td>Rs. 1,000,000</td><td>0.1% &times; 1,000,000 &times; 90 = Rs. 90,000 (cap is 50% = Rs. 500,000)</td><td>Rs. 90,000</td></tr>"),
 ("Several observations from these examples are worth noting. First, for nil-tax filers the penalty is effectively minimal (Rs.&nbsp;1,000) regardless of how late you are &mdash; FBR's system applies the minimum because there is no tax against which to compute 50%. Second, for taxpayers with moderate tax liabilities, the 50% cap kicks in fairly quickly &mdash; within 25 to 50 days &mdash; meaning the penalty stops growing after that point even if you continue to delay. Third, for high-tax-liability filers, the cap provides meaningful protection: on Rs.&nbsp;500,000 tax due, the penalty cannot exc",
  "Several observations from these examples are worth noting. First, the minimum matters most: for non-salaried filers with modest tax, the Rs.&nbsp;40,000 floor applies whether you are a few days or a few months late, while most salaried filers face a Rs.&nbsp;5,000 floor. Second, the 0.1% daily rate only overtakes the minimum when tax payable is large or the delay is long. Third, the 50% cap is reached only after 500 days, so for practical purposes it protects only very late filers: on Rs.&nbsp;500,000 tax due, the penalty cannot exc"),
 ("The penalty accumulates every single day until you file. There is no grace period after the deadline, no informal tolerance period, and no exemption based on lack of knowledge. The obligation is objective, and the penalty accrues automatically in FBR's system.",
  "The daily count runs until you file. There is no grace period after the deadline and no exemption based on lack of knowledge, although the penalty is imposed by an order after a notice, where a genuine, documented reason for the delay can be explained."),
 ("A late-filed return with a Rs.&nbsp;1,000 per day penalty (capped at 50% of tax due)",
  "A late-filed return with a Section 182 penalty"),
 ("The Section 182 penalty is automatic and accrues without any specific action by FBR. However, the law does provide a mechanism for penalty waiver or reduction in genuine hardship cases. Understanding when and how to seek a waiver is important for taxpayers who have missed the deadline due to circumstances beyond their control.",
  "The Section 182 penalty is imposed by an order of the tax officer, normally after a show-cause notice. That notice is your opportunity: a taxpayer who missed the deadline because of circumstances beyond their control can explain the reason with evidence before any order is made."),
 ("<strong>Section 214A &mdash; Waiver or Reduction of Penalty.</strong> Under Section 214A of the Income Tax Ordinance, the commissioner of inland revenue has the discretion to waive or reduce any penalty if the taxpayer demonstrates \"reasonable cause\" for the default. The law does not exhaustively define \"reasonable cause,\" but FBR's practice and case law have established certain grounds that are consistently accepted:",
  "<strong>Explaining a genuine reason.</strong> Section 214A is the power FBR uses to extend filing dates for everyone, as it did in October 2026; it is not an individual penalty waiver. For your own case, the route is a well-documented reply to the penalty notice, and if an order is still made, an appeal to the Commissioner (Appeals) under Section 127. Reasons that are commonly put forward include:"),
 ("cite Section 214A as the legal basis for the waiver request.", "and ask that no penalty be imposed in view of the documented reason."),
 ("Even if a full waiver is not granted, a partial reduction is common. FBR commissioners often reduce the penalty by 50% to 75% in cases where genuine cause is demonstrated and the return is filed promptly after the cause resolves. This makes the waiver application a worthwhile exercise even when you are not certain of full success.",
  "There is no guaranteed outcome. Each case depends on the evidence and on the officer or appellate authority deciding it. What reliably helps is filing promptly once the cause is resolved and keeping records of why the delay happened."),
 ("(Rs.&nbsp;1,000 for individuals, Rs.&nbsp;10,000 for AOPs, Rs.&nbsp;20,000 for companies)",
  "(Rs.&nbsp;25,000 for individuals, Rs.&nbsp;50,000 for AOPs, Rs.&nbsp;100,000 for companies, from 1 July 2026)"),
 ("The penalty accrues automatically regardless of whether FBR issues a notice &mdash; there is no \"notice required\" condition for the penalty to apply.",
  "The Section 182 penalty is imposed by an order, normally after a notice, but the exposure exists from the day after the due date."),
],
"blogs/fbr-penalty-pakistan-2026.html": [
 (f'<tr><td {S}>Salaried individual (salary only income)</td><td {S}>Rs. 1,000</td><td {S}>Rs. 50,000</td></tr>',
  f'<tr><td {S}>Salaried individual (75%+ income from salary, salary under Rs. 5 million)</td><td {S}>0.1% of tax payable per day (minimum Rs. 5,000)</td><td {S}>50% of tax payable</td></tr>'),
 (f'<tr><td {S}>Company</td><td {S}>Rs. 2,500 per day</td><td {S}>25% of tax payable</td></tr>',
  f'<tr><td {S}>Company</td><td {S}>0.1% of tax payable per day (minimum Rs. 40,000)</td><td {S}>50% of tax payable</td></tr>'),
 ("Ahmad is a salaried employee whose return was due 30 September 2026 but he filed on 15 October 2026 — 15 days late. Penalty = Rs. 1,000 × 15 days = Rs. 15,000 (well below the Rs. 50,000 cap). Even if he filed 6 months late, the maximum penalty is capped at Rs. 50,000.",
  "Ahmad is a salaried employee (salary Rs. 2.4 million, tax payable Rs. 120,000) who filed 30 days after the due date. Formula: 0.1% × Rs. 120,000 × 30 = Rs. 3,600. That is below the salaried minimum, so the penalty works out to Rs. 5,000. To rejoin the ATL he also pays the Rs. 25,000 Section 182A surcharge."),
 ("at Rs. 2,500 per day (capped at 25% of tax payable).", "at 0.1% of tax payable per day, capped at 50% of tax payable, with a minimum of Rs. 40,000."),
 ("The penalty rate for companies is Rs. 2,500 per day (capped at 25% of tax payable).", "The rate is 0.1% of tax payable per day, capped at 50% of tax payable, with a minimum of Rs. 40,000."),
],
"blogs/fbr-income-tax-return-deadline-2026-pakistan.html": [
 ("more than 22 times the Rs. 1,000 monthly filing penalty.", "and that is before any Section 182 penalty or the Rs. 25,000 ATL surcharge."),
 ("<strong>&ldquo;The penalty is just Rs. 1,000 &mdash; not worth rushing.&rdquo;</strong>", "<strong>&ldquo;The penalty is small &mdash; not worth rushing.&rdquo;</strong> It is not small: the minimum is Rs. 40,000 (Rs. 5,000 for most salaried), plus Rs. 25,000 to rejoin the ATL."),
],
"blogs/filer-vs-non-filer-pakistan-2026.html": [
 ("<strong>Late return:</strong> Rs 1,000 penalty lagti hai — lekin file karo zaroor, status wapas milta hai",
  "<strong>Late return:</strong> Section 182 penalty (kam az kam Rs 40,000, zyada tar salaried ke liye Rs 5,000) aur ATL ke liye Rs 25,000 surcharge — lekin file karo zaroor, status wapas milta hai"),
],
"income-tax-return-filing-cost-pakistan.html": [
 ("FBR ki taraf se late filing penalty hoti hai — minimum Rs. 1,000 per quarter.", "FBR Section 182 ke tehat late filing penalty laga sakta hai — 0.1% of tax payable per day, kam az kam Rs. 40,000 (zyada tar salaried ke liye Rs. 5,000) — aur ATL ke liye Rs. 25,000 surcharge alag hai."),
 ("FBR ki taraf se late filing penalty hoti hai &mdash; minimum Rs. 1,000 per quarter.", "FBR Section 182 ke tehat late filing penalty laga sakta hai &mdash; 0.1% of tax payable per day, kam az kam Rs. 40,000 (zyada tar salaried ke liye Rs. 5,000) &mdash; aur ATL ke liye Rs. 25,000 surcharge alag hai."),
],
}
for f in ["tax-filing-exporters-pakistan.html", "shopify-seller-tax-pakistan.html", "software-house-tax-pakistan.html",
          "digital-marketing-agency-tax-pakistan.html", "tax-filing-traders-pakistan.html"]:
    FIX[f] = [('<td style="padding:8px">Rs.1,000-10,000/month</td>', '<td style="padding:8px">0.1% of tax payable/day (min. Rs.40,000; Rs.5,000 for most salaried)</td>')]


def main():
    os.chdir(ROOT)
    missing = []
    for f, pairs in FIX.items():
        t = open(f, encoding="utf-8").read()
        for old, new in pairs:
            hits = t.count(old) + t.count(old.replace('"', '\\"'))
            if not hits:
                missing.append((f, old[:90]))
                continue
            t = t.replace(old, new).replace(old.replace('"', '\\"'), new.replace('"', '\\"'))
        open(f, "w", encoding="utf-8").write(t)
    print("missing:", missing or "NONE")


if __name__ == "__main__":
    main()
