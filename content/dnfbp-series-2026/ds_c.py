"""DNFBP series 2, posts 8-10: sanctions screening, penalties, NRA 2023."""
from ds_common import *

S_PF = ("FBR: Guidelines on Implementation of TFS for Proliferation Financing for DNFBPs", "https://download1.fbr.gov.pk/Docs/2022828168252153FBR-DNFBPs_PFguidelines.pdf")

# 8 ---------------------------------------------------------------- targeted financial sanctions
TFS = post(
    slug=SL["tfs"],
    title="Sanctions Screening for DNFBPs: Lists, Freeze and Report",
    h1="Targeted Financial Sanctions Screening for Property Dealers, Jewellers and Accountants: The FBR Rules Step by Step",
    crumb="Sanctions Screening (TFS)",
    description="Regulation 13 makes DNFBPs screen every customer against UN and domestic sanctions lists. Which lists, what to do on a match, who to report to, and how fast.",
    keywords="targeted financial sanctions dnfbp, sanctions screening real estate agent, tfs screening pakistan, proscribed persons list dnfbp, freeze without delay fbr, dnfbp mobile app sanctions list",
    read="12 min read",
    banner="A sanctions match is the one situation where a DNFBP must freeze and report without delay. The screening has to happen before the deal, every time.",
    tldr=("Regulation 13 of FBR's DNFBP Regulations, made under section 7H of the AML Act, requires a mechanism to screen customers, potential "
          "customers and their beneficial owners against the persons designated or proscribed in notifications of the Ministry of Foreign Affairs, "
          "NACTA and the Ministry of Interior, including UN Security Council designations. On a positive or potential match you must freeze without "
          "delay, provide no services or funds, reject the transaction if the relationship has not begun, and report to FBR and FMU (an STR on "
          "goAML). FBR's proliferation financing guidelines say “without delay” means within hours of a UN designation. The DNFBP Mobile App carries the lists."),
    lead=("Most AML duties are about judgement: how risky is this customer, how much to ask. Targeted financial sanctions are different. If a buyer, "
          "seller or beneficial owner is a designated or proscribed person, the law leaves no room for weighing: the deal stops, assets are frozen and "
          "the authorities are told. That makes the screening step, checking names before you act, the part a small property office or jewellery "
          "shop most needs to get right. This guide explains which lists, when to screen, and exactly what to do with a match."),
    answers={
        "law": "Regulation 13 under section 7H of the AML Act: screen, and on a match freeze, refuse and report; never provide services to designated persons.",
        "lists": "UN Security Council designations and domestic proscriptions notified by the Ministry of Foreign Affairs, NACTA and the Ministry of Interior.",
        "who": "The customer, the beneficial owner, and anyone acting on the customer's behalf (FBR FAQs Q47).",
        "match": "Freeze without delay, provide no services, reject if not yet started, report to FBR and file an STR with FMU.",
        "when": "Before every deal, and again across your whole customer base whenever a list changes.",
    },
    svc=svc("A Screening Step Built Into Every Deal",
            "We set up a screening routine that fits a small office, with the official lists, a record of each check, and a written match procedure you can follow on the day.",
            ["Screening procedure covering customers, beneficial owners and representatives",
             "Access set-up for the DNFBP Mobile App and the official list sources",
             "A screening log for every deal, kept with the CDD file",
             "A match procedure: verify, freeze, refuse, report to FBR, STR to FMU",
             "DNFBP registration and goAML access if you do not have them"],
            ["Screening after token money is taken is too late to refuse cleanly",
             "Checking only the buyer misses a designated beneficial owner or attorney",
             "A match handled without reporting to FBR and FMU breaches regulation 13"],
            "Screening customers against sanctions lists?", "Set up my sanctions screening", "a sanctions screening procedure and set-up"),
    cta_p="Tell us how many deals you handle a month; we size the screening routine to that.",
    wa_text="Assalam o Alaikum, DNFBP ke liye sanctions (TFS) screening ka procedure set karwana hai.",
    about=about(),
    body=f"""
{SERIES("tfs")}

<h2 id="law">The Obligation in Regulation 13</h2>
<p>Regulation 13 of FBR's AML/CFT Regulations for DNFBPs 2020 implements section 7H of the AML Act. It has four parts:</p>
{table(["Clause", "Requirement"], [
    ["13(1)(a)", "Develop mechanisms, processes and procedures to screen and monitor customers and potential customers for matches with designated/proscribed persons, or their beneficial owners, in SROs and notifications of the Ministry of Foreign Affairs, NACTA and the Ministry of Interior"],
    ["13(1)(b)", "On a positive or potential match: freeze without delay under the respective SRO; provide no services, property or funds; reject the transaction, attempted transaction or customer if the relationship has not commenced"],
    ["13(1)(c)", "Report to the Board and FMU in the mode and manner prescribed"],
    ["13(1)(d)", "Implement other obligations under the AML Act, the United Nations (Security Council) Act 1948 and the Anti-Terrorism Act 1997"],
])}
<p>Regulation 13(2) adds a standing prohibition: no financial services to designated or proscribed persons “or to those who are known for their association with such entities and persons, whether under the proscribed/ designated name or with a different name”. Its Explanation defines associates as those acting on behalf of, at the direction of, or for the benefit of designated persons.</p>

<h2 id="lists">Which Lists to Screen Against</h2>
{table(["List", "Where FBR's guidance points", "Covers"], [
    ["UN Security Council Consolidated List", a(S_UN[1], "un.org consolidated list"), "Persons and entities designated by the Security Council and its committees"],
    ["Domestic proscriptions", a(S_NACTA[1], "NACTA proscribed organizations"), "Organisations and persons proscribed in Pakistan"],
    ["Provincial list named in FBR's short guidance", "nfs.punjab.gov.pk", "Listed in FBR's guidance for real estate agents and DPMS"],
    ["DNFBP Mobile App", a(S_APP[1], "FBR's app page"), "FBR's guidance says the lists, including the UN lists for proliferation financing, are available in the app"],
])}
<p>FBR's proliferation financing guidelines add the Strategic Export Control Division's UNSC list page and an optional Ministry of Foreign Affairs e-portal subscription for list updates, and name UN resolutions 1718 (DPRK) and 2231 (Iran) and their successors as the PF regimes.</p>

<h2 id="who">Who to Screen, and When</h2>
<p>FBR's FAQs (Q47): “Sanctions list screening should be performed for client, beneficial owner of the client and person(s) acting on behalf of a client.” The PF guidelines add the timing:</p>
<ul>
<li><strong>Before the relationship or transaction:</strong> screen new and potential customers as part of CDD.</li>
<li><strong>Existing customers:</strong> screen the whole customer database “without delay when any amendments are made” to a UN resolution's list.</li>
<li><strong>Without delay</strong> means “acting within hours of a designation by the UNSC”.</li>
</ul>
<p>The guidelines also warn to “be wary of possible use of false identities, dual nationalities, multiple names and identities”, and to check funds derived from property owned or controlled by a designated person. A beneficial owner can only be screened once identified; see our {a(B["ubo"], "beneficial ownership guide")}.</p>

<h2 id="match">What to Do on a Match</h2>
<ol>
<li><strong>Verify.</strong> A name match is not yet a true match. The PF guidelines say to take appropriate measures to verify the customer's identity against the designated person, using CNIC, date of birth, nationality and other identifiers.</li>
<li><strong>Freeze or reject.</strong> For an existing customer, freeze funds or property; for a new or potential customer, reject the customer if the transaction has not commenced (regulation 13(1)(b); FAQs Q48).</li>
<li><strong>Stop services.</strong> Provide no services, property or funds to the person.</li>
<li><strong>Report.</strong> FBR's FAQs (Q48) say to lodge an STR with FMU and notify FBR; the PF guidelines say to report any freezing, blocking or rejection to FBR's DNFBP wing and to CRMC immediately, and to file an STR for positive matches and for attempted transactions.</li>
<li><strong>Do not tip off.</strong> FBR's FAQs (Q45) describe disclosing that an STR has been filed as tipping off, an offence.</li>
</ol>
{table(["Situation", "Action"], [
    ["Existing customer, confirmed match", "Freeze; no services; report to FBR; STR to FMU"],
    ["New customer, confirmed match", "Reject; report to FBR; STR to FMU"],
    ["Name similar but different person (false positive)", "Record the check; the PF guidelines say the affected person may apply to MoFA to unfreeze any assets frozen"],
    ["Attempted transaction by a designated person", "STR to FMU, per the PF guidelines"],
])}

<h2 id="frozen">Frozen Assets After the Event</h2>
<p>The PF guidelines say freezing remains in effect until the person is delisted or a false positive is confirmed; that if assets cannot be segregated the entire asset is frozen; that frozen assets may receive dividends or interest, which must stay frozen; that no outgoing payment may be made without prior approval of the Ministry of Foreign Affairs; and that a reporting entity holding frozen assets must report any change to FBR's DNFBP wing by 15 January of the next calendar year.</p>

<h2 id="practice">A Screening Routine for a Small Office</h2>
{table(["When", "What you do", "What you keep"], [
    ["At first contact", "Screen the buyer, seller, any attorney and any beneficial owner", "Screenshot or printout with date and list version"],
    ["Before token or advance", "Confirm no match; if a match, stop and follow the match procedure", "Note on the CDD form"],
    ["When a list is updated", "Re-screen existing customers", "Log of the re-screen"],
    ["At least yearly", "Check the routine still uses current sources", "Note in your risk assessment"],
])}
<p>FBR's PF guidelines include a worked example: a seller, Mr X, selling property owned by his family company; his name and the company were “checked against Ministry of Foreign Affairs and Ministry of Interior lists, and the UNSC website – all okay”, alongside an adverse news check, and the screening was recorded in the CDD file. That is the level of record an inspector expects.</p>
""",
    faqs=[
        ("Do real estate agents in Pakistan have to screen sanctions lists?",
         "Yes. Regulation 13 of FBR's DNFBP Regulations requires real estate agents, DPMS and accountants to screen customers and potential customers against designated and proscribed persons."),
        ("Which sanctions lists should a DNFBP check?",
         "UN Security Council designations and domestic proscriptions notified by the Ministry of Foreign Affairs, NACTA and the Ministry of Interior. FBR's guidance points to the UN consolidated list, NACTA's list and the DNFBP Mobile App."),
        ("Who must be screened?",
         "The client, the client's beneficial owner and any person acting on the client's behalf (FBR FAQs Q47)."),
        ("What does freeze without delay mean?",
         "FBR's proliferation financing guidelines say without delay means acting within hours of a designation by the UN Security Council."),
        ("What if a name match is a false positive?",
         "Verify identity against the designated person's details and record it. FBR's PF guidelines say an affected person may apply to the Ministry of Foreign Affairs to unfreeze assets."),
        ("Do I report a match to FBR or FMU?",
         "Both. Regulation 13(1)(c) requires reporting to the Board and FMU; FBR's FAQs say to lodge an STR with FMU and notify FBR."),
    ],
    sources=[S_REG, S_FAQ, S_PF, S_TFS, S_REA, S_UN, S_NACTA, S_APP],
    related=[(B["ubo"], "Beneficial owners"), (B["pep"], "PEPs"), (X["goaml"], "goAML registration"), (X["svc"], "DNFBP compliance service")],
)

# 9 ---------------------------------------------------------------- penalties
PEN = post(
    slug=SL["pen"],
    title="DNFBP Penalties in Pakistan: AML/CFT Sanctions Rules 2020",
    h1="DNFBP Penalties Explained: What the AML/CFT Sanctions Rules 2020 Allow FBR to Do, and How to Respond",
    crumb="DNFBP Penalties and Sanctions",
    description="Up to Rs 100 million per violation, de-registration, removal of managers: the sanctions FBR can impose on DNFBPs, the factors it weighs, and your appeal right.",
    keywords="dnfbp penalty, aml cft sanctions rules 2020, sro 950 2020, fbr dnfbp fine, dnfbp penalty pakistan, aml penalty real estate agent",
    read="12 min read",
    banner="The maximum penalty is Rs 100 million per violation. The Rules also say what makes FBR go lower, and when it may impose nothing at all.",
    tldr=("Regulation 16 of FBR's DNFBP Regulations subjects any violation to sanctions under the AML Act. The AML/CFT Sanctions Rules 2020 (S.R.O. "
          "950(I)/2020) let FBR, as the AML/CFT regulatory authority, impose monetary penalties of up to Rs 100 million per violation on a "
          "risk-based scale, conditions on the business, de-registration, warnings, suspension or removal of managers, censure, and remedial "
          "directions. FBR must weigh gravity, duration, compliance history, financial strength, gains, remedial steps and intent. Rule 4(2) says no "
          "sanction may be imposed where the entity took all reasonable steps and exercised all due diligence. Every sanction comes with a written "
          "notice and a right of appeal."),
    lead=("Penalty figures are the part of DNFBP rules that travels fastest, usually as “Rs 100 million fine” with no context. The Sanctions "
          "Rules say more than that. They give FBR a range of tools, list the factors it must weigh, set an appeal process and, importantly for a "
          "careful business, say when no sanction should be imposed. This guide walks through the Rules as published, and what an unregistered or "
          "partly compliant business can do to put itself in the strongest position."),
    answers={
        "basis": "Regulation 16 links violations to the AML Act's sanctions; the Sanctions Rules 2020 (S.R.O. 950(I)/2020) set out how they are applied.",
        "types": "Monetary penalty, conditions on business, de-registration, action against managers, censure, and remedial directions (rule 4(1)).",
        "amount": "Up to Rs 100 million per violation, on the regulator's risk-based penalty scale (rule 6(1)).",
        "defence": "Rule 4(2): no sanction where the entity took all reasonable steps and exercised all due diligence to comply.",
        "appeal": "Rule 7 requires a written notice stating the right of appeal; rule 8 sets an appellate body and a decision within 180 days.",
    },
    svc=svc("Registration and Records That Show Reasonable Steps",
            "We register you if you are not registered, put the programme and files in place that rule 4(2) looks for, and help you answer a sanction notice if one arrives.",
            ["DNFBP registration if you are operating without it",
             "Written risk assessment, policy, officer and training record",
             "CDD, screening and reporting files brought up to date",
             "A remediation plan where gaps already exist",
             "Help drafting a response to an FBR notice and any appeal"],
            ["Operating unregistered is itself a breach of regulation 3",
             "Without written procedures and records there is nothing to show “reasonable steps”",
             "Ignoring a sanction notice loses the appeal route the Rules provide"],
            "Worried about DNFBP penalties?", "Make my business penalty-ready", "registration, a compliance gap review and remediation"),
    cta_p="Tell us whether you are registered and what records you keep; we tell you where the gaps are.",
    wa_text="Assalam o Alaikum, DNFBP penalty se bachne ke liye registration aur compliance check karwana hai.",
    about=about({"@type": "Legislation", "name": "AML/CFT Sanctions Rules, 2020 (S.R.O. 950(I)/2020)", "legislationJurisdiction": "PK", "legislationDate": "2020-10-01", "url": S_SANC[1]}),
    body=f"""
{SERIES("pen")}

<h2 id="basis">Where the Penalties Come From</h2>
<p>Regulation 16 of FBR's AML/CFT Regulations for DNFBPs 2020 is one line: “Any violation of any provision of these regulations shall be subject to sanctions issued under the AML Act.” Those sanctions are in the AML/CFT Sanctions Rules 2020, made by the Federal Government on 1 October 2020 as S.R.O. 950(I)/2020 under section 43 of the AML Act. Under rule 3(2), the regulatory authority, FBR for real estate agents, DPMS and accountants it supervises, imposes sanctions for contraventions of:</p>
<ul>
<li>sections 7(1), 7(3) to 7(6) and 7A to 7H of the AML Act, which cover reporting, CDD, record-keeping, compliance programmes and sanctions screening;</li>
<li>AML/CFT regulations, including FBR's DNFBP Regulations; and</li>
<li>regulations issued by FMU.</li>
</ul>
<p>Rule 3(4) limits sanctions to the reporting entity and its directors, senior management and officers in similar positions.</p>

<h2 id="types">The Sanctions FBR Can Impose</h2>
{table(["Rule 4(1)", "Sanction"], [
    ["(a)", "A monetary penalty under the Rules"],
    ["(b)", "Any condition, limitation or restriction on the business or product offerings"],
    ["(c)", "Revocation of licence or de-registration of the reporting entity"],
    ["(d)", "Temporary or permanent prohibition on a person in a management decision-making role: written warning, temporary suspension or removal from service"],
    ["(e)", "A statement of censure, warning or reprimand"],
    ["(f)", "A direction to act: comply within a set time through a remedial plan, conduct internal inquiries, or take disciplinary action against directors and officers"],
    ["(g)", "Any other sanction permitted under the regulator's own legislation"],
])}
<p>“Any or all” may be imposed together. For a property office or jewellery shop, a remedial direction with a deadline is as consequential as a fine: failing it leads to further sanctions under rule 6(2).</p>

<h2 id="amount">How Much: Up to Rs 100 Million per Violation</h2>
<p>Rule 6(1): the regulatory authority “shall apply monetary penalties upto Rs. 100 Million per violation, in accordance with the risk-based penalty scale of the respective AML/CFT Regulatory Authority.” Two words matter. <strong>Per violation</strong>: several failures can each attract a penalty. <strong>Risk-based scale</strong>: the amount is set by the regulator's scale, not automatically at the maximum. If a penalty is neither paid nor appealed, rule 6(2) allows further sanctions, and rule 6(4) requires significant sanctions, with the violation and the entity's name, to be made public quarterly.</p>

<h2 id="factors">What FBR Must Weigh</h2>
<p>Rule 4(3) lists the circumstances to take into account:</p>
<ol>
<li>the gravity and duration of the contravention;</li>
<li>what is needed for a dissuasive, proportionate and effective sanction;</li>
<li>the person's compliance history, including systemic consequences and previous contraventions;</li>
<li>the financial strength of the reporting entity;</li>
<li>profits gained or losses avoided;</li>
<li>remedial measures taken to address the cause;</li>
<li>how far the contravention was negligent or wilful; and</li>
<li>any other appropriate factor.</li>
</ol>
<p>Several are within your control: a short, early-corrected failure with remedial steps taken and no history weighs very differently from a long, wilful one.</p>

<h2 id="defence">The Reasonable Steps Rule</h2>
<p>Rule 4(2) is the most important sentence for a careful business: the authority “may not impose a sanction on a person if the authority is satisfied that the reporting entity took all reasonable steps and exercised all due diligence to ensure that the requirement would be complied with.” Reasonable steps are shown by documents: registration, a written risk assessment, an approved policy, a named compliance officer, training records, complete CDD files, screening logs and goAML filings. Our {a(X["prog"], "compliance programme guide")} explains how to build them.</p>

<h2 id="process">Notice and Appeal</h2>
{table(["Rule", "What it guarantees"], [
    ["7(1)(a)", "A written notice stating the proposed sanctions and the violations giving rise to them"],
    ["7(1)(b)", "The notice states your right of appeal and how to file it"],
    ["8(1)", "A right to appeal against any sanction imposed"],
    ["8(2)", "An appellate body of senior persons who did not take part in the original decision"],
    ["8(3)", "Published procedures covering how and where to appeal, days allowed, and a decision within at most 180 days"],
])}

<h2 id="common">The Failures Most Likely to Be Found</h2>
{table(["Failure", "Rule breached", "What fixes it"], [
    ["Operating without DNFBP registration", "Reg. 3(1)", a(B["docs"], "Register") + " now and record the date"],
    ["No written risk assessment or policy", "Reg. 4", "A documented assessment and a senior-approved policy"],
    ["No compliance officer recorded with FBR", "Reg. 7; FAQs Q26", "Appoint one; a sole proprietor without staff is deemed the officer (" + a(B["sole"], "sole proprietors") + ")"],
    ["Deal files without CDD or “Original seen” copies", "Regs. 6 and 8", "Complete CDD from now on; remediate open relationships"],
    ["No sanctions screening record", "Reg. 13", a(B["tfs"], "Screening log") + " for every customer"],
    ["No goAML access, CTRs not filed", "Reg. 14", a(X["goaml"], "goAML registration") + " and CTRs for cash of Rs 2 million or more"],
])}

<h2 id="unregistered">If You Have Been Operating Unregistered</h2>
<p>Registering now does not erase past non-compliance, but the factors in rule 4(3), especially remedial measures and whether the failure was wilful, reward acting before an inspection rather than after. A business that registers, writes its programme and starts complete files today is in a far stronger position than one found by FBR first. Our {a(B["cert"], "certificate and status guide")} explains how to evidence the registration once done.</p>
""",
    faqs=[
        ("What is the maximum penalty for a DNFBP in Pakistan?",
         "Rule 6(1) of the AML/CFT Sanctions Rules 2020 allows monetary penalties of up to Rs 100 million per violation, on the regulator's risk-based penalty scale."),
        ("Can FBR de-register a DNFBP?",
         "Yes. Rule 4(1)(c) lists revocation of licence or de-registration of the reporting entity among the sanctions."),
        ("Can managers be penalised personally?",
         "Rule 4(1)(d) allows warnings, temporary suspension or removal of persons in management decision-making roles, and rule 3(4) extends sanctions to directors and senior management."),
        ("Is there any defence to a DNFBP sanction?",
         "Rule 4(2) says no sanction may be imposed if the authority is satisfied the entity took all reasonable steps and exercised all due diligence to comply."),
        ("Can I appeal an FBR DNFBP penalty?",
         "Yes. Rule 7 requires a written notice stating your appeal right, and rule 8 requires an independent senior appellate body deciding within at most 180 days."),
        ("Are DNFBP penalties made public?",
         "Rule 6(4) requires significant sanctions, the nature of the violation and the entity's name to be made public quarterly."),
    ],
    sources=[S_SANC, S_REG, S_FAQ, S_INTRO],
    related=[(X["prog"], "AML/CFT compliance programme"), (B["cert"], "Certificate and status"), (B["tfs"], "Sanctions screening"), (X["svc"], "DNFBP compliance service")],
)

# 10 --------------------------------------------------------------- NRA 2023
NRA = post(
    slug=SL["nra"],
    title="NRA 2023: Why Real Estate Is 'Very High' Risk for DNFBPs",
    h1="Pakistan's National Risk Assessment 2023: Real Estate Rated Very High, DPMS High, and What It Means for Your Business",
    crumb="NRA 2023 and DNFBPs",
    description="Pakistan's NRA 2023 rates real estate agents Very High and DPMS High for ML vulnerability. What it means for registration, CDD and your risk assessment.",
    keywords="national risk assessment 2023 pakistan, nra 2023 real estate, nra 2023 dnfbp, real estate very high risk pakistan, dpms high risk nra, dnfbp risk assessment",
    read="11 min read",
    banner="FBR expects every DNFBP's own risk assessment to reflect the national one. Real estate starts at the top of the scale.",
    tldr=("FBR's summary of Pakistan's National Risk Assessment 2023 rates the inherent money laundering and terrorist financing vulnerability of "
          "real estate agents (including builders and developers) as Very High and of dealers in precious metals and stones as High, both supervised "
          "by FBR. Accountants are rated Low, and lawyers, TCSPs and notaries Low. The NRA names real estate, the construction industry, cash-intensive "
          "businesses and DPMS among channels used to launder proceeds. FBR's Regulations require each DNFBP to assess its own risks and consider risk "
          "assessments provided by FBR, and the NRA summary asks reporting entities to update their internal risk assessments and procedures to reflect it."),
    lead=("When FBR asks a property dealer or jeweller for a risk assessment, it is not asking for an essay. It is asking whether the business "
          "understands where it is exposed, starting from the national picture. Pakistan's third National Risk Assessment, completed in 2023 after "
          "the first in 2017 and an update in 2019, sets that picture. This guide summarises what the NRA 2023 summary says about DNFBPs and shows "
          "how a small business turns it into the documented assessment regulation 4 requires."),
    answers={
        "ratings": "Real estate agents (including builders/developers) Very High; DPMS High; accountants Low; lawyers, TCSPs and notaries Low.",
        "scale": "The NRA 2023 used four ratings: Very High, High, Medium and Low.",
        "channels": "The NRA names real estate, the construction industry, cash-intensive businesses and DPMS among channels used to launder proceeds.",
        "duty": "Regulation 4 requires a documented risk assessment that considers FBR's risk assessments; the NRA summary asks entities to update theirs.",
    },
    svc=svc("A Risk Assessment That Starts From the NRA",
            "We write your documented risk assessment from the NRA 2023 ratings down to your own customers, areas and deal types, and set the controls that follow from it.",
            ["Documented risk assessment under regulation 4, referencing NRA 2023",
             "Customer risk categories and the CDD level for each",
             "Controls for cash, overseas customers, companies and PEPs",
             "Policy approved by senior management, as regulation 4(2) requires",
             "DNFBP registration and goAML set-up where needed"],
            ["A risk assessment that rates real estate low contradicts the national assessment",
             "An undocumented assessment does not meet regulation 4(1)(a)",
             "A generic template ignores your own customers and areas"],
            "Need a risk assessment FBR will accept?", "Write my DNFBP risk assessment", "a documented DNFBP risk assessment"),
    cta_p="Tell us your sector, city and typical customer; we draft the assessment from the NRA down.",
    wa_text="Assalam o Alaikum, NRA 2023 ke mutabiq DNFBP risk assessment banwani hai.",
    about=about(),
    body=f"""
{SERIES("nra")}

<h2 id="what">What the NRA 2023 Is</h2>
<p>FBR publishes a “Summarized National Risk Assessment 2023 for DNFBPs, Legal Persons &amp; Limited Liability Partnerships (LLPs) and Waqf, Trusts &amp; Cooperatives” on its DNFBP risk assessment page. It explains that Pakistan “completed its first comprehensive ML/TF National Risk Assessment in 2017, updated it in 2019 and has conducted its third National Risk Assessment in 2023.” Its stated purpose is to help stakeholders understand their risks, and it says those subject to Pakistan's AML/CFT laws “are expected to use the findings of this document to update their internal risk assessment documents / Standard Operating Procedures”.</p>
<p>The NRA used four rating levels: Very High, High, Medium and Low, and adds that “low risk doesn’t mean that no action is required”.</p>

<h2 id="ratings">The DNFBP Ratings</h2>
{table(["DNFBP sector", "Supervisor (per NRA)", "NRA 2023 inherent vulnerability"], [
    ["Real estate agents (including builders/developers)", "FBR", "Very High"],
    ["Dealers in precious metals and stones (DPMS)", "FBR", "High"],
    ["Lawyers, TCSPs and notaries", "PBC / SECP", "Low"],
    ["Accountants", "ICAP / ICMA, FBR", "Low"],
])}
<p>The NRA assessed each sector on “their unique characteristics, clientele, the offered products and services, their geographic reach, and the channels they operate through.” The two sectors FBR supervises most heavily, real estate and DPMS, sit at the top. That is the context for FBR's registration drive, for Condition No. 2 on housing societies (see {a(B["dev"], "developers and societies")}) and for the 2026 amendment that added title transferring authorities to the real estate definition (see {a(B["sro"], "S.R.O. 1439")}).</p>

<h2 id="channels">How the NRA Says Money Is Laundered</h2>
<p>In its money laundering threat section, the NRA summary lists the channels used to launder proceeds of predicate offences as including “illegal MVTS/ hundi/ hawala, cash smuggling, bank accounts, real estate, construction industry, cash-intensive businesses, DPMS, and front &amp; shell companies”, and names “investment in real estate/ precious metals &amp; stones/ other high-value assets” among the ways proceeds are used. It assigned ML threat ratings to 21 predicate offences and rated corruption and bribery, illegal MVTS/hundi/hawala, tax crimes, smuggling and cash smuggling “Very High”.</p>
<p>For a property dealer or jeweller, the message is practical: cash, high-value assets and third-party payments are the features that make a deal risky, and those are the features your CDD and reporting should focus on.</p>

<h2 id="duty">What Regulation 4 Requires of You</h2>
{table(["Regulation 4", "Requirement"], [
    ["4(1)", "Identify, assess and understand risks for customers, countries or geographic areas, and products, services, transactions or delivery channels"],
    ["4(1)(a)", "Document the risk assessment"],
    ["4(1)(b)–(d)", "Consider all relevant risk factors; keep it up to date; be able to provide it to FBR"],
    ["4(2)", "Policies, controls and procedures approved by senior management, managing risks in your own assessment “and any other risk assessment publicly available or provided by FBR”"],
    ["4(2)", "Enhanced measures where higher risks are identified"],
    ["4(3)", "Simplified measures allowed for lower risks, never where there is suspicion"],
])}
<p>FBR's FAQs (Q28) tell DNFBPs to consider the nature, size and complexity of the business, products and delivery methods, types of customers, countries dealt with and FBR guidance, and to consider whether any product involves new technologies favouring anonymity.</p>

<h2 id="translate">Turning the National Rating Into Your Own</h2>
{table(["Risk factor", "Higher-risk signs (from FBR's guidance)", "What your assessment should say"], [
    ["Sector", "Real estate Very High; DPMS High (NRA 2023)", "Start from the national rating; do not rate your sector low"],
    ["Customers", "PEPs, complex companies or trusts, non-residents, unclear beneficial owners, adverse media", "How often you see them and the EDD you apply"],
    ["Geography", "FBR's CDD form note lists customers from border areas of KP and Balochistan and high-risk countries", "Where your customers come from"],
    ["Transactions", "Cash, third-party payments, rapid resale", "Your cash share and the CTR threshold of Rs 2 million"],
    ["Delivery", "Non-face-to-face deals, attorneys", "How you verify identity when you do not meet the customer"],
])}
<p>Each factor then points to a control: EDD for PEPs (see {a(B["pep"], "PEP rules")}), beneficial ownership checks for companies (see {a(B["ubo"], "UBO guide")}), screening for everyone (see {a(B["tfs"], "sanctions screening")}). Our {a(X["prog"], "compliance programme guide")} shows how the assessment fits the wider programme.</p>

<h2 id="example">Example: A Small DPMS in Gujranwala</h2>
<p>A family jewellery shop sells mostly to local wedding buyers, about a quarter of sales above Rs 2 million in cash. Its assessment starts from the NRA's High rating for DPMS, then records its own picture: local, known customers (lower), heavy cash (higher), occasional buyers paying for others (higher). It sets controls to match: CDD and screening for every cash sale of Rs 2 million or more, a CTR to FMU for each, questions on who is paying, and senior approval for any PEP. The owner signs the policy, as regulation 4(2) requires, and reviews it each year. That two-page document is what FBR's inspector asks for first.</p>
""",
    faqs=[
        ("How does Pakistan's NRA 2023 rate real estate agents?",
         "FBR's summary of the NRA 2023 rates real estate agents, including builders and developers, at Very High inherent ML/TF vulnerability."),
        ("How are jewellers rated in the NRA 2023?",
         "Dealers in precious metals and stones (DPMS) are rated High."),
        ("Are accountants high risk under the NRA 2023?",
         "No. The summary rates accountants Low, and lawyers, TCSPs and notaries Low."),
        ("Do I have to use the NRA in my own risk assessment?",
         "Regulation 4(2) requires your controls to manage risks in your own assessment and any risk assessment provided by FBR, and the NRA summary asks entities to update their internal assessments with its findings."),
        ("How often was the national risk assessment done?",
         "First in 2017, updated in 2019, and the third in 2023, according to FBR's summary."),
        ("Does a Low rating mean no action is needed?",
         "No. The NRA summary says low risk does not mean that no action is required; each stakeholder must still adopt controls for low-risk items."),
    ],
    sources=[S_NRA, S_REG, S_FAQ, S_REA, S_INTRO],
    related=[(X["prog"], "AML/CFT compliance programme"), (B["sro"], "S.R.O. 1439 changes"), (B["pep"], "PEPs"), (X["svc"], "DNFBP compliance service")],
)
