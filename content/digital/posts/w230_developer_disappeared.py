import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=230,
    slug="developer-disappeared-mid-project",
    title="Developer Disappeared Mid-Project? What to Do Now",
    h1="Your Developer Disappeared Mid-Project: How to Recover Accounts and Restart",
    crumb="Developer Disappeared",
    description="Your developer disappeared mid-project? How to recover the domain and hosting, find out how much work was done, protect what you paid for and restart safely.",
    keyword="developer disappeared",
    cluster=["web developer not responding", "freelancer ran away with money", "unfinished website",
             "recover website from developer", "restart website project"],
    category="Planning & Launch",
    published="2026-11-03", published_h="3 November 2026",
    updated="2026-11-03", updated_h="3 November 2026",
    answer=(f"If your developer disappeared mid-project, act in this order: secure the domain and hosting, collect every file and login you can, record what was paid and delivered, then have a new developer assess the work before deciding to finish or rebuild. "
            f"Most recoveries take 1 to 3 weeks."),
    takeaways=[
        "Secure the domain first; whoever controls it controls your website and email.",
        "Gather every login, file, message and payment record before contacting the developer again.",
        "Send one clear written message asking for access and a handover by a specific date.",
        "Get an independent assessment of the unfinished work before paying anyone to continue it.",
        "Restart with milestone payments, accounts in your name and a written agreement.",
    ],
    body=f"""
<h2 id="dont-panic">The First 48 Hours After Your Developer Disappeared</h2>
<p>It happens more often than people admit. A developer who answered every message suddenly stops replying, the staging link stops working, and the launch date passes. Sometimes the person is ill or overwhelmed; sometimes they have taken on too much work; occasionally they have simply moved on with the advance. Whatever the reason, the first steps are the same, and doing them calmly protects what you have paid for.</p>
<p>Do not start by posting angry messages publicly. Start by finding out what you control.</p>

<h2 id="secure">What Should You Secure First?</h2>
<table>
<tr><th>Asset</th><th>How to check</th><th>What to do</th></tr>
<tr><td>Domain</td><td>Look it up on ICANN Lookup or ask the .pk registrar who the registrant is</td><td>If it is in your name, reset the login with the registrar; if not, gather proof you paid for it</td></tr>
<tr><td>Hosting</td><td>Who receives the hosting invoices? Can you log in?</td><td>Contact the host with your payment proof if the account is yours</td></tr>
<tr><td>Website files</td><td>Do you have any backup, code repository or staging link?</td><td>Download whatever is still accessible today</td></tr>
<tr><td>Admin logins</td><td>WordPress, Shopify or other admin accounts</td><td>Change passwords where you have owner access</td></tr>
<tr><td>Google accounts</td><td>Analytics, Search Console, Business Profile</td><td>Check you are the owner, remove the developer if needed</td></tr>
</table>
<p>Our guide to <a href="/digital/blog/who-owns-your-website">who owns your website</a> explains each of these in detail.</p>

<h2 id="evidence">Gather the Evidence</h2>
<p>Collect the quotation or agreement, all payment receipts or bank transfers, the WhatsApp and email history, the list of deliverables promised and anything already delivered, such as designs, staging links or files. Note the dates. This record matters whether you are negotiating a handover, asking a new developer to continue, or seeking advice about getting money back.</p>

<h2 id="message">How Should You Contact the Developer?</h2>
<p>Send one clear, polite written message by WhatsApp and email. State what was agreed, what has been paid, what has been delivered, and what you are asking for: the domain transfer code if the domain is held by them, hosting and admin access, the latest files and database, and a response by a specific date, such as seven days. Keep it factual. Many developers respond to a calm message that gives them a way to hand over without conflict. If there is no response by the date, you have a clear record that you tried.</p>

<h2 id="assess">How Do You Know How Much Work Was Done?</h2>
<p>Ask a new developer to assess what exists before deciding anything. A useful assessment checks whether the files and database are complete, whether the theme and plugins are licensed, whether the code is understandable and safe, and how much of the agreed scope is actually finished. Sometimes most of the work is usable and only finishing is needed. Sometimes the work is so incomplete or poorly built that rebuilding on a clean base is cheaper. Our guide to <a href="/digital/blog/taking-over-website-from-old-developer">taking over a website from an old developer</a> describes the checks we run.</p>

<h2 id="restart">Restarting Without Repeating the Problem</h2>
<ol>
<li>Create the domain, hosting and Google accounts in your own name and add the new developer as a user.</li>
<li>Agree a written scope, timeline and price, using our <a href="/digital/blog/website-development-contract-checklist">website contract checklist</a>.</li>
<li>Pay in milestones tied to visible progress, not a large advance.</li>
<li>Ask for weekly updates and access to the staging site throughout.</li>
<li>Require a full handover at the end: files, database, logins and documentation.</li>
</ol>

<h2 id="money">Can You Get Your Money Back?</h2>
<p>It depends on the agreement, what was delivered and how payment was made. Start with a written request. If the developer was hired through a freelancing platform, use the platform's dispute process. For larger amounts, a lawyer can advise on your options. In many cases, the practical priority is recovering your domain and files and getting the project finished, rather than spending months chasing a small refund.</p>

<h2 id="how-we-help">How We Take Over Abandoned Projects</h2>
<p>We assess abandoned projects, recover what can be recovered, and give a written plan to finish or rebuild, with a fixed price. Small business sites usually restart on our starter package at {P['starter']} or business package at {P['business']}, depending on the scope. Contact us through our <a href="/digital/contact">contact page</a> with whatever files and links you have.</p>
""",
    faqs=[
        ("What should I do first if my web developer stops responding?",
         "Secure what you control before anything else. Check who the domain is registered to, whether you can log in to the hosting and the website admin, and download any files or staging content still accessible. Then gather your agreement, payments and messages as a record."),
        ("How do I get my domain back from a developer?",
         "If the domain is registered in your name, contact the registrar, verify your identity and reset access. If it is in the developer's name, ask in writing for a transfer, citing your payment, and contact the registrar with your proof. This is why domains must always be registered to the owner."),
        ("Should a new developer finish the old developer's work?",
         "Only after an assessment. A new developer should check whether files and database are complete, whether themes and plugins are licensed, whether the code is safe and understandable and how much scope is finished. Sometimes finishing is cheaper, sometimes rebuilding on a clean base is."),
        ("Can I get my money back from a freelancer who disappeared?",
         "It depends on the agreement, what was delivered and how you paid. Start with a written request. Use the platform's dispute process if you hired through a freelancing site, and ask a lawyer about larger amounts. Recovering your domain and files is usually the more urgent priority."),
        ("How do I avoid a developer disappearing again?",
         "Keep the domain, hosting and Google accounts in your name, sign a written scope and timeline, pay in milestones tied to visible progress, ask for weekly updates and staging access, and require a full handover at the end. These steps limit the damage if anything goes wrong."),
        ("How much does it cost to restart an unfinished website?",
         f"It depends on what can be reused. After an assessment, small business sites usually restart on our starter package at {P['starter']} or business package at {P['business']}. We give a written plan and fixed price once we have seen the existing files and agreed the remaining scope."),
        ("Developer bhaag gaya, ab website ka kya karoon?",
         "Sab se pehle domain aur hosting apne control mein karein aur jo files aur logins mil sakein le lein. Payment, agreement aur messages ka record rakhein. Developer ko ek saaf likhit message bhejein aur tareekh dein. Phir naye developer se kaam ka jaiza lein ke mukammal karna sasta hai ya dobara banana."),
    ],
    sources=[
        ("ICANN Lookup: check domain registration details", "https://lookup.icann.org/"),
        ("ICANN: Registrants' benefits and responsibilities", "https://www.icann.org/resources/pages/benefits-2013-09-16-en"),
        ("PKNIC: .pk domain registry", "https://pknic.net.pk/"),
        ("Google Search Console Help: Manage owners, users and permissions", "https://support.google.com/webmasters/answer/7687615"),
        ("WIPO: Copyright", "https://www.wipo.int/copyright/en/"),
    ],
    method="We based these steps on how abandoned website projects are recovered in practice, the domain registrant rules from ICANN and PKNIC, and account ownership guidance from Google. Prices come from our published packages. Sources checked on 3 November 2026.",
    related=["who-owns-your-website", "taking-over-website-from-old-developer", "website-development-contract-checklist", "website-milestone-payments"],
    service_links=[("/digital/contact", "Get a written quote"), ("/digital/business-websites", "Business website packages")],
    cta="Stuck with an unfinished website and a silent developer?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20developers%20who%20disappear.%20I%20need%20help%20with%20my%20project.",
)
