import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=235,
    slug="add-online-payments-to-existing-website",
    title="Add a Payment Gateway to Your Website: A Step Guide",
    h1="Add a Payment Gateway to Your Existing Website: Options by Platform, Onboarding and Testing",
    crumb="Add Payment Gateway",
    description="How to add a payment gateway to a website you already have: options for WordPress, Shopify and custom sites in Pakistan, merchant onboarding steps and testing.",
    keyword="add payment gateway to website",
    cluster=["accept payments on existing website", "jazzcash on wordpress site", "payment integration existing site",
             "merchant account onboarding pakistan", "test payment gateway"],
    category="Planning & Launch",
    published="2026-11-03", published_h="3 November 2026",
    updated="2026-11-03", updated_h="3 November 2026",
    answer=(f"To add a payment gateway to a website you already have, first choose a provider that accepts your business, complete its merchant onboarding, then connect it through a plugin on WordPress, an app or provider on Shopify, or an API on a custom site. "
            f"Test real transactions before going live. Onboarding often takes 1 to 3 weeks."),
    takeaways=[
        "Onboarding with the payment provider, not the technical work, usually takes the longest.",
        "Prepare business documents, a bank account in the business name and clear website policies before applying.",
        "WordPress sites use a plugin, Shopify uses its supported providers, and custom sites use the provider's API.",
        "Test successful, failed and refunded payments in sandbox and then live before announcing.",
        "Keep cash on delivery or bank transfer as options while customers get used to paying online.",
    ],
    body=f"""
<h2 id="when">When Should You Add Online Payments?</h2>
<p>Many Pakistani websites start with "contact us" or WhatsApp orders and add online payments later, when customers ask for it, when cash on delivery causes too many refused orders, or when the business sells services, courses or bookings that need payment upfront. Adding payments to an existing site is usually simpler than building a new one, as long as the site is on a platform that supports the provider you choose.</p>

<h2 id="providers">Which Payment Options Can a Pakistani Website Use?</h2>
<p>Common options include mobile wallet and card payments from providers such as JazzCash and Easypaisa, payment aggregators that accept cards and wallets through one integration, direct bank gateways, and Raast or bank transfer instructions. International providers have their own country rules; Shopify, for example, publishes which countries Shopify Payments supports and lists third-party providers for other countries. Our <a href="/digital/blog/payment-gateways-pakistan-compared">comparison of payment gateways in Pakistan</a> covers fees and features in more detail, and each provider's own site lists current requirements.</p>

<h2 id="onboarding">What Does Merchant Onboarding Involve?</h2>
<p>Providers need to verify your business before you can accept payments. Typical requirements include:</p>
<ul>
<li>Business identity documents, such as CNIC for sole proprietors or registration documents for companies.</li>
<li>A bank account in the business name.</li>
<li>A live website showing products or services, prices, contact details, delivery terms, a refund policy, terms and conditions and a privacy policy.</li>
<li>A description of what you sell and expected transaction volumes.</li>
</ul>
<p>Missing policy pages are one of the most common reasons applications are delayed. Our guide to <a href="/digital/blog/return-refund-policy-online-store-pakistan">return and refund policies for online stores</a> helps you write them.</p>

<h2 id="by-platform">How Do You Add a Payment Gateway to a Website on Each Platform?</h2>
<table>
<tr><th>Platform</th><th>How payments are added</th><th>Watch out for</th></tr>
<tr><td>WordPress with WooCommerce</td><td>Install the provider's plugin, enter merchant credentials, configure the checkout</td><td>Plugin quality and updates; use the provider's official plugin where available</td></tr>
<tr><td>WordPress without a store</td><td>Add WooCommerce or a payment form plugin for services, donations or bookings</td><td>Keeping the site light if you only need a few payment buttons</td></tr>
<tr><td>Shopify</td><td>Choose from providers Shopify supports for your country, configured in the payment settings</td><td>Which providers are available for Pakistani stores and transaction fees</td></tr>
<tr><td>Custom or Laravel/Node site</td><td>Integrate the provider's API with server-side verification of each payment</td><td>Never trust the browser alone; confirm payment status from the provider's server</td></tr>
</table>

<h2 id="testing">Testing Before You Go Live</h2>
<ol>
<li>Use the provider's sandbox or test mode to run successful, declined and cancelled payments.</li>
<li>Check that orders are marked paid only after the provider confirms payment.</li>
<li>Test a refund and see how it appears in your admin panel and the customer's account.</li>
<li>Switch to live mode and make one or two small real payments with different methods.</li>
<li>Check confirmation emails, WhatsApp notifications and receipts.</li>
</ol>

<h2 id="keep-cod">Should You Keep Cash on Delivery?</h2>
<p>For most Pakistani stores, yes, at least at first. Many customers still prefer COD or bank transfer. Offering both lets you see how quickly online payments grow. Some stores offer a small discount or free delivery for online payment to encourage it. If refused COD orders are your main problem, our guide to <a href="/digital/blog/cod-website-fake-orders-pakistan">reducing fake COD orders</a> has other remedies too.</p>

<h2 id="security">Security and Data</h2>
<p>Hosted payment pages, where the customer enters card details on the provider's page, keep card data away from your server and reduce your security burden. Keep the site on HTTPS, keep plugins updated and limit who can access the payment settings in your admin panel.</p>

<h2 id="cost">What Does Adding Payments Cost?</h2>
<p>Providers charge transaction fees, set out in their agreements. The integration work depends on the platform: a plugin set-up on an existing WooCommerce store is a small job, while a custom API integration takes longer. A full store build including payments starts with our store package at {P['store']}. See our <a href="/digital/ecommerce-development">online store service</a> or ask for a quote for your existing site.</p>
""",
    faqs=[
        ("How do I add a payment gateway to my existing website?",
         "Choose a provider that accepts your business type, complete its merchant onboarding with your documents and website policies, then connect it with the official plugin on WordPress, the payment settings on Shopify or the provider's API on a custom site. Test payments thoroughly before going live."),
        ("What documents do payment providers in Pakistan ask for?",
         "Usually identity documents such as CNIC or company registration papers, a bank account in the business name, and a live website with prices, contact details, delivery terms, refund policy, terms and privacy policy. Exact requirements vary by provider, so check their current list."),
        ("Can I add JazzCash or Easypaisa to a WordPress website?",
         "Usually yes, through a plugin for WooCommerce or a payment form plugin, after you complete merchant onboarding with the provider and receive your credentials. Use official or well-maintained plugins, keep them updated, and test successful, failed and refunded payments before accepting real orders."),
        ("How long does it take to start accepting online payments?",
         "The technical set-up can take days, but merchant onboarding with the provider often takes one to three weeks, depending on documents and website checks. Having policy pages and business documents ready before applying is the best way to avoid delays."),
        ("Should I remove cash on delivery after adding online payments?",
         "Usually not at first. Many Pakistani customers still prefer COD or bank transfer. Offer online payment alongside them, consider a small incentive for paying online, and watch how the share of online payments grows before deciding whether to limit COD."),
        ("How much does it cost to add payments to a website?",
         f"Providers charge transaction fees under their agreements. Integration cost depends on the platform: setting up a plugin on an existing WooCommerce store is a small job, while a custom API integration takes longer. A complete store build with payments starts with our store package at {P['store']}."),
        ("Purani website par online payment kaise lagayein?",
         "Pehle aisa payment provider chunein jo aap ke business ko qubool kare, aur merchant onboarding ke liye CNIC, business bank account aur website ki policies tayyar rakhein. Phir WordPress par plugin, Shopify par payment settings ya custom site par API se jorein, aur live karne se pehle test zaroor karein."),
    ],
    sources=[
        ("JazzCash", "https://www.jazzcash.com.pk/"),
        ("Easypaisa", "https://easypaisa.com.pk/"),
        ("Shopify Help Center: Shopify Payments supported countries", "https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries-and-regions"),
        ("Shopify Help Center: Third-party payment providers", "https://help.shopify.com/en/manual/payments/third-party-providers"),
        ("WooCommerce: Products and extensions", "https://woocommerce.com/products/"),
        ("OWASP Top Ten", "https://owasp.org/www-project-top-ten/"),
    ],
    method="We listed the steps for adding payments to existing WordPress, Shopify and custom sites, reviewed providers' and platforms' own pages for requirements, and noted the onboarding issues that most often delay Pakistani businesses. Prices come from our published packages. Sources checked on 3 November 2026.",
    related=["payment-gateways-pakistan-compared", "return-refund-policy-online-store-pakistan", "cod-website-fake-orders-pakistan", "raast-bank-transfer-website-payments"],
    service_links=[("/digital/ecommerce-development", "Online store service"), ("/digital/contact", "Get a written quote")],
    cta="Ready to start taking payments on the website you already have?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20adding%20payments%20to%20a%20website.%20I%20need%20help.",
)
