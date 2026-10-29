import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=97,
    slug="how-long-to-build-a-website",
    title="How Long Does It Take to Build a Website? Real Timelines",
    h1="How Long to Build a Website? Realistic Timelines by Website Type and What Delays Projects",
    crumb="How Long to Build a Website",
    description="How long to build a website: realistic timelines for landing pages, small sites, business sites, online stores and web apps, plus the delays that add weeks.",
    keyword="how long to build a website",
    cluster=["website development time", "website kitne din mein banti hai", "website project timeline",
             "online store build time", "web app development timeline", "why website projects get delayed"],
    category="Planning & Launch",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("How long to build a website depends on its type: about 1 week for a landing page, 2 to 3 weeks for a 5-page site, 3 to 5 "
            "weeks for a 10-page business site, 4 to 8 weeks for an online store and 6 weeks or more for a web app. Missing content and "
            "slow feedback cause most delays."),
    takeaways=[
        "Typical timelines run from about a week for a landing page to several months for a large web app.",
        "The build itself is rarely the slowest part; content, photos and approvals usually are.",
        "Online stores take longer because of product entry, payments and courier set-up.",
        "A written scope with milestones and dates makes the timeline visible to both sides.",
        "You can speed things up by preparing content early and naming one person to approve work.",
    ],
    body=f"""
<h2 id="timelines">How Long Does It Take to Build a Website?</h2>
<p>The honest answer is that it depends on what you are building and how quickly content and decisions arrive. The table below shows typical timelines for our packages, from a signed scope to launch, assuming content is ready and feedback comes within two working days.</p>
<table>
<tr><th>Website type</th><th>Our starting price</th><th>Typical timeline</th><th>Main time drivers</th></tr>
<tr><td>Landing page</td><td class="price">{P['landing']}</td><td>About 1 week</td><td>Copy, one design round, form set-up</td></tr>
<tr><td>Small website, up to 5 pages</td><td class="price">{P['starter']}</td><td>2 to 3 weeks</td><td>Content, photos, design approval</td></tr>
<tr><td>Business website, up to 10 pages</td><td class="price">{P['business']}</td><td>3 to 5 weeks</td><td>More pages, more approvals</td></tr>
<tr><td>Online store</td><td class="price">{P['store']}</td><td>4 to 8 weeks</td><td>Product entry, payments, couriers, testing</td></tr>
<tr><td>Web application</td><td class="price">From {P['app']}</td><td>6 weeks to several months</td><td>Features, user roles, integrations</td></tr>
</table>
<p>These are typical ranges from our projects, not guarantees; your written scope gives your actual dates.</p>

<h2 id="stages">What Are the Stages of a Website Project?</h2>
<ol>
<li><strong>Brief and scope:</strong> a few days to agree pages, features, price and dates in writing.</li>
<li><strong>Design:</strong> home page and key templates, with one or two rounds of changes.</li>
<li><strong>Build:</strong> pages, forms, integrations and content entry on a staging site.</li>
<li><strong>Content and testing:</strong> your review, fixes, phone testing and final checks.</li>
<li><strong>Launch:</strong> going live, redirects if replacing an old site, and handover.</li>
</ol>

<h2 id="example-week">What Does a Four-Week Business Website Look Like?</h2>
<p>Example only, for a 10-page site with content ready. In week one, the scope is signed, the brief is reviewed and the home page design is shared. In week two, inner page designs are approved and building starts on a staging site. In week three, all pages are built, forms connected and content entered, and the client reviews everything on a phone. In week four, fixes are made, speed and SEO basics are checked, the site goes live and logins are handed over. Each week ends with something the client can see and approve, which keeps the project moving.</p>

<h2 id="delays">What Delays Website Projects?</h2>
<table>
<tr><th>Delay</th><th>How it shows up</th><th>How to avoid it</th></tr>
<tr><td>Missing content</td><td>Pages wait for text, photos or prices</td><td>Prepare content before design starts</td></tr>
<tr><td>Slow feedback</td><td>Designs sit unapproved for weeks</td><td>Name one decision-maker; agree reply times</td></tr>
<tr><td>Scope changes</td><td>New features added mid-build</td><td>Keep a "phase two" list; use change requests</td></tr>
<tr><td>Third-party approvals</td><td>Payment gateways, Business Profile or app stores</td><td>Apply early, in parallel with design</td></tr>
<tr><td>Domain and hosting access</td><td>Old developer holds the logins</td><td>Recover access before the project starts</td></tr>
<tr><td>Many decision-makers</td><td>Conflicting feedback from partners</td><td>Consolidate feedback into one list per round</td></tr>
</table>
<p>Payment gateway approvals in particular can take longer than the website build; our <a href="/digital/blog/payment-gateways-pakistan-compared">payment gateway comparison</a> explains why to apply early.</p>

<h2 id="speed-up">How Can You Speed Up Your Project?</h2>
<ul>
<li>Write a short brief using our <a href="/digital/blog/website-brief-template">website brief template</a>.</li>
<li>Collect text, photos, logo files and prices before the design stage.</li>
<li>Choose one person to approve work and reply within two working days.</li>
<li>Start any gateway, courier or Google Business Profile applications on day one.</li>
<li>Launch the core pages first and add extras in a second phase.</li>
</ul>

<h2 id="fast-quotes">Should You Trust a "Website in 3 Days" Offer?</h2>
<p>A simple template site with your logo swapped in can be put online in days, and sometimes that is all a business needs. But a quote that promises a full custom site, store or app in a few days usually means skipped steps: no proper content, no testing on phones, no backups or security set-up. Ask what is included, and compare the scope, not only the date.</p>

<h2 id="our-process">How We Plan Timelines</h2>
<p>Every project starts with a written scope that includes milestones and target dates, agreed before any deposit. Payments are tied to milestones, so progress is visible. See our <a href="/digital/pricing">prices and packages</a>, the <a href="/digital/blog/wordpress-vs-shopify-vs-custom-website">platform comparison pillar</a> and our <a href="/digital/blog/website-launch-checklist">website launch checklist</a>.</p>
""",
    faqs=[
        ("How long does it take to build a small business website?",
         "With content ready and quick feedback, a website of up to 5 pages typically takes 2 to 3 weeks with us, and a business website of up to 10 pages 3 to 5 weeks. Missing text and photos or slow approvals are the most common reasons projects take longer."),
        ("How long does it take to build an online store?",
         "Typically 4 to 8 weeks. Store projects take longer than ordinary websites because products, sizes and photos must be entered, and payments, delivery charges and couriers set up and tested. Payment gateway approvals can take longer than the build itself, so apply early."),
        ("How long does a web application take to develop?",
         "A focused first version of a web app often takes six weeks or more, while larger systems with several user roles and integrations take several months. Building in phases, starting with the core workflow, gets a usable version live sooner and lets real use guide the next phase."),
        ("Why do website projects get delayed?",
         "Most delays come from the client side rather than coding: missing content and photos, slow or conflicting feedback, new features added mid-project, and third-party approvals such as payment gateways. Preparing content early and naming one decision-maker prevents most of them."),
        ("Can a website be built in 3 days?",
         "A simple template site can go online in days if content is ready and little customisation is needed. A full custom site, store or web app in a few days usually means skipped steps, such as phone testing, security and backups. Compare what each quote includes, not only the deadline."),
        ("Website kitne din mein banti hai?",
         "Landing page taqreeban aik hafte mein, 5 page website 2 se 3 hafton mein, 10 page business website 3 se 5 hafton mein aur online store 4 se 8 hafton mein banta hai. Web app mein 6 hafte ya us se zyada lagte hain. Sab se zyada der text, tasveeron aur approval mein hoti hai."),
    ],
    sources=[
        ("GOV.UK Service Manual — Agile delivery", "https://www.gov.uk/service-manual/agile-delivery"),
        ("Agile Alliance — Minimum viable product (MVP)", "https://www.agilealliance.org/glossary/mvp/"),
        ("Google Business Profile Help — Verify your business", "https://support.google.com/business/answer/7107242"),
        ("Shopify — Pricing", "https://www.shopify.com/pricing"),
        ("WordPress Developer Resources — WordPress backups", "https://developer.wordpress.org/advanced-administration/security/backup/"),
    ],
    method=("Timelines are typical ranges from our own projects for our published packages, assuming ready content and feedback within two "
            "working days; they are not guarantees. Phased delivery follows GOV.UK and Agile Alliance practice. Prices are our own "
            "published packages, checked against our price list on 29 October 2026."),
    related=["wordpress-vs-shopify-vs-custom-website", "pages-for-small-business-website", "website-launch-checklist",
             "website-brief-template"],
    service_links=[("/digital/pricing", "Prices and timelines"), ("/digital/contact", "Get a scope with dates")],
    cta="Need your website by a certain date?",
    wa="Hi%2C%20I%20read%20your%20website%20timeline%20guide%20and%20need%20a%20quote%20with%20dates",
)
