import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=98,
    slug="pages-for-small-business-website",
    title="Pages for a Business Website: What a Small Business Needs",
    h1="What Pages Does a Small Business Website Need? Page Lists by Industry and What Each Must Say",
    crumb="Pages for a Business Website",
    description="Which pages for a business website do you need? Core pages every site needs, page lists for clinics, shops, consultants and manufacturers, and what each must say.",
    keyword="pages for business website",
    cluster=["business website pages list", "website sitemap example", "essential website pages", "about us page content",
             "website mein kaun se pages hon", "how many pages should a website have"],
    category="Planning & Launch",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=(f"Most small business websites need 5 core pages: home, services or products, about, contact, and a privacy policy. Then add "
            f"pages by industry, such as doctor profiles for a clinic or product categories for a manufacturer. A 5-page site starts from "
            f"{P['starter']}; most growing businesses need up to 10 pages, from {P['business']}."),
    takeaways=[
        "Every business website needs a home page, services or products, about, contact and a privacy policy.",
        "Give each main service or product line its own page, so customers and search engines find it.",
        "Industry needs differ: clinics need doctor profiles, shops need delivery and returns pages, manufacturers need catalogues.",
        "Each page should answer one set of customer questions and end with a clear next step.",
        "Start with the pages customers need now; add guides and extras once the core is strong.",
    ],
    body=f"""
<h2 id="core-pages">Which Pages for a Business Website Are Essential?</h2>
<p>Before choosing pages, think about what a customer needs to know to contact or buy from you. Almost every small business website answers the same five questions: what do you offer, who are you, can I trust you, how much, and how do I reach you? Those questions map to a small set of core pages.</p>
<table>
<tr><th>Core page</th><th>What it must contain</th></tr>
<tr><td>Home</td><td>What you do, for whom, where; main services; trust signals; call and WhatsApp buttons</td></tr>
<tr><td>Services or products</td><td>What each includes, who it suits, price or starting price, next step</td></tr>
<tr><td>About</td><td>Your story, team, experience, premises photos, registrations you genuinely hold</td></tr>
<tr><td>Contact</td><td>Address, map, hours, phone, WhatsApp, email and a short form</td></tr>
<tr><td>Privacy policy</td><td>What data you collect through forms and analytics, and how you use it</td></tr>
</table>

<h2 id="by-industry">Which Pages Does Each Industry Need?</h2>
<table>
<tr><th>Business</th><th>Pages to add</th><th>Typical total</th></tr>
<tr><td>Clinic</td><td>Doctor profiles, one page per service or speciality, timings and fees, booking</td><td>8 to 10</td></tr>
<tr><td>Shop or online store</td><td>Categories, products, delivery, returns and exchange, FAQs</td><td>Store package</td></tr>
<tr><td>Consultant or agency</td><td>One page per service, case examples with permission, process, FAQs</td><td>6 to 10</td></tr>
<tr><td>Manufacturer or exporter</td><td>Product categories, capabilities, quality and certifications, RFQ</td><td>8 to 10 or more</td></tr>
<tr><td>Restaurant</td><td>Menu, branches, ordering or reservations, catering</td><td>5 to 8</td></tr>
<tr><td>School or academy</td><td>Admissions, fees, academics, notices, gallery</td><td>8 to 10</td></tr>
</table>
<p>Our <a href="/digital/blog/clinic-website-design-pakistan">websites by industry guides</a> go deeper for each sector.</p>

<h2 id="home-page">What Should the Home Page Do First?</h2>
<p>The home page is not a brochure cover; it is a signpost. On a phone, the first screen should say what you do, where, and for whom, with a call or WhatsApp button. Below that, show your main services with links to their pages, a few trust signals such as reviews or registrations, and your location. Visitors who land on the home page should reach the right service page in one tap.</p>

<h2 id="service-pages">Why Give Each Service Its Own Page?</h2>
<p>A single "Services" page listing ten things gives search engines and customers little to work with. A separate page for each main service, such as "dental implants" or "corporate event catering", can answer specific questions, show relevant photos and prices, and appear when someone searches for exactly that service. Start with your three to five most profitable services.</p>

<h2 id="each-page-checklist">What Should Every Page Include?</h2>
<ul>
<li>a clear title and one main heading saying what the page is about</li>
<li>the answer to the main question in the first few lines</li>
<li>real photos rather than stock images where possible</li>
<li>prices or price guidance where you can share them</li>
<li>one clear next step, such as WhatsApp, call or a form</li>
<li>contact details in the footer</li>
</ul>

<h2 id="optional-pages">Which Pages Can Wait?</h2>
<p>A blog or guides section, team pages for every staff member, careers, detailed case studies and multiple language versions are valuable, but they can follow once the core pages are strong. An unfinished blog with two posts from three years ago looks worse than no blog at all.</p>

<h2 id="sitemap-example">What Does a Simple Sitemap Look Like?</h2>
<p>Example for a consultancy with a 10-page site: Home; Services, with four service pages beneath it; About; Case examples; FAQs; Contact; and Privacy policy. Each service page links to the contact page and to one related service. Our <a href="/digital/blog/website-brief-template">website brief template</a> helps you plan yours.</p>

<h2 id="what-we-build">What We Would Build for You</h2>
<p>We plan your page list with you during scoping, based on what your customers ask. A small site of up to 5 pages starts from {P['starter']}, a business site of up to 10 pages from {P['business']}, and an online store from {P['store']}. See our <a href="/digital/business-websites">business websites</a> service, the <a href="/digital/blog/how-long-to-build-a-website">guide to website timelines</a> and the <a href="/digital/blog/wordpress-vs-shopify-vs-custom-website">platform comparison</a>.</p>
""",
    faqs=[
        ("What pages should a small business website have?",
         "At minimum: a home page, a services or products page, an about page, a contact page with map, hours and WhatsApp, and a privacy policy. Most businesses then add one page per main service or product line, plus industry-specific pages such as doctor profiles or delivery and returns."),
        ("How many pages should a business website have?",
         "Many small businesses start with five core pages and grow to around ten, adding a page for each main service and a frequently asked questions page. The right number is the number needed to answer customers' main questions clearly, not a fixed target."),
        ("Do I need a separate page for each service?",
         "Usually yes, for your main services. A separate page can answer specific questions, show relevant photos and prices and appear in searches for that exact service. A single page listing everything gives customers and search engines much less to work with."),
        ("What should an about us page include?",
         "Your story and how long you have operated, the people behind the business with photos, your premises, the registrations or certifications you genuinely hold, and why customers choose you. Keep it factual and specific; trust comes from details customers can verify, not general claims."),
        ("Does a small business website need a privacy policy?",
         "If your website collects personal information through forms, bookings, orders or analytics, a privacy policy explaining what you collect and how you use it is good practice and may be required where your customers live. Ask your adviser what applies to your business."),
        ("Business website mein kaun se pages hone chahiye?",
         "Har business website mein home, services ya products, about, contact aur privacy policy ke pages hone chahiye. Phir har bari service ka alag page banayein. Clinic ke liye doctors ke profiles, dukan ke liye delivery aur return ka page, aur manufacturer ke liye products ka catalogue zaroori hai."),
    ],
    sources=[
        ("Google Search Central — SEO starter guide", "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"),
        ("Google Search Central — Creating helpful, reliable, people-first content", "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"),
        ("Nielsen Norman Group — Usability 101", "https://www.nngroup.com/articles/usability-101-introduction-to-usability/"),
        ("ICO — UK GDPR guidance and resources", "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/"),
        ("Google Search Central — Sitemaps overview", "https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview"),
    ],
    method=("Page structure advice follows Google's SEO starter and helpful content guidance and Nielsen Norman Group's usability basics, "
            "checked 29 October 2026. Page lists and totals by industry reflect how we plan sites with clients. The privacy point is "
            "general, not legal advice. Prices are our own packages."),
    related=["wordpress-vs-shopify-vs-custom-website", "how-long-to-build-a-website", "website-launch-checklist",
             "website-brief-template"],
    service_links=[("/digital/business-websites", "Plan your pages with us"), ("/digital/pricing", "See package sizes")],
    cta="Not sure which pages you need?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20website%20pages%20and%20need%20help%20planning%20mine",
)
