import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=168,
    slug='wordpress-updates-safely',
    title='How to Update WordPress Safely: Plugins, Themes, Core',
    h1='How to Update WordPress Safely: Plugins, Themes and Core Without Breaking Your Site',
    crumb='Update WordPress Safely',
    description='How to update WordPress safely: back up first, test on staging, update in the right order, check the site afterwards and roll back if an update breaks it.',
    keyword='update wordpress safely',
    cluster=['wordpress update broke site', 'plugin updates', 'staging site wordpress'],
    category='Fix a Problem',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="To update WordPress safely, take a full backup, test updates on a staging copy, then update the live site in order: plugins one at a time, then themes, then core, checking key pages after each. Keep a way to roll back. Updating about 1 time a week, or monthly with urgent security fixes sooner, keeps risk low.",
    takeaways=["Outdated plugins and themes are a leading cause of hacked WordPress sites.", "A recent, restorable backup is the first step before any update.", "Staging lets you find conflicts without customers seeing a broken site.", "Update one plugin at a time so you know which one caused a problem.", "After updating, test forms, checkout and key pages, not just the homepage."],
    body=f"""
<h2 id="why">Why Is It Important to Update WordPress Safely?</h2>
<p>WordPress, its themes and plugins release updates regularly, many fixing security holes. Skipping updates leaves sites open to attacks that target known weaknesses; WordPress.org's security guidance stresses keeping everything up to date. Yet owners hesitate, because an update can occasionally break a layout, a form or a checkout. The answer is a routine that lets you update WordPress safely: backup, staging, careful order, testing and a rollback plan.</p>
<p>Updates sit with the other ownership tasks linked from our Google starter guide. It works alongside our security checklist.</p>

<h2 id="routine">What Is a Safe Update Routine?</h2>
<table>
<tr><th>Step</th><th>What to do</th></tr>
<tr><td>1. Back up</td><td>Full backup of files and database, stored off the server</td></tr>
<tr><td>2. Read notes</td><td>Check changelogs for major version changes or warnings</td></tr>
<tr><td>3. Staging</td><td>Apply updates on a staging copy first</td></tr>
<tr><td>4. Test staging</td><td>Check homepage, key pages, forms, checkout, admin</td></tr>
<tr><td>5. Update live</td><td>Plugins one at a time, then theme, then core</td></tr>
<tr><td>6. Test live</td><td>Repeat key checks; place a test order if you sell online</td></tr>
<tr><td>7. Record</td><td>Note what was updated and when</td></tr>
</table>
<p>Our backups guide explains how to make backups you can actually restore.</p>

<h2 id="order">Why Does the Order Matter?</h2>
<p>Updating plugins one at a time means that if something breaks, you know exactly which update caused it. Plugins often need a recent WordPress version, so check compatibility notes; when a plugin requires a newer core, update core first on staging and test. Themes come after plugins because many themes depend on plugin features. Major WordPress versions deserve extra care: wait a few days after release for early fixes unless the update is a security release.</p>

<h2 id="auto">Should You Turn On Automatic Updates?</h2>
<p>WordPress can apply minor core releases automatically, and you can enable automatic updates for plugins and themes. Automatic minor and security updates are sensible for most sites. Automatic major plugin updates on a busy online store are riskier, because nobody tests before customers see the result. A common compromise: automatic security and minor updates, with a weekly manual round for everything else.</p>

<h2 id="broke">What If an Update Breaks the Site?</h2>
<ol>
<li>Note the error message and which update was last applied.</li>
<li>If you can reach the admin area, deactivate or roll back that plugin.</li>
<li>If the admin is unreachable, rename the plugin's folder through your host's file manager to disable it.</li>
<li>If that fails, restore the backup taken before updating.</li>
<li>Report the problem to the plugin developer and wait for a fix before updating again.</li>
</ol>

<h2 id="staging">How Do You Get a Staging Site?</h2>
<p>Many hosts offer one-click staging. Otherwise, a developer can create a password-protected copy on a subdomain. Staging should be blocked from search engines so it does not compete with the live site.</p>

<h2 id="php">What About PHP and Server Updates?</h2>
<p>WordPress runs on PHP, and hosts retire old PHP versions over time. Plugins increasingly require newer versions, so a site stuck on old PHP eventually cannot update at all. Check your PHP version in the host's control panel, test a newer version on staging, and switch once forms, checkout and admin all work. This is often the update owners forget.</p>

<h2 id="log">Why Keep an Update Log?</h2>
<p>A simple log, listing the date, what was updated and anything that went wrong, turns problems into quick fixes. When something breaks a week later, the log shows what changed. It also helps a new developer take over without guessing.</p>

<h2 id="privacy">What About Customer Data on Staging?</h2>
<p>Staging copies of online stores contain real customer data. Protect them with passwords, keep them out of search engines, and consider removing or anonymising customer records on staging.</p>

<h2 id="help">Updates in Our Care Plans</h2>
<p>Our care plans, from {P['maint']} a month, include tested updates, backups and rollback. Sites with many plugins benefit from a clean-up first; see our <a href="/digital/blog/too-many-wordpress-plugins">plugin audit guide</a>. See our <a href="/digital/pricing">pricing page</a>.</p>
<p>Keep the domain safe too: our <a href="/digital/blog/transfer-domain-to-new-registrar">domain transfer guide</a> explains locks and transfer codes.</p>
""",
    faqs=[
        ('How do I update WordPress safely?',
         "Take a full backup, test updates on a staging copy, then update the live site in order: plugins one at a time, then themes, then core, checking important pages after each step. Keep a rollback method ready and record what you updated and when."),
        ('Why did a WordPress update break my site?',
         "Usually because of a conflict between a plugin, the theme and the WordPress version, or a plugin that needs a newer PHP or core version. Updating one item at a time on staging first shows which update causes the problem before customers see it."),
        ('Should I turn on automatic WordPress updates?',
         "Automatic minor and security updates are sensible for most sites. Automatic major plugin updates are riskier on busy online stores, because nobody tests them first. A common approach is automatic security updates plus a weekly manual round for everything else, tested on staging."),
        ('What do I do if I cannot log in after an update?',
         "Disable the last updated plugin by renaming its folder through your host's file manager, which usually restores access. If that does not work, restore the backup taken before updating. Report the problem to the plugin developer and wait for a fixed version."),
        ('How often should WordPress be updated?',
         "Weekly or every two weeks suits most small business sites, with critical security updates applied as soon as possible. Waiting a few days after a major WordPress release, unless it is a security fix, lets early problems be found and fixed by others first."),
        ('What is a WordPress staging site?',
         "A staging site is a private copy of your website where updates and changes are tested before going live. Many hosts offer one-click staging. It should be password-protected and hidden from search engines, and any customer data on it should be protected or anonymised."),
        ('WordPress ko mehfooz tareeqe se update kaise karein?',
         "Pehle poora backup lein, phir staging copy par update test karein. Live site par plugins aik aik karke update karein, phir theme aur aakhir mein WordPress core. Har qadam ke baad forms aur checkout check karein. Agar site kharab ho jaye to aakhri plugin band karein ya backup wapas lagayen."),
    ],
    sources=[('WordPress.org — Hardening WordPress', 'https://developer.wordpress.org/advanced-administration/security/hardening/'), ('WordPress.org — Configuring automatic background updates', 'https://developer.wordpress.org/advanced-administration/upgrade/upgrading/'), ('WordPress.org — Backups', 'https://developer.wordpress.org/advanced-administration/security/backup/')],
    method="Update and security points reflect WordPress.org administration documentation. The routine, order and recovery steps are editorial, based on standard maintenance practice. No figures on hacked sites are given. Our prices come from the published list.",
    related=['too-many-wordpress-plugins', 'transfer-domain-to-new-registrar', 'move-website-to-new-hosting'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='Afraid to press update?',
    wa='Hi%2C%20I%20read%20your%20WordPress%20updates%20guide',
)
