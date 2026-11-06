"""Page-specific content for the P1 doorway pages (5 Nov 2026). Figures were checked against official sources:
Section 182 / 182A from FBR, TY2026 deadline extension to 31 Oct 2026 (FBR press release), others cite their regulator."""

FBR = '<a href="https://www.fbr.gov.pk/" rel="noopener">FBR</a>'
IRIS = '<a href="https://iris.fbr.gov.pk/" rel="noopener">IRIS</a>'
DEADLINE = ("The Tax Year 2026 return deadline for individuals and AOPs was extended to 31 October 2026 and has now passed. "
            "A late return can still be filed on IRIS. Under Section 182 the late-filing penalty is 0.1% of the tax payable per day, "
            "up to 50%, with a minimum of Rs 40,000 (Rs 5,000 where at least 75% of income is salary below Rs 5 million). "
            "Joining the Active Taxpayers List after the due date also needs the Section 182A surcharge: Rs 25,000 for individuals, "
            "Rs 50,000 for AOPs and Rs 100,000 for companies.")

T = {}

T["atl-registration-lahore"] = dict(
    sections=[
        ("What is the Active Taxpayers List and who is on it?",
         f"<p>The Active Taxpayers List (ATL) is the list {FBR} publishes of people and businesses who filed their income tax return for the previous tax year. Banks, property registrars and motor registration offices check it to decide which withholding rate applies to you. Being on it is what people mean by being a \"filer\".</p>"),
        ("How do you get onto the ATL from Lahore?",
         "<ol><li>Register on IRIS if you do not yet have an NTN; for individuals the CNIC becomes the tax number.</li>"
         "<li>File the income tax return (Form 114) and wealth statement (Form 116) for the latest tax year.</li>"
         "<li>If the return is filed after the due date, pay the Section 182A surcharge through a PSID on IRIS.</li>"
         "<li>Check your status once FBR updates the list.</li></ol>"),
        ("Late filing: penalty and surcharge", f"<p>{DEADLINE}</p>"),
        ("How to check your ATL status",
         "<ul><li>SMS <strong>ATL &lt;space&gt; 13-digit CNIC</strong> to 9966.</li>"
         "<li>Use the ATL search on FBR's website.</li><li>Check the status in FBR's Tax Asaan app.</li></ul>"
         "<p>Compare filer and non-filer rates with our <a href=\"/tools/filer-vs-non-filer-calculator\">filer vs non-filer calculator</a>.</p>"),
        ("Why Lahore residents check ATL status most often",
         "<p>In Lahore, ATL status usually matters at three moments: buying or selling property through the LDA, a housing society or the registrar, registering a new vehicle with Excise and Taxation, and receiving bank profit. The withholding difference between filer and non-filer rates on a single property transaction is often larger than the cost of filing every year.</p>"),
    ],
    faqs=[
        ("How long does it take to appear on the ATL?", "A return filed on time appears when FBR next updates the list. A late filer appears after the return is filed and the Section 182A surcharge is paid. Check your status by SMS to 9966 after filing."),
        ("What is the ATL surcharge for late filers?", "Under Section 182A it is Rs 25,000 for individuals, Rs 50,000 for AOPs and Rs 100,000 for companies. It is in addition to any Section 182 late-filing penalty."),
        ("Does ATL status expire?", "Yes. The list is based on the latest tax year's return, so you must file every year to stay on it."),
        ("Can I file and pay the surcharge myself?", "Yes, both are done on IRIS: file the return, generate a PSID for the surcharge and pay it through your bank. Keep the payment receipt."),
    ],
    sources=[("FBR: Active Taxpayers List", "https://www.fbr.gov.pk/"), ("FBR IRIS portal", "https://iris.fbr.gov.pk/")])

T["wealth-statement-consultant-lahore"] = dict(
    sections=[
        ("What is a wealth statement?",
         f"<p>The wealth statement (Form 116) is filed with the income tax return on {IRIS}. It lists everything you own and owe on 30 June: property, vehicles, bank balances, investments, gold, cash, loans and liabilities. Assets held in the name of a spouse or minor children who are not filers themselves are declared too.</p>"),
        ("Why the reconciliation matters most",
         "<p>The statement ends with a wealth reconciliation: opening net worth plus income for the year, minus personal expenses, should equal closing net worth. If your assets grew faster than your declared income can explain, FBR's systems can flag the difference and ask you to explain the source. Getting the reconciliation right is the main reason people ask for help.</p>"),
        ("What to gather before preparing it",
         "<table><tr><th>Item</th><th>What you need</th></tr>"
         "<tr><td>Property</td><td>Purchase deeds or allotment letters showing cost and date</td></tr>"
         "<tr><td>Vehicles</td><td>Registration book and purchase price</td></tr>"
         "<tr><td>Bank accounts</td><td>Balances on 30 June and annual tax certificates</td></tr>"
         "<tr><td>Investments</td><td>Shares, savings certificates, mutual funds at cost</td></tr>"
         "<tr><td>Liabilities</td><td>Loan statements and amounts owed</td></tr>"
         "<tr><td>Expenses</td><td>Household, education, utilities and travel for the year</td></tr></table>"),
        ("Common mistakes in Lahore wealth statements",
         "<ul><li>Declaring property at today's market value instead of its cost.</li>"
         "<li>Leaving out a plot or file bought in a housing society.</li>"
         "<li>Not recording gifts or inheritances that explain an increase in assets.</li>"
         "<li>Personal expenses so low that they are not believable for the household.</li></ul>"),
        ("Deadline and late filing", f"<p>{DEADLINE}</p>"),
    ],
    faqs=[
        ("Is a wealth statement compulsory for every filer?", "Individuals filing a return generally file the wealth statement with it. FBR's return form on IRIS shows when Form 116 is required for your case."),
        ("Should property be declared at market value?", "No. Assets are declared at cost, meaning what you paid plus related costs, not current market value."),
        ("Can a wealth statement be revised?", "Yes, a revised wealth statement can be filed on IRIS, subject to the conditions in the law. Revise only with a clear reason and keep supporting documents."),
        ("Do I declare my wife's assets?", "Assets of a spouse or minor children who are not filers themselves are declared in your statement. If your spouse files her own return, her assets go in her statement."),
    ],
    sources=[("FBR IRIS portal", "https://iris.fbr.gov.pk/"), ("Federal Board of Revenue", "https://www.fbr.gov.pk/")])

T["ntn-registration-lahore"] = dict(
    sections=[
        ("What NTN registration means for individuals and businesses",
         f"<p>An NTN is your registration with {FBR}. For an individual, registering on {IRIS} makes the CNIC the tax number. An AOP (partnership) and a company receive their own number. FBR does not charge a fee for online registration of individuals.</p>"),
        ("What you need before you start",
         "<ul><li>A valid CNIC.</li><li>A mobile SIM registered in your own name, for the verification code.</li>"
         "<li>An email address you check daily.</li><li>Home and business address, and your source of income.</li>"
         "<li>For an AOP: partnership deed and partners' CNICs. For a company: SECP incorporation certificate.</li></ul>"),
        ("Registering on IRIS step by step",
         "<ol><li>Open IRIS and choose registration for an unregistered person.</li><li>Enter CNIC, name, email and mobile number.</li>"
         "<li>Enter the codes sent to your email and phone.</li><li>Set your password and PIN, then log in.</li>"
         "<li>Complete the registration form with address, income source and bank details, and submit.</li></ol>"),
        ("FBR offices in Lahore",
         "<p>Lahore has several FBR field offices, including Regional Tax Offices, the Corporate RTO and the Large Taxpayers Office. Your case is assigned to one based on your status and address. Registration itself is online, so a visit is usually only needed if FBR asks for verification.</p>"),
        ("After registration", "<p>Registration is only the first step. File your return and wealth statement every year to stay on the Active Taxpayers List. Our <a href=\"/atl-registration-lahore\">ATL guide</a> explains the list and the surcharge for late filers.</p>"),
    ],
    faqs=[
        ("Is NTN registration free?", "FBR does not charge for online registration of individuals on IRIS. A consultant may charge for their own time if you ask them to do it for you."),
        ("Is my CNIC my NTN?", "For individuals registered on IRIS, the CNIC number is used as the tax number. AOPs and companies receive a separate number."),
        ("Why does the SIM need to be in my name?", "IRIS sends verification codes to that number and uses it for password recovery, so it must be a number you control."),
        ("Do I have to file a return after getting an NTN?", "Yes. Registration does not make you a filer. File the return and wealth statement each year to appear on the Active Taxpayers List."),
    ],
    sources=[("FBR IRIS portal", "https://iris.fbr.gov.pk/"), ("Federal Board of Revenue", "https://www.fbr.gov.pk/")])

T["income-tax-return-filing-lahore"] = dict(
    sections=[
        ("Who in Lahore needs to file an income tax return?",
         "<p>You need to file if your taxable income is above the exemption threshold, or if you own assets or carry out transactions the law links to filing, such as owning property or a vehicle above set limits. Salaried staff, shopkeepers, professionals, freelancers, landlords and overseas Pakistanis with Pakistani income all commonly file.</p>"),
        ("Deadline and late filing", f"<p>{DEADLINE}</p><p>For companies with a 30 June year end, the deadline is 31 December 2026. The Tax Year 2027 return, for July 2026 to June 2027, is due in September 2027.</p>"),
        ("Documents to prepare",
         "<table><tr><th>Document</th><th>Used for</th></tr><tr><td>Salary certificate</td><td>Salary and tax deducted</td></tr>"
         "<tr><td>Bank tax certificates</td><td>Profit and withholding tax</td></tr><tr><td>Utility and mobile bills</td><td>Advance tax on bills</td></tr>"
         "<tr><td>Rent agreements</td><td>Property income</td></tr><tr><td>Business records</td><td>Sales, purchases and expenses</td></tr>"
         "<tr><td>Property and vehicle papers</td><td>Wealth statement</td></tr></table>"),
        ("Filing on IRIS", "<p>The return (Form 114) and wealth statement (Form 116) are filed on IRIS. Salaried individuals with simple cases can also use FBR's Tax Asaan app. If tax is payable, a PSID is generated and paid through a bank before submission.</p>"),
        ("Getting it checked before you submit", "<p>Most notices we see in Lahore come from three issues: income that does not match bank and withholding data FBR already has, a wealth statement that does not reconcile, and property bought without declaring the funds. A review before submission avoids all three. Our <a href=\"/wealth-statement-consultant-lahore\">wealth statement guide</a> covers the reconciliation.</p>"),
    ],
    faqs=[
        ("Can I still file my Tax Year 2026 return?", "Yes. Late returns can still be filed on IRIS, but the Section 182 penalty may apply, and joining the Active Taxpayers List needs the Section 182A surcharge."),
        ("What is the minimum late-filing penalty?", "Rs 40,000, or Rs 5,000 where at least 75% of income is salary below Rs 5 million. The penalty is 0.1% of tax payable per day up to 50%."),
        ("Can salaried people file themselves?", "Yes, through IRIS or the Tax Asaan app. Help is useful when there are several income sources or a complex wealth statement."),
        ("When is the Tax Year 2027 return due?", "Returns for Tax Year 2027 (July 2026 to June 2027) are due by 30 September 2027 for individuals and AOPs, unless FBR extends the date."),
    ],
    sources=[("FBR IRIS portal", "https://iris.fbr.gov.pk/"), ("Federal Board of Revenue", "https://www.fbr.gov.pk/")])

T["fbr-consultant-near-me-lahore"] = dict(
    sections=[
        ("What an FBR consultant actually does",
         "<p>An FBR consultant prepares and files returns and statements, handles registration, and replies to FBR notices on your behalf. Before FBR, only persons the Income Tax Ordinance recognises as authorised representatives can appear for you in proceedings, so ask how the firm handles that before you hire it.</p>"),
        ("How to check a consultant before hiring",
         "<ul><li>A real office address you can visit, and a landline or business number.</li><li>A written fee quote before work starts.</li>"
         "<li>Copies of everything filed in your name, including the IRIS acknowledgement.</li><li>Never sharing your IRIS password with someone who will not give it back; ask for your own login to stay with you.</li>"
         "<li>No promises of guaranteed refunds or \"settling\" a notice.</li></ul>"),
        ("Services people in Lahore most often need",
         "<table><tr><th>Need</th><th>Where to start</th></tr><tr><td>First registration</td><td><a href=\"/ntn-registration-lahore\">NTN registration in Lahore</a></td></tr>"
         "<tr><td>Annual return</td><td><a href=\"/income-tax-return-filing-lahore\">Income tax return filing in Lahore</a></td></tr>"
         "<tr><td>Wealth statement</td><td><a href=\"/wealth-statement-consultant-lahore\">Wealth statement guide</a></td></tr>"
         "<tr><td>Notice received</td><td><a href=\"/how-to-respond-to-tax-notices-pakistan\">How to respond to tax notices</a></td></tr></table>"),
        ("Working with us", "<p>Kamboh Associates works from Shop No 34, Rizwan Block Market, Awan Town, Lahore, Monday to Saturday from 9:00 AM to 6:00 PM, and on Friday until 12:30 PM. Most work is done online; documents can be shared on WhatsApp or email and we send copies of everything filed.</p>"),
    ],
    faqs=[
        ("Do I need to visit an FBR office to file?", "Usually not. Registration, returns and most replies are submitted online on IRIS. A visit is needed only if FBR asks for verification."),
        ("Should I give my IRIS password to a consultant?", "Share access only with someone you trust, and change the password afterwards. Ask for copies of everything filed in your name."),
        ("Can a consultant guarantee a refund?", "No. Refunds depend on FBR's processing and your records. Treat guaranteed refund promises as a warning sign."),
        ("What are your office hours?", "Monday to Saturday, 9:00 AM to 6:00 PM, and Friday until 12:30 PM. We are closed on Sunday."),
    ],
    sources=[("Federal Board of Revenue", "https://www.fbr.gov.pk/"), ("FBR IRIS portal", "https://iris.fbr.gov.pk/")])

# ---------------- compliance guides ----------------
T["tax-on-agricultural-income-pakistan"] = dict(
    sections=[
        ("Is agricultural income taxed by FBR?",
         "<p>Agricultural income, such as income from crops grown on land in Pakistan, is exempt from federal income tax under the Income Tax Ordinance, because the Constitution gives the power to tax it to the provinces. It is taxed instead under each province's agricultural income tax law, such as the Punjab Agricultural Income Tax Act.</p>"),
        ("Do you still declare it in your federal return?",
         "<p>Yes. Agricultural income is shown in the federal return as exempt income, and the land, crops, machinery and livestock appear in the wealth statement. Declaring it explains the money that funds your assets and expenses; leaving it out is a common reason a wealth reconciliation fails.</p>"),
        ("What changed in the provinces",
         "<p>Provinces amended their agricultural income tax laws in 2024 and 2025 to bring rates for larger incomes closer to federal rates. Rates, slabs and the authority that collects the tax differ by province, so check the current law and notifications on your provincial government's official website before calculating what you owe.</p>"),
        ("Records farmers should keep",
         "<ul><li>Land ownership records (fard) and lease agreements.</li><li>Sale receipts from commission agents or mills.</li>"
         "<li>Input costs: seed, fertiliser, pesticide, diesel and labour.</li><li>Proof of provincial agricultural income tax paid.</li></ul>"),
        ("Non-agricultural income on the same farm",
         "<p>Income from processing, trading or renting out machinery is not agricultural income, even if earned on a farm. A rice mill, a dairy shop or a commission agency is taxed federally like any business.</p>"),
    ],
    faqs=[
        ("Is crop income taxable in Pakistan?", "It is exempt from federal income tax but taxed by the province under its agricultural income tax law."),
        ("Should agricultural income be shown in the FBR return?", "Yes, as exempt income, with land and farm assets in the wealth statement. This explains the source of your wealth."),
        ("Is income from a dairy or mill agricultural income?", "No. Processing, trading and similar business income is taxed federally, even when it is connected to farming."),
        ("Where can I find current agricultural income tax rates?", "On your provincial government's official website and the notifications under its agricultural income tax law, since rates differ by province."),
    ],
    sources=[("Federal Board of Revenue", "https://www.fbr.gov.pk/"), ("Government of the Punjab", "https://punjab.gov.pk/")])

T["tax-audit-preparation-checklist"] = dict(
    sections=[
        ("How cases are selected for audit",
         "<p>FBR can select a case for audit under Section 177 of the Income Tax Ordinance, and cases can also be picked through parametric computer balloting under Section 214C. Being selected does not mean wrongdoing; it means FBR wants to examine the return and records.</p>"),
        ("Checklist: what to have ready",
         "<table><tr><th>Area</th><th>Records</th></tr><tr><td>Income</td><td>Sales invoices, contracts, bank statements</td></tr>"
         "<tr><td>Expenses</td><td>Bills, receipts and payment proofs for every expense claimed</td></tr>"
         "<tr><td>Withholding</td><td>Certificates for tax deducted, and proof of tax you withheld and deposited</td></tr>"
         "<tr><td>Assets</td><td>Purchase documents for property, vehicles and investments</td></tr>"
         "<tr><td>Reconciliation</td><td>Working showing how income explains the change in wealth</td></tr></table>"),
        ("How long to keep records", "<p>The Ordinance requires records to be kept for six years after the end of the tax year to which they relate. Keep scanned copies as well as originals.</p>"),
        ("Replying to audit notices", "<ul><li>Reply on IRIS before the date in the notice, or request an adjournment in writing.</li><li>Answer only what is asked, with indexed documents.</li><li>Keep copies and acknowledgements of every submission.</li></ul><p>Our guide on <a href=\"/how-to-respond-to-tax-notices-pakistan\">responding to tax notices</a> covers the replies step by step.</p>"),
    ],
    faqs=[
        ("What is Section 177?", "It allows the Commissioner to select a person's case for audit and call for records."),
        ("What is Section 214C?", "It provides for selecting cases for audit through parametric computer balloting by FBR."),
        ("How many years of records should I keep?", "Six years after the end of the tax year the records relate to."),
        ("Can I ask for more time to reply?", "Yes, an adjournment can be requested in writing before the due date, with a reason."),
    ],
    sources=[("Federal Board of Revenue: Income Tax Ordinance", "https://www.fbr.gov.pk/"), ("FBR IRIS portal", "https://iris.fbr.gov.pk/")])

T["fbr-notice-after-tax-return-pakistan"] = dict(
    sections=[
        ("Why notices arrive after a return is filed",
         "<p>After filing, FBR's systems compare your return with data it already holds: bank profit and withholding, property and vehicle transactions, utility bills and third-party reports. A mismatch, an unexplained increase in wealth or a missing document often triggers a notice.</p>"),
        ("Common notices and what they mean",
         "<table><tr><th>Section</th><th>Usually means</th></tr><tr><td>114(4)</td><td>FBR thinks you should file a return for a tax year</td></tr>"
         "<tr><td>176</td><td>A request for information or documents</td></tr><tr><td>122(9)</td><td>Show cause before an assessment is amended</td></tr>"
         "<tr><td>177</td><td>Selection for audit</td></tr><tr><td>161 / 205</td><td>Withholding tax not deducted or deposited, and default surcharge</td></tr></table>"),
        ("What to do first", "<ol><li>Read the notice on IRIS and note the section and due date.</li><li>Collect the documents it asks for.</li><li>Reply on IRIS before the due date, or request an adjournment in writing.</li><li>Keep the acknowledgement of every reply.</li></ol>"),
        ("Mistakes that make it worse", "<ul><li>Ignoring the notice until the date passes.</li><li>Filing a revised return without understanding what is being questioned.</li><li>Sending documents that contradict the return.</li></ul><p>More detail is in our <a href=\"/how-to-respond-to-tax-notices-pakistan\">guide to responding to tax notices</a>.</p>"),
    ],
    faqs=[
        ("Is a notice after filing serious?", "It is a formal request that needs a reply by the due date. Many are resolved by providing the documents asked for."),
        ("Where do I see FBR notices?", "Notices are issued to your IRIS account and email. Check IRIS regularly, not only during filing season."),
        ("What happens if I do not reply?", "FBR can proceed on the information it has, which may lead to an amended assessment, tax demand or penalty."),
        ("Can I get more time?", "You can request an adjournment in writing before the due date, giving a reason."),
    ],
    sources=[("FBR IRIS portal", "https://iris.fbr.gov.pk/"), ("Federal Board of Revenue", "https://www.fbr.gov.pk/")])

T["how-to-respond-to-tax-notices-pakistan"] = dict(
    sections=[
        ("Step 1: identify the notice",
         "<p>Every notice names the section of the law it is issued under, the tax year and a due date. The section tells you what FBR wants: information (176), a return (114(4)), an explanation before amending an assessment (122(9)), an audit (177) or recovery of withholding tax (161).</p>"),
        ("Step 2: prepare a structured reply",
         "<ol><li>Address each point in the notice in order.</li><li>Attach indexed supporting documents for every figure.</li><li>Refer to the return and wealth statement already filed.</li><li>Keep the tone factual and short.</li></ol>"),
        ("Step 3: submit on time", "<p>Submit the reply through IRIS before the due date and keep the acknowledgement. If you need more time, ask for an adjournment in writing before the date passes, explaining why.</p>"),
        ("If you disagree with an order", "<p>If FBR passes an order you disagree with, the law provides appeal routes, first to the Commissioner (Appeals) and then to the Appellate Tribunal Inland Revenue, within the time limits stated. Get advice quickly, because the limits are short.</p>"),
        ("Records that win most cases", "<ul><li>Bank statements that match declared income.</li><li>Withholding certificates.</li><li>Purchase documents for assets.</li><li>Gift or inheritance documents explaining increases in wealth.</li></ul><p>See also our <a href=\"/tax-audit-preparation-checklist\">tax audit preparation checklist</a>.</p>"),
    ],
    faqs=[
        ("How long do I have to reply to an FBR notice?", "The due date is written on the notice. Reply before it, or request an adjournment in writing before it passes."),
        ("Can I reply online?", "Yes, replies and documents are submitted through IRIS, which gives an acknowledgement."),
        ("What if I disagree with the final order?", "You can appeal to the Commissioner (Appeals) and then the Appellate Tribunal Inland Revenue within the legal time limits."),
        ("Should I file a revised return after a notice?", "Only after understanding what is questioned. A revision without reason can create new questions."),
    ],
    sources=[("FBR IRIS portal", "https://iris.fbr.gov.pk/"), ("Federal Board of Revenue", "https://www.fbr.gov.pk/")])

T["tax-penalties-in-pakistan"] = dict(
    sections=[
        ("Late filing of the income tax return",
         "<p>Under Section 182, failing to file the return on time attracts a penalty of 0.1% of the tax payable for each day of default, up to 50% of the tax payable, with a minimum of Rs 40,000. Where at least 75% of income is salary and the salary is below Rs 5 million, the minimum is Rs 5,000.</p>"),
        ("Joining the Active Taxpayers List late", "<p>Section 182A requires a surcharge to join the ATL after the due date: Rs 25,000 for individuals, Rs 50,000 for AOPs and Rs 100,000 for companies.</p>"),
        ("Withholding statements and unpaid tax",
         "<table><tr><th>Default</th><th>Consequence</th></tr><tr><td>Late withholding statement</td><td>Rs 2,500 per day, minimum Rs 10,000; Rs 5,000 if the tax was paid and the statement filed within 90 days</td></tr>"
         "<tr><td>Tax not paid on time</td><td>Default surcharge under Section 205 at 12% a year or KIBOR + 3%, whichever is higher</td></tr></table>"),
        ("How to keep penalties low", "<ul><li>File as soon as possible after a missed date; daily penalties keep growing.</li><li>Pay tax due through a PSID before filing.</li><li>Reply to notices before their due dates.</li></ul><p>Estimate your exposure with our <a href=\"/tools/late-filing-penalty-calculator\">late filing penalty calculator</a>.</p>"),
    ],
    faqs=[
        ("What is the penalty for filing the income tax return late?", "0.1% of tax payable per day up to 50%, minimum Rs 40,000, or Rs 5,000 for low-salary cases, under Section 182."),
        ("Is the ATL surcharge the same as the late-filing penalty?", "No. The Section 182A surcharge is paid to join the ATL after the due date and is separate from the Section 182 penalty."),
        ("What is the penalty for a late withholding statement?", "Rs 2,500 per day with a minimum of Rs 10,000, or Rs 5,000 if the tax was paid and the statement is filed within 90 days."),
        ("What is the default surcharge rate?", "Under Section 205 it is 12% a year or KIBOR plus 3%, whichever is higher, on tax paid late."),
    ],
    sources=[("Federal Board of Revenue", "https://www.fbr.gov.pk/"), ("FBR IRIS portal", "https://iris.fbr.gov.pk/")])

T["annual-company-filing-guide-pakistan"] = dict(
    sections=[
        ("Two regulators, two sets of filings",
         "<p>A company in Pakistan files with the <a href=\"https://www.secp.gov.pk/\" rel=\"noopener\">SECP</a> under the Companies Act 2017 and with FBR under the tax laws. Missing either leads to separate penalties.</p>"),
        ("Main SECP filings",
         "<table><tr><th>Filing</th><th>When</th></tr><tr><td>Annual general meeting</td><td>Within 120 days of the financial year end</td></tr>"
         "<tr><td>Annual return (Form A for companies with share capital)</td><td>Within 30 days of the AGM</td></tr>"
         "<tr><td>Financial statements</td><td>Filed after the AGM as the Act requires</td></tr>"
         "<tr><td>Changes in directors or officers</td><td>Within the time the Act allows after the change</td></tr></table>"
         "<p>Filings are made online through SECP's eZfile/LEAP portal. Check SECP's current forms and fees before filing.</p>"),
        ("Main FBR filings", "<ul><li>Annual income tax return; due 31 December for a 30 June year end.</li><li>Withholding tax statements by their due dates.</li><li>Monthly sales tax return, if registered.</li></ul>"),
        ("A simple yearly calendar", "<p>Close the books after 30 June, finalise accounts and audit where required, hold the AGM, file the SECP annual return, then file the company's tax return by 31 December. Our <a href=\"/business-compliance-checklist-pakistan\">business compliance checklist</a> lists the other registrations a business may need.</p>"),
    ],
    faqs=[
        ("When must a company hold its AGM?", "Within 120 days of the end of its financial year under the Companies Act 2017."),
        ("When is the annual return filed?", "Form A is filed with SECP within 30 days of the AGM for companies with share capital."),
        ("When is a company's tax return due?", "For a 30 June year end, by 31 December of that year."),
        ("Where are SECP filings made?", "Online on SECP's eZfile/LEAP portal."),
    ],
    sources=[("SECP", "https://www.secp.gov.pk/"), ("Federal Board of Revenue", "https://www.fbr.gov.pk/")])

T["business-compliance-checklist-pakistan"] = dict(
    sections=[
        ("Federal registrations", "<ul><li>NTN with FBR for the business or owner.</li><li>Sales tax registration (STRN) if you manufacture, import or supply goods in the scope of the Sales Tax Act.</li><li>SECP incorporation if you operate as a company.</li></ul>"),
        ("Provincial registrations", "<ul><li>Sales tax on services with the provincial authority: <a href=\"https://pra.punjab.gov.pk/\" rel=\"noopener\">PRA</a> (Punjab), SRB (Sindh), KPRA (KP) or BRA (Balochistan).</li><li>Employees' social security with the provincial institution, such as PESSI in Punjab.</li><li>Provincial professional tax where it applies.</li></ul>"),
        ("Employer obligations", "<ul><li>EOBI registration for establishments with five or more employees.</li><li>Withholding tax on salaries and deposit by the due dates.</li><li>Employment records and contracts.</li></ul>"),
        ("Recurring filings", "<table><tr><th>Filing</th><th>Frequency</th></tr><tr><td>FBR income tax return</td><td>Yearly</td></tr><tr><td>Withholding statements</td><td>By the due dates set by FBR</td></tr><tr><td>Federal sales tax return</td><td>Monthly</td></tr><tr><td>Provincial services sales tax return</td><td>Monthly</td></tr><tr><td>SECP annual return</td><td>Yearly, after the AGM</td></tr></table>"),
        ("Where to start", "<p>Start with the NTN, then add only the registrations your activity needs. Our guides on <a href=\"/pra-registration-guide-pakistan\">PRA registration</a> and <a href=\"/eobi-registration-guide-pakistan\">EOBI registration</a> explain two of the most common.</p>"),
    ],
    faqs=[
        ("Does every business need sales tax registration?", "No. It depends on the activity. Goods fall under the federal Sales Tax Act; services are taxed by the provinces."),
        ("When does EOBI apply?", "To establishments with five or more employees under the EOBI Act."),
        ("Which authority taxes services in Punjab?", "The Punjab Revenue Authority (PRA)."),
        ("Is SECP registration compulsory?", "Only if you choose to operate as a company. Sole proprietors and partnerships do not incorporate with SECP."),
    ],
    sources=[("Federal Board of Revenue", "https://www.fbr.gov.pk/"), ("SECP", "https://www.secp.gov.pk/"), ("Punjab Revenue Authority", "https://pra.punjab.gov.pk/")])

T["pra-registration-guide-pakistan"] = dict(
    sections=[
        ("What PRA taxes", "<p>The <a href=\"https://pra.punjab.gov.pk/\" rel=\"noopener\">Punjab Revenue Authority</a> collects sales tax on services provided in Punjab under the Punjab Sales Tax on Services Act 2012. Restaurants, consultants, IT and marketing firms, contractors, beauty salons and many other service providers fall within its schedule.</p>"),
        ("Who must register", "<p>A person providing taxable services listed in the Act's schedule from Punjab must register with PRA. Check the current schedule and any exemptions on PRA's website, because the list and rates are revised through finance acts.</p>"),
        ("How registration works", "<ol><li>Have your NTN with FBR ready.</li><li>Apply on PRA's online e-registration system with business details, bank account and premises information.</li><li>Upload the documents PRA asks for.</li><li>Once approved, you file monthly returns online.</li></ol>"),
        ("After registration", "<p>PRA returns are filed monthly; the Punjab sales tax return is generally due by the 15th of the following month. Issue tax invoices for taxable services and keep records. FBR's sales tax on goods is separate; see our <a href=\"/business-compliance-checklist-pakistan\">business compliance checklist</a>.</p>"),
    ],
    faqs=[
        ("Is PRA the same as FBR sales tax?", "No. FBR collects sales tax on goods; PRA collects sales tax on services provided in Punjab."),
        ("When is the PRA return due?", "Generally by the 15th of the following month. Check PRA's website for any change."),
        ("Do I need an NTN before PRA registration?", "Yes, have your FBR registration ready before applying."),
        ("Where can I find PRA's current rates?", "On the Punjab Revenue Authority's official website and the schedule to the Act."),
    ],
    sources=[("Punjab Revenue Authority", "https://pra.punjab.gov.pk/"), ("Federal Board of Revenue", "https://www.fbr.gov.pk/")])

T["srb-registration-guide-pakistan"] = dict(
    sections=[
        ("What SRB taxes", "<p>The <a href=\"https://www.srb.gos.pk/\" rel=\"noopener\">Sindh Revenue Board</a> collects sales tax on services provided in Sindh under the Sindh Sales Tax on Services Act 2011. Businesses in Karachi, Hyderabad and the rest of Sindh providing listed services must register.</p>"),
        ("Who must register", "<p>Service providers whose services appear in the Act's schedule and are provided in Sindh. A business providing services in both Sindh and Punjab may need registration with both SRB and PRA, depending on where services are provided.</p>"),
        ("How registration works", "<ol><li>Keep your FBR NTN ready.</li><li>Apply on SRB's online registration system with business, bank and premises details.</li><li>Upload the documents requested.</li><li>After approval, file returns online every month.</li></ol>"),
        ("After registration", "<p>Issue tax invoices, keep records and file monthly returns by SRB's due date. Check SRB's website for current rates and due dates. For Punjab, see our <a href=\"/pra-registration-guide-pakistan\">PRA registration guide</a>.</p>"),
    ],
    faqs=[
        ("Is SRB registration needed for a Lahore business?", "Only if it provides taxable services in Sindh. Services provided in Punjab fall under PRA."),
        ("What law applies to SRB?", "The Sindh Sales Tax on Services Act 2011."),
        ("Can a business be registered with both SRB and PRA?", "Yes, if it provides taxable services in both provinces."),
        ("Where are SRB rates published?", "On the Sindh Revenue Board's official website."),
    ],
    sources=[("Sindh Revenue Board", "https://www.srb.gos.pk/"), ("Punjab Revenue Authority", "https://pra.punjab.gov.pk/")])

T["kpra-registration-guide-pakistan"] = dict(
    sections=[
        ("What KPRA taxes", "<p>The <a href=\"https://kpra.gov.pk/\" rel=\"noopener\">Khyber Pakhtunkhwa Revenue Authority</a> collects sales tax on services provided in Khyber Pakhtunkhwa under the province's sales tax on services law, along with other provincial levies assigned to it.</p>"),
        ("Who must register", "<p>Persons providing services listed in the KP schedule from or in Khyber Pakhtunkhwa. Businesses based in Punjab that provide services in KP should check whether KP registration is needed for those services.</p>"),
        ("How registration works", "<ol><li>Have your FBR NTN ready.</li><li>Apply online through KPRA's registration system with business, bank and premises details.</li><li>Upload the documents KPRA requests.</li><li>File monthly returns once registered.</li></ol>"),
        ("After registration", "<p>Issue invoices, keep records and file returns by KPRA's due date. Check KPRA's website for current rates. Compare with <a href=\"/pra-registration-guide-pakistan\">PRA in Punjab</a> and <a href=\"/srb-registration-guide-pakistan\">SRB in Sindh</a>.</p>"),
    ],
    faqs=[
        ("Is KPRA the same as FBR?", "No. KPRA is the provincial authority for sales tax on services in Khyber Pakhtunkhwa; FBR handles federal taxes."),
        ("Does a Punjab business need KPRA registration?", "Only if it provides taxable services in Khyber Pakhtunkhwa."),
        ("How often are KPRA returns filed?", "Monthly, by the date KPRA sets."),
        ("Where can I check KPRA rates?", "On KPRA's official website."),
    ],
    sources=[("Khyber Pakhtunkhwa Revenue Authority", "https://kpra.gov.pk/"), ("Federal Board of Revenue", "https://www.fbr.gov.pk/")])

T["eobi-registration-guide-pakistan"] = dict(
    sections=[
        ("What EOBI is", "<p>The <a href=\"https://www.eobi.gov.pk/\" rel=\"noopener\">Employees' Old-Age Benefits Institution</a> runs the old-age pension scheme for private-sector workers under the EOBI Act 1976. Employers register their establishment and pay monthly contributions for insured employees.</p>"),
        ("Who must register", "<p>Industrial and commercial establishments with five or more employees fall under the Act. Once covered, the establishment registers with EOBI and registers each eligible employee.</p>"),
        ("Contributions", "<p>The employer contributes 5% and the employee 1% of the minimum wage notified by the government, paid monthly. Check EOBI's website for the current minimum wage basis and payment method.</p>"),
        ("Benefits for employees", "<ul><li>Old-age pension on retirement after the required contribution period.</li><li>Invalidity pension.</li><li>Survivors' pension for the family.</li><li>Old-age grant where pension conditions are not met.</li></ul>"),
        ("Related obligations", "<p>EOBI is separate from provincial social security, such as PESSI in Punjab, which provides medical and cash benefits. See our <a href=\"/social-security-registration-pakistan\">social security registration guide</a>.</p>"),
    ],
    faqs=[
        ("How many employees make EOBI compulsory?", "Five or more employees in an industrial or commercial establishment."),
        ("What is the EOBI contribution rate?", "5% from the employer and 1% from the employee, calculated on the notified minimum wage."),
        ("Is EOBI the same as social security?", "No. EOBI provides pensions; provincial social security institutions provide medical and cash benefits."),
        ("Where do I register?", "With EOBI through its official channels; details are on eobi.gov.pk."),
    ],
    sources=[("EOBI", "https://www.eobi.gov.pk/"), ("PESSI Punjab", "https://pessi.punjab.gov.pk/")])

T["social-security-registration-pakistan"] = dict(
    sections=[
        ("Provincial schemes", "<p>Employees' social security is run by the provinces: the <a href=\"https://pessi.punjab.gov.pk/\" rel=\"noopener\">Punjab Employees Social Security Institution</a> (PESSI) in Punjab, SESSI in Sindh and similar bodies in other provinces. They provide medical care and cash benefits to covered workers and their families.</p>"),
        ("Who is covered", "<p>Establishments within the provincial law's scope register their eligible employees, generally those earning up to the wage limit the province sets. Check the current coverage rules and wage limit on the institution's website.</p>"),
        ("Contributions", "<p>The employer pays a percentage of each covered employee's wages each month; in Punjab, PESSI's contribution is 6% of wages for covered employees. Confirm the current rate and ceiling with the institution before calculating.</p>"),
        ("Registration steps", "<ol><li>Register the establishment with the provincial institution.</li><li>Register each eligible employee.</li><li>Pay monthly contributions by the due date.</li><li>Keep wage records for inspection.</li></ol>"),
        ("Related obligations", "<p>Social security is separate from EOBI pensions; most employers need both. See our <a href=\"/eobi-registration-guide-pakistan\">EOBI registration guide</a>.</p>"),
    ],
    faqs=[
        ("Who runs social security in Punjab?", "The Punjab Employees Social Security Institution (PESSI)."),
        ("What benefits does social security provide?", "Medical care and cash benefits for covered workers and their families, as set by provincial law."),
        ("Who pays the contribution?", "The employer pays a percentage of covered employees' wages each month."),
        ("Is social security the same as EOBI?", "No. EOBI is the federal-level pension scheme; social security is provincial and covers medical and cash benefits."),
    ],
    sources=[("PESSI Punjab", "https://pessi.punjab.gov.pk/"), ("EOBI", "https://www.eobi.gov.pk/")])

T["tax-on-commercial-property-pakistan"] = dict(
    sections=[
        ("Taxes over the life of a commercial property",
         "<table><tr><th>Stage</th><th>Tax</th></tr><tr><td>Buying</td><td>Advance tax on purchase under Section 236K, plus provincial stamp duty and registration fees</td></tr>"
         "<tr><td>Owning</td><td>Provincial urban immovable property tax collected by the Excise and Taxation department</td></tr>"
         "<tr><td>Renting out</td><td>Income tax on rent; tenants that are companies or other prescribed persons deduct tax under Section 155</td></tr>"
         "<tr><td>Selling</td><td>Advance tax on sale under Section 236C and tax on any capital gain under Section 37</td></tr></table>"),
        ("Rental income", "<p>Rent from a shop, office or warehouse is property income. It is declared in the return, and tax deducted by tenants is claimed against the liability. Keep rent agreements and deduction certificates.</p>"),
        ("Filer status matters", "<p>Withholding rates on purchase and sale are higher for persons not on the Active Taxpayers List. Check the current rates for your transaction in the Income Tax Ordinance's schedules on FBR's website before signing.</p>"),
        ("Records to keep", "<ul><li>Purchase deed and proof of payment.</li><li>Rent agreements and tenant certificates.</li><li>Property tax receipts.</li><li>Improvement and repair bills.</li></ul><p>See also our <a href=\"/tax-penalties-in-pakistan\">guide to tax penalties</a>.</p>"),
    ],
    faqs=[
        ("Is rent from a shop taxable?", "Yes. Rent is property income declared in the return; tax deducted by tenants is credited."),
        ("Which tax applies when buying commercial property?", "Advance tax under Section 236K, plus provincial stamp duty and registration fees."),
        ("Which tax applies on selling?", "Advance tax under Section 236C and tax on capital gain under Section 37."),
        ("Who collects property tax on buildings?", "The provincial Excise and Taxation department."),
    ],
    sources=[("Federal Board of Revenue", "https://www.fbr.gov.pk/"), ("Punjab Excise, Taxation and Narcotics Control", "https://excise.punjab.gov.pk/")])

T["trademark-registration-cost-pakistan"] = dict(
    sections=[
        ("What a trademark registration costs", "<p>The cost has two parts: official fees paid to the <a href=\"https://ipo.gov.pk/\" rel=\"noopener\">Intellectual Property Organisation of Pakistan</a> (IPO-Pakistan) for each application and class, and any professional fee for searches and filing. IPO publishes its current fee schedule on its website; check it before filing, because fees are revised.</p>"),
        ("What drives the total", "<ul><li>Number of classes: each class of goods or services needs its own application.</li><li>Word mark, logo or both: each is filed separately.</li><li>Opposition: costs rise if someone opposes your mark.</li><li>Renewal: registration lasts ten years and is renewable.</li></ul>"),
        ("The process in order", "<ol><li>Search existing marks.</li><li>File the application in the right class.</li><li>Examination by the Registrar.</li><li>Publication in the Trade Marks Journal for opposition.</li><li>Registration certificate if there is no successful opposition.</li></ol>"),
        ("Keeping cost under control", "<p>Choose classes carefully, run a search before filing and use the exact name and logo you will trade under. See our guides on <a href=\"/brand-name-registration-guide-pakistan\">brand name registration</a> and <a href=\"/logo-registration-process-pakistan\">logo registration</a>.</p>"),
    ],
    faqs=[
        ("Who registers trademarks in Pakistan?", "The Trade Marks Registry under IPO-Pakistan, under the Trade Marks Ordinance 2001."),
        ("How long does a trademark registration last?", "Ten years, renewable for further periods."),
        ("Do I pay per class?", "Yes, each class of goods or services is a separate application with its own fee."),
        ("Where can I see the current official fees?", "On IPO-Pakistan's website in its published fee schedule."),
    ],
    sources=[("IPO-Pakistan", "https://ipo.gov.pk/")])

T["brand-name-registration-guide-pakistan"] = dict(
    sections=[
        ("Brand name vs company name", "<p>Registering a company with SECP or a business with FBR does not give you exclusive rights to a brand name. Exclusive rights come from registering it as a trademark with the <a href=\"https://ipo.gov.pk/\" rel=\"noopener\">IPO-Pakistan</a> Trade Marks Registry.</p>"),
        ("Choosing a name that can be registered", "<ul><li>Distinctive words are easier to register than descriptive ones such as \"Best Tailors\".</li><li>Avoid names close to existing marks in the same class.</li><li>Check that the domain and social handles are free.</li></ul>"),
        ("Steps to register", "<ol><li>Search the trademark records for similar marks.</li><li>Pick the class for your goods or services.</li><li>File the application with IPO.</li><li>Respond to any examination objections.</li><li>After publication and the opposition period, receive the certificate.</li></ol>"),
        ("Protecting the name after registration", "<p>Use the name consistently, watch for copycats and renew before expiry. Registration lasts ten years. See the costs in our <a href=\"/trademark-registration-cost-pakistan\">trademark registration cost guide</a>.</p>"),
    ],
    faqs=[
        ("Does SECP registration protect my brand name?", "No. Company registration does not give trademark rights; register the brand with IPO-Pakistan."),
        ("Can a descriptive name be registered?", "It is harder. Distinctive names are more likely to be accepted."),
        ("Can I use ™ before registration?", "™ can show you claim the mark; ® should be used only after registration."),
        ("How long does protection last?", "Ten years from registration, renewable."),
    ],
    sources=[("IPO-Pakistan", "https://ipo.gov.pk/"), ("SECP", "https://www.secp.gov.pk/")])

T["logo-registration-process-pakistan"] = dict(
    sections=[
        ("Two ways to protect a logo", "<p>A logo can be protected as a trademark, which protects it as a badge of your business in a class of goods or services, and its artwork can be registered for copyright. Both are handled by <a href=\"https://ipo.gov.pk/\" rel=\"noopener\">IPO-Pakistan</a>.</p>"),
        ("Preparing the logo for filing", "<ul><li>Use the final version, in the colours or black and white you want protected.</li><li>If the logo includes your brand name, consider filing the word mark separately too.</li><li>Keep proof that you own the design, such as the designer's assignment.</li></ul>"),
        ("Trademark filing steps", "<ol><li>Search for similar device marks.</li><li>File the application with the logo image and class.</li><li>Answer examination objections.</li><li>Publication in the Trade Marks Journal.</li><li>Registration if unopposed.</li></ol>"),
        ("Common mistakes", "<ul><li>Filing a draft logo and changing it later.</li><li>Not owning the artwork because the designer kept the rights.</li><li>Filing in the wrong class.</li></ul><p>For the name itself, see our <a href=\"/brand-name-registration-guide-pakistan\">brand name registration guide</a>.</p>"),
    ],
    faqs=[
        ("Is a logo registered as a trademark or copyright?", "It can be both: trademark for business use in a class, copyright for the artwork."),
        ("Should I register the name and logo separately?", "Often yes, so the name is protected even if the logo changes."),
        ("Who owns a logo made by a designer?", "Get a written assignment from the designer, so ownership is clearly yours."),
        ("Where is a logo registered?", "With IPO-Pakistan, which handles trademarks and copyright."),
    ],
    sources=[("IPO-Pakistan", "https://ipo.gov.pk/")])

T["tax-benefits-filer-pakistan"] = dict(
    sections=[
        ("Where filers pay less", "<table><tr><th>Transaction</th><th>Provision</th><th>Effect of filer status</th></tr>"
         "<tr><td>Bank profit</td><td>Section 151</td><td>Lower withholding rate</td></tr><tr><td>Buying property</td><td>Section 236K</td><td>Lower advance tax</td></tr>"
         "<tr><td>Selling property</td><td>Section 236C</td><td>Lower advance tax</td></tr><tr><td>Registering a vehicle</td><td>Section 231B</td><td>Lower advance tax</td></tr>"
         "<tr><td>Dividends</td><td>Section 150</td><td>Lower withholding rate</td></tr></table>"
         "<p>Rates change through finance acts; compare current figures with our <a href=\"/tools/filer-vs-non-filer-calculator\">filer vs non-filer calculator</a>.</p>"),
        ("Beyond tax rates", "<ul><li>Government and corporate tenders usually require ATL status.</li><li>Banks and lenders ask for returns as proof of income.</li><li>Visa applications often ask for tax returns.</li></ul>"),
        ("How to become a filer", "<p>File the return and wealth statement for the latest tax year on IRIS. If filing late, pay the Section 182A surcharge to join the ATL. Our <a href=\"/atl-registration-lahore\">ATL guide</a> explains the steps.</p>"),
        ("Staying a filer", "<p>The ATL is based on the latest return, so file every year by the due date. The Tax Year 2027 return is due by 30 September 2027 unless extended.</p>"),
    ],
    faqs=[
        ("What is the biggest benefit of being a filer?", "Lower withholding and advance tax on bank profit, property, vehicles and dividends."),
        ("How do I become a filer?", "File the income tax return and wealth statement on IRIS; late filers also pay the Section 182A surcharge."),
        ("Does filer status last forever?", "No. You must file every year to remain on the Active Taxpayers List."),
        ("Where can I compare filer and non-filer rates?", "In the Income Tax Ordinance schedules on FBR's website, or with our filer vs non-filer calculator."),
    ],
    sources=[("Federal Board of Revenue", "https://www.fbr.gov.pk/"), ("FBR IRIS portal", "https://iris.fbr.gov.pk/")])

# ---------------- professions ----------------
PROF_FAQ = {
    "Architects": [("Can an architect claim design software as an expense?", "Yes. Licences and subscriptions used for client work are business expenses when supported by invoices and payment records."),
                   ("Are fees from a client abroad taxed differently?", "Foreign fees received through a bank can have their own treatment; record each receipt and check the current rules for export of services."),
                   ("Do salaried architects with private projects file once?", "Yes. Salary and private-practice income are declared in the same return, each under its own head.")],
    "Engineers": [("Can an engineering contractor claim site costs?", "Yes. Labour, materials, equipment hire and site travel for a contract are deductible when supported by bills and payment records."),
                  ("Does PEC registration replace tax registration?", "No. PEC registration lets you practise or bid; tax registration with FBR, and with the province for services, is separate."),
                  ("Is withholding on contract payments the final tax?", "Whether it is final or adjustable depends on the payment type and current law; claim it in the return either way.")],
    "Exporters": [("Where are export sales tax refunds claimed?", "Through FBR's sales tax refund system, supported by monthly returns and matching export documents."),
                  ("Do exporters still file an annual return?", "Yes. Exporters file an income tax return each year, declaring export proceeds and the tax collected on them."),
                  ("What records support export proceeds?", "Bank realisation certificates, export invoices and goods declarations for each shipment.")],
    "Importers": [("Is advance tax paid at import claimed in the return?", "It is shown in the return; whether it can be adjusted depends on the importer's category under the current law."),
                  ("Where can I see my import data?", "Goods declarations and payments are recorded in Pakistan Customs' WeBOC system, which FBR also uses."),
                  ("Do commercial importers pay extra sales tax at import?", "Commercial importers may pay value-addition sales tax at import in addition to normal sales tax; check the current rules.")],
    "Traders": [("Is tax on my shop's electricity bill adjustable?", "Tax collected on commercial electricity bills is generally claimed in the return when the bills are kept."),
                ("How do traders show stock in the return?", "Record opening and closing stock at cost; profit is sales less purchases and expenses, adjusted for the change in stock."),
                ("Do wholesalers need sales tax registration?", "Wholesalers and certain retailers must register under the Sales Tax Act; check FBR's current criteria.")],
}


def prof(name, body, reg, extra_h2, extra, faq_extra):
    return dict(
        sections=[
            (f"How {name} are taxed", body),
            ("Registration and professional bodies", reg),
            (extra_h2, extra),
            (f"Filing for {name.lower()}", f"<p>{name} file Form 114 and the wealth statement on IRIS by the due date. Late filing penalties and the ATL surcharge are explained in our <a href=\"/tax-penalties-in-pakistan\">guide to tax penalties</a>.</p>"),
        ],
        faqs=PROF_FAQ[name] + [faq_extra],
        sources=[("Federal Board of Revenue", "https://www.fbr.gov.pk/"), ("FBR IRIS portal", "https://iris.fbr.gov.pk/")])

T["tax-filing-architects-pakistan"] = prof("Architects",
    "<p>An architect in private practice earns income from business or profession: design fees, supervision fees and consultancy. Expenses incurred to earn that income, such as office rent, staff salaries, software licences and travel to sites, are deductible when supported by records. Salaried architects are taxed on salary, with tax deducted by the employer.</p>",
    "<p>Architects practise under registration with the <a href=\"https://www.pcatp.org.pk/\" rel=\"noopener\">Pakistan Council of Architects and Town Planners</a> (PCATP). Tax registration is separate: register on IRIS for an NTN, and with PRA in Punjab if your architectural services are taxable services under the provincial schedule.</p>",
    "Tax deducted on fees",
    "<p>When companies and other prescribed persons pay for services, they deduct withholding tax under Section 153. Keep the certificates; the tax is credited in your return. Services provided to clients abroad have their own treatment, so record foreign receipts through your bank.</p>",
    ("Do architects charge provincial sales tax?", "Architectural and design services can be taxable services under provincial law, such as PRA in Punjab. Check the current schedule on the authority's website."))

T["tax-filing-engineers-pakistan"] = prof("Engineers",
    "<p>Engineers in employment are taxed on salary through employer deduction. Consulting engineers and engineering firms earn business income from design, supervision and contracts, and deduct expenses such as staff, equipment, software and site travel when supported by records.</p>",
    "<p>Engineers register with the <a href=\"https://www.pec.org.pk/\" rel=\"noopener\">Pakistan Engineering Council</a> (PEC) to practise, and firms bidding for projects often need PEC registration as constructors or operators. Tax registration with FBR and, for services, the provincial authority, is separate.</p>",
    "Contracts and withholding",
    "<p>Payments for contracts and services by companies and government bodies are subject to withholding under Section 153. Engineers working as contractors should keep each certificate, reconcile it with the contract value and claim it in the return.</p>",
    ("Do engineering firms pay provincial sales tax?", "Engineering and construction services can be taxable under provincial sales tax on services, such as PRA in Punjab. Check the current schedule."))

T["tax-filing-exporters-pakistan"] = prof("Exporters",
    "<p>Exporters pay tax on export proceeds, collected when the bank realises the proceeds under Section 154, and the treatment of that tax has changed in recent finance acts. Check the current rules in the Income Tax Ordinance on FBR's website for your tax year before preparing the return.</p>",
    "<p>Exporters register with FBR for income tax and sales tax, and with the relevant trade body or chamber where required. Export of goods is generally zero-rated for sales tax, and input tax refunds are processed through FBR's refund system.</p>",
    "Sales tax refunds",
    "<p>Because exports are zero-rated, many exporters have input tax refunds. Accurate monthly sales tax returns, matching invoices and timely refund claims are what keep refunds moving. The <a href=\"https://tdap.gov.pk/\" rel=\"noopener\">Trade Development Authority of Pakistan</a> publishes export support information.</p>",
    ("Are exports subject to sales tax?", "Export of goods is generally zero-rated, which allows input tax to be claimed back through the refund system."))

T["tax-filing-importers-pakistan"] = prof("Importers",
    "<p>Importers pay advance income tax at the import stage under Section 148, collected by Customs with duties, along with sales tax on imports. Whether the advance tax is adjustable against the final liability depends on the importer's category and the current law, so check FBR's rules for your tax year.</p>",
    "<p>Imports are cleared through Pakistan Customs' WeBOC system, and importers need an NTN and, usually, sales tax registration. Commercial importers may also pay value-addition sales tax at import.</p>",
    "Matching import data with the return",
    "<p>FBR holds import data from Customs. The return must reflect the same import values, duties and advance tax paid, or a notice may follow. Keep goods declarations and payment receipts for every consignment.</p>",
    ("Is advance tax on imports adjustable?", "It depends on the importer's category and the current law. Check FBR's rules for your tax year."))

T["tax-filing-traders-pakistan"] = prof("Traders",
    "<p>Traders, wholesalers and retailers are taxed on business income: sales minus cost of goods and expenses, adjusted for opening and closing stock. Accurate stock records and purchase invoices are what keep profit figures defensible.</p>",
    "<p>Traders need an NTN, and wholesalers and certain retailers must also register for sales tax. FBR has run schemes for retailers in major cities; check FBR's website for any scheme that currently applies to your shop.</p>",
    "Withholding on purchases and electricity",
    "<p>Tax is collected from traders at several points, such as on commercial electricity bills and purchases from manufacturers and distributors. These amounts are credited in the return when certificates and bills are kept.</p>",
    ("Do shopkeepers need sales tax registration?", "Wholesalers and certain retailers must register under the Sales Tax Act. Check FBR's current criteria for your business."))

# Area hubs: short hand-checked intros; the rest is built from content/lahore-areas data.
INTRO = {
    "dha": "DHA Lahore is a large planned housing authority spread over many phases, home to business owners, professionals and overseas Pakistanis. Most tax questions here involve property purchases and sales, rental income and wealth statements.",
    "cantt": "Lahore Cantt is administered by cantonment boards and mixes armed forces families, long-established traders around Saddar and newer housing schemes. Pension, rental and property questions are common.",
    "bahria": "Bahria Town Lahore is a private housing scheme off Canal Road, with many plot investors, overseas owners and shopkeepers in its commercial areas. File transfers, rent and property gains drive most questions.",
    "gulberg": "Gulberg is one of Lahore's main commercial districts, around Main Boulevard, MM Alam Road and Liberty Market, with offices, restaurants and retailers. Business registration and sales tax questions dominate.",
    "johar": "Johar Town is a large residential and commercial area home to the Expo Centre, Emporium Mall and Shaukat Khanum hospital, with many students, freelancers and small businesses.",
    "ait": "Allama Iqbal Town is an established residential area organised in named blocks, with busy markets such as Moon Market. Families, shopkeepers and landlords make up most enquiries.",
    "modeltown": "Model Town is one of Lahore's oldest planned communities, with large family plots and professionals. Subdividing, inheriting and renting out property are frequent tax topics.",
    "faisaltown": "Faisal Town is a residential area between Model Town and Johar Town, with commercial activity around Akbar Chowk. Shop owners and salaried families form most of its taxpayers.",
    "gardentown": "Garden Town and New Garden Town are residential areas near Barkat Market, a busy shopping centre. Retail, rental and salaried filing are common needs.",
    "gulshanravi": "Gulshan-e-Ravi is a residential area in west Lahore with many small traders and family businesses. Registration and first-time filing are common needs.",
    "samanabad": "Samanabad is an older residential area in west-central Lahore, with shops around its main roads and many long-settled families. Property inherited across generations is a frequent topic.",
    "shadman": "Shadman and the Jail Road area sit close to major hospitals and offices, with doctors, professionals and established families among residents.",
    "township": "Township in south Lahore combines housing blocks with small manufacturing and workshops nearby. Business income and salaried filing are common needs.",
    "wapda": "Wapda Town is a housing society first developed for WAPDA employees, now home to many salaried families, retirees and landlords.",
}

T["tax-consultant-shadman-lahore"] = dict(
    sections=[
        ("Tax help for Shadman and Jail Road residents",
         "<p>Shadman and the Jail Road corridor sit close to major hospitals, government offices and colleges, so many residents are doctors, consultants, civil servants and established families. Their tax questions usually involve more than one income source: a salary plus private practice, rent from a second property, or pension and bank profit.</p>"),
        ("Doctors with salary and private practice",
         "<p>A doctor employed by a hospital is taxed on salary through employer deduction, while fees from a private clinic or consultations are business income declared separately in the same return, with clinic rent, staff and equipment as expenses. Both appear in one return, and the wealth statement must explain assets funded by either.</p>"),
        ("Retirees, pensions and rental income",
         "<p>Pension and bank profit are declared with the tax already deducted by the bank shown as a credit. Rent from a house or upper portion is property income; if the tenant is a company, it deducts tax under Section 155, and that certificate is claimed in the return.</p>"),
        ("Filing status for Tax Year 2026", f"<p>{DEADLINE}</p>"),
        ("Working with us", "<p>Our office is at Shop No 34, Rizwan Block Market, Awan Town, Lahore, Monday to Saturday from 9:00 AM to 6:00 PM and Friday until 12:30 PM. Most Shadman clients share documents on WhatsApp. See our <a href=\"/tax-consultant-lahore\">Lahore area guide</a> for nearby areas.</p>"),
    ],
    faqs=[
        ("Can a doctor show salary and clinic income in one return?", "Yes. Salary and private practice income are both declared in the same return, under their own heads, with clinic expenses deducted from practice income."),
        ("Is rent from an upper portion taxable?", "Yes. It is property income declared in the return; tax deducted by a company tenant under Section 155 is credited."),
        ("Do retirees need to file?", "Retirees with taxable income or assets linked to filing should file; filing also keeps bank withholding at filer rates."),
        ("Do I need to visit your office?", "No. Most clients share documents on WhatsApp or email, and copies of everything filed are sent back."),
    ],
    sources=[("Federal Board of Revenue", "https://www.fbr.gov.pk/"), ("FBR IRIS portal", "https://iris.fbr.gov.pk/")])

T["tax-consultant-cavalry-ground-lahore"] = dict(
    sections=[
        ("Tax help for Cavalry Ground residents",
         "<p>Cavalry Ground is a residential area within Lahore Cantonment, with a busy commercial market and many serving and retired armed forces families, professionals and shop owners. Common questions involve pensions, rental income from family property, and returns for small businesses in the market.</p>"),
        ("Pensions and commuted pension",
         "<p>Pension received by a retired employee is declared in the return; the treatment of pension and commuted pension depends on the current provisions of the Income Tax Ordinance, so check them for your tax year. Bank profit on savings is declared with the bank's withholding certificate as a credit.</p>"),
        ("Shops in Cavalry Ground market",
         "<p>Shop owners declare sales, purchases, rent, staff and utilities, with stock at 30 June. Tax collected on commercial electricity bills is credited when the bills are kept. If you rent out a shop instead, the rent is property income.</p>"),
        ("Property in Lahore Cantt", "<p>Property in the cantonment is administered by the cantonment board, but federal tax on buying (Section 236K) and selling (Section 236C) applies as elsewhere, at lower rates for filers. Our <a href=\"/tax-consultant-lahore-cantt\">Lahore Cantt guide</a> lists block-level guides for the wider area.</p>"),
        ("Filing status for Tax Year 2026", f"<p>{DEADLINE}</p>"),
    ],
    faqs=[
        ("Is a pension taxable?", "Pension is declared in the return, and its tax treatment depends on the current Income Tax Ordinance provisions for your tax year. Keep the pension statement."),
        ("Is tax on my shop's electricity bill adjustable?", "Tax collected on commercial electricity bills is generally claimed as a credit in the return when the bills are kept."),
        ("Does federal tax apply to cantonment property?", "Yes. Advance tax on buying and selling property applies in cantonments as elsewhere, with lower rates for filers."),
        ("Can I file without visiting an office?", "Yes. Returns are filed on IRIS, and documents can be shared on WhatsApp or email."),
    ],
    sources=[("Federal Board of Revenue", "https://www.fbr.gov.pk/"), ("FBR IRIS portal", "https://iris.fbr.gov.pk/")])

# Extra depth for the shortest guides: one more section and two FAQs each.
EXTRA = {
    "kpra-registration-guide-pakistan": (("Practical checklist before applying",
        "<ul><li>Confirm that your service appears in the KP schedule and is provided in or from Khyber Pakhtunkhwa.</li><li>Keep the business bank account, premises details and the owner's or directors' CNICs ready.</li><li>Decide who will file the monthly return and keep the login secure.</li><li>Set up invoices that show the KPRA registration number and tax charged.</li><li>If you also provide services in Punjab or Sindh, check PRA and SRB obligations separately, because each province taxes services provided within it.</li></ul>"),
        [("Do I need separate registration in each province?", "If you provide taxable services in more than one province, each province's authority may require registration for services provided there. Check KPRA, PRA and SRB rules for your case."),
         ("What should a KPRA invoice show?", "Your registration number, the customer's details, the service, its value and the provincial sales tax charged, as KPRA's rules require.")]),
    "eobi-registration-guide-pakistan": (("Employer checklist",
        "<ul><li>Count all employees, including those on daily wages, to see whether you reach five.</li><li>Register the establishment, then each insured employee, with their CNIC.</li><li>Pay contributions every month and keep payment receipts.</li><li>Update EOBI when employees join or leave, so their contribution record stays accurate.</li><li>Keep wage registers and attendance records for inspection.</li></ul><p>Employees can check their contribution record with EOBI, so gaps in payment are easily spotted and lead to recovery action.</p>"),
        [("Can employees check their EOBI contributions?", "Yes. Insured persons can check their record with EOBI, which is why missed months are often noticed by employees themselves."),
         ("What if an employer does not register with EOBI?", "EOBI can assess and recover contributions for the period of default, with additional charges under its law. Registering on time is cheaper.")]),
    "srb-registration-guide-pakistan": (("Lahore businesses with Sindh clients",
        "<p>A Lahore-based firm that serves clients in Karachi does not automatically need SRB registration; the question is where the service is treated as provided under the provincial laws. Consultancy delivered from Lahore may fall under PRA, while services delivered on site in Sindh, or through an office there, can fall under SRB. Contracts, invoices and the place of performance decide it, so record them clearly.</p><p>Where both provinces could claim the same transaction, check each authority's rules before invoicing, so tax is charged once and correctly.</p>"),
        [("Does serving a Karachi client make me liable to SRB?", "Not automatically. It depends on where the service is treated as provided under provincial law. Services performed in Sindh or through a Sindh office usually fall under SRB."),
         ("What records help decide the province?", "Contracts, invoices, the place where the service is performed and the location of the office providing it.")]),
    "brand-name-registration-guide-pakistan": (("Searching before you file",
        "<p>A search of existing marks is the cheapest step in the whole process. IPO-Pakistan's trademark records show marks already filed or registered; look for identical and similar names in your class and in related classes. Check spelling variants, translations into Urdu and names that sound alike, because the Registrar considers how a name looks and sounds, not only its exact spelling.</p><p>If a close match exists, changing the name before you print packaging is far cheaper than defending an opposition later.</p>"),
        [("Does the Registrar compare names that sound alike?", "Yes. Marks are compared for how they look, sound and the idea they convey, so similar-sounding names in the same class can be refused."),
         ("Should I register the Urdu version of my brand?", "If you use the Urdu name on signs or packaging, consider protecting it as well, since it can be filed as a separate mark.")]),
    "social-security-registration-pakistan": (("Employer checklist",
        "<ul><li>Check whether your establishment and employees fall within the provincial law's coverage.</li><li>Register the establishment and every covered employee.</li><li>Pay contributions monthly and keep the receipts.</li><li>Report new joiners and leavers promptly.</li><li>Keep wage records, as inspectors compare them with contributions paid.</li></ul><p>Registered workers receive medical care through the institution's facilities, so delays in registration directly affect your staff.</p>"),
        [("What records do social security inspectors check?", "Wage registers, attendance records and the contributions paid for each covered employee."),
         ("Do I register new employees separately?", "Yes. Each covered employee is registered, and joiners and leavers should be reported promptly.")]),
    "trademark-registration-cost-pakistan": (("Hidden costs to plan for",
        "<ul><li>Responding to an examination objection, which may need a written reply.</li><li>Defending an opposition filed after publication.</li><li>Filing in extra classes as the business expands.</li><li>Recording a change of owner or address.</li><li>Renewal at the end of ten years.</li></ul><p>Budget for these at the start, and keep the application number and filing receipt safe, because every later step refers to them.</p>"),
        [("Is there a cost to renew a trademark?", "Yes. Renewal fees are paid to IPO-Pakistan at the end of each ten-year period; check the current fee schedule."),
         ("What makes trademark registration more expensive?", "Extra classes, examination objections and oppositions are the main reasons costs rise beyond the basic filing fee.")]),
    "tax-benefits-filer-pakistan": (("A simple example",
        "<p>Take a family that sells a plot and keeps the proceeds in a savings account. On the sale, advance tax under Section 236C is lower for a filer. On the bank profit that follows, withholding under Section 151 is lower for a filer. If they later buy a car, advance tax at registration under Section 231B is again lower. Across one year, the savings from filer rates on these three transactions are usually far larger than the cost of filing a return.</p>"),
        [("Is filing worth it if I have little income?", "Often yes, because filer status lowers withholding on property, vehicles and bank profit, which can outweigh the cost of filing."),
         ("Can a non-filer claim back the extra tax?", "Some withholding can be adjusted by filing a return, but higher non-filer rates are designed to make staying unfiled costly.")]),
    "logo-registration-process-pakistan": (("Using your logo while the application is pending",
        "<p>You can use the logo while the application is examined, and the filing date gives you priority over later applicants. Use the ™ symbol to show you claim the mark, and switch to ® only after registration. Keep dated examples of use, such as invoices, packaging and website screenshots, because they help if anyone challenges your mark or claims earlier use.</p>"),
        [("Can I use my logo before registration is complete?", "Yes. Use ™ while the application is pending and ® only after registration."),
         ("What evidence of use should I keep?", "Dated invoices, packaging, signboards and website screenshots that show the logo in use.")]),
    "tax-on-commercial-property-pakistan": (("Rental income in practice",
        "<p>Suppose you rent a shop in Lahore to a bank. The bank deducts tax from each rent payment under Section 155 and issues certificates. In your return, you declare the gross rent, claim the tax deducted as a credit and pay any difference. If the tenant is an individual who does not deduct tax, you declare the rent and pay the tax yourself. Keep the rent agreement, bank credits and certificates together for each property.</p>"),
        [("Does every tenant deduct tax on rent?", "No. Companies and other prescribed persons deduct tax under Section 155; individual tenants usually do not, so the landlord pays the tax with the return."),
         ("How is gross rent declared?", "Declare the full rent received in the return and claim any tax deducted by the tenant as a credit.")]),
    "business-compliance-checklist-pakistan": (("A first-month plan for a new business",
        "<ol><li>Week 1: register the NTN on IRIS and open a business bank account.</li><li>Week 2: decide whether you need sales tax registration with FBR or a provincial authority.</li><li>Week 3: if you have employees, check EOBI and provincial social security coverage.</li><li>Week 4: set up invoicing, record keeping and a filing calendar for monthly and yearly returns.</li></ol><p>Doing this in the first month avoids back-dated penalties later.</p>"),
        [("What is the first registration for a new business?", "The NTN with FBR, followed by a business bank account and any sales tax registration your activity needs."),
         ("Do small shops need EOBI?", "Only if they have five or more employees; below that, EOBI registration is not required under the Act.")]),
    "pra-registration-guide-pakistan": (("Common PRA mistakes",
        "<ul><li>Not registering because the business is small, when the service is in the schedule.</li><li>Charging provincial sales tax without being registered.</li><li>Missing monthly returns in months with no sales; a nil return is still due.</li><li>Not keeping copies of invoices issued.</li></ul><p>PRA's e-registration user guides explain each screen of the online form.</p>"),
        [("Is a nil PRA return needed in a month with no sales?", "Yes. Registered persons file monthly returns even when there are no taxable services in that month."),
         ("Can I charge PRA tax before registering?", "No. Charge provincial sales tax only after registration, and show the registration number on invoices.")]),
    "annual-company-filing-guide-pakistan": (("What happens if filings are missed",
        "<p>Late SECP filings attract additional fees and can lead to penalties for the company and its officers under the Companies Act 2017. Repeated non-filing can lead SECP to treat the company as defunct. On the tax side, a late company return attracts the Section 182 penalty and the Rs 100,000 Section 182A surcharge to join the Active Taxpayers List. A dormant company still files, so close a company formally if it will not trade.</p>"),
        [("Does a dormant company still file?", "Yes. A company that exists must file its SECP and FBR returns, even with no activity, unless it is formally closed."),
         ("What is the ATL surcharge for a company filing late?", "Rs 100,000 under Section 182A, in addition to the Section 182 late-filing penalty.")]),
    "tax-audit-preparation-checklist": (("During the audit",
        "<p>Keep one person responsible for all correspondence. Provide documents in the order the notice lists them, with a short index. Answer questions in writing and avoid giving explanations that are not supported by documents. If the officer proposes additions, ask for the basis in writing, because the final order must be based on the record. Our <a href=\"/tax-penalties-in-pakistan\">guide to tax penalties</a> explains what is at stake if tax is found short.</p>"),
        [("Should I meet the auditor in person?", "Written submissions on IRIS are usually best, as they create a record. Attend in person only when asked, with a representative if possible."),
         ("Can the audit be extended to other years?", "The notice states the tax year under audit; other years can be examined only under the law's provisions for those years.")]),
    "fbr-notice-after-tax-return-pakistan": (("Preventing the next notice",
        "<ul><li>Before filing, compare your income with bank and withholding data on IRIS.</li><li>Declare every property and vehicle in the wealth statement at cost.</li><li>Keep evidence for gifts and loans that fund assets.</li><li>File withholding statements if you are required to deduct tax.</li></ul>"),
        [("Can I see the data FBR has about me?", "IRIS shows withholding tax collected against your CNIC, which helps match your return to FBR's records."),
         ("Do notices come only after filing?", "No. Notices can also be issued to non-filers whose transactions show taxable income or assets.")]),
    "how-to-respond-to-tax-notices-pakistan": (("A reply template",
        "<p>Start with the notice reference, section and tax year. Then answer each point under its own number, refer to the attached document for every figure, and end with a list of attachments. Keep the reply factual and avoid new claims you cannot support. Save the IRIS acknowledgement with the reply and attachments in one folder.</p>"),
        [("What should the first line of a reply include?", "The notice reference number, the section of the law and the tax year it concerns."),
         ("Should a reply include extra explanations?", "Only explanations supported by documents. New, unsupported claims can lead to further questions.")]),
}
for _k, (_sec, _faqs) in EXTRA.items():
    T[_k]["sections"].append(_sec)
    T[_k]["faqs"].extend(_faqs)
