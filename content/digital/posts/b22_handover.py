import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=22,
    slug="website-handover-checklist",
    title="Website Handover Checklist: What to Get at Launch",
    h1="Website Handover Checklist: Everything You Must Receive at Launch",
    crumb="Website Handover Checklist",
    description="A website handover checklist for launch day: the logins, files, backups, licences and documents you must receive before making the final payment to your developer.",
    keyword="website handover checklist",
    cluster=["website handover document", "what to get from web developer", "website launch checklist",
             "website credentials handover", "website documentation"],
    category="Hiring a Developer",
    published="2026-10-28", published_h="28 October 2026",
    updated="2026-10-28", updated_h="28 October 2026",
    answer=("A website handover checklist covers five groups: account access (domain, hosting, admin, email, Google tools), files and backups, "
            "licences for themes and plugins, documentation for editing the site, and a short support agreement. Receive and test every "
            "item before the final payment, so you can run or move your website without depending on one developer."),
    takeaways=[
        "Handover is complete only when you can log in to every account yourself.",
        "Test each login before the final payment, not after.",
        "Ask for a full backup stored outside the hosting account.",
        "Licences must be in your name, or you may lose updates and support.",
        "Change shared passwords after handover and remove access you no longer need.",
    ],
    body="""
<h2 id="checklist">The Website Handover Checklist</h2>
<h3>1. Account access</h3>
<table>
<tr><th>Item</th><th>What to confirm</th></tr>
<tr><td>Domain registrar</td><td>Registered to you; you can log in; auto-renew on</td></tr>
<tr><td>Hosting account</td><td>In your name; billing to your card or account</td></tr>
<tr><td>Website admin</td><td>Administrator or store-owner account in your name</td></tr>
<tr><td>Business email</td><td>Admin access to the email service</td></tr>
<tr><td>Google Search Console</td><td>You are the owner</td></tr>
<tr><td>Google Analytics</td><td>You are the administrator</td></tr>
<tr><td>Google Business Profile</td><td>You are the primary owner</td></tr>
<tr><td>Payment gateway and courier accounts</td><td>Registered to your business</td></tr>
</table>
<h3>2. Files and backups</h3>
<ul>
<li>A full backup of files and database, downloaded and stored outside the hosting account.</li>
<li>Source code, or a transfer of the code repository to your account for custom builds.</li>
<li>Original design files, logo files and images used on the site.</li>
</ul>
<h3>3. Licences</h3>
<ul>
<li>Theme and paid plugin or app licences in your name, with renewal dates.</li>
<li>Font and stock image licences, if any were bought.</li>
</ul>
<h3>4. Documentation</h3>
<ul>
<li>A short guide to editing pages, products, prices and blog posts.</li>
<li>A list of every plugin, app or integration and what it does.</li>
<li>Renewal dates and yearly costs for the domain, hosting and licences.</li>
<li>How redirects, forms and email notifications are set up.</li>
</ul>
<h3>5. Support</h3>
<ul>
<li>The bug-fix period after launch, in writing.</li>
<li>Response time for urgent problems.</li>
<li>Prices for ongoing changes or maintenance, if needed.</li>
</ul>

<h2 id="test">How to Test the Handover</h2>
<ol>
<li>Log in to every account above from your own device.</li>
<li>Open the backup file and check it is not empty.</li>
<li>Submit a form and place a test order, if the site sells online.</li>
<li>Check the site on your phone using mobile data.</li>
<li>Confirm that the sitemap is submitted in Search Console.</li>
</ol>
<p>Make the final payment once every item is received and working. Our guide to <a href="/digital/blog/website-milestone-payments">milestone payments</a> explains how to tie the last payment to handover.</p>

<h2 id="security">Security After Handover</h2>
<ul>
<li>Change any passwords that were shared during the project.</li>
<li>Turn on two-step verification on the domain, hosting, email and admin accounts.</li>
<li>Remove developer accounts you no longer need, or reduce them to limited roles.</li>
<li>Keep the backup and a list of accounts somewhere safe that a trusted colleague can reach.</li>
</ul>

<h2 id="platforms">Platform Notes</h2>
<table>
<tr><th>Platform</th><th>Handover focus</th></tr>
<tr><td>WordPress</td><td>Administrator account, full backup, plugin licences, hosting control panel</td></tr>
<tr><td>Shopify</td><td>Store ownership in your name, staff accounts for the developer, app subscriptions billed to you</td></tr>
<tr><td>Custom build</td><td>Code repository transfer, server access, environment documentation, deployment steps</td></tr>
</table>

<h2 id="missing">What If Items Are Missing?</h2>
<p>Ask in writing for each missing item, referring to your agreement, and hold the final payment until it is received. If the domain or hosting is in the developer's name, prioritise moving those first. Our guide to <a href="/digital/blog/who-owns-your-website">who owns your website</a> explains how to take back control, and our <a href="/digital/blog/website-development-contract-checklist">contract checklist</a> shows how to include handover in the next agreement.</p>

<h2 id="our-handover">Our Handover</h2>
<p>Every project we deliver ends with the domain and hosting in your name, full admin access, a backup, a short editing guide and a list of renewal dates. Ongoing maintenance is optional and priced separately.</p>
""",
    faqs=[
        ("What should I receive when my website is finished?",
         "You should receive login access to the domain, hosting, website admin, email and Google tools in your own name, a full backup, the source or design files, licences for themes and plugins, a short editing guide, a list of renewal dates and costs, and the support terms in writing."),
        ("Should I pay the developer before or after handover?",
         "Make the final payment after handover is complete and tested. Agree at the start that the last milestone covers launch plus delivery of all logins, files, licences and documentation. This protects you, and a professional developer will be comfortable with it because it is a normal, fair structure."),
        ("What is a website handover document?",
         "A handover document lists every account, who owns it and how to access it, plus the plugins or apps used, renewal dates and costs, and how forms, redirects and email notifications work. It lets you or any future developer run, edit and move the website without depending on the original developer."),
        ("How do I keep my website secure after handover?",
         "Change any passwords shared during the project, turn on two-step verification on the domain, hosting, email and admin accounts, remove developer accounts you no longer need and keep an offline backup. Store a list of accounts somewhere safe that a trusted colleague can reach in an emergency."),
        ("Website mukammal hone par developer se kya kya lena chahiye?",
         "Domain, hosting, website admin aur email ke logins apne naam par lein, poora backup, design files, themes aur plugins ke licence, website edit karne ki choti guide aur renewal ki tareekhein. Sab kuch khud login kar ke check karein, phir aakhri payment karein."),
        ("Do I need the source code if my site is on Shopify?",
         "Shopify hosts the platform, so you do not receive server code, but you should own the store account and have the theme files, any custom code and a product export. For WordPress or custom builds, a full backup or repository transfer is essential because it lets another developer take over."),
    ],
    sources=[
        ("Google Search Console Help — Manage owners, users and permissions", "https://support.google.com/webmasters/answer/7687615"),
        ("Google Analytics Help — Add, edit and delete users", "https://support.google.com/analytics/answer/9305788"),
        ("Google Business Profile Help — Add or remove owners and managers", "https://support.google.com/business/answer/3403100"),
        ("GitHub Docs — Transferring a repository", "https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository"),
        ("WordPress Developer Resources — WordPress backups", "https://developer.wordpress.org/advanced-administration/security/backup/"),
        ("OWASP — Top 10 web application security risks", "https://owasp.org/www-project-top-ten/"),
    ],
    method=("The checklist is the one we complete at the end of every project, extended with items clients have found missing after "
            "projects with other developers. Account steps follow the official Google, GitHub and WordPress documentation; security "
            "steps follow common OWASP guidance."),
    related=["who-owns-your-website", "website-milestone-payments", "website-development-contract-checklist",
             "website-maintenance-charges-in-pakistan"],
    service_links=[("/digital/business-websites", "Websites delivered with full handover"), ("/digital/contact", "Ask about our handover")],
    cta="Need help with a website handover?",
    wa="Hi%2C%20I%20read%20your%20handover%20checklist%20and%20need%20help",
)
