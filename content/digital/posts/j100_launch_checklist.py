import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=100,
    slug="website-launch-checklist",
    title="Website Launch Checklist: 40 Checks Before Going Live",
    h1="Website Launch Checklist: 40 Checks to Run Before Your Website Goes Live",
    crumb="Website Launch Checklist",
    description="A website launch checklist with 40 checks before going live: content, SEO, speed, security, forms, tracking, legal pages and backups, grouped for your team.",
    keyword="website launch checklist",
    cluster=["go live checklist", "pre launch website checklist", "website testing checklist", "website qa before launch",
             "new website checklist", "website launch se pehle kya check karein"],
    category="Planning & Launch",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("A website launch checklist should cover 40 checks in 8 groups before going live: content, SEO, speed, security, forms and "
            "contact, tracking, legal pages, and backups and ownership. Run it on a phone and a laptop, fix every failure, then repeat the "
            "key checks within 1 week after launch."),
    takeaways=[
        "Most launch problems are small and avoidable: broken forms, wrong numbers, leftover test content and blocked indexing.",
        "Group the checks so different people can own content, technical and business items.",
        "Test on a real phone over mobile data, not only on the developer's computer.",
        "Confirm that domain, hosting, analytics and admin accounts are in the owner's name before launch.",
        "Recheck forms, indexing and speed in the first week after going live.",
    ],
    body=f"""
<h2 id="how-to-use">How Should You Use This Website Launch Checklist?</h2>
<p>Run through these 40 checks on the staging site a few days before launch, then again on the live site straight after. Print it or copy it into a spreadsheet, assign each group to a person, and do not launch until every item is either done or knowingly postponed. Test on a mid-range phone over mobile data as well as on a laptop.</p>

<h2 id="content">Content Checks (1 to 5): Is Everything Real and Correct?</h2>
<table>
<tr><th>#</th><th>Check</th></tr>
<tr><td>1</td><td>No placeholder or demo text, images or pages remain</td></tr>
<tr><td>2</td><td>Prices, phone numbers, addresses and hours are correct everywhere</td></tr>
<tr><td>3</td><td>Spelling and grammar checked on every page</td></tr>
<tr><td>4</td><td>Images are your own or properly licensed</td></tr>
<tr><td>5</td><td>Every link in menus, buttons and footer works</td></tr>
</table>

<h2 id="seo">SEO Checks (6 to 10): Can Google Find the Site?</h2>
<table>
<tr><th>#</th><th>Check</th></tr>
<tr><td>6</td><td>Search engine blocking from development is switched off; no stray noindex</td></tr>
<tr><td>7</td><td>Every page has a unique title and description</td></tr>
<tr><td>8</td><td>One main heading per page, with logical subheadings</td></tr>
<tr><td>9</td><td>XML sitemap exists and is submitted in Search Console</td></tr>
<tr><td>10</td><td>Old URLs redirect to new ones if replacing a site</td></tr>
</table>
<p>Our <a href="/digital/blog/seo-ready-website-checklist">SEO-ready website checklist</a> explains each of these.</p>

<h2 id="speed">Speed Checks (11 to 15)</h2>
<table>
<tr><th>#</th><th>Check</th></tr>
<tr><td>11</td><td>PageSpeed Insights mobile test run on home and key pages</td></tr>
<tr><td>12</td><td>Images resized and compressed</td></tr>
<tr><td>13</td><td>Caching switched on</td></tr>
<tr><td>14</td><td>Unused plugins and scripts removed</td></tr>
<tr><td>15</td><td>Pages tested on a real phone over mobile data</td></tr>
</table>

<h2 id="security">Security Checks (16 to 20)</h2>
<table>
<tr><th>#</th><th>Check</th></tr>
<tr><td>16</td><td>HTTPS works on every page with no certificate warnings</td></tr>
<tr><td>17</td><td>Core software, theme and plugins up to date</td></tr>
<tr><td>18</td><td>Strong passwords and two-step login on admin and hosting</td></tr>
<tr><td>19</td><td>Test and temporary user accounts removed</td></tr>
<tr><td>20</td><td>Dashboard file editing disabled; only trusted plugins installed</td></tr>
</table>

<h2 id="forms">Forms and Contact Checks (21 to 25): Do Enquiries Reach You?</h2>
<table>
<tr><th>#</th><th>Check</th></tr>
<tr><td>21</td><td>Every form submitted and received, including in spam folders</td></tr>
<tr><td>22</td><td>Auto-reply emails read correctly</td></tr>
<tr><td>23</td><td>WhatsApp links open the right chat with the right message</td></tr>
<tr><td>24</td><td>Call buttons dial the right number on a phone</td></tr>
<tr><td>25</td><td>Checkout or booking tested end to end, including payment and confirmation</td></tr>
</table>

<h2 id="tracking">Tracking Checks (26 to 30)</h2>
<table>
<tr><th>#</th><th>Check</th></tr>
<tr><td>26</td><td>Analytics installed and receiving data in real time</td></tr>
<tr><td>27</td><td>Events set for form submissions, WhatsApp and call clicks</td></tr>
<tr><td>28</td><td>Search Console verified in the owner's account</td></tr>
<tr><td>29</td><td>Google Business Profile linked to the new site</td></tr>
<tr><td>30</td><td>Tracking respects cookie consent where required</td></tr>
</table>

<h2 id="legal">Legal and Policy Checks (31 to 35)</h2>
<table>
<tr><th>#</th><th>Check</th></tr>
<tr><td>31</td><td>Privacy policy published and linked in the footer</td></tr>
<tr><td>32</td><td>Terms, delivery and returns pages published for stores</td></tr>
<tr><td>33</td><td>Cookie banner in place if you use non-essential cookies for visitors in regions that require consent</td></tr>
<tr><td>34</td><td>Business name, address and contact details shown clearly</td></tr>
<tr><td>35</td><td>Claims about qualifications, certifications or results are accurate</td></tr>
</table>

<h2 id="ownership-backups">Backup and Ownership Checks (36 to 40)</h2>
<table>
<tr><th>#</th><th>Check</th></tr>
<tr><td>36</td><td>Full backup taken just before launch and stored off the server</td></tr>
<tr><td>37</td><td>Automatic backups scheduled and one restore tested</td></tr>
<tr><td>38</td><td>Domain and hosting registered in the owner's name, with auto-renewal</td></tr>
<tr><td>39</td><td>Owner has admin logins; developer added as a separate user</td></tr>
<tr><td>40</td><td>Handover documents received: logins list, licences and how-to notes</td></tr>
</table>
<p>Our <a href="/digital/blog/website-handover-checklist">website handover checklist</a> covers item 40 in full.</p>

<h2 id="after-launch">What Should You Check in the First Week?</h2>
<p>Within a week of launch, submit every form again, check Search Console for indexing errors, look at analytics for broken pages, retest speed on a phone and ask a few customers to try the site. Small issues found now are cheap to fix.</p>

<h2 id="what-we-offer">How We Handle Launches</h2>
<p>We run all 40 checks before every launch we handle and share the completed list with you, along with logins and a short handover guide. Websites start from {P['starter']}, and stores from {P['store']}; ongoing care is {P['maint']} a month. Use our <a href="/digital/contact">contact page</a> to plan your launch, or read the <a href="/digital/blog/get-business-website-on-google">guide to getting found on Google</a>.</p>
""",
    faqs=[
        ("What should I check before launching a website?",
         "Check content for placeholders and wrong details, SEO basics such as indexing and titles, mobile speed, HTTPS and updates, every form and WhatsApp link, analytics and Search Console, privacy and policy pages, and that backups exist and the domain, hosting and admin accounts are in your name."),
        ("Why do forms often fail after a website launch?",
         "Forms that worked on staging can fail on the live site because email settings change with the domain or hosting, or messages land in spam. Submit every form after launch, check that emails arrive, including in spam folders, and consider sending a copy of each enquiry to a second address."),
        ("How do I make sure Google can index my new website?",
         "Switch off any search engine blocking left on during development, remove stray noindex tags, submit an XML sitemap in Google Search Console and inspect key pages there. A week after launch, check the indexing report for errors and fix any pages Google cannot index."),
        ("Should I take a backup before launching my website?",
         "Yes. Take a full backup of files and database just before launch and store it away from the server. Make sure automatic backups are scheduled for the live site and test one restore, so you can recover quickly if anything goes wrong in the first weeks."),
        ("Who should own the domain and hosting at launch?",
         "The business owner. Before launch, confirm that the domain and hosting are registered in your name with your email, that you have admin logins to the website, analytics and Search Console, and that your developer is added as a separate user you can remove later."),
        ("Website launch se pehle kya check karein?",
         "Launch se pehle dekhein ke koi demo text na ho, qeematein aur phone number sahi hon, har form aur WhatsApp button kaam kare, website mobile par jaldi khule, HTTPS ho, Search Console aur Analytics set hon, privacy policy ho, backup liya gaya ho aur domain aur hosting aap ke naam par hon."),
    ],
    sources=[
        ("Google Search Central — SEO starter guide", "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"),
        ("Google Search Central — Sitemaps overview", "https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview"),
        ("PageSpeed Insights", "https://pagespeed.web.dev/"),
        ("WordPress Developer Resources — Hardening WordPress", "https://developer.wordpress.org/advanced-administration/security/hardening/"),
        ("WordPress Developer Resources — WordPress backups", "https://developer.wordpress.org/advanced-administration/security/backup/"),
        ("ICO — Guide to PECR: cookies and similar technologies", "https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/"),
        ("Google Analytics Help — Recommended events", "https://support.google.com/analytics/answer/9267735"),
    ],
    method=("The 40 checks draw on Google Search Central, PageSpeed Insights, WordPress hardening and backup documentation, the ICO's cookie "
            "guidance and Google Analytics Help, checked 29 October 2026. The grouping and wording are our own launch checklist, used on "
            "client projects. Prices are our own packages."),
    related=["get-business-website-on-google", "seo-ready-website-checklist", "website-handover-checklist",
             "website-accessibility-basics", "how-long-to-build-a-website"],
    service_links=[("/digital/contact", "Plan your launch with us"), ("/digital/business-websites", "Business websites")],
    cta="Getting ready to launch?",
    wa="Hi%2C%20I%20read%20your%20website%20launch%20checklist%20and%20need%20help%20launching",
)
