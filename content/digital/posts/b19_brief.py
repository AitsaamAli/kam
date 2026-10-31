import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=19,
    slug="website-brief-template",
    title="How to Write a Website Brief (Free Template)",
    h1="How to Write a Website Brief: Free Template and Worked Example",
    crumb="Website Brief Template",
    description="A free website brief template you can copy, with a worked example for a Lahore clinic. Write a clear brief in 30 minutes and get accurate, comparable quotes.",
    keyword="website brief template",
    cluster=["website requirements document", "how to write a website brief", "web design brief example",
             "website project brief", "website requirements checklist"],
    category="Hiring a Developer",
    published="2026-10-28", published_h="28 October 2026",
    updated="2026-10-28", updated_h="28 October 2026",
    answer=("A website brief template covers ten points: your business, goals, customers, pages, features, content, design preferences, "
            "examples you like, budget and deadline. Filling it in takes about 30 minutes, and sending the same brief to every developer "
            "gives you accurate quotes you can compare fairly. Copy the template below."),
    takeaways=[
        "A brief is one or two pages, not a technical specification.",
        "Goals and customers matter more than colours and fonts.",
        "Listing features precisely is what makes quotes comparable.",
        "Share your budget range; it helps developers suggest the right scope.",
        "Send the identical brief to every developer you approach.",
    ],
    body="""
<h2 id="why">Why Write a Website Brief?</h2>
<p>Without a brief, every developer guesses what you need, and their quotes describe different projects. With a brief, quotes become comparable, timelines become realistic, and the first design is much closer to what you want. A brief is not technical: it describes your business and what the website must do, in your own words.</p>

<h2 id="template">Website Brief Template: Copy and Fill In</h2>
<div class="answer-box"><div class="lbl">Template</div>
<ol>
<li><strong>Business:</strong> name, what you sell, where you operate, years in business.</li>
<li><strong>Goal:</strong> what the website must achieve, such as enquiries, bookings, online orders or credibility with overseas buyers.</li>
<li><strong>Customers:</strong> who they are, what they search for, and which device they mostly use.</li>
<li><strong>Pages:</strong> the list of pages you expect, for example Home, About, Services (one per service), Contact.</li>
<li><strong>Features:</strong> WhatsApp button, contact form, booking, online payments, cash on delivery, courier booking, Urdu version, blog.</li>
<li><strong>Content:</strong> who writes the text and who supplies photos, and whether you have a logo.</li>
<li><strong>Design:</strong> brand colours, tone (formal, friendly, premium), anything you dislike.</li>
<li><strong>Examples:</strong> two or three websites you like, and what exactly you like about each.</li>
<li><strong>Budget:</strong> a range, for example Rs 40,000 to Rs 90,000.</li>
<li><strong>Deadline:</strong> launch date and the reason for it, such as a product launch or season.</li>
</ol>
</div>
<p>Copy the ten points into WhatsApp, email or a document and fill in a few lines for each.</p>

<h2 id="example">Worked Example: A Lahore Dental Clinic</h2>
<table>
<tr><th>Point</th><th>Example answer</th></tr>
<tr><td>Business</td><td>Two-dentist clinic in Johar Town, Lahore, open since 2015</td></tr>
<tr><td>Goal</td><td>More appointment requests from new patients through Google and WhatsApp</td></tr>
<tr><td>Customers</td><td>Families and working adults nearby; 80% visit on mobile phones</td></tr>
<tr><td>Pages</td><td>Home, About the dentists, 6 treatment pages, Prices, Contact</td></tr>
<tr><td>Features</td><td>WhatsApp button, appointment request form, Google Map, patient reviews</td></tr>
<tr><td>Content</td><td>We supply photos; we need help writing treatment pages</td></tr>
<tr><td>Design</td><td>Clean, calm and trustworthy; blue and white; no stock photos of models</td></tr>
<tr><td>Examples</td><td>Two clinic sites we like for their clear prices and booking button</td></tr>
<tr><td>Budget</td><td>Rs 60,000 to Rs 100,000</td></tr>
<tr><td>Deadline</td><td>Live within six weeks, before our second branch opens</td></tr>
</table>

<h2 id="mistakes">Which Brief Mistakes Cost the Most?</h2>
<ul>
<li><strong>Describing the look, not the goal.</strong> "Modern and attractive" tells a developer less than "more bookings from mobile visitors".</li>
<li><strong>Leaving out features.</strong> Online payments, Urdu pages or courier integration change the price significantly; mention them early.</li>
<li><strong>Hiding the budget.</strong> A range helps developers propose a sensible scope instead of guessing.</li>
<li><strong>Forgetting content.</strong> Content is the most common cause of delays. Say who writes it.</li>
<li><strong>Sending different briefs to different developers,</strong> which makes quotes impossible to compare.</li>
</ul>

<h2 id="apps">Briefs for Web Applications</h2>
<p>For a portal, booking system or marketplace, add three more points: the types of users (customer, staff, admin), the main tasks each user must complete, and any software it must connect to. Writing each task as a short user story, such as "as a patient, I want to book an appointment so that I do not have to call", helps developers estimate accurately. Our <a href="/digital/blog/web-app-development-cost-in-pakistan">web app cost guide</a> explains how scope affects budget.</p>

<h2 id="next">What Should You Do After Writing the Brief?</h2>
<p>Send it to three or four developers along with our <a href="/digital/blog/how-to-choose-web-development-company">20 questions</a>, then compare the replies using our guide on <a href="/digital/blog/why-website-quotes-vary">why website quotes vary</a>. If you would like, send the brief to us on WhatsApp and we will reply with a written scope and fixed price within one business day.</p>
<p>Finished your brief? Send it through our <a href="/digital/contact">quote page</a> for a written scope and fixed price.</p>
""",
    faqs=[
        ("What should a website brief include?",
         "A website brief should include your business background, the goal of the website, your customers, the pages you expect, the features you need, who supplies the content, design preferences, two or three example websites you like, a budget range and a deadline. One or two pages covering these points is enough for most projects."),
        ("How long should a website brief be?",
         "For most business websites and online stores, one or two pages is enough. The aim is to describe your goals and needs clearly, not to write a technical specification. Web applications need a little more detail, such as user types, main tasks and integrations, but should still be readable in a few minutes."),
        ("Should I tell developers my budget?",
         "Yes, share a range. It helps developers propose a scope that fits, rather than guessing high or low. A range also makes it easier to compare quotes, because each developer explains what they can deliver for that amount. You can still negotiate once you see the written scope and price."),
        ("What is the difference between a brief and a requirements document?",
         "A brief describes your business, goals and needs in plain language so developers can quote. A requirements document, usually written with the developer after you choose one, lists every page, feature and rule in detail and becomes part of the agreement. The brief comes first; the requirements follow."),
        ("Website brief Urdu mein likh sakte hain?",
         "Ji haan. Brief kisi bhi zubaan mein ho sakta hai, zaroori yeh hai ke saaf ho. Apna kaarobar, website ka maqsad, customers, pages, features, content kaun likhega, pasand ki websites, budget aur deadline likh dein. Yahi brief har developer ko bhejein taake qeematon ka muqabla aasaan ho."),
        ("Can a developer help me write the brief?",
         "Yes. Many developers will ask questions on a call and turn your answers into a brief or written scope. It still helps to prepare the ten points yourself first, because you know your business and customers best, and the same brief lets you compare several developers fairly."),
    ],
    sources=[
        ("Agile Alliance — User stories", "https://www.agilealliance.org/glossary/user-stories/"),
        ("Nielsen Norman Group — Usability 101", "https://www.nngroup.com/articles/usability-101-introduction-to-usability/"),
        ("GOV.UK Service Manual — Agile delivery", "https://www.gov.uk/service-manual/agile-delivery"),
        ("W3C — Web Content Accessibility Guidelines (WCAG) 2.2", "https://www.w3.org/TR/WCAG22/"),
    ],
    method=("The template reflects the questions we ask on every first call, condensed into ten points. The dental clinic example is "
            "illustrative and not a real client. User-story guidance follows the Agile Alliance glossary; the focus on goals and users "
            "follows Nielsen Norman Group's usability principles."),
    related=["how-to-choose-web-development-company", "why-website-quotes-vary", "website-price-in-pakistan",
             "website-development-contract-checklist"],
    service_links=[("/digital/contact", "Send us your brief"), ("/digital/pricing", "Our published prices")],
    cta="Written your brief?",
    wa="Hi%2C%20I%20used%20your%20website%20brief%20template%20and%20want%20a%20quote",
)
