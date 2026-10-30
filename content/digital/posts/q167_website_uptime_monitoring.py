import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=167,
    slug='website-uptime-monitoring',
    title='Website Uptime Monitoring: Know Before Your Customers Do',
    h1='Website Uptime Monitoring for Small Businesses: Find Out Before Your Customers Do',
    crumb='Website Uptime Monitoring',
    description='Website uptime monitoring for small businesses: what to monitor, free and paid tools, routing alerts to email or WhatsApp, and what to do when an alert arrives.',
    keyword='website uptime monitoring',
    cluster=['website down alert', 'uptime monitor free', 'server monitoring small business'],
    category='Fix a Problem',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="Website uptime monitoring checks your site every few minutes from outside and alerts you when it stops responding, so you hear about problems before customers do. UptimeRobot's official pricing page, for example, lists a free plan with 50 monitors checked every 5 minutes and email alerts. Route alerts to someone who can act.",
    takeaways=["Monitoring tells you when the site is down; it does not fix anything by itself.", "Monitor the homepage, a key form or checkout page, and certificate expiry.", "Free plans cover most small businesses; paid plans add faster checks and SMS or call alerts.", "Alerts must reach someone who can act, including outside office hours.", "Keep a short written plan for what to do when an alert arrives."],
    body=f"""
<h2 id="why">Why Do Small Businesses Need Website Uptime Monitoring?</h2>
<p>Most small business owners find out their website is down when a customer calls to ask, or worse, never finds out and simply loses enquiries. Hosting failures, expired domains, certificate problems and plugin errors can take a site offline at any hour. Website uptime monitoring is a simple external check that visits your site at regular intervals and alerts you the moment it stops responding properly. It costs little or nothing, and it changes the problem from "how long has this been broken?" to "it broke ten minutes ago".</p>
<p>Downtime also hurts search, as our Google indexing guide explains. For what to do when the site is already down, see our website down checklist.</p>

<h2 id="what">What Should You Monitor?</h2>
<table>
<tr><th>Check</th><th>Why</th></tr>
<tr><td>Homepage response</td><td>Basic up or down status</td></tr>
<tr><td>Keyword on the page</td><td>Catches pages that load but show an error message</td></tr>
<tr><td>Contact or checkout page</td><td>The page that earns money</td></tr>
<tr><td>Certificate expiry</td><td>Warns before HTTPS breaks</td></tr>
<tr><td>Domain expiry</td><td>Warns before the domain lapses</td></tr>
<tr><td>Response time</td><td>Shows slowdowns before they become outages</td></tr>
</table>

<h2 id="tools">Which Tools Can You Use?</h2>
<p>Many monitoring services offer free plans. As one example, UptimeRobot's official pricing page, checked on 30 October 2026, lists a free plan with 50 monitors, checks every 5 minutes and email alerts, with SMS and voice credits sold separately, and a paid Solo plan at $12 a month billed annually. Other services offer similar free tiers with different limits; compare check intervals, alert channels and how many monitors you need on each provider's official page. Some hosting companies and Cloudflare also include basic alerts.</p>

<h2 id="alerts">Where Should Alerts Go?</h2>
<p>An alert nobody reads is useless. Send alerts to at least two people: the owner and whoever maintains the site. Email is the default; many tools also support mobile apps, SMS, or integrations with chat tools, and some can post to WhatsApp through third-party automation. Choose channels you actually check in the evening and on Sundays. Avoid alerting on every brief blip; most tools can wait for two failed checks before alerting, which cuts false alarms.</p>

<h2 id="plan">What Should You Do When an Alert Arrives?</h2>
<ol>
<li>Open the site on mobile data, not office Wi-Fi, to confirm it is really down.</li>
<li>Check the monitoring tool's error: timeout, server error, certificate or DNS.</li>
<li>Check whether the domain or hosting has expired.</li>
<li>Contact the host's support with the time and error message.</li>
<li>If a recent change caused it, roll back the change.</li>
<li>Post a short update on WhatsApp status or social media if it lasts long.</li>
</ol>
<p>Write these steps down with your host's support contact and your developer's number, so anyone on the team can follow them.</p>

<h2 id="reports">What Do Uptime Reports Tell You?</h2>
<p>Monthly uptime figures and response times show whether your host is reliable. Repeated short outages, or slow responses at busy times, are evidence when asking for a better plan or deciding to move. Our guide to <a href="/digital/blog/move-website-to-new-hosting">moving to a new host</a> explains how to switch safely if the reports point that way.</p>

<h2 id="status">Should You Have a Status Page?</h2>
<p>For most small businesses, no. A short message on WhatsApp status, Instagram or your Google Business Profile during a long outage is enough. Online stores and software products with many daily users can benefit from a simple public status page, which many monitoring tools provide, so customers can check before calling. Keep updates brief, honest and timed.</p>

<h2 id="privacy">Does Monitoring Involve Personal Data?</h2>
<p>Basic monitoring only visits public pages, so it does not handle customer data. Avoid monitoring tools that require storing customer login details, and keep the monitoring account secured with two-step verification.</p>

<h2 id="help">Monitoring in Our Care Plans</h2>
<p>Our care plans, from {P['maint']} a month, include uptime, certificate and domain expiry monitoring with alerts to our team and yours. Our <a href="/digital/blog/ssl-certificate-https-explained">SSL guide</a> explains why certificate alerts matter. See our <a href="/digital/pricing">pricing page</a>.</p>
""",
    faqs=[
        ('What is website uptime monitoring?',
         "It is an external service that checks your website at regular intervals, often every few minutes, and alerts you when it stops responding or shows an error. It tells you about problems quickly, so you can fix them before many customers notice, but it does not fix anything by itself."),
        ('Is there a free website uptime monitor?',
         "Yes. Several services have free plans. For example, UptimeRobot's official pricing page, checked 30 October 2026, lists a free plan with 50 monitors, checks every five minutes and email alerts. Compare limits and alert channels on each provider's official page before choosing."),
        ('What should a small business monitor on its website?',
         "Monitor the homepage, a keyword on an important page, the contact or checkout page, certificate expiry, domain expiry and response time. Together these catch outages, error pages, expiring HTTPS and the slowdowns that often come before a full failure of the site."),
        ('Can I get website down alerts on WhatsApp?',
         "Some monitoring tools offer mobile apps, SMS or chat integrations, and alerts can reach WhatsApp through third-party automation. Whatever channel you choose, make sure at least two people receive alerts and that someone checks them in the evenings and at weekends."),
        ('What should I do when I get a website down alert?',
         "Confirm on mobile data that the site is really down, read the error in the monitoring tool, check domain and hosting expiry, contact your host's support with the time and error, and roll back any recent change. Keep these steps written down for your team."),
        ('How often should uptime be checked?',
         "Every five minutes is enough for most small businesses and is common on free plans. Online stores with heavy traffic may prefer faster checks on a paid plan. Setting alerts to trigger after two failed checks cuts false alarms from brief network blips."),
        ('Website band ho jaye to pata kaise chale?',
         "Uptime monitoring tool lagayen jo har chand minute baad website check kare aur band hone par email ya app par alert bheje. Kai tools ka free plan hai. Alert kam az kam do logon ko jaye, aur pehle se likh lein ke alert aane par kya karna hai aur hosting support ka number kya hai."),
    ],
    sources=[('UptimeRobot — Pricing', 'https://uptimerobot.com/pricing/'), ('Cloudflare — Plans', 'https://www.cloudflare.com/plans/'), ('Google Search Central — Handling site outages', 'https://developers.google.com/search/docs/crawling-indexing/http-network-errors')],
    method="Free and paid plan details for UptimeRobot come from its official pricing page, checked 30 October 2026, and are given as one example. The monitoring table, alert advice and response steps are editorial. Our prices come from the published list.",
    related=['move-website-to-new-hosting', 'ssl-certificate-https-explained', 'transfer-domain-to-new-registrar'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='Find out first when your site goes down',
    wa='Hi%2C%20I%20read%20your%20uptime%20monitoring%20guide',
)
