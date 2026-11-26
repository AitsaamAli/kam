"""DNFBP series 2, posts 5-7: documents, PEPs, beneficial owners."""
from ds_common import *

# 5 ---------------------------------------------------------------- documents
DOCS = post(
    slug=SL["docs"],
    title="DNFBP Registration Documents Required: Full Checklist",
    h1="DNFBP Registration Documents: What FBR Needs From You, and What You Must Collect From Every Customer",
    crumb="DNFBP Documents Checklist",
    description="Documents for DNFBP registration with FBR, then the CDD documents regulation 8(11) requires from individual, company, trust and government customers.",
    keywords="dnfbp registration required documents, dnfbp documents, dnfbp registration requirements, cdd documents dnfbp, kyc documents real estate agent pakistan",
    read="12 min read",
    banner="There are two document lists in DNFBP compliance: one you give FBR to register, and one you collect from every customer. Both are set by FBR's Regulations.",
    tldr=("To register as a DNFBP you need an active NTN and IRIS access for whoever runs the business, details of owners, partners, directors and "
          "beneficial owners, the compliance officer's details, and any information FBR requires, including criminal records of senior management and "
          "beneficial owners (regulation 3(2)). After registration, regulation 8(11) lists what counts as reliable identification for customers: a "
          "CNIC, NICOP, POC, Form B or ARC/passport for individuals; board resolution, memorandum, articles, incorporation certificate and director "
          "lists for companies; the trust instrument and registration papers for trusts. Copies are stamped “Original seen” (regulation 6)."),
    lead=("“What documents are required for DNFBP registration?” is usually asked as one question, but the Regulations answer two. The first "
          "list is short and goes to FBR once, to register the business. The second is long and is collected from every customer, for as long as you "
          "operate, because it is what an FBR inspector asks to see. This guide gives both lists from the text of FBR's Regulations and guidance, "
          "with the practical forms they take in a property office, a jewellery shop or an accounting practice."),
    answers={
        "register": "An NTN and IRIS access, details of owners and beneficial owners, the compliance officer, and information FBR requires, including criminal records of senior management and beneficial owners.",
        "individual": "CNIC; for overseas Pakistanis a NICOP and/or passport; POC for former nationals; Form B for minors; ARC or passport with valid visa for foreigners.",
        "company": "Board resolution, memorandum and articles, incorporation certificate, commencement declaration and directors list, and identity documents of directors and beneficial owners.",
        "keep": "Stamp copies “Original seen”, keep a list of refused customers, and retain CDD records at least five years after the relationship ends.",
    },
    svc=svc("Registration File and Customer Forms, Prepared Together",
            "We assemble what FBR needs to register you, then give you CDD forms and a checklist matched to regulation 8(11), so every customer file is complete from the first deal.",
            ["Registration file: NTN, IRIS profile, owners, beneficial owners and compliance officer",
             "Guidance on the criminal-record information FBR may ask for",
             "CDD forms for individual, company, partnership and trust customers",
             "“Original seen” and refused-customer procedures in writing",
             "A record-keeping system that meets the five-year and ten-year rules"],
            ["Registering without a complete owner and beneficial owner list invites follow-up questions",
             "Customer files without the regulation 8(11) documents fail inspection even when you are registered",
             "Copies not marked as seen against originals do not meet regulation 6"],
            "Collecting DNFBP documents for the first time?", "Prepare my DNFBP documents", "the DNFBP registration file and CDD forms"),
    cta_p="Send your business type and legal form; we send back the exact document list for registration and for customers.",
    wa_text="Assalam o Alaikum, DNFBP registration ke liye kaun se documents chahiye? Business ki detail bhej raha hoon.",
    about=about(),
    body=f"""
{SERIES("docs")}

<h2 id="register">List 1: What You Provide to Register</h2>
<p>Regulation 3(2) of FBR's AML/CFT Regulations for DNFBPs 2020 says the DNFBP “shall provide any information or documentation that may be required by the Board for the purposes of registration or keeping the DNFBP registration up to date, including but not limited to criminal records of the senior management and beneficial owners”. FBR's DNFBP portal link opens the IRIS login, so registration starts from an IRIS account. In practice that means:</p>
{table(["Item", "Why it is needed", "Notes"], [
    ["NTN and IRIS access of the business", "Registration runs through IRIS", "Individual for a sole proprietor, AOP for a firm, company for a Pvt Ltd; get an " + a(X["ntn"], "NTN") + " first if needed"],
    ["CNICs of owners, partners or directors", "They are senior management", "FBR's FAQs (Q27) list the sole proprietor, CEO, managing partner and COO"],
    ["Beneficial owner details", "Regulation 3(2) names beneficial owners", "The natural persons who ultimately own or control the business; see " + a(B["ubo"], "beneficial owners")],
    ["Criminal-record information", "Regulation 3(2) names it expressly", "For senior management and beneficial owners, in the form FBR asks"],
    ["Compliance officer's details", "FBR's FAQs (Q26) require them to be shared with FBR", "A sole proprietor with no staff is deemed the officer; see " + a(B["sole"], "sole proprietors")],
    ["Business address and category", "Decides your Directorate under S.R.O. 1497(I)/2026 and your duties", "Real estate agent, DPMS or accountant"],
    ["Firm or company papers", "To show the legal form and who controls it", "Partnership deed; incorporation certificate, memorandum and articles"],
])}
<p>A housing society or developer applying for an NOC should also plan for the Registration Certificate that FBR's Condition No. 2 says may be obtained from the Director DNFBPs after registration; see our {a(B["cert"], "certificate guide")}.</p>

<h2 id="individual">List 2a: Documents From an Individual Customer</h2>
<p>Regulation 8(11)(a) sets the reliable and independent documents for a natural person:</p>
{table(["Customer", "Identity document"], [
    ["Pakistani resident", "Computerized National Identity Card (CNIC) issued by NADRA"],
    ["Overseas Pakistani or dual national", "NICOP and/or a machine-readable passport"],
    ["Pakistani who has given up nationality", "Pakistan Origin Card (POC) and/or passport"],
    ["Child under 18", "Form B or smart/juvenile card issued by NADRA"],
    ["Foreign national", "Alien Registration Card (ARC) from NARA, or passport with a valid visa or other proof of legal stay"],
])}
<p>FBR's short guidance for real estate agents adds the information to record alongside: full name, date of birth, residential address, identity number, whether the customer acts for someone else, beneficial ownership and the purpose of the relationship. For higher-risk customers and PEPs it adds source of wealth or funds, which may be shown by an NTN, bank statement, tax documents, salary slips or business information. Its CDD form suggests a recent utility bill for address and NADRA's online verification services for identity.</p>

<h2 id="company">List 2b: Documents From a Company</h2>
<p>Regulation 8(11)(b) asks for certified copies of:</p>
<ol>
<li>the board resolution naming who is authorised to act (not needed for a single member company);</li>
<li>the memorandum of association and, where applicable, the articles;</li>
<li>the certificate of incorporation;</li>
<li>the SECP-registered declaration for commencement of business, where the Companies Act 2017 requires one;</li>
<li>the list of directors filed under the Companies Act 2017, where applicable;</li>
<li>identity documents of all directors, beneficial owners and authorised persons, as in List 2a; and</li>
<li>any other documents needed to understand the company's activities and sources and uses of funds, including annual accounts.</li>
</ol>
<p>Regulation 8(8) also requires the company's name, legal form and proof of existence, the powers that bind it, the names of its senior managers, and its registered office and principal place of business.</p>

<h2 id="trust">List 2c: Trusts, Waqfs and Government Bodies</h2>
{table(["Customer", "Documents under regulation 8(11)(c) and (d)"], [
    ["Trust, waqf or other legal arrangement", "The instrument creating it; registration documents and certificates; its bylaws, rules and regulations; authority of the person acting; identity documents of authorised persons, beneficial owners and members of the governing body; other documents on its activities and funds"],
    ["Government institution", "CNICs of the authorised persons and a letter of authorisation from the authority concerned"],
])}
<p>For a trust, regulation 8(10) adds the persons whose identity must be known: settlor, trustees, protector, beneficiaries or class of beneficiaries, and anyone exercising ultimate effective control.</p>

<h2 id="agent">When Someone Acts for the Customer</h2>
<p>Property deals in Pakistan are often signed by an attorney or a family member. Regulation 8(4) requires you to identify every person acting on the customer's behalf, verify that person's identity from reliable documents, and verify their authority to act, for example a registered power of attorney. FBR's FAQs (Q31) list “any person acting on behalf of a customer” among the people CDD is conducted on.</p>

<h2 id="keep">How the Documents Must Be Kept</h2>
{table(["Rule", "Source"], [
    ["Copies stamped “Original seen” after viewing originals", "Regulation 6"],
    ["A list of customers whose transaction was refused or closed for failing to provide documents or originals", "Regulation 6"],
    ["CDD and EDD records kept at least five years after the relationship ends", "Regulation 6; FBR FAQs Q54"],
    ["STR and CTR records kept at least ten years from filing", "FBR FAQs Q54"],
    ["Records under litigation kept until the case ends or the authority releases them", "Regulation 6(4), as substituted by S.R.O. 1439(I)/2026"],
    ["Paper, electronic or microfilm form all allowed", "Regulation 6"],
])}
<p>For a real estate agent, FBR's short guidance lists the core deal file as the CNIC of seller and purchaser, the sale deed, the bank draft and the CDD form.</p>

<h2 id="timing">When the Documents Must Be in Hand</h2>
<p>Regulation 8(12) says identity of the customer and beneficial owner is verified before establishing a business relationship or conducting an occasional transaction. Regulation 8(13) allows verification shortly after only if it happens as soon as reasonably practicable, is essential not to interrupt normal business, and the risks are effectively managed. A customer who will not produce documents should be refused, recorded on the refused list, and considered for an STR, as FBR's FAQs (Q41) suggest.</p>
""",
    faqs=[
        ("What documents are required for DNFBP registration?",
         "An NTN and IRIS access for the business, details of owners, partners or directors and beneficial owners, the compliance officer's details, and any information FBR requires, including criminal records of senior management and beneficial owners under regulation 3(2)."),
        ("Which ID can I accept from an overseas Pakistani customer?",
         "Regulation 8(11)(a) allows a NICOP and/or a machine-readable passport for non-resident or overseas Pakistanis and dual nationals."),
        ("What documents does a company customer need to give?",
         "Certified copies of the board resolution, memorandum and articles, certificate of incorporation, commencement declaration and directors list where applicable, and identity documents of directors, beneficial owners and authorised persons."),
        ("What does “Original seen” mean?",
         "Regulation 6 requires copies of identity and verification documents to be stamped “Original seen” by the real estate agent, DPMS or accountant after viewing the originals."),
        ("How long must CDD documents be kept?",
         "At least five years after the business relationship ends; records relating to STRs and CTRs at least ten years from filing, per FBR's FAQs."),
        ("Can I complete the deal before collecting documents?",
         "Only in the limited case regulation 8(13) allows: verification as soon as reasonably practicable, essential to avoid interrupting business, with risks managed."),
    ],
    sources=[S_REG, S_1439, S_FAQ, S_REA, S_C2, S_PORTAL],
    related=[(X["main"], "Complete DNFBP guide"), (B["ubo"], "Beneficial owners"), (B["sole"], "Sole proprietors"), (X["svc"], "DNFBP compliance service")],
)

# 6 ---------------------------------------------------------------- PEPs
PEP = post(
    slug=SL["pep"],
    title="Politically Exposed Persons (PEPs): Rules for DNFBPs",
    h1="Politically Exposed Persons in Property and Jewellery Deals: FBR's PEP Rules for DNFBPs, Explained",
    crumb="PEPs and DNFBPs",
    description="Selling property or gold to a politician, senior officer or their family? Who is a PEP under FBR's regulations and the EDD steps regulation 9 requires.",
    keywords="politically exposed person pakistan, pep dnfbp, pep real estate agent, pep jeweller aml, enhanced due diligence pep fbr, close associate pep",
    read="11 min read",
    banner="A PEP customer is not forbidden. But regulation 9 sets minimum steps that must be taken before the deal, not after it.",
    tldr=("FBR's Regulations define a politically exposed person as anyone who is or has been entrusted with a prominent public function in Pakistan, "
          "abroad or in an international organisation, including heads of state or government, senior politicians, senior government, judicial or "
          "military officials, senior executives of state-owned corporations and political party officials. Family members (spouse, lineal "
          "ascendants and descendants, siblings) and close associates are covered too. Regulation 9 requires a system to identify PEPs before and "
          "during a relationship, senior management approval, reasonable measures to establish source of wealth and funds, and enhanced ongoing monitoring."),
    lead=("Pakistani property and gold markets serve a large number of public officials, politicians and their families. FBR's Regulations do not "
          "ask DNFBPs to turn them away. They ask for something narrower and more demanding: know when the customer is a PEP, get senior approval, "
          "find out where the money came from, and watch the relationship more closely. This guide explains each element from the text of "
          "regulations 2 and 9 and FBR's FAQs, with how it works in a property office or a jewellery shop."),
    answers={
        "who": "A person who is or has been entrusted with a prominent public function at home, abroad or in an international organisation.",
        "family": "Family members (spouse, lineal ascendants and descendants, siblings) and close associates are treated with the PEP.",
        "steps": "Regulation 9(3): a system to identify PEPs, senior management approval, source of wealth and funds, and enhanced ongoing monitoring.",
        "former": "FBR's FAQs: consider the influence the person can still exercise and links between past and current functions before declassifying.",
    },
    svc=svc("A PEP Procedure Your Office Can Actually Run",
            "We write a PEP identification step into your CDD form, set the approval and source-of-wealth checks regulation 9 requires, and train you or your staff to apply them.",
            ["PEP, family member and close associate questions built into your CDD form",
             "A senior management approval record for each PEP relationship",
             "A source-of-wealth checklist using documents customers actually have",
             "Enhanced monitoring rules for existing PEP customers",
             "DNFBP registration and goAML access if you do not have them yet"],
            ["Learning after the deal that a buyer was a PEP means the regulation 9 steps were missed",
             "Treating only the official, not the spouse or business partner, misses the family and associate rules",
             "Source of wealth recorded as “business” without any document is not a reasonable measure"],
            "Dealing with PEP customers?", "Set up my PEP checks", "a PEP procedure and CDD update"),
    cta_p="Tell us what you sell and how often public office holders buy from you; we tailor the PEP step to that.",
    wa_text="Assalam o Alaikum, PEP customers ke liye DNFBP rules ke mutabiq procedure chahiye.",
    about=about(),
    body=f"""
{SERIES("pep")}

<h2 id="who">Who Counts as a PEP</h2>
<p>Regulation 2(1)(m) of FBR's AML/CFT Regulations for DNFBPs 2020 defines “Politically Exposed Persons” as “any individual who is or has been entrusted with a prominent public function either domestically or by a foreign country, or in an international organization”, and includes, without limiting it:</p>
{table(["Type", "Examples named in the regulation"], [
    ["Domestic PEPs", "Heads of State or of government, senior politicians, senior government, judicial or military officials, senior executives of state owned corporations, political party officials"],
    ["Foreign PEPs", "The same functions held for a foreign country"],
    ["International organisation PEPs", "Members of senior management or individuals entrusted with equivalent functions"],
])}
<p>“Is or has been” matters: a retired senior official is within the definition. FBR's short guidance for real estate agents lists PEPs, their close associates and family members first among examples of higher-risk customers.</p>

<h2 id="family">Family Members and Close Associates</h2>
<p>The Regulations extend PEP treatment beyond the office holder:</p>
{table(["Category", "Definition in the Regulations"], [
    ["Family member, reg. 2(1)(i)", "A spouse of the PEP; lineal ascendants and descendants; and siblings"],
    ["Close associate, reg. 2(1)(e)", "Someone known to have joint beneficial ownership of a legal person or arrangement, or any other close business relations with the PEP; someone with sole beneficial ownership of a legal person or arrangement known to be set up for the PEP's benefit; or someone reasonably found or believed to be closely connected with the PEP, socially or professionally"],
])}
<p>In practice, the plot bought in a son's name, the jewellery paid for by a brother-in-law, and the company owned by a long-time business partner can all bring a deal within the PEP rules.</p>

<h2 id="steps">What Regulation 9 Requires</h2>
<p>Regulation 9(1)(c) makes EDD compulsory for PEPs and their close associates and family members. Regulation 9(3) then sets the minimum:</p>
<ol>
<li><strong>Identify.</strong> “Implement appropriate risk management systems to determine if a customer or beneficial owner is a PEP or a close associate or a family member of a PEP, both prior to establishing a business relationship or conducting a transaction, and periodically throughout the course of the business relationship.”</li>
<li><strong>Approve.</strong> Obtain senior management approval to establish or continue the relationship, including where an existing customer later becomes a PEP.</li>
<li><strong>Source.</strong> Take reasonable measures to establish the source of wealth and the source of funds of customers and beneficial owners identified as PEPs, family members or close associates.</li>
<li><strong>Monitor.</strong> Conduct enhanced ongoing monitoring of the relationship.</li>
</ol>
<p>The general EDD measures in regulation 9(2) can be added: more information on the customer and the purpose of the transaction, more frequent updating of identification data, and more controls on the pattern of transactions.</p>

<h2 id="practice">How It Works in a Property Office or Jewellery Shop</h2>
{table(["Step", "Property office", "Jewellery shop (DPMS)"], [
    ["Identify", "Ask on the CDD form whether the buyer, seller or beneficial owner holds or has held public office, or is a family member or associate of someone who has", "Ask the same at any cash sale of Rs 2 million or more"],
    ["Approve", "Senior management, the proprietor for a sole proprietorship, signs off before token money is accepted", "The owner or manager signs off before the sale is completed"],
    ["Source", "Bank statement, sale deed of a property sold, tax return, inheritance papers", "Bank withdrawal record, tax documents, business accounts"],
    ["Monitor", "Review the customer's further deals more closely", "Watch repeat purchases and the use of cash"],
])}
<p>FBR's short guidance for real estate agents gives examples of evidence of source of wealth: “details of the bank account the funds came from or verification from evidence of sold property such as a sale deed, wealth return, inheritance payment or audited financials of a business.” A PEP who is also an FBR filer usually has a wealth statement; our {a("/blogs/wealth-statement-guide-pakistan-2026", "wealth statement guide")} explains what it shows.</p>

<h2 id="former">When Does a PEP Stop Being a PEP?</h2>
<p>FBR's FAQs (Q56) do not set a fixed period. They say the entity “should consider the level of influence that the individual could still exercise and whether the individual's previous and current function are linked in any way.” A senior official who retired last year and now advises a ministry is still a PEP in substance. A clerk-level appointment held decades ago was never within the definition. Record the reasoning when you declassify someone.</p>

<h2 id="example">Example: A Plot Bought in a Daughter's Name</h2>
<p>A buyer in Islamabad asks a dealer to arrange a Rs 45,000,000 plot in his daughter's name. The CDD form reveals that the buyer retired last year as a senior official in a federal ministry. The daughter is the customer; the father is a PEP who has held a prominent public function, and she is his family member. Under regulation 9, the dealer obtains senior management approval, asks for the source of funds (a bank transfer from the father's account) and the source of wealth behind it (pension commutation and the sale of an earlier property, with the sale deed), screens both names against sanctions lists, and marks the relationship for enhanced monitoring. If the explanation does not hold together, the dealer considers an STR on goAML; see our {a(X["goaml"], "goAML guide")}.</p>
""",
    faqs=[
        ("Who is a politically exposed person in Pakistan?",
         "Under FBR's Regulations, anyone who is or has been entrusted with a prominent public function domestically, abroad or in an international organisation, including senior politicians, senior government, judicial or military officials, senior executives of state owned corporations and political party officials."),
        ("Can a real estate agent deal with a PEP?",
         "Yes. The Regulations do not prohibit it, but regulation 9 requires senior management approval, reasonable measures on source of wealth and funds, and enhanced ongoing monitoring."),
        ("Are a PEP's children covered?",
         "Yes. Family members include the spouse, lineal ascendants and descendants and siblings of the PEP."),
        ("Who is a close associate of a PEP?",
         "Someone with joint beneficial ownership of a legal person with the PEP or other close business relations, someone owning a vehicle set up for the PEP's benefit, or someone closely connected socially or professionally."),
        ("Is a retired official still a PEP?",
         "The definition covers anyone who “is or has been” entrusted with a prominent public function. FBR's FAQs say to weigh remaining influence and links between past and current roles before declassifying."),
        ("What proof of source of wealth can a PEP customer give?",
         "FBR's guidance mentions bank account details, a sale deed of property sold, a wealth return, an inheritance payment or audited business accounts."),
    ],
    sources=[S_REG, S_FAQ, S_REA, S_DPMS, S_GOAML],
    related=[(B["ubo"], "Beneficial owners"), (B["tfs"], "Sanctions screening"), (X["rea"], "Real estate agents and AML"), (X["svc"], "DNFBP compliance service")],
)

# 7 ---------------------------------------------------------------- beneficial owners
UBO = post(
    slug=SL["ubo"],
    title="Beneficial Owner (UBO) Checks for DNFBPs in Pakistan",
    h1="Who Really Owns the Buyer? Beneficial Ownership Checks for Real Estate Agents, DPMS and Accountants",
    crumb="Beneficial Owners (UBO)",
    description="When the buyer is a company, trust or someone acting for another, FBR's regulations require you to find the beneficial owner. Tests and worked examples.",
    keywords="beneficial owner dnfbp, ultimate beneficial owner pakistan, ubo real estate agent, beneficial ownership fbr regulations, 25 percent ownership aml pakistan",
    read="12 min read",
    banner="The name on the transfer is not always the person behind the money. FBR's Regulations make finding that person part of every deal.",
    tldr=("FBR's FAQs define the beneficial owner as the natural person who ultimately owns or controls a customer, or on whose behalf a transaction "
          "is conducted, including legal heirs and anyone exercising ultimate effective control. Regulation 8(9) sets a three-step test for companies: "
          "the natural person with a controlling ownership interest; if in doubt or none, the person controlling it by other means; failing both, the "
          "senior managing official. For trusts, regulation 8(10) requires the settlor, trustees, protector, beneficiaries and anyone in ultimate "
          "control. FBR's FAQs illustrate indirect ownership: 50% of a company that owns 25% of the buyer is 12.5% indirect ownership."),
    lead=("Property and high-value goods are bought through companies, firms, family trusts and attorneys every day in Pakistan, often for good "
          "reasons. They can also be used to put distance between an asset and the person who paid for it. That is why FBR's Regulations do not stop "
          "at identifying the customer on the paperwork. They require you to look through it to the natural person who ultimately owns or controls "
          "it. This guide explains the test, the documents, and how to apply it to the structures you actually see."),
    answers={
        "who": "The natural person who ultimately owns or controls the customer, or on whose behalf a transaction is conducted, including legal heirs and anyone in ultimate effective control.",
        "company": "Regulation 8(9): controlling ownership interest first; then control by other means; failing both, the senior managing official.",
        "indirect": "FBR's FAQs: if A owns 50% of a company that owns 25% of the buyer, A indirectly owns 12.5% of the buyer.",
        "trust": "Regulation 8(10): settlor, trustees, protector, beneficiaries or class, and any person exercising ultimate effective control.",
    },
    svc=svc("Beneficial Ownership Checks Built Into Your Deal File",
            "We add the regulation 8(9) and 8(10) tests to your CDD forms, show you which company and trust documents to ask for, and check complex buyers with you.",
            ["Beneficial ownership section on your CDD form for companies, firms and trusts",
             "Document checklist for proving ownership and control",
             "Help with layered or overseas ownership structures",
             "Sanctions and PEP screening of the beneficial owners you identify",
             "DNFBP registration and goAML access if not already in place"],
            ["Recording only the company's name leaves the person behind the money unknown",
             "Stopping at a director who holds no shares can miss the real controller",
             "An unexplained structure that you could not see through is itself a reason to consider an STR"],
            "Buyers coming through companies or trusts?", "Check beneficial ownership with me", "beneficial ownership procedures and a complex-buyer review"),
    cta_p="Send the type of buyer structure you see most often; we show you exactly what to collect.",
    wa_text="Assalam o Alaikum, company/trust buyer ke beneficial owner ki DNFBP check karni hai.",
    about=about(),
    body=f"""
{SERIES("ubo")}

<h2 id="who">The Definition</h2>
<p>FBR's FAQs on AML/CFT (Q49) define the beneficial owner as “the natural person who ultimately owns or controls a customer or the person on whose behalf a transaction is being conducted and includes legal heir(s) and the person who exercise ultimate effective control over a person.” Two features stand out. The beneficial owner is always a <strong>natural person</strong>; the FAQs (Q51) explain that a legal person cannot exert ultimate control, because legal persons are always controlled by natural persons in the end. And the definition covers both <strong>ownership</strong> and <strong>control</strong>, so a person with no shares can still be the beneficial owner.</p>
<p>Regulation 8(3) of FBR's AML/CFT Regulations for DNFBPs 2020 requires you to identify the beneficial owner and take reasonable measures to verify that person's identity from reliable and independent sources, “such that the DNFBP is satisfied that it knows who the beneficial owner is”.</p>

<h2 id="company">The Three-Step Test for Companies and Other Legal Persons</h2>
<p>Regulation 8(9) sets the order:</p>
{table(["Step", "Who you identify", "When you move to the next step"], [
    ["(a)", "The natural person, if any, who ultimately has a controlling ownership interest", "If there is doubt whether that person is the beneficial owner, or no natural person controls through ownership"],
    ["(b)", "The natural person, if any, exercising control by other means", "If no natural person is identified under (a) or (b)"],
    ["(c)", "The natural person who holds the position of senior managing official", "This is the fallback, not a shortcut"],
])}
<p>Regulation 8(7) adds that for legal persons you must understand the nature of the customer's business and its ownership and control structure. Regulation 8(8) asks for its name, legal form, proof of existence, the powers that bind it, its senior managers, and its registered office and principal place of business.</p>

<h2 id="indirect">Direct and Indirect Ownership</h2>
<p>FBR's FAQs (Q50) use a 25% example for direct ownership and show how indirect ownership is calculated:</p>
<blockquote><p>“if Company ‘B’ is owned to the extent of 25% by Company ‘A’, and Company ‘A’ is owned to the extent of 50% by a natural person, then the said Person is an indirect owner of Company ‘B’ through Company ‘A’, to the extent of 12.5% ownership in Company ‘B’ i.e. 50% of 25%.”</p></blockquote>
{table(["Structure", "Calculation", "Indirect interest in the buyer"], [
    ["A owns 50% of HoldCo; HoldCo owns 25% of the buyer", "50% × 25%", "12.5%"],
    ["A owns 80% of HoldCo; HoldCo owns 60% of the buyer", "80% × 60%", "48%"],
    ["A owns 100% of HoldCo; HoldCo owns 30% of the buyer", "100% × 30%", "30%"],
])}
<p>Multiply through each layer. Where several people hold small stakes and none reaches a controlling interest, step (b) asks who controls the company by other means, for example through an agreement, a family arrangement or the power to appoint directors.</p>

<h2 id="trust">Trusts, Waqfs and Other Arrangements</h2>
<p>Regulation 8(10) requires, for a trust, the identity of the settlor, the trustees, the protector if any, the beneficiaries or class of beneficiaries, and any other natural person exercising ultimate effective control, including through a chain of control or ownership. For a waqf or other legal arrangement, the persons in equivalent or similar positions. Where any of those is itself a legal person or arrangement, its beneficial owner must be identified too. The documents are listed in regulation 8(11)(c); see our {a(B["docs"], "documents checklist")}.</p>

<h2 id="behalf">The Person “On Whose Behalf”</h2>
<p>Beneficial ownership is not only about companies. FBR's short guidance for real estate agents says the beneficial owner is “a natural person on whose behalf a transaction is being conducted”. A plot bought in a driver's name with an employer's money, or jewellery bought by a relative who is reimbursed by someone else, has a beneficial owner who is not the customer on paper. Regulation 8(4) also requires you to identify and verify anyone acting for the customer and their authority to act.</p>

<h2 id="legal">Legal Owner Versus Beneficial Owner</h2>
<p>FBR's FAQs (Q51) distinguish the legal owner, who holds title, from the beneficial owner, who has the right to enjoy or benefit from the asset, including its income. In most cases they are the same person. The cases where they differ are exactly the ones regulation 8 is aimed at: nominees, benami-style arrangements and layered companies.</p>

<h2 id="example">Example: A Shop Bought Through a Private Limited Company</h2>
<p>A Lahore developer is selling a Rs 90,000,000 shop to ABC (Pvt) Ltd. The SECP papers show two shareholders: XYZ Holdings (Pvt) Ltd with 70% and an individual, Sana, with 30%. XYZ Holdings is 60% owned by Faisal and 40% by his brother. Faisal's indirect interest in ABC is 60% × 70% = 42%; his brother's is 28%; Sana holds 30% directly. The developer records all three, verifies their CNICs, screens them against sanctions lists, asks whether any is a PEP (see our {a(B["pep"], "PEP guide")}), and obtains the board resolution authorising the person signing. If the structure had led abroad or to a trust with no clear controller, regulation 8(9)(b) and (c) would apply, and an unexplained structure would be a reason to consider an STR.</p>

<h2 id="screen">After You Identify the Beneficial Owner</h2>
<ul>
<li><strong>Screen</strong> them against UN and domestic sanctions lists; regulation 13 covers beneficial owners expressly. See {a(B["tfs"], "sanctions screening")}.</li>
<li><strong>Risk-rate</strong> the customer: FBR's short guidance lists “unclear or unconfirmed beneficial owner (complex control/ownership structure)” among higher-risk cases needing EDD.</li>
<li><strong>Keep</strong> the evidence in the deal file for at least five years after the relationship ends.</li>
</ul>
""",
    faqs=[
        ("What is an ultimate beneficial owner?",
         "FBR's FAQs define it as the natural person who ultimately owns or controls a customer, or on whose behalf a transaction is conducted, including legal heirs and anyone exercising ultimate effective control."),
        ("Can a company be a beneficial owner?",
         "No. FBR's FAQs say a beneficial owner must always be a natural person, because legal persons are always controlled by natural persons in the end."),
        ("How do I calculate indirect ownership?",
         "Multiply the stakes through each layer. FBR's FAQs give the example of 50% of a company that owns 25% of the buyer, which is 12.5% indirect ownership."),
        ("What if no shareholder controls the company?",
         "Regulation 8(9) moves to the person who controls it by other means, and if none, to the senior managing official."),
        ("Who is the beneficial owner of a trust?",
         "Regulation 8(10) requires the settlor, trustees, protector if any, beneficiaries or class of beneficiaries, and any natural person exercising ultimate effective control."),
        ("Do beneficial owners need sanctions screening?",
         "Yes. Regulation 13 and FBR's FAQs (Q47) require screening of the client, its beneficial owner and persons acting on its behalf."),
    ],
    sources=[S_FAQ, S_REG, S_REA, S_TFS],
    related=[(B["pep"], "PEPs"), (B["docs"], "Documents checklist"), (B["dev"], "Developers and societies"), (X["svc"], "DNFBP compliance service")],
)
