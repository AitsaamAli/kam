import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=75,
    slug="outsourcing-website-ip-nda-code-ownership",
    title="Outsourcing Contract IP Ownership: NDA and Code Rights",
    h1="Outsourcing Contract IP Ownership: NDAs, Code Rights and Clauses Explained in Plain English",
    crumb="IP, NDA and Code Ownership",
    description="Outsourcing contract IP ownership explained: what an NDA covers, assignment and licence clauses, open-source parts, and keeping control of code and accounts.",
    keyword="outsourcing contract ip ownership",
    cluster=["nda for software development", "who owns code outsourcing", "ip assignment clause", "source code ownership",
             "open source licence in client project", "confidentiality agreement developer"],
    category="Working With Overseas Clients",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("In an outsourcing contract, IP ownership should be settled in writing before work starts: an NDA for confidentiality, an "
            "assignment clause transferring code and design to you after final payment, and a list of third-party and open-source parts "
            "you only license. Keep the repository, domain and hosting in your name from day 1. This is not legal advice."),
    takeaways=[
        "Copyright in code and design generally starts with whoever creates it, so ownership must be transferred in writing.",
        "An NDA protects confidential information; it does not by itself transfer ownership of the work.",
        "An assignment clause transfers rights in the custom work, usually on final payment.",
        "Themes, plugins, libraries and fonts are licensed, not owned; the contract should list them.",
        "Control of the repository, domain and hosting matters as much as the words in the contract.",
    ],
    body=f"""
<h2 id="why-it-matters">Why Does Outsourcing Contract IP Ownership Matter?</h2>
<p>When you outsource a website or app, you are paying someone else to create code, designs and sometimes content. WIPO describes copyright as the rights creators have over their works, and it lists computer programs among the works commonly protected. In many countries, the creator holds those rights by default unless an agreement transfers them. Without clear terms, you may have paid for a website you cannot freely change, move or resell.</p>
<p>We are web developers, not lawyers. This guide explains the common clauses in plain English so you can discuss them with your lawyer. Laws differ by country, so take legal advice on the final wording.</p>

<h2 id="clauses">Which Clauses Should Your Contract Include?</h2>
<table>
<tr><th>Clause</th><th>Plain-English meaning</th><th>Example wording idea</th></tr>
<tr><td>Confidentiality (NDA)</td><td>The developer keeps your business information secret</td><td>"Supplier will not disclose Client's confidential information to anyone"</td></tr>
<tr><td>Assignment of rights</td><td>Ownership of custom code and design passes to you</td><td>"On final payment, Supplier assigns all rights in the Deliverables to Client"</td></tr>
<tr><td>Third-party components</td><td>Licensed parts stay under their own licences</td><td>"Third-party and open-source components are listed in Schedule B"</td></tr>
<tr><td>Supplier's pre-existing tools</td><td>The developer may reuse its own general tools, licensed to you</td><td>"Supplier grants Client a perpetual licence to use pre-existing tools in the Deliverables"</td></tr>
<tr><td>Moral rights and credits</td><td>No credits or claims to the work unless agreed</td><td>"Supplier will not add credits or links without Client's consent"</td></tr>
<tr><td>Handover</td><td>What you receive at the end</td><td>"Supplier delivers source code, database, documentation and credentials"</td></tr>
</table>
<p>The wording ideas show the intent only. Have a lawyer draft the actual clauses for your jurisdiction.</p>

<h2 id="nda-vs-assignment">Is an NDA Enough?</h2>
<p>No. A non-disclosure agreement stops the developer sharing your information, such as your business plans, customer data or unreleased designs. It does not usually transfer ownership of what they build. You need both: an NDA from the first conversation in which you share sensitive material, and an assignment or ownership clause in the main contract.</p>

<h2 id="open-source">What About Open-Source and Third-Party Parts?</h2>
<p>Almost every website uses parts the developer did not write: WordPress itself, themes, plugins, JavaScript libraries, fonts and icons. These are licensed, not owned. Some open-source licences require you to keep notices or share changes in certain cases; paid themes and plugins usually allow use on a set number of sites. Ask for a list of every significant component with its licence, and make sure paid licences are bought in your name.</p>

<h2 id="control">Why Is Control as Important as the Contract?</h2>
<p>A perfect clause helps little if the developer holds the keys. From day one, keep these in your own name and add the developer as a user:</p>
<ul>
<li>the code repository, such as a GitHub or GitLab organisation you own</li>
<li>the domain name, registered with your details</li>
<li>hosting and server accounts, billed to you</li>
<li>admin logins, analytics, Search Console and app store accounts</li>
</ul>
<p>Our guide on <a href="/digital/blog/who-owns-your-website">who owns your website</a> covers each account in detail.</p>

<h2 id="disputes">What If a Developer Refuses to Hand Over Code?</h2>
<p>Prevention is far easier than cure. If you control the repository and hosting, the code is already yours to use. If not, ask in writing with reference to the contract and payments made, request the repository transfer or a full backup, and seek legal advice for serious disputes. Milestone payments tied to delivered code reduce how much is at stake at any point.</p>

<h2 id="our-terms">What Are Our Own Terms?</h2>
<p>Our standard terms keep things simple: we sign an NDA before receiving confidential material, the domain and hosting are registered in the client's name, the client owns the custom code and design after final payment, third-party licences are bought in the client's name and listed at handover, and we add no credits without permission. Projects start from {P['starter']} for websites and {P['app']} for web applications. See our <a href="/digital/contact">contact page</a>, our <a href="/digital/blog/website-development-contract-checklist">website contract checklist</a> and the <a href="/digital/blog/hire-pakistani-web-developers">guide to hiring Pakistani developers</a>.</p>
""",
    faqs=[
        ("Who owns the code when I outsource website development?",
         "It depends on the contract. Copyright generally starts with whoever creates the work, so unless an agreement transfers the rights, the developer may keep them. A clear assignment clause, usually effective on final payment, transfers ownership of the custom code and design to you. Take legal advice for your country."),
        ("Does an NDA give me ownership of the code?",
         "Usually not. A non-disclosure agreement keeps your confidential information private, but it does not normally transfer ownership of the work. You need a separate assignment or ownership clause in the main development contract, as well as an NDA covering the information you share."),
        ("What is an IP assignment clause?",
         "It is a contract clause by which the developer transfers their rights in the custom work, such as code, designs and content, to the client, often once the final payment is made. It should be clear about which deliverables are covered and which third-party or pre-existing parts are only licensed."),
        ("Can a developer reuse code from my project?",
         "Developers often reuse their own general tools and techniques across projects, which is normal. Your contract should give you a licence to any such pre-existing tools used in your project, assign the custom work to you, and stop the developer reusing your confidential business logic or designs elsewhere."),
        ("How do open-source licences affect ownership of my website?",
         "Open-source parts such as WordPress, libraries and plugins stay under their own licences; you use them, but you do not own them. Some licences require keeping notices or sharing changes in certain cases. Ask your developer for a list of components and licences at handover."),
        ("How can I protect my IP when outsourcing to another country?",
         "Sign an NDA before sharing sensitive material, include an assignment clause in the main contract, list third-party components, and keep the code repository, domain, hosting and admin accounts in your own name from day one. Pay in milestones tied to delivered code, and take legal advice in your jurisdiction."),
    ],
    sources=[
        ("WIPO — Copyright (rights of creators, includes computer programs)", "https://www.wipo.int/copyright/en/"),
        ("ICANN — Registrants' benefits and responsibilities", "https://www.icann.org/resources/pages/benefits-2013-09-16-en"),
        ("WordPress.org — Roles and capabilities", "https://wordpress.org/documentation/article/roles-and-capabilities/"),
        ("Google Search Console Help — Manage owners, users and permissions", "https://support.google.com/webmasters/answer/7687615"),
        ("Google Analytics Help — Add, edit and delete users", "https://support.google.com/analytics/answer/9305788"),
    ],
    method=("Copyright points follow WIPO's overview, checked 29 October 2026; account control follows ICANN and Google help pages. The "
            "clause table gives plain-English intent and wording ideas only and is not legal advice. Our own terms are approved business "
            "facts. Prices are our own published packages."),
    related=["hire-pakistani-web-developers", "white-label-web-development-pakistan", "who-owns-your-website",
             "website-development-contract-checklist", "pay-web-developer-in-pakistan"],
    service_links=[("/digital/contact", "Ask for our standard terms"), ("/digital/web-app-development", "Web apps you fully own")],
    cta="Want clear ownership terms from day one?",
    wa="Hi%2C%20I%20read%20your%20IP%20and%20code%20ownership%20guide%20and%20need%20a%20quote",
)
