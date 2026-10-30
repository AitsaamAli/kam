import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=165,
    slug='ssl-certificate-https-explained',
    title='SSL Certificate for Website: What Owners Need to Know',
    h1='SSL Certificate for Your Website and HTTPS: What Every Owner Needs to Know',
    crumb='SSL Certificate and HTTPS',
    description="An SSL certificate for your website explained: what HTTPS does, free Let's Encrypt certificates, why renewals fail, mixed content warnings and when to pay for one.",
    keyword='ssl certificate for website',
    cluster=['https website', 'free ssl lets encrypt', 'website not secure warning'],
    category='Fix a Problem',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="An SSL certificate for your website enables HTTPS, which encrypts data between visitors and your site and removes the \"Not secure\" warning. Free certificates from Let's Encrypt suit most small businesses; they last 90 days and should renew automatically about every 60 days. Most problems come from failed renewals or mixed content.",
    takeaways=["Every website needs HTTPS, not only shops; browsers warn visitors on pages without it.", "Let's Encrypt certificates are free and suit most small business websites.", "Let's Encrypt certificates last 90 days, so automatic renewal is essential.", "Mixed content, such as images loaded over plain HTTP, breaks the padlock.", "Paid certificates add organisation validation and support, not stronger encryption."],
    body=f"""
<h2 id="what">What Does an SSL Certificate for a Website Do?</h2>
<p>When you see a padlock and https:// in the address bar, the connection between the visitor's browser and the website is encrypted. An SSL certificate for your website, more accurately called a TLS certificate today, makes that possible. It stops anyone between the visitor and your server, on public Wi-Fi for example, from reading or changing what is sent: form entries, passwords, order details. It also proves the visitor is talking to your domain and not an impostor.</p>
<p>Without HTTPS, browsers label pages "Not secure", which scares visitors away, especially on forms and checkouts. Certificates are also a search factor covered in our Google basics guide.</p>

<h2 id="free-vs-paid">Free or Paid Certificate?</h2>
<table>
<tr><th>Type</th><th>Cost</th><th>Validation</th><th>Suits</th></tr>
<tr><td>Let's Encrypt (domain validated)</td><td>Free</td><td>Proves control of the domain</td><td>Most small business sites and stores</td></tr>
<tr><td>Host-provided free certificate</td><td>Included with hosting</td><td>Usually domain validated</td><td>Same as above</td></tr>
<tr><td>Paid organisation validated</td><td>Annual fee</td><td>Also checks the organisation exists</td><td>Larger firms with specific policy needs</td></tr>
</table>
<p>The encryption strength is the same; paid certificates add identity checks, warranties and vendor support. Let's Encrypt's FAQ states its certificates are free, though some hosting providers may charge a small fee to cover their own costs of setting them up.</p>

<h2 id="renewal">Why Do Certificates Expire and Renewals Fail?</h2>
<p>Let's Encrypt certificates are valid for 90 days by default, and its FAQ recommends renewing every 60 days. Hosts and control panels normally renew automatically. Renewals fail when DNS has moved to another provider, the domain points to a different server, a firewall blocks the verification request, or a site was migrated and the old automation stopped. When that happens, visitors see a full-page browser warning, which is far worse than the old "Not secure" label. Set up an alert for certificate expiry; our <a href="/digital/blog/website-uptime-monitoring">uptime monitoring guide</a> covers tools that check this.</p>

<h2 id="mixed-content">What Is Mixed Content?</h2>
<p>A page loaded over HTTPS that pulls in images, scripts or styles over plain HTTP has mixed content. Browsers may block those items or remove the padlock. It often appears after moving a site to HTTPS when old content still uses http:// links. Fix it by updating links in the database and theme, and check pages with the browser's developer console.</p>

<h2 id="switch">How Do You Move a Site to HTTPS Properly?</h2>
<ol>
<li>Install the certificate and confirm the site loads on https://.</li>
<li>Redirect every http:// address to its https:// version with permanent redirects.</li>
<li>Update internal links, images and scripts to https://.</li>
<li>Update the site address in your CMS settings.</li>
<li>Add the HTTPS version to Google Search Console and check for errors.</li>
</ol>
<p>Google's guidance on site moves applies, since the protocol change alters every URL; see our guide to changing websites without losing traffic.</p>

<h2 id="warnings">Which Warnings Should Worry You?</h2>
<ul>
<li><strong>"Not secure" in the address bar:</strong> no HTTPS, or a page with a form loaded over HTTP.</li>
<li><strong>"Your connection is not private":</strong> expired, mismatched or invalid certificate; fix immediately.</li>
<li><strong>Padlock missing on some pages:</strong> mixed content on those pages.</li>
</ul>

<h2 id="checks">How Can You Check Your Certificate Yourself?</h2>
<p>Click the padlock in the browser address bar and open the certificate details. You will see who issued it, which domain names it covers and its expiry date. Check both the www and non-www versions of your address, and any subdomains such as shop.yourbusiness.pk, because a certificate that covers one may not cover the others. Put the expiry date in a calendar as a backup to automatic alerts.</p>

<h2 id="privacy">Why Does HTTPS Matter for Privacy?</h2>
<p>Contact forms, logins and checkouts send personal data. Without HTTPS, that data travels unencrypted. HTTPS is a basic expectation of data protection rules in many countries.</p>

<h2 id="help">How We Handle It</h2>
<p>Every site we build, from {P['starter']}, uses HTTPS with automatic renewal, and our care plans from {P['maint']} a month include expiry monitoring. Our security checklist lists the related basics. See our <a href="/digital/pricing">pricing page</a>.</p>
<p>For moving the domain itself, see our <a href="/digital/blog/transfer-domain-to-new-registrar">step-by-step domain transfer guide</a>.</p>
""",
    faqs=[
        ('What is an SSL certificate for a website?',
         "It is a small file installed on your web server that enables HTTPS, encrypting data between visitors' browsers and your site and proving visitors are connected to your real domain. Today it is technically a TLS certificate, but most people still call it SSL."),
        ('Is a free SSL certificate good enough for a business?',
         "For most small businesses and online stores, yes. Let's Encrypt certificates provide the same encryption strength as paid ones. Paid certificates add organisation validation, warranties and vendor support, which some larger organisations require for policy reasons, but encryption is identical."),
        ("How long does a Let's Encrypt certificate last?",
         "Let's Encrypt certificates are valid for 90 days by default, and its FAQ recommends renewing every 60 days. Hosts and control panels normally do this automatically, but it is worth setting an expiry alert in case automatic renewal fails after a DNS or server change."),
        ('Why does my website say Not secure?',
         "Either the site has no certificate and loads over plain HTTP, or a page, often one with a form, loads some content over HTTP. Install a certificate, redirect all HTTP addresses to HTTPS, and fix any mixed content links in your pages and theme."),
        ('What is mixed content and how do I fix it?',
         "Mixed content happens when an HTTPS page loads images, scripts or styles over plain HTTP. Browsers may block them or remove the padlock. Update old http links in your database, theme and settings to https, then check affected pages using the browser's developer console."),
        ('Why did my SSL certificate stop renewing?',
         "Common causes are DNS moved to another provider, the domain pointing to a different server, a firewall blocking the verification request, or a migration that left the old renewal automation behind. Check where the domain points, then reissue the certificate on the current server."),
        ('SSL certificate kya hai aur zaroori kyun hai?',
         "SSL certificate website par HTTPS chalata hai, jis se visitor aur website ke darmiyan data mehfooz rehta hai aur browser Not secure ka nishan nahin dikhata. Let's Encrypt ka muft certificate aksar businesses ke liye kaafi hai. Yeh 90 din chalta hai, is liye khud ba khud renew hona zaroori hai."),
    ],
    sources=[("Let's Encrypt — FAQ", 'https://letsencrypt.org/docs/faq/'), ('MDN Web Docs — Mixed content', 'https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content'), ('Google Search Central — HTTPS as a ranking signal', 'https://developers.google.com/search/blog/2014/08/https-as-ranking-signal'), ('Google Search Central — Site moves with URL changes', 'https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes')],
    method="Certificate lifetime (90 days), renewal advice (every 60 days) and the free status come from Let's Encrypt's FAQ, checked 30 October 2026. The free versus paid table and warnings list are editorial. Our prices come from the published list.",
    related=['website-uptime-monitoring', 'cloudflare-for-small-business-website', 'transfer-domain-to-new-registrar'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='Seeing a Not secure warning?',
    wa='Hi%2C%20I%20read%20your%20SSL%20certificate%20guide',
)
