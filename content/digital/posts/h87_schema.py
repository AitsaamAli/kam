import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=87,
    slug="schema-markup-business-websites",
    title="Schema Markup for Business Websites, Explained Simply",
    h1="Schema Markup for Business Websites Explained Simply: Which Types Matter and How to Check Them",
    crumb="Schema Markup Explained",
    description="Schema markup for business websites in plain English: what it is, which types matter, such as LocalBusiness and Product, and how to test it properly.",
    keyword="schema markup for business websites",
    cluster=["local business schema", "structured data for small business", "faq schema", "product schema",
             "breadcrumb schema", "rich results test"],
    category="Getting Found Online",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("Schema markup for business websites is hidden code that labels facts, such as your name, address, hours, products and FAQs, "
            "in the schema.org vocabulary so search engines read them reliably. Most businesses need 4 or 5 types: Organization or "
            "LocalBusiness, BreadcrumbList, and FAQPage or Product where relevant. Test it with Google's Rich Results Test."),
    takeaways=[
        "Schema markup labels facts on a page in a standard vocabulary, schema.org, without changing what visitors see.",
        "LocalBusiness, or a more specific subtype, is the most useful type for businesses customers visit.",
        "Markup must match what is visible on the page; hidden or false claims break Google's guidelines.",
        "Rich results are never guaranteed, even with valid markup.",
        "Test markup with Google's Rich Results Test and the Schema Markup Validator after every change.",
    ],
    body=f"""
<h2 id="what-it-is">What Is Schema Markup for Business Websites?</h2>
<p>Schema markup, also called structured data, is a small block of code on a web page that labels facts in a standard vocabulary published at schema.org. A person reading your contact page sees an address. The markup tells a search engine, in a format it reads reliably: this is a business, this is its name, this is its street address, these are its opening hours.</p>
<p>Google explains that structured data helps it understand page content and can make pages eligible for richer appearances in search results. It does not change what visitors see, and it does not by itself push a page up the rankings.</p>

<h2 id="which-types">Which Schema Types Matter for a Business?</h2>
<table>
<tr><th>Type</th><th>Use it on</th><th>Key details it labels</th></tr>
<tr><td>Organization</td><td>Home or about page</td><td>Official name, logo, website, contact points, social profiles</td></tr>
<tr><td>LocalBusiness (or a subtype such as Dentist or Restaurant)</td><td>Home or contact page of a business customers visit</td><td>Name, address, phone, opening hours, map coordinates</td></tr>
<tr><td>BreadcrumbList</td><td>Every page below the home page</td><td>The page's position in your site, such as Home, Services, Implants</td></tr>
<tr><td>FAQPage</td><td>Pages with a visible list of questions and answers</td><td>Each question and its answer</td></tr>
<tr><td>Product</td><td>Product pages in an online store</td><td>Name, image, price, currency, availability, reviews if genuine</td></tr>
</table>
<p>Google's local business documentation names name and address as required properties and recommends opening hours and geographic coordinates. It also advises using the most specific subtype that fits, such as Dentist instead of LocalBusiness.</p>

<h2 id="local-business-fields">What Should LocalBusiness Markup Contain?</h2>
<table>
<tr><th>Field</th><th>Example value</th></tr>
<tr><td>Name</td><td>Your exact business name, as on your signboard and Google profile</td></tr>
<tr><td>Address</td><td>Street, area, city, postal code and country</td></tr>
<tr><td>Telephone</td><td>The number customers call, in international format</td></tr>
<tr><td>Opening hours</td><td>Days with opening and closing times, including short Friday hours if any</td></tr>
<tr><td>Geo coordinates</td><td>Latitude and longitude of the entrance</td></tr>
<tr><td>URL and image</td><td>Your website address and a real photo of the business</td></tr>
</table>
<p>These must match your visible page and your Google Business Profile exactly. Our <a href="/digital/blog/google-business-profile-pakistan">Google Business Profile guide</a> explains why consistency matters.</p>

<h2 id="rules">What Rules Must Markup Follow?</h2>
<ul>
<li>Mark up only content visible on the page; do not add hidden claims.</li>
<li>Keep it accurate and current, such as hours and prices.</li>
<li>Do not mark up fake or self-written reviews.</li>
<li>Follow Google's general structured data guidelines and Search Essentials.</li>
</ul>
<p>Even with valid markup, Google decides whether to show a rich result. Treat rich results as a possible bonus, not a promise.</p>

<h2 id="testing">How Do You Test Schema Markup?</h2>
<ol>
<li>Paste the page address into Google's <strong>Rich Results Test</strong> to see which rich result types it finds and any errors.</li>
<li>Use the <strong>Schema Markup Validator</strong> to check the markup against the schema.org vocabulary in general.</li>
<li>After launch, check the enhancement reports in Google Search Console for errors across the site.</li>
<li>Retest whenever you change hours, prices or page templates.</li>
</ol>

<h2 id="platforms">How Is Markup Added on WordPress or Shopify?</h2>
<p>On WordPress, SEO plugins add basic Organization and breadcrumb markup, and a developer can add LocalBusiness details correctly. Shopify themes usually include Product markup; check it with the Rich Results Test, as quality varies. On custom sites, the developer adds it in page templates. In every case, someone should check it again after theme or plugin updates, because updates can remove or duplicate markup without warning.</p>

<h2 id="what-we-build">The Structured Data We Add to Every Site</h2>
<p>Every website we build includes Organization or the right LocalBusiness subtype, BreadcrumbList, and FAQPage or Product markup where the page content supports it, tested with the Rich Results Test before launch. Sites start from {P['starter']}, and stores from {P['store']}. See our <a href="/digital/business-websites">business websites</a> service, the <a href="/digital/blog/seo-ready-website-checklist">SEO-ready website checklist</a> and the <a href="/digital/blog/get-business-website-on-google">guide to getting your website on Google</a>.</p>
""",
    faqs=[
        ("What is schema markup in simple words?",
         "Schema markup is hidden code on a web page that labels facts, such as your business name, address, hours, products or FAQs, using the standard schema.org vocabulary. Visitors never see it; search engines read it reliably, which helps them understand your page and can make it eligible for richer results."),
        ("Which schema type should a local business use?",
         "Use LocalBusiness or, better, the most specific subtype that fits, such as Dentist, Restaurant or Store, as Google's documentation advises. Include the required name and address, plus recommended opening hours and map coordinates, and make every detail match your visible page and Google Business Profile."),
        ("Does schema markup improve Google rankings?",
         "Not directly. Structured data helps Google understand your content and can make pages eligible for rich results, which may attract more clicks. Rankings still depend on helpful content, relevance, page experience and trust. Valid markup does not guarantee that Google will show a rich result."),
        ("How do I test my website's schema markup?",
         "Use Google's Rich Results Test to see which rich result types a page is eligible for and any errors, and the Schema Markup Validator for general schema.org checks. After launch, review the enhancement reports in Google Search Console, and retest whenever hours, prices or templates change."),
        ("Can I add review stars with schema markup?",
         "Only for genuine reviews that are visible on the page and allowed under Google's guidelines. Never mark up fake, self-written or hidden reviews. Google also restricts some self-serving review markup for businesses, so check its current review snippet documentation before adding review markup."),
        ("Schema markup kya hota hai aur kya meri website ko chahiye?",
         "Schema markup chhupa hua code hai jo search engines ko aap ka naam, pata, timings aur products saaf tareeqe se batata hai. Zyada tar businesses ko LocalBusiness, BreadcrumbList aur zaroorat ke mutabiq FAQPage ya Product chahiye. Isay Google ke Rich Results Test se check karein."),
    ],
    sources=[
        ("Google Search Central — Introduction to structured data", "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"),
        ("Google Search Central — Local business structured data", "https://developers.google.com/search/docs/appearance/structured-data/local-business"),
        ("schema.org — Vocabulary for structured data", "https://schema.org/"),
        ("schema.org — LocalBusiness", "https://schema.org/LocalBusiness"),
        ("Google — Rich Results Test", "https://search.google.com/test/rich-results"),
        ("Schema Markup Validator", "https://validator.schema.org/"),
    ],
    method=("Definitions, required and recommended LocalBusiness properties, the advice to use specific subtypes and the testing tools come "
            "from Google Search Central and schema.org, checked 29 October 2026. As the brief asks, there are no code blocks; fields are "
            "described in tables. Prices are our own published packages."),
    related=["get-business-website-on-google", "seo-ready-website-checklist", "ai-search-visibility-for-business",
             "google-business-profile-pakistan"],
    service_links=[("/digital/business-websites", "Websites with schema built in"), ("/digital/contact", "Get your markup checked")],
    cta="Want search engines to read your details correctly?",
    wa="Hi%2C%20I%20read%20your%20schema%20markup%20guide%20and%20need%20help",
)
