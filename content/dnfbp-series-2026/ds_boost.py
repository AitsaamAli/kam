"""Second section and two FAQs per guide, aimed at Google suggestions (gl=pk, 26 Nov 2026): "dnfbp registration status",
"dnfbp fbr contact number", "fbr dnfbp login", "dnfbp registration requirements", "property dealer registration punjab".
Facts from the same FBR texts as ds_common.py; nothing those texts do not state."""
from ds_common import *

BOOST = {
"dev": (f"""
<h2 id="noc-file">What to Put in the NOC or Approval File</h2>
<p>Condition No. 2 tells the authority what it must see; it does not prescribe a form. A file that answers both of its tests, and anticipates the questions FBR's Directorate may later ask, usually contains:</p>
<ul>
<li>proof of DNFBP registration of the entity that runs the scheme, in the real estate agent category, from its IRIS record;</li>
<li>the Registration Certificate from the concerned Director DNFBPs, once issued;</li>
<li>a letter naming the AML/CFT compliance officer, with designation and contact details, matching what was shared with FBR;</li>
<li>the scheme's written AML/CFT policy, approved by its board or chief executive as regulation 4(2) requires; and</li>
<li>evidence that goAML registration is in place for filing CTRs and STRs with FMU.</li>
</ul>
<p>Keeping the same set on file also answers the second paragraph of the condition, which obliges authorities to check schemes already approved. A scheme that can hand over these five items when asked is unlikely to have its next approval held.</p>
""", [
    ("Which authority enforces Condition No. 2 on housing societies?",
     "It is addressed to all public sector development departments and authorities, which must not issue NOCs or approvals to unregistered schemes; FBR's Directors DNFBPs keep the enforcement follow-up."),
    ("When did Condition No. 2 take effect?",
     "On 15 March 2022, according to the condition issued by FBR's Director General (DNFBPs) on 28 February 2022."),
]),
"cert": (f"""
<h2 id="category">Choosing the Right Category, and Businesses With More Than One</h2>
<p>Registration records the category of DNFBP you are, and the category decides your duties. FBR's Regulations, as amended by S.R.O. 1439(I)/2026, apply to three groups:</p>
{table(["Category", "When you fall in it", "The duty that changes most"], [
    ["Real estate agent", "Builders, developers, title transferring authorities, brokers and dealers when they execute, participate in or carry out transactional activity for property transfers", "CDD on buyers and sellers in every property deal (reg. 8(1)(a))"],
    ["DPMS", "Bullion dealers and sellers of jewellery, precious metals and stones, in a cash transaction of Rs 2 million or more", "CDD triggered by cash of Rs 2 million or more (reg. 8(1)(b))"],
    ["Accountant", "Non-ICAP/ICMAP practitioners carrying out the specified activities in the AML Act", "CDD when preparing for or carrying out those activities (reg. 8(1)(c))"],
])}
<p>Some businesses span two. A jeweller who also arranges plot sales for clients, or an accountant who forms companies and brokers property, carries on two DNFBP activities. The Regulations do not provide a combined category; regulation 3(2) requires any information FBR needs for registration, so the safe course is to declare every activity at registration and apply each set of CDD rules to the deals it covers. A category chosen too narrowly is a registration that is not “up to date”.</p>
<p>FBR's FAQs (Q25) give a dedicated email, help.dnfbp.fbr@gmail.com, and helpline, +92 51 9106606, for questions on AML/CFT compliance, including which category applies.</p>
""", [
    ("What is the FBR DNFBP helpline number?",
     "FBR's FAQs give +92 51 9106606 as the dedicated helpline and help.dnfbp.fbr@gmail.com as the dedicated email for AML/CFT compliance queries."),
    ("Which DNFBP office covers Lahore?",
     "Under S.R.O. 1497(I)/2026, the Director DNFBPs Lahore covers businesses in the jurisdiction of RTO-I and RTO-II Lahore, CTO Lahore, LTO Lahore and Multan, and the RTOs of Sialkot, Gujranwala, Faisalabad, Sargodha, Multan, Sahiwal and Bahawalpur."),
]),
"sole": (f"""
<h2 id="training">Training and the Independent Check, for One Person</h2>
<p>Regulation 7(1) lists four parts of a compliance programme, and two of them sound as if they need an organisation: an ongoing employee training programme, and an independent audit function to test the system. Regulation 7(2) explains what testing means: an assessment of the adequacy and effectiveness of the policies, controls and procedures, with recommendations. For a sole proprietor that can be scaled without losing the substance:</p>
<ul>
<li><strong>Training:</strong> keep a record of what you have studied each year, FBR's sector guidance and red flag indicators, FBR webinars, and any session you attend, and train any employee you take on before they handle customers.</li>
<li><strong>Hiring screening:</strong> regulation 7(1)(b) requires screening when hiring to ensure integrity and skills; for a small office, a CNIC copy, references and a short record of why the person was hired.</li>
<li><strong>Independent check:</strong> someone other than you, an outside adviser or a peer, reviews a sample of your deal files against your policy once a year and writes down what they found.</li>
</ul>
<p>The record is what matters. Rule 4(2) of the Sanctions Rules 2020 protects a business that took all reasonable steps; a dated training note and a one-page review are evidence of exactly that. See our {a(B["pen"], "penalties guide")}.</p>
""", [
    ("Does a sole proprietor need an independent audit for AML?",
     "Regulation 7(1)(d) requires an independent audit function to test the system. For a one-person business, an annual review of a sample of files by someone other than the proprietor, recorded in writing, serves that purpose."),
    ("Do I need to train myself as a one-person DNFBP?",
     "Regulation 7 requires an ongoing training programme. Keeping a dated record of the FBR guidance and sessions you have studied each year shows it in practice."),
]),
"docs": (f"""
<h2 id="reliance">Relying on Someone Else's CDD</h2>
<p>Property deals often involve two dealers, one for each side, and sometimes a bank or another regulated firm. Regulation 12 lets a DNFBP rely on a third party for identifying the customer and CDD, but only on four conditions: the relying DNFBP remains liable for any failure; it immediately obtains the CDD information from the third party; it keeps copies of the identification documents as regulation 6 requires; and it satisfies itself that the third party is supervised by an AML/CFT regulatory authority, or an equivalent foreign authority, and has CDD and record-keeping measures in place. FBR's FAQs (Q40) put it simply: you can authorise another person to carry out CDD, “however, you are still legally responsible”. In practice, take copies of the other dealer's CDD file for your customer, and check that the dealer is itself a registered DNFBP.</p>
""", [
    ("Can I use another dealer's KYC documents for my customer?",
     "Regulation 12 allows reliance on a supervised third party, but you remain liable, must immediately obtain the CDD information and keep copies of the identification documents."),
    ("Is NADRA verification accepted for CDD?",
     "FBR's short guidance for real estate agents refers to electronic verification through NADRA's identity verification services alongside original documents."),
]),
"pep": (f"""
<h2 id="becomes">When an Existing Customer Becomes a PEP</h2>
<p>PEP status is not fixed at onboarding. Regulation 9(3)(a) requires systems to identify PEPs “both prior to establishing a business relationship or conducting a transaction, and periodically throughout the course of the business relationship”, and regulation 9(3)(b) requires senior management approval to continue a relationship where a customer “subsequently becomes a PEP”. FBR's short guidance for real estate agents gives the same instruction in plain terms: during ongoing monitoring, if there is a material change in the customer's profile, “like customer becomes a PEP, non-resident etc.”, update the CDD.</p>
<p>For a property office with repeat investors, or a jeweller with regular family customers, that means three habits: ask the PEP question again at each new deal, note public appointments and election results that affect known customers, and record the senior approval when a long-standing customer's status changes. FBR's FAQs (Q36) suggest review cycles of at least once a year for high-risk cases, every two years for medium and every three years for low risk; a PEP relationship sits in the first group.</p>
""", [
    ("How often should PEP customers be reviewed?",
     "FBR's FAQs suggest at least once a year for very high or high-risk relationships, which is where PEP relationships sit under regulation 9."),
    ("What if a customer becomes a PEP after the deal?",
     "Regulation 9(3) requires periodic identification during the relationship and senior management approval to continue it once the customer becomes a PEP."),
]),
"ubo": (f"""
<h2 id="aop">Partnerships, AOPs and Family Firms</h2>
<p>Many Pakistani buyers and sellers are partnerships or associations of persons rather than companies. The same principle applies: the beneficial owners are the natural persons who ultimately own or control the firm. FBR's FAQs (Q34) list the partnership agreement as the proof-of-existence document for a legal person or arrangement, and regulation 8(7) requires you to understand the customer's ownership and control structure whatever its form. For a firm, that usually means the registered or notarised partnership deed showing partners and shares, the CNIC of each partner, the NTN of the firm, and a letter or authority from the partners for the person signing. Where one partner is itself a company, look through it to its own beneficial owners as in the company test. A family business run by one brother but owned in equal shares by four has four beneficial owners by ownership, and possibly a fifth controller by other means, such as a father who directs the business without holding a share.</p>
""", [
    ("Who are the beneficial owners of a partnership firm?",
     "The natural persons who ultimately own or control it, usually the partners shown in the partnership deed, and anyone controlling the firm by other means."),
    ("Which document proves a partnership's existence for CDD?",
     "FBR's FAQs list the partnership agreement among proof-of-existence documents, alongside identity documents of the partners and the authority of the person acting."),
]),
"tfs": (f"""
<h2 id="countries">High-Risk Countries: A Separate Screening Step</h2>
<p>Sanctions screening is about named persons. A second, related step concerns countries. Regulation 11 of FBR's Regulations requires DNFBPs to apply the countermeasures the Federal Government indicates on the recommendation of the National Executive Committee. The Counter-measures for High Risk Jurisdictions Rules 2020 (S.R.O. 951(I)/2020) explain how: the National Executive Committee notifies a list of high-risk countries, including those subject to a FATF call for countermeasures; the Financial Monitoring Unit publishes the list and its updates on its website; and rule 6 requires every reporting entity to apply enhanced due diligence, proportionate to the risk, to business relationships and transactions with natural and legal persons from any country on that list. Regulation 9(1)(b) of FBR's Regulations also makes EDD compulsory for persons from countries for which FATF calls for it. FBR's short guidance for real estate agents gives North Korea, Iran and Afghanistan as examples of high-risk countries in its CDD form note. So a complete screening step checks two things: whether the person is listed, and whether the person or the funds come from a listed country.</p>
""", [
    ("Where is Pakistan's high-risk countries list published?",
     "Under the Counter-measures for High Risk Jurisdictions Rules 2020, the Financial Monitoring Unit publishes the list notified by the National Executive Committee on its official website."),
    ("What must a DNFBP do with a customer from a high-risk country?",
     "Apply enhanced due diligence proportionate to the risk, under rule 6 of the 2020 Rules and regulation 9(1)(b) of FBR's Regulations."),
]),
"pen": (f"""
<h2 id="inspection">How a Breach Usually Comes to Light: Inspection</h2>
<p>Regulation 15 of FBR's Regulations says the records a DNFBP must keep “shall be subject to inspection by FBR, as laid down in section 6A(2)(f) of AML Act, who may be assisted by other law enforcement agencies.” Regulation 6(5), as restated by S.R.O. 1439(I)/2026 in August 2026, requires the DNFBP to “promptly satisfy any inquiry or order from the board, designated law enforcement agencies, and FMU for the supply of CDD information and transaction records”. In practice an inspection tests the documents a sanction decision will later be based on:</p>
{table(["What an inspector asks for", "Where the requirement comes from"], [
    ["Proof of registration and the compliance officer", "Regulations 3 and 7"],
    ["The documented risk assessment and approved policy", "Regulation 4"],
    ["A sample of customer files with CDD and “Original seen” copies", "Regulations 6 and 8"],
    ["The refused-customer list", "Regulation 6"],
    ["Screening records", "Regulation 13"],
    ["CTRs and STRs filed on goAML", "Regulation 14"],
    ["Training and independent review records", "Regulation 7"],
])}
<p>A business that can produce these quickly has met regulation 6(5) and has the evidence that rule 4(2) of the Sanctions Rules asks for. One that cannot has two problems at once: the underlying gaps, and the failure to satisfy the inquiry promptly.</p>
""", [
    ("Can FBR inspect a DNFBP's records?",
     "Yes. Regulation 15 subjects the records DNFBPs keep to inspection by FBR under section 6A(2)(f) of the AML Act, with possible assistance from other law enforcement agencies."),
    ("How quickly must I produce records when FBR asks?",
     "Regulation 6(5), as restated in 2026, requires a DNFBP to promptly satisfy any inquiry or order from FBR, designated law enforcement agencies and FMU for CDD information and transaction records."),
]),
"nra": (f"""
<h2 id="update">Keeping the Assessment Current: New Products and Technology</h2>
<p>A risk assessment written once and filed away does not meet regulation 4(1), which requires DNFBPs to keep the assessment up to date and to have mechanisms to provide it to FBR. Three events should prompt a review:</p>
<ol>
<li><strong>A new national or FBR assessment.</strong> The NRA summary itself asks entities to update their internal assessments and procedures in line with its findings.</li>
<li><strong>A change in your own business.</strong> A dealer who starts handling overseas buyers, a jeweller who starts taking large online orders, or a society opening file trading.</li>
<li><strong>A new product, practice or technology.</strong> Regulation 5 requires a DNFBP to identify and assess the ML and TF risks of new products, business practices and delivery mechanisms, and the use of new or existing technology, and to do so <em>before</em> launching them. FBR's FAQs (Q28) ask DNFBPs to consider whether any of their products involve new or developing technologies that may favour customer anonymity.</li>
</ol>
<p>Selling plots through an app or social media, accepting payment through a new digital channel, or offering instalment files to buyers you never meet are all examples where regulation 5 applies. The review need not be long, a dated page recording the change, its risks and the controls added, but it must exist before the new practice starts.</p>

<h2 id="simplified">Where Lower Risk Allows Simplified Measures</h2>
<p>The NRA's ratings do not mean every customer is high risk. Regulation 10 allows simplified due diligence where lower risks are identified through an adequate analysis, for example verifying identity after the relationship begins or reducing the frequency of monitoring, and FBR's FAQs (Q36) suggest review cycles of up to three years for low-risk customers. Regulation 10(3) adds the limit: no simplified measures whenever there is a suspicion of ML or TF. For a real estate agent starting from a Very High sector rating, simplified measures should be the documented exception, not the default.</p>
""", [
    ("Do I need a new risk assessment when I start selling online?",
     "Regulation 5 requires a DNFBP to assess the ML/TF risks of new products, practices, delivery mechanisms and technologies before launching them."),
    ("Can a real estate agent use simplified due diligence?",
     "Regulation 10 allows it only where lower risks are identified through adequate analysis, and never where there is suspicion; for a sector rated Very High it should be the documented exception."),
]),
}
