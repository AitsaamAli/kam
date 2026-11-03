import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=238,
    slug="multi-location-business-website",
    title="Multi Location Website for Branches and Cities",
    h1="Multi Location Website for a Business With Several Branches or Cities",
    crumb="Multi Location Website",
    description="How to build a multi location website: branch pages that are genuinely useful rather than doorways, one Google Business Profile per branch, and the right schema.",
    keyword="multi location website",
    cluster=["branch pages website", "multiple locations seo", "franchise website structure",
             "location page content", "business profile per branch"],
    category="Planning & Launch",
    published="2026-11-03", published_h="3 November 2026",
    updated="2026-11-03", updated_h="3 November 2026",
    answer=(f"A multi location website needs one real page per branch, each with its own address, hours, phone, photos, team and services available there, plus a store locator and one Google Business Profile per branch. "
            f"Avoid copying the same page with only the city name changed. Branch-ready builds start from {P['business']}."),
    takeaways=[
        "Create a page only for branches that physically exist, each with genuinely local details.",
        "Copied pages that change only the city name are doorway pages and can hurt the whole site.",
        "Give every branch its own Google Business Profile with matching name, address and phone.",
        "Add LocalBusiness structured data per branch page, nested under the main organisation.",
        "A store locator helps visitors find the nearest branch; keep hours and holiday timings current.",
    ],
    body=f"""
<h2 id="problem">The Multi Location Website Problem</h2>
<p>A pharmacy chain with eight branches in Lahore, a school with campuses in three cities, a car workshop with outlets in Rawalpindi and Islamabad: each needs customers to find the right branch quickly. The common mistake is creating dozens of nearly identical pages, one per area or city, with only the name swapped. Google calls these doorway pages, and its spam policies warn against them. A good multi location website does the opposite: fewer pages, each one genuinely useful to someone visiting that branch.</p>

<h2 id="branch-page">What Should Each Branch Page Contain?</h2>
<table>
<tr><th>Element</th><th>Why it matters</th></tr>
<tr><td>Full address and map</td><td>The first thing a visitor needs</td></tr>
<tr><td>Phone and WhatsApp for that branch</td><td>Calls reach the right staff</td></tr>
<tr><td>Opening hours and holiday timings</td><td>Avoids wasted trips</td></tr>
<tr><td>Photos of that branch, inside and outside</td><td>Helps people recognise it</td></tr>
<tr><td>Services or stock available there</td><td>Not every branch offers everything</td></tr>
<tr><td>Branch manager or team</td><td>Adds a local, human touch</td></tr>
<tr><td>Parking, landmarks and directions</td><td>Practical details unique to the location</td></tr>
<tr><td>Reviews from that branch's customers</td><td>Local proof of quality</td></tr>
</table>
<p>These details make each page different in substance, not just in name. If you cannot write that much about a location, it may not need its own page.</p>

<h2 id="doorways">Why Do Copied City Pages Hurt?</h2>
<p>Creating pages for areas where you have no branch, or copying the same text across many city pages, is a tactic Google's spam policies specifically address. It can lower trust in the whole site, not only those pages. If you serve customers in areas without a branch, such as home delivery across Lahore, describe your service areas on one page instead of creating a page for each neighbourhood. Our guide to <a href="/digital/blog/google-business-profile-pakistan">Google Business Profile in Pakistan</a> explains how service areas work on Maps.</p>

<h2 id="gbp">How Should Google Business Profiles Work for Several Branches?</h2>
<p>Each physical branch that serves customers in person should have its own Google Business Profile. Use the same business name pattern, the branch's own address and phone, accurate hours and the correct category. Link each profile to its branch page on the website, not just the homepage. Businesses with many locations can manage profiles together as a group. Keep the name, address and phone identical between the profile and the branch page.</p>

<h2 id="schema">Structured Data for Branches</h2>
<p>Add LocalBusiness structured data, or a more specific type such as a store or medical clinic, to each branch page with its own address, phone, hours and coordinates. Connect each branch to the parent organisation. This helps search engines understand that the branches belong to one business. Our guide to <a href="/digital/blog/schema-markup-business-websites">schema markup for business websites</a> explains the format, and Google's Rich Results Test checks it.</p>

<h2 id="locator">Store Locator and Navigation</h2>
<p>A branch finder page with a list grouped by city, a map and a "nearest branch" option helps visitors on phones. Put a "Find a branch" link in the main menu. On each service page, mention which branches offer it. Avoid making visitors pick a city before they can see anything, which slows everyone down.</p>

<h2 id="keeping-current">Keeping Branch Details Current</h2>
<p>Outdated hours and closed branches still listed online are the biggest frustration for customers. Assign one person to update branch pages and Business Profiles together whenever hours, phone numbers or services change, and before Ramadan, Eid and public holidays. When a branch closes, mark it closed on the profile and redirect its page to the nearest branch.</p>

<h2 id="cost">What Does a Multi Location Website Cost?</h2>
<p>A business with a few branches fits our business package at {P['business']}, including branch pages, a locator and structured data. Large chains with many branches, stock by branch or booking per location may need custom development through our <a href="/digital/web-app-development">web app development service</a>. If your branches are run by separate owners, see our guide to <a href="/digital/blog/franchise-website-structure">franchise website structure</a>.</p>
""",
    faqs=[
        ("Should every branch have its own page on the website?",
         "Yes, every physical branch that serves customers should have its own page with its address, map, phone, hours, photos, services available there and local details such as parking. Do not create pages for areas where you have no branch; describe service areas on one page instead."),
        ("Are city landing pages bad for SEO?",
         "Copied pages that change only the city name, especially for places where you have no branch, are treated by Google as doorway pages and can lower trust in the whole site. Pages for real branches with genuinely local content are fine and helpful."),
        ("Does each branch need a separate Google Business Profile?",
         "Each physical branch that serves customers in person should have its own profile with its own address, phone and hours, linked to its branch page on the website. Keep the business name pattern consistent and the details identical between the profile and the website."),
        ("What schema should a multi-branch business use?",
         "Add LocalBusiness structured data, or a more specific type such as a store or clinic, to each branch page with its address, phone, hours and coordinates, and connect each branch to the parent organisation. Test the markup with Google's Rich Results Test."),
        ("How do I handle a branch that closes?",
         "Mark it as permanently closed on its Google Business Profile, remove it from the branch finder, and redirect its page to the nearest open branch or the branch finder with a 301. Tell regular customers where to go instead, by WhatsApp or a notice."),
        ("What does a multi location business website cost?",
         f"A business with a few branches fits our business package at {P['business']}, including branch pages, a branch finder and structured data. Large chains with many branches, stock by branch or bookings per location may need custom development, quoted after we understand how the branches operate."),
        ("Kai branches wale business ki website kaise banayein?",
         "Har asal branch ka alag page banayein jis mein pata, map, phone, timings, us branch ki tasveerein aur wahan ki services hon. Har branch ki apni Google Business Profile ho. Sirf shehar ka naam badal kar ek jaise pages na banayein, Google inhein doorway pages samajhta hai."),
    ],
    sources=[
        ("Google Search Central: Spam policies (doorway pages)", "https://developers.google.com/search/docs/essentials/spam-policies"),
        ("Google Search Central: LocalBusiness structured data", "https://developers.google.com/search/docs/appearance/structured-data/local-business"),
        ("Google Business Profile Help: Tips to improve your local ranking", "https://support.google.com/business/answer/7091"),
        ("Schema.org: LocalBusiness", "https://schema.org/LocalBusiness"),
        ("Google Rich Results Test", "https://search.google.com/test/rich-results"),
    ],
    method="We followed Google's spam policies on doorway pages, its local business structured data documentation and Business Profile guidance, and the branch details customers most often look for. Prices come from our published packages. Sources checked on 3 November 2026.",
    related=["google-business-profile-pakistan", "schema-markup-business-websites", "franchise-website-structure", "lahore-web-design-prices-by-area"],
    service_links=[("/digital/business-websites", "Business website packages"), ("/digital/web-app-development", "Web app development")],
    cta="Running several branches and want each one easy to find?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20multi%20location%20websites.%20We%20have%20several%20branches.",
)
