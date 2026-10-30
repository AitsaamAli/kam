import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=91,
    slug="website-hacked-what-to-do",
    title="Website Hacked? What to Do in the First 24 Hours",
    h1="Website Hacked: What to Do in the First 24 Hours, Step by Step",
    crumb="Website Hacked: First 24 Hours",
    description="Website hacked and not sure what to do? An hour-by-hour plan for the first 24 hours: contain it, change passwords, restore a clean backup and check Google.",
    keyword="website hacked what to do",
    cluster=["hacked website recovery", "website malware removal", "wordpress site hacked", "website showing spam links",
             "google says site hacked", "website hack ho gayi kya karein"],
    category="Fix a Problem",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("If your website is hacked, act in this order within 24 hours: put the site into maintenance or take it offline, change every "
            "password, tell your hosting company, restore a clean backup from before the hack, update everything, then check Google Search "
            "Console for security issues. Find how they got in, or it will happen again."),
    takeaways=[
        "Contain first: stop the damage spreading to visitors before trying to fix anything.",
        "Change all passwords, including hosting, admin, database, FTP and email, from a clean device.",
        "Restoring a clean backup taken before the hack is usually the fastest reliable fix.",
        "Update WordPress, themes and plugins, and remove anything unused, before going live again.",
        "Check Google Search Console for security warnings and request a review once the site is clean.",
    ],
    body=f"""
<h2 id="signs">How Do You Know Your Website Was Hacked?</h2>
<p>Common signs include strange pages or spam links you did not create, visitors being redirected to other sites, a browser or Google warning that the site is unsafe, new admin users you did not add, emails from your host about suspicious activity, or a sudden drop in traffic. Sometimes the owner only notices when a customer complains. Do not panic, and do not start deleting files at random; follow a clear order.</p>

<h2 id="first-24-hours">What Should You Do in the First 24 Hours?</h2>
<table>
<tr><th>Time</th><th>Action</th><th>Who</th></tr>
<tr><td>Hour 0 to 1</td><td>Put the site in maintenance mode or ask the host to take it offline; save screenshots of what you see</td><td>Owner or developer</td></tr>
<tr><td>Hour 1 to 2</td><td>From a clean device, change passwords for hosting, website admin, database, FTP or SFTP, domain and email; turn on two-step login</td><td>Owner</td></tr>
<tr><td>Hour 2 to 3</td><td>Contact your hosting company; ask for logs and whether other sites on the account are affected</td><td>Owner or developer</td></tr>
<tr><td>Hour 3 to 8</td><td>Find the last clean backup from before the hack and restore it; if none exists, clean the files and database</td><td>Developer</td></tr>
<tr><td>Hour 8 to 12</td><td>Update WordPress, themes and plugins; delete unused ones; remove unknown admin users</td><td>Developer</td></tr>
<tr><td>Hour 12 to 18</td><td>Look for the entry point: outdated plugin, weak password, nulled theme, shared login</td><td>Developer</td></tr>
<tr><td>Hour 18 to 24</td><td>Bring the site back online; check Search Console security issues; request a review if flagged</td><td>Owner and developer</td></tr>
</table>
<p>Example plan; a complex hack may take longer. If customer payment or personal data may have been exposed, take advice on your obligations.</p>

<h2 id="who-to-contact">Who Should You Contact?</h2>
<ul>
<li><strong>Your hosting company:</strong> for logs, malware scans, isolating the account and restoring server backups.</li>
<li><strong>Your developer or a maintenance provider:</strong> for cleaning, restoring and hardening the site.</li>
<li><strong>Your domain registrar:</strong> if you think the domain or DNS settings were changed.</li>
<li><strong>Your payment provider:</strong> if the checkout or payment pages may have been tampered with.</li>
<li><strong>Your customers:</strong> if their data may be affected, after taking advice on what to say.</li>
</ul>

<h2 id="restore">Should You Restore a Backup or Clean the Site?</h2>
<p>Restoring a backup from before the hack is usually faster and more reliable than finding every infected file. The catch is knowing when the hack started; restore from too late and the problem returns. If you have no clean backup, a developer must clean files and the database line by line, compare core files with fresh copies and remove hidden users and scheduled tasks. This is why regular, off-site backups matter; see our <a href="/digital/blog/website-backups-small-business">website backups guide</a>.</p>

<h2 id="google">What About Google Warnings?</h2>
<p>Google Search Console alerts site owners to security and spam problems it finds. Once the site is clean, check the security issues report and request a review if your site was flagged. Warnings in search results and browsers are removed after Google confirms the site is clean, which can take some time. Make sure Search Console is set up in your name before you need it.</p>

<h2 id="prevent">How Do You Stop It Happening Again?</h2>
<p>The WordPress hardening guide's basics apply to most sites: keep everything updated, use strong unique passwords and two-step login, give each person their own account with the least access they need, use only trusted plugins and themes, disable file editing in the dashboard, and keep regular backups off the server. Never use pirated or "nulled" themes and plugins; they are a common entry point. Our <a href="/digital/blog/website-security-checklist-small-business">security checklist</a> lists every step.</p>

<h2 id="what-we-offer">How We Can Help</h2>
<p>If your site has been hacked, message us on WhatsApp with what you are seeing. We restore from clean backups where available, clean the site, update and harden it, and help with Search Console reviews; emergency clean-ups are quoted after a first look. Our maintenance plan at {P['maint']} a month includes updates, off-site backups and monitoring, which prevents most hacks in the first place. See our <a href="/digital/pricing">pricing page</a> and the <a href="/digital/blog/get-business-website-on-google">guide to getting your website on Google</a>.</p>
""",
    faqs=[
        ("What should I do first if my website is hacked?",
         "Contain the damage first: put the site into maintenance mode or ask your host to take it offline, and save screenshots of what you see. Then change every password from a clean device, turn on two-step login and contact your hosting company for logs and help."),
        ("Can I restore my hacked website from a backup?",
         "Usually yes, and it is often the fastest reliable fix, if you have a clean backup from before the hack. Restore from too late and the problem returns. After restoring, update everything, remove unknown users, change passwords and find how attackers got in before going live again."),
        ("Why does Google say my site may be hacked?",
         "Google flags sites where it detects malware, spam pages or other signs of compromise, to protect searchers. Check the security issues report in Google Search Console, clean the site, then request a review. Warnings are removed after Google confirms the site is clean, which can take some time."),
        ("How do websites usually get hacked?",
         "Common entry points are outdated plugins, themes or core software with known flaws, weak or reused passwords, pirated or nulled themes and plugins, shared logins and insecure hosting. Keeping software updated, using strong unique passwords with two-step login and avoiding pirated add-ons prevents most attacks."),
        ("How much does it cost to fix a hacked website?",
         f"It depends on how badly the site is affected and whether a clean backup exists. We quote emergency clean-ups after a first look. Prevention costs much less: our maintenance plan at {P['maint']} a month includes updates, off-site backups and monitoring, which stop most hacks before they happen."),
        ("Website hack ho jaye to kya karein?",
         "Sab se pehle website band karein ya maintenance mode lagayen, phir saaf device se tamam passwords badlein aur two-step login lagayen. Hosting company ko batayen, hack se pehle ka saaf backup restore karein, sab kuch update karein aur Google Search Console mein security warning check karein."),
    ],
    sources=[
        ("WordPress Developer Resources — Hardening WordPress", "https://developer.wordpress.org/advanced-administration/security/hardening/"),
        ("WordPress Developer Resources — WordPress backups", "https://developer.wordpress.org/advanced-administration/security/backup/"),
        ("Google Search Console Help — About Search Console", "https://support.google.com/webmasters/answer/9128668"),
        ("OWASP — Top 10 web application security risks", "https://owasp.org/www-project-top-ten/"),
        ("Google Search Console Help — Manage owners, users and permissions", "https://support.google.com/webmasters/answer/7687615"),
    ],
    method=("Hardening and backup advice follows WordPress developer documentation, and Search Console alerts follow Google's help page, "
            "checked 29 October 2026. The hour-by-hour table is an illustrative plan based on how we handle clean-ups; complex cases take "
            "longer. We quote no clean-up price because it depends on the damage. Maintenance price is our own."),
    related=["get-business-website-on-google", "website-security-checklist-small-business", "website-backups-small-business",
             "website-down-check"],
    service_links=[("/digital/pricing", "Maintenance and security plans"), ("/digital/contact", "Get help with a hacked site")],
    cta="Has your website been hacked?",
    wa="Hi%2C%20I%20read%20your%20website%20hacked%20guide%20and%20need%20urgent%20help",
)
