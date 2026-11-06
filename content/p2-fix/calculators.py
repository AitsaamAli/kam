#!/usr/bin/env python3
"""P2 fix (6 Nov 2026): repair the four root calculators and business-advisory.

Found: the calculators' buttons called functions that did not exist and their CSS was missing, the slab table
showed wrong rates (5/15/25%), the pages said 2025-26, and all five shared a generic 'About / Key facts / FAQ'
block. This script adds a working engine (Tax Year 2027 rates), page CSS, a correct slab table, page-specific
content and FAQs (JSON-LD rebuilt to match), and replaces unsupported claims.

Rates, Tax Year 2027 (Finance Act 2026): salaried slabs as below; non-salaried slabs unchanged from TY2026,
with a 10% surcharge on tax where taxable income exceeds Rs 10 million. Sources: FBR, Finance Act 2026 reporting.
Usage: python3 content/p2-fix/calculators.py
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "content", "p1-fix"))
from rebuild import unmatched_closers, update_ld  # noqa: E402

SAL = [(600000, 0, 0), (1200000, 0, .01), (2200000, 6000, .11), (3200000, 116000, .20), (4100000, 316000, .25),
       (5600000, 541000, .29), (7000000, 976000, .32), (None, 1424000, .35)]
BUS = [(600000, 0, 0), (1200000, 0, .15), (1600000, 90000, .20), (3200000, 170000, .30), (5600000, 650000, .40), (None, 1610000, .45)]

ENGINE = """<script id="calc-engine">
(function(){
var SAL=%s, BUS=%s, MIN_WAGE=40000;
function slabTax(x,S){var lo=0;for(var i=0;i<S.length;i++){var hi=S[i][0];if(hi===null||x<=hi){return S[i][1]+(x-lo)*S[i][2];}lo=hi;}return 0;}
function band(x,S){var lo=0;for(var i=0;i<S.length;i++){var hi=S[i][0];if(hi===null||x<=hi){return (S[i][2]*100).toFixed(0)+'%% slab';}lo=hi;}return '';}
function rs(n){return 'Rs. '+Math.round(n).toLocaleString('en-PK');}
function num(id){var e=document.getElementById(id);return e?Math.max(0,parseFloat(e.value)||0):0;}
function set(id,v){var e=document.getElementById(id);if(e)e.textContent=v;}
function show(id){var e=document.getElementById(id);if(e){e.style.display='block';e.scrollIntoView({behavior:'smooth',block:'nearest'});}}
function incomeTax(x,type){var t=type==='business'?slabTax(x,BUS):slabTax(x,SAL);if(type==='business'&&x>10000000)t*=1.10;return t;}
window.calculateTax=function(){var a=num('annualIncome');var m=num('monthlySalary');if(!a&&m)a=m*12;if(!a){alert('Please enter your annual income or monthly salary.');return;}
var type=(document.getElementById('taxpayerType')||{}).value||'salaried';var t=incomeTax(a,type);
set('res-income',rs(a));set('res-monthly',rs(a/12));set('res-bracket',band(a,type==='business'?BUS:SAL)+(type==='business'&&a>10000000?' + 10%% surcharge':''));
set('res-tax',rs(t));set('res-monthly-tax',rs(t/12));set('res-rate',(a?t/a*100:0).toFixed(2)+'%%');set('res-net',rs(a-t));
set('res-note',type==='business'?'Non-salaried slabs for Tax Year 2027. A 10%% surcharge on tax applies where taxable income exceeds Rs 10 million.':'Salaried slabs for Tax Year 2027 (July 2026 to June 2027), applied where salary is more than 75%% of taxable income.');show('taxResult');};
window.calcSalary=function(){var g=num('grossSalary');if(!g){alert('Please enter your monthly gross salary.');return;}
var ann=g*12,t=slabTax(ann,SAL),eobi=((document.getElementById('eobiStatus')||{}).value==='yes')?MIN_WAGE*0.01:0,pf=g*(parseFloat((document.getElementById('pfStatus')||{}).value)||0)/100,ded=t/12+eobi+pf;
set('s-gross',rs(g));set('s-annual',rs(ann));set('s-tax',rs(t/12)+' a month');set('s-eobi',rs(eobi));set('s-pf',rs(pf));set('s-deductions',rs(ded));set('s-net',rs(g-ded));set('s-net-annual',rs((g-ded)*12));show('salaryResult');};
window.estimateIncome=function(){var s=num('e-salary'),b=num('e-business'),r=num('e-rental'),o=num('e-other'),p=num('e-paid'),tot=s+b+r+o;if(!tot){alert('Please enter at least one income.');return;}
var type=s>0.75*tot?'salaried':'business',t=incomeTax(tot,type);
set('ei-salary',rs(s));set('ei-business',rs(b));set('ei-rental',rs(r));set('ei-other',rs(o));set('ei-total',rs(tot));set('ei-tax',rs(t));set('ei-paid',rs(p));set('ei-rate',(t/tot*100).toFixed(2)+'%%');
var bal=t-p;set('ei-balance',bal>=0?rs(bal)+' payable':rs(-bal)+' refundable (subject to FBR verification)');
set('ei-note',(type==='salaried'?'Salary is more than 75%% of your income, so salaried slabs apply to the total. ':'Salary is 75%% or less of your income, so non-salaried slabs apply. ')+'Rental and some other income can be taxed under separate rules for your case; treat this as an estimate and confirm before filing.');show('estimateResult');};
window.calcGST=function(){var a=num('gstAmount');if(!a){alert('Please enter an amount.');return;}var rv=(document.getElementById('gstRate')||{}).value;var r=(rv==='custom'?num('customRate'):parseFloat(rv)||0)/100;
var add=((document.getElementById('gstType')||{}).value||'add')==='add',pre=add?a:a/(1+r),tax=pre*r;
set('g-original',rs(a));set('g-rate',(r*100).toFixed(2)+'%%');set('g-tax',rs(tax));set('g-pretax',rs(pre));set('g-total',rs(pre+tax));show('gstResult');};
var gr=document.getElementById('gstRate');if(gr){gr.addEventListener('change',function(){var c=document.getElementById('customRateField');if(c)c.style.display=gr.value==='custom'?'block':'none';});}
})();
</script>""" % (json.dumps(SAL), json.dumps(BUS))

CSS = """<style id="calc-css">
.calc-layout{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:24px;align-items:start}
.calc-card,.slab-box{background:#fff;border:1px solid #E2E8F0;border-top:3px solid #14B8A6;border-radius:14px;padding:24px;box-shadow:0 6px 24px rgba(15,23,42,.06)}
.calc-card h2,.calc-card h3{margin:0 0 6px}.calc-desc{color:#475569;font-size:.92rem;margin:0 0 16px}
.calc-field{margin-bottom:14px}.calc-field label{display:block;font-size:.84rem;font-weight:600;color:#0F172A;margin-bottom:6px}
.calc-input,.calc-select{width:100%;box-sizing:border-box;padding:11px 14px;border:1px solid #CBD5E1;border-radius:8px;font-size:.95rem;background:#F8FAFC}
.calc-input:focus,.calc-select:focus{outline:none;border-color:#14B8A6;box-shadow:0 0 0 3px rgba(20,184,166,.15)}
.calc-btn{width:100%;padding:13px;border:0;border-radius:10px;background:linear-gradient(135deg,#0F766E,#14B8A6);color:#fff;font-weight:700;font-size:1rem;cursor:pointer;margin-top:4px}
.calc-result{display:none;margin-top:20px;padding:18px;border:1px solid rgba(20,184,166,.3);border-radius:12px;background:rgba(20,184,166,.06)}
.result-title{font-weight:700;margin-bottom:10px;color:#0F172A}.result-row{display:flex;justify-content:space-between;gap:12px;padding:8px 0;border-bottom:1px dashed #E2E8F0;font-size:.92rem}
.result-value{font-weight:700;color:#0F172A;text-align:right}.result-value.teal{color:#0F766E}.result-note{font-size:.8rem;color:#64748B;margin-top:10px}
.slab-table{width:100%;border-collapse:collapse;font-size:.9rem}.slab-table th,.slab-table td{padding:8px 10px;border-bottom:1px solid #E2E8F0;text-align:left}.slab-table th{background:#F1F5F9}
@media(max-width:820px){.calc-layout{grid-template-columns:1fr}.calc-card,.slab-box{padding:18px}}
</style>"""


def rs(n):
    return f"{n:,.0f}"


def slab_table(S, label):
    rows, lo = [], 0
    for hi, fixed, rate in S:
        rng = f"Up to Rs {rs(hi)}" if lo == 0 else (f"Rs {rs(lo + 1)} to {rs(hi)}" if hi else f"Above Rs {rs(lo)}")
        tax = "0%" if rate == 0 else (f"{rate * 100:.0f}% of amount above Rs {rs(lo)}" if not fixed else f"Rs {rs(fixed)} + {rate * 100:.0f}% above Rs {rs(lo)}")
        rows.append(f"<tr><td>{rng}</td><td>{tax}</td></tr>")
        lo = hi or lo
    return f'<table class="slab-table"><thead><tr><th>Annual taxable income ({label})</th><th>Tax</th></tr></thead><tbody>{"".join(rows)}</tbody></table>'


DEADLINE = ("The Tax Year 2026 return deadline was extended to 31 October 2026 and has passed; late returns can still be filed on IRIS, "
            "with the Section 182 penalty (0.1% of tax per day, minimum Rs 40,000, or Rs 5,000 for low-salary cases) and the Section 182A "
            "surcharge of Rs 25,000 for individuals to join the Active Taxpayers List.")

PAGES = {
    "tax-calculator": dict(
        sections=[("How this calculator works",
                   "<p>Enter annual income, or monthly salary, and choose salaried or business. The calculator applies the Tax Year 2027 slabs from the Finance Act 2026: salaried slabs where salary is more than 75% of taxable income, and non-salaried slabs otherwise, with the 10% surcharge on tax where non-salaried income exceeds Rs 10 million. It shows annual and monthly tax, the effective rate and income after tax.</p>"),
                  ("Worked example",
                   "<p>A salaried person earning Rs 2,400,000 a year falls in the Rs 2,200,001 to 3,200,000 slab. Tax is Rs 116,000 plus 20% of Rs 200,000, which is Rs 156,000 a year, or Rs 13,000 a month: an effective rate of 6.5%. The same income from business is taxed at Rs 170,000 plus 30% of Rs 800,000, which is Rs 410,000.</p>"),
                  ("Non-salaried slabs, Tax Year 2027", slab_table(BUS, "non-salaried") + "<p>A 10% surcharge on tax applies where taxable income exceeds Rs 10 million.</p>"),
                  ("Deadlines", f"<p>{DEADLINE} The Tax Year 2027 return is due by 30 September 2027 unless FBR extends it.</p>")],
        faqs=[("Which slabs does this calculator use?", "Tax Year 2027 slabs from the Finance Act 2026: salaried slabs for salaried taxpayers and unchanged non-salaried slabs for business income, with a 10% surcharge above Rs 10 million for non-salaried taxpayers."),
              ("Is income up to Rs 600,000 tax-free?", "Yes. Taxable income up to Rs 600,000 a year is taxed at 0% under both salaried and non-salaried slabs."),
              ("Why is my business tax higher than salary tax on the same income?", "Non-salaried slabs are higher than salaried slabs, and the Finance Act 2026 cut salaried rates while leaving non-salaried rates unchanged."),
              ("Is the result my final tax?", "It is an estimate. Final tax depends on exempt income, tax credits, withholding already paid and your return. Check with FBR's IRIS calculation before filing.")]),
    "salary-calculator": dict(
        sections=[("How the take-home figure is worked out",
                   "<p>Your monthly gross salary is converted to an annual figure and taxed with the Tax Year 2027 salaried slabs. The monthly share of that tax, an optional EOBI employee contribution (1% of the notified minimum wage, taken here as Rs 40,000; check the current notification) and an optional provident fund deduction are subtracted to give monthly and annual take-home pay.</p>"),
                  ("Worked example",
                   "<p>On a gross salary of Rs 150,000 a month, annual salary is Rs 1,800,000. Tax is Rs 6,000 plus 11% of Rs 600,000, which is Rs 72,000 a year, or Rs 6,000 a month. With EOBI of Rs 400 and no provident fund, take-home pay is Rs 143,600 a month.</p>"),
                  ("Salaried slabs, Tax Year 2027", slab_table(SAL, "salaried")),
                  ("What can reduce salary tax", "<ul><li>Contributions to an approved pension fund can give a tax credit under the Ordinance.</li><li>Zakat deducted under the Zakat law is deductible from income.</li><li>Donations to approved institutions can give a tax credit.</li></ul><p>Limits and conditions apply; check them for your tax year.</p>")],
        faqs=[("How much tax is deducted from a Rs 100,000 monthly salary?", "Annual salary is Rs 1,200,000, so tax is 1% of Rs 600,000, which is Rs 6,000 a year, or Rs 500 a month, under the Tax Year 2027 salaried slabs."),
              ("Does my employer deduct tax every month?", "Yes. Employers deduct tax from salary each month under Section 149 based on estimated annual salary and deposit it with FBR."),
              ("Is EOBI deducted from salary?", "Where the employer is covered, the employee contributes 1% of the notified minimum wage each month and the employer 5%."),
              ("Do I still need to file a return if tax is deducted?", "Salaried people with taxable income should still file, so they stay on the Active Taxpayers List and pay lower withholding on other transactions.")]),
    "income-estimator": dict(
        sections=[("How the estimate is worked out",
                   "<p>Enter each type of income and the tax already deducted. If salary is more than 75% of the total, the salaried slabs are applied to all income; otherwise the non-salaried slabs apply, with the 10% surcharge on tax above Rs 10 million. Tax already paid is subtracted to show the balance payable or refundable.</p>"),
                  ("Freelancers and IT exporters",
                   "<p>Freelancers who receive foreign income through banks may have special tax treatment for export of services, depending on registration and how proceeds are received. This estimator uses normal slabs; check the current rules on FBR's website if you receive IT export proceeds.</p>"),
                  ("Rental income", "<p>Rent can be taxed under separate rules depending on your case, and the Finance Act 2026 removed the Section 7E tax on deemed income from property. Treat the rental part of the estimate as a guide only.</p>"),
                  ("Before you file", f"<p>{DEADLINE}</p>")],
        faqs=[("When do salaried slabs apply to all my income?", "When salary is more than 75% of taxable income, the salaried slabs are applied to the total taxable income."),
              ("Is there a surcharge on high business income?", "Yes. For non-salaried individuals and AOPs, a 10% surcharge on tax applies where taxable income exceeds Rs 10 million."),
              ("Does the estimate include tax already deducted?", "Yes. Enter tax deducted by employers, banks and others to see the balance payable or refundable."),
              ("Is the estimate final?", "No. Exempt income, separate-rule income and tax credits can change the result. Confirm figures in the return on IRIS.")]),
    "gst-calculator": dict(
        sections=[("How to use the sales tax calculator",
                   "<p>Choose whether to add sales tax to a price or remove it from a tax-inclusive total, enter the amount and pick the rate. Adding multiplies the price by the rate; removing divides the total by one plus the rate to find the price before tax.</p>"),
                  ("Worked example", "<p>A price of Rs 10,000 plus 18% sales tax is Rs 11,800. A tax-inclusive bill of Rs 11,800 contains Rs 1,800 of tax at 18%.</p>"),
                  ("Which rate applies", "<p>The standard federal sales tax rate on goods is 18%. Sales tax on services is charged by the provinces, such as the Punjab Revenue Authority, at rates set in each province's law. Reduced and zero rates apply to specified goods and exports; check the schedule for your item.</p>")],
        faqs=[("What is the standard sales tax rate in Pakistan?", "The standard federal sales tax rate on goods is 18%. Services are taxed by the provinces at their own rates."),
              ("How do I remove sales tax from a total?", "Divide the tax-inclusive total by one plus the rate. At 18%, Rs 11,800 divided by 1.18 is Rs 10,000 before tax."),
              ("Who charges sales tax on services?", "Provincial authorities: PRA in Punjab, SRB in Sindh, KPRA in Khyber Pakhtunkhwa and BRA in Balochistan."),
              ("Are exports charged sales tax?", "Exports of goods are generally zero-rated, which allows input tax to be reclaimed through the refund system.")]),
    "business-advisory": dict(
        sections=[("Choosing a business structure",
                   "<table><tr><th>Structure</th><th>Tax treatment</th><th>Suits</th></tr><tr><td>Sole proprietor</td><td>Owner taxed on business income at non-salaried slabs</td><td>Small, owner-run businesses</td></tr>"
                   "<tr><td>AOP (partnership)</td><td>AOP taxed as one unit; partners' shares are then generally exempt in their hands</td><td>Two or more partners</td></tr>"
                   "<tr><td>Private limited company</td><td>Company taxed at corporate rate; dividends taxed separately</td><td>Growing businesses, investors, limited liability</td></tr></table>"),
                  ("Lawful ways to manage tax", "<ul><li>Claim every allowable business expense with records.</li><li>Use tax credits the law allows, such as for approved pension contributions and donations.</li><li>Keep filer status so withholding stays at lower rates.</li><li>Time asset purchases and sales with their tax effect in mind.</li></ul>"),
                  ("Registrations a growing business may need", "<p>NTN with FBR, sales tax registration for goods, provincial registration for services, EOBI and social security for employees, and SECP if incorporating. Our <a href=\"/business-compliance-checklist-pakistan\">business compliance checklist</a> lists each one.</p>"),
                  ("How an advisory session works", "<p>We review your income, structure and filings, list the risks and options in writing, and quote any follow-up work before it starts. Office hours are Monday to Saturday, 9:00 AM to 6:00 PM, and Friday until 12:30 PM.</p>")],
        faqs=[("Should I run my business as a company or sole proprietor?", "It depends on size, partners, investors and liability. Companies pay corporate tax and file with SECP; sole proprietors pay non-salaried slabs with fewer filings."),
              ("How is an AOP taxed?", "The AOP is taxed as one unit on its income, and the partners' shares are then generally exempt in their hands."),
              ("What is legal tax planning?", "Using deductions, credits and structures the law allows, with proper records. It never involves hiding income or false documents."),
              ("Do you charge for an advisory session?", "We quote the fee in writing before any paid work starts.")]),
}

TEXT_FIX = [
    (r"Pakistan 2025[–-]26", "Pakistan 2026–27"), (r"Pakistan 2025(?=[^\d–-])", "Pakistan 2026–27"),
    (r"Tax Calculation Result — TY 2025-26", "Tax Calculation Result, Tax Year 2027"),
    (r"FBR Tax Slabs 2025-26 \(Salaried\)", "FBR Salaried Tax Slabs, Tax Year 2027"),
    (r"for Tax Year 2026\.", "for Tax Year 2027 (July 2026 to June 2027)."),
    (r"File your return in 24 hours", "Return checked before you submit"),
    (r"Starting from PKR 2,500", 'Fees on our <a href="/pricing">pricing page</a>'),
    (r"Yes — EOBI applicable \(PKR 370/month employee\)", "Yes, EOBI applies (employee 1% of minimum wage)"),
    (r"â†&rsquo;|â†’", "→"),
    (r"18% — Standard Federal Sales Tax \(FY 2025-26\)", "18% — Standard federal sales tax on goods"),
    (r"17% — Standard Rate \(previous year\)", "17% — Earlier standard rate"),
    (r"16% — Sindh/Punjab Sales Tax on Services", "16% — Punjab sales tax on services (PRA standard rate)"),
    (r"13% — Reduced Rate \(certain goods\)", "13% — Reduced rate (check the schedule)"),
    (r"10% — Reduced Rate", "10% — Reduced rate (check the schedule)"),
    (r"5% — Special Rate", "5% — Reduced rate (check the schedule)"),
]


def content_html(d):
    body = "".join(f'<h2 id="c{i}">{html.escape(h)}</h2>{c}' for i, (h, c) in enumerate(d["sections"], 1))
    faq = "".join(f'<div class="faq-item"><div class="faq-q" onclick="toggleFAQ(this)">{html.escape(q)}<i class="fas fa-chevron-down"></i></div>'
                  f'<div class="faq-a"><p>{html.escape(a)}</p></div></div>' for q, a in d["faqs"])
    src = ('<p style="font-size:.85rem;color:#64748b">Sources: <a href="https://www.fbr.gov.pk/" rel="noopener">Federal Board of Revenue</a> and '
           '<a href="https://iris.fbr.gov.pk/" rel="noopener">IRIS</a>; rates per the Finance Act 2026, checked 6 November 2026.</p>')
    return (f'<section class="section" id="guide"><div class="container" style="max-width:860px">{body}'
            f'<h2 id="faqs">Frequently Asked Questions</h2><div class="faq-list">{faq}</div>{src}</div></section>')


def main():
    os.chdir(ROOT)
    for slug, d in PAGES.items():
        f = slug + ".html"
        t = open(f, encoding="utf-8").read()
        start = t.find('<section style="margin:2rem 0;padding:1.5rem;background:#f8f9fa')
        if start < 0:
            start = t.find('<section class="section" id="guide">')
        end = t.find("<footer", start)
        assert start > 0 and end > start, f
        t = t[:start] + content_html(d) + unmatched_closers(t[start:end]) + t[end:]
        t = update_ld(t, d["faqs"])
        t = re.sub(r'<table class="slab-table">.*?</table>', lambda m: slab_table(SAL, "salaried"), t, flags=re.S)
        for pat, rep in TEXT_FIX:
            t = re.sub(pat, rep, t)
        t = re.sub(r'<style id="calc-css">.*?</style>', "", t, flags=re.S)
        t = re.sub(r'<script id="calc-engine">.*?</script>', "", t, flags=re.S)
        add = (CSS if 'class="calc-' in t else "") + (ENGINE if 'class="calc-btn"' in t else "")
        if "function toggleFAQ" not in t:
            add += "<script>function toggleFAQ(el){var i=el.closest('.faq-item');var o=i.classList.contains('open');document.querySelectorAll('.faq-item.open').forEach(function(x){x.classList.remove('open');});if(!o)i.classList.add('open');}</script>"
        t = t.replace("</body>", add + "</body>", 1)
        open(f, "w", encoding="utf-8").write(t)
    print("updated", len(PAGES))


if __name__ == "__main__":
    main()
