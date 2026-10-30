import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=161,
    slug='transfer-domain-to-new-registrar',
    title='How to Transfer a Domain Name to a New Registrar Safely',
    h1='How to Transfer Your Domain Name to a New Registrar Without Breaking Email or Website',
    crumb='Transfer a Domain Name',
    description="How to transfer a domain name to a new registrar safely: the auth code, ICANN's 60-day locks, .pk domains through PKNIC, protecting email and timing.",
    keyword='transfer domain name',
    cluster=['domain transfer pakistan', 'move .pk domain', 'epp code'],
    category='Fix a Problem',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="To transfer a domain name, unlock it at your current registrar, get the auth (EPP) code, start the transfer at the new registrar and approve it by email. Under ICANN rules, the old registrar must provide the code within 5 calendar days. Copy your DNS records first, so your website and email keep working. .pk domains follow PKNIC's own process.",
    takeaways=["Copy every DNS record before you start; missing email records are the most common cause of trouble.", "Make sure the domain is registered in your name and that you control the registrant email.", "ICANN rules allow a 60-day lock after certain changes, so plan transfers around them.", ".pk domains follow PKNIC's own procedures, which differ from generic domains.", "Avoid transferring close to the expiry date or during a busy sales period."],
    body=f"""
<h2 id="why">Why Transfer a Domain Name?</h2>
<p>Business owners transfer domains for good reasons: the previous developer registered it under their own account, the renewal price has climbed, support is poor, or you want all your domains in one place. Whatever the reason, the domain is the address for both your website and your email, so a careless transfer can take both offline. This guide explains how to transfer a domain name step by step, and what is different for .pk domains.</p>
<p>Domains are the first of the ownership topics that follow on from our guide to getting found on Google. Our guide to who owns your website explains why the domain should be in your name in the first place.</p>

<h2 id="before">What Should You Check Before Starting?</h2>
<ol>
<li><strong>Ownership:</strong> confirm the registrant name is you or your business, and that you can receive email at the registrant address.</li>
<li><strong>DNS records:</strong> export or screenshot every record, especially MX, SPF, DKIM and any verification records.</li>
<li><strong>Expiry date:</strong> avoid transfers in the last days before expiry.</li>
<li><strong>Recent changes:</strong> check whether the registrant details were changed in the last 60 days.</li>
<li><strong>Nameservers:</strong> know where DNS is hosted; it may be at the registrar, the host or a service such as Cloudflare.</li>
</ol>

<h2 id="steps">How Does a Generic Domain Transfer Work?</h2>
<table>
<tr><th>Step</th><th>Where</th><th>What happens</th></tr>
<tr><td>1. Unlock the domain</td><td>Current registrar</td><td>Remove the transfer lock</td></tr>
<tr><td>2. Get the auth code</td><td>Current registrar</td><td>Also called EPP or AuthInfo code</td></tr>
<tr><td>3. Start the transfer</td><td>New registrar</td><td>Enter the domain and code, pay any fee</td></tr>
<tr><td>4. Approve</td><td>Your email</td><td>Confirm the request if asked</td></tr>
<tr><td>5. Wait</td><td>Both</td><td>Usually several days</td></tr>
<tr><td>6. Check DNS</td><td>New registrar or DNS host</td><td>Confirm records match your copy</td></tr>
</table>
<p>ICANN's guidance for domain name holders says the auth code verifies you are the holder, and if you cannot generate it yourself the registrar must provide it within five calendar days of your request. Registrars may charge a transfer fee, but ICANN states a transfer cannot be denied for non-payment of that fee.</p>

<h2 id="locks">What Are the 60-Day Locks?</h2>
<p>ICANN's rules mean that after you change the registrant name, organisation or email, the domain cannot move to another registrar for 60 days, unless the registrar offers and you accept an opt-out. A registrar may also deny a transfer within 60 days of the domain's first registration or its previous transfer. If you need to change ownership details and move registrar, plan the order carefully.</p>

<h2 id="pk">What Is Different for .pk Domains?</h2>
<p>.pk domains are managed by PKNIC, Pakistan's registry, not under the same ICANN transfer system. PKNIC's site lists "Change Registrar" and "Change Details" procedures; contact PKNIC or your reseller for the current process before you start. PKNIC states a fee of Rs 2,100 a year for Pakistan-based registrants from 1 August 2026, and $15.99 a year for registrants outside Pakistan, with the fee charged for a two-year period. Our domain and hosting price guide has more detail.</p>

<h2 id="email">How Do You Protect Email During a Transfer?</h2>
<p>Email breaks during transfers when DNS moves to a new provider without the MX and authentication records. If DNS stays with a separate host such as Cloudflare, the registrar transfer alone does not change records. If DNS is hosted at the old registrar, recreate every record at the new provider before changing nameservers, then test sending and receiving. Our guide to <a href="/digital/blog/email-going-to-spam-fix">emails going to spam</a> explains the authentication records.</p>

<h2 id="timing">When Is the Best Time?</h2>
<p>Choose a quiet weekday, well before expiry and away from sales or launches. Tell staff that email may need checking for a day.</p>

<h2 id="privacy">What About Registrant Privacy?</h2>
<p>Registration details include names, phones and emails. Use the new registrar's privacy service where available, and keep a business email, not a personal one, as the registrant address.</p>

<h2 id="help">Getting Help</h2>
<p>We handle domain transfers as part of website care plans from {P['maint']} a month, or as a one-off task. See our <a href="/digital/pricing">pricing page</a>.</p>
<p>See also our <a href="/digital/blog/move-website-to-new-hosting">guide to moving your website to a new host</a>.</p>
""",
    faqs=[
        ('How do I transfer a domain name to a new registrar?',
         "Unlock the domain at your current registrar, request the auth or EPP code, start the transfer at the new registrar with that code, approve any confirmation email and wait for completion. Copy all DNS records first so your website and email keep working throughout."),
        ('How long does the old registrar have to give me the auth code?',
         "ICANN's guidance for domain name holders says that if you cannot generate the auth code yourself through an online tool, your registrar must provide it within five calendar days of your request. Registrars may charge a transfer fee, but cannot deny the transfer for non-payment."),
        ("Why can't I transfer my domain right now?",
         "Common reasons are a transfer lock still on, a change to the registrant name, organisation or email within the last 60 days, the domain being registered or transferred within the last 60 days, or unpaid fees for a previous period. Check with your current registrar."),
        ('How do I transfer a .pk domain?',
         ".pk domains are managed by PKNIC, Pakistan's registry, which has its own change registrar and change details procedures. Contact PKNIC or your reseller for the current process before starting, and make sure the domain is registered in your own name."),
        ('Will my email stop working during a domain transfer?',
         "It should not, if DNS records are preserved. Problems happen when DNS moves to a new provider without the MX and authentication records. Copy every record first, recreate them at the new provider before changing nameservers, and test sending and receiving from outside addresses afterwards."),
        ('What does a .pk domain cost?',
         "PKNIC lists Rs 2,100 a year for Pakistan-based registrants from 1 August 2026, and $15.99 a year for registrants outside Pakistan, with the fee charged for a two-year period. Resellers may charge more for their services, so compare total costs."),
        ('Domain doosri company mein kaise transfer karein?',
         "Pehle tamam DNS records ki copy bana lein, khas taur par email wale. Purani company se domain unlock karwayen aur auth code lein, phir nayi company mein transfer shuru karein. .pk domain ke liye PKNIC ka apna tareeqa hai. Expiry ke qareeb ya sale ke dinon mein transfer na karein."),
    ],
    sources=[('ICANN — FAQs for domain name holders (transfers)', 'https://www.icann.org/resources/pages/name-holder-faqs-2017-10-10-en'), ('PKNIC — .pk domain registration', 'https://pknic.net.pk/'), ('Cloudflare — Plans', 'https://www.cloudflare.com/plans/')],
    method="Transfer rules (auth code within five calendar days, 60-day locks, transfer fees) come from ICANN's FAQ for domain name holders, and .pk fees from PKNIC's site, both checked 30 October 2026. PKNIC's transfer procedure text could not be read, so readers are directed to PKNIC. Our prices come from the published list.",
    related=['email-going-to-spam-fix', 'move-website-to-new-hosting', 'business-email-on-own-domain-pakistan'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/contact', 'Get a written quote')],
    cta='Domain stuck with an old developer?',
    wa='Hi%2C%20I%20read%20your%20domain%20transfer%20guide',
)
