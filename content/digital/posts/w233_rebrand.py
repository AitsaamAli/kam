import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=233,
    slug="rebrand-website-after-business-name-change",
    title="Rebrand Your Website After a Business Name Change",
    h1="Changed Your Business Name? How to Rebrand Your Website Without Losing Customers",
    crumb="Rebrand Website",
    description="How to rebrand a website after a business name change: moving to a new domain with redirects, updating Google and social profiles, and telling customers clearly.",
    keyword="rebrand website",
    cluster=["business name change website", "new domain after rebrand", "rebranding seo",
             "change of address tool google", "announce new business name"],
    category="Planning & Launch",
    published="2026-11-03", published_h="3 November 2026",
    updated="2026-11-03", updated_h="3 November 2026",
    answer=(f"To rebrand a website after a name change, keep the old domain, move to the new one with permanent 301 redirects page by page, tell Google through Search Console's Change of Address tool, and update every profile and listing. "
            f"Done carefully, most traffic transfers within a few weeks to a few months."),
    takeaways=[
        "Never let the old domain expire; keep renewing it for years so redirects keep working.",
        "Redirect every old page to its matching new page with a 301, not everything to the homepage.",
        "Use Search Console's Change of Address tool after the redirects are live.",
        "Update your Google Business Profile, social profiles, directories, email signatures and printed material.",
        "Tell customers directly and keep the old name visible for a while, such as 'formerly known as'.",
    ],
    body=f"""
<h2 id="why">Why Rebranding a Website Needs a Plan</h2>
<p>Businesses change names for good reasons: a partnership ends, the business expands beyond its original product, a trademark conflict appears, or the old name no longer fits. Customers, Google and partners all know you by the old name, though. If the website simply switches to a new domain overnight, old links break, search rankings drop, emails bounce and regular customers wonder whether you closed. A planned rebrand website project protects all of these.</p>

<h2 id="decide">Do You Need a New Domain?</h2>
<table>
<tr><th>Situation</th><th>Recommended approach</th></tr>
<tr><td>Name changes, domain still fits</td><td>Keep the domain, update branding on the site only</td></tr>
<tr><td>Old domain contains the old name</td><td>Move to a new domain with full redirects</td></tr>
<tr><td>Legal or trademark reason to stop using the old name</td><td>Move to a new domain quickly, keep redirects, take legal advice on the old name</td></tr>
<tr><td>Two businesses merging</td><td>Choose one domain, redirect the other's pages to the closest equivalents</td></tr>
</table>
<p>If you do need a new domain, register it in your own name and check it is not used elsewhere. Our guide to <a href="/digital/blog/domain-and-hosting-price-in-pakistan">domain and hosting prices in Pakistan</a> covers registration.</p>

<h2 id="redirects">How Should Redirects Be Set Up When You Rebrand a Website?</h2>
<p>A 301 redirect tells browsers and Google that a page has moved permanently. Make a list of every URL on the old site, including blog posts and product pages, and map each to its matching page on the new domain. Redirect page to page, not everything to the new homepage, because Google treats mass homepage redirects as missing pages. Test a sample of old URLs after launch. Google's documentation on site moves explains the process in detail, and our guide to <a href="/digital/blog/new-website-without-losing-google-traffic">launching a new website without losing Google traffic</a> covers redirect mapping step by step.</p>

<h2 id="google">Telling Google About the Move</h2>
<ol>
<li>Verify both the old and new domains in Google Search Console.</li>
<li>Once redirects are live, use the <strong>Change of Address</strong> tool from the old property.</li>
<li>Submit the new sitemap in the new property.</li>
<li>Watch the Pages report and performance data for both properties over the following weeks.</li>
</ol>
<p>Rankings often wobble for a few weeks during a domain move and then settle. Keep the redirects in place for at least a year, and ideally keep the old domain renewed indefinitely.</p>

<h2 id="profiles">Update Everything Outside the Website</h2>
<ul>
<li>Google Business Profile: change the name to the new legal or trading name, keeping it accurate.</li>
<li>WhatsApp Business, Facebook, Instagram, LinkedIn and YouTube names and links.</li>
<li>Business directories, marketplace stores and supplier listings.</li>
<li>Email addresses: set up the new domain and forward the old addresses for a long period.</li>
<li>Invoices, letterheads, sign boards, packaging and vehicle branding.</li>
</ul>

<h2 id="customers">How Do You Tell Customers About the New Name?</h2>
<p>Announce the change directly by WhatsApp broadcast, email and social media, explaining what changed and what stays the same, such as the team, products, address and phone number. On the new website, add a short line such as "formerly known as" in the footer and on the About page for several months, so people searching the old name understand they are in the right place. Our guide to <a href="/digital/blog/about-us-page-that-builds-trust">About pages that build trust</a> helps with the wording.</p>

<h2 id="cost">What Does a Rebrand Cost?</h2>
<p>If only the branding changes on the same site, the work is usually small. A move to a new domain with redirect mapping, Search Console set-up and profile updates is a larger job, especially for sites with many pages. A full redesign at the same time is priced like a new site, starting with our business package at {P['business']}. See our <a href="/digital/business-websites">business website packages</a> or ask for a quote.</p>
""",
    faqs=[
        ("Will changing my business name hurt my Google rankings?",
         "It can for a few weeks if you move to a new domain, but careful 301 redirects from every old page to its matching new page, plus Search Console's Change of Address tool, usually let rankings settle on the new domain. Keep the old domain renewed so redirects keep working."),
        ("Do I need a new domain when I rename my business?",
         "Only if the old domain contains the old name or you have a legal reason to stop using it. If the domain still fits, keep it and update the branding on the site. If you move, register the new domain in your own name and redirect every old page."),
        ("How long should I keep redirects after a rebrand?",
         "At least a year, and ideally for as long as you can keep the old domain renewed. Old links in directories, social posts and other websites continue sending visitors for years, and removing redirects early turns those visits into errors and lost customers."),
        ("What is Google's Change of Address tool?",
         "It is a feature in Google Search Console that tells Google your site has moved to a new domain. You use it from the old domain's property after setting up 301 redirects and verifying both domains. It helps Google transfer signals to the new address faster."),
        ("How do I tell customers about our new business name?",
         "Announce it by WhatsApp broadcast, email and social media, explaining what changed and what stays the same. Add a 'formerly known as' line on the new website's footer and About page for several months, and update your Google Business Profile so searches for either name find you."),
        ("What does it cost to rebrand a business website?",
         f"Changing branding on the same site is usually a small job. Moving to a new domain with redirect mapping, Search Console set-up and profile updates takes more work. A full redesign at the same time is priced like a new site, from our business package at {P['business']}."),
        ("Business ka naam badal gaya, website ka kya karein?",
         "Purana domain kabhi expire na hone dein. Naye domain par har purane page ka 301 redirect lagayein, Search Console mein Change of Address tool istemal karein, aur Google Business Profile, social media aur directories mein naam update karein. Customers ko WhatsApp par naye naam ke baare mein batayein."),
    ],
    sources=[
        ("Google Search Central: Site moves with URL changes", "https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes"),
        ("Google Search Central: Redirects and Google Search", "https://developers.google.com/search/docs/crawling-indexing/301-redirects"),
        ("Google Search Console Help: Change of Address tool", "https://support.google.com/webmasters/answer/9370220"),
        ("Google Business Profile Help: Edit your Business Profile", "https://support.google.com/business/answer/3039617"),
        ("WIPO: Trademarks", "https://www.wipo.int/trademarks/en/"),
    ],
    method="We followed Google's documentation on site moves, redirects and the Change of Address tool, and the profile updates businesses most often forget during a rename. Prices come from our published packages. Sources checked on 3 November 2026.",
    related=["new-website-without-losing-google-traffic", "website-redesign-cost", "about-us-page-that-builds-trust", "switch-com-to-pk-domain"],
    service_links=[("/digital/business-websites", "Business website packages"), ("/digital/contact", "Get a written quote")],
    cta="Renaming your business and worried about losing customers online?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20rebranding%20a%20website.%20We%20are%20changing%20our%20name.",
)
