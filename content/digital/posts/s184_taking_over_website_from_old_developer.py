import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=184,
    slug='taking-over-website-from-old-developer',
    title='Take Over a Website From a Previous Developer Safely',
    h1='How to Take Over a Website From a Previous Developer: Access, Audit and First-Week Fixes',
    crumb='Take Over a Website',
    description='How to take over a website from a previous developer: recovering access, auditing the site, securing accounts and the fixes to make in the first week.',
    keyword='take over website from developer',
    cluster=['new developer for existing website', 'website handover from old developer', 'inherited website problems'],
    category='Hiring a Developer',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="To take over a website from a previous developer, first recover owner access to the domain, hosting, website admin and email, then take a full backup, change all passwords and audit the site: software versions, plugins, security, speed and forms. Fix urgent problems in the first week and plan the rest, without rushing a rebuild.",
    takeaways=["Access comes first: domain, hosting, website admin, email, analytics and DNS.", "Take a full backup before changing anything.", "Change every password and remove the old developer's accounts once access is secure.", "Audit before rebuilding; many inherited sites need fixes, not replacement.", "Document what you find so the next handover is easier."],
    body=f"""
<h2 id="situation">Why Is It Tricky to Take Over a Website From a Developer?</h2>
<p>Developers move on, freelancers disappear and agencies close. Sometimes the relationship simply ended badly. Whatever the reason, many Pakistani businesses find themselves needing to take over a website from a previous developer who held all the logins and left no notes. Done carefully, the takeover can be smooth. Done carelessly, it can lead to lost email, a hacked site or a domain that expires because nobody knew the renewal date.</p>
<p>When choosing who takes over, these selection criteria apply too. It pairs with our website handover checklist.</p>

<h2 id="access">Which Access Do You Need to Recover?</h2>
<table>
<tr><th>Account</th><th>Why it matters</th><th>How to recover if missing</th></tr>
<tr><td>Domain registrar</td><td>Controls the address, DNS and renewals</td><td>Registrar support with proof of ownership</td></tr>
<tr><td>Hosting</td><td>Holds the site files, database and often email</td><td>Host support, billing records</td></tr>
<tr><td>Website admin</td><td>Content, users and settings</td><td>Password reset via email, or hosting access</td></tr>
<tr><td>Email service</td><td>Business communication</td><td>Provider support; admin account recovery</td></tr>
<tr><td>DNS provider (if separate)</td><td>Points domain to hosting and email</td><td>Provider support</td></tr>
<tr><td>Analytics and Search Console</td><td>Traffic history and search data</td><td>Add new owner via domain verification</td></tr>
<tr><td>Code repository, if any</td><td>Source code for custom work</td><td>Ask the previous developer; contract terms</td></tr>
</table>
<p>If the domain is registered in the old developer's name, recovering it is the top priority; our guide to website ownership explains why, and our <a href="/digital/blog/transfer-domain-to-new-registrar">domain transfer guide</a> explains the process.</p>

<h2 id="secure">How Do You Secure Everything?</h2>
<ol>
<li>Take a full backup of files, database and email.</li>
<li>Change passwords on every account, starting with email and domain.</li>
<li>Turn on two-step verification.</li>
<li>Remove the old developer's user accounts and any unknown admin users.</li>
<li>Check DNS records and note what each does.</li>
<li>Note renewal dates for domain, hosting, licences and certificates.</li>
</ol>

<h2 id="audit">What Should the Audit Check?</h2>
<ul>
<li>Software versions: CMS, plugins, themes, server software.</li>
<li>Unused, abandoned or pirated plugins.</li>
<li>Signs of malware or unknown files.</li>
<li>Forms: do messages arrive, and where?</li>
<li>Speed on mobile.</li>
<li>Backups: do any exist, and do they restore?</li>
<li>Search Console errors and indexing.</li>
<li>Custom code: is it documented, and does anyone understand it?</li>
</ul>
<p>Our guides to <a href="/digital/blog/too-many-wordpress-plugins">plugin audits</a> and website security go deeper.</p>

<h2 id="first-week">What Should Be Fixed in the First Week?</h2>
<p>Anything that risks losing data, customers or access: missing backups, critical security updates, broken forms, expired or expiring certificates and domains, and malware. Everything else, such as design changes, speed improvements and content updates, can be planned calmly once the site is stable.</p>

<h2 id="rebuild">Should You Rebuild Instead?</h2>
<p>Not automatically. A rebuild makes sense when the site is on an abandoned platform, heavily hacked, impossible to update or no longer fits the business. Often, a cleaned-up, updated site serves well for years. Decide after the audit, not before.</p>

<h2 id="document">Why Should You Document Everything Now?</h2>
<p>The takeover is the moment to create the notes the previous developer never left: a list of accounts and who holds them, renewal dates, plugins and licences, custom code and what it does, and where backups live. Keep this document with the business, not with any developer, and update it after every significant change. The next handover, whenever it comes, will then take hours instead of weeks.</p>

<h2 id="privacy">What About Data the Old Developer Holds?</h2>
<p>The previous developer may have copies of your database, customer data or backups. Ask in writing for them to be deleted, and confirm it. If customer data was exposed, take advice on your obligations.</p>

<h2 id="ours">How We Take Over Sites</h2>
<p>We recover access, back up, secure and audit inherited websites, then recommend fixes or a rebuild with prices. Ongoing care starts from {P['maint']} a month. See our <a href="/digital/pricing">pricing page</a>.</p>
""",
    faqs=[
        ('How do I take over a website from my previous developer?',
         "Recover owner access to the domain, hosting, website admin, email, DNS and analytics first. Then take a full backup, change every password, turn on two-step verification, remove the old developer's accounts and audit the site before deciding on fixes or a rebuild."),
        ('What if my old developer will not give me the logins?',
         "Contact the domain registrar, hosting company and email provider directly with proof of ownership, such as invoices, business documents or billing records. They have recovery processes. If the domain is registered in the developer's name, check your contract and take advice."),
        ('What should a new developer check on an inherited website?',
         "Software and plugin versions, abandoned or pirated plugins, signs of malware, whether forms deliver messages, mobile speed, existing backups and whether they restore, Search Console errors, and whether any custom code is documented and understood well enough for another developer to maintain it."),
        ('Should I rebuild a website I inherited from another developer?',
         "Not automatically. Rebuild if the site runs on an abandoned platform, is heavily hacked, cannot be updated or no longer fits the business. Otherwise, a cleaned-up, updated site may serve well for years. Decide after a proper audit rather than before."),
        ('What should be fixed first on a taken-over website?',
         "Anything that risks losing data, customers or access: missing backups, critical security updates, broken forms, expiring certificates or domains, and malware. Design, speed and content improvements can follow calmly, in a planned order, once the site is stable and secure again."),
        ('What about customer data my old developer still has?',
         "Ask the previous developer in writing to delete any copies of your database, customer data or backups, and to confirm deletion. If you believe customer data was exposed or misused, take advice promptly on your obligations to the customers and other people affected."),
        ('Purane developer se website kaise wapas lein?',
         "Sab se pehle domain, hosting, website admin aur email ka owner access hasil karein. Phir poora backup lein, tamam passwords badlein, purane developer ke accounts hata dein aur website ka audit karwayen. Pehle hafte sirf zaroori masail theek karein, naye sire se banana baad mein sochein."),
    ],
    sources=[('ICANN — FAQs for domain name holders (transfers)', 'https://www.icann.org/resources/pages/name-holder-faqs-2017-10-10-en'), ('Google Search Console Help — Add or remove owners', 'https://support.google.com/webmasters/answer/7687615'), ('WordPress.org — Hardening WordPress', 'https://developer.wordpress.org/advanced-administration/security/hardening/')],
    method="The access table, security steps and audit list are editorial, based on standard takeover practice. Domain transfer rules refer to ICANN's FAQ, checked 30 October 2026. This is general guidance, not legal advice. Our prices come from the published list.",
    related=['transfer-domain-to-new-registrar', 'website-discovery-meeting-what-to-expect', 'how-to-give-website-design-feedback'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='Stuck with a site from an old developer?',
    wa='Hi%2C%20I%20read%20your%20website%20takeover%20guide',
)
