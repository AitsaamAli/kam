import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=93,
    slug="website-down-check",
    title="Website Down Check: Find the Cause in 10 Minutes",
    h1="Website Down? A 10-Minute Check to Find the Cause and Know Who to Call",
    crumb="Website Down Check",
    description="Website down check in 10 minutes: is it just you, has the domain or SSL expired, is hosting suspended, or did an update break it? Plus who to call for each cause.",
    keyword="website down check",
    cluster=["why is my website not opening", "website not working", "site down for me", "domain expired website down",
             "website showing 500 error", "website nahin khul rahi"],
    category="Fix a Problem",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("A website down check takes about 10 minutes: first test on mobile data and another device to see if it is down for everyone, "
            "then check whether the domain or SSL certificate has expired, whether the hosting account is suspended or full, and whether "
            "a recent update caused an error. Each cause has a different person to call."),
    takeaways=[
        "First confirm the site is down for everyone, not just your office network or browser.",
        "Expired domains and SSL certificates are among the most common and easiest causes to fix.",
        "Hosting suspensions often follow an unpaid invoice or a site using too many resources.",
        "A blank page or server error straight after an update usually points to a plugin or theme conflict.",
        "Knowing who controls the domain, hosting and code saves hours when something breaks.",
    ],
    body=f"""
<h2 id="ten-minute-check">How Do You Run a Website Down Check?</h2>
<p>When your website stops opening, customers cannot find you and the phone goes quiet. Before calling anyone, spend ten minutes working out what kind of problem it is. The steps below go from the quickest checks to the more technical ones, and the table at the end tells you who to contact for each cause.</p>

<h2 id="step-1">Step 1: Is It Down for Everyone or Just You?</h2>
<ol>
<li>Open the site on your phone using mobile data, not office Wi-Fi.</li>
<li>Try another browser, or a private window, to rule out your browser cache.</li>
<li>Ask someone in another city to open it.</li>
</ol>
<p>If it works elsewhere, the problem is likely your network, browser or a local DNS cache, not the website. Restart your router or try again later. If it fails everywhere, continue.</p>

<h2 id="step-2">Step 2: Has the Domain Expired?</h2>
<p>An expired domain is one of the most common causes, and one of the easiest to fix if caught quickly. Look up your domain with ICANN's lookup tool for generic domains such as .com, or ask your registrar for .pk domains, and check the expiry date. Signs include a parking page or advertisements in place of your site, and email stopping at the same time. Renew immediately; some registrars release expired domains after a grace period.</p>

<h2 id="step-3">Step 3: Has the SSL Certificate Expired?</h2>
<p>If browsers show a warning such as "Your connection is not private", the SSL certificate may have expired or be misconfigured. Visitors may still be able to click through, but most will not. Most hosts now issue free certificates through Let's Encrypt and renew them automatically; when renewal fails, the host can usually reissue it quickly.</p>

<h2 id="step-4">Step 4: Is the Hosting Account Working?</h2>
<p>Log in to your hosting control panel. Look for a suspension notice, an unpaid invoice, or warnings that the account has hit its limits on disk space, memory or processing. Check the host's status page for outages. Shared hosting accounts are sometimes suspended when a site uses too many resources, for example after a traffic spike or a hack.</p>

<h2 id="step-5">Step 5: Did an Update or Change Break It?</h2>
<p>A blank white page, a "critical error" message or a 500 error right after updating a plugin, theme or WordPress itself usually means a conflict. Your developer can disable the last updated plugin through the hosting file manager, check the error log and restore the previous version. If you changed DNS settings or moved hosting recently, those changes may also be the cause.</p>

<h2 id="who-to-call">Who Should You Call for Each Cause?</h2>
<table>
<tr><th>Symptom</th><th>Likely cause</th><th>Who to call</th></tr>
<tr><td>Works on mobile data, not on office Wi-Fi</td><td>Local network or DNS cache</td><td>Your internet provider or office IT</td></tr>
<tr><td>Parking page or adverts instead of your site</td><td>Domain expired</td><td>Domain registrar, or whoever registered it</td></tr>
<tr><td>"Not secure" or certificate warning</td><td>SSL expired or misconfigured</td><td>Hosting company</td></tr>
<tr><td>Suspension or "account limit" page</td><td>Unpaid hosting or resource limits</td><td>Hosting company</td></tr>
<tr><td>Site does not respond at all</td><td>Server outage or DNS problem</td><td>Hosting company, then registrar</td></tr>
<tr><td>White screen or 500 error after an update</td><td>Plugin, theme or code error</td><td>Your developer</td></tr>
<tr><td>Strange pages or redirects</td><td>Possible hack</td><td>Developer and host; see our hacked guide</td></tr>
</table>
<p>If you see signs of a hack, follow our <a href="/digital/blog/website-hacked-what-to-do">website hacked guide</a> instead.</p>

<h2 id="prevent">How Do You Prevent the Next Outage?</h2>
<ul>
<li>Turn on auto-renewal for the domain and hosting, with a card or reminder you will see.</li>
<li>Keep the domain, hosting and logins in your own name, with your own email as contact.</li>
<li>Use uptime monitoring that alerts you by email or WhatsApp when the site goes down.</li>
<li>Take a backup before every update, and test updates on a staging copy for important sites.</li>
<li>Keep a one-page list of who controls what: registrar, host, developer and their contacts.</li>
</ul>

<h2 id="what-we-offer">How We Diagnose a Website That Is Down</h2>
<p>Our maintenance plan at {P['maint']} a month includes uptime monitoring, renewal reminders, backups before updates and fixes when something breaks. If your site is down now, message us on WhatsApp with the address and what you see. See our <a href="/digital/pricing">pricing page</a>, the <a href="/digital/blog/website-security-checklist-small-business">security checklist</a> and the <a href="/digital/blog/get-business-website-on-google">guide to getting your website on Google</a>.</p>
""",
    faqs=[
        ("Why is my website not opening?",
         "Common reasons are a problem with your own network, an expired domain, an expired or broken SSL certificate, a suspended or overloaded hosting account, or an error after a plugin, theme or software update. Test on mobile data and another device first, then check the domain, certificate and hosting in turn."),
        ("How do I check if my website is down for everyone?",
         "Open it on your phone using mobile data instead of Wi-Fi, try a different browser or private window, and ask someone in another city to open it. If it works for others, the problem is likely your network or browser cache rather than the website itself."),
        ("What happens when a domain expires?",
         "The website and email linked to it stop working, and visitors may see a parking page or advertisements. Registrars usually allow a grace period to renew, after which the domain may be released and registered by someone else. Renew immediately and turn on auto-renewal to avoid it happening again."),
        ("What does a 500 error on my website mean?",
         "A 500 error is a general server error, often caused by a plugin, theme or code problem, especially right after an update. Your developer can check the error log, disable the last changed plugin through the hosting file manager and restore the previous version to bring the site back."),
        ("How can I get alerts when my website goes down?",
         "Use an uptime monitoring service that checks your site every few minutes and alerts you by email or messaging when it stops responding. Many hosts and maintenance plans include monitoring. Combine it with auto-renewal for the domain and hosting, which prevents some of the most common outages."),
        ("Website nahin khul rahi, kya karein?",
         "Pehle mobile data aur doosre phone par check karein ke sab ke liye band hai ya sirf aap ke liye. Phir dekhein ke domain ya SSL ki muddat to khatam nahin hui, hosting ka bill ada hai ya nahin, aur kisi update ke baad error to nahin aaya. Har wajah ke liye alag shakhs se rabta karein."),
    ],
    sources=[
        ("ICANN Lookup — check domain registration details", "https://lookup.icann.org/"),
        ("ICANN — Registrants' benefits and responsibilities", "https://www.icann.org/resources/pages/benefits-2013-09-16-en"),
        ("PKNIC — .pk domain registry", "https://pknic.net.pk/"),
        ("Let's Encrypt — Free, automated certificate authority", "https://letsencrypt.org/"),
        ("WordPress Developer Resources — WordPress backups", "https://developer.wordpress.org/advanced-administration/security/backup/"),
    ],
    method=("Domain lookup and registrant points follow ICANN and PKNIC, SSL points follow Let's Encrypt, and backup advice follows WordPress "
            "documentation, checked 29 October 2026. The step order and symptom table reflect how we diagnose outages for clients. The "
            "maintenance price is our own."),
    related=["get-business-website-on-google", "website-hacked-what-to-do", "website-security-checklist-small-business",
             "domain-and-hosting-price-in-pakistan"],
    service_links=[("/digital/pricing", "Maintenance with uptime monitoring"), ("/digital/contact", "Get help now")],
    cta="Is your website down right now?",
    wa="Hi%2C%20I%20read%20your%20website%20down%20guide%20and%20my%20site%20is%20not%20opening",
)
