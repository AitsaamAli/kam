import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=34,
    slug="payment-gateways-pakistan-compared",
    title="Payment Gateways in Pakistan Compared: Wallets, Cards, Raast",
    h1="Payment Gateway Options in Pakistan Compared: JazzCash, Easypaisa, PayFast, Banks and Raast",
    crumb="Payment Gateways Compared",
    description="Payment gateway options in Pakistan compared: JazzCash, Easypaisa, PayFast, bank card gateways and Raast, with typical documents, fee notes and settlement questions.",
    keyword="payment gateway pakistan",
    cluster=["jazzcash payment gateway for website", "easypaisa merchant account", "best payment gateway for ecommerce pakistan",
             "online payment integration pakistan", "card payment for website pakistan", "website par online payment kaise lein"],
    category="E-commerce in Pakistan",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("The main payment gateway options in Pakistan are wallet gateways from JazzCash and Easypaisa, aggregators such as PayFast "
            "that combine cards, wallets and bank accounts, card gateways from banks, and Raast for instant bank payments. Reported "
            "charges are about 1.5% to 3% per payment, but always check each provider's current rates."),
    takeaways=[
        "A payment gateway connects your website checkout to the customer's wallet, card or bank and confirms the payment.",
        "Wallet gateways reach JazzCash and Easypaisa users; aggregators combine several methods in one integration.",
        "Raast lets customers pay instantly from their bank account by QR code, alias or IBAN.",
        "Fees, documents and settlement times change often, so get current terms in writing from each provider.",
        "Most Pakistani stores keep cash on delivery and add one or two online methods, not every gateway at once.",
    ],
    body=f"""
<h2 id="what-is">Which Payment Gateway in Pakistan Should Your Website Use?</h2>
<p>A payment gateway is the service that connects your website's checkout to the customer's wallet, card or bank, takes the payment and tells your store it succeeded. Without one, you can only take cash on delivery or ask customers to transfer money manually.</p>
<p>No single gateway is best for every store. The right choice depends on how your customers prefer to pay, which platform your store uses, and how quickly you need the money in your account. Most stores start with one gateway that covers the methods their customers use most.</p>

<h2 id="comparison">How Do the Main Options Compare?</h2>
<table>
<tr><th>Option</th><th>Customers pay with</th><th>Good for</th><th>Notes</th></tr>
<tr><td>JazzCash merchant gateway</td><td>JazzCash wallet; ask about cards</td><td>Stores whose buyers already use JazzCash</td><td>Check current plugins for your platform</td></tr>
<tr><td>Easypaisa merchant services</td><td>Easypaisa wallet; ask about cards</td><td>Stores whose buyers already use Easypaisa</td><td>Run by easypaisa Bank, which calls itself Pakistan's first digital bank</td></tr>
<tr><td>PayFast and similar aggregators</td><td>Several online methods through one checkout</td><td>Stores wanting one integration for many methods</td><td>PayFast describes itself as State Bank licensed and regulated</td></tr>
<tr><td>Bank card gateway</td><td>Debit and credit cards</td><td>Larger stores with an existing bank relationship</td><td>Usually more paperwork and a longer approval</td></tr>
<tr><td>Raast</td><td>Bank account, by QR, alias or IBAN</td><td>Low-cost instant bank payments</td><td>Through your bank or a provider offering Raast merchant payments</td></tr>
</table>
<p>Provider descriptions come from each provider's own website, viewed 29 October 2026. Features change, so confirm current details directly.</p>

<h2 id="fees">What Do Payment Gateways Charge?</h2>
<p>Gateway charges in Pakistan are commonly reported at about 1.5% to 3% per transaction, depending on the method, the provider and your sales volume. Some providers also charge set-up or yearly fees. Because these terms change and are often negotiated, we do not publish a rate for any single provider. Ask each one for a written rate card covering:</p>
<ul>
<li>the percentage per wallet, card and bank payment</li>
<li>any fixed fee per transaction</li>
<li>set-up, monthly or yearly charges</li>
<li>refund and chargeback fees</li>
</ul>
<p>On Shopify, remember the platform's own fee on top: because Shopify Payments is not available in Pakistan, Shopify adds 2% on Basic, 1% on Grow and 0.6% on Advanced to third-party gateway payments. Our <a href="/digital/blog/shopify-vs-woocommerce-pakistan">Shopify vs WooCommerce guide</a> shows how that adds up.</p>

<h2 id="documents">What Documents Do Gateways Usually Ask For?</h2>
<p>Requirements differ by provider and business type, but the usual list includes:</p>
<ol>
<li>the owner's CNIC</li>
<li>a bank account in the business's or owner's name, as the provider requires</li>
<li>proof that the business exists, in the form the provider asks for</li>
<li>a working website with product pages, prices, and delivery, return and privacy policies</li>
<li>business contact details matching the website</li>
</ol>
<p>Gateways often review the website before approval, so publish your policy pages first. If you are unsure which business documents apply to you, ask your accountant or adviser before applying.</p>

<h2 id="raast">Where Does Raast Fit?</h2>
<p>Raast is the State Bank of Pakistan's instant payment system. According to the State Bank's press release of 6 December 2023, its person-to-merchant service lets merchants accept payments through QR codes, Raast aliases such as mobile numbers, IBANs and request-to-pay. The same release says customers cannot be charged a fee for using Raast payment options. For a store, Raast can be a low-cost alternative to cards. Our <a href="/digital/blog/raast-bank-transfer-website-payments">Raast and bank transfer guide</a> shows how to add it to a checkout.</p>

<h2 id="settlement">How Quickly Do You Get Your Money?</h2>
<p>Settlement is the time between the customer paying and the money reaching your account. It varies by provider and method, and it matters for cash flow. Ask each provider:</p>
<ul>
<li>How many working days until funds reach my bank account?</li>
<li>Is settlement to a bank account or to a wallet?</li>
<li>Is there a minimum amount before payout?</li>
<li>How are refunds deducted?</li>
</ul>

<h2 id="choose">Which Gateway Fits Your Store?</h2>
<table>
<tr><th>Your situation</th><th>Sensible start</th></tr>
<tr><td>New store, mostly COD, young mobile-first buyers</td><td>One wallet gateway plus COD</td></tr>
<tr><td>Growing store with mixed customers</td><td>An aggregator covering wallets and cards</td></tr>
<tr><td>High-value items such as electronics or furniture</td><td>Card gateway or aggregator, plus Raast or bank transfer</td></tr>
<tr><td>Customers abroad</td><td>See our guide to <a href="/digital/blog/stripe-paypal-pakistan-website">Stripe and PayPal alternatives</a></td></tr>
</table>

<h2 id="what-we-build">What We Would Build for You</h2>
<p>Our online store package, from {P['store']}, includes COD checkout and an online payment connection with the gateway of your choice, where it supports your platform. We test real payments, failed payments and refunds before launch, and connect payment confirmations to your order emails and WhatsApp notifications. Custom integrations for gateways without a ready plugin are quoted in the written scope. See our <a href="/digital/ecommerce-development">online store development</a> service.</p>

<h2 id="next-step">Questions to Ask Every Gateway</h2>
<ol>
<li>Which payment methods will my customers see at checkout?</li>
<li>Do you have a current plugin for Shopify or WooCommerce?</li>
<li>What is the full written rate card?</li>
<li>How long is approval, and what documents do you need?</li>
<li>How many days until settlement, and to which account?</li>
</ol>
<p>Setting up a whole store? Start with our <a href="/digital/blog/start-online-store-pakistan">guide to starting an online store in Pakistan</a>, and read <a href="/digital/blog/cod-website-fake-orders-pakistan">how to cut COD fake orders</a> for the cash side.</p>
""",
    faqs=[
        ("Which is the best payment gateway in Pakistan for a website?",
         "There is no single best gateway. Wallet gateways suit stores whose buyers use JazzCash or Easypaisa, aggregators such as PayFast suit stores wanting several methods in one integration, and bank card gateways suit larger stores. Choose by how your customers pay, your platform's plugins, written fees and settlement time."),
        ("How much do payment gateways charge in Pakistan?",
         "Charges are commonly reported at about 1.5% to 3% per transaction, varying by method, provider and sales volume. Some providers add set-up or yearly fees. Terms change and are often negotiated, so ask each provider for a written rate card. Shopify stores also pay Shopify's own fee on gateway payments."),
        ("Can I add JazzCash to my website?",
         "Yes, JazzCash offers merchant payment services for websites. Ask JazzCash for its current merchant requirements, fees and plugins for your platform, such as WooCommerce or Shopify. Your website usually needs clear product prices and delivery, return and privacy policies before a gateway approves your application."),
        ("Do I need a business bank account for a payment gateway?",
         "Most gateways settle payments to a bank account and ask for one in the business's or owner's name, depending on their rules. They also ask for the owner's CNIC and proof that the business exists. Requirements differ by provider, so ask for the current list, and check with your accountant or adviser."),
        ("Is Raast a payment gateway?",
         "Raast is the State Bank of Pakistan's instant payment system, not a gateway company. Merchants can accept Raast payments by QR code, alias, IBAN or request-to-pay through their bank or a provider offering Raast merchant services. A website can show Raast details at checkout or connect through a provider for automatic confirmation."),
        ("Website par online payment kaise lein, konsa gateway behtar hai?",
         "Pehle dekhein ke aap ke customers kaise payment karna pasand karte hain. Agar zyada log JazzCash ya Easypaisa use karte hain to wallet gateway lein. Agar cards aur wallets dono chahiye to PayFast jaisa aggregator behtar hai. Har provider se fees, documents aur paisay milne ka waqt likhwa kar lein."),
        ("How long does payment gateway approval take?",
         "It varies from a few days to several weeks, depending on the provider, your documents and whether your website is ready. Approvals move faster when your site already shows real products, prices, contact details and delivery, return and privacy policies. Apply early so approval does not delay your store launch."),
    ],
    sources=[
        ("PayFast — Payment gateway for Pakistani merchants (homepage)", "https://gopayfast.com/"),
        ("easypaisa — Digital bank and wallet (homepage)", "https://easypaisa.com.pk/"),
        ("State Bank of Pakistan — Press release on Raast P2M, 6 December 2023", "https://www.sbp.org.pk/press/2023/Pr-06-Dec-2023.pdf"),
        ("State Bank of Pakistan — Homepage", "https://www.sbp.org.pk/"),
        ("Shopify — Pricing (third-party transaction fees)", "https://www.shopify.com/pricing"),
        ("Shopify Help Center — Third-party payment providers", "https://help.shopify.com/en/manual/payments/third-party-providers"),
        ("Baymard Institute — Cart abandonment rate statistics", "https://baymard.com/lists/cart-abandonment-rate"),
    ],
    method=("Provider descriptions come from the PayFast and easypaisa homepages and Raast details from the State Bank's press release "
            "of 6 December 2023, all opened 29 October 2026. The JazzCash site could not be loaded for checking, so we state only general "
            "points about it. The 1.5% to 3% fee range is a reported range, not a quote. Store prices are our own."),
    related=["start-online-store-pakistan", "raast-bank-transfer-website-payments", "stripe-paypal-pakistan-website",
             "cod-website-fake-orders-pakistan"],
    service_links=[("/digital/ecommerce-development", "Stores with payment gateways set up"), ("/digital/contact", "Ask about your gateway")],
    cta="Need online payments on your website?",
    wa="Hi%2C%20I%20read%20your%20payment%20gateway%20guide%20and%20need%20help%20adding%20payments",
)
