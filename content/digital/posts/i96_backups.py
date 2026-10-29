import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=96,
    slug="website-backups-small-business",
    title="Website Backup Guide: How Often and Where to Keep It",
    h1="Website Backup Guide for Small Businesses: How Often, Where to Store It and How to Test",
    crumb="Website Backups",
    description="Website backup guide for small businesses: how often to back up by site type, the 3-2-1 rule, where to store copies, and why you must test a restore.",
    keyword="website backup",
    cluster=["website backup frequency", "3-2-1 backup rule", "how to backup website", "test website restore",
             "offsite backup website", "website ka backup kaise lein"],
    category="Fix a Problem",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("A good website backup plan copies both files and database, weekly for a small brochure site and daily or more often for "
            "online stores, keeps at least 3 copies with 1 stored away from your hosting, and is tested by actually restoring it. "
            "Always take a backup before any update."),
    takeaways=[
        "A complete backup includes the website files and the database; one without the other is not enough.",
        "Back up weekly for small, rarely changed sites and daily or more for stores and busy sites.",
        "Follow the 3-2-1 idea: three copies, on two kinds of storage, with one away from your host.",
        "Take a backup before every update, plugin install or major change.",
        "Test a restore regularly; an untested backup may not work when you need it.",
    ],
    body=f"""
<h2 id="what-is">What Is a Website Backup?</h2>
<p>A backup is a copy of everything needed to rebuild your site: the files, such as themes, plugins, images and uploads, and the database, which holds pages, products, orders and settings. If a hack, failed update, server problem or human mistake breaks your site, a recent backup lets you restore it in hours instead of rebuilding for weeks.</p>
<p>Many owners assume their host or developer keeps backups. Sometimes they do, sometimes only on the same server, and sometimes not at all. Check.</p>

<h2 id="how-often">How Often Should You Back Up?</h2>
<p>WordPress's own backup guidance suggests weekly backups for smaller sites, daily backups for high-activity sites and always backing up before an upgrade. Here is how that translates by site type:</p>
<table>
<tr><th>Site type</th><th>Suggested frequency</th><th>Why</th></tr>
<tr><td>Brochure site updated a few times a month</td><td>Weekly, plus before every change</td><td>Little changes between backups</td></tr>
<tr><td>Blog or news site</td><td>Daily or after publishing</td><td>New content each week</td></tr>
<tr><td>Online store</td><td>Daily at least; database more often if orders are frequent</td><td>Orders and customer data change constantly</td></tr>
<tr><td>Booking system or web app</td><td>Database several times a day or continuous</td><td>Lost bookings or records are hard to recreate</td></tr>
</table>

<h2 id="three-two-one">What Is the 3-2-1 Backup Rule?</h2>
<p>The 3-2-1 rule is a widely used rule of thumb: keep at least three copies of your data, on two different kinds of storage, with one copy kept off-site. WordPress's guidance makes a similar point, suggesting at least three to five recent backups stored in different places, such as the host's server, cloud storage and your own computer. For a small business website, a practical version is:</p>
<ol>
<li>the live site itself</li>
<li>automatic backups by your host</li>
<li>a separate copy in cloud storage you control, such as your own Google Drive or other cloud account</li>
</ol>
<p>The off-site copy matters most. If the hosting account is hacked, suspended or deleted, backups stored on the same server can be lost with it.</p>

<h2 id="test-restore">Why Must You Test a Restore?</h2>
<p>A backup is only useful if it can be restored. Files can be incomplete, the database can be missing, or the backup plugin may have been failing silently for months. WordPress's guidance recommends occasionally making a manual backup to confirm the automated process works. Better still, every few months restore a backup to a staging copy and check that pages, images, forms and orders all work.</p>

<h2 id="before-updates">When Else Should You Take a Backup?</h2>
<ul>
<li>before updating WordPress, themes or plugins</li>
<li>before installing a new plugin or changing the theme</li>
<li>before a redesign, migration or hosting move</li>
<li>before big content imports, such as hundreds of new products</li>
</ul>

<h2 id="how-long">How Long Should You Keep Old Backups?</h2>
<p>Keep several recent backups, not just the latest one. Hacks and mistakes are sometimes noticed days or weeks later, and by then the newest backups may contain the problem. A practical pattern for small businesses is daily copies kept for two weeks, weekly copies for two months and monthly copies for a year. Delete older copies that contain customer data you no longer need, in line with your privacy policy.</p>

<h2 id="ownership">Who Should Control the Backups?</h2>
<p>You should. Store at least one copy in an account in your own name, not only in your developer's account. If you part ways with a developer, you will still have your site. Our guide on <a href="/digital/blog/who-owns-your-website">who owns your website</a> explains why each account should be yours.</p>

<h2 id="what-we-offer">How We Handle Backups</h2>
<p>Our maintenance plan at {P['maint']} a month includes scheduled backups of files and database, an off-site copy in storage you can access, backups before every update and quarterly test restores to staging. Every site we build is handed over with backups configured. See our <a href="/digital/pricing">pricing page</a>, the <a href="/digital/blog/website-hacked-what-to-do">hacked website guide</a> and the <a href="/digital/blog/get-business-website-on-google">guide to getting your website on Google</a>.</p>
""",
    faqs=[
        ("How often should I back up my website?",
         "WordPress's guidance suggests weekly backups for smaller sites and daily backups for busy ones, plus a backup before every upgrade. Online stores and booking systems usually need daily backups or more, because orders and bookings change constantly and are difficult to recreate once lost."),
        ("What is the 3-2-1 backup rule?",
         "It is a common rule of thumb: keep at least three copies of your data, on two different kinds of storage, with one copy off-site. For a website, that might be the live site, your host's backups and a separate copy in cloud storage you control."),
        ("Are my hosting company's backups enough?",
         "Often not on their own. Host backups may be stored on the same server, kept for only a few days, or lost if the account is hacked or suspended. Keep at least one additional copy in storage you control, and check how long the host keeps backups and how to restore them."),
        ("What should a website backup include?",
         "A complete backup includes the website files, such as themes, plugins, images and uploaded documents, and the database, which stores pages, posts, products, orders, users and settings. A backup missing either part cannot fully restore the site, so check that both are included."),
        ("How do I know my website backup works?",
         "Test it. Every few months, restore a backup to a staging copy of the site and check that pages, images, forms and orders work. WordPress's guidance also recommends occasionally taking a manual backup to confirm the automated process is running properly."),
        ("Website ka backup kaise aur kitni dafa lein?",
         "Chhoti website ka har hafte aur online store ka rozana backup lein, aur har update se pehle bhi. Backup mein files aur database dono hon. Kam az kam teen copies rakhein, jin mein se aik hosting se bahar apne cloud account mein ho, aur kabhi kabhi restore kar ke test zaroor karein."),
    ],
    sources=[
        ("WordPress Developer Resources — WordPress backups", "https://developer.wordpress.org/advanced-administration/security/backup/"),
        ("WordPress Developer Resources — Hardening WordPress", "https://developer.wordpress.org/advanced-administration/security/hardening/"),
        ("OWASP — Top 10 web application security risks", "https://owasp.org/www-project-top-ten/"),
        ("ICANN — Registrants' benefits and responsibilities", "https://www.icann.org/resources/pages/benefits-2013-09-16-en"),
        ("Internet Archive — Wayback Machine", "https://web.archive.org/"),
    ],
    method=("Backup frequency, number of copies, storage locations and manual checks follow WordPress's backup documentation, checked 29 "
            "October 2026. The 3-2-1 rule is described as a widely used rule of thumb. The frequency table by site type is our "
            "recommendation. The maintenance price is our own."),
    related=["get-business-website-on-google", "website-hacked-what-to-do", "website-security-checklist-small-business",
             "website-down-check"],
    service_links=[("/digital/pricing", "Maintenance with tested backups"), ("/digital/contact", "Check your backups")],
    cta="Not sure your website is backed up?",
    wa="Hi%2C%20I%20read%20your%20website%20backup%20guide%20and%20need%20help",
)
