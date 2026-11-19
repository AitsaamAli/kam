"""Specs for the 2026 calculators. Every rate is from the Income Tax Ordinance 2001 amended up to 30.06.2026 (FBR)."""
ITO = ("Income Tax Ordinance, 2001 (FBR, amended up to 30.06.2026)", "https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf")
IRIS = ("FBR IRIS", "https://iris.fbr.gov.pk/")
ATL = ("FBR Active Taxpayers List", "https://www.fbr.gov.pk/categ/active-taxpayer-list-income-tax/51147/30859/71168")
SRO = ("FBR Income Tax SROs (SRO 2097(I)/2026)", "https://www.fbr.gov.pk/Categ/Income-Tax-SROs/334")
L = 'style="color:#0D9488;font-weight:600"'
def a(h, t): return f'<a href="{h}" {L}>{t}</a>'
P = lambda x: f'<p style="margin-bottom:12px">{x}</p>'

CALCS = []

# 1 ── ATL route cost ─────────────────────────────────────────────────────────
CALCS.append(dict(
    slug="atl-surcharge-vs-form-atl-u-calculator",
    title="ATL Surcharge vs Form ATL-U Calculator 2026 (Late Filers)",
    desc="Late filer? Compare the Rs 25,000 ATL surcharge with Form ATL-U, see which route fits your property plans and what being off the ATL costs you each month.",
    h1="ATL Surcharge vs Form ATL-U Calculator: Cheapest Way Back Onto the Active Taxpayers List",
    crumb="ATL Surcharge vs Form ATL-U", tag="Section 182A and 182A(3)",
    quick=f"A late filer rejoins the ATL by paying the Section 182A surcharge (Rs 25,000 individual, Rs 50,000 AOP, Rs 100,000 company) or, as an individual, by furnishing {a('/blogs/form-atl-u-fbr-guide-2026','Form ATL-U')} and obtaining no property for six months. Form ATL-U costs nothing at FBR, so it saves Rs 25,000 whenever you can keep the promise.",
    warn="Form ATL-U was notified by SRO 2097(I)/2026 on 10 November 2026 under Section 182A(3).",
    calc_h="Which ATL Route Costs Less?", calc_p="Pick who is filing, what kind of return it is, and whether any property is coming to you in six months.",
    fields=[("sel", "aType", "Who filed late?", [("individual", "Individual"), ("aop", "Association of persons (AOP)"), ("company", "Company")]),
            ("sel", "aRet", "Return type (for our published fee)", [("3500", "Salaried or pensioner (Rs 3,500)"), ("5000", "Freelancer or sole proprietor (Rs 5,000)"), ("6000", "Overseas Pakistani (Rs 6,000)"), ("8000", "AOP (Rs 8,000)"), ("0", "Already filed, only the ATL step")]),
            ("sel", "aPlan", "Will you buy, book or receive any property in the next six months?", [("no", "No"), ("yes", "Yes"), ("unsure", "Not sure")]),
            ("num", "aBank", "Annual bank profit (PKR, optional)", "e.g. 300000", "Off the ATL, the 20% deduction on bank profit is increased by 100%.")],
    res_h="Your Route", cards=[("rBest", "Recommended route", "#0D9488"), ("rSur", "Surcharge route", "#B45309"), ("rAtlu", "Form ATL-U route", "#0D9488"), ("rBank", "Extra bank tax per month off the ATL", "#EF4444")],
    verify="Costs exclude tax and any Section 182 penalty, which are paid to FBR either way. Our fees are the published ones; Form ATL-U preparation is Rs 2,000.",
    js=r"""function sync(){var ind=$('aType').value==='individual';$('aPlanRow').style.display=ind?'':'none';}
$('aType').addEventListener('change',sync);sync();
$('cBtn').addEventListener('click',function(){
 $('cErr').textContent='';var ty=$('aType').value,fee=+$('aRet').value,plan=$('aPlan').value,bank=num('aBank');
 if(!isNaN(bank)&&bank<0){$('cErr').textContent='Bank profit cannot be negative.';return;}
 var SUR={individual:25000,aop:50000,company:100000}[ty];
 var surTot=SUR+fee, atluTot=fee+2000, best, exp;
 if(ty!=='individual'){best='Surcharge';$('rAtlu').textContent='Not available';$('rAtluN').textContent='Form ATL-U is for individuals only (s.182A(3))';
   exp='An '+(ty==='aop'?'AOP':'company')+' cannot give the undertaking, so the only route is the '+rs(SUR)+' surcharge.';}
 else{$('rAtlu').textContent=rs(atluTot);$('rAtluN').textContent='Rs 0 to FBR + our fees';
   if(plan==='no'){best='Form ATL-U';exp='You keep the six-month promise, so Form ATL-U saves '+rs(surTot-atluTot)+' against the surcharge route.';}
   else if(plan==='yes'){best='Surcharge';exp='A purchase, booking or transfer to you within six months would breach Form ATL-U, so pay the surcharge before the deal.';}
   else{best='Talk to us first';exp='If any property may come to you, the surcharge buys certainty. If not, Form ATL-U saves '+rs(surTot-atluTot)+'.';}}
 $('rBest').textContent=best;$('rBestN').textContent='';
 $('rSur').textContent=rs(surTot);$('rSurN').textContent=rs(SUR)+' to FBR + our fees';
 if(!isNaN(bank)&&bank>0){$('rBank').textContent=rs(bank*0.2/12);$('rBankN').textContent='20% vs 40% on '+rs(bank)+' a year';exp+=' Every month off the ATL your bank deducts about '+rs(bank*0.2/12)+' more.';}
 else{$('rBank').textContent='-';$('rBankN').textContent='Enter bank profit to see this';}
 $('cExp').textContent=exp;show('cRes');});""",
    rules_short="The surcharge amounts and the undertaking come from Section 182A; the bank-profit effect from Section 151 and rule 1 of the Tenth Schedule.",
    rules=[("Surcharge, individual", "Rs 25,000", "s.182A(1)(a), proviso (iii)"), ("Surcharge, AOP", "Rs 50,000", "s.182A(1)(a), proviso (ii)"),
           ("Surcharge, company", "Rs 100,000", "s.182A(1)(a), proviso (i)"),
           ("Undertaking", "Individual: no purchase, acquisition, ownership or beneficial interest in any property for six months", "s.182A(3); SRO 2097(I)/2026"),
           ("Bank profit, on ATL", "20%", "First Schedule, Part III, Division IA"), ("Bank profit, off ATL", "Rate increased by 100%", "Tenth Schedule, rule 1")],
    sections=[("When Form ATL-U Is the Right Choice", "when you are an individual and nothing in your household plans brings property to you for six months.",
               P(f"Salaried people, pensioners, freelancers and people who are only selling property usually fit. The undertaking covers buying, acquiring, ownership and beneficial interest, so a plot bought in a relative's name with your money still counts. Our guide on {a('/blogs/form-atl-u-property-purchase-6-months-breach','what you cannot buy for six months')} goes through gifts, inheritance and vehicles.")),
              ("When to Pay the Surcharge", "when you are buying or booking property soon, when you are not sure, or when an AOP or company filed late.",
               P(f"The surcharge is certain: once paid, nothing else is required. Pay it before the property deal, so you are on the ATL when the buyer's tax under Section 236K is collected. See our {a('/tools/property-transfer-tax-calculator','property transfer tax calculator')}.")),
              ("Worked Example", "a salaried late filer with Rs 300,000 bank profit and no property plans pays Rs 5,500 with Form ATL-U instead of Rs 28,500.",
               P("Surcharge route: Rs 25,000 to FBR + Rs 3,500 return fee = Rs 28,500. Form ATL-U route: Rs 3,500 + Rs 2,000 = Rs 5,500. Meanwhile, each month off the ATL the bank deducts about Rs 5,000 more on Rs 300,000 of annual profit."))],
    faqs=[("Is Form ATL-U free?", "FBR charges nothing for the undertaking. Our fee for preparing and furnishing it is Rs 2,000."),
          ("Can an AOP or company use Form ATL-U?", "No. Section 182A(3) applies only to individuals."),
          ("Does either route remove the late filing penalty?", "No. The Section 182 penalty is separate from the ATL route."),
          ("What if I breach Form ATL-U?", "As notified, the benefit is withdrawn from the date of breach after a hearing, and the surcharge rule applies."),
          ("Can I sell property after Form ATL-U?", "Yes. The undertaking restricts acquiring property, not selling it.")],
    related=[("/blogs/form-atl-u-fbr-guide-2026", "Form ATL-U guide"), ("/tools/late-filing-penalty-calculator", "Late filing penalty calculator"), ("/tools/form-atl-u-end-date-calculator", "Form ATL-U six-month end date"), ("/blogs/filer-fee-2026-pakistan-late-filer-cost", "Filer fee 2026")],
    sources=[ITO, SRO, ATL],
    cta=("Back on the ATL by the Cheapest Route", "We file the late return and furnish Form ATL-U or arrange the surcharge, then confirm your ATL status.", "Assalam o Alaikum, ATL route calculator use kiya. Late return aur Form ATL-U karwana hai.", "File My Return With Form ATL-U"),
))

# 2 ── Form ATL-U end date ────────────────────────────────────────────────────
CALCS.append(dict(
    slug="form-atl-u-end-date-calculator",
    title="Form ATL-U Six-Month End Date Calculator (2026)",
    desc="Enter your Form ATL-U acknowledgement date to see the last day of the six-month property undertaking and the first safe day to book or buy property.",
    h1="Form ATL-U End Date Calculator: When Your Six-Month Property Undertaking Ends",
    crumb="Form ATL-U End Date", tag="Section 182A(3)",
    quick="The six months under Section 182A(3) start on the date you furnish the undertaking, shown on the IRIS acknowledgement. An undertaking furnished on 25 November 2026 runs to 24 May 2027; the first safe day to book or buy is 25 May 2027, and we suggest a two-week buffer.",
    warn="Count from the Form ATL-U acknowledgement date, not the return filing date or the date your name appears on the ATL.",
    calc_h="Find Your End Date", calc_p="Enter the date on your Form ATL-U IRIS acknowledgement.",
    fields=[("date", "eDate", "Form ATL-U acknowledgement date", "2026-11-20")],
    res_h="Your Six Months", cards=[("eEnd", "Last day of the undertaking", "#B45309"), ("eFree", "First day property is allowed", "#0D9488"), ("eSafe", "Suggested booking date (2-week buffer)", "#0D9488"), ("eLeft", "Days left from today", "")],
    verify="The law says six months commencing from the date the undertaking is furnished. Keep the IRIS acknowledgement as proof of the date.",
    js=r"""$('cBtn').addEventListener('click',function(){
 $('cErr').textContent='';var v=$('eDate').value;if(!v){$('cErr').textContent='Please enter the acknowledgement date.';return;}
 var d=parseD(v),free=addM(d,6),end=addD(free,-1),safe=addD(free,14),left=Math.round((end-today())/86400000);
 $('eEnd').textContent=nice(end);$('eFree').textContent=nice(free);$('eSafe').textContent=nice(safe);
 $('eLeft').textContent=left>=0?left:'Ended';$('eLeftN').textContent=left>=0?'days until the undertaking ends':'the six months have passed';
 $('cExp').textContent='Six months commencing on '+nice(d)+' end on '+nice(end)+'. Do not purchase, book, acquire or take a beneficial interest in any property until '+nice(free)+'. A two-week buffer, to '+nice(safe)+', removes any argument about counting.';
 show('cRes');});""",
    rules_short="Section 182A(3) fixes a period of six months commencing from the date the undertaking is furnished.",
    rules=[("Start", "Date of furnishing the undertaking (IRIS acknowledgement date)", "s.182A(3)"), ("Length", "Six months", "s.182A(3)"),
           ("What is restricted", "Purchase, acquisition, or ownership or beneficial interest in any property", "s.182A(3)"),
           ("Breach", "Benefit withdrawn from the breach date after a hearing; surcharge rule applies", "Rule 81B as notified by SRO 2097(I)/2026")],
    sections=[("How the Six Months Are Counted", "from the acknowledgement date to the day before the same date six months later.",
               P("A period of six months commencing on 20 November 2026 covers 20 November 2026 to 19 May 2027. Where the start date does not exist six months later (for example 31 August), the calculator uses the last day of that shorter month. When in doubt, wait an extra day.")),
              ("What You Can Do During the Six Months", "sell property, rent as a tenant and carry on your normal life; just do not acquire property or an interest in it.",
               P(f"Selling is not restricted, and a seller on the ATL pays 2.75% under Section 236C instead of 11.5%. See {a('/blogs/late-filer-tax-on-property-sale-form-atl-u','selling property as a late filer')}."))],
    faqs=[("When does my Form ATL-U six months start?", "On the date you furnish the undertaking, which is the date on the IRIS acknowledgement."),
          ("Can I book a plot on the last day?", "No. The last day is still inside the six months. Book from the following day, ideally with a buffer."),
          ("Does the six months start from my return date?", "No. The return date and the date your name appears on the ATL are not the start date."),
          ("Can I buy a car during the six months?", "The law says 'any property' and does not mention vehicles; until FBR clarifies, avoid it or pay the surcharge instead.")],
    related=[("/blogs/form-atl-u-property-purchase-6-months-breach", "What you cannot buy for six months"), ("/tools/atl-surcharge-vs-form-atl-u-calculator", "ATL surcharge vs Form ATL-U"), ("/blogs/form-atl-u-iris-submit-step-by-step", "Submit Form ATL-U on IRIS")],
    sources=[ITO, SRO],
    cta=("Not Sure Your Plans Fit the Six Months?", "We check your household's property plans before you sign, then file the route that fits.", "Assalam o Alaikum, Form ATL-U ke 6 maah ke baare mein mashwara chahiye.", "Check My Six Months"),
))

# 3 ── Property transfer tax 236C / 236K ──────────────────────────────────────
CALCS.append(dict(
    slug="property-transfer-tax-calculator",
    title="Property Transfer Tax Calculator 2026: 236C and 236K",
    desc="Advance tax on selling (236C) and buying (236K) property in 2026: 2.75% and 1.25% on the ATL, 11.5% and 10.5% to 18.5% off it. See your exact figure.",
    h1="Property Transfer Tax Calculator 2026: Seller's 236C and Buyer's 236K, On and Off the ATL",
    crumb="Property Transfer Tax", tag="Sections 236C and 236K",
    quick="When property is transferred in 2026, the seller pays advance tax under Section 236C at 2.75% of the gross consideration if on the ATL and 11.5% if not. The buyer pays under Section 236K at 1.25% of fair market value if on the ATL, or 10.5% (up to Rs 50 million), 14.5% (up to Rs 100 million) or 18.5% (above) if not.",
    warn="Rates as substituted by the Finance Act 2026. Rule 1A, which charged separate rates to late filers on the ATL, was omitted from 1 July 2026.",
    calc_h="Work Out the Advance Tax", calc_p="Enter the value and each party's ATL status at the date of transfer.",
    fields=[("num", "pVal", "Gross consideration / fair market value (PKR)", "e.g. 10000000", "236C uses the gross consideration received; 236K uses fair market value. Enter the figure that applies."),
            ("sel", "pSeller", "Seller on the Active Taxpayers List?", [("y", "Yes"), ("n", "No")]),
            ("sel", "pBuyer", "Buyer on the Active Taxpayers List?", [("y", "Yes"), ("n", "No")])],
    res_h="Advance Tax at Transfer", cards=[("pS", "Seller pays (236C)", "#B45309"), ("pB", "Buyer pays (236K)", "#B45309"), ("pX", "Extra because someone is off the ATL", "#EF4444"), ("pT", "Total collected", "")],
    verify="Both taxes are advance taxes, adjustable in the return for the year (subject to the Ordinance). Registrars may apply their own valuation tables for fair market value.",
    js=r"""$('cBtn').addEventListener('click',function(){
 $('cErr').textContent='';var v=num('pVal');if(isNaN(v)||v<=0){$('cErr').textContent='Please enter the property value.';return;}
 var sOn=$('pSeller').value==='y',bOn=$('pBuyer').value==='y';
 var sr=sOn?0.0275:0.115, br=bOn?0.0125:(v<=50000000?0.105:(v<=100000000?0.145:0.185));
 var s=v*sr,b=v*br,base=v*0.0275+v*0.0125;
 $('pS').textContent=rs(s);$('pSN').textContent=(sr*100).toFixed(2).replace(/\.?0+$/,'')+'% '+(sOn?'(on ATL)':'(off ATL)');
 $('pB').textContent=rs(b);$('pBN').textContent=(br*100).toFixed(2).replace(/\.?0+$/,'')+'% '+(bOn?'(on ATL)':'(off ATL)');
 $('pX').textContent=rs(s+b-base);$('pXN').textContent=(s+b-base)>0?'avoidable by joining the ATL before transfer':'both parties on the ATL';
 $('pT').textContent=rs(s+b);
 $('cExp').textContent='On '+rs(v)+', a seller on the ATL pays '+rs(v*0.0275)+' and off it '+rs(v*0.115)+'. A buyer on the ATL pays '+rs(v*0.0125)+'. A late filer who is only selling can join the ATL without the surcharge through Form ATL-U.';
 show('cRes');});""",
    rules_short="The ATL rates are in Part IV of the First Schedule; the off-ATL rates are in the Tenth Schedule.",
    rules=[("Seller, on ATL", "2.75% of gross consideration", "First Schedule, Part IV, Division X (Finance Act 2026)"),
           ("Seller, off ATL", "11.5% of gross consideration", "Tenth Schedule, rule 1, third proviso table"),
           ("Buyer, on ATL", "1.25% of fair market value", "First Schedule, Part IV, Division XVIII"),
           ("Buyer, off ATL", "10.5% up to Rs 50m; 14.5% up to Rs 100m; 18.5% above", "Tenth Schedule, rule 1, second proviso"),
           ("Late filers on the ATL", "No separate rate since 1 July 2026 (rule 1A omitted)", "Tenth Schedule, rule 1A omitted by Finance Act 2026")],
    sections=[("Getting the ATL Rate as a Late Filer", "file the return, then pay the surcharge or, if you are only selling, furnish Form ATL-U before the transfer date.",
               P(f"The rate is decided by the ATL at the time of transfer. Sellers with no purchase planned can use {a('/blogs/late-filer-tax-on-property-sale-form-atl-u','Form ATL-U')}; buyers cannot, because buying is what the undertaking forbids.")),
              ("Worked Example", "on a Rs 1 crore sale between two filers, the seller pays Rs 275,000 and the buyer Rs 125,000.",
               P("If the seller is off the ATL, the seller's tax rises to Rs 1,150,000. If the buyer is off the ATL, the buyer's tax rises to Rs 1,050,000. Joining the ATL before transfer saves either party far more than any surcharge."))],
    faqs=[("What is the tax on selling property for a filer in 2026?", "2.75% of the gross consideration under Section 236C."),
          ("What does a non-filer pay when selling property?", "11.5% under the Tenth Schedule."),
          ("What does a buyer pay?", "1.25% of fair market value on the ATL; 10.5%, 14.5% or 18.5% by value off it."),
          ("Do active late filers still pay higher property tax?", "No. Rule 1A was omitted by the Finance Act 2026; a late filer on the ATL pays ordinary filer rates."),
          ("Is this the capital gains tax?", "No. These are advance taxes at transfer. Capital gain is worked out in the return; see our capital gains calculator.")],
    related=[("/tools/property-capital-gains-calculator", "Capital gains calculator"), ("/blogs/late-filer-tax-on-property-sale-form-atl-u", "Late filer property sale"), ("/blogs/tax-on-property-sale-pakistan-2026", "Tax on property sale 2026"), ("/tools/atl-surcharge-vs-form-atl-u-calculator", "ATL route calculator")],
    sources=[ITO, ATL],
    cta=("Selling or Buying Soon? Get on the ATL First", "We file your return and the right ATL route before the transfer date.", "Assalam o Alaikum, property transfer se pehle ATL mein aana hai.", "Get Me on the ATL"),
))

# 4 ── Bank profit tax ────────────────────────────────────────────────────────
CALCS.append(dict(
    slug="bank-profit-tax-calculator",
    title="Bank Profit Tax Calculator 2026: Filer 20% vs Non-Filer 40%",
    desc="Work out tax deducted on bank profit and savings under Section 151 in 2026: 20% on the ATL, increased by 100% off it. Monthly and yearly figures.",
    h1="Bank Profit Tax Calculator 2026: How Much Your Bank Deducts On and Off the ATL",
    crumb="Bank Profit Tax", tag="Section 151",
    quick="Banks deduct 20% of the profit on accounts and deposits under Section 151 for people on the Active Taxpayers List. For people not on the ATL, rule 1 of the Tenth Schedule increases the rate by 100%, to 40%.",
    warn="The rate is decided by your ATL status on each profit payment date.",
    calc_h="Work Out the Deduction", calc_p="Enter either the annual profit, or the deposit and profit rate.",
    fields=[("num", "bProfit", "Annual profit (PKR)", "e.g. 300000", "Leave blank to calculate from the deposit and rate below."),
            ("num", "bDep", "Deposit amount (PKR, optional)", "e.g. 3000000"), ("num", "bRate", "Annual profit rate (%, optional)", "e.g. 10"),
            ("sel", "bAtl", "On the Active Taxpayers List?", [("y", "Yes"), ("n", "No")])],
    res_h="Tax on Your Profit", cards=[("bT", "Tax deducted per year", "#B45309"), ("bM", "Per month", ""), ("bNet", "Profit after tax per year", "#0D9488"), ("bX", "Extra paid off the ATL per year", "#EF4444")],
    verify="Tax deducted on an individual's profit on debt is generally dealt with under Section 7B; excess deductions are claimed through the return, and refunds are blocked while you are off the ATL (s.182A(1)(c)).",
    js=r"""$('cBtn').addEventListener('click',function(){
 $('cErr').textContent='';var p=num('bProfit');
 if(isNaN(p)){var d=num('bDep'),r=num('bRate');if(isNaN(d)||isNaN(r)){$('cErr').textContent='Enter the annual profit, or both the deposit and the rate.';return;}p=d*r/100;}
 if(p<0){$('cErr').textContent='Profit cannot be negative.';return;}
 var on=$('bAtl').value==='y',rate=on?0.2:0.4,t=p*rate;
 $('bT').textContent=rs(t);$('bTN').textContent=(rate*100)+'% of '+rs(p);$('bM').textContent=rs(t/12);$('bNet').textContent=rs(p-t);
 $('bX').textContent=on?rs(0):rs(p*0.2);$('bXN').textContent=on?'you are on the ATL':'avoidable by joining the ATL';
 $('cExp').textContent=on?'On the ATL your bank deducts 20%.':'Off the ATL your bank deducts 40%, which is '+rs(p*0.2)+' a year more. A late filer can rejoin the ATL without the Rs 25,000 surcharge through Form ATL-U.';
 show('cRes');});""",
    rules_short="20% comes from Division IA of Part III of the First Schedule; the 100% increase from rule 1 of the Tenth Schedule.",
    rules=[("Profit on bank accounts and deposits, on ATL", "20%", "First Schedule, Part III, Division IA(a)"),
           ("Not on ATL", "Rate increased by 100%", "Tenth Schedule, rule 1 (separate 35% row omitted by Finance Act 2025)"),
           ("Refunds while off ATL", "Not issued", "s.182A(1)(c)")],
    sections=[("Getting Back to 20%", "join the ATL: file the return, then pay the surcharge or furnish Form ATL-U, and tell your bank once your name appears.",
               P(f"Pensioners and savers rarely buy property within six months, so {a('/blogs/late-filer-tax-on-bank-profit-form-atl-u','Form ATL-U')} usually fits.")),
              ("Worked Example", "Rs 3 million at 10% earns Rs 300,000 a year; the bank deducts Rs 60,000 on the ATL and Rs 120,000 off it.",
               P("The Rs 60,000 difference is Rs 5,000 a month, so five months off the ATL cost as much as the whole Rs 25,000 surcharge."))],
    faqs=[("What is the tax on bank profit for filers in 2026?", "20% under Section 151 for people on the ATL."),
          ("What do non-filers pay on bank profit?", "The 20% rate increased by 100%, which is 40%."),
          ("Does a late filer pay 40%?", "Yes, until the surcharge is paid or Form ATL-U is furnished and the name appears on the ATL."),
          ("Can I get the extra deduction back?", "It is claimed through the return, and Section 182A(1)(c) blocks refunds while you are off the ATL.")],
    related=[("/blogs/late-filer-tax-on-bank-profit-form-atl-u", "Late filer bank profit tax"), ("/blogs/tax-on-bank-profit-pakistan-2026", "Tax on bank profit 2026"), ("/tools/atl-surcharge-vs-form-atl-u-calculator", "ATL route calculator")],
    sources=[ITO, ATL],
    cta=("Stop the Double Deduction", "Late return, Form ATL-U and an ATL check, so your bank goes back to 20%.", "Assalam o Alaikum, bank profit par 40% kat raha hai. ATL mein aana hai.", "Fix My Bank Tax"),
))

# 5 ── Business / AOP income tax ──────────────────────────────────────────────
CALCS.append(dict(
    slug="business-income-tax-calculator",
    title="Business Income Tax Calculator 2026-27 (Non-Salaried)",
    desc="Income tax on non-salaried income for Tax Year 2027: 0% to 45% slabs for individuals and AOPs, plus the 10% surcharge above Rs 10 million. Free calculator.",
    h1="Business Income Tax Calculator 2026-27 for Freelancers, Sole Proprietors and AOPs",
    crumb="Business Income Tax", tag="First Schedule, Part I, Division I",
    quick="Non-salaried individuals and AOPs pay 0% up to Rs 600,000, then 15%, 20%, 30% and 40% in bands, and 45% above Rs 5.6 million. A 10% surcharge on that tax applies under Section 4AB where taxable income exceeds Rs 10 million.",
    warn="Slabs as in Division I of Part I of the First Schedule (table substituted by the Finance Act 2024). Salaried individuals use separate slabs.",
    calc_h="Work Out the Tax", calc_p="Enter annual taxable income (after allowable expenses).",
    fields=[("num", "iInc", "Annual taxable income (PKR)", "e.g. 2400000"), ("sel", "iType", "Taxpayer", [("ind", "Individual (non-salaried)"), ("aop", "Association of persons")])],
    res_h="Tax for the Year", cards=[("iT", "Tax under the slabs", "#B45309"), ("iS", "Surcharge (s.4AB)", "#B45309"), ("iTot", "Total tax", "#EF4444"), ("iEff", "Effective rate", "")],
    verify="Excludes income taxed separately (final or fixed taxes, capital gains, profit on debt under s.7B) and tax credits. Advance tax already paid is adjusted in the return.",
    js=r"""$('cBtn').addEventListener('click',function(){
 $('cErr').textContent='';var x=num('iInc');if(isNaN(x)||x<0){$('cErr').textContent='Please enter taxable income.';return;}
 var B=[[600000,0,0],[1200000,0,.15],[1600000,90000,.20],[3200000,170000,.30],[5600000,650000,.40],[Infinity,1610000,.45]],lo=[0,600000,1200000,1600000,3200000,5600000],t=0;
 for(var i=0;i<B.length;i++){if(x<=B[i][0]){t=B[i][1]+(x-lo[i])*B[i][2];if(i===0)t=0;break;}}
 var s=x>10000000?t*0.10:0;
 $('iT').textContent=rs(t);$('iS').textContent=rs(s);$('iSN').textContent=s?'10% of tax, income above Rs 10m':'income not above Rs 10m';
 $('iTot').textContent=rs(t+s);$('iEff').textContent=x?((t+s)/x*100).toFixed(2)+'%':'0%';$('iEffN').textContent=rs((t+s)/12)+' a month';
 $('cExp').textContent='Taxable income '+rs(x)+': tax '+rs(t)+(s?(' plus surcharge '+rs(s)):'')+'. Quarterly advance tax under Section 147 may apply; see the advance tax calculator.';
 show('cRes');});""",
    rules_short="The slab table and the surcharge are quoted from the Ordinance; nothing else is assumed.",
    rules=[("Up to Rs 600,000", "0%", "First Schedule, Part I, Division I(1)"), ("Rs 600,001 to 1,200,000", "15% of the amount above Rs 600,000", "Division I(1)"),
           ("Rs 1,200,001 to 1,600,000", "Rs 90,000 + 20% above Rs 1,200,000", "Division I(1)"), ("Rs 1,600,001 to 3,200,000", "Rs 170,000 + 30% above Rs 1,600,000", "Division I(1)"),
           ("Rs 3,200,001 to 5,600,000", "Rs 650,000 + 40% above Rs 3,200,000", "Division I(1)"), ("Above Rs 5,600,000", "Rs 1,610,000 + 45% above Rs 5,600,000", "Division I(1)"),
           ("Surcharge", "10% of the tax where taxable income exceeds Rs 10 million (not for salaried individuals)", "s.4AB")],
    sections=[("Who Uses These Slabs", "freelancers, shopkeepers, sole proprietors, professionals and AOPs; not salaried individuals.",
               P(f"Salaried individuals use the salary slabs in our {a('/tools/salary-tax-calculator','salary tax calculator')}. A sole proprietor is taxed as an individual on business income.")),
              ("Worked Example", "on Rs 2.4 million of business income the tax is Rs 410,000, an effective 17.08%.",
               P("Rs 170,000 for the first Rs 1.6 million, plus 30% of Rs 800,000 (Rs 240,000), equals Rs 410,000. No surcharge applies below Rs 10 million."))],
    faqs=[("What is the tax-free limit for business income in 2026-27?", "Rs 600,000 of taxable income."),
          ("What is the top rate for non-salaried individuals?", "45% on income above Rs 5.6 million, plus a 10% surcharge on the tax where income exceeds Rs 10 million."),
          ("Do AOPs use the same slabs?", "Yes. Division I(1) applies to individuals and associations of persons other than salaried individuals."),
          ("Is the surcharge payable by salaried people?", "No. The proviso to Section 4AB says no surcharge is payable by an individual deriving salary income.")],
    related=[("/tools/advance-tax-instalment-calculator", "Advance tax instalment calculator"), ("/tools/income-tax-calculator-pakistan", "Income tax calculator"), ("/blogs/tax-return-for-freelancers-2026", "Freelancer tax return")],
    sources=[ITO],
    cta=("Business Return Filed Right", "Freelancer and sole proprietor returns Rs 5,000, AOP returns Rs 8,000, published fees.", "Assalam o Alaikum, business income ki return file karwani hai.", "File My Business Return"),
))

# 6 ── Advance tax s.147 ──────────────────────────────────────────────────────
CALCS.append(dict(
    slug="advance-tax-instalment-calculator",
    title="Advance Tax Calculator: Section 147 Instalments 2026",
    desc="Quarterly advance tax under Section 147(4B) for individuals: (A/4) minus B, due 15 September, 15 December, 15 March and 15 June. Check if it applies.",
    h1="Advance Tax Instalment Calculator: Section 147 Quarterly Tax for Individuals",
    crumb="Advance Tax Instalments", tag="Section 147",
    quick="An individual whose latest assessed taxable income, excluding salary and final-tax income, is Rs 1 million or more pays quarterly advance tax under Section 147(4B): one quarter of last year's assessed tax, minus tax already paid in that quarter that qualifies for credit. Instalments are due on 15 September, 15 December, 15 March and 15 June.",
    warn="AOPs and companies use a turnover-based formula under Section 147(4), not this one.",
    calc_h="Work Out Your Instalment", calc_p="Use last year's assessed figures.",
    fields=[("num", "aInc", "Latest assessed taxable income, excluding salary and final-tax income (PKR)", "e.g. 2500000"),
            ("num", "aTax", "Tax assessed for the latest tax year, A (PKR)", "e.g. 400000"),
            ("num", "aPaid", "Tax already paid this quarter that qualifies for credit, B (PKR)", "e.g. 20000", "For example advance tax on electricity bills or other adjustable withholding."),
            ("sel", "aQ", "Quarter", [("Sep", "July to September (due 15 September)"), ("Dec", "October to December (due 15 December)"), ("Mar", "January to March (due 15 March)"), ("Jun", "April to June (due 15 June)")])],
    res_h="Your Quarterly Advance Tax", cards=[("aApp", "Does Section 147 apply?", ""), ("aI", "Instalment for the quarter", "#B45309"), ("aDue", "Due date", ""), ("aY", "Full-year estimate (4 quarters)", "")],
    verify="If you expect this year's tax to be lower or higher, Section 147 has estimate provisions; we can file the estimate for you.",
    js=r"""$('cBtn').addEventListener('click',function(){
 $('cErr').textContent='';var inc=num('aInc'),A=num('aTax'),B=num('aPaid');if(isNaN(B))B=0;
 if(isNaN(inc)||isNaN(A)||inc<0||A<0||B<0){$('cErr').textContent='Please enter last year\'s assessed income and tax.';return;}
 var due={Sep:'15 September',Dec:'15 December',Mar:'15 March',Jun:'15 June'}[$('aQ').value];
 if(inc<1000000){$('aApp').textContent='No';$('aAppN').textContent='below Rs 1 million (s.147(2))';$('aI').textContent=rs(0);$('aDue').textContent='-';$('aY').textContent=rs(0);
  $('cExp').textContent='Section 147 does not apply where the latest assessed taxable income, excluding salary and final-tax income, is below Rs 1 million.';show('cRes');return;}
 var q=Math.max(A/4-B,0);
 $('aApp').textContent='Yes';$('aAppN').textContent='Rs 1 million or more';$('aI').textContent=rs(q);$('aIN').textContent='('+rs(A)+' / 4) - '+rs(B);$('aDue').textContent=due;$('aY').textContent=rs(A);$('aYN').textContent='before quarterly credits';
 $('cExp').textContent='Formula (A/4) - B: '+rs(A/4)+' less '+rs(B)+' = '+rs(q)+', payable by '+due+'.';show('cRes');});""",
    rules_short="The threshold, the formula and the quarters come from Section 147.",
    rules=[("Who pays", "Individuals with latest assessed taxable income (excluding s.5, 6, 7, salary and final-tax income) of Rs 1 million or more", "s.147(1), (2)"),
           ("Formula", "(A/4) - B; A = tax assessed for the latest year; B = tax paid in the quarter with a s.168 credit", "s.147(4B)"),
           ("Quarters", "Jul-Sep, Oct-Dec, Jan-Mar, Apr-Jun", "s.147(3)"), ("Due dates", "15 September, 15 December, 15 March, 15 June", "s.147")],
    sections=[("Who Must Pay Advance Tax", "individuals with business, professional, rental or other non-final income of Rs 1 million or more last year.",
               P("Salary taxed under Section 149 and income under final or separate regimes are excluded from the threshold and the formula. Most salaried people therefore never pay Section 147 instalments.")),
              ("Worked Example", "last year's tax Rs 400,000 and Rs 20,000 already paid this quarter: the instalment is Rs 80,000.",
               P("A/4 = Rs 100,000; minus B of Rs 20,000 = Rs 80,000 due by the quarter's due date."))],
    faqs=[("Who has to pay advance tax under Section 147?", "Individuals whose latest assessed taxable income, excluding salary and final-tax income, is Rs 1 million or more."),
          ("How is the instalment calculated?", "(A/4) - B: a quarter of last year's assessed tax minus creditable tax already paid in the quarter."),
          ("When are instalments due?", "15 September, 15 December, 15 March and 15 June."),
          ("Do salaried people pay advance tax?", "Not on salary. Section 149 deduction covers it, and salary is excluded from the Section 147 threshold.")],
    related=[("/tools/business-income-tax-calculator", "Business income tax calculator"), ("/blogs/advance-tax-pakistan-2026", "Advance tax guide"), ("/withholding-tax", "Withholding tax")],
    sources=[ITO, IRIS],
    cta=("Advance Tax Worked Out and Paid on Time", "We calculate your instalments, prepare the PSIDs and keep the credits for your return.", "Assalam o Alaikum, Section 147 advance tax instalment ka hisaab chahiye.", "Calculate My Advance Tax"),
))

# 7 ── Revised return window ──────────────────────────────────────────────────
CALCS.append(dict(
    slug="revised-return-deadline-calculator",
    title="Revised Return Deadline Calculator: 60-Day Window",
    desc="Enter your original filing date to see the last day you can file a revised income tax return without the Commissioner's approval under Section 114(6).",
    h1="Revised Return Deadline Calculator: Your 60-Day Window Under Section 114(6)",
    crumb="Revised Return Deadline", tag="Section 114(6)",
    quick="Under Section 114(6), a revised return needs the Commissioner's approval, except when it is filed within 60 days of filing the original return. A return filed on 31 October 2026 can be revised without approval until 30 December 2026.",
    warn="A revised return must carry written, signed reasons, and revised accounts for business cases; one that misses a condition is treated as invalid.",
    calc_h="Find Your 60-Day Deadline", calc_p="Enter the date on your original return's IRIS acknowledgement.",
    fields=[("date", "rDate", "Original return filing date", "2026-10-31")],
    res_h="Your Revision Window", cards=[("r60", "Last day without approval", "#0D9488"), ("rLeft", "Days left from today", "#B45309"), ("rAfter", "After that", "")],
    verify="After the 60 days, apply for approval; if no written order is made within 60 days of the application, approval is deemed granted.",
    js=r"""$('cBtn').addEventListener('click',function(){
 $('cErr').textContent='';var v=$('rDate').value;if(!v){$('cErr').textContent='Please enter the filing date.';return;}
 var d=parseD(v),end=addD(d,60),left=Math.round((end-today())/86400000);
 $('r60').textContent=nice(end);$('rLeft').textContent=left>=0?left:'Passed';$('rLeftN').textContent=left>=0?'days to revise without approval':'approval now needed';
 $('rAfter').textContent='Approval';$('rAfterN').textContent='deemed granted if no order in 60 days';
 $('cExp').textContent='Filed on '+nice(d)+': revise without approval by '+nice(end)+'. '+(left>=0?'Prepare the reasons and revised figures now.':'You can still revise with the Commissioner\'s approval.');show('cRes');});""",
    rules_short="The 60-day window, the conditions and deemed approval are all in Section 114(6).",
    rules=[("No approval needed", "Revised return filed within 60 days of the original", "s.114(6), proviso"), ("Conditions", "Written signed reasons; revised accounts where relevant", "s.114(6)(a), (b)"),
           ("After 60 days", "Commissioner's approval; deemed granted if no order within 60 days", "s.114(6)"), ("Invalid revision", "One that misses a condition is treated as invalid", "s.114(6)")],
    sections=[("What to Prepare", "the corrected figures, revised wealth statement if needed, and signed written reasons.",
               P(f"Our guide on {a('/blogs/revised-return-tax-year-2026-60-days-pakistan','revising a Tax Year 2026 return within 60 days')} lists each step.")),
              ("Worked Example", "filed on 15 November 2026, the window runs to 14 January 2027.",
               P("Count 60 days from the filing date on the acknowledgement. Filing the revision a few days early protects against IRIS delays."))],
    faqs=[("How long do I have to revise without approval?", "60 days from filing the original return, under Section 114(6)."),
          ("What if the 60 days have passed?", "Apply to the Commissioner; approval is deemed granted if no written order is made within 60 days."),
          ("Will revising cause a penalty?", "Not if you revise voluntarily before a notice and pay any tax and default surcharge, under Section 114(6A).")],
    related=[("/blogs/revised-return-tax-year-2026-60-days-pakistan", "TY2026 revised return"), ("/blogs/revised-return-before-notice-penalty-relief-section-114-6a", "Revise before a notice"), ("/tools/wealth-reconciliation-calculator", "Wealth reconciliation checker")],
    sources=[ITO, IRIS],
    cta=("Revise Inside the 60 Days", "We check the original, prepare the reasons and file the revision.", "Assalam o Alaikum, apni return revise karwani hai (60 din ke andar).", "Revise My Return"),
))

# 8 ── Wealth reconciliation ──────────────────────────────────────────────────
CALCS.append(dict(
    slug="wealth-reconciliation-calculator",
    title="Wealth Reconciliation Calculator: Unreconciled Amount",
    desc="Check your wealth statement before filing: opening net assets plus inflows minus outflows must equal closing net assets. Find the unreconciled amount.",
    h1="Wealth Reconciliation Calculator: Find the Unreconciled Amount Before IRIS Does",
    crumb="Wealth Reconciliation", tag="Section 116",
    quick="A wealth statement reconciles when last year's net assets, plus this year's inflows (income, exempt income, gifts and gains), minus outflows (personal expenses, gifts given and losses), equals this year's net assets. Any gap is the unreconciled amount, which IRIS expects to be zero.",
    warn="Section 116 requires a wealth statement and wealth reconciliation from individuals in the cases it specifies.",
    calc_h="Reconcile Your Wealth", calc_p="Enter whole-year figures in PKR. Leave unused boxes blank.",
    fields=[("num", "wOpen", "Net assets at the end of last year (PKR)", "e.g. 5000000"), ("num", "wClose", "Net assets at the end of this year (PKR)", "e.g. 6200000"),
            ("num", "wInc", "Income declared in the return, after tax (PKR)", "e.g. 1800000", "Use income after the tax you paid."),
            ("num", "wEx", "Exempt or final-tax income not in the line above (PKR)", ""), ("num", "wGift", "Gifts, inheritance or loans received (PKR)", ""),
            ("num", "wGain", "Gains on sale of assets (PKR)", ""), ("num", "wExp", "Personal and household expenses (PKR)", "e.g. 600000"),
            ("num", "wOut", "Gifts given, losses and other outflows (PKR)", "")],
    res_h="Your Reconciliation", cards=[("wIn", "Total inflows", ""), ("wOutT", "Total outflows", ""), ("wExpct", "Expected closing net assets", "#0D9488"), ("wGap", "Unreconciled amount", "#EF4444")],
    verify="An unexplained increase in assets can be examined under Section 111. Fix the reconciliation before filing, not after a notice.",
    js=r"""function z(id){var v=num(id);return isNaN(v)?0:v;}
$('cBtn').addEventListener('click',function(){
 $('cErr').textContent='';if(isNaN(num('wOpen'))||isNaN(num('wClose'))){$('cErr').textContent='Enter last year\'s and this year\'s net assets.';return;}
 var inf=z('wInc')+z('wEx')+z('wGift')+z('wGain'),out=z('wExp')+z('wOut'),exp=z('wOpen')+inf-out,gap=z('wClose')-exp;
 $('wIn').textContent=rs(inf);$('wOutT').textContent=rs(out);$('wExpct').textContent=rs(exp);$('wGap').textContent=rs(gap);
 $('wGapN').textContent=Math.abs(gap)<1?'reconciled':(gap>0?'assets higher than explained':'assets lower than explained');
 $('cExp').textContent=Math.abs(gap)<1?'Your figures reconcile.':(gap>0?'Your closing assets are '+rs(gap)+' higher than your inflows explain. Look for missing income, gifts or loans received, or an overstated asset.':'Your closing assets are '+rs(-gap)+' lower than expected. Look for missing expenses, gifts given or an asset left out.');
 show('cRes');});""",
    rules_short="Net assets at the end of the year must equal last year's net assets plus inflows minus outflows; that is the reconciliation Section 116 requires.",
    rules=[("Wealth statement and reconciliation", "Filed with the return by individuals in the cases specified", "s.116"),
           ("Revised wealth statement", "Allowed with a revised reconciliation and reasons before a notice under s.122(9)", "s.116(3)"),
           ("Unexplained assets", "Can be treated as income", "s.111")],
    sections=[("Most Common Reasons It Does Not Reconcile", "missing household expenses, a forgotten bank account, gifts or loans not recorded, and assets entered at the wrong value.",
               P(f"Our guide on {a('/blogs/wealth-statement-guide-pakistan-2026','the wealth statement')} explains each line, and the {a('/blogs/assets-missing-from-wealth-statement-pakistan','assets people leave out')} guide lists the usual omissions.")),
              ("Worked Example", "net assets rise from Rs 5 million to Rs 6.2 million with Rs 1.8 million after-tax income and Rs 600,000 expenses: the gap is zero.",
               P("Rs 5,000,000 + Rs 1,800,000 - Rs 600,000 = Rs 6,200,000, which matches the closing figure."))],
    faqs=[("What is the unreconciled amount?", "The difference between your closing net assets and what your opening assets, inflows and outflows explain."),
          ("Will IRIS accept a return with an unreconciled amount?", "IRIS flags it; fix the figures so the reconciliation balances before you submit."),
          ("Can I fix last year's wealth statement?", "Yes, Section 116(3) allows a revised wealth statement with reasons before a notice under Section 122(9).")],
    related=[("/blogs/wealth-statement-guide-pakistan-2026", "Wealth statement guide"), ("/blogs/revise-wealth-statement-last-5-years-pakistan", "Revise old wealth statements"), ("/tools/revised-return-deadline-calculator", "Revised return deadline")],
    sources=[ITO, IRIS],
    cta=("Wealth Statement That Reconciles", "Wealth statement preparation Rs 2,000 (published fee), or included with your return.", "Assalam o Alaikum, meri wealth reconciliation match nahi ho rahi.", "Fix My Reconciliation"),
))
