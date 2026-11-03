import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=231,
    slug="website-not-showing-on-google",
    title="New Website Not on Google? Causes and Fixes",
    h1="New Website Not Showing on Google After Launch: Causes, Checks and Fixes",
    crumb="New Website Not on Google",
    description="New website not on Google weeks after launch? The Search Console checks to run, common blockers such as noindex and robots.txt, and how long indexing takes.",
    keyword="new website not on google",
    cluster=["site not indexed", "website not in google search", "new website not appearing",
             "noindex tag check", "submit sitemap search console"],
    category="Planning & Launch",
    published="2026-11-03", published_h="3 November 2026",
    updated="2026-11-03", updated_h="3 November 2026",
    answer=(f"A new website not on Google is usually blocked by a setting or simply not discovered yet. "
            f"Run 4 checks: Search Console's URL Inspection, look for a leftover noindex tag or a robots.txt block, submit a sitemap and request indexing. "
            f"New sites often take a few days to a few weeks to appear, and ranking takes longer."),
    takeaways=[
        "Search your exact domain on Google first; being indexed and ranking for keywords are different things.",
        "The most common blocker is a 'discourage search engines' or noindex setting left on after development.",
        "Set up Google Search Console, submit your sitemap and use URL Inspection on the homepage.",
        "Thin pages with little text, or near-copies of other pages, may be crawled but not indexed.",
        "A Google Business Profile and a few genuine links from other sites help Google discover a new business.",
    ],
    body=f"""
<h2 id="indexed-or-ranking">Is the New Website Not on Google, or Just Not Ranking?</h2>
<p>These are two different problems. Search for <strong>site:yourdomain.pk</strong> on Google. If no pages appear, the site is not indexed: Google either has not found it or has been told not to include it. If pages appear but you cannot find the site when searching for your services, it is indexed but not ranking yet. Ranking takes time and depends on content, competition and reputation. This guide covers the first problem in detail; for the second, our guide to <a href="/digital/blog/get-business-website-on-google">getting a business website on Google</a> explains how ranking is built.</p>

<h2 id="common-causes">Common Reasons a New Website Is Not Indexed</h2>
<table>
<tr><th>Cause</th><th>How to spot it</th><th>Fix</th></tr>
<tr><td>Search engines discouraged</td><td>WordPress: Settings, Reading, the "discourage search engines" box is ticked</td><td>Untick it and save</td></tr>
<tr><td>Noindex tag</td><td>Page source contains a robots meta tag with "noindex"</td><td>Remove it from live pages</td></tr>
<tr><td>Robots.txt blocking</td><td>yourdomain.pk/robots.txt shows "Disallow: /"</td><td>Allow crawling of the live site</td></tr>
<tr><td>Password protection</td><td>The site asks for a login or shows "coming soon"</td><td>Remove the protection at launch</td></tr>
<tr><td>Not discovered yet</td><td>Search Console shows the URL is unknown to Google</td><td>Submit a sitemap and request indexing</td></tr>
<tr><td>Wrong canonical</td><td>Pages point their canonical tag to the staging site or another URL</td><td>Set canonicals to the live URLs</td></tr>
</table>
<p>Developers often turn on noindex during development so the unfinished site does not appear in search. Forgetting to remove it at launch is the single most common cause we see.</p>

<h2 id="search-console">How to Use Search Console to Check</h2>
<ol>
<li>Add your site to Google Search Console and verify ownership, ideally with a domain property.</li>
<li>Open <strong>URL Inspection</strong>, paste your homepage address and read the result: whether the page is on Google and, if not, why.</li>
<li>Use <strong>Test live URL</strong> to see whether Google can fetch the page now, after any fixes.</li>
<li>Click <strong>Request indexing</strong> for the homepage and your most important pages.</li>
<li>Submit your sitemap under <strong>Sitemaps</strong>, using the full sitemap address.</li>
<li>Check the <strong>Pages</strong> report over the following days to see which pages are indexed and which are excluded.</li>
</ol>

<h2 id="how-long">How Long Does It Take to Appear on Google?</h2>
<p>There is no fixed time. Many new sites appear within a few days of submitting a sitemap and requesting indexing; others take a few weeks. Google decides what and when to crawl. Requesting indexing repeatedly does not speed it up. If several weeks pass with no pages indexed and URL Inspection shows no blocker, look at the content and the site's discoverability.</p>

<h2 id="content-quality">Why Might Google Crawl a Page but Not Index It?</h2>
<p>Search Console sometimes reports "Crawled, currently not indexed" or "Discovered, currently not indexed". For new small sites, this often means pages have very little unique text, or several pages are near-copies of each other, such as area pages with only the city name changed. Add genuinely useful content to key pages: what you offer, prices or ranges, photos, and answers to customers' questions. Merge thin pages into stronger ones. Google's helpful content guidance describes what it looks for.</p>

<h2 id="discovery">Helping Google Discover a New Business</h2>
<ul>
<li>Create or update your Google Business Profile with the website link.</li>
<li>Add the website to your WhatsApp Business, Facebook, Instagram and LinkedIn profiles.</li>
<li>Get listed in genuine directories and associations relevant to your trade.</li>
<li>Ask suppliers or partners who already link to businesses like yours to include you.</li>
</ul>
<p>Avoid buying links or joining link schemes; they break Google's spam policies and can hurt a new site badly.</p>

<h2 id="redesign">Was It Indexed Before a Redesign?</h2>
<p>If an old site was on Google and disappeared after a new version launched, the cause is usually different: changed URLs without redirects, a noindex left on, or a domain change. Our guide on <a href="/digital/blog/new-website-without-losing-google-traffic">launching a new website without losing Google traffic</a> covers that case.</p>

<h2 id="help">When to Get Help</h2>
<p>If you have checked the settings above and the site is still not indexed after a few weeks, a technical review can find less obvious problems such as redirect loops, server errors or JavaScript rendering issues. Every site we build launches with these checks done and Search Console set up; see our <a href="/digital/business-websites">business website packages</a>, or ask us to review an existing site. Ongoing checks are part of maintenance from {P['maint']} a month.</p>
""",
    faqs=[
        ("Why is my new website not showing on Google?",
         "Usually because Google has not discovered it yet, or a setting is blocking it. Check for a noindex tag, a WordPress 'discourage search engines' setting, a robots.txt block or password protection. Then add the site to Search Console, submit a sitemap and request indexing for the homepage."),
        ("How do I check if Google has indexed my website?",
         "Search site:yourdomain on Google to see indexed pages, then use URL Inspection in Google Search Console for a definite answer on any page. URL Inspection also explains why a page is not indexed and lets you test the live page after fixing problems."),
        ("How long does Google take to index a new website?",
         "There is no fixed time. Many new sites appear within a few days of submitting a sitemap and requesting indexing, while others take a few weeks. Requesting indexing repeatedly does not speed it up. If weeks pass with no indexing and no blockers, review content quality and discoverability."),
        ("What does crawled but not indexed mean in Search Console?",
         "Google visited the page but chose not to include it for now. On small new sites this often means the page has little unique content or closely duplicates other pages. Add useful, specific information, merge near-identical pages and request indexing again after improving them."),
        ("Does submitting a sitemap guarantee my site appears on Google?",
         "No. A sitemap helps Google discover your pages, but Google still decides what to crawl and index. Make sure pages are not blocked, have useful content and are linked from your homepage and menu. A Google Business Profile and genuine links also help discovery."),
        ("Can a developer's setting stop my site appearing on Google?",
         "Yes. Developers often switch on noindex or 'discourage search engines' during development so unfinished pages stay out of search. If it is not switched off at launch, Google will not index the site. Ask your developer to confirm, or check the page source and WordPress reading settings."),
        ("Nayi website Google par kyun nahi aa rahi?",
         "Aksar developer ki lagai hui noindex setting launch ke baad bhi lagi reh jati hai, ya Google ne website ab tak dhoondi hi nahi. Search Console mein site add karein, URL Inspection chalayein, sitemap submit karein aur indexing request karein. Aam tor par kuch din se kuch hafte lagte hain."),
    ],
    sources=[
        ("Google Search Console Help: URL Inspection tool", "https://support.google.com/webmasters/answer/9012289"),
        ("Google Search Central: Block search indexing with noindex", "https://developers.google.com/search/docs/crawling-indexing/block-indexing"),
        ("Google Search Central: Introduction to robots.txt", "https://developers.google.com/search/docs/crawling-indexing/robots/intro"),
        ("Google Search Central: Sitemaps overview", "https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview"),
        ("Google Search Central: Ask Google to recrawl your URLs", "https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl"),
        ("Google Search Central: Creating helpful, reliable, people-first content", "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"),
    ],
    method="We followed Google's own documentation on indexing, noindex, robots.txt, sitemaps and recrawl requests, and the causes we most often find when reviewing newly launched sites. Prices come from our published packages. Sources checked on 3 November 2026.",
    related=["get-business-website-on-google", "seo-ready-website-checklist", "new-website-without-losing-google-traffic", "website-launch-checklist"],
    service_links=[("/digital/business-websites", "Business website packages"), ("/digital/contact", "Get a written quote")],
    cta="Launched a site that Google still cannot find?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20websites%20not%20showing%20on%20Google.%20Can%20you%20check%20mine%3F",
)
