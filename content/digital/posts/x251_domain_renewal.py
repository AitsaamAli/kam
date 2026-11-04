import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=251,
    slug="domain-renewal-charges-pakistan",
    title="Domain Renewal Price in Pakistan: .pk, .com.pk and .com",
    h1="Domain Renewal Price in Pakistan for .pk, .com.pk and .com Addresses",
    crumb="Domain Renewal Price Pakistan",
    description="The domain renewal price in Pakistan for .pk, .com.pk and .com, how PKNIC bills two years at a time, and the renewal traps that cost owners their address.",
    keyword="domain renewal price pakistan",
    cluster=["pk domain renewal fee", "com.pk renewal cost", "pknic renewal charges",
             "com domain renewal pakistan", "domain expiry warning"],
    category="Costs & Budgets",
    published="2026-11-04", published_h="4 November 2026",
    updated="2026-11-04", updated_h="4 November 2026",
    answer=("The domain renewal price in Pakistan for a .pk or .com.pk address is set by PKNIC: Rs 2,100 per year for registrants in Pakistan, billed for two years at a time (checked 4 November 2026). "
            ".com renewals are set by each registrar, usually in US dollars. The bigger risk than price is letting the renewal lapse."),
    takeaways=[
        "PKNIC lists Rs 2,100 per year for Pakistani registrants, charged for two years at a time, with payment possible for up to ten years.",
        "Registrants outside Pakistan pay PKNIC's foreign fee, listed as US$15.99 per domain per year.",
        ".com renewal prices vary by registrar; compare the renewal price, not the first-year offer.",
        "Most domain losses happen because renewal notices go to an old email address or a former developer.",
        "Keep the domain in your own name, turn on auto-renewal where available, and renew for several years.",
    ],
    body=f"""
<h2 id="pknic">What Is the Domain Renewal Price in Pakistan for .pk?</h2>
<p>Addresses ending in .pk, .com.pk, .org.pk and the other Pakistani extensions are run by PKNIC, the national registry. On its payment page, PKNIC lists a domain fee of Rs 2,100 per year for registrants based in Pakistan, charged on a biennial basis, meaning you pay for two years at a time. It also allows payment for up to ten years in advance. Registrants outside Pakistan are charged a separate foreign fee, listed as US$15.99 per domain per year. These figures were checked on 4 November 2026; PKNIC can change them, so confirm on its site before paying.</p>
<p>For a business, that works out to Rs 4,200 for each two-year renewal, or Rs 21,000 if you pay for the full ten years at once. PKNIC does not accept cash. Its page lists online payment by credit card, pre-paid cards sold by listed resellers, and cheques or bank drafts sent to its collection office in Lahore.</p>

<h2 id="com">How Is .com Renewal Priced?</h2>
<p>A .com domain is renewed through whichever registrar you bought it from. Each registrar sets its own price, usually in US dollars, so the rupee cost changes with the exchange rate. Many registrars advertise a low first-year price and charge much more at renewal. Before choosing a registrar, look at the renewal price on its official pricing page, and check whether privacy protection, which hides your personal details from public lookups, is included or charged extra.</p>

<h2 id="compare">Renewal Costs Side by Side</h2>
<table>
<tr><th>Extension</th><th>Who sets the price</th><th>Billing</th><th>What to watch</th></tr>
<tr><td>.pk and .com.pk</td><td>PKNIC</td><td>Two years at a time, up to ten</td><td>Renewal notices going to an old email</td></tr>
<tr><td>.com</td><td>Your registrar</td><td>Usually yearly, can be several years</td><td>Renewal higher than the first-year offer</td></tr>
<tr><td>Reseller packages</td><td>The reseller</td><td>Often bundled with hosting</td><td>Domain registered in the reseller's name</td></tr>
</table>

<h2 id="traps">Which Renewal Traps Cost Owners Their Domain?</h2>
<ul>
<li><strong>Old contact email.</strong> Renewal reminders go to an address nobody checks, often a former employee's.</li>
<li><strong>Developer-held domains.</strong> The domain sits in a past developer's account, and they stop renewing it.</li>
<li><strong>Bundled renewals.</strong> A hosting company renews the domain with hosting, and when hosting is cancelled, the domain lapses too.</li>
<li><strong>Card failures.</strong> Auto-renewal fails because a card expired, and nobody sees the warning.</li>
</ul>
<p>When a domain expires, the website and business email stop working. If it is not renewed within the registry's grace rules, someone else can register it. Our guide to <a href="/digital/blog/who-owns-your-website">who owns your website</a> explains how to check whose name your domain is in.</p>

<h2 id="protect">How to Make Sure Your Domain Never Lapses</h2>
<ol>
<li>Confirm the registrant name is you or your company, and the contact email is one you check daily.</li>
<li>Renew for several years at once; PKNIC allows up to ten.</li>
<li>Turn on auto-renewal for .com domains and keep a valid card on file.</li>
<li>Put the expiry date in your calendar with a reminder a month before.</li>
<li>Keep the registrar login with your business records, not only with your developer.</li>
</ol>
<p>If you are moving a domain to a different registrar, our guide on <a href="/digital/blog/transfer-domain-to-new-registrar">transferring a domain</a> covers the steps.</p>

<h2 id="hosting-vs-domain">Domain Renewal Is Separate From Hosting</h2>
<p>Many owners think of their website as one bill, but the domain and the hosting are two different services with two different renewal dates. You can keep the same domain and move hosting, or keep the hosting and move the domain. Our guide to <a href="/digital/blog/domain-and-hosting-price-in-pakistan">domain and hosting prices in Pakistan</a> compares both.</p>

<h2 id="with-us">Domain Renewals on Sites We Manage</h2>
<p>For websites on our maintenance plan, from {P['maint']} a month, we track domain and hosting renewal dates and remind you well before they are due, while the domain stays registered in your own name. See our <a href="/digital/pricing">published prices</a> for what each plan includes.</p>
""",
    faqs=[
        ("How much does it cost to renew a .pk domain?",
         "PKNIC lists Rs 2,100 per year for registrants based in Pakistan, charged for two years at a time, so a standard renewal is Rs 4,200 for two years. You can pay for up to ten years. Figures were checked on 4 November 2026; confirm on PKNIC's site before paying."),
        ("Is the .com.pk renewal fee different from .pk?",
         "PKNIC's payment page lists one domain fee for registrants in Pakistan rather than separate prices per Pakistani extension. Check the fee shown in your PKNIC account or invoice for your exact domain before renewing, and confirm any reseller's markup separately."),
        ("Why is my .com renewal more expensive than the first year?",
         "Many registrars advertise a discounted first-year price and charge their standard rate at renewal, often in US dollars. Compare renewal prices on official registrar pages before buying, and consider transferring to a registrar with fair renewal pricing if yours has become expensive."),
        ("What happens after a .pk or .com domain lapses?",
         "Your website and business email stop working. The domain usually enters a grace period during which you can still renew, but if it is not renewed in time, it can be released and registered by someone else. Renew early and keep the contact email current."),
        ("Can I renew a .pk domain for more than two years?",
         "Yes. PKNIC bills on a two-year basis and lets you pay for up to ten years in advance. Renewing for several years reduces the risk of losing the domain because of a missed reminder, an expired card or a change of staff."),
        ("Who should hold the domain renewal login?",
         f"You or your company should own the registrar or PKNIC account, with your own email as the contact. A developer can be given access, but should not own the account. On our maintenance plan from {P['maint']} a month we track renewals while the domain stays in your name."),
        ("Domain renew na karein to kya hoga?",
         "Website aur business email band ho jati hai. Kuch arsa renewal ka mauqa milta hai, magar is ke baad koi aur aap ka domain le sakta hai. Domain apne naam par rakhein, contact email woh rakhein jo roz check karte hain, aur kai saal ke liye renew karwayein."),
    ],
    sources=[
        ("PKNIC: How to pay", "https://pknic.net.pk/how-to-pay.html"),
        ("PKNIC: .pk domain registry", "https://pknic.net.pk/"),
        ("ICANN Lookup: check domain registration details", "https://lookup.icann.org/"),
        ("ICANN: Registrants' benefits and responsibilities", "https://www.icann.org/resources/pages/benefits-2013-09-16-en"),
    ],
    method="We took .pk fees and payment methods from PKNIC's official payment page on 4 November 2026, described .com renewal pricing without quoting any registrar's rate, and listed the renewal failures we see most often. Our own price comes from our published packages.",
    related=["domain-and-hosting-price-in-pakistan", "transfer-domain-to-new-registrar", "who-owns-your-website", "hosting-renewal-price-traps"],
    service_links=[("/digital/pricing", "Our published prices"), ("/digital/contact", "Get a written quote")],
    cta="Not sure when your domain expires or whose name it is in?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20domain%20renewal%20prices.%20Can%20you%20check%20my%20domain%3F",
)
