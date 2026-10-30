import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=58,
    slug="ngo-donation-website-pakistan",
    title="NGO Website in Pakistan: Donations, Reports, Transparency",
    h1="NGO and Trust Website in Pakistan: Online Donations, Annual Reports and Donor Transparency",
    crumb="NGO Donation Website",
    description="NGO website in Pakistan: donation options for local and overseas donors, annual reports and transparency pages, donor privacy, and what a donation website costs.",
    keyword="ngo website pakistan",
    cluster=["donation website", "charity website design", "online donation pakistan", "trust website with donations",
             "zakat donation page", "ngo ki website"],
    category="Websites by Industry",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=(f"An NGO website in Pakistan should make giving easy through bank transfer, Raast, wallets and cards where available, publish "
            f"annual reports and audited accounts, show where money goes, and protect donor details. A 10-page trust website with donation "
            f"pages starts from {P['business']}; a donor portal with receipts and recurring pledges is a web app from {P['app']}."),
    takeaways=[
        "Donors give when they trust you: show who you are, what you do, and where the money went.",
        "Offer the donation methods your donors use: bank transfer and Raast, wallets, cards where available, and international transfers.",
        "Separate donation types, such as Zakat, Sadaqah and general donations, if you accept more than one.",
        "Publish annual reports and audited accounts, and update programme results at least yearly.",
        "Donor names, amounts and contact details are private; publish them only with permission.",
    ],
    body=f"""
<h2 id="trust-first">What Makes an NGO Website in Pakistan Trusted?</h2>
<p>Pakistanis give generously, but many donors have learned to be careful. Before giving to an organisation they do not know personally, they look for proof: a real address, named trustees, programmes with results, and reports showing where money was spent. An NGO website in Pakistan raises more when it answers those questions openly, before asking for a donation.</p>

<h2 id="pages">Which Pages Does an NGO or Trust Website Need?</h2>
<table>
<tr><th>Page</th><th>What it shows donors</th></tr>
<tr><td>About and governance</td><td>Legal name, registration number as issued, trustees or board, registered address</td></tr>
<tr><td>Programmes</td><td>Each programme's aim, location, beneficiaries and latest results</td></tr>
<tr><td>Reports and accounts</td><td>Annual reports and audited financial statements, by year</td></tr>
<tr><td>Donate</td><td>All donation methods, donation types and what each amount can fund</td></tr>
<tr><td>Stories and updates</td><td>Dated updates with photos used with consent</td></tr>
<tr><td>Contact</td><td>Office address, phone, email and visiting hours</td></tr>
</table>

<h2 id="donation-options">Which Donation Options Should You Offer?</h2>
<p>Offer the methods your donors already use, and show each one clearly on the donate page:</p>
<ul>
<li><strong>Bank transfer and Raast.</strong> Show the account title, bank, IBAN and a Raast QR code. The State Bank's merchant payment service supports QR codes, aliases and IBANs, and its December 2023 release says customers cannot be charged a fee for Raast payment options.</li>
<li><strong>Mobile wallets.</strong> Easypaisa and JazzCash accounts are widely used for small donations; show the merchant or account details your provider issues.</li>
<li><strong>Cards online.</strong> Through a Pakistani payment gateway, where your organisation qualifies. Ask the gateway about non-profit onboarding.</li>
<li><strong>Overseas donors.</strong> International bank transfer to your account, with the SWIFT code shown. Stripe does not list Pakistan as a supported country, so card checkouts built on Stripe are not available to a Pakistan-registered organisation.</li>
</ul>
<p>Ask each donor to add a reference, such as "Zakat" or a programme name, and send a receipt once you confirm the payment. Our <a href="/digital/blog/raast-bank-transfer-website-payments">Raast and bank transfer guide</a> explains how to match payments to donors.</p>

<h2 id="donation-types">How Should Donation Types Be Handled?</h2>
<p>Many Pakistani donors want to know how their Zakat, Sadaqah or Fitrana will be used. If you accept more than one type, give each its own option on the form or a separate account, and explain on the website how each is spent. Many donors also want to give to a specific programme, such as a school or a water project; let them choose, and report on it.</p>

<h2 id="transparency">What Should Transparency Pages Include?</h2>
<ol>
<li>Annual reports for at least the last few years, as dated PDFs.</li>
<li>Audited financial statements, with the auditor's name.</li>
<li>A simple breakdown of spending by programme and administration.</li>
<li>Programme results with numbers you can back up, such as students enrolled or patients treated.</li>
<li>Names of trustees or board members and how decisions are made.</li>
</ol>
<p>If you work with international donors or partners, you may also need to publish reports in the format they require. Keep everything dated, so visitors see it is current.</p>

<h2 id="privacy">How Should Donor and Beneficiary Privacy Be Protected?</h2>
<p>Do not publish donor names or amounts without permission; many donors give privately for religious or personal reasons. Keep donor lists and payment details in a protected system with limited access. Beneficiaries need even more care: use photos and stories only with informed consent, avoid images that shame or identify vulnerable people, and take extra care with children.</p>

<h2 id="what-we-build">What We Would Build for You</h2>
<p>An NGO or trust website with programme pages, a donate page covering bank, Raast, wallet and international transfer details, a reports archive and a contact page starts from {P['business']} for up to 10 pages; a smaller trust may need only five pages, from {P['starter']}. Online card donations depend on your gateway. A donor portal with receipts, recurring pledges and programme reporting is built as a web application, priced from {P['app']}. Our <a href="/digital/web-app-development">web app service page</a> explains how we scope these, and our <a href="/digital/blog/clinic-website-design-pakistan">guide to websites by industry</a> lists other sectors. Trusts that run schools should also read our <a href="/digital/blog/school-website-design-pakistan">school website guide</a>.</p>
""",
    faqs=[
        ("How can an NGO in Pakistan accept donations online?",
         "Show bank transfer details with IBAN and a Raast QR code, mobile wallet details, and a card option through a Pakistani payment gateway if your organisation qualifies. For overseas donors, show international transfer details with the SWIFT code. Ask donors to add a reference so you can match payments and send receipts."),
        ("Can a Pakistani NGO use Stripe or PayPal for donations?",
         "Stripe does not list Pakistan as a supported country, so a Pakistan-registered organisation cannot open a Stripe account, and PayPal does not offer Pakistan-based accounts for receiving payments. Use international bank transfers for overseas donors, and Pakistani gateways, wallets and Raast for local donors."),
        ("What should an NGO publish to build donor trust?",
         "Publish your legal name, registration number as issued and address, trustees or board members, programme pages with results, annual reports, audited financial statements and a spending breakdown. Date everything and keep it current. Donors trust organisations that show where money went, not just what they plan to do."),
        ("Should Zakat be collected separately on a donation website?",
         "If you accept Zakat alongside other donations, give it a separate option on the donation form or a separate account, and explain on the website how Zakat funds are used. Many donors want this clarity, and keeping the funds separate makes reporting easier for your organisation as well."),
        ("How much does an NGO website cost?",
         f"A trust or NGO website with programme pages, a donate page, reports archive and contact page starts from {P['business']} for up to 10 pages, or {P['starter']} for five. A donor portal with receipts, recurring pledges and programme reporting is a web application starting from {P['app']}."),
        ("NGO ki website par donation kaise lein?",
         "Donate page par bank account ka IBAN, Raast QR code aur wallet ki tafseel dein, aur agar gateway ijazat de to card option bhi rakhein. Zakat aur Sadaqah ke alag option banayein. Saalana report aur audited accounts website par lagayen taake donors ko pata chale paisa kahan kharch hua."),
    ],
    sources=[
        ("State Bank of Pakistan — Press release on Raast P2M, 6 December 2023", "https://www.sbp.org.pk/press/2023/Pr-06-Dec-2023.pdf"),
        ("easypaisa — Digital bank and wallet (homepage)", "https://easypaisa.com.pk/"),
        ("PayFast — Payment gateway for Pakistani merchants (homepage)", "https://gopayfast.com/"),
        ("Stripe — Global availability (Pakistan not listed)", "https://stripe.com/global"),
        ("PayPal — Pakistan home page", "https://www.paypal.com/pk/home"),
        ("W3C — Introduction to web accessibility", "https://www.w3.org/WAI/fundamentals/accessibility-intro/"),
    ],
    method=("Donation method facts come from the State Bank's Raast release, the easypaisa and PayFast homepages and Stripe's global page, "
            "opened 29 October 2026; the PayPal point repeats our Part 1 finding and should be confirmed. We give no legal advice on "
            "NGO rules. Page lists and transparency items are our own templates. Prices are our own packages."),
    related=["clinic-website-design-pakistan", "school-website-design-pakistan", "raast-bank-transfer-website-payments",
             "web-development-company-islamabad"],
    service_links=[("/digital/web-app-development", "Donation and donor portals"), ("/digital/business-websites", "NGO and trust websites")],
    cta="Want donors to trust and give online?",
    wa="Hi%2C%20I%20read%20your%20NGO%20website%20guide%20and%20need%20a%20quote",
)
