import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=243,
    slug="split-website-into-two-brands",
    title="Separate Websites for Two Businesses, or One?",
    h1="Separate Websites for Two Businesses or One Site? When to Split, With a Worked Example",
    crumb="Separate Websites for Two Businesses",
    description="Separate websites for two businesses, or one shared site? A decision table, SEO effects, costs, and how we kept our own two services apart.",
    keyword="separate websites for two businesses",
    cluster=["two brands one website", "split website", "sub-brand website",
             "subdomain or subfolder for second business", "keep two services separate online"],
    category="Planning & Launch",
    published="2026-11-03", published_h="3 November 2026",
    updated="2026-11-03", updated_h="3 November 2026",
    answer=(f"If you run 2 businesses, choose separate websites for two businesses when they serve different customers, need different reputations or may be sold separately. "
            f"Keep one website with clear sections when customers overlap and one strong domain helps both. "
            f"Either way, keep the two offers clearly apart so neither confuses the other's customers."),
    takeaways=[
        "Different customers, different trust needs or a possible future sale point towards separate websites.",
        "Overlapping customers and a shared team point towards one website with clearly separated sections.",
        "A section on the main domain shares its strength; a new domain starts from zero.",
        "Whichever you choose, avoid mixing the two offers in titles, menus and pages.",
        "Our own site keeps web development in a separate section from our tax services, with separate menus and no cross-linking.",
    ],
    body=f"""
<h2 id="question">The Question Many Owners Face</h2>
<p>A tax consultant starts offering web development. A furniture maker opens a café. A school starts a tuition academy. A clothing brand launches a separate men's line. At some point the owner asks whether the new business belongs on the existing website or needs its own. There is no single right answer, but there is a clear way to decide, based on customers, trust, the team and the future of each business.</p>

<h2 id="decide">How Do You Decide Between One Website and Separate Websites for Two Businesses?</h2>
<table>
<tr><th>Question</th><th>Points to one website</th><th>Points to two websites</th></tr>
<tr><td>Do the same customers buy both?</td><td>Yes, often together</td><td>No, completely different buyers</td></tr>
<tr><td>Does each need a different reputation?</td><td>No, one brand covers both</td><td>Yes, one could confuse trust in the other</td></tr>
<tr><td>Is the team the same?</td><td>Same people, same contact</td><td>Different teams and contacts</td></tr>
<tr><td>Might one be sold or spun off?</td><td>Unlikely</td><td>Possible</td></tr>
<tr><td>Is the existing site strong in search?</td><td>Yes, and the new business is related</td><td>The new business is unrelated to what it ranks for</td></tr>
<tr><td>Budget for two sites and their upkeep?</td><td>Limited</td><td>Available</td></tr>
</table>

<h2 id="seo">What Are the SEO Effects of Each Choice?</h2>
<p>A section on an established domain benefits from the domain's existing reputation, so new pages can be found sooner. However, if the two businesses are unrelated, mixing them can blur what the site is about, for both visitors and search engines. A new domain starts from nothing and has to earn its own reputation over time, but it can focus completely on one topic. A subdomain sits in between and is treated by Google much like a separate site in many cases. Google's guidance on site structure encourages organising content so users and search engines can understand it, which matters more than the technical choice.</p>

<h2 id="example">A Worked Example: How We Separated Our Two Services</h2>
<p>Kamboh Associates offers tax services and, separately, web development. We decided to keep web development in its own section of the same domain, under /digital, because it shares the company's name, office and reputation for reliability. At the same time, the two services serve different customers with different questions, so we kept them strictly apart: the web development pages have their own menu, footer, contact routes and blog, page titles and headings never mention the tax services, and the two sections do not link to each other. A tax client reading about filing deadlines never lands on a page about Shopify stores, and a business looking for a website never wades through tax content. This approach let the new service benefit from the domain while keeping each audience's experience focused.</p>

<h2 id="one-site">If You Keep One Website</h2>
<ul>
<li>Give each business its own clearly named section, menu and contact route.</li>
<li>Keep page titles and headings focused on the section's own topic.</li>
<li>Do not cross-promote heavily where customers do not overlap.</li>
<li>Track enquiries for each section separately in analytics.</li>
</ul>

<h2 id="two-sites">If You Split Into Two Websites</h2>
<ol>
<li>Register the new domain in the business's name.</li>
<li>Move the second business's pages to the new site and redirect old URLs page by page.</li>
<li>Create separate Google Business Profiles if each has its own location or service area.</li>
<li>Link between the sites only where it genuinely helps visitors.</li>
</ol>
<p>Our guide on <a href="/digital/blog/new-website-without-losing-google-traffic">launching a new website without losing Google traffic</a> explains the redirect steps.</p>

<h2 id="cost">What Does Each Option Cost?</h2>
<p>A new section on an existing site is usually cheaper than a second website, because hosting, design and maintenance are shared. A separate website is priced like any new site, from our starter package at {P['starter']} or business package at {P['business']}, plus its own domain and upkeep. See our <a href="/digital/business-websites">business website packages</a>, and if you have several branches rather than several businesses, read our guide to <a href="/digital/blog/multi-location-business-website">multi location websites</a>.</p>
""",
    faqs=[
        ("Should two different businesses share one website?",
         "Share one website when the same customers often buy from both, one brand and team cover both, and the existing site is strong in a related topic. Choose separate websites when customers, reputation needs or teams differ, or when one business may be sold or spun off later."),
        ("Is a subfolder or a new domain better for a second business?",
         "A subfolder on an established domain benefits from its existing reputation, which helps if the businesses are related. A new domain starts from zero but focuses on one topic, which suits unrelated businesses. A subdomain is often treated much like a separate site by Google."),
        ("Does mixing two unrelated businesses on one website hurt SEO?",
         "It can blur what the site is about for visitors and search engines, especially if titles, menus and pages mix the two offers. If you keep one site, give each business its own clearly separated section, menu, contact routes and focused page titles."),
        ("How do I split one website into two?",
         "Register the new domain in the business's name, move the second business's pages to it, redirect each old URL to its new page with a 301, create separate Google Business Profiles where needed, and link between the sites only where it genuinely helps visitors."),
        ("How does Kamboh Associates keep its services separate online?",
         "Our web development service sits in its own /digital section of the same domain, with its own menu, footer, contact routes and blog. Its titles and headings do not mention our other services, and the two sections do not link to each other, so each audience sees only what it came for."),
        ("Is a second website more expensive than a new section?",
         f"Usually yes, because a separate site needs its own domain, hosting, design and upkeep, while a section shares them. A separate website is priced like any new site, from our starter package at {P['starter']} or business package at {P['business']}."),
        ("Do businesses ke liye ek website ho ya do?",
         "Agar dono ke customer aksar ek hi hain aur ek brand dono ko cover karta hai to ek website mein alag alag sections kaafi hain. Agar customer, team ya shohrat alag hai, ya mustaqbil mein ek business bechna ho sakta hai, to alag website behtar hai. Har haal mein dono ko aapas mein mix na karein."),
    ],
    sources=[
        ("Google Search Central: SEO Starter Guide", "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"),
        ("Google Search Central: Site moves with URL changes", "https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes"),
        ("Google Search Central: Site names in search results", "https://developers.google.com/search/docs/appearance/site-names"),
        ("Google Business Profile Help: Tips to improve your local ranking", "https://support.google.com/business/answer/7091"),
    ],
    method="We set out the factors that decide whether two businesses should share a website, reviewed Google's guidance on site structure, site names and moves, and described our own set-up as a real example. Prices come from our published packages. Sources checked on 3 November 2026.",
    related=["multi-location-business-website", "new-website-without-losing-google-traffic", "rebrand-website-after-business-name-change", "software-house-own-website"],
    service_links=[("/digital/business-websites", "Business website packages"), ("/digital/contact", "Get a written quote")],
    cta="Running two businesses and unsure whether to split the website?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20one%20website%20or%20two.%20I%20would%20like%20advice.",
)
