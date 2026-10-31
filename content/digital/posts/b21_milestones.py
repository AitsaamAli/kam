import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=21,
    slug="website-milestone-payments",
    title="Website Advance Payment: A Fair Milestone Payment Plan",
    h1="Website Advance Payment and Milestones: How a Fair Payment Plan Works",
    crumb="Website Milestone Payments",
    description="How milestone payments for websites work: fair advance payment percentages, what you should see before each payment, and example schedules in PKR.",
    keyword="website advance payment",
    cluster=["milestone payment web project", "website payment terms", "website development payment schedule",
             "web developer advance payment", "how much advance for website"],
    category="Hiring a Developer",
    published="2026-10-28", published_h="28 October 2026",
    updated="2026-10-28", updated_h="28 October 2026",
    answer=("A fair website advance payment is usually 30 to 50 percent, followed by a mid-project payment after you approve the design or "
            "see a working staging site, and the balance on launch. Each payment should follow work you can see. Paying 100 percent "
            "upfront removes your leverage; paying nothing until the end is unfair to the developer."),
    takeaways=[
        "Milestones protect both sides: the developer is paid for progress, and you pay only for work you can see.",
        "A 30 to 50 percent advance is common; larger advances need a good reason.",
        "Define each milestone as a visible result, such as an approved design or a working staging site.",
        "Hold the final payment until the site is live and handed over.",
        "Keep receipts and confirmations of every payment and approval.",
    ],
    body=f"""
<h2 id="how-it-works">How Website Advance Payment and Milestones Work</h2>
<p>A milestone payment plan splits the price into stages. You pay an advance to start, then further payments as visible work is delivered and approved. The developer has income to cover early work, and you keep leverage until the project is finished. It is the standard structure for fixed-price website projects, and it is how we work on every project.</p>

<h2 id="schedules">Example Payment Schedules in PKR</h2>
<table>
<tr><th>Project</th><th>Advance</th><th>Mid-project</th><th>On launch</th></tr>
<tr><td>Small website, {P['starter']}</td><td>40% after scope approval</td><td>30% after design approval</td><td>30% after launch and handover</td></tr>
<tr><td>Business website, {P['business']}</td><td>40% after scope approval</td><td>30% when staging site is ready</td><td>30% after launch and handover</td></tr>
<tr><td>Online store, {P['store']}</td><td>30% after scope approval</td><td>40% when the store works on staging with test orders</td><td>30% after launch and handover</td></tr>
<tr><td>Web application, from {P['app']}</td><td colspan="3">Usually four or more milestones, each tied to a working feature set</td></tr>
</table>
<p>The percentages are examples. What matters is that each payment follows something you can see and test.</p>

<h2 id="visible-work">What Should You See Before Each Payment?</h2>
<table>
<tr><th>Milestone</th><th>Evidence before paying</th></tr>
<tr><td>Advance</td><td>A written scope, price, timeline and agreement</td></tr>
<tr><td>Design approval</td><td>Homepage and key page designs on desktop and mobile</td></tr>
<tr><td>Staging site</td><td>A working site on a test address that you can click through on your phone</td></tr>
<tr><td>Launch</td><td>The live site, plus all logins, files and documentation</td></tr>
</table>

<h2 id="upfront">Why Not Pay 100% Upfront?</h2>
<p>Full payment upfront removes your only leverage. If the developer becomes slow, changes priorities or disappears, you have no simple way to recover the money or the work. Some developers offer a discount for full payment; the discount rarely outweighs the risk. Our <a href="/digital/blog/how-to-choose-web-development-company">guide to choosing a developer</a> lists this as one of the main red flags.</p>

<h2 id="fair-to-developer">Why Not Pay Everything at the End?</h2>
<p>Asking a developer to work for weeks with no payment is unfair and attracts only those who need work urgently. It also creates pressure to cut corners. A reasonable advance shows commitment and allows the developer to plan the work properly.</p>

<h2 id="disputes">What If You Disagree at a Milestone?</h2>
<ul>
<li><strong>Compare the work with the written scope,</strong> not with new ideas added since.</li>
<li><strong>List specific issues in writing</strong> and agree a date to fix them.</li>
<li><strong>Pay for what has been delivered</strong> if the project must stop, and request the work in progress.</li>
<li><strong>Use the agreement's ending clause,</strong> as described in our <a href="/digital/blog/website-development-contract-checklist">contract checklist</a>.</li>
</ul>

<h2 id="overseas">Payments for Overseas Clients</h2>
<p>For clients in the UK, the Gulf and elsewhere, we invoice in Pakistani rupees and receive payment by international bank transfer, using the same milestone schedule. The written quote states the exact amount for each milestone before the advance is paid. Read our <a href="/digital/blog/website-handover-checklist">handover checklist</a> to know what to request before the final payment.</p>
<p>Our standard milestone terms sit alongside every package on the <a href="/digital/pricing">website prices page</a>.</p>
""",
    faqs=[
        ("How much advance payment should I give for a website?",
         "A 30 to 50 percent advance is common for website projects in Pakistan, paid after you approve a written scope, price and timeline. The rest is usually split between a mid-project payment after design approval or a working staging site, and a final payment after launch and handover of all logins and files."),
        ("Is it safe to pay a web developer 100% upfront?",
         "It is risky. Full payment upfront leaves you with no leverage if the project slows down or the developer stops replying, and recovering money is difficult. A milestone plan, where each payment follows visible work, protects you while still paying the developer fairly for progress made at each stage."),
        ("What is a milestone payment in a website project?",
         "A milestone payment is a part of the total price paid when a defined stage is completed and approved, such as an approved design, a working staging site or the live launch. Milestones tie money to visible progress, so both the client and the developer know exactly when each payment is due."),
        ("When should I make the final website payment?",
         "Make the final payment once the site is live, tested and handed over: you should have the domain, hosting and admin logins in your name, a full backup and any documentation. Agree this in writing at the start, so the final payment is linked to handover and not just to the site going live."),
        ("Website ke liye kitna advance dena chahiye?",
         "Aam tor par 30 se 50 feesad advance diya jata hai, likhit scope aur qeemat tay hone ke baad. Baqi raqam design manzoor hone ya test website dekhne ke baad, aur aakhri qist launch aur saare logins milne par di jati hai. Poori raqam pehle dena mehfooz nahi."),
        ("What happens to my advance if the project is cancelled?",
         "That depends on your agreement, which is why it should include an ending clause. A fair approach is that the developer keeps payment for work already completed and hands over that work, while any unused portion is refunded or credited. Agree these terms in writing before paying the advance."),
    ],
    sources=[
        ("GOV.UK Service Manual — Agile delivery (staged delivery and review)", "https://www.gov.uk/service-manual/agile-delivery"),
        ("Google Search Central — Do you need an SEO? (agreeing work with web professionals)", "https://developers.google.com/search/docs/fundamentals/do-i-need-seo"),
        ("ICANN — Registrants' benefits and responsibilities", "https://www.icann.org/resources/pages/benefits-2013-09-16-en"),
    ],
    method=("The schedules reflect our own milestone structure, published on our pricing page, applied to our published prices. Advice on "
            "staged review follows the GOV.UK Service Manual. The percentages are examples; your agreement sets the actual amounts."),
    related=["website-development-contract-checklist", "fixed-price-vs-hourly-web-development", "website-handover-checklist",
             "how-to-choose-web-development-company"],
    service_links=[("/digital/pricing", "Our prices and milestone terms"), ("/digital/contact", "Get a written payment plan")],
    cta="Want a clear payment plan for your website?",
    wa="Hi%2C%20I%20read%20your%20milestone%20payments%20guide%20and%20want%20a%20quote",
)
