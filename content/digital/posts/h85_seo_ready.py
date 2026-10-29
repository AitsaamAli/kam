import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=85,
    slug="seo-ready-website-checklist",
    title="SEO Friendly Website Development: 15 Things Built In",
    h1="SEO Friendly Website Development: The 15 Things That Should Be Built In Before Launch",
    crumb="SEO-Ready Website Checklist",
    description="SEO friendly website development: a 15-point checklist of what to build in before launch, from indexing and titles to speed and structured data.",
    keyword="seo friendly website development",
    cluster=["seo ready website", "technical seo checklist", "website seo basics", "seo before launch",
             "on page seo checklist", "seo friendly website kaise banayein"],
    category="Getting Found Online",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=(f"SEO friendly website development means building in 15 basics before launch: indexable pages, a sitemap, Search Console, clean "
            f"URLs, unique titles, one H1 per page, fast mobile pages, image alt text, internal links, HTTPS, structured data, redirects "
            f"and analytics. These are included in our websites from {P['starter']}."),
    takeaways=[
        "Technical basics decide whether Google can read your site at all; content decides whether it ranks.",
        "Most SEO problems on new sites are simple: pages left on noindex, missing titles, slow images or broken links.",
        "Every page needs a unique, descriptive title and one clear main heading.",
        "Structured data describes your business details for search engines in a standard format.",
        "Ask for this checklist in writing before you hire a developer, and check it at launch.",
    ],
    body=f"""
<h2 id="what-it-means">What Does SEO Friendly Website Development Mean?</h2>
<p>Search engine optimisation, or SEO, is the work of helping search engines understand your pages and show them to the right people. An SEO friendly website is built so that nothing in its structure gets in the way. It does not guarantee rankings; that depends on content, competition and trust. But a site with technical problems can struggle no matter how good its content is.</p>
<p>Google's SEO starter guide covers the fundamentals. The checklist below turns them into 15 things your developer should build in before launch.</p>

<h2 id="checklist">What Are the 15 Things to Build In?</h2>
<table>
<tr><th>#</th><th>Item</th><th>What it means in plain words</th></tr>
<tr><td>1</td><td>Indexable pages</td><td>No leftover noindex tags or robots.txt blocks from development</td></tr>
<tr><td>2</td><td>XML sitemap</td><td>A list of your pages, submitted in Search Console</td></tr>
<tr><td>3</td><td>Search Console and Analytics</td><td>Set up in the owner's name from day one</td></tr>
<tr><td>4</td><td>Clean URLs</td><td>Readable addresses such as /services/dental-implants</td></tr>
<tr><td>5</td><td>Unique titles</td><td>Each page's title describes that page clearly</td></tr>
<tr><td>6</td><td>Meta descriptions</td><td>A short, unique summary per page</td></tr>
<tr><td>7</td><td>One H1 and logical headings</td><td>One main heading, then H2s and H3s in order</td></tr>
<tr><td>8</td><td>Mobile-first layout</td><td>Readable and usable on a phone without zooming</td></tr>
<tr><td>9</td><td>Fast loading</td><td>Compressed images, light theme, caching; good Core Web Vitals</td></tr>
<tr><td>10</td><td>Image alt text</td><td>Short descriptions of meaningful images</td></tr>
<tr><td>11</td><td>Internal links</td><td>Important pages linked from menus and related pages</td></tr>
<tr><td>12</td><td>HTTPS everywhere</td><td>A valid certificate and no mixed insecure content</td></tr>
<tr><td>13</td><td>Structured data</td><td>Business name, address, hours and pages labelled in a standard format</td></tr>
<tr><td>14</td><td>Redirects and 404 page</td><td>Old addresses redirect; a helpful page for missing links</td></tr>
<tr><td>15</td><td>Canonical tags</td><td>Tell Google the main version when pages are similar</td></tr>
</table>

<h2 id="structured-data">What Does Structured Data Look Like in Plain Words?</h2>
<p>Structured data is extra code that labels facts on a page so search engines can read them reliably. For a clinic, the labels would say, in effect: this is a medical business named X, at this address, with this phone number, open these hours, on this map location. The page looks the same to visitors. Google's local business documentation lists name and address as required properties and recommends hours and coordinates. Our <a href="/digital/blog/schema-markup-business-websites">schema markup guide</a> explains which types matter.</p>

<h2 id="common-mistakes">Which Mistakes Are Most Common on New Sites?</h2>
<ul>
<li>The whole site launched with "discourage search engines" still ticked from development.</li>
<li>Every page titled "Home" or the business name only.</li>
<li>Huge photos straight from a phone, making pages slow on mobile data.</li>
<li>Text inside images, which search engines and screen readers cannot read well.</li>
<li>Old website addresses left without redirects after a redesign.</li>
<li>Meta keywords added; Google says it does not use them.</li>
</ul>

<h2 id="local-language">What About Urdu and Local Searches?</h2>
<p>Many Pakistani customers search in English, Urdu or Roman Urdu. If your customers do, give Urdu content its own pages with the correct right-to-left direction, rather than mixing languages in one page, and write Roman Urdu phrases naturally in FAQs where people actually use them. Put your city and area in titles and contact pages where relevant, matching your Google Business Profile.</p>

<h2 id="check-at-launch">How Do You Check It at Launch?</h2>
<ol>
<li>Search <em>site:yourdomain</em> a week after launch to see what is indexed.</li>
<li>Open Search Console's page indexing report and fix any errors.</li>
<li>Run PageSpeed Insights or Lighthouse on key pages, on the mobile setting.</li>
<li>Test structured data with Google's Rich Results Test.</li>
<li>Click through every menu link on your phone.</li>
</ol>
<p>For a full pre-launch list beyond SEO, see our <a href="/digital/blog/website-launch-checklist">website launch checklist</a>.</p>

<h2 id="what-we-build">What We Would Build for You</h2>
<p>All 15 items are part of our standard build, not an add-on: a 5-page site from {P['starter']}, a 10-page site from {P['business']}, and stores from {P['store']}. We set up Search Console and Analytics in your name and hand over a short report at launch. See our <a href="/digital/business-websites">business websites</a> service and the <a href="/digital/blog/get-business-website-on-google">guide to getting your website on Google</a>.</p>
""",
    faqs=[
        ("What makes a website SEO friendly?",
         "An SEO friendly website lets search engines find, read and understand every important page: indexable pages, a sitemap, clean URLs, unique titles and descriptions, logical headings, fast mobile pages, image alt text, internal links, HTTPS, structured data and redirects. Content quality then decides how well pages rank."),
        ("Does an SEO friendly website guarantee rankings?",
         "No. It removes technical obstacles, but rankings depend on how helpful your content is, competition for the search, and signals of trust such as reviews and genuine links. Google's own SEO guide says there are no shortcuts to the top of results."),
        ("What is structured data on a website?",
         "Structured data is code that labels facts on a page, such as your business name, address, phone, hours and location, in a standard format search engines read reliably. Visitors do not see it. It helps search engines understand your details and can make pages eligible for richer results."),
        ("Should I use meta keywords for SEO?",
         "There is no need. Google states plainly that its search does not read the meta keywords tag at all. Put the effort into unique, descriptive titles, helpful content that answers customer questions, clear headings, fast pages and internal links, which help both visitors and search engines understand your site."),
        ("How do I check if my new website is SEO ready?",
         "A week after launch, search site:yourdomain to see indexed pages, review Search Console's indexing report, test key pages with PageSpeed Insights or Lighthouse on mobile, check structured data with the Rich Results Test and click every menu link on a phone. Fix any errors found."),
        ("SEO friendly website kaise banayein?",
         "Website ke har page ka alag aur saaf title ho, aik main heading ho, tasveerein halki hon aur alt text ho, pages mobile par jaldi khulen, sitemap aur Search Console set ho, HTTPS ho aur purane pages ke redirects lagay hon. Developer se yeh 15 cheezein likhwa kar lein aur launch par check karein."),
    ],
    sources=[
        ("Google Search Central — SEO starter guide", "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"),
        ("Google Search Central — Sitemaps overview", "https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview"),
        ("Google Search Central — Local business structured data", "https://developers.google.com/search/docs/appearance/structured-data/local-business"),
        ("Google — Rich Results Test", "https://search.google.com/test/rich-results"),
        ("Chrome for Developers — Lighthouse overview", "https://developer.chrome.com/docs/lighthouse/overview"),
        ("web.dev — Web Vitals", "https://web.dev/articles/vitals"),
    ],
    method=("The checklist follows Google's SEO starter guide, sitemap and local business structured data documentation, and Lighthouse and "
            "web.dev guidance, checked 29 October 2026. The 15-point grouping and the common mistakes list are our own, from launching and "
            "fixing client sites. Prices are our own published packages."),
    related=["get-business-website-on-google", "schema-markup-business-websites", "website-speed-pakistan-mobile",
             "website-launch-checklist"],
    service_links=[("/digital/business-websites", "SEO-ready business websites"), ("/digital/contact", "Get your site checked")],
    cta="Want a website built to be found?",
    wa="Hi%2C%20I%20read%20your%20SEO-ready%20website%20checklist%20and%20need%20a%20quote",
)
