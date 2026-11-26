"""DNFBP series 2, posts 1-4: S.R.O. 1439 amendments, developers/societies, certificate and status, sole proprietors."""
from ds_common import *

# 1 ---------------------------------------------------------------- S.R.O. 1439(I)/2026
SRO = post(
    slug=SL["sro"],
    title="S.R.O. 1439(I)/2026: What Changed for DNFBPs in Pakistan",
    h1="S.R.O. 1439(I)/2026 Explained: FBR's August 2026 Changes to the DNFBP Regulations, Clause by Clause",
    crumb="S.R.O. 1439(I)/2026 DNFBP Changes",
    description="FBR's S.R.O. 1439(I)/2026 rewrote key DNFBP definitions: jewellers became DPMS, title transferring authorities joined real estate agents. What it means.",
    keywords="sro 1439 2026, sro 1439(i)/2026 fbr, dnfbp regulations amendment 2026, dpms definition fbr, title transferring authorities dnfbp, fbr aml cft regulations 2026",
    read="12 min read",
    banner="FBR amended its DNFBP Regulations on 27 August 2026. If you deal in property, gold, gems or stones, check whether the new wording covers you.",
    tldr=("On 27 August 2026 FBR issued S.R.O. 1439(I)/2026, amending its AML/CFT Regulations for DNFBPs 2020 (S.R.O. 924(I)/2020). The word "
          "“Jewellers” is replaced throughout by “DPMS” (dealers in precious metals and dealers in precious stones), defined to "
          "include bullion dealers and sellers of jewellery, precious stones and metals, including articles of gold, platinum, diamonds and pearls, "
          "when they take a cash transaction of Rs 2 million or more. The real estate agent definition now names title transferring authorities "
          "alongside builders, developers, brokers and dealers. The record-keeping rules for litigation and for enquiries from FBR, law enforcement "
          "and FMU are restated. Registration with FBR remains compulsory under regulation 3."),
    lead=("Most DNFBP guidance in circulation still quotes the 2020 text of FBR's Regulations. That text changed in August 2026. S.R.O. 1439(I)/2026 "
          "is short, two pages, but it rewrites the definitions that decide who is a DNFBP, and therefore who must register with FBR, appoint a "
          "compliance officer and file reports on goAML. This guide sets the old wording beside the new, explains what each change means in "
          "practice, and lists what an affected business should do now."),
    answers={
        "what": "An FBR notification of 27 August 2026 under section 6A of the AML Act, amending the 2020 DNFBP Regulations in seven places.",
        "dpms": "“Jewellers” becomes “DPMS” everywhere, with a new clause (fa) definition; the Rs 2 million cash test stays.",
        "rea": "The real estate agent definition now includes title transferring authorities, alongside builders, developers, brokers and dealers.",
        "records": "Regulation 6(4) and 6(5) are rewritten: keep litigation records until the case ends, and promptly answer FBR, law enforcement and FMU.",
        "todo": "Check your category, register if you are not registered, and update your policy's definitions and record-keeping clause.",
    },
    svc=svc("Check Your Business Against the 2026 Wording",
            "We read your business model against the amended definitions, tell you whether you are a DNFBP, and if you are, register you with FBR and bring your policy up to date.",
            ["Category check under the amended regulations 1(2) and 2(1)(fa) and (n)",
             "DNFBP registration with FBR, or a written note if you are out of scope",
             "Policy wording updated from “jeweller” to DPMS and for the new record-keeping text",
             "goAML registration so you can file CTRs and STRs with FMU",
             "Compliance officer appointment recorded and shared with FBR"],
            ["Policies still written for the 2020 text can fail an inspection on definitions alone",
             "Title transferring bodies that assumed they were outside scope now need to review that view",
             "Unregistered DNFBPs face the sanctions in the AML/CFT Sanctions Rules 2020"],
            "Not sure whether the 2026 changes cover your business?", "Check my business against S.R.O. 1439", "a DNFBP category check and registration"),
    cta_p="Send a line on what your business sells or arranges; we tell you whether the amended definitions cover it.",
    wa_text="Assalam o Alaikum, SRO 1439/2026 ke baad kya mujhe DNFBP registration karni hogi? Business ki detail bhej raha hoon.",
    about=about({"@type": "Legislation", "name": "S.R.O. 1439(I)/2026", "legislationJurisdiction": "PK", "legislationDate": "2026-08-27", "url": S_1439[1]}),
    body=f"""
{SERIES("sro")}

<h2 id="what">What S.R.O. 1439(I)/2026 Is</h2>
<p>S.R.O. 1439(I)/2026 is a notification of the Federal Board of Revenue dated 27 August 2026, signed by the Secretary (Rules &amp; SROs). It is made under section 6A of the Anti-Money Laundering Act 2010, read with Schedule IV to that Act, the same power FBR used to make the original Regulations, S.R.O. 924(I)/2020 of 29 September 2020. It does not replace the 2020 Regulations. It amends them in seven numbered places, and the amended Regulations are what FBR's Directorate General of DNFBPs now applies.</p>
<p>FBR lists both texts together on its AML/CFT Legislation and Regulations page, the original Regulations and “Amended SRO 1439”, alongside the new jurisdiction notification S.R.O. 1497(I)/2026, which reorganised the DNFBP Directorates in September 2026.</p>

<h2 id="changes">The Seven Changes at a Glance</h2>
{table(["No.", "Where", "2020 text", "After S.R.O. 1439(I)/2026"], [
    ["(i)", "Preamble", "“Regulations”", "“regulations” (style only)"],
    ["(ii)", "Throughout", "“Jewellers”", "“DPMS”"],
    ["(iii)", "Reg. 1(2)", "Applies to real estate agents, jewelers and accountants", "Applies to real estate agents, dealers in precious metals and dealers in precious stones, and accountants"],
    ["(iv)", "Reg. 2(1)(f), new (fa), (k), (n), (q)", "“Jeweler” defined in clause (k)", "DPMS defined in new clause (fa); clause (k) omitted; real estate agent redefined in (n)"],
    ["(v)", "Reg. 4(1)(b)", "“what is” in the risk-factor clause", "Words omitted (drafting)"],
    ["(vi)", "Reg. 6(4), 6(5)", "Litigation records and enquiries", "Both sub-regulations restated"],
    ["(vii)", "Reg. 8(1)(b), 8(6), 8(11)", "“Jewellers and” dealers", "Words omitted; minor drafting"],
])}
<p>Three of the seven, numbers (ii)–(iv) and (vi), change how the Regulations work in practice. The rest tidy the drafting.</p>

<h2 id="dpms">From “Jewellers” to DPMS</h2>
<p>The 2020 Regulations used the word “Jeweler”. The new clause (fa) of regulation 2(1) defines “Dealers in precious metals and dealers in precious stones (DPMS)” as including:</p>
<blockquote><p>“a person who is a bullion dealer or engaged in sale of jewellery, precious stones and metals including all articles made wholly or mainly of gold, platinum, diamonds of all kinds, precious or semi-precious stones, pearls whether or not mounted, set or strung and articles set or mounted with diamonds, precious or semi-precious stones or pearls, when they engage in a cash transaction with a customer of a value equivalent to two Million rupees or more”.</p></blockquote>
<p>The list of goods is the same one the old “Jeweler” definition used; the name now matches the AML Act's own vocabulary and FATF's. Two practical consequences follow:</p>
<ul>
<li><strong>The trigger is still cash.</strong> A dealer becomes a DPMS for these purposes when it engages in a cash transaction of Rs 2 million or more. Regulation 8(1)(b), as amended, ties customer due diligence for DPMS to the same Rs 2 million cash threshold.</li>
<li><strong>Gem and stone dealers are named in their own right.</strong> “Dealers in precious stones” now sits in the scope clause of regulation 1(2). A gemstone trader who never sells gold jewellery can no longer read the Regulations as aimed only at jewellers.</li>
</ul>
<p>Our {a(X["jew"], "DPMS and jeweller guide")} covers the day-to-day duties once you are in scope.</p>

<h2 id="rea">Real Estate Agents: Title Transferring Authorities Added</h2>
<p>The 2020 definition said “Real Estate Agent” includes builders, real estate developers and property brokers and dealers when they execute a purchase and sale of real property, participate in a real estate transaction or exercise professional transactional activity for a real property transfer. The substituted clause (n) reads: real estate agent “includes builders, real estate developers, title transferring authorities, property brokers and dealers” in those same circumstances.</p>
<p>“Title transferring authorities” is not defined in the Regulations. Read with the rest of clause (n), it points to bodies through which the title to real property passes, the transfer office of a housing society or development authority being the obvious example. Such bodies should look at whether they “participate in real estate transactions” or carry out “professional transactional activity for real property transfer”, the tests the definition uses. Housing societies and developers were already pressed by FBR's Condition No. 2 (2022) to register; our guide for {a(B["dev"], "developers and housing societies")} explains that condition. Brokers and dealers remain covered exactly as before; see our {a(X["rea"], "real estate agent guide")}.</p>

<h2 id="records">Record-Keeping: Two Sub-Regulations Restated</h2>
<p>Regulation 6 already required DNFBPs to keep CDD records for at least five years after a business relationship ends. S.R.O. 1439(I)/2026 rewrites two of its sub-regulations:</p>
{table(["Sub-regulation", "New text in short"], [
    ["6(4)", "DNFBPs must retain records of transactions, customers or instruments subject to litigation until the case is resolved; where a court or other competent authority requests them, until the litigation ends or the authority says retention is no longer required"],
    ["6(5)", "The DNFBP shall promptly satisfy any inquiry or order from the Board, designated law enforcement agencies and FMU for CDD information and transaction records, as the AML Act provides"],
])}
<p>Neither change shortens any period. They make two obligations explicit: litigation can extend retention indefinitely, and a request from FBR, a law enforcement agency or FMU must be answered promptly. A file system that cannot produce a 2021 customer's CDD file within days does not meet the second test.</p>

<h2 id="unchanged">What Did Not Change</h2>
<ul>
<li><strong>Registration.</strong> Regulation 3(1) still says every DNFBP “shall be registered with the Board”, and regulation 3(2) still requires information including the criminal records of senior management and beneficial owners.</li>
<li><strong>Accountants.</strong> The definition of accountants, other than those regulated by ICAP and ICMAP, is untouched; see our {a(X["acc"], "accountants guide")}.</li>
<li><strong>The duties.</strong> Risk assessment (reg. 4), the compliance programme (reg. 7), CDD and EDD (regs. 8–9), sanctions screening (reg. 13) and STR/CTR reporting to FMU (reg. 14) are all as before.</li>
<li><strong>Sanctions.</strong> Regulation 16 still subjects any violation to the sanctions under the AML Act; the Sanctions Rules 2020 allow monetary penalties of up to Rs 100 million per violation. See our {a(B["pen"], "penalties guide")}.</li>
</ul>

<h2 id="todo">What an Affected Business Should Do Now</h2>
<ol>
<li><strong>Re-read the definitions against your business.</strong> A gem trader, a bullion dealer, a society's transfer office and a developer should each check the amended clauses (fa) and (n).</li>
<li><strong>Register if you are in scope and not registered.</strong> Regulation 3(1) does not give a grace period. Our {a(B["docs"], "documents checklist")} lists what to prepare.</li>
<li><strong>Update your written policy.</strong> Replace “jeweller” with DPMS, quote the new clause (n) if you are in property, and add the restated record-keeping text.</li>
<li><strong>Check your record retrieval.</strong> Test whether you can produce any customer's CDD file quickly, as regulation 6(5) now spells out.</li>
<li><strong>Confirm your supervising Directorate.</strong> Under S.R.O. 1497(I)/2026, Directors at Lahore, Islamabad, Karachi and Quetta cover named RTOs; see our {a(X["lhr"], "Lahore and Punjab")} and {a(X["khi"], "Karachi and Sindh")} guides.</li>
</ol>
""",
    faqs=[
        ("What is S.R.O. 1439(I)/2026?",
         "An FBR notification of 27 August 2026 amending the FBR AML/CFT Regulations for DNFBPs 2020 (S.R.O. 924(I)/2020), made under section 6A of the AML Act 2010."),
        ("What does DPMS mean in FBR's regulations?",
         "Dealers in precious metals and dealers in precious stones: bullion dealers and sellers of jewellery, precious stones and metals, when they engage in a cash transaction of Rs 2 million or more."),
        ("Are jewellers still covered after the 2026 amendment?",
         "Yes. The word “Jewellers” is replaced by DPMS, and the new definition covers jewellery sellers when they take cash of Rs 2 million or more in a transaction."),
        ("Who are title transferring authorities?",
         "The Regulations do not define the term. It appears in the amended real estate agent definition beside builders, developers, brokers and dealers, and points to bodies through which property title passes."),
        ("Did S.R.O. 1439 change the record-keeping period?",
         "No. It restated regulation 6(4) on litigation records and 6(5) on promptly answering FBR, law enforcement and FMU. The five-year minimum after a relationship ends remains."),
        ("Do I need to register again because of the amendment?",
         "Not if you are already registered and your category is unchanged. If the new wording brings you into scope, register under regulation 3(1)."),
    ],
    sources=[S_1439, S_REG, S_1497, S_C2, S_SANC, S_INTRO],
    related=[(X["main"], "Complete DNFBP guide"), (X["jew"], "DPMS and jewellers"), (B["dev"], "Developers and societies"), (X["svc"], "DNFBP compliance service")],
)

# 2 ---------------------------------------------------------------- developers and housing societies
DEV = post(
    slug=SL["dev"],
    title="Housing Society & Developer DNFBP Registration: NOC Rule",
    h1="Housing Societies and Real Estate Developers: DNFBP Registration, the Compliance Officer and FBR's NOC Condition",
    crumb="Societies and Developers: DNFBP",
    description="FBR's Condition No. 2 (2022): no NOC or approval for a housing society or developer unless it is a registered DNFBP with an AML compliance officer.",
    keywords="housing society dnfbp registration, developer dnfbp registration, condition no 2 fbr dnfbp, noc housing society fbr dnfbp, builder aml registration pakistan",
    read="12 min read",
    banner="Without DNFBP registration and a named compliance officer, a housing scheme cannot get its NOC or approval from a public development authority.",
    tldr=("FBR's Condition No. 2 (2022), in force from 15 March 2022, tells every public sector development department or authority not to grant "
          "any NOC, approval or permission to a real estate development authority or housing society unless the applicant is registered with FBR as a "
          "DNFBP and has appointed or nominated an AML/CFT compliance officer. Authorities must also make sure societies already approved and still "
          "in business are registered. FBR's Regulations count builders and developers as real estate agents, and since S.R.O. 1439(I)/2026 the "
          "definition also names title transferring authorities. A registered society may obtain a Registration Certificate from its Director DNFBPs."),
    lead=("For a housing scheme in Pakistan, the approvals from a development authority are the business. Since March 2022 FBR has linked those "
          "approvals to AML compliance: no DNFBP registration, no compliance officer, no NOC. Many developers first meet the rule when a file stalls at "
          "the authority. This guide explains the condition in FBR's own words, how it fits the Regulations, and what a society or developer has to "
          "put in place to satisfy both the authority and FBR."),
    answers={
        "condition": "Condition No. 2 (2022): no NOC, approval or permission to a development authority or housing society unless it is an FBR-registered DNFBP with a compliance officer.",
        "who": "Builders and developers are real estate agents under FBR's Regulations; since 2026 the definition also names title transferring authorities.",
        "existing": "Authorities must also ensure societies already approved and still operating are registered and have compliance officers.",
        "certificate": "FBR's condition says societies may obtain a Registration Certificate from the concerned Director DNFBPs once registered.",
        "duties": "Registration is the start: CDD on buyers, CTRs for cash of Rs 2 million or more, sanctions screening, STRs and record-keeping follow.",
    },
    svc=svc("DNFBP Registration for Your Scheme, Before the NOC Stalls",
            "We register the developer or society with FBR as a DNFBP, record the compliance officer, obtain the registration certificate and set up the AML file the authority and FBR will both expect.",
            ["DNFBP registration for the company, AOP or society that runs the scheme",
             "Compliance officer nomination and the details FBR needs",
             "Request for the Registration Certificate from the Director DNFBPs",
             "Buyer and transfer CDD forms suited to file sales and allotments",
             "goAML registration so CTRs and STRs can be filed with FMU"],
            ["An NOC or approval application without DNFBP registration can be held under Condition No. 2",
             "Schemes approved before 2022 are not exempt: authorities must check them too",
             "Allotments and file transfers without CDD leave the scheme exposed at inspection"],
            "Developer or society facing an NOC hold?", "Register my scheme as a DNFBP", "a developer or society DNFBP registration"),
    cta_p="Send the scheme's legal form (company, AOP or society) and the authority whose NOC you need.",
    wa_text="Assalam o Alaikum, housing society/developer ki DNFBP registration aur compliance officer chahiye NOC ke liye.",
    about=about({"@type": "Legislation", "name": "FBR Condition No. 2 (2022) for Public Sector Development Departments/Authorities", "legislationJurisdiction": "PK", "legislationDate": "2022-02-28", "url": S_C2[1]}),
    body=f"""
{SERIES("dev")}

<h2 id="condition">FBR's Condition No. 2 (2022), Word for Word</h2>
<p>On 28 February 2022 the Director General (DNFBPs) at FBR issued “Condition No. 2 (2022) for Public Sector Development Departments/Authorities”, under section 6A of the AML Act read with Schedule IV and in pursuance of Condition No. 1 of 2021. The operative condition reads:</p>
<blockquote><p>“No Public Sector Development Department/Authority shall provide any NOC/Approval/Permission to any kind of Real Estate Development Authority or Housing Society (commercial/residential) unless the applicant is registered with the Federal Board of Revenue as a Designated Non-Financial Business and Profession (DNFBP) and has also appointed or nominated AML/CFT Compliance Officer.”</p></blockquote>
<p>A second paragraph extends it backwards: the authorities “shall also ensure that previously approved Real Estate Authorities or Societies falling in their respective jurisdiction and currently in business are registered with FBR as DNFBPs and have appointed or nominated AML/CFT Compliance Officers.” The condition took effect on 15 March 2022.</p>

<h2 id="who">Why Developers and Societies Are DNFBPs</h2>
<p>FBR's Regulations define “Real Estate Agent” to include builders and real estate developers when they execute a purchase and sale of real property, participate in a real estate transaction, or exercise professional transactional activity for a property transfer. A society or developer selling plots, files or units does all three. S.R.O. 1439(I)/2026, issued on 27 August 2026, substituted that definition and added “title transferring authorities” to the list, which speaks directly to a scheme's own transfer office. Our guide to {a(B["sro"], "the 2026 amendments")} sets the old and new text side by side.</p>
<p>The National Risk Assessment 2023 rates real estate agents, a category it describes as “including builders/ developers”, at “Very High” inherent vulnerability, the highest rating among DNFBP sectors. That rating is the background to FBR's focus on schemes; see our {a(B["nra"], "NRA 2023 guide")}.</p>

<h2 id="registration">What Registration Involves for a Scheme</h2>
{table(["Step", "What the scheme needs", "Source"], [
    ["Taxpayer record", "An NTN and IRIS access for the company, AOP or society that runs the scheme", "FBR's DNFBP portal login is the IRIS login"],
    ["DNFBP registration", "Registration with the Board, with any information FBR requires, including criminal records of senior management and beneficial owners", "Regulation 3(1)–(2)"],
    ["Compliance officer", "A compliance officer at management level, reporting to the board or chief executive", "Regulation 7(1)(a), 7(3); Condition No. 2"],
    ["Registration Certificate", "May be obtained from the concerned Director DNFBPs once registered", "Condition No. 2, paragraph 3"],
    ["goAML", "Registration on FMU's portal to file STRs and CTRs", "Regulation 14; FBR FAQs Q43"],
])}
<p>Which Director handles the scheme depends on its RTO under S.R.O. 1497(I)/2026. Our guides for {a(X["lhr"], "Lahore and Punjab")}, {a(X["isb"], "Islamabad and Rawalpindi")}, {a(X["khi"], "Karachi and Sindh")}, {a(X["pew"], "Peshawar and KP")} and {a(X["qta"], "Quetta and Balochistan")} list the offices.</p>

<h2 id="officer">The Compliance Officer the Authority Will Ask About</h2>
<p>Regulation 7(3) says the compliance officer must report directly to the board of directors, chief executive or a committee, have timely access to all customer records, and be responsible for, among other things, getting the AML/CFT policies approved and implemented, keeping them up to date, submitting accurate returns on time and “monitoring and timely reporting of Suspicious and Currency Transactions to FMU”. FBR's FAQs (Q26) add that the DNFBP designates senior management personnel and shares the officer's contact details with FBR. For a scheme, that usually means a director or the head of sales or transfers, not a junior clerk.</p>

<h2 id="duties">Duties After Registration, Applied to Plot and File Sales</h2>
{table(["Duty", "How it shows up in a scheme"], [
    ["CDD (reg. 8)", "Identity of every allottee, buyer and seller of a file or plot, and of anyone acting for them; beneficial owner where the buyer is a company"],
    ["CTR", "FBR's short guidance for real estate agents: report cash transactions of Rs 2 million or more to FMU"],
    ["Sanctions screening (reg. 13)", "Screen buyers and beneficial owners against UN and domestic lists before allotment or transfer; see " + a(B["tfs"], "screening guide")],
    ["PEPs (reg. 9)", "Senior management approval and source of wealth for politically exposed buyers; see " + a(B["pep"], "PEP guide")],
    ["Records (reg. 6)", "CNICs of seller and purchaser, sale deed or transfer papers, bank draft and CDD form, kept at least five years after the relationship ends"],
    ["STR (reg. 14)", "Report suspicion to FMU through goAML, including attempted transactions"],
])}
<p>File trading is where schemes are most exposed. A single file may change hands several times before possession, and each transfer through the scheme's office is a transaction the scheme participates in. A transfer desk that records only the new holder's name, without CDD, is the gap an inspection is likely to find. Our {a(X["rea"], "real estate agent guide")} covers deal-level red flags.</p>

<h2 id="example">Example: A Scheme Applying for Revised Layout Approval</h2>
<p>A private limited company runs a 400-kanal residential scheme approved in 2019. In 2026 it applies to the development authority for a revised layout. The authority's checklist now asks for proof of DNFBP registration and the name of the compliance officer. The company has an NTN but never registered as a DNFBP, on the view that it is a developer, not a dealer. Under FBR's definition it is a real estate agent, and under Condition No. 2 the authority cannot issue the approval until it registers and nominates an officer. The fix is registration with the Lahore, Islamabad, Karachi or Quetta Directorate as S.R.O. 1497 assigns it, nomination of a director as compliance officer, and a request for the Registration Certificate to put on the file.</p>
""",
    faqs=[
        ("Does a housing society need DNFBP registration for an NOC?",
         "Yes. Under FBR's Condition No. 2 (2022), no public sector development department or authority shall give an NOC, approval or permission to a housing society or real estate development authority unless it is a registered DNFBP with an AML/CFT compliance officer."),
        ("Does the condition apply to societies approved before 2022?",
         "Yes. The authorities must ensure that previously approved societies still in business are registered with FBR as DNFBPs and have compliance officers."),
        ("Are builders and developers DNFBPs?",
         "Yes. FBR's Regulations define real estate agents to include builders and real estate developers; since S.R.O. 1439(I)/2026 the definition also names title transferring authorities."),
        ("Who should be a scheme's compliance officer?",
         "A person at management level who reports directly to the board or chief executive and has access to all customer records, as regulation 7 requires."),
        ("Is there a DNFBP registration certificate?",
         "FBR's Condition No. 2 says real estate development authorities or societies may obtain a Registration Certificate from the concerned Director DNFBPs once registered."),
        ("Does every file transfer need customer due diligence?",
         "Where the scheme participates in the transfer, the Regulations' CDD duties apply to the buyer and seller, including identification and, where relevant, beneficial ownership."),
    ],
    sources=[S_C2, S_COND, S_REG, S_1439, S_REA, S_NRA, S_1497],
    related=[(X["rea"], "Real estate agents and AML"), (B["sro"], "S.R.O. 1439 changes"), (B["cert"], "Registration certificate"), (X["svc"], "DNFBP compliance service")],
)

# 3 ---------------------------------------------------------------- certificate and status
CERT = post(
    slug=SL["cert"],
    title="DNFBP Registration Certificate and Status: What FBR Says",
    h1="DNFBP Registration Certificate, Status and Verification: What FBR's Own Texts Say (2026)",
    crumb="DNFBP Certificate and Status",
    description="Is there a DNFBP certificate? Where is the FBR DNFBP portal, who issues the certificate, how to confirm your status, and what to do when details change.",
    keywords="dnfbp certificate, dnfbp registration certificate, dnfbp registration status, dnfbp certificate download, dnfbp certificate verification, fbr dnfbp portal login",
    read="11 min read",
    banner="People search for a DNFBP certificate more than anything else about DNFBPs. Here is what FBR's published texts actually say, and what they do not.",
    tldr=("FBR's DNFBP Regulations require every DNFBP to be registered with the Board and to keep the registration up to date (regulation 3). "
          "FBR's AML/CFT pages send the “FBR DNFBP Portal Login” to the IRIS login, so registration runs through your IRIS account. FBR's "
          "Condition No. 2 (2022) says a registered society may “obtain Registration Certificate from the concerned Director, DNFBPs”, so the "
          "certificate comes from the Directorate that supervises you under S.R.O. 1497(I)/2026. None of the FBR texts we read describe a public "
          "online verification tool or a certificate fee. To confirm status, use your IRIS record and the Directorate or FBR's DNFBP helpline."),
    lead=("“DNFBP certificate”, “DNFBP certificate download” and “DNFBP certificate verification” are among the most searched "
          "DNFBP questions in Pakistan. Property dealers want something to show a buyer, a society or a bank; jewellers want proof for a landlord or a "
          "supplier. Much of what circulates online is guesswork. This guide sticks to what FBR has published, separates it from what it has not, "
          "and explains how to get, keep and update proof of registration."),
    answers={
        "law": "Regulation 3: every DNFBP shall be registered with the Board, give the information FBR requires and keep the registration up to date.",
        "portal": "FBR's AML/CFT pages link the “FBR DNFBP Portal Login” to the IRIS login page.",
        "certificate": "FBR's Condition No. 2 refers to obtaining a Registration Certificate from the concerned Director DNFBPs once registered.",
        "verify": "FBR's published texts do not describe a public online verification tool. Confirm status through IRIS and the Directorate or helpline.",
        "change": "Keep registration details current; if you stop operating as a DNFBP, notify FBR within thirty business days so it can deregister you.",
    },
    svc=svc("Registration, Certificate and a Status You Can Prove",
            "We complete the DNFBP registration on IRIS, follow it with your Directorate until the certificate is issued, and keep your details current afterwards.",
            ["DNFBP registration on IRIS in the right category",
             "Follow-up with the supervising Director DNFBPs for the registration certificate",
             "A copy of your registration and certificate organised for inspections and counterparties",
             "Updates when owners, partners, the compliance officer or the address change",
             "Deregistration notice within thirty business days if you stop operating as a DNFBP"],
            ["A screenshot is not proof if a society or inspector asks for the Directorate's certificate",
             "Out-of-date owner or officer details leave the registration inaccurate under regulation 3",
             "Stopping business without notice leaves you registered, and supervised, as a DNFBP"],
            "Need a DNFBP certificate you can show?", "Get my DNFBP registration certificate", "DNFBP registration and the certificate follow-up"),
    cta_p="Tell us your category and city; we confirm your Directorate and what is needed for the certificate.",
    wa_text="Assalam o Alaikum, DNFBP registration certificate chahiye. Status bhi confirm karna hai.",
    about=about(),
    body=f"""
{SERIES("cert")}

<h2 id="law">What the Regulations Require</h2>
<p>Regulation 3 of FBR's AML/CFT Regulations for DNFBPs 2020 is titled “Registration and market entry control of DNFBPs”. It has three parts:</p>
{table(["Sub-regulation", "Requirement"], [
    ["3(1)", "Every DNFBP shall be registered with the Board"],
    ["3(2)", "The DNFBP shall provide any information or documentation the Board requires for registration or for keeping the registration up to date, including criminal records of senior management and beneficial owners"],
    ["3(3)", "The DNFBP shall notify the Board if it ceases operations as a DNFBP within thirty business days, and the Board shall deregister it if the appropriate information is provided"],
])}
<p>So registration is not a one-time event. It is a record that must stay accurate for as long as you operate, and it ends only through a notice from you.</p>

<h2 id="portal">Where Registration Happens: IRIS</h2>
<p>FBR's AML/CFT pages for DNFBPs carry a link labelled “FBR DNFBP Portal Login”. It points to FBR's IRIS login page, the same system used for returns and NTNs. Registration therefore runs through the IRIS account of the person or entity that carries on the business: the individual for a sole proprietor, the AOP for a partnership, the company for a private limited company. If that account does not exist yet, the first step is an {a(X["ntn"], "NTN")}. The steps inside IRIS are covered in our {a(X["main"], "complete DNFBP guide")}.</p>
<p>The same pages list a separate link for reports: “File STR or CTR with the FMU via GoAML”. goAML belongs to the Financial Monitoring Unit, not FBR, and needs its own registration; see our {a(X["goaml"], "goAML guide")}.</p>

<h2 id="certificate">The Registration Certificate: Who Issues It</h2>
<p>The clearest official reference to a certificate is in FBR's Condition No. 2 (2022), addressed to public sector development authorities. After requiring housing societies and real estate development authorities to register, it says they “may also be informed to obtain Registration Certificate from the concerned Director, DNFBPs once registered as a DNFBP with FBR.” Two points follow:</p>
<ul>
<li>the certificate is issued by the <strong>Director DNFBPs</strong> who supervises you, not generated by a public website; and</li>
<li>it comes <strong>after</strong> registration, as evidence of it.</li>
</ul>
<p>Which Director supervises you is fixed by S.R.O. 1497(I)/2026 (2 September 2026): Directors at Lahore, Islamabad, Karachi and Quetta, each for listed Regional Tax Offices, under the Director General's all-Pakistan jurisdiction. Our regional guides list the offices: {a(X["lhr"], "Lahore and Punjab")}, {a(X["isb"], "Islamabad and Rawalpindi")}, {a(X["khi"], "Karachi and Sindh")}, {a(X["pew"], "Peshawar and KP")}, {a(X["qta"], "Quetta and Balochistan")}.</p>

<h2 id="verify">Status and Verification: What Is and Is Not Published</h2>
{table(["Question people ask", "What FBR's published texts we read say"], [
    ["Is there an online DNFBP certificate download?", "No such facility is described. The certificate is referred to as obtained from the Director DNFBPs"],
    ["Is there a public verification page?", "None is described in the Regulations, FAQs, conditions or FBR's AML/CFT pages we read"],
    ["Is there a fee for registration or the certificate?", "None of those texts mention one"],
    ["Where can a DNFBP ask?", "FBR's FAQs (Q25) give help.dnfbp.fbr@gmail.com and +92 51 9106606 for AML/CFT compliance queries"],
    ["Is there an app?", "Yes. FBR publishes a DNFBP Mobile Application on Google Play and the Apple App Store; FBR's guidance says sanctions lists are available on it"],
])}
<p>In practice, your own proof of status is the registration record in your IRIS account plus the certificate from your Directorate. A counterparty, such as a society, bank or landlord, that wants to confirm your registration can be shown both; if they want confirmation from FBR itself, the Directorate is the authority to ask.</p>

<h2 id="change">Keeping the Registration Current</h2>
<p>Regulation 3(2) requires information for “keeping the DNFBP registration up to date”. The changes that matter most are:</p>
<ol>
<li>a new owner, partner, director or beneficial owner, whose details and criminal-record information FBR may require;</li>
<li>a new compliance officer, whose contact details FBR's FAQs (Q26) say must be shared with FBR;</li>
<li>a new business address, which may also change your supervising Directorate under S.R.O. 1497(I)/2026;</li>
<li>a change of category, for example a jeweller who stops taking cash of Rs 2 million or more, or a dealer who starts.</li>
</ol>
<p>If you stop operating as a DNFBP, regulation 3(3) requires notice within thirty business days in the form FBR requires, and FBR then deregisters you. Until that happens, you remain a registered DNFBP and within FBR's supervision.</p>

<h2 id="use">When You Will Be Asked for Proof</h2>
<ul>
<li><strong>Development authorities</strong> processing a society's NOC or approval, under Condition No. 2; see {a(B["dev"], "developers and societies")}.</li>
<li><strong>FBR inspections</strong> under regulation 15, where the inspector starts from your registration and compliance officer.</li>
<li><strong>Counterparties</strong> such as banks and larger developers that run their own AML checks on the agents they work with.</li>
</ul>
<p>Registration alone does not make a business compliant. The written programme, CDD files and goAML access are what an inspection tests; see our {a(X["prog"], "compliance programme guide")} and {a(B["pen"], "penalties guide")}.</p>
""",
    faqs=[
        ("Is there a DNFBP registration certificate in Pakistan?",
         "Yes. FBR's Condition No. 2 (2022) refers to obtaining a Registration Certificate from the concerned Director DNFBPs once registered as a DNFBP with FBR."),
        ("Can I download my DNFBP certificate online?",
         "None of the FBR texts we read describe an online download. The certificate is obtained from the Director DNFBPs who supervises you."),
        ("How can I check my DNFBP registration status?",
         "Through your IRIS account, which FBR's DNFBP portal link opens, and by asking your Directorate or FBR's DNFBP helpline (help.dnfbp.fbr@gmail.com, +92 51 9106606)."),
        ("Is there a public DNFBP verification website?",
         "FBR's Regulations, FAQs, conditions and AML/CFT pages that we read describe none. Confirmation comes from the Directorate."),
        ("Is there a fee for DNFBP registration?",
         "None of the FBR texts we read mention a government fee for registration or the certificate. Our professional fee is fixed and confirmed before work starts."),
        ("What happens if I close my business?",
         "Under regulation 3(3) you must notify FBR within thirty business days of ceasing operations as a DNFBP; FBR then deregisters you."),
    ],
    sources=[S_REG, S_C2, S_APP, S_PORTAL, S_FAQ, S_1497, S_GOAML],
    related=[(X["main"], "Complete DNFBP guide"), (X["goaml"], "goAML registration"), (B["docs"], "Documents checklist"), (X["svc"], "DNFBP compliance service")],
)

# 4 ---------------------------------------------------------------- sole proprietors
SOLE = post(
    slug=SL["sole"],
    title="DNFBP Registration for Sole Proprietors: Officer Rules",
    h1="DNFBP Registration for a Sole Proprietor: One-Person Property Offices and Jewellers, Explained",
    crumb="Sole Proprietor DNFBP Registration",
    description="Running a one-person property office or jewellery shop? How DNFBP registration works for a sole proprietor, and when FBR deems you the compliance officer.",
    keywords="dnfbp registration sole proprietor, sole proprietor compliance officer dnfbp, condition no 3 fbr, property dealer sole proprietor dnfbp, jeweller sole proprietor aml",
    read="12 min read",
    banner="Most property dealers and many jewellers in Pakistan are one-person businesses. FBR has a specific rule for who the compliance officer is when there is no one else.",
    tldr=("A sole proprietor who works as a real estate agent, a DPMS taking cash of Rs 2 million or more, or a non-ICAP/ICMAP accountant doing "
          "specified services is a DNFBP and must register with FBR under regulation 3. Registration runs through the proprietor's own IRIS account, "
          "since a sole proprietorship has no separate legal identity. FBR's FAQs (Q29) say the proprietor must designate an employee as compliance "
          "officer, but where there are no employees, FBR's Condition No. 3 (2022) deems the sole proprietor to be the AML/CFT compliance officer "
          "under section 7G of the AML Act. The role does not have to be standalone. All other duties apply in full."),
    lead=("The typical Pakistani property office is one person with a phone, a register and a network of buyers and sellers. Many jewellers are the "
          "owner, a family member and a karigar. FBR's AML rules were written for every size of business, and small owners often assume they are "
          "too small to matter or that they cannot meet the rules alone. FBR has addressed both points. This guide explains what registration "
          "means for a sole proprietor, who the compliance officer is, and how a one-person business can meet the duties without a compliance "
          "department."),
    answers={
        "scope": "Size does not decide it: the activity does. A one-person real estate office, a DPMS taking Rs 2 million cash, or an accountant doing specified services is a DNFBP.",
        "identity": "A sole proprietorship is the owner. Registration runs through the owner's own NTN and IRIS account.",
        "officer": "Designate an employee if you have one; if you have none, Condition No. 3 (2022) deems you the compliance officer under section 7G.",
        "duties": "Risk assessment, written policy, CDD, sanctions screening, record-keeping, CTRs and STRs on goAML all still apply.",
        "practical": "A one-page risk assessment, a short policy, a CDD form per deal and a record box per year cover most of it.",
    },
    svc=svc("DNFBP Registration Sized for a One-Person Business",
            "We register you as a DNFBP through your own IRIS account, set up the compliance officer position correctly, and give you a programme you can run alone.",
            ["Business NTN and IRIS profile checked or created for the proprietorship",
             "DNFBP registration in your category",
             "Compliance officer position recorded: an employee, or you under Condition No. 3",
             "A short written risk assessment and policy that fit a small office",
             "CDD forms and a filing system for each deal, plus goAML registration"],
            ["Assuming a small office is out of scope leaves you unregistered and open to sanction",
             "Naming an unqualified relative as compliance officer without authority does not meet regulation 7",
             "Policies copied from a large firm are ones a one-person business cannot follow"],
            "One-person property office or jewellery shop?", "Register my sole proprietorship as a DNFBP", "a sole proprietor DNFBP registration"),
    cta_p="Send your CNIC and a line about your business; we tell you your category and what registration needs.",
    wa_text="Assalam o Alaikum, sole proprietor hoon (property/jewellery). DNFBP registration karwani hai.",
    about=about({"@type": "Legislation", "name": "FBR Condition No. 3 (2022) for Sole Proprietorship Concerns", "legislationJurisdiction": "PK", "legislationDate": "2022", "url": S_C3[1]}),
    body=f"""
{SERIES("sole")}

<h2 id="scope">Size Does Not Take You Out of Scope</h2>
<p>Nothing in FBR's Regulations exempts small businesses. What decides it is the activity:</p>
{table(["You are a sole proprietor who", "You are a DNFBP if", "Source"], [
    ["Buys, sells or arranges property for clients", "You execute purchases and sales, participate in real estate transactions or carry out professional transactional activity for property transfer", "Reg. 2(1)(n), as substituted by S.R.O. 1439(I)/2026"],
    ["Sells jewellery, bullion, gems or stones", "You engage in a cash transaction with a customer of Rs 2 million or more", "Reg. 2(1)(fa), inserted by S.R.O. 1439(I)/2026"],
    ["Practises as an accountant, not an ICAP or ICMAP member", "You carry out the specified activities in the AML Act, such as company formation or managing client money", "Reg. 2(1)(a); FBR FAQs Q1–Q3"],
])}
<p>FBR's FAQs (Q19) make the same point for accountants: there is “no financial limit / threshold / benchmark”; the services decide. A one-person office that does one property deal a month is as much a DNFBP as a firm that does a hundred.</p>

<h2 id="identity">Registering a Business That Is Also You</h2>
<p>A sole proprietorship has no legal identity apart from its owner. The business name on the signboard is a trade name; in FBR's records the taxpayer is the individual. That has three consequences for DNFBP registration:</p>
<ol>
<li><strong>The IRIS account is yours.</strong> FBR's DNFBP portal link opens the IRIS login, and the registration is made through the proprietor's own NTN and IRIS profile, with the business details recorded in it. Our {a(X["sole"], "sole proprietor guide")} covers setting up that profile.</li>
<li><strong>You are senior management.</strong> FBR's FAQs (Q27) list “a sole proprietor of the Reporting Entity” first in the meaning of senior management. Regulation 3(2)'s request for criminal-record information on senior management and beneficial owners therefore points at you.</li>
<li><strong>You are the beneficial owner.</strong> The natural person who ultimately owns and controls the business is the proprietor.</li>
</ol>

<h2 id="officer">Who Is the Compliance Officer?</h2>
<p>Regulation 7(1)(a) requires a compliance officer “at the management level”. FBR's FAQs answer the sole-proprietor question directly (Q29):</p>
<blockquote><p>“Sole Proprietor must designate an employee to be the Compliance Officer. However, if there are no employees, FBR has imposed Condition No 3 (2022) which states that the Sole Proprietor shall be deemed to be AML/CFT compliance officer for the purpose of section 7G of the AML Act, 2010 and FBR's DNFBPs AML/CFT Regulations, 2020. Moreover, the Compliance Officer can carry out other duties not related to AML / CFT compliance. It does not have to be a standalone position.”</p></blockquote>
{table(["Your set-up", "Compliance officer"], [
    ["Proprietor alone, no employees", "You, by Condition No. 3 (2022)"],
    ["Proprietor with one or more employees", "Designate an employee; FBR's FAQs (Q27) describe senior management as including an employee with sufficient knowledge and authority on ML/TF risk"],
    ["Any case", "The role may be combined with other work; it need not be a separate post"],
])}
<p>Whoever it is, regulation 7(3) expects the officer to have access to all customer records and to be responsible for keeping the policy current and for timely reporting of STRs and CTRs to FMU. FBR's FAQs (Q26) require the officer's contact details to be shared with FBR.</p>

<h2 id="duties">The Duties a One-Person Business Must Still Meet</h2>
{table(["Duty", "What it looks like in a one-person office"], [
    ["Risk assessment (reg. 4)", "A written page on your customers, areas, deal types and cash use, updated each year, reflecting FBR's sector risk ratings"],
    ["Policy and controls (reg. 4(2))", "A short policy you have approved as senior management, saying what you check and when you refuse"],
    ["Compliance programme (reg. 7)", "Officer named; hiring screening if you take on staff; your own training; an independent check of the system"],
    ["CDD (reg. 8)", "A CDD form and CNIC copy, stamped “Original seen”, for every buyer and seller; beneficial owner where the customer is a company"],
    ["Screening (reg. 13)", "Check names against UN and domestic lists before each deal; see " + a(B["tfs"], "sanctions screening")],
    ["Records (reg. 6)", "One file per deal, kept at least five years after the relationship ends; a list of customers you refused"],
    ["Reports (reg. 14)", "goAML registration; CTR for cash of Rs 2 million or more; STR on suspicion"],
])}

<h2 id="example">Example: A Property Dealer in Johar Town</h2>
<p>Imran runs a property office in Johar Town, Lahore, alone, arranging plot and house sales for about three deals a month. He has an NTN as a salaried person from an old job and no business details on IRIS. To register, he updates his IRIS profile with the business, registers as a DNFBP in the real estate agent category with the Lahore Directorate, and, with no employees, records himself as compliance officer under Condition No. 3. He writes a one-page risk assessment (cash-heavy plot deals, some overseas buyers), adopts a short policy, starts a CDD form for every party, registers on goAML, and keeps a box file per year. When an overseas buyer pays Rs 2,500,000 in cash for a token, he files a CTR. Nothing in this requires staff; it requires a routine.</p>

<h2 id="tax">How This Sits With Your Tax Registration</h2>
<p>DNFBP registration is an AML registration, separate from income tax. You still file your return as a sole proprietor, and a property office providing services in Punjab may also need {a(X["pra"], "PRA registration")}. Our guide to {a(X["solefee"], "sole proprietor services and fees")} sets out the published fees for the tax side.</p>
""",
    faqs=[
        ("Does a one-person property office need DNFBP registration?",
         "Yes, if it executes, participates in or carries out transactional activity for property sales. FBR's Regulations set no size threshold for real estate agents."),
        ("Who is the compliance officer in a sole proprietorship?",
         "FBR's FAQs (Q29) say the proprietor must designate an employee; if there are no employees, Condition No. 3 (2022) deems the sole proprietor to be the AML/CFT compliance officer."),
        ("Can the compliance officer do other work?",
         "Yes. FBR's FAQs say the compliance officer can carry out other duties and it does not have to be a standalone position."),
        ("Is the DNFBP registration in my name or the shop's name?",
         "A sole proprietorship has no separate legal identity, so registration runs through the proprietor's own NTN and IRIS account, with the business details recorded."),
        ("Is a small jeweller a DNFBP?",
         "A jeweller is a DPMS for FBR's purposes when it engages in a cash transaction with a customer of Rs 2 million or more."),
        ("Do I still need to file my income tax return?",
         "Yes. DNFBP registration is an AML registration; your tax return and any provincial sales tax registration are separate obligations."),
    ],
    sources=[S_FAQ, S_C3, S_COND, S_REG, S_1439, S_PORTAL],
    related=[(X["sole"], "Sole proprietor complete guide"), (B["docs"], "Documents checklist"), (X["rea"], "Real estate agents and AML"), (X["svc"], "DNFBP compliance service")],
)
