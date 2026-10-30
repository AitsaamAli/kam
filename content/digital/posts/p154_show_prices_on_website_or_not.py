import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=154,
    slug='show-prices-on-website-or-not',
    title='Should You Show Prices on Your Website? A Decision Guide',
    h1='Should You Show Prices on Your Website? A Decision Table by Business Type',
    crumb='Show Prices on Website',
    description='Should you show prices on your website? A decision table by business type, price on request vs price lists, showing ranges, and our own prices as a case.',
    keyword='show prices on website',
    cluster=['price on request vs price list', 'pricing page examples', 'should i show my rates'],
    category='Content and Conversion',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer=f"Most small businesses should show prices on their website in some form: a full price list, starting prices, typical ranges or example projects. Prices filter out poor-fit enquiries and build trust. Hide them only when every job is genuinely unique, and even then explain how pricing works. We publish ours, from {P['landing']}.",
    takeaways=["Visitors who cannot find any price often leave rather than ask.", "Showing prices filters out enquiries that were never going to buy.", "Starting prices, ranges and example projects work when exact prices vary.", "Explain what moves the price up or down, so the figure is not misread.", "Keep prices updated; old prices cause disputes and damage trust."],
    body=f"""
<h2 id="question">Should You Show Prices on Your Website?</h2>
<p>Many Pakistani businesses write "price on request" or "call for rates" everywhere. The reasons are understandable: fear that competitors will undercut them, worry that a customer will see one figure and expect it for a bigger job, or simply never having written prices down. Yet when visitors cannot find any indication of price, a large share simply leave and find someone who tells them. Deciding whether to show prices on your website is really deciding how to give a useful signal without promising the wrong thing.</p>
<p>Pricing is one of several decisions covered alongside our <a href="/digital/blog/homepage-content-guide">homepage guide</a>.</p>

<h2 id="decision">Which Approach Fits Your Business?</h2>
<table>
<tr><th>Business type</th><th>Suggested approach</th></tr>
<tr><td>Shops and online stores</td><td>Full prices on every product</td></tr>
<tr><td>Fixed-scope services (haircut, AC service, consultation)</td><td>Full price list</td></tr>
<tr><td>Packaged services (websites, photography, events)</td><td>Package prices with what each includes</td></tr>
<tr><td>Variable projects (renovation, custom software, fit-outs)</td><td>Starting prices, typical ranges and example projects</td></tr>
<tr><td>Trade and wholesale</td><td>Prices behind a trade login</td></tr>
<tr><td>Highly bespoke or confidential work</td><td>Explain how pricing works and typical budget bands</td></tr>
</table>

<h2 id="benefits">What Do You Gain From Showing Prices?</h2>
<ul>
<li><strong>Better enquiries.</strong> People who contact you already know roughly what it costs.</li>
<li><strong>Less time on quotes</strong> that go nowhere.</li>
<li><strong>Trust.</strong> Openness signals confidence and fair dealing.</li>
<li><strong>Search and AI visibility.</strong> Pages that answer "how much does X cost" give search engines and AI tools something specific to use.</li>
</ul>

<h2 id="worries">What About Competitors Seeing Your Prices?</h2>
<p>Competitors can usually find your prices anyway by posing as customers. What they cannot copy easily is your quality, speed, service and reputation. If you compete only on price, hiding it does not protect you for long; if you compete on value, explaining what your price includes is your strongest argument.</p>

<h2 id="ranges">How Do You Show Prices When Every Job Differs?</h2>
<p>Use one or more of these:</p>
<ol>
<li><strong>Starting prices:</strong> "Kitchen renovations from Rs 450,000", with what the starting job includes.</li>
<li><strong>Typical ranges:</strong> "Most two-bedroom repaints cost between Rs 60,000 and Rs 110,000."</li>
<li><strong>Example projects:</strong> three real jobs with scope and final cost, shared with permission.</li>
<li><strong>Price factors:</strong> a short list of what moves the price, such as size, materials and deadline.</li>
</ol>
<p>The figures above are invented for illustration. Use your own, and review them every few months.</p>

<h2 id="our-case">How Do We Handle Our Own Prices?</h2>
<p>We publish our package prices openly: landing pages from {P['landing']}, starter websites from {P['starter']}, business websites from {P['business']}, online stores from {P['store']}, web applications within {P['app_range']}, and care plans from {P['maint']} a month. Each package lists what it includes, and our guide to why quotes vary explains what changes the final figure. Publishing these has meant enquiries arrive better informed and quotes are faster to agree. See our <a href="/digital/pricing">pricing page</a>.</p>

<h2 id="wording">How Should Prices Be Worded?</h2>
<p>Be clear about what the price covers, whether delivery or materials are included, how payment works, and how long the price is valid. Avoid vague terms such as "affordable" or "competitive" without a number. If prices change often, date the list: "Prices updated October 2026".</p>

<h2 id="updates">How Often Should Prices Be Updated?</h2>
<p>Review prices whenever your costs change and at least every quarter. In Pakistan, material costs, fuel and the exchange rate can shift quickly, so a list from last year may already be wrong. When you change prices, update every page that mentions them, including service pages, FAQs, your Google Business Profile and any PDF price lists sent on WhatsApp. Honour any quote already given in writing for its stated validity period.</p>

<h2 id="privacy">Is There a Privacy Angle?</h2>
<p>When sharing example projects with costs, get the client's permission and leave out names, addresses or details that identify them unless they agree.</p>

<h2 id="build">Building a Pricing Page</h2>
<p>Our business websites, from {P['business']}, can include a pricing page or price lists per service. Our <a href="/digital/blog/service-page-structure">service page guide</a> shows where prices sit on each page. See <a href="/digital/business-websites">business websites</a>.</p>
""",
    faqs=[
        ('Is it a good idea to publish prices on a website?',
         "In most cases, yes, in some form: a full price list, package prices, starting prices, ranges or example projects. Prices filter out poor-fit enquiries and build trust. Hide them only when every job is genuinely unique, and even then explain how pricing works."),
        ('Is price on request a good idea?',
         "Usually not as the only information. Many visitors leave when they find no price at all. If you cannot publish fixed prices, give starting prices, typical ranges or example projects with costs, and explain clearly which factors change the final figure for each customer."),
        ("Won't competitors copy my prices if I publish them?",
         "Competitors can usually find your prices anyway, simply by posing as customers. What they cannot easily copy is your quality, speed, service and reputation. Explaining clearly what your price includes is often your strongest argument when a cheaper rival appears."),
        ('How do I show prices when every project is different?',
         "Use starting prices with what the basic job includes, typical ranges for common jobs, two or three example projects with real costs shared with permission, and a short list of factors that move the price, such as size, materials and deadlines."),
        ('Do published prices help with Google and AI search?',
         "Pages that answer how much something costs give search engines and AI tools specific information to use, which can help visibility for price searches. Keep prices accurate and dated, because outdated figures mislead customers and can be repeated by AI tools."),
        ('What prices does Kamboh Associates Digital publish?',
         f"Landing pages from {P['landing']}, starter websites from {P['starter']}, business websites from {P['business']}, online stores from {P['store']}, web applications within {P['app_range']}, and care plans from {P['maint']} a month. Each package lists what it includes."),
        ('Website par qeemat likhni chahiye ya nahin?',
         "Aksar businesses ke liye haan. Poori list, shuruati qeemat ya andazan range likhne se sahi log raabta karte hain aur bharosa barhta hai. Agar har kaam alag hai to misaal ke projects aur qeemat badalne wali cheezein batayein. Purani qeematein website par na chhorein."),
    ],
    sources=[('Google Search Central — Creating helpful, reliable, people-first content', 'https://developers.google.com/search/docs/fundamentals/creating-helpful-content'), ('Google Search Central — Product structured data', 'https://developers.google.com/search/docs/appearance/structured-data/product'), ('Google Search Central — AI features and your website', 'https://developers.google.com/search/docs/appearance/ai-features')],
    method="The decision table and wording advice are editorial. Renovation and repaint figures are invented for illustration. Our own prices come from the published list, used here as a worked case as the plan requires. No claim is made about conversion rates.",
    related=['homepage-content-guide', 'service-page-structure', 'about-us-page-that-builds-trust'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/business-websites', 'Business website service')],
    cta='Unsure how to present your prices?',
    wa='Hi%2C%20I%20read%20your%20guide%20on%20showing%20prices',
)
