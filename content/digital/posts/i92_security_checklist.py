import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=92,
    slug="website-security-checklist-small-business",
    title="Website Security Checklist for Small Businesses",
    h1="Website Security Checklist for Small Businesses: 14 Checks You Can Do This Month",
    crumb="Website Security Checklist",
    description="A website security checklist for small businesses: updates, passwords, two-step login, user access, backups, SSL and hosting, based on WordPress and OWASP guidance.",
    keyword="website security checklist",
    cluster=["secure website tips", "wordpress security checklist", "small business website security", "two factor login website",
             "website user access review", "website ko hack se kaise bachayen"],
    category="Fix a Problem",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("A website security checklist for a small business covers 14 checks: updates for core, themes and plugins; strong unique "
            "passwords; two-step login; one account per person; removing old users; off-site backups; HTTPS; trusted plugins only; file "
            "editing disabled; and hosting, domain and email security. Review it monthly."),
    takeaways=[
        "Most small business websites are hacked through outdated software, weak passwords or pirated add-ons, not targeted attacks.",
        "Updates, strong passwords with two-step login and backups prevent most problems.",
        "Give each person their own account with the least access they need, and remove it when they leave.",
        "Protect the accounts around the website too: hosting, domain registrar and email.",
        "A monthly 30-minute review, or a maintenance plan, keeps the checklist working.",
    ],
    body=f"""
<h2 id="why-small-businesses">Why Does a Website Security Checklist Matter for Small Businesses?</h2>
<p>Small business owners often assume hackers are not interested in them. In practice, most attacks are automated: bots scan thousands of websites for outdated plugins, weak passwords and known flaws, and break into whichever ones are open. A clinic, school or online shop is as likely a target as anyone. The good news is that a handful of habits block most of these attacks.</p>
<p>The OWASP Top 10, a widely used list of the most serious web application risks, includes problems such as broken access control and using components with known vulnerabilities. For a small business website, that translates into the practical checks below, which also follow WordPress's own hardening guidance.</p>

<h2 id="checklist">What Is on the 14-Point Checklist?</h2>
<table>
<tr><th>#</th><th>Check</th><th>How often</th></tr>
<tr><td>1</td><td>Core software (such as WordPress) on the latest version</td><td>Monthly, or when security releases appear</td></tr>
<tr><td>2</td><td>Themes and plugins updated</td><td>Monthly</td></tr>
<tr><td>3</td><td>Unused themes and plugins deleted</td><td>Monthly</td></tr>
<tr><td>4</td><td>Only plugins and themes from trusted sources; no nulled copies</td><td>Every install</td></tr>
<tr><td>5</td><td>Strong, unique passwords for every account</td><td>At set-up and after staff changes</td></tr>
<tr><td>6</td><td>Two-step login on admin, hosting, domain and email</td><td>At set-up</td></tr>
<tr><td>7</td><td>One account per person, with the least access needed</td><td>Quarterly review</td></tr>
<tr><td>8</td><td>Old staff and developer accounts removed</td><td>When people leave</td></tr>
<tr><td>9</td><td>Backups stored off the server, and a test restore done</td><td>Backups daily or weekly; test quarterly</td></tr>
<tr><td>10</td><td>HTTPS on every page with a valid certificate</td><td>Monthly check</td></tr>
<tr><td>11</td><td>File editing disabled in the dashboard</td><td>At set-up</td></tr>
<tr><td>12</td><td>Hosting account secure, with server software current</td><td>Quarterly</td></tr>
<tr><td>13</td><td>Domain registrar locked, with your own email as contact</td><td>Yearly</td></tr>
<tr><td>14</td><td>Search Console set up to receive security alerts</td><td>At set-up</td></tr>
</table>

<h2 id="passwords-2fa">Why Are Passwords and Two-Step Login So Important?</h2>
<p>WordPress's hardening guide advises strong passwords that avoid short words, dictionary words and all-number patterns, and recommends adding two-step authentication. Reused passwords are a major risk: if a staff member's password leaks from another site, attackers try it everywhere. Use a password manager, and turn on two-step login for the website admin, hosting, domain registrar and email, because whoever controls your email can reset everything else.</p>

<h2 id="access">How Should Access Be Managed?</h2>
<p>Give every person their own login. WordPress roles let you give editors access to content without letting them install plugins, and Google tools let you add users without sharing the owner account. When a staff member, agency or developer leaves, remove their access the same day. Our guide on <a href="/digital/blog/who-owns-your-website">who owns your website</a> explains how to keep yourself as owner.</p>

<h2 id="backups">Why Do Backups Count as Security?</h2>
<p>No security is perfect. A recent, clean backup stored away from the server turns a disaster into an inconvenience. WordPress's backup guidance suggests at least weekly backups for small sites, daily for busy ones, with several copies kept in different places. Test a restore occasionally; a backup you cannot restore is not a backup. See our <a href="/digital/blog/website-backups-small-business">website backups guide</a>.</p>

<h2 id="pakistan-specifics">Are There Pakistan-Specific Risks?</h2>
<p>Two come up often. First, pirated themes and plugins, sold cheaply or shared freely, frequently contain hidden malicious code; buy from the official seller. Second, websites built by a developer who holds the only logins and the domain; if that relationship ends badly, the site is exposed. Keep ownership and access in your own name.</p>

<h2 id="what-we-offer">How We Can Help</h2>
<p>Our maintenance plan, at {P['maint']} a month, covers most of this checklist for you: updates, off-site backups with restore tests, user access reviews, uptime and security monitoring, and Search Console alerts. Every site we build starts with these settings in place. See our <a href="/digital/pricing">pricing page</a>, and if the worst happens, our <a href="/digital/blog/website-hacked-what-to-do">website hacked guide</a> and the <a href="/digital/blog/get-business-website-on-google">getting found on Google pillar</a>.</p>
""",
    faqs=[
        ("How do I secure my small business website?",
         "Keep core software, themes and plugins updated, delete unused ones, use strong unique passwords with two-step login, give each person their own account with limited access, remove old users, keep off-site backups and test restores, use HTTPS everywhere and secure your hosting, domain and email accounts."),
        ("How often should I update my WordPress website?",
         "Check for updates at least monthly, and apply security releases as soon as they appear. WordPress's hardening guide notes that older versions are not maintained with security updates. Take a backup before updating, and test key pages and forms afterwards to catch any conflicts."),
        ("Are free or nulled WordPress themes safe?",
         "Free themes from the official WordPress directory are reviewed and generally safe. Nulled themes are pirated copies of paid themes, often shared on unofficial sites, and frequently contain hidden malicious code. They also receive no updates. Always buy paid themes and plugins from the official seller."),
        ("Do I need two-factor login on my website?",
         "Yes. WordPress's hardening guide recommends two-step authentication as an extra layer beyond passwords. Turn it on for the website admin, hosting, domain registrar and email accounts. Email matters most, because whoever controls your email can usually reset the passwords on every other account."),
        ("Does a small business website need a maintenance plan for security?",
         f"Not if someone on your team reliably updates software, reviews access and checks backups every month. If not, a maintenance plan is cheaper than a hack. Ours costs {P['maint']} a month and covers updates, off-site backups with restore tests, access reviews and monitoring."),
        ("Website ko hack hone se kaise bachayen?",
         "WordPress, themes aur plugins har maheene update karein, mazboot aur alag passwords ke saath two-step login lagayen, har bande ka apna account rakhein aur chhorne walon ka account foran hatayen. Backup server se bahar rakhein, kabhi nulled theme na lagayen, aur domain aur email ko bhi mehfooz rakhein."),
    ],
    sources=[
        ("OWASP — Top 10 web application security risks", "https://owasp.org/www-project-top-ten/"),
        ("WordPress Developer Resources — Hardening WordPress", "https://developer.wordpress.org/advanced-administration/security/hardening/"),
        ("WordPress Developer Resources — WordPress backups", "https://developer.wordpress.org/advanced-administration/security/backup/"),
        ("WordPress.org — Roles and capabilities", "https://wordpress.org/documentation/article/roles-and-capabilities/"),
        ("Let's Encrypt — Free, automated certificate authority", "https://letsencrypt.org/"),
        ("Google Search Console Help — About Search Console", "https://support.google.com/webmasters/answer/9128668"),
    ],
    method=("Checks follow WordPress's hardening and backup documentation and the OWASP Top 10 project page, checked 29 October 2026; we "
            "describe OWASP categories generally rather than naming an edition. Frequencies are our recommendations. The Pakistan-specific "
            "risks reflect sites we have recovered. Maintenance price is our own."),
    related=["get-business-website-on-google", "website-hacked-what-to-do", "website-backups-small-business", "website-down-check"],
    service_links=[("/digital/pricing", "Maintenance and security plans"), ("/digital/contact", "Get a security check")],
    cta="Want your website security handled for you?",
    wa="Hi%2C%20I%20read%20your%20website%20security%20checklist%20and%20need%20help",
)
