import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=196,
    slug='website-budget-planner-first-year',
    title='Website Budget Planner: Your First-Year Costs in One Table',
    h1='Website Budget Planner: Every First-Year Website Cost for a Pakistani Business in One Table',
    crumb='Website Budget Planner',
    description='A website budget planner for Pakistani businesses: build, domain, hosting, email, maintenance, photos and ads in one first-year table, with dated facts.',
    keyword='website budget',
    cluster=['website first year cost', 'website annual cost pakistan', 'website budget template'],
    category='Planning & Launch',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer=f"A first-year website budget for a Pakistani business has 7 lines: build, domain, hosting, business email, maintenance, content and marketing. Our landing pages begin at {P['landing']}; the national registry charges Rs 2,100 yearly for a .pk name; care plans begin at {P['maint']} monthly. Ad spend is optional and yours to set.",
    takeaways=["The build is only one line; running costs continue every year.", "Domain, hosting and email are small but must never lapse.", "Maintenance protects the investment; budget for it from day one.", "Content and photos are often forgotten, then delay the launch.", "Marketing spend is a separate decision from the website itself."],
    body=f"""
<h2 id="why">Why Plan a Website Budget for the Whole First Year?</h2>
<p>Most owners ask "how much does a website cost?" and hear one number: the build. Then come the domain renewal, hosting bill, email accounts, a plugin licence, a photographer, and perhaps a first ad campaign. None are large on their own, but together they decide whether the website is affordable and whether it keeps working. A clear website budget for the first year avoids surprises and helps you compare quotes fairly.</p>
<p>This planner is part of our planning guides, alongside choosing a platform and our full website price guide.</p>

<h2 id="table">What Goes in the First-Year Budget?</h2>
<table>
<tr><th>Line</th><th>What it covers</th><th>Figure or guide (checked 30 Oct 2026)</th><th>Your amount</th></tr>
<tr><td>1. Build</td><td>Design and development</td><td class="price">Landing page from {P['landing']}; starter site from {P['starter']}; business site from {P['business']}; online store from {P['store']}</td><td></td></tr>
<tr><td>2. Domain</td><td>Your web address</td><td>.pk via PKNIC: Rs 2,100 yearly for local registrants, charged two years at a time</td><td></td></tr>
<tr><td>3. Hosting</td><td>Server space for the site</td><td>Varies by host and plan; compare renewal prices, not just the first term</td><td></td></tr>
<tr><td>4. Business email</td><td>Addresses on your domain</td><td>Zoho Mail free for up to 5 users; Google Workspace priced per user</td><td></td></tr>
<tr><td>5. Maintenance</td><td>Updates, backups, monitoring, small changes</td><td class="price">Care plans from {P['maint']} a month</td><td></td></tr>
<tr><td>6. Content and photos</td><td>Writing, translation, photography</td><td>Your time, or a writer and photographer you hire</td><td></td></tr>
<tr><td>7. Marketing</td><td>Ads, promotions, listings</td><td>Optional; set your own monthly limit</td><td></td></tr>
</table>
<p>Copy this table into a spreadsheet and fill in the last column. Add a contingency of a small percentage for surprises, such as a premium plugin or an extra page.</p>

<h2 id="build">How Do You Choose the Build Line?</h2>
<p>Match the build to what the business needs this year, not in five years. A landing page suits a single service or campaign. A starter site suits a small business with a few pages. A business website suits firms with several services and more content. An online store suits selling with payments and delivery. Our pages guide helps decide which pages you need.</p>

<h2 id="small-lines">Why Do Small Lines Matter So Much?</h2>
<p>Domain, hosting and email are the cheapest lines but the most dangerous to forget. If the domain lapses, the website and email stop. If hosting renewal fails, the site goes offline. Put renewal dates in a calendar, keep payment details current, and make sure accounts are in the business's name. Our <a href="/digital/blog/hosting-renewal-price-traps">hosting renewal guide</a> explains why year-two hosting often costs more.</p>

<h2 id="maintenance">Is Maintenance Really Necessary?</h2>
<p>A website that is never updated becomes slower, less secure and eventually broken. Budget for maintenance either as a care plan or as your own time with a backup routine. Our maintenance charges guide explains what is included.</p>

<h2 id="content">How Much Should Content Cost?</h2>
<p>If you write and photograph yourself, the cost is time: often several days for a small site. If you hire help, get quotes from writers and photographers for the specific pages and shots you need. Do not leave this line empty; late content is the most common cause of delayed launches.</p>

<h2 id="marketing">How Should Marketing Be Budgeted?</h2>
<p>Treat ads as a separate, adjustable line. Start with a modest monthly limit, track enquiries, and increase only if the numbers justify it. Our guides to <a href="/digital/blog/google-ads-landing-page-pakistan">Google Ads readiness</a> and <a href="/digital/blog/meta-ads-to-website-or-whatsapp">Meta ads routes</a> help before you spend.</p>

<h2 id="year-two">What Changes in Year Two?</h2>
<p>The build cost disappears, but renewals, maintenance, content updates and marketing continue, and hosting may rise after its introductory term. Review the table at the end of year one and adjust.</p>

<h2 id="privacy">Is There a Privacy Line in the Budget?</h2>
<p>It is rarely a separate cost. Still, allow time to write a privacy policy and set up secure forms, especially if you collect customer details or sell to overseas customers.</p>

<h2 id="quote">Getting Exact Figures</h2>
<p>We provide fixed build quotes and tell you hosting and renewal costs before you buy. See our <a href="/digital/pricing">pricing page</a>.</p>
""",
    faqs=[
        ('What should a first-year website budget include?',
         "Seven lines: the build, the domain, hosting, business email, maintenance, content and photos, and marketing. The build is a one-off cost, but domain, hosting, email and maintenance continue every year, and marketing is an adjustable, optional line you control yourself."),
        ('How much does a website cost in the first year in Pakistan?',
         f"It depends on your choices. A single landing page begins at {P['landing']} and a small starter site at {P['starter']}; the registry charges Rs 2,100 yearly for a local .pk name, and care plans start from {P['maint']} a month, plus hosting and optional marketing."),
        ('How much is a .pk domain per year?',
         "Since 1 August 2026, PKNIC has charged registrants inside Pakistan Rs 2,100 per year, collected for two years at once, while those abroad pay $15.99 yearly. Resellers may add their own service charges, so compare the total you will pay."),
        ('Is business email expensive?',
         "Not necessarily. Zoho's official pricing page lists a free plan for up to five users on one domain, with limits. Google Workspace and paid Zoho plans charge per user per month. Hosting packages often include basic email, though with weaker filtering and deliverability."),
        ('Do I need to budget for website maintenance?',
         "Yes. Without updates, backups and monitoring, websites become slower, less secure and eventually break. Budget for a care plan or for your own time and a backup routine. Our care plans start from a published monthly price, listed with what each plan includes."),
        ('What website costs do owners usually forget?',
         "Content and photos, domain and hosting renewals, hosting price rises after the introductory term, premium plugin or app licences, business email for staff, and maintenance. Listing all seven budget lines before you start, with renewal dates, prevents most of these surprises."),
        ('Website ka pehle saal ka budget kaise banayein?',
         "Saat cheezein likhein: website banwana, domain, hosting, business email, maintenance, mawaad aur tasveerein, aur ishtehar. .pk domain PKNIC ke mutabiq Rs 2,100 salana hai. Domain aur hosting ki renewal tareekh calendar mein likh lein, aur ishtehar ka budget alag rakhein."),
    ],
    sources=[('PKNIC — .pk domain registration', 'https://pknic.net.pk/'), ('Zoho Mail — Pricing', 'https://www.zoho.com/mail/zohomail-pricing.html'), ('Google Workspace — Pricing', 'https://workspace.google.com/pricing'), ('Bluehost — Shared hosting', 'https://www.bluehost.com/hosting/shared')],
    method="Build and care plan prices come from our published list (P). The .pk fee comes from PKNIC and email plan details from Zoho and Google, checked 30 October 2026. Hosting is described without a figure because it varies; the renewal pattern references official host pages. The table structure is editorial.",
    related=['hosting-renewal-price-traps', 'when-to-upgrade-your-website', 'website-roi-small-business'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='Planning your website budget?',
    wa='Hi%2C%20I%20read%20your%20website%20budget%20planner',
)
