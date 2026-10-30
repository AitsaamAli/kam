import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=162,
    slug='move-website-to-new-hosting',
    title='Move a Website to a New Host Without Downtime',
    h1='How to Move Your Website to a New Host Without Downtime or Lost Email',
    crumb='Move Website to New Host',
    description='How to move a website to a new host without downtime: a checklist covering backups, lowering DNS TTL, email records, testing first and what to check after.',
    keyword='move website to new host',
    cluster=['website migration hosting', 'change hosting company', 'hosting transfer pakistan'],
    category='Fix a Problem',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="To move a website to a new host without downtime, take a full backup, copy files and database to the new server, test it there before changing anything public, lower the DNS TTL a day ahead, recreate email records, then switch DNS at a quiet time. Keep the old hosting active for at least 7 days afterwards.",
    takeaways=["Never cancel the old hosting until the new site and email are confirmed working.", "Lower the DNS TTL a day before the switch so changes spread faster.", "Email is often hosted with the website; plan where it will live after the move.", "Test the site on the new server before pointing the domain to it.", "Check forms, payments, HTTPS and search console after the switch."],
    body=f"""
<h2 id="when">When Should You Move a Website to a New Host?</h2>
<p>Slow pages, repeated downtime, poor support or a renewal price that doubled are the usual triggers. Whatever the reason, moving a website to a new host is mostly a matter of order: copy, test, switch, verify. Problems come from doing these out of sequence, especially cancelling the old hosting too early or forgetting that email lives there too. Our hosting guide for Pakistani websites covers choosing the new host.</p>
<p>Hosting moves are one of the fixes collected alongside our Google visibility guide.</p>

<h2 id="checklist">What Is the Step-by-Step Checklist?</h2>
<table>
<tr><th>When</th><th>Task</th></tr>
<tr><td>1 week before</td><td>Choose the new host; list everything on the old account: sites, databases, email accounts, cron jobs, SSL</td></tr>
<tr><td>3 days before</td><td>Full backup of files, database and email; store it off both servers</td></tr>
<tr><td>2 days before</td><td>Copy the site to the new server and test it using a temporary address or hosts-file preview</td></tr>
<tr><td>1 day before</td><td>Lower the DNS TTL on key records to a few minutes</td></tr>
<tr><td>Switch day</td><td>Freeze content changes; final database sync; update DNS to the new server</td></tr>
<tr><td>Switch day</td><td>Recreate or confirm email records; issue SSL on the new server</td></tr>
<tr><td>Following days</td><td>Test forms, payments, email and speed; watch for errors</td></tr>
<tr><td>After 7+ days</td><td>Restore normal TTL; cancel the old hosting once everything is confirmed</td></tr>
</table>

<h2 id="ttl">What Does Lowering the DNS TTL Do?</h2>
<p>TTL, or time to live, tells other servers how long to remember your DNS records. If it is set to a day, some visitors may keep reaching the old server for up to a day after you switch. Lowering it to a few minutes a day before the move means the change spreads quickly. Raise it again once the move is stable.</p>

<h2 id="email">What Happens to Email?</h2>
<p>Many small businesses have email on the same hosting account as the website. When you move, decide whether email moves to the new host, stays put, or moves to a dedicated service such as Google Workspace or Zoho. Copy old mailboxes if needed, recreate MX, SPF and DKIM records, and test both sending and receiving. Our guide to <a href="/digital/blog/business-email-on-own-domain-pakistan">business email on your own domain</a> compares the options.</p>

<h2 id="wordpress">Are There Special Points for WordPress?</h2>
<p>WordPress sites need the database and files moved together, with the site address unchanged. Migration plugins or the host's migration service can help. After moving, check permalinks, image paths, caching plugins and scheduled tasks, and clear any old caches. Our backups guide explains how to keep a restorable copy.</p>

<h2 id="after">What Should You Check After the Switch?</h2>
<ul>
<li>Every main page loads over HTTPS with no warnings.</li>
<li>Contact forms send and are received.</li>
<li>Payments and order emails work on a test order.</li>
<li>Email sends and receives from every account.</li>
<li>Search Console shows no new crawl errors.</li>
<li>Page speed on mobile is at least as good as before.</li>
</ul>

<h2 id="mistakes">What Are the Most Common Hosting Move Mistakes?</h2>
<ul>
<li>Cancelling the old plan first, then discovering the backup was incomplete.</li>
<li>Forgetting email accounts, so messages bounce for days.</li>
<li>Leaving the old site editable, so new orders or posts land on the wrong server during the switch.</li>
<li>Not reissuing the SSL certificate, so visitors see security warnings.</li>
<li>Moving during a sale, Eid rush or product launch.</li>
<li>Skipping a test of the contact form, so enquiries silently stop arriving.</li>
<li>Assuming the new host copied everything without checking scheduled tasks and redirects.</li>
</ul>

<h2 id="privacy">What About Customer Data During a Move?</h2>
<p>Database copies contain customer details and orders. Transfer them securely, do not leave backup files in public folders, and delete temporary copies once the move is complete.</p>

<h2 id="help">Getting It Done</h2>
<p>We move websites as a one-off task or as part of care plans from {P['maint']} a month. See our <a href="/digital/pricing">pricing page</a>.</p>
<p>If the domain also needs to move, follow our <a href="/digital/blog/transfer-domain-to-new-registrar">domain transfer checklist</a> first.</p>
""",
    faqs=[
        ('How do I move my website to a new host without downtime?',
         "Back up everything, copy files and database to the new server, test the site there before changing DNS, lower the DNS TTL a day ahead, recreate email records, switch DNS at a quiet time, then keep the old hosting active for at least a week."),
        ('What is DNS TTL and why lower it before moving?',
         "TTL, or time to live, tells other servers how long to remember your DNS records. Lowering it to a few minutes a day before the move means visitors reach the new server soon after you switch. Raise it again once everything is stable."),
        ('Will my email stop working when I change hosting?',
         "It can, if email is hosted with the website and the records are not recreated. Decide where email will live, copy mailboxes if needed, recreate MX, SPF and DKIM records, and test sending and receiving before cancelling the old hosting."),
        ('When should I cancel my old hosting?',
         "Only after the website, forms, payments and email are confirmed working on the new host, usually after at least seven days. Keep a final backup from the old account stored separately, in case a file, mailbox or setting was missed during the move."),
        ('How do I move a WordPress site to a new host?',
         "Move the database and files together, keep the site address unchanged, and use a migration plugin or the host's migration service if available. Afterwards check permalinks, image paths, caching and scheduled tasks, and clear old caches before testing every main page again."),
        ('What should I test after moving hosting?',
         "Check that every main page loads over HTTPS, forms send and arrive, test orders and payments work, email sends and receives, Search Console shows no new errors, and mobile page speed is at least as good as it was before the move."),
        ('Website ki hosting kaise badlein bina band huye?',
         "Pehle poora backup lein, phir nayi hosting par website copy karke test karein. Aik din pehle DNS ka TTL kam kar dein, email ke records dobara banayein, aur phir DNS badlein. Purani hosting kam az kam aik hafta chalne dein jab tak sab kuch theek kaam na kare."),
    ],
    sources=[('Google Search Central — Site moves without URL changes', 'https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes'), ('Cloudflare Learning — What is DNS TTL?', 'https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/'), ('WordPress.org — Moving WordPress', 'https://developer.wordpress.org/advanced-administration/upgrade/migrating/')],
    method="The checklist and timings are editorial, based on standard hosting migration practice; Google's guidance on site moves without URL changes and WordPress.org's migration documentation were used as references. No host is named or priced. Our prices come from the published list.",
    related=['business-email-on-own-domain-pakistan', 'hosting-renewal-price-traps', 'transfer-domain-to-new-registrar'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='Need to change hosting safely?',
    wa='Hi%2C%20I%20read%20your%20hosting%20move%20guide',
)
