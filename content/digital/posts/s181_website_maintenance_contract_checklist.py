import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=181,
    slug='website-maintenance-contract-checklist',
    title='Website Maintenance Contract: What to Agree in Writing',
    h1='Website Maintenance Contract Checklist: Response Times, Exclusions, Access and Exit Terms',
    crumb='Website Maintenance Contract',
    description='What a website maintenance contract should cover: tasks included, response times, exclusions, hours, access and ownership, backups, price changes and how to exit.',
    keyword='website maintenance contract',
    cluster=['maintenance agreement website', 'sla website support', 'website support terms'],
    category='Hiring a Developer',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer=f"A website maintenance contract should list exactly which tasks are included, such as updates, backups, monitoring and a number of small changes, plus response times by severity, what is excluded, who holds access, how backups are restored, how prices can change and how either side can end it. Our care plans start from {P['maint']} a month.",
    takeaways=["Vague promises like full support cause disputes; list tasks and limits.", "Response times should differ by severity: site down, feature broken, minor issue.", "You should keep owner-level access to hosting, domain and the website at all times.", "Backups need a stated frequency, storage location and a tested restore.", "Exit terms and handover duties protect you if the relationship ends."],
    body=f"""
<h2 id="why">Why Do You Need a Website Maintenance Contract?</h2>
<p>Once a website is live, someone must keep it updated, backed up and working. Many Pakistani businesses agree this informally with their developer: "we will look after it". Months later, when the site goes down on a Friday evening or a plugin update breaks the checkout, it turns out nobody agreed what "looking after it" meant, how fast problems are fixed or what is charged extra. A written website maintenance contract settles these questions in advance.</p>
<p>Picking the provider comes first; our selection guide lists what to check. For prices, see our website maintenance charges guide.</p>

<h2 id="checklist">What Should the Contract Cover?</h2>
<table>
<tr><th>Clause</th><th>What to agree</th></tr>
<tr><td>Included tasks</td><td>Updates, backups, monitoring, security checks, a set number of small changes or hours</td></tr>
<tr><td>Response times</td><td>By severity, with working hours stated</td></tr>
<tr><td>Exclusions</td><td>New features, redesigns, content writing, third-party outages</td></tr>
<tr><td>Extra work</td><td>Hourly rate or quote process for anything outside the plan</td></tr>
<tr><td>Access and ownership</td><td>You keep owner-level access; the provider has its own accounts</td></tr>
<tr><td>Backups</td><td>Frequency, storage location, retention period, restore tests</td></tr>
<tr><td>Reporting</td><td>Monthly summary of updates, issues and time used</td></tr>
<tr><td>Price and term</td><td>Monthly fee, payment terms, notice for price changes</td></tr>
<tr><td>Exit</td><td>Notice period, handover of access and documentation</td></tr>
</table>

<h2 id="response">How Should Response Times Work?</h2>
<p>An illustrative structure: site down or checkout broken, response within a few working hours; a feature not working, within one working day; minor issues and small changes, within a few working days. State working hours plainly; for us that is Monday to Saturday, 9:00 AM to 6:00 PM, with Friday until 12:30 PM. If you need out-of-hours cover, agree it and its price explicitly.</p>

<h2 id="exclusions">What Is Usually Excluded?</h2>
<ul>
<li>New pages, features or redesigns, which are quoted separately.</li>
<li>Writing content or taking photos.</li>
<li>Problems caused by third parties, such as a payment gateway outage, though the provider should help diagnose them.</li>
<li>Damage from changes made by someone else without coordination.</li>
<li>Licence fees for premium plugins or services, unless included.</li>
</ul>
<p>Clear exclusions are fair to both sides; they prevent the plan from silently turning into unlimited development.</p>

<h2 id="access">Why Does Access Matter?</h2>
<p>Your business should own the domain, hosting and website accounts, with the provider given its own user access. Never let a maintenance provider be the only holder of owner logins. If the relationship ends badly, you must still be able to reach your site. Our guide to who owns your website explains this in detail.</p>

<h2 id="backups">What Should the Backup Clause Say?</h2>
<p>How often backups run, where they are stored (ideally off the hosting server), how long they are kept, and how often a test restore is done. A backup that has never been restored is a hope, not a plan. Our backups guide sets out a sensible routine.</p>

<h2 id="exit">How Should Exit Terms Work?</h2>
<p>Agree a notice period, for example one month, and what the provider hands over: access removal confirmation, documentation of custom work, the latest backup and a list of plugins and licences. Our guide to <a href="/digital/blog/taking-over-website-from-old-developer">taking over a website</a> shows why this matters for whoever comes next.</p>

<h2 id="reports">What Should Monthly Reports Show?</h2>
<p>A short monthly report should list updates applied, backups taken and tested, uptime, issues fixed, small changes made and hours used against the plan. It shows you are getting what you pay for, and it builds a history that helps when something goes wrong or a new provider takes over.</p>

<h2 id="privacy">Should the Contract Cover Data Protection?</h2>
<p>Yes, if the provider can access customer data in forms, orders or emails. Add confidentiality terms, and for UK or EU customers a data processing agreement.</p>

<h2 id="ours">Our Care Plans</h2>
<p>Our care plans start from {P['maint']} a month and list tasks, response times and exclusions in writing. See our <a href="/digital/pricing">pricing page</a>.</p>
<p>See also <a href="/digital/blog/website-discovery-meeting-what-to-expect">Your First Website Discovery Meeting</a>.</p>
""",
    faqs=[
        ('What should a website maintenance contract include?',
         "Included tasks, response times by severity, working hours, exclusions, the rate or process for extra work, access and ownership terms, backup frequency and restore tests, monthly reporting, the fee and notice for price changes, and exit terms with a handover of access and documentation."),
        ('What response time should I expect from website support?',
         "It should depend on severity. A site that is down or a broken checkout needs the fastest response, often within a few working hours, while minor issues may take a few working days. Agree working hours in writing and pay separately for out-of-hours cover if needed."),
        ('What is usually excluded from website maintenance?',
         "New pages, features and redesigns, content writing and photography, problems caused by third-party outages, damage from uncoordinated changes by others, and licence fees for premium plugins unless the contract includes them. Clear exclusions prevent a care plan becoming unlimited development."),
        ('Should my maintenance provider hold my website logins?',
         "They should have their own user access, but your business must keep owner-level access to the domain, hosting and website. Never let a provider be the only holder of owner logins, because you could lose control of your site if the relationship ends."),
        ('How often should website backups be taken?',
         "It depends on how often the site changes. Many small business sites back up daily, while busy online stores may need more frequent backups. The contract should state frequency, storage location off the hosting server, retention period and how often restores are tested."),
        ('How do I end a website maintenance contract?',
         "Follow the agreed notice period, often one month, then collect a handover: confirmation that the provider's access is removed, documentation of custom work, the latest backup and a list of plugins and licences. Change passwords once the handover is complete."),
        ('Website maintenance ka muahida kaise likhwayen?',
         "Likh kar tay karein ke kaun se kaam shamil hain, masla hone par kitni der mein jawab milega, kya shamil nahin, extra kaam ka rate kya hai, backup kab aur kahan hoga, aur muahida khatam karne ka tareeqa kya hai. Domain aur hosting ka owner access hamesha apne paas rakhein."),
    ],
    sources=[('OWASP — Top 10 web application security risks', 'https://owasp.org/www-project-top-ten/'), ('WordPress.org — Backups', 'https://developer.wordpress.org/advanced-administration/security/backup/'), ('ICO — UK GDPR guidance and resources', 'https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/')],
    method="The clause checklist and response-time structure are editorial and labelled illustrative. Our office hours and care plan price are approved business facts from the published list. This is general guidance, not legal advice.",
    related=['non-technical-owner-managing-developer', 'website-discovery-meeting-what-to-expect', 'how-to-give-website-design-feedback'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='Need maintenance terms in writing?',
    wa='Hi%2C%20I%20read%20your%20maintenance%20contract%20guide',
)
