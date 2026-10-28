import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=11,
    slug="website-redesign-cost",
    title="Website Redesign Cost in Pakistan: Fix or Rebuild?",
    h1="Website Redesign Cost: When to Redesign, When to Fix, and What It Costs",
    crumb="Website Redesign Cost",
    description=f"A website redesign usually costs about the same as a new build: from {P['starter']} for a small site with us. Learn when a fix is enough and how to keep rankings.",
    keyword="website redesign cost",
    cluster=["website redesign price pakistan", "website revamp cost", "redesign website without losing seo",
             "website makeover price", "old website update cost"],
    category="Costs & Budgets",
    published="2026-10-28", published_h="28 October 2026",
    updated="2026-10-28", updated_h="28 October 2026",
    answer=(f"A full redesign usually costs about the same as a new website of the same size: from {P['starter']} for a small site and "
            f"{P['business']} for a ten-page business site with us. Many sites do not need one. Fixing speed, mobile layout, content and "
            "calls to action often costs far less, and a redesign done carelessly can lose the Google rankings you already have."),
    takeaways=[
        "Redesign when the platform is outdated, the site cannot be edited, or the brand has changed. Fix when the problems are speed, content or conversion.",
        "A redesign is priced like a new build because the design, development and testing work is similar.",
        "Keep your URLs where possible, or set up 301 redirects for every changed URL, to protect search rankings.",
        "Measure before and after: traffic, enquiries, speed and rankings for your main pages.",
        "Ask for a fix-first audit before paying for a full redesign.",
    ],
    body=f"""
<h2 id="redesign-or-fix">Do You Need a Redesign or a Fix?</h2>
<p>Business owners often ask for a redesign when what they really want is more enquiries. Use this table to decide which problem you have.</p>
<table>
<tr><th>Symptom</th><th>Usually needs</th></tr>
<tr><td>Site is slow on mobile</td><td>Fix: image compression, caching, removing heavy plugins</td></tr>
<tr><td>Looks dated but works</td><td>Refresh: new styling on the existing structure</td></tr>
<tr><td>Visitors but few enquiries</td><td>Fix: clearer offer, visible WhatsApp and call buttons, better forms</td></tr>
<tr><td>You cannot edit it, or the developer has disappeared</td><td>Rebuild on a platform you control</td></tr>
<tr><td>Built on an unsupported or pirated theme</td><td>Rebuild</td></tr>
<tr><td>Brand, services or market have changed</td><td>Redesign</td></tr>
<tr><td>Not mobile-friendly at all</td><td>Redesign</td></tr>
</table>

<h2 id="cost">What Does a Redesign Cost?</h2>
<p>A full redesign involves the same steps as a new site: planning, design, development, content migration and testing. It is therefore priced like a new build of the same size. Our prices:</p>
<table>
<tr><th>Scope</th><th>Typical price with us</th></tr>
<tr><td>Fix package (speed, mobile layout, calls to action)</td><td>Quoted after an audit; usually a fraction of a rebuild</td></tr>
<tr><td>Small site redesign, up to 5 pages</td><td class="price">{P['starter']}</td></tr>
<tr><td>Business site redesign, up to 10 pages</td><td class="price">{P['business']}</td></tr>
<tr><td>Online store redesign or platform move</td><td class="price">from {P['store']}</td></tr>
</table>
<p>Content migration can add cost when a site has many pages or blog posts to move. Ask for this to be listed separately in the quote.</p>

<h2 id="seo-risk">How to Redesign Without Losing Google Rankings</h2>
<p>A redesign is one of the most common causes of a sudden drop in search traffic. Google's own guidance on site moves explains why: when URLs change, search engines must learn the new locations, and any page without a redirect loses the value it built up. To protect your rankings:</p>
<ol>
<li><strong>Crawl the old site</strong> and export every URL, title and meta description.</li>
<li><strong>Keep URLs the same</strong> wherever possible.</li>
<li><strong>Map every changed URL</strong> to its new address and set up 301 redirects.</li>
<li><strong>Keep the content that ranks.</strong> Rewrite carefully; do not delete pages that bring traffic.</li>
<li><strong>Carry over titles, headings and structured data</strong> on important pages.</li>
<li><strong>Test on a staging site</strong> before launch, including redirects and forms.</li>
<li><strong>Submit the new sitemap</strong> in Google Search Console and watch for errors for a few weeks.</li>
</ol>

<h2 id="measure">Measure Before and After</h2>
<p>Record these numbers for the month before the redesign so you can judge whether it worked:</p>
<ul>
<li>Organic clicks and impressions for your main pages in Google Search Console.</li>
<li>Enquiries: WhatsApp clicks, calls and form submissions.</li>
<li>Mobile speed (Largest Contentful Paint) on key pages.</li>
<li>Rankings for your five to ten most important searches.</li>
</ul>

<h2 id="process">Our Redesign Process</h2>
<ol>
<li><strong>Audit:</strong> speed, mobile usability, content, conversions and SEO, with a written fix-or-redesign recommendation.</li>
<li><strong>Plan:</strong> sitemap, URL map, content to keep, rewrite or merge.</li>
<li><strong>Design and build</strong> on staging.</li>
<li><strong>Migrate content</strong> and set up redirects.</li>
<li><strong>Test</strong> on phones, forms, redirects and speed.</li>
<li><strong>Launch and monitor</strong> Search Console for at least four weeks.</li>
</ol>

<h2 id="platform-move">Moving Platform During a Redesign</h2>
<p>Redesigns are a natural time to leave an outdated or locked-in platform, for example a builder you cannot export from, or a custom system nobody can maintain. Moving to WordPress, Shopify or a well-documented custom stack gives you control. It also means extra work for content and URL migration, so plan it from the start. Our <a href="/digital/blog/wordpress-website-price-in-pakistan">WordPress</a> and <a href="/digital/blog/shopify-store-price-in-pakistan">Shopify</a> price guides explain each platform's running costs.</p>

<h2 id="ask">Questions to Ask Before Paying for a Redesign</h2>
<ul>
<li>What exactly is wrong with the current site, and can it be fixed instead?</li>
<li>Will my URLs change, and how will redirects be handled?</li>
<li>Who moves the content, and is it in the price?</li>
<li>How will you measure success after launch?</li>
<li>Will I own the new site, domain and hosting?</li>
</ul>
<p>For overall budgets, see our <a href="/digital/blog/website-price-in-pakistan">website price guide</a>; for keeping the new site healthy, read our <a href="/digital/blog/website-maintenance-charges-in-pakistan">maintenance guide</a>.</p>
""",
    faqs=[
        ("How much does a website redesign cost in Pakistan?",
         f"A full redesign is usually priced like a new site of the same size. With us that means {P['starter']} for up to five pages and {P['business']} for up to ten pages. Smaller fixes for speed, mobile layout or conversions cost less and are quoted after an audit."),
        ("Will redesigning my website affect my Google rankings?",
         "It can, if URLs change without redirects or ranking content is removed. Keeping URLs, mapping 301 redirects, preserving important content and submitting a new sitemap protects most rankings."),
        ("How do I know if my website needs a redesign?",
         "Redesign if you cannot edit the site, it is built on an unsupported platform, it is not mobile-friendly, or your brand has changed. If the problems are speed, content or low enquiries, targeted fixes are usually enough."),
        ("What is a 301 redirect?",
         "A 301 redirect permanently sends visitors and search engines from an old URL to a new one. It passes most of the old page's search value to the new page, which is why every changed URL needs one during a redesign."),
        ("How long does a website redesign take?",
         "A small site redesign usually takes two to four weeks, a business site four to eight weeks, and a store or platform move longer, depending on how much content must be migrated and tested."),
        ("Can I keep my content and just change the design?",
         "Yes. A design refresh keeps your structure and content and changes how it looks. It is often the cheapest way to modernise a site that still works well."),
        ("Should I change platforms during a redesign?",
         "Only if the current platform limits you, for example if you cannot edit or export it, or it is no longer supported. Moving adds content and URL migration work, so plan and budget it from the start."),
    ],
    sources=[
        ("Google Search Central — Site moves with URL changes", "https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes"),
        ("Google Search Central — Redirects and Google Search", "https://developers.google.com/search/docs/crawling-indexing/301-redirects"),
        ("web.dev — Largest Contentful Paint", "https://web.dev/articles/lcp"),
    ],
    method=("Redesign steps follow Google Search Central's documentation on site moves and redirects, and the audits we run before every "
            "redesign. Prices are from our published price list. We do not quote market redesign ranges for Pakistan because published "
            "figures are rare and inconsistent."),
    related=["website-price-in-pakistan", "website-maintenance-charges-in-pakistan", "landing-page-design-cost-in-pakistan"],
    service_links=[("/digital/business-websites", "Business website service"), ("/digital/contact", "Ask for a fix-first audit")],
    cta="Thinking about redesigning your website?",
    wa="Hi%2C%20I%20read%20your%20redesign%20guide%20and%20want%20an%20audit",
)
