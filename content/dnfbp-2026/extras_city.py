"""Region-specific depth for the five DNFBP directorate pages (SRO 1497(I)/2026; FBR guidance; checked 10 November 2026)."""
from posts import a, table, L

EXTRA = {}

EXTRA["dnfbp-registration-lahore-punjab"] = (f"""
<h2 id="add2">Additional Director-II's Area: Industrial Cities</h2>
<p>Sialkot, Gujranwala, Faisalabad and Sargodha are manufacturing and export centres, and their DNFBPs often look different from Lahore's. Accountants and consultants here frequently form companies for exporters and manufacturers, manage client payments, or provide registered addresses, all of which are specified services under FBR's list. Property dealers serve industrial buyers purchasing land for units and warehouses, and jewellers in these cities serve both local families and traders. For DNFBP purposes, all of them report to Additional Director-II (DNFBPs), Lahore, whatever their trade.</p>

<h2 id="add3">Additional Director-III's Area: South Punjab</h2>
<p>LTO Multan and the RTOs of Multan, Sahiwal and Bahawalpur fall under Additional Director-III. Agricultural land is a large part of property dealing in these districts, and FBR's real estate definition covers the purchase and sale of real property generally, not only urban plots. A dealer arranging a land sale identifies both buyer and seller, records how the price is paid, and treats cash of Rs 2 million or more as a CTR, exactly as a city dealer would.</p>

<h2 id="firms">Partnerships Registered With the Registrar of Firms</h2>
<p>Many Punjab estate agencies and jewellery businesses are partnerships registered with the provincial Registrar of Firms. For DNFBP registration the firm, not each partner, is the reporting entity: register the firm on IRIS under its own NTN, declare each partner and any other beneficial owner, and appoint one partner with enough authority as compliance officer. Use the firm's name exactly as on the registration certificate and bank account; a mismatch between "Al-Noor Estate" and "Al Noor Estate &amp; Builders" causes avoidable questions.</p>

<h2 id="letters">When a Letter Arrives From the Lahore Directorate</h2>
<ol>
<li>Note the officer's designation and the reply date.</li>
<li>Check whether it is about registration, information, or an inspection visit.</li>
<li>Gather what it asks for: registration details, policy, CDD files, CTR records.</li>
<li>Reply in writing to that office before the date, and keep proof of delivery.</li>
</ol>
""", [
    ("Who is the DNFBP supervisor for Sialkot exporters' accountants?",
     "Additional Director-II (DNFBPs), Lahore, who covers businesses within RTO Sialkot, Gujranwala, Faisalabad and Sargodha."),
    ("Does selling agricultural land count as a real estate transaction?",
     "Yes. FBR's definition covers the purchase and sale of real property; a dealer arranging a land sale has the same CDD and CTR duties."),
    ("Should a partnership register as a DNFBP, or each partner?",
     "The firm registers as the reporting entity under its own NTN, declaring the partners and beneficial owners, with one partner as compliance officer."),
])

EXTRA["dnfbp-registration-karachi-sindh"] = (f"""
<h2 id="booking-cycles">Builders' Booking Cycles: CDD That Lasts Years</h2>
<p>A Karachi apartment project can take years from booking to possession, with instalments throughout. FBR's guidance requires ongoing monitoring, not one check at booking. A practical approach for developers:</p>
<ul>
<li>Complete CDD and screening at booking, and rate the buyer's risk.</li>
<li>Record every instalment with its payment method; any cash of Rs 2 million or more needs a CTR.</li>
<li>Re-screen buyers when sanctions lists change, and review higher-risk buyers at least yearly.</li>
<li>Treat transfers of a booking to a new buyer as a new customer relationship, with fresh CDD.</li>
<li>Watch for sub-sales well above or below market value, which FMU lists as a red flag.</li>
</ul>

<h2 id="csp">Corporate Service Providers in Karachi</h2>
<p>Karachi has many practices that form companies, provide registered offices, and act as company secretaries for clients. FBR's FAQs treat these as Trust and Company Service Provider activities: forming a company with SECP for a client, providing a registered or correspondence address, and acting as or arranging a director, secretary or nominee shareholder. Practices outside ICAP and ICMAP that offer these services in the ordinary course of business are DNFBPs, and their supervisor depends on their own tax office: Additional Director-I for the Karachi offices.</p>

<h2 id="interior">Interior Sindh: Hyderabad and Sukkur</h2>
<p>Property dealers and jewellers in Hyderabad and Sukkur, and the areas within those RTOs, report to Additional Director-II (DNFBPs), Karachi. Land transactions, including agricultural land, are real property transactions for DNFBP purposes. The same identification, screening and CTR rules apply; the difference is only the supervising officer.</p>

<h2 id="first-steps">First Steps for a Karachi Business</h2>
<ol>
<li>Find your tax office in IRIS: CTO, LTO, RTO-I, RTO-II, Hyderabad or Sukkur.</li>
<li>Register as a DNFBP on IRIS and on goAML.</li>
<li>Appoint the compliance officer and put the policy and CDD forms in place.</li>
<li>For builders, set up an instalment register that links cash receipts to CTRs.</li>
</ol>
""", [
    ("Does transferring a booking to a new buyer need new CDD?",
     "Treat it as a new customer relationship: identify and screen the new buyer and record how they pay."),
    ("Are Karachi corporate service providers DNFBPs?",
     "Practices outside ICAP and ICMAP that form companies, provide registered addresses, or act as or arrange directors, secretaries or nominee shareholders in the ordinary course of business are DNFBPs under FBR's FAQs."),
    ("Who supervises property dealers in Hyderabad?",
     "Additional Director-II (DNFBPs), Karachi, who covers RTO Hyderabad and RTO Sukkur."),
])

EXTRA["dnfbp-registration-islamabad-rawalpindi"] = (f"""
<h2 id="gb">Gilgit-Baltistan Businesses</h2>
<p>S.R.O. 1497(I)/2026 places Gilgit-Baltistan under the Islamabad directorate, through Additional Director-II. Distance does not change the process: registration is on IRIS and goAML is online, so a property dealer or jeweller in Gilgit or Skardu can complete everything remotely. What deserves extra care is property purchased by buyers from outside the region, often for hotels or holiday homes: identify the buyer, record where the funds come from, and treat cash of Rs 2 million or more as a CTR.</p>

<h2 id="remote-buyers">Remote Buyers for Islamabad Projects</h2>
<p>Developers in Islamabad sell many units to buyers who never visit, including overseas Pakistanis. FBR's red flags include buyers who do not inspect the property, significant unexplained distance between agent and client, and payments from unusual or offshore sources. A sound remote-sale process:</p>
<ul>
<li>Verify identity with NICOP, POC or passport and NADRA's verification services.</li>
<li>Require payment from the buyer's own bank account, and record the remitting bank.</li>
<li>Screen the buyer and any attorney before confirming the booking.</li>
<li>Ask about the purpose of the purchase and record the answer.</li>
</ul>

<h2 id="pep-detail">Who Is a PEP in Practice</h2>
<p>FBR's guidance defines PEPs as individuals entrusted with prominent public functions, such as heads of state or government, senior politicians, senior government, judicial or military officials, senior executives of state-owned corporations and important political party officials, plus their family members and close associates. Ordinary government employees are not PEPs on that basis alone; the test is a <em>prominent</em> function. Your CDD form should ask the question, and your policy should say who decides when the answer is unclear.</p>
""", [
    ("Is every government employee a politically exposed person?",
     "No. FBR's definition covers individuals with prominent public functions, such as senior officials and politicians, and their family members and close associates."),
    ("Can a Gilgit-Baltistan business register without visiting Islamabad?",
     "Yes. DNFBP registration is on IRIS and goAML registration is online with FMU."),
    ("How should a developer handle buyers who never visit?",
     "Verify identity with NICOP, POC or passport, require payment from the buyer's own bank account, screen the buyer and any attorney, and record the purpose of the purchase."),
])

EXTRA["dnfbp-registration-peshawar-kp"] = (f"""
<h2 id="cash-markets">Cash-Heavy Trading and CTR Timing</h2>
<p>Property and gold deals in many KP markets are settled largely in cash. Two rules keep a business safe. First, any cash transaction with a customer of Rs 2 million or more needs a CTR, whether or not anything looks wrong. Second, a series of smaller cash payments that add up to a large total is a red flag in itself. Record each cash payment with the customer's name on the day it is received, and decide on the CTR at that point rather than at month end.</p>

<h2 id="family-property">Family and Inherited Property</h2>
<p>Many property sales in KP involve inherited land with several co-owners. Each seller is your customer: identify every co-owner who is selling, check the authority of anyone signing for others, and record how the price is split. Purchases in the name of a relative other than a spouse or child, or for someone without the means, are FMU red flags; family arrangements are common and lawful, but the reason should be recorded.</p>

<h2 id="abbottabad">Abbottabad and Hill-Area Property</h2>
<p>Businesses within RTO Abbottabad's territory are supervised by the KP directorate. Buyers from other cities purchasing land or homes in hill areas are ordinary customers, but the deal file should show who the buyer is, how they paid and why they are buying. Buyers who show no interest in the property's location or price, or who buy several properties quickly, fit FMU's red flag patterns.</p>

<h2 id="kp-first-steps">First Steps for a KP Business</h2>
<ol>
<li>Confirm in IRIS that your tax office is RTO Peshawar or RTO Abbottabad.</li>
<li>Register on IRIS as a DNFBP and on goAML with FMU.</li>
<li>Set up the screening log and CDD forms.</li>
<li>Write a cash policy that names who can accept large cash and how CTRs are filed.</li>
</ol>
""", [
    ("Do I need to identify every co-owner selling inherited land?",
     "Yes. Each seller is your customer, so identify every co-owner who is selling and check the authority of anyone signing for others."),
    ("When should a CTR decision be made?",
     "On the day the cash is received, with the customer's details recorded, rather than at month end."),
    ("Are hill-area property sales to outside buyers suspicious?",
     "Not in themselves, but the file should record who the buyer is, how they paid and why they are buying; buying several properties quickly with little interest in price is a red flag."),
])

EXTRA["dnfbp-registration-quetta-balochistan"] = (f"""
<h2 id="remote">Doing It All Remotely From Balochistan</h2>
<p>Businesses across Balochistan within RTO Quetta's territory do not need to travel to comply. DNFBP registration is on IRIS, goAML registration is online with FMU (with a hard copy of the authority letter posted to FMU), and FBR's DNFBP helpline is a telephone and email service. What does need to be on paper locally is the business's own file: CDD forms, cash register, screening notes and the policy.</p>

<h2 id="informal">Informal Money Transfers</h2>
<p>Pakistan's anti-money laundering framework treats unregulated value transfer as a serious risk. For a property dealer or jeweller, the practical point is simple: money that arrives through an unlicensed channel, or is paid on the customer's behalf by someone who is not the owner of the funds, has no reliable trail. FMU's red flags for both real estate and jewellers include third-party payments without a legitimate reason and unclear sources of funds. Ask how the money reached the customer, prefer bank channels, and record the answer.</p>

<h2 id="gold-trade">Gold Traders: Buying as Well as Selling</h2>
<p>Many gold traders buy old gold from the public as often as they sell. The Rs 2 million test applies to cash transactions with a customer in either direction. When paying cash for gold, identify the seller, record where they say the gold came from, screen the name, and file a CTR when the threshold is met. A seller who brings large quantities often, with no explanation, is a pattern to note.</p>

<h2 id="quetta-checklist">Quetta Business Checklist</h2>
<ul>
<li>☐ Tax office confirmed as RTO Quetta in IRIS.</li>
<li>☐ DNFBP registration on IRIS and goAML account approved.</li>
<li>☐ Compliance officer named (the owner, in a one-person business).</li>
<li>☐ CDD form, cash register and screening log in use.</li>
<li>☐ Short risk assessment and policy signed and dated.</li>
</ul>
""", [
    ("Does buying old gold for cash count for the Rs 2 million test?",
     "Yes. The test applies to cash transactions with a customer whether the trader is buying or selling."),
    ("What should I do if a customer's money came through an informal channel?",
     "Ask how the funds reached the customer and record the answer. Third-party payments without a legitimate reason and unclear sources of funds are FMU red flags that may call for an STR."),
    ("Is a hard copy needed for goAML registration?",
     "Yes. FMU's guideline requires the signed authority letter to be uploaded as a PDF and the hard copy to be sent to the Additional Director, FMU."),
])
