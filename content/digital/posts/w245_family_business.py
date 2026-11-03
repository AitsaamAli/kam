import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=245,
    slug="inherited-family-business-website",
    title="Modernising Your Family Business Website",
    h1="Taking Over the Family Business: How to Modernise Its Family Business Website",
    crumb="Family Business Website",
    description="Taking over a family business? How to modernise its website while respecting the old name, recovering old accounts and moving to new systems in planned stages.",
    keyword="family business website",
    cluster=["old family business online", "modernise family shop website", "recover old website accounts",
             "heritage brand website", "second generation business online"],
    category="Planning & Launch",
    published="2026-11-03", published_h="3 November 2026",
    updated="2026-11-03", updated_h="3 November 2026",
    answer=(f"Modernising a family business website starts with recovering control of the old domain, email and listings, then keeping what customers recognise, such as the name and history, while updating the design, content and ordering in planned stages. "
            f"Most family businesses complete the change over 3 to 6 months."),
    takeaways=[
        "First, find out who controls the domain, hosting, email, Google Business Profile and social pages.",
        "Keep the family name, founding year and story; they are trust signals new competitors do not have.",
        "Modernise in stages: first the website, then online ordering or booking, then internal systems.",
        "Involve the older generation in decisions about the name and history, even if you lead the technology.",
        "Keep old phone numbers and addresses working, and redirect old web pages, so loyal customers are not lost.",
    ],
    body=f"""
<h2 id="situation">The Second-Generation Challenge</h2>
<p>A son or daughter returns from university or a job abroad to run the family shop, factory or practice. The business has decades of goodwill, loyal customers and a respected name in its bazaar or industry. Its website, if there is one, was built years ago by a relative or a local shop, and nobody remembers the password. The new generation wants online orders, social media and modern systems; the older generation worries about losing what made the business successful. A good family business website modernisation respects both.</p>

<h2 id="recover">How Do You Recover Old Accounts?</h2>
<table>
<tr><th>Account</th><th>How to find it</th><th>How to recover it</th></tr>
<tr><td>Domain</td><td>ICANN Lookup or the .pk registrar shows the registrant</td><td>Contact the registrar with business documents; update the registrant to the business</td></tr>
<tr><td>Hosting</td><td>Old invoices, bank statements, or the person who built the site</td><td>Ask the host to verify ownership and reset access</td></tr>
<tr><td>Email</td><td>Who receives mail for the business domain?</td><td>Move mailboxes to an account the business controls</td></tr>
<tr><td>Google Business Profile</td><td>Search the business on Google Maps</td><td>Request ownership through Google if the old owner is unreachable</td></tr>
<tr><td>Social pages</td><td>Which family member or employee created them?</td><td>Add yourself as admin before anyone leaves</td></tr>
</table>
<p>Do this before any redesign. Our guide to <a href="/digital/blog/who-owns-your-website">who owns your website</a> explains each account, and our guide to <a href="/digital/blog/taking-over-website-from-old-developer">taking over a website from an old developer</a> covers technical handovers.</p>

<h2 id="keep">What Should You Keep From the Old Business?</h2>
<p>The things customers recognise are valuable: the name, the founding year, the founder's story, the original location, a signature product, even a familiar colour or sign. These are trust signals new competitors cannot copy. Put them on the About page and in the footer, with old photos if the family has them. Many customers search for the business by its old name or the founder's name, so keep those words on the site.</p>

<h2 id="stages">How Should You Modernise a Family Business Website in Stages?</h2>
<ol>
<li><strong>Stage 1, the website:</strong> a clean, mobile-friendly site with accurate products or services, prices, contact details, history and Google Business Profile.</li>
<li><strong>Stage 2, customer-facing tools:</strong> online ordering, a catalogue, booking or WhatsApp ordering, depending on the business.</li>
<li><strong>Stage 3, internal systems:</strong> stock, invoicing or customer records, once staff are comfortable with the first two stages.</li>
</ol>
<p>Changing everything at once overwhelms long-serving staff and risks confusing loyal customers. Staged change also spreads the cost.</p>

<h2 id="family">Bringing the Family Along</h2>
<p>Show the older generation what customers see when they search for the business today, and what competitors' websites look like. Involve them in decisions about the name, history and photos. Explain each change in terms of results, such as more orders from younger customers or fewer phone calls about prices. When elders feel the business's identity is being protected, they usually support the modernisation.</p>

<h2 id="customers">How Do You Avoid Losing Loyal Customers?</h2>
<p>Keep old phone numbers working, and if the shop moves, keep the old address listed with directions to the new one for a while. If the old website had pages that people visited, redirect each one to its new equivalent. Tell regular customers about the new website and ordering options personally, by WhatsApp or at the counter. Our guide to <a href="/digital/blog/new-website-without-losing-google-traffic">launching a new website without losing Google traffic</a> explains redirects.</p>

<h2 id="cost">What Does Modernising a Family Business Website Cost?</h2>
<p>Stage 1 usually fits our starter package at {P['starter']} or business package at {P['business']}, depending on the size of the business and catalogue. Online stores start at {P['store']}, and internal systems are quoted through our <a href="/digital/web-app-development">web app development service</a>. We can help recover old accounts as part of the project.</p>
""",
    faqs=[
        ("How do I recover the old website of my family business?",
         "Find out who controls the domain using ICANN Lookup or the .pk registrar, then contact the registrar and hosting company with business documents to update ownership and reset access. Do the same for email, Google Business Profile and social pages before starting any redesign."),
        ("Should a family business keep its old name online?",
         "Usually yes. The name, founding year and founder's story are trust signals new competitors cannot copy, and many customers search by the old name. Keep them on the About page and footer, with old photos if available, while modernising the design and content."),
        ("How should a family business modernise its website?",
         "In planned stages. First build a clean, mobile-friendly site with accurate products, prices, contact details and the business history. Then add customer tools such as online ordering, booking or a catalogue. Finally move internal systems like stock and invoicing, once staff are comfortable."),
        ("How do I convince older family members to modernise the website?",
         "Show them what customers see when searching for the business today and what competitors offer. Involve them in decisions about the name, history and photos, and explain each change through results such as more orders or fewer calls. Protecting the business's identity earns their support."),
        ("How can I modernise without losing loyal customers?",
         "Keep old phone numbers working, show the old address with directions if the shop moves, redirect old web pages to their new equivalents, and tell regular customers personally about the new website and ordering options. Familiar details should stay visible throughout the change."),
        ("What does modernising a family business website cost?",
         f"The first stage, a new website, usually fits our starter package at {P['starter']} or business package at {P['business']}. Online stores start at {P['store']}, and internal systems are quoted separately. Account recovery can be included in the project."),
        ("Khandani business ki purani website ko naya kaise banayein?",
         "Pehle domain, hosting, email aur Google Business Profile ka control wapis lein. Phir business ka naam, shuru hone ka saal aur bani ki kahani rakh kar nayi website banayein. Online orders aur andaruni systems ko marhala war shamil karein, aur purane customers ke phone number aur pate chalte rakhein."),
    ],
    sources=[
        ("ICANN Lookup: check domain registration details", "https://lookup.icann.org/"),
        ("PKNIC: .pk domain registry", "https://pknic.net.pk/"),
        ("Google Business Profile Help: Add or remove owners and managers", "https://support.google.com/business/answer/3403100"),
        ("Google Search Central: Redirects and Google Search", "https://developers.google.com/search/docs/crawling-indexing/301-redirects"),
        ("Web Archive: Wayback Machine", "https://web.archive.org/"),
    ],
    method="We followed the steps second-generation owners usually take when modernising a family business online, including account recovery through registrars and Google, and priced each stage from our published packages. Sources checked on 3 November 2026.",
    related=["who-owns-your-website", "taking-over-website-from-old-developer", "when-to-upgrade-your-website", "website-redesign-cost"],
    service_links=[("/digital/business-websites", "Business website packages"), ("/digital/web-app-development", "Web app development")],
    cta="Taking over the family business and ready to bring it online properly?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20modernising%20a%20family%20business%20website.%20I%20would%20like%20advice.",
)
