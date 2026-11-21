"""PRA series posts 6-10: who must register, compulsory notice, sole proprietors, FBR-registered (P+NTN), changes and de-registration."""
from pra_common import *

WHO = post(
    slug=SL["who"],
    title="Who Must Register With PRA? Section 25 Explained (2026)",
    h1="Who Must Register With PRA? Section 25, Voluntary Registration and the Recipient Rule",
    crumb="Who Must Register With PRA",
    description="Section 25 of the Punjab Sales Tax on Services Act: who must register with PRA, when voluntary registration is allowed, and the buyer rule.",
    keywords="who must register with pra, pra registration requirements, pra registration means, section 25 punjab sales tax on services act, voluntary registration pra, is pra registration mandatory",
    read="10 min read",
    banner="The test in the Act is short: do you provide a taxable service from an office or place of business in Punjab?",
    tldr=("Section 25(1) of the Punjab Sales Tax on Services Act 2012 says a person shall register who (a) provides any taxable service from his office "
          "or place of business in the Punjab, (b) is otherwise required to register under the Act or rules, or (c) meets criteria PRA prescribes. "
          "Section 26 allows voluntary registration by someone carrying on an economic activity who is not required to register, if PRA is satisfied "
          "on four conditions. Section 25(3) treats an unregistered recipient of certain taxable services as registered for that tax period. Rule 2(1) "
          "repeats the duty for every person providing taxable services."),
    lead=("\"Do I need PRA?\" is the first question every Punjab service business asks, and the answer is in four short sections of the Act. This guide "
          "reads them in order, with the questions they leave you to answer about your own business."),
    answers={
        "rule": "You must register if you provide a taxable service from an office or place of business in Punjab (s.25(1)(a)), or another provision requires it.",
        "voluntary": "Section 26 lets a person not required to register apply at any time; PRA registers them if four conditions are met.",
        "recipient": "An unregistered recipient of a service made taxable by section 3(2) is treated as registered for that tax period (s.25(3)).",
        "provinces": "Services rendered in Punjab need a separate Punjab registration even if you are registered in another province (rule 2(4)).",
        "check": "Ask three questions: is the service taxable, is it provided from a place of business in Punjab, and is any other provision catching you.",
    },
    svc=svc("Not Sure If You Need PRA? Ask Before You Register",
            "We look at what you sell and where you sell it from, tell you whether PRA registration applies, and register you if it does.",
            ["A plain answer on whether section 25 applies to your business",
             "Voluntary registration if a client or tender requires it",
             "Separate Punjab registration where you work across provinces",
             "Filing on PRA IRIS and follow-up to the certificate"],
            ["Waiting for a notice: PRA can register you compulsorily under section 27",
             "Registering under the wrong basis or activity",
             "Assuming another province's registration covers Punjab (rule 2(4))"],
            "Wondering whether your business needs PRA?", "Tell me if I need PRA"),
    wa_text="Assalam o Alaikum, kya mujhe PRA registration ki zaroorat hai? Business ki details bhej raha hoon.",
    body=f"""
{SERIES("who")}

<h2 id="rule">The Rule: Section 25(1)</h2>
<p>Section 25(1) of the Punjab Sales Tax on Services Act 2012 lists three cases. A person shall register who:</p>
<ol>
<li><strong>(a)</strong> "Provides any taxable service from his office or place of business in the Punjab"; or</li>
<li><strong>(b)</strong> "Is otherwise required to be registered under any of the provisions of the Act or the rules"; or</li>
<li><strong>(c)</strong> "Fulfills any other criteria or requirements which the Authority may prescribe" under section 25(2).</li>
</ol>
<p>Section 25(2) adds that registration is regulated in the manner, conditions and restrictions PRA prescribes by Gazette notification. Rule 2(1) of the 2012 Rules repeats the duty: "Every person engaged in providing taxable service or services or pay tax under the Act is required to be registered."</p>
<p>Clause (a) has two parts, and you need both: the service is a <strong>taxable service</strong>, and you provide it <strong>from an office or place of business in Punjab</strong>. Which services are taxable is set by the Act's charging provisions and schedules, which PRA updates through Finance Acts; check the current list on {a(S_PRA[1], "PRA's website")} or ask us before you decide.</p>

<h2 id="questions">Three Questions to Ask About Your Business</h2>
{table(["Question", "If yes", "If no"], [
    ["Is what I charge for a taxable service under the current Act and schedules?", "Go to the next question", "Section 25(1)(a) does not catch you; check (b) and (c)"],
    ["Do I provide it from an office or place of business in Punjab?", "Registration is required under s.25(1)(a)", "Check whether another province applies"],
    ["Does any other provision or PRA notification require me to register?", "Register under s.25(1)(b) or (c)", "You may still register voluntarily (s.26)"],
])}
<p>Our guide on {a(X["which"], "which provincial authority applies")} helps when you work from more than one province.</p>

<h2 id="voluntary">Voluntary Registration: Section 26</h2>
<p>Some businesses are asked for PRA registration by clients or in tenders before the law requires it. Section 26(1) allows "a person who carries on an economic activity but is not required to be registered" to apply "at any time". Under section 26(2), PRA may register the person if satisfied that:</p>
<ul>
<li>(a) the person is providing, or shall provide, a service that would be taxable if the person were registered;</li>
<li>(b) the person has a place of business at which he carries on an economic activity;</li>
<li>(c) there are reasonable grounds to believe the person will keep proper records and file regular returns; and</li>
<li>(d) if the activity has already started, the person has kept proper records and complied with other tax laws.</li>
</ul>
<p>Condition (d) is why an up-to-date FBR income tax record matters even for a voluntary applicant. Voluntary registration also brings every duty of a registered person, so register when you are ready to meet them.</p>

<h2 id="recipient">When the Buyer Is Treated as Registered: Section 25(3)</h2>
<p>Section 25(3) covers the other side of a transaction. A person who receives a service that is taxable by virtue of section 3(2), and is not registered, "shall be deemed to be a registered person" for the tax period in which the service is received, invoiced or paid for, whichever is earlier, and all the Act and rules apply to that person for that period "as if that person had provided the service". In plain terms, buying certain services can bring an unregistered business into PRA's net for that period.</p>

<h2 id="provinces">Working in More Than One Province</h2>
<p>Rule 2(4) is direct: a person providing taxable services in more than one province including Punjab "is required to take a separate registration for the Punjab" for services rendered in Punjab. Registration in Sindh, Khyber Pakhtunkhwa or Balochistan does not cover Punjab. See our guide for {a(X["cross"], "freelancers serving other provinces")}.</p>

<h2 id="check">If You Should Have Registered Already</h2>
<p>Section 27 lets PRA register a person who is required to register but has not applied, after advance notice and a hearing. It is better to register yourself first. If a notice has already arrived, read {a(B["comp"], "compulsory registration and e-Enrolment")} before doing anything else.</p>
""",
    faqs=[
        ("Is PRA registration mandatory?", "Yes for anyone who provides a taxable service from an office or place of business in Punjab, or is otherwise required by the Act, rules or a PRA notification (section 25(1))."),
        ("Can I register with PRA voluntarily?", "Yes. Section 26 allows a person carrying on an economic activity who is not required to register to apply at any time, subject to four conditions."),
        ("I am registered with SRB in Sindh. Do I need PRA too?", "For services rendered in Punjab, rule 2(4) requires a separate Punjab registration."),
        ("Can buying a service make me liable to PRA?", "Section 25(3) treats an unregistered recipient of a service taxable under section 3(2) as registered for that tax period."),
        ("What happens if I do not register?", "Section 27 lets PRA register you compulsorily after advance notice and an opportunity to be heard."),
    ],
    sources=[S_ACT4, S_RULES, S_PRA],
    related=[(SVC, "PRA registration service"), (B["comp"], "PRA compulsory registration notice"), (X["which"], "Which provincial authority applies")],
)

COMP = post(
    slug=SL["comp"],
    title="PRA Compulsory Registration Notice and e-Enrolment: What to Do",
    h1="PRA Compulsory Registration Notice (Section 27) and e-Enrolment: What to Do Next",
    crumb="PRA Compulsory Registration",
    description="Got a PRA compulsory registration notice? Section 27 rights, the notice bar code, e-Enrolment on IRIS, and relief if you were registered by mistake.",
    keywords="pra compulsory registration, pra notice registration, pra e-enrolment, section 27 punjab sales tax on services, pra notice bar code, pra registration notice",
    read="10 min read",
    banner="A PRA registration notice is not a penalty. It is a step you can answer, and the law gives you a hearing.",
    tldr=("Section 27 of the Punjab Sales Tax on Services Act 2012 lets PRA register a person who is required to register but has not applied. It must "
          "notify the person at least fifteen days before the registration takes effect, with the date and the registration number, and no one may be "
          "registered compulsorily without advance notice and an opportunity of being heard. On PRA IRIS, a person with a notice uses the Notice/Compulsory "
          "basis and the Notice Bar Code, and after a 27(1) order completes e-Enrolment. Rule 13 cancels a wrong compulsory registration from the start "
          "with no tax liability for that period."),
    lead=("Letters from PRA about compulsory registration worry business owners more than they need to. The Act gives you a timeline and a hearing, and "
          "the IRIS system gives you a set route. This guide explains both, and what to do if PRA has registered you by mistake."),
    answers={
        "law": "PRA may register a person who should have registered, but only after advance notice and a hearing, and must notify fifteen days before it takes effect.",
        "options": "If you agree you must register, apply on the notice route; if you do not, answer the notice with reasons at the hearing.",
        "iris": "On PRA IRIS choose the Notice/Compulsory basis and verify the Notice Bar Code; after a 27(1) order, use e-Enrolment.",
        "wrong": "Rule 13: a compulsory registration later proved wrong is cancelled from the start, with no tax liability for that period.",
    },
    svc=svc("PRA Notice? We Handle the Response and the Registration",
            "We read the notice, tell you whether registration genuinely applies, and either register you on the notice route or prepare your reply for the hearing.",
            ["Reading the notice and its dates with you",
             "A clear view on whether section 25 applies to your business",
             "Registration through the notice bar code or e-Enrolment",
             "A written reply with reasons if registration does not apply"],
            ["Ignoring the notice: PRA may register you anyway under section 27",
             "Registering voluntarily when a notice exists, creating two records",
             "Missing the hearing where you could show registration does not apply"],
            "Received a PRA registration notice?", "Help me with my PRA notice"),
    wa_text="Assalam o Alaikum, PRA ka registration notice aaya hai. Notice bhej raha hoon.",
    body=f"""
{SERIES("comp")}

<h2 id="law">What Section 27 Allows, and What It Requires</h2>
<p>Section 27(1): if PRA "is satisfied that a person who is required to be registered and has not applied for registration", it "shall register the person and shall, not later than fifteen days before the day on which the registration takes effect, notify the person of the registration, the day on which it takes effect, and the registration number issued to the person."</p>
<p>Section 27(2) is the safeguard: "No person shall be registered compulsorily without being given an advance notice and an opportunity of being heard in such manner as the Authority may specify." Section 27(3) lets PRA authorise officers by Gazette notification to carry out compulsory registration.</p>
{table(["Step", "What happens", "Section"], [
    ["Advance notice", "You are told PRA believes you must register", "27(2)"],
    ["Hearing", "You can show why registration does or does not apply", "27(2)"],
    ["Order and notification", "Registration date and number notified at least 15 days before it takes effect", "27(1)"],
    ["e-Enrolment", "You activate the registration on PRA IRIS", "PRAL manual, part 3.2"],
])}

<h2 id="options">Your Two Options</h2>
<p><strong>If registration does apply to you</strong> (you provide a taxable service from a place of business in Punjab, see {a(B["who"], "section 25")}), the fastest course is to complete registration on the notice route, with complete and correct details.</p>
<p><strong>If it does not apply</strong>, use the hearing. Explain what you actually do, where you do it from, and why section 25 does not catch it. Keep a copy of everything you send.</p>

<h2 id="iris">The IRIS Route for a Notice</h2>
<p>The PRAL user manual describes two notice paths on PRA IRIS.</p>
<h3>Notice bar code (part 3.1)</h3>
<p>Click New Registration as usual. In the <strong>Registration Basis</strong> drop-down choose <strong>Notice/Compulsory</strong>. The system then asks you to "provide and verify the Notice Bar Code". After that the screens are the same as a voluntary application: person type, verification codes, basic information, address, business, utilities and verification. Our {a(B["proc"], "step-by-step guide")} covers them.</p>
<h3>e-Enrolment after a 27(1) order (part 3.2)</h3>
<p>Once "the 27(1) Order on Notice for Compulsory Registration" has been sent by the tax officer, open the IRIS site and click <strong>e-Enrolment</strong>. Fill the mandatory fields and captcha and submit. A verification SMS and code go to your mobile and email; enter them and submit. Then log in with your registered number and password, where you will see the notification that you are registered.</p>

<h2 id="wrong">If PRA Registered You by Mistake</h2>
<p>Rule 13 of the 2012 Rules: where a person has been compulsorily registered and "it is subsequently proved that such person is not liable to registration", PRA "may cancel such registration ab initio" and the person "shall not be subjected to any tax liability for the period of his such compulsory registration". Ab initio means from the start, as if it never happened.</p>
<p>You need proof: what services you provide, from where, and why they fall outside section 25. A registration that is correct but no longer needed is a different case, handled by de-registration; see {a(B["chg"], "de-registration")}.</p>

<h2 id="dont">What Not to Do</h2>
<ul>
<li><strong>Do not ignore the notice.</strong> Section 27 lets PRA register you whether you respond or not.</li>
<li><strong>Do not open a separate voluntary application</strong> to get around a notice. Use the notice route the manual describes.</li>
<li><strong>Do not lend or borrow a registration</strong> to avoid one. Rule 4 bars anyone except the registered person from using it.</li>
</ul>
""",
    faqs=[
        ("Can PRA register me without my consent?", "Yes, under section 27, but only after advance notice and an opportunity of being heard, and with at least fifteen days' notice of the date it takes effect."),
        ("What is the PRA notice bar code?", "On PRA IRIS, a person registering on a notice chooses the Notice/Compulsory basis and enters and verifies the Notice Bar Code from the notice."),
        ("What is PRA e-Enrolment?", "After a 27(1) order is sent, the taxpayer clicks e-Enrolment on IRIS, verifies codes sent by SMS and email, and logs in to see the registration."),
        ("What if I am not liable to register?", "Explain at the hearing. If you were registered and it is later proved you were not liable, rule 13 cancels the registration ab initio with no tax liability for that period."),
        ("Is compulsory registration a fine?", "No. Section 27 is a registration step. Any penalty would come from other provisions of the Act."),
    ],
    sources=[S_ACT4, S_RULES, S_MAN, S_LOGIN, S_PRA],
    related=[(SVC, "PRA registration service"), (B["who"], "Who must register with PRA"), (B["proc"], "PRA registration step by step")],
)

SOLE = post(
    slug=SL["sole"],
    title="PRA Registration for Sole Proprietors in Punjab (2026)",
    h1="PRA Registration for a Sole Proprietor: Individual Category, Documents and Steps (2026)",
    crumb="PRA for Sole Proprietors",
    description="How a sole proprietor registers with PRA as an individual: NTN first, Form PST-01 details, premises and bank account, one registration for all services, fee.",
    keywords="pra registration sole proprietor, pra registration individual, sole proprietorship pra registration, pra registration for freelancer punjab, pra registration small business",
    read="10 min read",
    banner="A sole proprietor registers with PRA as an individual, under his own CNIC and NTN. Here is what that means in practice.",
    tldr=("A sole proprietorship has no separate legal identity, so on Form PST-01 it registers in the Individual category under the owner's CNIC, with "
          "the owner's FBR NTN supplying the basic details on PRA IRIS. The trade name goes against each business place. Every service can go on one "
          "application and one certificate (rule 2(3)), and several shops with central billing in Punjab can share one registration (rule 2(2)). PRA "
          "charges no fee (rule 15); our fee is Rs 5,000, plus Rs 2,000 if an NTN is needed first."),
    lead=("Most PRA registrations we file are for one person running a service business: a salon, a consultancy, an agency, a workshop, a caterer. The "
          "Act and rules do not have a separate sole proprietor form, so the question is how a one-person business fits the individual route. This "
          "guide answers that, with the details that trip sole proprietors up."),
    answers={
        "category": "Individual: the proprietor's CNIC and FBR NTN are the identity; the trade name goes against the business place.",
        "steps": "Update the FBR NTN, collect premises, utility and bank details, then file Form PST-01 on PRA IRIS as an individual.",
        "trade": "Form PST-01 records a business or branch name and a trade name for each place, under the owner's registration.",
        "shops": "One registration can cover several places if billing or accounting is centralised in Punjab (rule 2(2)).",
        "sell": "Selling a registered business needs prior permission from the Commissioner (rule 14) and the buyer needs its own registration.",
    },
    svc=svc("Sole Proprietor PRA Registration, Start to Finish",
            "We register sole proprietors every week: NTN if needed, the right category and activity, and the certificate in your name and trade name.",
            ["FBR NTN check, or a new NTN for Rs 2,000",
             "Individual category with your trade name on each business place",
             "All your services on one application",
             "Filing on PRA IRIS and follow-up to the certificate"],
            ["Registering in the wrong category for a one-person business",
             "A trade name that does not match signboards and invoices",
             "Leaving out a second shop or a business bank account"],
            "Running your own service business in Punjab?", "Register my business with PRA"),
    wa_text="Assalam o Alaikum, sole proprietorship ki PRA registration karwani hai.",
    body=f"""
{SERIES("sole")}

<h2 id="category">Which Category: Individual</h2>
<p>Field 4 of Form PST-01 offers three categories: company, individual and AOP. A sole proprietorship is not a company and not an association, so it registers as an <strong>individual</strong>. The identity is the owner's: field 7 asks for the CNIC of an individual, and the PRA IRIS Basic Information screen fills from the owner's FBR record and cannot be edited there.</p>
<p>The business name is not lost. Fields 20 to 22 record, for each business place, a business or branch name and a <strong>trade name</strong>. Your shop or brand name sits there, under your own registration.</p>

<h2 id="steps">Steps for a Sole Proprietor</h2>
<ol>
<li><strong>Check or get your FBR NTN.</strong> PRA takes your basic details from FBR. If you have no NTN, start with {a(X["ntn"], "NTN registration")}.</li>
<li><strong>Collect the business details</strong>: address of each place, owned or rented (with the landlord's CNIC or NTN), the electricity reference number, gas connection, start date, and each business bank account. Our {a(B["docs"], "documents checklist")} lists them.</li>
<li><strong>Decide your principal service.</strong> One activity must be marked principal on IRIS.</li>
<li><strong>File on PRA IRIS</strong> under New Registration, Individual, with the codes sent to your phone and email. See the {a(B["proc"], "step-by-step guide")}.</li>
<li><strong>Keep the provisional certificate</strong> issued on applying (rule 3(1)) until the final PST-03 certificate arrives.</li>
</ol>

<h2 id="trade">One Person, Several Services or Shops</h2>
{table(["Situation", "What the rules allow", "Rule"], [
    ["Several services (e.g. design and printing)", "One application listing all; the certificate shows all", "2(3)"],
    ["Two or three shops with one billing system in Punjab", "One registration, all places listed", "2(2)"],
    ["Services also provided in another province", "A separate Punjab registration for services rendered in Punjab", "2(4)"],
])}
<p>Rule 2(5) then requires your registration number on every invoice, bill and voucher. Put it on your invoice template the day the certificate arrives.</p>

<h2 id="voluntary">Small Businesses and Voluntary Registration</h2>
<p>Some sole proprietors register because a corporate client or tender asks for a PRA number. If section 25 does not require you to register, section 26 allows voluntary registration where PRA is satisfied you provide or will provide a service that would be taxable, have a place of business, will keep proper records and file returns, and, if trading already, have kept records and complied with other tax laws. Your FBR income tax compliance matters for that last condition. Read {a(B["who"], "who must register")} to see which side of the line you are on.</p>

<h2 id="sell">Changes, Selling and Closing</h2>
<ul>
<li><strong>New address or name:</strong> report it on Form PST-01 under rule 11; PRA decides, preferably within thirty days.</li>
<li><strong>Selling the business:</strong> a registered business "shall not be sold or disposed off without prior permission from the Commissioner" (rule 14(1)); the buyer needs a new registration or approved changes (rule 14(2)). The Act also requires the former owner to tell the Commissioner within one month of a sale or transfer (section 20(1)).</li>
<li><strong>Closing down:</strong> apply for de-registration on Form PST-02 (rule 5). See {a(B["chg"], "changes and de-registration")}.</li>
</ul>
<p>Sole proprietors also have income tax work alongside PRA. Our {a(X["sole"], "sole proprietor services")} cover the FBR side.</p>
""",
    faqs=[
        ("Which category does a sole proprietor choose on PRA?", "Individual. Form PST-01 offers company, individual and AOP; a sole proprietorship registers under the owner's CNIC and NTN, with the trade name against the business place."),
        ("Can my shop name appear on the PRA registration?", "Yes. Form PST-01 records a business or branch name and a trade name for each place."),
        ("I have two shops. Do I need two PRA registrations?", "Not if billing or accounting is centralised in Punjab; rule 2(2) allows one registration, with both places listed."),
        ("How much does PRA registration cost a sole proprietor?", "PRA charges nothing (rule 15). Our fee is Rs 5,000, plus Rs 2,000 if you need an FBR NTN first."),
        ("Can I sell my PRA-registered business?", "Only with prior permission from the Commissioner (rule 14), and the buyer needs a new registration or approved changes."),
    ],
    sources=[S_RULES, S_ACT4, S_ACT3, S_MAN, S_PRA],
    related=[(SVC, "PRA registration service"), (B["docs"], "PRA documents checklist"), (X["sole"], "Sole proprietor tax services")],
)

FBR = post(
    slug=SL["fbr"],
    title="Already on FBR Sales Tax? PRA Registration and P+NTN Explained",
    h1="Already Registered With FBR? PRA Registration, Rule 10 and Your P+NTN",
    crumb="PRA and FBR (P+NTN)",
    description="Businesses already registered with FBR: rule 10 automatic PRA registration with P+NTN, how to check it, update details and register new Punjab services.",
    keywords="pra p ntn, pntn pra, pra registration fbr registered, already registered with fbr pra, pra automatic registration, pra registration who already have ntn",
    read="9 min read",
    banner="If your business was on FBR's books, PRA may already have registered you. Check before you apply again.",
    tldr=("Rule 10 of the Punjab Sales Tax on Services (Registration and De-registration) Rules 2012 says taxpayers already registered with FBR were not "
          "required to apply again: they were registered automatically for the Act and told by email, SMS, courier or post, with \"P\" as a prefix to "
          "their NTN (P+NTN). Form PST-01 now has an option for PRA registration of persons who already have an NTN, authorising PRA to take their "
          "particulars from FBR. Under rule 11, changes to those particulars, including in rule 10 cases, are made on Form PST-01."),
    lead=("Businesses that registered with FBR years ago are often surprised to learn they may already have a PRA number. Others assume their FBR sales "
          "tax registration covers Punjab services when it does not. This guide explains the rule that links the two, and how to find out where you stand."),
    answers={
        "rule10": "Rule 10: existing FBR-registered taxpayers were registered with PRA automatically and given P+NTN as their PRA number.",
        "check": "Search the Taxpayer Profile Inquiry on e-PRA by PNTN (P followed by your NTN) or by CNIC.",
        "update": "Rule 11: report changed name, address or other particulars on Form PST-01, including for rule 10 registrations.",
        "new": "If you are not found, apply on PRA IRIS; Form PST-01 has an option for persons who already have an NTN.",
        "both": "FBR and PRA are separate registrations; services rendered in Punjab need the Punjab registration.",
    },
    svc=svc("Find Out If You Are Already on PRA",
            "We check your P+NTN, update stale details or file a new registration, whichever your record needs.",
            ["Check your P+NTN on PRA's Taxpayer Profile Inquiry",
             "Update old particulars on Form PST-01 (rule 11)",
             "New PRA registration if you are not found",
             "Add Punjab services missing from the registration"],
            ["Applying twice and ending up with two records",
             "An old automatic registration with outdated details",
             "Assuming FBR registration covers Punjab services"],
            "Registered with FBR and unsure about PRA?", "Check my PRA status"),
    wa_text="Assalam o Alaikum, FBR registered hoon, PRA status check karwana hai.",
    body=f"""
{SERIES("fbr")}

<h2 id="rule10">Rule 10: Automatic Registration and P+NTN</h2>
<p>Rule 10, headed "Automatic grant of registration", reads: "The existing taxpayers already registered with the Federal Board of Revenue shall not be required to file any new application for registration, they shall be automatically registered for the purpose of the Act and shall receive an intimation from the Authority either through email or SMS or by courier or post, assigning them 'P' as prefix to NTN (P+NTN)."</p>
<p>Two practical points follow. First, your PRA number may simply be the letter P followed by your NTN. Second, the intimation may have gone to an old email, phone or address, so many owners never saw it.</p>

<h2 id="check">How to Check</h2>
<p>The e-PRA portal's Taxpayer Profile Inquiry searches by PNTN, CNIC, passport number or registration/incorporation number. Search your P+NTN first, then your CNIC (or company registration number). The Active Taxpayer List (Sales Tax) on the same page shows whether the registration is active. Our {a(B["ver"], "verification guide")} explains each result.</p>
{table(["What you find", "What it means", "Next step"], [
    ["Registered, active, details correct", "You are already registered with PRA", "Use the number on invoices (rule 2(5))"],
    ["Registered, details outdated", "An automatic registration with old particulars", "Change on Form PST-01 (rule 11)"],
    ["Registered, a service missing", "The certificate does not list all services", "Add it on Form PST-01 (rules 2(3), 11)"],
    ["Not found", "No PRA registration", "Apply on PRA IRIS"],
])}

<h2 id="update">Updating an Automatic Registration</h2>
<p>Rule 11 covers it expressly: where the name, address or other particulars on the certificate change, "including the cases covered under rule 10", the registered person intimates the change on Form PST-01, and PRA "may either approve or reject the request for change preferably within thirty days". Keep the address and email current: Form PST-01's declaration accepts notices sent to them as legal notice.</p>

<h2 id="new">Applying When You Already Have an NTN</h2>
<p>Form PST-01 now carries an option for "PRA Registration, who already have NTN", with an authorisation that PRA may obtain your particulars from FBR. On PRA IRIS this is why the Basic Information screen arrives pre-filled and locked. Make sure FBR's record is right before you apply; our {a(B["proc"], "step-by-step guide")} covers the screens.</p>

<h2 id="both">FBR and PRA Are Two Registrations</h2>
<p>An FBR sales tax registration and a PRA registration are not the same thing. Rule 2(4) requires a separate Punjab registration for services rendered in Punjab by anyone working in more than one province, and FBR registration does not stand in for it. Our guide on {a(X["dual"], "when a business needs both FBR and provincial registration")} explains the split, and the {a(X["strn"], "FBR sales tax registration")} page covers the federal side.</p>
""",
    faqs=[
        ("What is P+NTN?", "Under rule 10 of the 2012 Rules, taxpayers already registered with FBR were registered with PRA automatically, with \"P\" as a prefix to their NTN."),
        ("Do I need to apply to PRA if I am registered with FBR?", "Rule 10 registered existing FBR taxpayers automatically. Check the Taxpayer Profile Inquiry first; apply only if you are not found."),
        ("How do I update an automatic PRA registration?", "Rule 11 says changes, including in rule 10 cases, are intimated on Form PST-01; PRA decides preferably within thirty days."),
        ("Does FBR sales tax registration cover my services in Punjab?", "No. PRA registration is separate; rule 2(4) requires a separate Punjab registration for services rendered in Punjab."),
        ("Why are my PRA details pre-filled from FBR?", "Form PST-01 authorises PRA to obtain your registration particulars from FBR, and the IRIS Basic Information screen fills from FBR's record."),
    ],
    sources=[S_RULES, S_LOGIN, S_ATL, S_MAN, S_PRA],
    related=[(SVC, "PRA registration service"), (B["ver"], "PRA verification"), (X["dual"], "FBR and provincial registration")],
)

CHG = post(
    slug=SL["chg"],
    title="PRA Registration Changes, Suspension and De-registration",
    h1="Changing, Suspending or Cancelling a PRA Registration: Sections 28-29 and Rules 5-14",
    crumb="PRA Changes and De-registration",
    description="Change PRA registration details, transfer it, deal with suspension, or de-register on Form PST-02: the Act's timelines and what happens to your invoices.",
    keywords="pra de-registration, pra registration cancellation, pra suspension, pra change of address, pra registration transfer, pst-02 form, pra deregistration form",
    read="11 min read",
    banner="A PRA registration does not end when you stop working. It ends when PRA de-registers you.",
    tldr=("Change of name, address or other particulars: Form PST-01, decided preferably within thirty days (rule 11). Transfer between PRA offices on "
          "application or by PRA (rule 12). Suspension: PRA may temporarily inactivate a registration, must give notice with reasons, may then suspend by "
          "removing the name from its list, and may withdraw the suspension within sixty days (section 28). De-registration: apply on Form PST-02 when you "
          "stop providing taxable services (rule 5); PRA decides within three months, extendable by up to sixty days (section 29(4)). Both are free (rule 15)."),
    lead=("Registration is the start of a record, not a one-time event. Businesses move, rename, add branches, get sold or close, and each of those has "
          "its own rule. This guide puts them in one place, with the timelines the Act and rules set."),
    answers={
        "change": "Report changes on Form PST-01 under rule 11; PRA approves or rejects, preferably within thirty days.",
        "transfer": "Shifting to another PRA office's area: apply for transfer with documents (rule 12(2)); PRA can also transfer on its own motion.",
        "suspend": "Notice first, then suspension by removing the name from the list; PRA may withdraw it within sixty days (section 28).",
        "dereg": "Apply on Form PST-02 when you stop taxable services (rule 5); decided within three months, extendable by sixty days (section 29(4)).",
        "sale": "Selling the business needs the Commissioner's prior permission (rule 14) and notice within one month of the sale (section 20).",
    },
    svc=svc("PRA Changes and De-registration, Handled",
            "Registration changes and closures are where old businesses get stuck. We file the right form, with the right evidence, and follow up.",
            ["Change of name, address, branch or services on Form PST-01",
             "Transfer of registration to the right PRA office",
             "Reply to a temporary inactivation or suspension notice",
             "De-registration on Form PST-02 with supporting documents"],
            ["A closed business left registered keeps its obligations",
             "Invoices issued while suspended do not give customers credit (rule 8)",
             "Selling without the Commissioner's permission breaches rule 14"],
            "Moving, renaming, selling or closing a PRA-registered business?", "Help with my PRA registration"),
    wa_text="Assalam o Alaikum, PRA registration mein change / de-registration karwani hai.",
    body=f"""
{SERIES("chg")}

<h2 id="change">Changing Your Particulars</h2>
<p>Rule 11 applies to "a change in the name, address or other particulars as stated in the registration certificate". You intimate the proposed change on Form PST-01, and PRA "may either approve or reject the request for change preferably within thirty days of the receipt of such intimation". Common changes:</p>
<ul>
<li>A new business address, or a new branch to add</li>
<li>A new service to add to the certificate (rule 2(3) lets one certificate list all services)</li>
<li>A new bank account, or one closed</li>
<li>A new email or mobile; Form PST-01's declaration accepts notices sent to them as legal notice</li>
</ul>

<h2 id="transfer">Transferring to Another PRA Office</h2>
<p>Rule 12 covers jurisdiction. If you shift your business activity from one PRA office's area to another, or have another valid reason, you apply for transfer "along with necessary documents, if any", and PRA decides after verification (rule 12(2)). PRA can also transfer a registration on its own motion, with notice to you (rule 12(3)).</p>

<h2 id="suspend">Inactivation and Suspension: Section 28</h2>
{table(["Stage", "What happens", "Section"], [
    ["Temporary inactivation", "If PRA is satisfied you are not entitled to registration or have not complied with the Act or rules", "28(1)"],
    ["Notice", "Reasons and the remedial action required, with a time limit", "28(2)"],
    ["Suspension", "If the response or action is not satisfactory, or no response arrives", "28(3)"],
    ["Removal from list", "Suspension is effected by removing the name from PRA's published list", "28(4)"],
    ["Within 60 days", "PRA may withdraw the suspension if satisfied with your remedial action", "28(5)"],
    ["After 60 days", "Proceedings, reinstatement, or cancellation", "28(6)"],
])}
<p>Rule 6 adds a separate route: for tax fraud, deliberate non-payment or short payment, or evasion, PRA may suspend and, after inquiry and a hearing, cancel. Section 28(7) and rule 9 make the same point: cancellation or suspension does not end your liabilities. Rule 8 says invoices issued during a suspension do not give tax credit, adjustment or refund, which your customers will notice. Check your status any time with the {a(B["ver"], "Taxpayer Profile Inquiry")}.</p>
<p>If a cancellation was based on a misunderstanding of the facts, rule 7 lets PRA revive it, on conditions and from a date it specifies.</p>

<h2 id="dereg">De-registration: Section 29 and Rule 5</h2>
<p>Rule 5: every registered person "who ceases to provide taxable service shall apply" for cancellation on <strong>Form PST-02</strong>. After any audit or enquiry, PRA de-registers from the date it specifies or the date outstanding tax is deposited, whichever is later. Form PST-02 lists the grounds:</p>
<ul>
<li>Ceased to carry on business</li>
<li>The service has become exempt</li>
<li>Taxable turnover in the last twelve months has stayed below the threshold (with the value and reasons)</li>
<li>Transfer or sale of the business, or merger (with proof)</li>
<li>Other, described</li>
</ul>
<p>Section 29(2) lets a person who believes he no longer meets section 25 apply; under section 29(3), PRA de-registers if satisfied he is not required to be registered and has met his obligations. Section 29(4) sets the timetable: PRA disposes of the application within <strong>three months</strong>, extendable by up to <strong>sixty days</strong> for recorded reasons. PRA may also de-register a person or class not required to be registered (section 29(1)). Rule 15 makes de-registration free.</p>

<h2 id="sale">Selling or Merging the Business</h2>
<p>Rule 14 requires the Commissioner's <strong>prior permission</strong> before a registered business is sold or disposed of, and the explanation says sale includes merger. The buyer must obtain a new registration or, if allowed, changes to the existing one (rule 14(2)). Section 20(1) of the Act separately requires the former owner to tell the Commissioner within one month of a sale or transfer as an ongoing concern, and section 20(2) makes the buyer liable for tax on the business's services and liable to registration.</p>

<h2 id="wrong">If You Were Registered by Mistake</h2>
<p>A wrong compulsory registration is not de-registered; it is cancelled ab initio under rule 13, with no tax liability for that period. See {a(B["comp"], "compulsory registration")}.</p>
""",
    faqs=[
        ("How do I change my address on PRA registration?", "Intimate the change on Form PST-01 under rule 11; PRA approves or rejects it, preferably within thirty days."),
        ("How long does PRA de-registration take?", "Section 29(4): PRA disposes of the application within three months, extendable by up to sixty days for recorded reasons."),
        ("Which form is used to cancel PRA registration?", "Form PST-02, under rule 5 of the Registration and De-registration Rules 2012. It is free under rule 15."),
        ("What happens if my PRA registration is suspended?", "Your name is removed from PRA's published list (s.28(4)); PRA may withdraw the suspension within sixty days if satisfied with your remedial action (s.28(5))."),
        ("Can I sell my PRA-registered business?", "Only with the Commissioner's prior permission (rule 14). The former owner must also inform the Commissioner within one month of the sale (section 20(1))."),
    ],
    sources=[S_ACT4, S_ACT3, S_RULES, S_LOGIN, S_PRA],
    related=[(SVC, "PRA registration service"), (B["ver"], "PRA verification"), (B["comp"], "Compulsory registration")],
)
