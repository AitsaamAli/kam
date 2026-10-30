import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=164,
    slug='email-going-to-spam-fix',
    title='Emails Going to Spam? SPF, DKIM and DMARC Explained',
    h1='Why Your Emails Are Going to Spam: SPF, DKIM and DMARC Explained in Plain Words',
    crumb='Emails Going to Spam',
    description='Why emails are going to spam from your website or business address, how SPF, DKIM and DMARC fix it, what Gmail now requires of senders, and how to test the fix.',
    keyword='emails going to spam',
    cluster=['spf dkim dmarc setup', 'contact form emails spam', 'email authentication'],
    category='Fix a Problem',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="Emails going to spam usually means the receiving server cannot confirm they really come from your domain. Add SPF and DKIM records, then DMARC, send website form emails through an authenticated service, and keep complaints low. Gmail's sender guidelines require all senders to use SPF or DKIM, and bulk senders of 5,000+ a day to use both plus DMARC.",
    takeaways=["SPF lists which servers may send for your domain; DKIM signs each message; DMARC tells receivers what to do when checks fail.", "Website contact forms often send from the web server without authentication, which lands mail in spam.", "Gmail's guidelines, effective 1 February 2024, set requirements for all senders and stricter ones for bulk senders.", "Keep complaint rates low: Google asks senders to stay below 0.30% in Postmaster Tools.", "Test with external addresses after every change."],
    body=f"""
<h2 id="why">Why Are Emails Going to Spam?</h2>
<p>A customer says your quote never arrived. Your contact form "works" but enquiries vanish. Invoices land in clients' junk folders. When emails are going to spam, the cause is usually not the wording of the message but missing proof that the email genuinely came from your domain. Mailbox providers such as Gmail and Outlook check for that proof, and without it they treat messages with suspicion.</p>
<p>For the search side of the same problems, read our guide to appearing on Google.</p>

<h2 id="three-records">What Are SPF, DKIM and DMARC?</h2>
<table>
<tr><th>Record</th><th>What it does</th><th>Plain-words analogy</th></tr>
<tr><td>SPF</td><td>Lists the servers allowed to send email for your domain</td><td>A guest list at the gate</td></tr>
<tr><td>DKIM</td><td>Adds a digital signature to each message, checked against a key in your DNS</td><td>A wax seal on a letter</td></tr>
<tr><td>DMARC</td><td>Tells receivers what to do if SPF or DKIM fail, and sends you reports</td><td>Instructions to the guard for anyone not on the list</td></tr>
</table>
<p>All three are text records added to your domain's DNS. Your email provider, such as Google Workspace, Zoho or your host, gives you the exact values.</p>

<h2 id="gmail">What Does Gmail Require?</h2>
<p>Google's email sender guidelines, in effect since 1 February 2024, set out requirements:</p>
<ul>
<li><strong>All senders:</strong> authenticate with SPF or DKIM, have valid forward and reverse DNS, use TLS, keep the spam rate reported in Postmaster Tools below 0.30%, and follow standard message formatting.</li>
<li><strong>Senders of 5,000 or more messages a day to Gmail:</strong> use both SPF and DKIM, set up DMARC (a policy of "none" is acceptable), align the From domain with SPF or DKIM, and support one-click unsubscribe for marketing messages.</li>
</ul>
<p>Most small businesses send far fewer than 5,000 a day, but setting up all three records is still the best protection.</p>

<h2 id="forms">Why Do Website Form Emails Go to Spam?</h2>
<p>Many websites send form notifications using the web server's built-in mail function, from an address like wordpress@yourdomain, without SPF or DKIM covering that server. Receivers see an unauthenticated message and filter it. The fix is to send through an authenticated route: your email provider's SMTP settings, or a transactional email service, with the sending domain authenticated. Our <a href="/digital/blog/contact-forms-that-convert">contact form guide</a> covers related form problems.</p>

<h2 id="steps">How Do You Fix It Step by Step?</h2>
<ol>
<li>List every service that sends email for your domain: mailbox provider, website, invoicing software, newsletter tool.</li>
<li>Create one SPF record that includes all of them; a domain should have only one SPF record.</li>
<li>Enable DKIM in each sending service and add the keys it gives you to DNS.</li>
<li>Add a DMARC record, starting with a monitoring policy, and read the reports for a few weeks.</li>
<li>Switch website forms to authenticated sending.</li>
<li>Test by sending to Gmail and Outlook addresses and checking the message headers show SPF, DKIM and DMARC passing.</li>
</ol>

<h2 id="other-causes">What Else Can Cause Spam Filtering?</h2>
<ul>
<li>Sending from a shared hosting server with a poor reputation.</li>
<li>Bulk emails to people who never agreed to receive them, leading to complaints.</li>
<li>Misleading subject lines or link shorteners.</li>
<li>A newly registered domain sending large volumes suddenly.</li>
</ul>

<h2 id="newsletters">What About Newsletters and Bulk Messages?</h2>
<p>Send newsletters through a dedicated email marketing service rather than your normal mailbox, so bulk sending does not damage the reputation of the address you use for quotes and invoices. Authenticate the service with your domain, warm up a new list slowly, and remove addresses that bounce. Sending a sudden large batch from a new domain is a common way to land everything in spam.</p>

<h2 id="privacy">Do Marketing Emails Need Consent?</h2>
<p>Yes, in most places. Send newsletters only to people who opted in, include a clear unsubscribe link, and remove people who ask. Complaints are one of the strongest signals spam filters use.</p>

<h2 id="help">Getting It Fixed</h2>
<p>Setting up SPF, DKIM, DMARC and authenticated form email is part of every website we build from {P['starter']}, and of our care plans from {P['maint']} a month. See our guide to <a href="/digital/blog/business-email-on-own-domain-pakistan">business email on your own domain</a> or our <a href="/digital/pricing">pricing page</a>.</p>
""",
    faqs=[
        ('Why are my emails going to spam?',
         "Usually because receiving servers cannot confirm the email really came from your domain. Missing or incorrect SPF, DKIM and DMARC records are the most common cause, followed by unauthenticated website form emails, poor shared server reputation, and complaints from people who did not want the messages."),
        ('What are SPF, DKIM and DMARC in simple words?',
         "SPF is a list of servers allowed to send email for your domain. DKIM adds a digital signature to each message that receivers check against your DNS. DMARC tells receivers what to do if those checks fail and sends you reports about your email."),
        ('What does Gmail require from email senders?',
         "Google's sender guidelines, effective 1 February 2024, require all senders to use SPF or DKIM, valid DNS, TLS and a spam rate below 0.30%. Senders of 5,000 or more messages a day to Gmail must use SPF, DKIM and DMARC and support one-click unsubscribe."),
        ('Why do my website contact form emails go to spam?',
         "Many sites send form notifications through the web server's mail function without authentication. Receivers see an unverified message and filter it. Send form emails through your email provider's SMTP or a transactional email service with your domain authenticated, then test with external addresses."),
        ('Can I have more than one SPF record?',
         "No. A domain should have a single SPF record that lists every service allowed to send for it, such as your mailbox provider, website and invoicing tool. Multiple SPF records cause checks to fail, which can send even genuine messages to spam."),
        ('How do I check whether SPF, DKIM and DMARC are working?',
         "Send a test email to a Gmail or Outlook address, open the message headers or the show original option, and look for SPF, DKIM and DMARC results showing pass. Read DMARC reports for a few weeks to spot any services you forgot to include."),
        ('Meri emails spam mein kyun ja rahi hain?',
         "Aksar wajah yeh hai ke domain ke DNS mein SPF, DKIM aur DMARC records nahin lage, ya website ka form bina authentication email bhejta hai. Email provider se records lekar DNS mein lagayen, form ko SMTP se jodein, aur Gmail par test email bhej kar check karein."),
    ],
    sources=[('Google — Email sender guidelines', 'https://support.google.com/mail/answer/81126'), ('Google Workspace Admin Help — Set up SPF, DKIM and DMARC', 'https://support.google.com/a/answer/10583557'), ('Cloudflare Learning — What are DMARC, DKIM and SPF?', 'https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/')],
    method="Gmail requirements, the 1 February 2024 date, the 0.30% spam rate and the 5,000-message threshold come from Google's email sender guidelines, checked 30 October 2026. The plain-words analogies and fix steps are editorial. Our prices come from the published list.",
    related=['business-email-on-own-domain-pakistan', 'contact-forms-that-convert', 'transfer-domain-to-new-registrar'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='Quotes landing in spam?',
    wa='Hi%2C%20I%20read%20your%20emails%20going%20to%20spam%20guide',
)
