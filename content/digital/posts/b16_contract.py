import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=16,
    slug="website-development-contract-checklist",
    title="Website Development Contract Checklist for Pakistan",
    h1="Website Development Contract Checklist: 15 Clauses to Agree Before You Pay",
    crumb="Website Development Contract Checklist",
    description="A website development contract checklist for Pakistani businesses: 15 clauses covering scope, ownership, payments, delays, changes, handover and support.",
    keyword="website development contract",
    cluster=["web design agreement", "website contract template pakistan", "website development agreement clauses",
             "web developer contract checklist", "website project agreement"],
    category="Hiring a Developer",
    published="2026-10-28", published_h="28 October 2026",
    updated="2026-10-28", updated_h="28 October 2026",
    answer=("A website development contract should state the scope, price, payment milestones, timeline, revision rounds, ownership of the "
            "domain, hosting and code, licences, change requests, delays, testing, handover, support and how either side can end the "
            "project. A two-page agreement covering these points prevents most disputes. It does not need to be long."),
    takeaways=[
        "Agree the contract before paying any deposit.",
        "The ownership and handover clauses protect you most; never leave them out.",
        "A change-request clause stops scope creep from turning into arguments about money.",
        "Define what \"done\" means for each milestone, so payments are tied to visible work.",
        "Short and specific beats long and vague. This checklist is not legal advice; ask a lawyer for large projects.",
    ],
    body="""
<h2 id="why">Why a Website Development Contract Matters</h2>
<p>Most website disputes in Pakistan start with a WhatsApp conversation and no written agreement. Each side remembers the deal differently: how many pages, who writes the content, whether the shop needs online payments. A short website development contract fixes those points before money changes hands. It protects the developer too, because it defines when work is finished and payment is due.</p>

<h2 id="clauses">The 15 Clauses Your Contract Needs</h2>
<table>
<tr><th>Clause</th><th>What it should say</th></tr>
<tr><td>1. Parties</td><td>Full legal names, addresses and contact people for both sides</td></tr>
<tr><td>2. Scope</td><td>Every page and feature, plus a list of what is excluded</td></tr>
<tr><td>3. Platform</td><td>WordPress, Shopify or custom, and which theme or framework</td></tr>
<tr><td>4. Content</td><td>Who writes text and supplies images, and by which date</td></tr>
<tr><td>5. Price</td><td>Total price in PKR, and what could change it</td></tr>
<tr><td>6. Payment milestones</td><td>Amount due at each stage and the work delivered for it</td></tr>
<tr><td>7. Timeline</td><td>Dates for each milestone, including the client's review time</td></tr>
<tr><td>8. Revisions</td><td>Number of design and development revision rounds included</td></tr>
<tr><td>9. Change requests</td><td>How new requests are priced and approved in writing</td></tr>
<tr><td>10. Ownership</td><td>Domain, hosting, code, design and content belong to the client after final payment</td></tr>
<tr><td>11. Licences</td><td>Themes, plugins, fonts and images licensed in the client's name</td></tr>
<tr><td>12. Testing and acceptance</td><td>Devices and browsers tested, and how the client signs off</td></tr>
<tr><td>13. Handover</td><td>Logins, files, backups and documentation delivered at launch</td></tr>
<tr><td>14. Support and warranty</td><td>Bug-fix period after launch and paid support options</td></tr>
<tr><td>15. Ending the project</td><td>Notice period, payment for work done, and handover of work in progress</td></tr>
</table>

<h2 id="ownership-clause">The Ownership Clause in Detail</h2>
<p>This is the clause that matters most. It should say that once the final payment is made, the client owns the website's code, design and content, and that the domain and hosting are registered to the client from the start. Without it, some developers keep control of the domain or refuse to hand over files. Our guide to <a href="/digital/blog/who-owns-your-website">who owns your website</a> explains each part of ownership.</p>

<h2 id="change-clause">The Change-Request Clause in Detail</h2>
<p>New ideas appear during every project. A good clause says that anything outside the written scope is quoted separately, approved in writing (a WhatsApp message is enough if both sides agree) and added to the timeline. This keeps the project moving without arguments about whether an extra page was "included".</p>

<h2 id="delays">Delays on Either Side</h2>
<p>Projects are delayed by both developers and clients. A fair contract says what happens in each case: if the developer misses a milestone date without reason, the client may pause payment; if the client takes weeks to send content or feedback, the timeline moves by the same amount. Agree a maximum pause, for example 60 days, after which the project can be closed and paid up to the work completed.</p>

<h2 id="payments">Linking Payments to Visible Work</h2>
<p>Each payment should follow something you can see: an approved design, a working staging site, or the live launch. Our guide to <a href="/digital/blog/website-milestone-payments">milestone payments</a> shows a fair schedule, and the <a href="/digital/blog/website-handover-checklist">handover checklist</a> lists what you should receive at the end.</p>

<h2 id="language">Plain Language Is Fine</h2>
<p>A website agreement does not need legal jargon. Clear sentences in English or Urdu that both sides understand are better than a long template copied from the internet. For large projects, international clients or software with significant value, ask a lawyer to review the agreement. This checklist is general guidance, not legal advice.</p>
""",
    faqs=[
        ("What should a website development contract include?",
         "It should include both parties, the scope with exclusions, the platform, who supplies content, total price, payment milestones, timeline, revision rounds, change requests, ownership of the domain and code, licences, testing and acceptance, handover, support after launch and how either side can end the project fairly."),
        ("Do I need a contract for a small website?",
         "Yes, even a one-page agreement helps. Small projects cause disputes too, usually about pages, content, revisions or ownership of the domain. A short written agreement that both sides sign or confirm by email takes an hour to prepare and saves weeks of argument if expectations differ later."),
        ("Who owns the website code after the project?",
         "That depends on the contract, which is why the ownership clause matters. A fair agreement says the client owns the code, design and content once the final payment is made, and that the domain and hosting are in the client's name from the start. Without such a clause, ownership can be disputed."),
        ("Is a WhatsApp agreement valid for a website project?",
         "Written messages can show what was agreed, but a scattered chat is hard to rely on. It is better to put the scope, price, milestones and ownership in one short document, then confirm it by email or WhatsApp. For larger projects, ask a lawyer about signatures and enforceability."),
        ("What is a change request in a website project?",
         "A change request is any work outside the agreed scope, such as an extra page, a new feature or a different design direction. A good contract says change requests are quoted separately, approved in writing and added to the timeline, so the project stays fair to both the client and the developer."),
        ("Website banwane ka agreement kaisa hona chahiye?",
         "Agreement mein pages aur features ki list, total qeemat, milestone payments, timeline, revisions ki tadaad, aur yeh likha ho ke domain, hosting aur code aap ke naam par honge. Launch par saare logins aur files milne ki shart bhi likhein. Saada zubaan kaafi hai, lambe legal alfaaz zaroori nahi."),
    ],
    sources=[
        ("ICANN — Registrants' benefits and responsibilities", "https://www.icann.org/resources/pages/benefits-2013-09-16-en"),
        ("WIPO — Copyright (ownership of creative and software works)", "https://www.wipo.int/copyright/en/"),
        ("GitHub Docs — Transferring a repository", "https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository"),
        ("W3C — Web Content Accessibility Guidelines (WCAG) 2.2", "https://www.w3.org/TR/WCAG22/"),
    ],
    method=("The 15 clauses are drawn from the short written agreement we send before every project and from disputes clients describe when "
            "they come to us from other developers. Ownership guidance follows ICANN's registrant guidance and WIPO's copyright overview. "
            "This is general guidance, not legal advice."),
    related=["who-owns-your-website", "website-milestone-payments", "website-handover-checklist",
             "how-to-choose-web-development-company"],
    service_links=[("/digital/pricing", "Our terms and published prices"), ("/digital/contact", "Request a written scope")],
    cta="Want a clear written agreement for your website?",
    wa="Hi%2C%20I%20read%20your%20contract%20checklist%20and%20want%20a%20written%20scope",
)
