import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=83,
    slug="get-business-website-on-google",
    title="How to Get Your Business Website on Google: Pakistan Guide",
    h1="How to Get Your Business Website on Google: A Practical Pakistan Guide With a 30-Day Plan",
    crumb="Get Your Website on Google",
    description="How to get your business website on Google in Pakistan: indexing with Search Console, Google Business Profile, reviews, useful content and links, with a 30-day plan.",
    keyword="website on google",
    cluster=["google par business kaise laye", "get website indexed", "business on google search", "how to show website on google",
             "website not showing on google", "submit website to google", "google search console setup"],
    category="Getting Found Online",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("To get your website on Google, do 4 things: let Google index it through Search Console and a sitemap, create a verified "
            "Google Business Profile, publish pages that answer customers' questions, and earn genuine reviews and links. Indexing can take "
            "days to weeks; ranking takes longer, and no one can promise a position."),
    takeaways=[
        "Getting on Google has two parts: being indexed, so Google knows your pages exist, and ranking, so they appear for useful searches.",
        "Google Search Console is free and shows whether your pages are indexed and which searches bring visitors.",
        "For local businesses, a verified Google Business Profile often brings more customers than the website alone.",
        "Pages that answer real customer questions in plain language are what rank over time.",
        "Expect indexing in days to weeks and real results in months; anyone guaranteeing a position is not being honest.",
    ],
    body=f"""
<h2 id="two-parts">How Do You Get a Website on Google?</h2>
<p>Getting a business website on Google happens in two stages. First, Google must <strong>find and index</strong> your pages, meaning it knows they exist and stores them. Second, your pages must <strong>rank</strong>, meaning Google decides they are among the best answers for a search. Many Pakistani business owners say "my website is not on Google" when it is indexed but ranks too low to see, or when nobody has checked at all.</p>
<p>Google's own SEO starter guide is clear that there is no guarantee any site will be added to its index and no shortcut to the top. What you can do is remove obstacles and give Google, and customers, good reasons to choose your pages. This guide is the hub for our series on getting found and fixing website problems.</p>

<h2 id="check-indexing">Is Your Website Already on Google?</h2>
<p>Start with a two-minute check. Search Google for <em>site:yourdomain.pk</em>, replacing it with your own domain. If pages appear, your site is indexed; if nothing appears, Google has not indexed it yet. For a precise answer, set up Google Search Console, a free tool that shows which pages are indexed, which searches show your site, how many people click, and any problems Google finds.</p>

<h2 id="indexing-steps">What Are the Indexing Steps?</h2>
<ol>
<li><strong>Verify your site in Search Console</strong> as the owner, using your own Google account.</li>
<li><strong>Submit a sitemap.</strong> A sitemap lists your pages for Google. Google says small, well-linked sites of about 500 pages or fewer may not strictly need one; it still helps new sites with few links pointing to them.</li>
<li><strong>Inspect key pages</strong> with the URL Inspection tool and request indexing for new or changed pages. Requests have a quota, and resubmitting does not speed things up.</li>
<li><strong>Check for blocks.</strong> Make sure pages are not set to noindex and that robots.txt does not block them; developers sometimes leave these on after building a site.</li>
<li><strong>Link pages together.</strong> Every important page should be reachable from your menu or other pages, ideally within two or three clicks of the home page.</li>
</ol>
<p>Google says recrawling can take from a few days to a few weeks. Our <a href="/digital/blog/seo-ready-website-checklist">SEO-ready website checklist</a> lists everything that should be built in before launch.</p>

<h2 id="business-profile">Why Is Google Business Profile So Important?</h2>
<p>For businesses customers visit or that serve an area, such as clinics, shops, restaurants and service companies, a Google Business Profile controls how you appear on Google Maps and in local results, often above ordinary website results. It is free. Google's help pages say profiles are for storefront and service-area businesses that meet customers in person, not online-only businesses. Our <a href="/digital/blog/google-business-profile-pakistan">Google Business Profile guide for Pakistan</a> covers setup and verification step by step.</p>

<h2 id="content">What Kind of Content Ranks?</h2>
<p>Google's guidance on helpful content asks whether a page is written for people first, shows real expertise, and leaves the reader feeling they found what they needed. For a business website, that means:</p>
<ul>
<li>one clear page for each main service or product, with prices or price guidance where possible</li>
<li>pages that answer the questions customers ask on WhatsApp, written in plain language</li>
<li>real photos, real addresses and named people where appropriate</li>
<li>Urdu or Roman Urdu content where your customers search that way</li>
</ul>
<p>Titles matter too. Google's starter guide advises a title that is unique to the page, clear and accurately describes it. Google does not use the meta keywords tag, so skip it.</p>

<h2 id="speed-mobile">Does Speed on Mobile Matter?</h2>
<p>Yes, for both rankings and customers. Most Pakistani visitors use phones on mobile data. Google measures page experience with Core Web Vitals; for example, a good Largest Contentful Paint is 2.5 seconds or less. Our <a href="/digital/blog/website-speed-pakistan-mobile">website speed guide</a> explains what matters most, and the <a href="/digital/blog/website-slow-on-mobile">slow on mobile guide</a> covers fixes.</p>

<h2 id="reviews-links">How Do Reviews and Links Help?</h2>
<p>Reviews on your Business Profile influence local results and customers' choices. Ask every customer for an honest review; Google's policy forbids rewards for reviews and asking only happy customers. Links from other reputable websites, such as your trade association, suppliers, local news or directories you are genuinely listed in, help Google trust your site. Avoid buying links; it breaks Google's spam policies and can backfire.</p>

<h2 id="thirty-day-plan">What Is a Realistic 30-Day Plan?</h2>
<table>
<tr><th>Days</th><th>Actions</th></tr>
<tr><td>1 to 3</td><td>Set up Search Console and Analytics in your name; submit sitemap; check indexing</td></tr>
<tr><td>4 to 7</td><td>Create or claim your Google Business Profile and start verification</td></tr>
<tr><td>8 to 14</td><td>Rewrite titles and descriptions for main pages; add WhatsApp and call buttons</td></tr>
<tr><td>15 to 21</td><td>Publish two pages answering common customer questions; add structured data</td></tr>
<tr><td>22 to 28</td><td>Ask recent customers for reviews; reply to all reviews; list on genuine directories</td></tr>
<tr><td>29 to 30</td><td>Check Search Console for indexed pages and searches; plan next month</td></tr>
</table>
<p>Example plan only. After the first month, repeat the content and review steps every month. Results take longer than 30 days; Google notes some changes show in hours and others take months.</p>

<h2 id="ai-and-conversions">What About AI Search and Turning Visits Into Enquiries?</h2>
<p>Google's AI Overviews and assistants such as ChatGPT draw on the same well-structured, trustworthy pages. Our guide to <a href="/digital/blog/ai-search-visibility-for-business">AI search visibility</a> explains what helps. Getting visitors is only half the job: if they arrive but do not contact you, read <a href="/digital/blog/website-visitors-no-enquiries">12 fixes for websites with visitors but no enquiries</a> and <a href="/digital/blog/whatsapp-button-website-leads">WhatsApp leads from your website</a>. Structured data helps search engines read your details; see <a href="/digital/blog/schema-markup-business-websites">schema markup explained simply</a>.</p>
<p>If your site has a problem, start with <a href="/digital/blog/website-down-check">website down? find the cause</a>, <a href="/digital/blog/website-hacked-what-to-do">website hacked: the first 24 hours</a>, <a href="/digital/blog/website-security-checklist-small-business">the security checklist</a>, <a href="/digital/blog/website-backups-small-business">website backups</a> or <a href="/digital/blog/new-website-without-losing-google-traffic">moving to a new website without losing traffic</a>.</p>

<h2 id="what-we-build">How We Build Websites That Google Can Find</h2>
<p>Every website we build is set up to be found: Search Console and Analytics in your name, a sitemap, clean titles, structured data, fast mobile pages and Business Profile guidance. New sites begin at {P['starter']} for five pages, or {P['business']} for ten. For an existing site, optional maintenance at {P['maint']} a month includes monthly Search Console checks. We do not promise rankings; we fix what is in your control. See our <a href="/digital/business-websites">business websites</a> service.</p>
""",
    faqs=[
        ("How long does it take for a new website to appear on Google?",
         "Google says crawling and indexing can take from a few days to a few weeks after you submit a sitemap or request indexing, and it does not promise that every page will be indexed. Ranking well for useful searches usually takes months and depends on content, competition and trust."),
        ("Why is my website not showing on Google?",
         "Common reasons are that Google has not indexed it yet, pages are set to noindex or blocked in robots.txt after development, the site is new with no links, or it is indexed but ranks too low to see. Check in Google Search Console, which shows the exact status of each page."),
        ("Is it free to put my business on Google?",
         "Yes. Indexing in Google Search, Google Search Console and Google Business Profile are all free. You pay only if you choose Google Ads or hire someone to build or improve your website. Be wary of anyone charging a fee simply to 'submit' your site to Google."),
        ("Do I need a sitemap for my small business website?",
         "Google says small, well-linked sites of about 500 pages or fewer may manage without one. Sitemaps still help new sites with few external links, and most website platforms create one automatically. Submitting it in Search Console is quick and lets you see any indexing problems."),
        ("What is Google Search Console?",
         "It is a free Google tool that shows whether your pages are indexed, which searches show your site, how many people click, which sites link to you and any problems Google finds, such as errors, security issues or penalties. Every business website should have it set up in the owner's name."),
        ("Can anyone guarantee my website will be first on Google?",
         "No. Google's own guide says there is no guarantee a site will be indexed and no shortcut to the top of results. Anyone promising a fixed position is either misleading you or using tactics that can get a site penalised. Good content, speed, reviews and genuine links improve your chances."),
        ("Google par apna business kaise laayen?",
         "Pehle Google Search Console mein apni website verify karein aur sitemap submit karein. Phir Google Business Profile banayein aur verify karein, asli tasveerein aur timings dein. Customers ke sawalon ke jawab wale pages likhein aur har customer se imaandari se review ka kahein. Natije hafton se mahinon mein aate hain."),
        ("Does Google Business Profile help my website rank?",
         "It mainly controls how your business appears on Google Maps and in local results, which for many local searches show above ordinary website results. Linking the profile to your website, keeping details consistent and collecting genuine reviews help customers find both the profile and the website."),
        ("Should I use the meta keywords tag?",
         "No. Google's SEO starter guide says Google Search does not use the keywords meta tag. Spend the effort instead on clear, unique page titles, helpful content that answers customer questions, fast mobile pages and descriptive headings, which all help both visitors and search engines."),
    ],
    sources=[
        ("Google Search Central — SEO starter guide", "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"),
        ("Google Search Central — Ask Google to recrawl your URLs", "https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl"),
        ("Google Search Central — Sitemaps overview", "https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview"),
        ("Google Search Console Help — About Search Console", "https://support.google.com/webmasters/answer/9128668"),
        ("Google Business Profile Help — Create and manage your Business Profile", "https://support.google.com/business/answer/7039811"),
        ("Google Search Central — Creating helpful, reliable, people-first content", "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"),
        ("web.dev — Largest Contentful Paint", "https://web.dev/articles/lcp"),
        ("Google Maps — Prohibited and restricted content (review policy)", "https://support.google.com/contributionpolicy/answer/7400114"),
    ],
    method=("Indexing, sitemap, recrawl timing, meta keywords and title advice come from Google Search Central pages; Business Profile and "
            "review rules from Google's help and policy pages; the LCP threshold from web.dev, all checked 29 October 2026. The 30-day plan "
            "is an illustrative template. Prices are our own published packages."),
    related=["google-business-profile-pakistan", "seo-ready-website-checklist", "ai-search-visibility-for-business",
             "website-visitors-no-enquiries", "website-speed-pakistan-mobile"],
    service_links=[("/digital/business-websites", "Websites built to be found"), ("/digital/pricing", "See maintenance plans")],
    cta="Want your business found on Google?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20getting%20my%20website%20on%20Google%20and%20need%20help",
)
