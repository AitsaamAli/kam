import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=94,
    slug="new-website-without-losing-google-traffic",
    title="Website Redesign Without Losing Traffic: A Safe Move Plan",
    h1="Website Redesign Without Losing Traffic: Redirect Maps and Google's Site-Move Steps",
    crumb="Redesign Without Losing Traffic",
    description="Plan a website redesign without losing traffic: build a redirect map, use permanent redirects, follow Google's site-move steps and monitor Search Console.",
    keyword="website redesign without losing traffic",
    cluster=["website migration seo", "redirect map", "change website without losing ranking", "301 redirect old pages",
             "domain change seo", "nayi website par traffic kaise bachayen"],
    category="Fix a Problem",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("A website redesign without losing traffic depends on one document: a redirect map that sends every old address to its best new "
            "equivalent with a permanent 301 or 308 redirect. Google advises keeping redirects for at least 1 year, updating internal links "
            "and sitemaps, and expecting some ranking movement for a few weeks."),
    takeaways=[
        "Most traffic losses after a redesign come from old addresses that no longer work, not from the new design.",
        "List every old URL that gets traffic or links, and map each one to its closest new page.",
        "Use server-side permanent redirects, and avoid sending everything to the home page.",
        "Google advises keeping redirects for at least one year after a move.",
        "Monitor Search Console and analytics closely for several weeks after launch.",
    ],
    body=f"""
<h2 id="why-traffic-drops">How Do You Plan a Website Redesign Without Losing Traffic?</h2>
<p>A redesign often changes page addresses: /services.html becomes /services/, product pages move into new categories, or the whole site moves to a new domain. Google has the old addresses indexed, other websites link to them, and customers have them bookmarked. If those addresses return "page not found", the traffic and trust built over years disappear overnight.</p>
<p>A website redesign without losing traffic is mostly careful planning, done before launch. This guide covers the process; if you want to know what a redesign costs, read our <a href="/digital/blog/website-redesign-cost">website redesign cost guide</a>.</p>

<h2 id="redirect-map">How Do You Build a Redirect Map?</h2>
<p>A redirect map is a spreadsheet listing every old address and where it should go on the new site. Google's site-move guidance suggests collecting old URLs from your sitemaps, analytics, server logs and content system.</p>
<table>
<tr><th>Old URL</th><th>New URL</th><th>Notes</th></tr>
<tr><td>/services.html</td><td>/services/</td><td>Same content, new address</td></tr>
<tr><td>/dental-implants-lahore.html</td><td>/services/dental-implants/</td><td>Top traffic page; check title kept</td></tr>
<tr><td>/blog/2019/teeth-whitening-tips</td><td>/guides/teeth-whitening/</td><td>Updated article</td></tr>
<tr><td>/old-offer-page</td><td>/offers/</td><td>Closest equivalent</td></tr>
<tr><td>/discontinued-product</td><td>Returns 404 or 410</td><td>No equivalent; do not force to home page</td></tr>
</table>
<p>Example template; your own map should cover every page that gets search traffic, has links from other sites or appears in printed material.</p>

<h2 id="redirect-rules">Which Redirects Should You Use?</h2>
<p>Google says permanent redirects, 301 or 308, signal that the new address should be shown in results, and that server-side redirects are the most reliable. Meta refresh and JavaScript redirects are fallbacks. Its site-move guidance adds:</p>
<ul>
<li>redirect each old URL directly to its final new URL, avoiding chains</li>
<li>do not send many unrelated old pages to the home page</li>
<li>return a proper 404 or 410 for content that has no replacement</li>
<li>keep the redirects for as long as possible, generally at least one year</li>
</ul>

<h2 id="content-changes">What If You Are Rewriting the Content Too?</h2>
<p>Redirects protect addresses, but rankings also depend on what is on each page. If a top page currently ranks for "dental implants in Lahore", the new version should still answer that search as fully as before, with the same key details, headings and FAQs, or better ones. Merging several pages into one can work well, as long as the new page covers everything the old ones did and each old address redirects to it. Removing popular content without a replacement is the change most likely to cost traffic.</p>

<h2 id="before-launch">What Should Happen Before Launch?</h2>
<ol>
<li>Record current traffic and top pages from analytics and Search Console as a baseline.</li>
<li>Keep the titles, headings and content of top pages unless there is a reason to change them.</li>
<li>Update internal links, canonical tags and the new sitemap to use new URLs.</li>
<li>Test every redirect on the staging site with a crawler or spreadsheet check.</li>
<li>Check that the staging site is blocked from Google, and that the block is removed at launch.</li>
</ol>

<h2 id="launch-day">What Should Happen on Launch Day and After?</h2>
<ul>
<li>Switch on redirects at the same moment the new site goes live.</li>
<li>Submit the new sitemap in Search Console and remove the old one.</li>
<li>For a domain change, verify both domains and use Search Console's Change of Address tool.</li>
<li>Watch Search Console for crawl errors and 404s daily for the first two weeks, then weekly.</li>
<li>Make sure the server can handle extra crawling, which Google says increases after a move.</li>
</ul>
<p>Google warns rankings may fluctuate for weeks or longer. A temporary dip is normal; a steep, lasting drop usually means missing redirects.</p>

<h2 id="what-we-offer">What We Would Build for You</h2>
<p>Every redesign we do includes a full redirect map, testing on staging, sitemap and Search Console updates, and post-launch monitoring. A redesigned business website of up to 10 pages starts from {P['business']}, and larger sites or stores are scoped after reviewing your current URLs. See our <a href="/digital/business-websites">business websites</a> service, the <a href="/digital/blog/website-launch-checklist">website launch checklist</a> and the <a href="/digital/blog/get-business-website-on-google">guide to getting your website on Google</a>.</p>
""",
    faqs=[
        ("Will I lose Google rankings if I redesign my website?",
         "Not necessarily. Most losses come from old page addresses that stop working. With a complete redirect map, permanent server-side redirects, unchanged or improved content on top pages and updated sitemaps, rankings usually settle after some fluctuation. Google notes that changes can take weeks or longer to settle."),
        ("What is a redirect map?",
         "A redirect map is a spreadsheet listing every old URL on your website and the new URL it should redirect to. It covers pages with search traffic, links from other sites or printed references. Pages with no equivalent should return a proper not-found response rather than redirect to the home page."),
        ("Should I use 301 or 302 redirects when moving my website?",
         "Use permanent redirects, 301 or 308, for a redesign or move. Google says permanent redirects signal that the new URL should be shown in results, while temporary ones, such as 302, keep the old URL as the main one. Server-side redirects are the most reliable."),
        ("How long should I keep redirects after a website move?",
         "Google's site-move guidance says to keep redirects for as long as possible, generally at least one year. Many businesses keep them indefinitely, because old links from other websites, emails and printed material keep sending visitors to the old addresses for years."),
        ("Can I redirect all old pages to my new home page?",
         "Avoid it. Google advises against sending many unrelated old URLs to one page such as the home page, because it treats them more like missing pages. Redirect each old page to its closest new equivalent, and let pages with no replacement return a not-found response."),
        ("Nayi website banwate hue Google traffic kaise bachayen?",
         "Purani website ke har page ka address aur us ka naya address aik list mein likhein aur 301 redirect lagayen. Sab ko home page par na bhejein. Launch par naya sitemap Search Console mein dein aur kuch hafte errors check karte rahein. Redirects kam az kam aik saal rakhein."),
    ],
    sources=[
        ("Google Search Central — Site moves with URL changes", "https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes"),
        ("Google Search Central — Redirects and Google Search", "https://developers.google.com/search/docs/crawling-indexing/301-redirects"),
        ("Google Search Central — Sitemaps overview", "https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview"),
        ("Google Search Console Help — About Search Console", "https://support.google.com/webmasters/answer/9128668"),
        ("Internet Archive — Wayback Machine (find old URLs)", "https://web.archive.org/"),
    ],
    method=("Site-move steps, the one-year redirect advice, redirect types and expected fluctuation come from Google Search Central's site-move "
            "and redirects pages, checked 29 October 2026. The redirect map is an illustrative template. This guide covers process; costs "
            "are in our separate redesign cost guide. Prices are our own."),
    related=["get-business-website-on-google", "website-redesign-cost", "website-launch-checklist", "seo-ready-website-checklist"],
    service_links=[("/digital/business-websites", "Redesigns with redirect maps"), ("/digital/contact", "Plan your redesign")],
    cta="Planning a redesign?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20redesigning%20without%20losing%20traffic%20and%20need%20help",
)
