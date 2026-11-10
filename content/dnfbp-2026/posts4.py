"""DNFBP regional guides: one page per FBR DNFBP directorate under S.R.O. 1497(I)/2026 (checked 10 November 2026).
Smaller cities are covered inside their directorate's page, not on separate pages, to avoid near-duplicate city pages."""
from posts import WA, L, a, table, S_1497, S_FAQ23, S_GOAML, S_REGS, S_950, S_IRIS

DATE = "2026-11-10"
DLONG = "10 November 2026"
G = {"goaml": "/blogs/goaml-registration-dnfbp-pakistan", "prog": "/blogs/aml-cft-compliance-programme-dnfbp-pakistan",
     "acc": "/blogs/accountant-dnfbp-registration-aml-pakistan"}
HELP = ("help.dnfbp.fbr@gmail.com", "+92 51 9106606")


def duties(city):
    return (f'<p>The rules themselves are national: registration with FBR, a compliance officer, customer due diligence, sanctions screening, STRs and CTRs '
            f'on goAML, and record keeping apply the same way in {city} as anywhere else. Our {a(L["pillar"], "DNFBP registration guide")} explains them, '
            f'with sector detail for {a(L["rea"], "real estate agents")}, {a(L["jew"], "jewellers")} and {a(G["acc"], "accountants")}, and the '
            f'{a(G["goaml"], "goAML registration steps")}.</p>')


LHR = dict(
    slug="dnfbp-registration-lahore-punjab",
    title="DNFBP Registration Lahore & Punjab: Which FBR Office Is Yours",
    h1="DNFBP Registration in Lahore and Punjab: The FBR Directorate, Its Offices, and Which One Supervises Your Business",
    crumb="DNFBP Lahore & Punjab",
    description="Which FBR DNFBP officer supervises property dealers, jewellers and accountants in Lahore, Faisalabad, Multan, Gujranwala, Sialkot and the rest of Punjab.",
    keywords="DNFBP registration Lahore, DNFBP Lahore office, FBR DNFBP Punjab, property dealer DNFBP Faisalabad, jeweller DNFBP Multan, DNFBP Gujranwala Sialkot",
    category="AML/CFT — Lahore & Punjab",
    icon="🏙️",
    read="9 min read",
    banner="Under S.R.O. 1497(I)/2026, one Lahore-based directorate supervises DNFBPs across most of Punjab, split between three Additional Directors by tax office.",
    tldr=("FBR's Director (DNFBPs) Lahore supervises DNFBPs whose income tax cases sit with CTO Lahore, LTO Lahore or LTO Multan, and all DNFBPs doing business within "
          "the territory of RTO-I and RTO-II Lahore and the RTOs of Sialkot, Gujranwala, Faisalabad, Sargodha, Multan, Sahiwal and Bahawalpur (S.R.O. 1497(I)/2026, "
          "2 September 2026). Additional Director-I covers Lahore, Additional Director-II covers Sialkot, Gujranwala, Faisalabad and Sargodha, and Additional "
          "Director-III covers Multan, Sahiwal and Bahawalpur. Registration itself is online on IRIS, wherever you are."),
    lead=("Property dealers in Lahore, jewellers in Faisalabad and accountants in Multan all ask the same practical question: which FBR office is mine for DNFBP "
          "matters? The answer comes from the jurisdiction table FBR replaced on 2 September 2026. This page sets it out for Punjab outside the Islamabad "
          "directorate's area."),
    body=f"""
<h2 id="map">Your Tax Office Decides Your DNFBP Officer</h2>
<p>S.R.O. 1497(I)/2026 assigns DNFBPs by the income tax office that holds their case, or by the area in which they carry on business. Where neither fits, the place of residence decides. For the Lahore directorate:</p>
{table(["If your business or tax case is with…", "Your DNFBP officer (Lahore)"], [
    ["Corporate Tax Office Lahore or Large Taxpayers' Office Lahore", "Additional Director-I (DNFBPs), Lahore"],
    ["RTO-I Lahore or RTO-II Lahore", "Additional Director-I (DNFBPs), Lahore"],
    ["RTO Sialkot, RTO Gujranwala, RTO Faisalabad or RTO Sargodha", "Additional Director-II (DNFBPs), Lahore"],
    ["Large Taxpayers' Office Multan, or RTO Multan, RTO Sahiwal or RTO Bahawalpur", "Additional Director-III (DNFBPs), Lahore"],
])}
<p>All of them report to the Director (DNFBPs), Lahore. Day-to-day cases are assigned to Deputy or Assistant Directors (the notification lists eight) and inspectors working under the Director and Additional Directors. The Director General of DNFBPs has jurisdiction over the whole country.</p>
<p>Rawalpindi is not in this list: it falls under the {a("/blogs/dnfbp-registration-islamabad-rawalpindi", "Islamabad directorate")}.</p>

<h2 id="find-office">How to Find Your Income Tax Office</h2>
<p>Your RTO or LTO is shown in your IRIS profile and on your registration details. If you are not sure, check IRIS before writing to FBR; correspondence sent to the wrong officer slows replies.</p>

<h2 id="cities">What This Means City by City</h2>
{table(["City", "Typical DNFBPs", "Supervised by"], [
    ["Lahore", "Estate agents and dealers, builders and developers, jewellers and bullion dealers, corporate service providers", "Additional Director-I"],
    ["Faisalabad", "Property dealers, jewellers, accountants serving textile businesses", "Additional Director-II"],
    ["Gujranwala and Sialkot", "Property dealers, jewellers, accountants serving manufacturers and exporters", "Additional Director-II"],
    ["Sargodha", "Property dealers and jewellers", "Additional Director-II"],
    ["Multan, Sahiwal and Bahawalpur", "Property dealers, jewellers, agricultural-region accountants", "Additional Director-III"],
])}

<h2 id="registration">Registering From Punjab</h2>
<p>There is no separate Punjab form. Registration is done on FBR's IRIS portal; the system assigns your case by jurisdiction. Then register on goAML with the Financial Monitoring Unit. Most delays we see in Punjab come from mismatched details: a business name on the signboard that differs from IRIS, or a partnership registered with the Registrar of Firms under a slightly different name.</p>

<p>The registration, CDD, screening, reporting and record-keeping rules do not change between Punjab cities; only the supervising officer does. Start with our {a(L["pillar"], "DNFBP registration guide")}, then the guide for your trade: {a(L["rea"], "real estate agents")}, {a(L["jew"], "jewellers")} or {a(G["acc"], "accountants")}.</p>

<h2 id="scenarios">Two Punjab Scenarios</h2>
<p><strong>A dealer in Johar Town, Lahore</strong>, whose income tax case is with RTO-II Lahore, receives a letter about DNFBP registration. It comes under Additional Director-I. The dealer registers on IRIS, appoints the owner as compliance officer, registers on goAML and adopts a buyer-and-seller CDD form before the next deal.</p>
<p><strong>A jeweller in Faisalabad</strong> sells a bridal set for Rs 2.6 million in cash. That one sale makes the business a DNFBP and requires a CTR. Supervision sits with Additional Director-II, because the business falls within RTO Faisalabad's territory.</p>
<p>The examples are illustrative.</p>

<h2 id="contact">Contacting FBR About DNFBP Matters</h2>
<p>For general questions, FBR's DNFBP helpline is {HELP[1]} and its help email is {HELP[0]} (FBR FAQs, February 2023). Letters from your supervising officer will state the officer's designation; reply to that office and keep a copy.</p>

<h2 id="how-we-help">How We Help in Lahore and Punjab</h2>
<p>Our office is in Awan Town, Lahore, and we work with clients across Punjab over WhatsApp. We handle IRIS DNFBP registration, goAML, AML policies and replies to DNFBP letters. See also our {a("/tax-consultant-lahore", "tax services in Lahore")}. Replies within office hours.</p>
""",
    faqs=[
        ("Which FBR office handles DNFBPs in Lahore?",
         "The Director (DNFBPs), Lahore. Under S.R.O. 1497(I)/2026, Additional Director-I covers DNFBPs with CTO or LTO Lahore and those in the territory of RTO-I and RTO-II Lahore."),
        ("Who supervises DNFBPs in Faisalabad?",
         "Additional Director-II (DNFBPs), Lahore, who covers businesses within the territory of RTOs Sialkot, Gujranwala, Faisalabad and Sargodha."),
        ("Who supervises DNFBPs in Multan?",
         "Additional Director-III (DNFBPs), Lahore, covering LTO Multan and the RTOs of Multan, Sahiwal and Bahawalpur."),
        ("Is Rawalpindi under the Lahore DNFBP directorate?",
         "No. RTO Rawalpindi falls under the Director (DNFBPs), Islamabad."),
        ("Do I register at the Lahore office in person?",
         "No. DNFBP registration is done online on FBR's IRIS portal, and goAML registration is online with FMU."),
        ("What if my business is in one city and I live in another?",
         "The notification assigns DNFBPs mainly by tax office or place of business; place of residence applies to DNFBPs not otherwise covered."),
        ("When did these jurisdictions take effect?",
         "S.R.O. 1497(I)/2026 was issued on 2 September 2026 and replaced the earlier jurisdiction table."),
    ],
    sources=[S_1497, S_FAQ23, S_REGS, S_GOAML, S_IRIS],
    related=[(L["pillar"], "DNFBP Registration Guide"), ("/blogs/dnfbp-registration-islamabad-rawalpindi", "DNFBP Islamabad & Rawalpindi"), (L["rea"], "DNFBP for Real Estate Agents")],
    cta_h="DNFBP Registration Anywhere in Punjab",
    cta_p="From our Lahore office or over WhatsApp: IRIS registration, goAML and an AML policy for your business.",
    wa_text="Assalam o Alaikum, main Punjab mein hoon. DNFBP registration mein madad chahiye.",
)


KHI = dict(
    slug="dnfbp-registration-karachi-sindh",
    title="DNFBP Registration Karachi & Sindh: Which FBR Office Is Yours",
    h1="DNFBP Registration in Karachi and Sindh: FBR's Karachi Directorate, Hyderabad and Sukkur",
    crumb="DNFBP Karachi & Sindh",
    description="Which FBR DNFBP officer supervises estate agents, builders, jewellers and accountants in Karachi, Hyderabad and Sukkur under the September 2026 order.",
    keywords="DNFBP registration Karachi, DNFBP Karachi office, FBR DNFBP Sindh, estate agent DNFBP Karachi, jeweller DNFBP Karachi, DNFBP Hyderabad Sukkur",
    category="AML/CFT — Karachi & Sindh",
    icon="🌊",
    read="8 min read",
    banner="FBR's Karachi DNFBP directorate covers Karachi's corporate and large taxpayer offices, both Karachi RTOs, and the RTOs of Hyderabad and Sukkur.",
    tldr=("Under S.R.O. 1497(I)/2026, the Director (DNFBPs) Karachi supervises DNFBPs whose cases are with Corporate Tax Office-I or II Karachi or the Large "
          "Taxpayers' Office Karachi, and all DNFBPs doing business within the territory of RTO-I and RTO-II Karachi and the RTOs of Hyderabad and Sukkur. "
          "Additional Director-I covers the Karachi offices; Additional Director-II covers Hyderabad and Sukkur. Registration is online on IRIS; reports go to FMU "
          "through goAML."),
    lead=("Karachi's builders, estate agencies, jewellers and corporate service providers are spread across several income tax offices, including the corporate "
          "and large taxpayer offices, and the September 2026 order ties DNFBP supervision to those offices. This page shows where your business falls, and how "
          "Hyderabad and Sukkur fit in."),
    body=f"""
<h2 id="map">Karachi Directorate: Who Covers What</h2>
{table(["If your business or tax case is with…", "Your DNFBP officer (Karachi)"], [
    ["Corporate Tax Office-I or II Karachi", "Additional Director-I (DNFBPs), Karachi"],
    ["Large Taxpayers' Office Karachi", "Additional Director-I (DNFBPs), Karachi"],
    ["RTO-I or RTO-II Karachi", "Additional Director-I (DNFBPs), Karachi"],
    ["RTO Hyderabad or RTO Sukkur", "Additional Director-II (DNFBPs), Karachi"],
])}
<p>Both Additional Directors work under the Director (DNFBPs), Karachi, with Deputy or Assistant Directors (the notification lists five) and inspectors handling assigned cases. Where a DNFBP is not covered by the tax-office or business-location test, its place of residence in these areas decides.</p>

<h2 id="corporate">Why Companies in Karachi Often Sit With CTO or LTO</h2>
<p>Builders and developers that operate as companies may have their income tax cases with a Corporate Tax Office or the Large Taxpayers' Office rather than an RTO. For DNFBP purposes, that tax office decides the supervisor. Check your IRIS profile for the office name before you correspond with FBR.</p>

<h2 id="sectors">Karachi's Main DNFBP Sectors</h2>
{table(["Sector", "Points to watch in Karachi"], [
    ["Builders and developers", "Booking-to-possession relationships last years; keep CDD current and watch file transfers before possession."],
    ["Estate agents", "Identify both buyer and seller; overseas buyers need NICOP, POC or passport verification."],
    ["Jewellers and bullion dealers", "Any cash transaction of Rs 2 million or more makes the business a DNFBP and needs a CTR."],
    ["Accountants and corporate service providers", "Company formation and registered-address services are specified services; tax work alone is not."],
])}

<h2 id="hyderabad-sukkur">Hyderabad and Sukkur</h2>
<p>Businesses in the territory of RTO Hyderabad and RTO Sukkur are supervised by Additional Director-II (DNFBPs), Karachi. They follow the same registration and reporting process; there is no separate interior-Sindh form.</p>

<h2 id="services-tax">A Note on Sindh Sales Tax</h2>
<p>DNFBP status is a federal anti-money laundering matter and has nothing to do with Sindh sales tax on services. An estate agency providing taxable services in Sindh deals with the Sindh Revenue Board for that tax separately.</p>

<p>What differs in Sindh is only who supervises you. The substance of the duties is in our {a(L["pillar"], "DNFBP registration guide")}; Karachi builders and agencies should read the {a(L["rea"], "real estate agents")} guide, and gold traders the {a(L["jew"], "jewellers")} guide.</p>

<h2 id="scenarios">Two Sindh Scenarios</h2>
<p><strong>A Karachi developer</strong> registered as a private limited company, with its case at a Corporate Tax Office, is supervised by Additional Director-I. Its booking office accepts cash instalments, so it needs a CTR process for any cash of Rs 2 million or more and a review cycle for long-running buyer files.</p>
<p><strong>A jeweller in Hyderabad</strong> with its case at RTO Hyderabad is supervised by Additional Director-II. It registers on IRIS and goAML before the wedding season and keeps a CDD form at the counter for large cash sales.</p>
<p>The examples are illustrative.</p>

<h2 id="how-we-help">How We Help Sindh Businesses</h2>
<p>We work with Karachi, Hyderabad and Sukkur clients over WhatsApp: IRIS DNFBP registration, goAML, AML policies and replies to directorate letters. See also our {a("/blogs/tax-consultant-karachi", "tax services for Karachi")}. Replies within office hours.</p>
""",
    faqs=[
        ("Which FBR office supervises DNFBPs in Karachi?",
         "The Director (DNFBPs), Karachi. Additional Director-I covers CTO-I and CTO-II Karachi, LTO Karachi, and businesses in the territory of RTO-I and RTO-II Karachi."),
        ("Who supervises DNFBPs in Hyderabad and Sukkur?",
         "Additional Director-II (DNFBPs), Karachi, under S.R.O. 1497(I)/2026."),
        ("Is there a separate DNFBP registration for Sindh?",
         "No. Registration is online on FBR's IRIS portal for the whole country, with goAML registration through FMU."),
        ("Does DNFBP registration replace Sindh Revenue Board registration?",
         "No. DNFBP registration is under the federal AML law. Sindh sales tax on services is a separate provincial matter with the SRB."),
        ("My company's tax case is at LTO Karachi. Who is my DNFBP supervisor?",
         "Additional Director-I (DNFBPs), Karachi, who covers cases assigned to the Large Taxpayers' Office Karachi."),
        ("When did the current Karachi jurisdiction take effect?",
         "S.R.O. 1497(I)/2026, issued on 2 September 2026, sets the current jurisdiction table."),
    ],
    sources=[S_1497, S_FAQ23, S_REGS, S_GOAML, S_IRIS],
    related=[(L["pillar"], "DNFBP Registration Guide"), (L["rea"], "DNFBP for Real Estate Agents"), (L["jew"], "DNFBP for Jewellers")],
    cta_h="DNFBP Registration for Karachi and Sindh",
    cta_p="IRIS registration, goAML and AML policies for builders, agents, jewellers and accountants.",
    wa_text="Assalam o Alaikum, main Karachi / Sindh mein hoon. DNFBP registration mein madad chahiye.",
)


ISB = dict(
    slug="dnfbp-registration-islamabad-rawalpindi",
    title="DNFBP Registration Islamabad & Rawalpindi: FBR Office Guide",
    h1="DNFBP Registration in Islamabad, Rawalpindi and Gilgit-Baltistan: FBR's Islamabad Directorate",
    crumb="DNFBP Islamabad & Rawalpindi",
    description="Which FBR DNFBP officer supervises estate agents, developers, jewellers and accountants in Islamabad, Rawalpindi and Gilgit-Baltistan (SRO 1497/2026).",
    keywords="DNFBP registration Islamabad, DNFBP Rawalpindi, FBR DNFBP Islamabad office, estate agent DNFBP Islamabad, DNFBP Gilgit Baltistan",
    category="AML/CFT — Islamabad & Rawalpindi",
    icon="🏛️",
    read="8 min read",
    banner="FBR's Islamabad DNFBP directorate covers LTO Islamabad, RTO Islamabad, RTO Rawalpindi and Gilgit-Baltistan, and sits close to the Directorate General itself.",
    tldr=("Under S.R.O. 1497(I)/2026, the Director (DNFBPs) Islamabad supervises DNFBPs with cases at the Large Taxpayers' Office Islamabad and all DNFBPs doing "
          "business within the territory of RTO Rawalpindi, RTO Islamabad and Gilgit-Baltistan. Additional Director-I covers RTO Islamabad and LTO Islamabad; "
          "Additional Director-II covers RTO Rawalpindi and Gilgit-Baltistan. The Directorate General of DNFBPs, with all-Pakistan jurisdiction, also sits within "
          "FBR, whose DNFBP helpline is an Islamabad number."),
    lead=("Islamabad and Rawalpindi share one property market but two tax offices, and that split carries over to DNFBP supervision. This page shows which "
          "officer covers your business, including in Gilgit-Baltistan."),
    body=f"""
<h2 id="map">Islamabad Directorate: Who Covers What</h2>
{table(["If your business or tax case is with…", "Your DNFBP officer (Islamabad)"], [
    ["Large Taxpayers' Office Islamabad", "Additional Director-I (DNFBPs), Islamabad"],
    ["RTO Islamabad (business in Islamabad's territory)", "Additional Director-I (DNFBPs), Islamabad"],
    ["RTO Rawalpindi (business in Rawalpindi's territory)", "Additional Director-II (DNFBPs), Islamabad"],
    ["Business in Gilgit-Baltistan", "Additional Director-II (DNFBPs), Islamabad"],
])}
<p>The Additional Directors work under the Director (DNFBPs), Islamabad, with Deputy or Assistant Directors and inspectors handling assigned cases. A DNFBP not covered by the tax-office or business-location test falls here if it resides in these areas.</p>

<h2 id="twin-cities">The Twin Cities Split</h2>
<p>A dealer whose office is in Rawalpindi but who sells plots in Islamabad schemes is assigned by where the business is carried on and which tax office holds the case, not by where the plots are. In most cases, a Rawalpindi office with an RTO Rawalpindi case means Additional Director-II; an Islamabad office with an RTO Islamabad case means Additional Director-I. Check your IRIS profile if you have offices in both cities.</p>

<h2 id="sectors">Main DNFBP Sectors Here</h2>
{table(["Sector", "Points to watch"], [
    ["Estate agents and developers", "Many buyers are overseas Pakistanis or government employees; verify NICOP or POC for overseas buyers and apply PEP checks where a buyer holds or held a prominent public function."],
    ["Jewellers", "Cash sales of Rs 2 million or more bring the business into the regime and require a CTR."],
    ["Accountants and corporate service providers", "Company formation and registered-address services are specified services."],
])}

<h2 id="pep">Why PEP Checks Matter More in the Capital</h2>
<p>FBR's guidance defines politically exposed persons to include senior politicians and senior government, judicial and military officials, and their family members and close associates. In the capital, agents and jewellers are more likely to meet such customers, so the CDD form should ask the question and the policy should require enhanced due diligence and senior management approval when the answer is yes. A PEP customer is not prohibited; the extra checks are what the law requires.</p>

<h2 id="scenarios">Two Twin-Cities Scenarios</h2>
<p><strong>An estate agency on Murree Road, Rawalpindi</strong>, with its case at RTO Rawalpindi, handles a sale where the buyer is a retired senior government officer. The agency is supervised by Additional Director-II. The buyer is a politically exposed person, so the agency records the source of funds (for example, the sale deed of an earlier property and bank statements) and the owner approves the deal in writing before accepting the token.</p>
<p><strong>A developer in Islamabad</strong> registered as a company with its case at LTO Islamabad is supervised by Additional Director-I. Overseas buyers book units remotely, so its CDD process verifies NICOP or passport details and screens every buyer before the booking is confirmed.</p>
<p>The examples are illustrative.</p>

<p>For the duties themselves, our {a(L["pillar"], "DNFBP registration guide")} is the starting point, and {a(G["goaml"], "our goAML registration guide")} explains the separate FMU account every DNFBP needs.</p>

<h2 id="how-we-help">How We Help in the Twin Cities</h2>
<p>We work with Islamabad, Rawalpindi and Gilgit-Baltistan clients over WhatsApp: IRIS DNFBP registration, goAML, PEP-ready CDD forms and AML policies. See also our tax services for {a("/blogs/tax-consultant-islamabad", "Islamabad")} and {a("/blogs/tax-consultant-rawalpindi", "Rawalpindi")}. Replies within office hours.</p>
""",
    faqs=[
        ("Which FBR office supervises DNFBPs in Islamabad?",
         "The Director (DNFBPs), Islamabad. Additional Director-I covers LTO Islamabad and businesses in the territory of RTO Islamabad."),
        ("Who supervises DNFBPs in Rawalpindi?",
         "Additional Director-II (DNFBPs), Islamabad, who covers RTO Rawalpindi's territory and Gilgit-Baltistan."),
        ("Is Gilgit-Baltistan covered by a DNFBP directorate?",
         "Yes. S.R.O. 1497(I)/2026 places Gilgit-Baltistan under the Director (DNFBPs), Islamabad, through Additional Director-II."),
        ("Do I need extra checks for government officials as customers?",
         "Where a customer is a politically exposed person, FBR's guidance requires enhanced due diligence, including source of funds and senior management approval."),
        ("I have offices in both Islamabad and Rawalpindi. Which officer is mine?",
         "Supervision follows your tax office and place of business. Check which RTO holds your case in IRIS."),
        ("Is registration done at the Islamabad office?",
         "No. DNFBP registration is online on IRIS, and goAML registration is online with FMU."),
    ],
    sources=[S_1497, S_FAQ23, S_REGS, S_GOAML, S_IRIS],
    related=[(L["pillar"], "DNFBP Registration Guide"), ("/blogs/dnfbp-registration-lahore-punjab", "DNFBP Lahore & Punjab"), (L["rea"], "DNFBP for Real Estate Agents")],
    cta_h="DNFBP Registration in the Twin Cities",
    cta_p="IRIS registration, goAML and PEP-ready AML policies for agents, developers, jewellers and accountants.",
    wa_text="Assalam o Alaikum, main Islamabad / Rawalpindi mein hoon. DNFBP registration mein madad chahiye.",
)


PSH = dict(
    slug="dnfbp-registration-peshawar-kp",
    title="DNFBP Registration Peshawar & KP: Which FBR Office Is Yours",
    h1="DNFBP Registration in Peshawar and Khyber Pakhtunkhwa: FBR's KP Directorate",
    crumb="DNFBP Peshawar & KP",
    description="Which FBR DNFBP office supervises property dealers, jewellers and accountants in Peshawar, Abbottabad and Khyber Pakhtunkhwa (SRO 1497/2026).",
    keywords="DNFBP registration Peshawar, DNFBP KP, FBR DNFBP Khyber Pakhtunkhwa, property dealer DNFBP Peshawar, jeweller DNFBP Peshawar, DNFBP Abbottabad",
    category="AML/CFT — Peshawar & KP",
    icon="⛰️",
    read="7 min read",
    banner="Khyber Pakhtunkhwa has its own FBR DNFBP directorate, covering businesses within the territory of RTO Peshawar and RTO Abbottabad.",
    tldr=("Under S.R.O. 1497(I)/2026, the Director (DNFBPs), Khyber Pakhtunkhwa supervises all DNFBPs doing business within the territorial limits of the Regional "
          "Tax Offices Peshawar and Abbottabad, and DNFBPs not otherwise covered who reside there. An Additional Director, Deputy or Assistant Directors and "
          "inspectors work under the Director. Registration is online on IRIS and goAML."),
    lead=("Property dealers, jewellers and accountants in Khyber Pakhtunkhwa have a directorate of their own rather than one based in Islamabad or Lahore. This "
          "page explains its coverage and the points KP businesses most often ask about."),
    body=f"""
<h2 id="map">KP Directorate: Who Covers What</h2>
{table(["If your business is within…", "Your DNFBP officer"], [
    ["The territory of RTO Peshawar", "Director / Additional Director (DNFBPs), Khyber Pakhtunkhwa"],
    ["The territory of RTO Abbottabad", "Director / Additional Director (DNFBPs), Khyber Pakhtunkhwa"],
    ["Not covered above, but you reside in those areas", "Director (DNFBPs), Khyber Pakhtunkhwa"],
])}
<p>Cases are assigned by the Director or Additional Director to Deputy or Assistant Directors (the notification lists two) and inspectors.</p>

<h2 id="which-rto">Which RTO Covers Your District?</h2>
<p>The notification names the two RTOs, not the districts within them. Your income tax RTO appears in your IRIS profile; if it is RTO Peshawar or RTO Abbottabad, the KP directorate supervises you for DNFBP purposes.</p>

<h2 id="sectors">Points for KP Businesses</h2>
{table(["Sector", "What to watch"], [
    ["Property dealers", "Identify both parties; record how each payment is made; watch for third-party payers and purchases in the names of relatives other than a spouse or child, which FMU lists as red flags."],
    ["Jewellers and gold traders", "A cash transaction of Rs 2 million or more makes the business a DNFBP and requires a CTR. Keep the customer's CNIC and CDD form."],
    ["Cross-border links", "Customers or funds linked to jurisdictions FATF has called out need enhanced due diligence. Screen names against the UN and domestic proscribed lists before any deal."],
    ["Accountants", "Company formation, managing client money and registered-address services are specified services."],
])}

<h2 id="screening">Sanctions Screening Is Not Optional</h2>
<p>FBR expects every DNFBP to screen customers, their beneficial owners and agents against the UN Security Council consolidated list and Pakistan's proscribed persons lists. On a true match the business must freeze the funds without delay, refuse the transaction, file an STR with FMU and inform FBR immediately. Write down how and when you screen, and keep the result in the customer file.</p>

<h2 id="scenarios">Two KP Scenarios</h2>
<p><strong>A property dealer in Peshawar</strong> is asked to arrange the purchase of a house in the name of a buyer's nephew, with payment coming from a third person the dealer has never met. Purchases in the name of a relative other than a spouse or child, and third-party payments, are both FMU red flags. The dealer identifies the payer, asks about the source of funds, and if the answers do not hold up, declines the deal and files an STR without telling the parties.</p>
<p><strong>A jeweller in Abbottabad</strong> sells a gold set for Rs 2.2 million in cash during the wedding season. The business is a DNFBP, files a CTR on goAML, and is supervised by the KP directorate because it is within RTO Abbottabad's territory.</p>
<p>The examples are illustrative.</p>

<p>KP businesses follow the national rules set out in our {a(L["pillar"], "DNFBP registration guide")}; jewellers should also read the {a(L["jew"], "jewellers")} guide.</p>

<h2 id="how-we-help">How We Help KP Businesses</h2>
<p>We work with Peshawar, Abbottabad and other KP clients over WhatsApp: IRIS DNFBP registration, goAML, screening procedures and AML policies. See also our {a("/blogs/tax-consultant-peshawar", "tax services for Peshawar")}. Replies within office hours.</p>
""",
    faqs=[
        ("Which FBR office supervises DNFBPs in Peshawar?",
         "The Director (DNFBPs), Khyber Pakhtunkhwa, under S.R.O. 1497(I)/2026, for businesses within the territory of RTO Peshawar."),
        ("Is Abbottabad under the KP DNFBP directorate?",
         "Yes. The KP directorate covers DNFBPs within the territorial limits of both RTO Peshawar and RTO Abbottabad."),
        ("Do KP jewellers need to register as DNFBPs?",
         "A jeweller is a DNFBP when it engages in a cash transaction of Rs 2 million or more with a customer, and must then register and file CTRs."),
        ("What should I do if a customer matches a sanctions list?",
         "Freeze the funds without delay, refuse the transaction, file an STR with FMU on goAML and inform FBR immediately."),
        ("Does KPRA registration cover DNFBP requirements?",
         "No. KPRA collects provincial tax on services; it does not supervise anti-money laundering compliance, which for DNFBPs in KP is FBR's job."),
    ],
    sources=[S_1497, S_FAQ23, S_REGS, S_GOAML, S_IRIS],
    related=[(L["pillar"], "DNFBP Registration Guide"), (L["jew"], "DNFBP for Jewellers"), (L["rea"], "DNFBP for Real Estate Agents")],
    cta_h="DNFBP Registration in Khyber Pakhtunkhwa",
    cta_p="IRIS registration, goAML, sanctions screening procedures and AML policies, over WhatsApp.",
    wa_text="Assalam o Alaikum, main Peshawar / KP mein hoon. DNFBP registration mein madad chahiye.",
)


QTA = dict(
    slug="dnfbp-registration-quetta-balochistan",
    title="DNFBP Registration in Quetta & Balochistan: FBR Office Guide",
    h1="DNFBP Registration in Quetta and Balochistan: FBR's Quetta Directorate",
    crumb="DNFBP Quetta & Balochistan",
    description="Which FBR DNFBP office supervises property dealers, jewellers and accountants in Quetta and Balochistan under SRO 1497(I)/2026, and what they must do.",
    keywords="DNFBP registration Quetta, DNFBP Balochistan, FBR DNFBP Quetta office, property dealer DNFBP Quetta, jeweller DNFBP Quetta",
    category="AML/CFT — Quetta & Balochistan",
    icon="🏜️",
    read="7 min read",
    banner="Balochistan has its own FBR DNFBP directorate in Quetta, covering businesses within the territory of RTO Quetta.",
    tldr=("Balochistan's DNFBP supervisor is the Director (DNFBPs), Quetta. S.R.O. 1497(I)/2026 gives that office every DNFBP whose business lies in RTO Quetta's "
          "territory, plus residents of that area not assigned elsewhere. For cash-based trades the Rs 2 million rule is the key test: a single cash deal at that "
          "level makes a jeweller a DNFBP and requires a currency transaction report to FMU on goAML."),
    lead=("For property dealers, jewellers and accountants in Balochistan, the supervising DNFBP office is in Quetta. This page sets out its coverage and the "
          "points that matter most for businesses there."),
    body=f"""
<h2 id="map">Quetta Directorate: Who Covers What</h2>
{table(["Test in the notification", "Result"], [
    ["Business carried on in RTO Quetta's territorial jurisdiction", "Supervised from Quetta (Director and Additional Director, DNFBPs)"],
    ["Residence in that area, where no other rule applies", "Also supervised from Quetta"],
])}
<p>Your RTO is shown in your IRIS profile. If it is RTO Quetta, the Quetta directorate supervises you for DNFBP purposes.</p>

<h2 id="cash">Cash-Heavy Markets</h2>
<p>Where trade is largely in cash, the Rs 2 million thresholds matter most. A jeweller becomes a DNFBP through a single cash transaction of Rs 2 million or more with a customer, and every such transaction needs a CTR. Estate agents also file CTRs for cash of Rs 2 million or more. Splitting a payment into smaller cash amounts does not avoid reporting; FMU treats it as a red flag.</p>

<h2 id="cross-border">Cross-Border Risk and Enhanced Due Diligence</h2>
<p>FBR's guidance treats customers and funds linked to countries that FATF has called out, or that have weak AML controls, as higher risk. For such customers, collect information on the source of funds, get senior management approval and monitor the relationship more closely. Screen every customer against the UN Security Council list and Pakistan's proscribed persons lists before the deal.</p>

<h2 id="small-business">A Practical Setup for a Small Quetta Business</h2>
<ol>
<li>Register as a DNFBP on IRIS and on goAML.</li>
<li>As a sole owner without staff, you are the compliance officer (FBR Condition No. 3 of 2022).</li>
<li>Use a one-page CDD form for every customer in scope, with a CNIC copy and a screening note.</li>
<li>Keep a cash register that shows each large cash receipt and the CTR filed for it.</li>
<li>Write a short risk assessment and policy; our {a(G["prog"], "compliance programme guide")} shows what to include.</li>
</ol>

<h2 id="scenarios">A Quetta Scenario</h2>
<p><strong>A gold dealer in Quetta</strong> is offered Rs 4.5 million in cash for bullion by a customer who asks that no record be kept and says the money came from "trade" without further detail. Requests not to keep records, an unclear source of funds and large cash are all on FMU's red flag list for jewellers. The dealer asks for identification and an explanation; if suspicion remains, the dealer declines the transaction and files an STR, and because the cash offered is above Rs 2 million, any completed sale would also need a CTR.</p>
<p>The example is illustrative.</p>

<p>The full list of obligations is in our {a(L["pillar"], "DNFBP registration guide")}, and the {a(G["prog"], "AML/CFT compliance programme")} guide shows how to write the policy.</p>

<h2 id="how-we-help">How We Help Balochistan Businesses</h2>
<p>Quetta businesses can do the whole process with us remotely. We file the IRIS registration, open the goAML account, and give you a counter-ready CDD form and cash register format. For income tax work in the city, visit our {a("/blogs/tax-consultant-quetta", "Quetta page")}. We reply within office hours.</p>
""",
    faqs=[
        ("Which FBR office supervises DNFBPs in Quetta?",
         "The Director (DNFBPs), Quetta, under S.R.O. 1497(I)/2026, for businesses within the territorial jurisdiction of RTO Quetta."),
        ("Do I have to travel to Quetta's FBR office to register?",
         "No. DNFBP registration is online on IRIS, and goAML registration is online with FMU."),
        ("Who is the compliance officer in a one-person business?",
         "Under FBR's Condition No. 3 (2022), a sole proprietor with no employees is deemed to be the AML/CFT compliance officer."),
        ("Does splitting a cash payment avoid a CTR?",
         "No. FMU lists several smaller transactions adding up to a large total as a red flag, and it may call for an STR."),
        ("Is the Balochistan Revenue Authority involved in DNFBP supervision?",
         "No. BRA deals with provincial tax on services. Anti-money laundering supervision of DNFBPs in Balochistan sits with FBR's Quetta directorate."),
    ],
    sources=[S_FAQ23, S_1497, S_GOAML, S_REGS],
    related=[(L["pillar"], "DNFBP Registration Guide"), (G["prog"], "AML/CFT Compliance Programme"), (L["jew"], "DNFBP for Jewellers")],
    cta_h="DNFBP Registration in Balochistan",
    cta_p="IRIS registration, goAML, CDD forms and AML policies, over WhatsApp.",
    wa_text="Assalam o Alaikum, main Quetta / Balochistan mein hoon. DNFBP registration mein madad chahiye.",
)

POSTS = [LHR, KHI, ISB, PSH, QTA]
