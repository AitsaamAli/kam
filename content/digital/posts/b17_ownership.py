import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=17,
    slug="who-owns-your-website",
    title="Who Owns Your Website? Domain, Hosting and Code",
    h1="Who Owns Your Website? Domain, Hosting and Code Ownership Explained",
    crumb="Who Owns Your Website",
    description="Who owns your website: how to check who controls your domain, hosting, code and Google accounts, the warning signs of lock-in, and how to take back control.",
    keyword="who owns my website",
    cluster=["website ownership", "domain ownership check", "developer holding my domain",
             "get website back from developer", "website lock-in"],
    category="Hiring a Developer",
    published="2026-10-28", published_h="28 October 2026",
    updated="2026-10-28", updated_h="28 October 2026",
    answer=("Who owns your website depends on whose name is on six things: the domain, the hosting account, the code and design, the admin "
            "login, the business email and your Google accounts. If any of them sits in your developer's name, they control that part. "
            "Check each one today and move it into your own name."),
    takeaways=[
        "Website ownership is six separate things, not one.",
        "The domain matters most: whoever controls it controls your website and email.",
        "Paying for a website does not automatically transfer ownership; the agreement and account names decide it.",
        "Add your developer as a user on your accounts instead of letting them own the accounts.",
        "If a developer refuses to hand over access, start with the domain registrar and your written agreement.",
    ],
    body="""
<h2 id="six-parts">Who Owns My Website? The Six Parts</h2>
<table>
<tr><th>Part</th><th>What it is</th><th>Should be registered to</th></tr>
<tr><td>Domain</td><td>Your address, such as yourbusiness.pk</td><td>You, with your email as the contact</td></tr>
<tr><td>Hosting</td><td>The server account where files live</td><td>You, paid from your card or account</td></tr>
<tr><td>Code and design</td><td>Files, theme and custom work</td><td>You, after final payment, by agreement</td></tr>
<tr><td>Admin login</td><td>WordPress, Shopify or app administrator</td><td>You as owner; developer as a separate user</td></tr>
<tr><td>Business email</td><td>info@yourbusiness.pk mailboxes</td><td>You, on an account you control</td></tr>
<tr><td>Google accounts</td><td>Analytics, Search Console, Business Profile</td><td>You as owner; developer added as a user</td></tr>
</table>

<h2 id="check">How Do You Check Who Owns Each Part?</h2>
<ol>
<li><strong>Domain:</strong> look up your domain on ICANN's lookup tool for generic domains, or ask your registrar. For .pk domains, check the contact details with your registrar or PKNIC. The registrant name and email should be yours.</li>
<li><strong>Hosting:</strong> can you log in to the hosting control panel yourself? Who receives the renewal invoice?</li>
<li><strong>Admin login:</strong> do you have an administrator or store-owner account, not only an editor account?</li>
<li><strong>Google accounts:</strong> in Analytics, Search Console and your Business Profile, check that you are listed as owner.</li>
<li><strong>Code:</strong> do you have a recent full backup or access to the code repository?</li>
</ol>

<h2 id="warning-signs">What Are the Warning Signs of Website Lock-in?</h2>
<ul>
<li>You receive hosting or domain renewal requests from the developer, not from the provider.</li>
<li>You have never logged in to your own site's admin panel.</li>
<li>The developer says the theme or system is "theirs" and cannot be moved.</li>
<li>Monthly fees continue, but you cannot get a list of what they cover.</li>
<li>Your business email stops working whenever an invoice is late.</li>
</ul>

<h2 id="paid-not-owned">Paying for a Website Is Not the Same as Owning It</h2>
<p>Many owners assume that paying for a site means owning it. In practice, ownership depends on whose name is on the accounts and on what your agreement says about the code and design. Copyright in creative and software work generally starts with whoever creates it, unless an agreement transfers it. That is why our <a href="/digital/blog/website-development-contract-checklist">contract checklist</a> includes a clear ownership clause that applies once the final payment is made.</p>

<h2 id="right-setup">The Right Set-up From Day One</h2>
<p>The safest pattern is simple: you create the accounts in your name and add your developer as a user. Google Analytics, Search Console and Business Profile all let owners add other users with limited permissions and remove them later. WordPress has user roles for this, and Shopify lets store owners add staff accounts. When the project ends, you remove the developer's access; nothing needs to be "transferred".</p>

<h2 id="take-back">How Do You Take Back Control of Your Website?</h2>
<ol>
<li><strong>Ask politely in writing</strong> for each login and the domain transfer code, referring to your agreement.</li>
<li><strong>Start with the domain.</strong> If it is registered to you, the registrar can help you regain access to it.</li>
<li><strong>Request a full backup</strong> of files and database, or the code repository transfer.</li>
<li><strong>Claim your Google accounts</strong> through each service's ownership verification process.</li>
<li><strong>Set up new hosting</strong> in your name and restore the backup there.</li>
</ol>
<p>If the domain itself is registered to the developer, recovery is harder; this is why it must be in your name from the start. Our <a href="/digital/blog/website-handover-checklist">handover checklist</a> lists everything you should receive at launch.</p>
<p>Every site in our <a href="/digital/business-websites">business website packages</a> is handed over with all six parts in your name.</p>
""",
    faqs=[
        ("How do I know if I own my website?",
         "Check six things: the domain registrant, the hosting account, your admin login, your business email, ownership of Google Analytics, Search Console and Business Profile, and a copy of the code. If every one of them is in your name and you can log in yourself, you control your website."),
        ("Can a web developer keep my domain name?",
         "If the domain was registered in the developer's name, they control it, which is why it should always be registered to you. If it is registered to you but they hold the login, contact the registrar to recover access. Your written agreement and payment records help if there is a dispute."),
        ("Who owns the copyright of my website design?",
         "Copyright in creative and software work generally starts with whoever creates it, unless an agreement transfers it. A good website contract states that the client owns the design, code and content after final payment. Without that clause, ownership can be unclear, so add it before the project starts."),
        ("Should my developer have access to my Google accounts?",
         "Yes, but as an added user, not as the owner. Create Analytics, Search Console and Business Profile in your own account, then add the developer with the permissions they need. When the project or contract ends, you simply remove their access, and you keep all the data and history."),
        ("Meri website ka maalik kaun hai, kaise check karoon?",
         "Dekhein ke domain kis ke naam par register hai, hosting ka bill kis ko aata hai, aur kya aap khud admin panel mein login kar sakte hain. Google Analytics aur Search Console mein bhi owner aap hon. Agar koi cheez developer ke naam par hai, to usay abhi apne naam par muntaqil karwayen."),
        ("What should I do if my developer refuses to hand over my website?",
         "Ask in writing for each login and the domain transfer code, referring to your agreement and payments. Contact the domain registrar if the domain is in your name. Request a backup, set up hosting in your name and claim your Google accounts through their verification process. Get legal advice for serious disputes."),
    ],
    sources=[
        ("ICANN — Registrants' benefits and responsibilities", "https://www.icann.org/resources/pages/benefits-2013-09-16-en"),
        ("ICANN Lookup — check domain registration details", "https://lookup.icann.org/"),
        ("Google Analytics Help — Add, edit and delete users", "https://support.google.com/analytics/answer/9305788"),
        ("Google Search Console Help — Manage owners, users and permissions", "https://support.google.com/webmasters/answer/7687615"),
        ("Google Business Profile Help — Add or remove owners and managers", "https://support.google.com/business/answer/3403100"),
        ("WordPress.org — Roles and capabilities", "https://wordpress.org/documentation/article/roles-and-capabilities/"),
        ("WIPO — Copyright", "https://www.wipo.int/copyright/en/"),
    ],
    method=("The six-part checklist reflects the ownership problems we see when clients move to us from other developers. Account steps follow "
            "the official help pages for ICANN, Google Analytics, Search Console, Business Profile and WordPress. The copyright point "
            "follows WIPO's general overview and is not legal advice for any specific dispute."),
    related=["website-handover-checklist", "website-development-contract-checklist", "domain-and-hosting-price-in-pakistan",
             "how-to-choose-web-development-company"],
    service_links=[("/digital/business-websites", "Business websites you fully own"), ("/digital/contact", "Get help recovering access")],
    cta="Not sure who controls your website?",
    wa="Hi%2C%20I%20read%20your%20website%20ownership%20guide%20and%20need%20help%20checking%20mine",
)
