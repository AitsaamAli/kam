import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=150,
    slug='eu-gdpr-website-checklist-offshore',
    title='GDPR Website Checklist for EU Clients Building Offshore',
    h1='A GDPR Website Checklist for EU Clients Whose Site Is Built Offshore',
    crumb='GDPR Website Checklist',
    description='A GDPR website checklist for EU businesses using an offshore team: privacy notice, cookie consent, processor agreements, security and hosting.',
    keyword='gdpr website checklist',
    cluster=['gdpr compliant website', 'cookie consent eu', 'website privacy policy eu'],
    category='Working With Overseas Clients',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="A GDPR website checklist for an EU business covers a clear privacy notice, cookie consent before non-essential cookies load, forms that collect only needed data, a written processor contract with your offshore developer and host, security basics and a plan for 4 kinds of request: access, correction, deletion and objection. This is not legal advice.",
    takeaways=["As the business, you are usually the controller; your developer and host are processors acting for you.", "The European Commission says controller and processor need a contract setting out the processor's duties.", "Non-essential cookies, such as analytics and advertising, need consent before they load.", "Forms should collect only what you need, with a link to the privacy notice.", "Offshore developers should have limited, logged access and delete copies of data after work ends."],
    body=f"""
<h2 id="roles">Who Is Responsible Under GDPR When a Site Is Built Offshore?</h2>
<p>EU businesses increasingly have websites built by teams in Pakistan and elsewhere. Building offshore does not change who is responsible for personal data on your website. Under the GDPR, the organisation that decides why and how personal data is processed is the controller, usually your business. An external party processing data on your behalf, such as a developer, hosting company or cloud provider, is a processor. The European Commission's guidance says the processor may only act on the controller's behalf and that their relationship must be set out in a contract.</p>
<p>This GDPR website checklist is practical guidance for working with an offshore team. It is not legal advice; consult your data protection adviser for your situation. UK businesses follow UK GDPR, overseen by the ICO, with very similar principles.</p>

<h2 id="checklist">What Is on the GDPR Website Checklist?</h2>
<table>
<tr><th>#</th><th>Item</th><th>Who acts</th></tr>
<tr><td>1</td><td>List every type of personal data the site collects: forms, orders, analytics, chat</td><td>You, with developer</td></tr>
<tr><td>2</td><td>Write a privacy notice: who you are, what you collect, why, legal basis, who receives it, retention, rights</td><td>You, with adviser</td></tr>
<tr><td>3</td><td>Cookie consent banner that blocks non-essential cookies until consent</td><td>Developer</td></tr>
<tr><td>4</td><td>Equal options to accept or reject, and an easy way to change choices later</td><td>Developer</td></tr>
<tr><td>5</td><td>Forms collect only necessary fields, with a link to the privacy notice</td><td>Developer</td></tr>
<tr><td>6</td><td>Separate, unticked opt-in for marketing emails</td><td>Developer</td></tr>
<tr><td>7</td><td>HTTPS everywhere, updated software, strong admin authentication</td><td>Developer, host</td></tr>
<tr><td>8</td><td>Processor contracts with developer, host and key service providers</td><td>You</td></tr>
<tr><td>9</td><td>Know where data is hosted and how transfers outside the EU are covered</td><td>You, with adviser</td></tr>
<tr><td>10</td><td>Retention periods set, and old form entries deleted on schedule</td><td>You, developer</td></tr>
<tr><td>11</td><td>A process to handle access, correction and deletion requests</td><td>You</td></tr>
<tr><td>12</td><td>A breach plan: who to contact and how fast</td><td>You, developer, host</td></tr>
</table>

<h2 id="cookies">How Should Cookie Consent Work?</h2>
<p>Strictly necessary cookies, such as those keeping a shopping cart working, can run without consent. Analytics, advertising and many embedded third-party tools set cookies that need consent first. The European Data Protection Board's consent guidelines (05/2020, adopted 4 May 2020) address consent quality, including that consent must be freely given and clearly expressed. In practice: show a banner on first visit, do not load non-essential scripts until the visitor agrees, give an equally easy way to reject, and record the choice. Ask your developer to prove it works by loading the site with consent refused and checking which cookies are set.</p>

<h2 id="processor">What Should the Developer Contract Include?</h2>
<ul>
<li>That the developer processes personal data only on your written instructions.</li>
<li>Confidentiality obligations for everyone with access.</li>
<li>Security measures, including limited and logged access.</li>
<li>No subcontracting without your prior written authorisation, as the Commission's guidance notes.</li>
<li>Help with data subject requests and breaches.</li>
<li>Deletion or return of personal data when the work ends.</li>
</ul>
<p>For transfers of personal data to a country outside the EU, such as Pakistan, additional safeguards may be required. Ask your adviser which mechanism applies. Our guide to outsourcing contracts and code ownership covers the commercial side.</p>

<h2 id="minimise">How Can Offshore Access Be Minimised?</h2>
<p>Most build work needs no real customer data at all. Developers can work on a staging site with test data, and production access can be limited to specific tasks. Give each developer their own account, remove access when the project ends, and ask for confirmation that downloaded copies are deleted.</p>

<h2 id="security">Which Security Basics Matter Most?</h2>
<p>HTTPS on every page, updated software, two-step login for admin accounts, regular backups and protection against common attacks. Our security checklist lists the full set.</p>

<h2 id="build">How We Work With EU Clients</h2>
<p>We build with consent-first cookie set-ups, minimal forms and staging data, and sign processor terms on request. Business websites start from {P['business']} in PKR. Our guide to hiring Pakistani developers explains our process. See <a href="/digital/business-websites">business websites</a>.</p>
<p>See also <a href="/digital/blog/website-cost-saudi-arabia">website development cost in Saudi Arabia</a> and <a href="/digital/blog/website-cost-qatar">Website Design Cost in Qatar</a>.</p>
""",
    faqs=[
        ('What is on a GDPR website checklist?',
         "A privacy notice, consent-first cookie banner, forms collecting only needed data, separate marketing opt-ins, HTTPS and security basics, processor contracts with your developer and host, known hosting locations, retention periods, a process for data subject requests and a breach plan. Take advice for your situation."),
        ('Is my offshore web developer a data processor under GDPR?',
         "Usually yes, if they handle personal data on your behalf, for example when accessing form entries or orders. The European Commission explains that a processor acts only on the controller's behalf and that the relationship must be set out in a contract with defined duties."),
        ('Do I need cookie consent for analytics?',
         "Analytics and advertising cookies generally need consent before they load, while strictly necessary cookies do not. Show a banner on first visit, block non-essential scripts until the visitor agrees, offer an equally easy way to reject, and test that refusal actually prevents those cookies being set."),
        ('Can an EU business legally use a developer in Pakistan?',
         "Yes, many do. Where the developer accesses personal data from outside the EU, additional safeguards for international transfers may be required. Limit access, use staging data where possible, sign processor terms, and ask your data protection adviser which transfer mechanism applies."),
        ('What should a privacy notice on my website include?',
         "Who you are and how to contact you, what personal data you collect, why and on what legal basis, who receives it, including processors, how long it is kept, international transfers, and how people can exercise their rights, such as access, correction and deletion."),
        ('How can I reduce GDPR risk when outsourcing website work?',
         "Give developers staging sites with test data instead of live customer data, create individual accounts with limited permissions, log access, remove it when projects end, ask for deletion of any copies, and put processor terms in the contract before work starts."),
    ],
    sources=[('European Commission — What is a data controller or a data processor?', 'https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations_en'), ('European Commission — Rules for business and organisations', 'https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations_en'), ('EDPB — Guidelines 05/2020 on consent', 'https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en'), ('EUR-Lex — General Data Protection Regulation (EU) 2016/679', 'https://eur-lex.europa.eu/eli/reg/2016/679/oj'), ('ICO — UK GDPR guidance and resources', 'https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/')],
    method="Controller and processor definitions and contract points come from the European Commission's page, and the consent guidelines reference from the EDPB's page dated 4 May 2020, both checked 30 October 2026. Only official EU and UK sources are cited, as the plan requires. The checklist is editorial and not legal advice. Our prices come from the published list in PKR.",
    related=['website-data-privacy-when-using-ai', 'website-cost-usa-small-business', 'website-cost-saudi-arabia'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/business-websites', 'Business website service')],
    cta='Building for EU customers?',
    wa='Hi%2C%20I%20read%20your%20GDPR%20website%20checklist',
)
