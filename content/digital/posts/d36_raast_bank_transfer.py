import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=36,
    slug="raast-bank-transfer-website-payments",
    title="Raast Payment Integration on Your Website: How to Set It Up",
    h1="Raast Payment Integration and Bank Transfers: Checkout, Confirmation and Reconciliation",
    crumb="Raast and Bank Transfers",
    description="Raast payment integration for your website: what Raast is, manual and automated checkout flows, order confirmation and daily reconciliation steps.",
    keyword="raast payment integration",
    cluster=["raast for business", "bank transfer checkout", "manual payment confirmation website",
             "raast qr code for shop", "raast id for online store", "raast se payment kaise lein"],
    category="E-commerce in Pakistan",
    published="2026-10-29", published_h="29 October 2026",
    updated="2026-10-29", updated_h="29 October 2026",
    answer=("Raast payment integration lets customers pay your website from their bank app by QR code, Raast ID or IBAN. You can set it up "
            "manually in 1 day by showing your details at checkout and confirming each payment, or automatically through your bank or a "
            "provider offering Raast merchant payments, which confirms orders for you."),
    takeaways=[
        "Raast is the State Bank of Pakistan's instant payment system, which moves money between bank accounts in seconds.",
        "Its merchant service accepts payments by QR code, Raast alias, IBAN and request-to-pay, according to the State Bank.",
        "A manual set-up is quick and free but needs someone to confirm every payment against the bank statement.",
        "An automated set-up through a bank or provider confirms payments and updates orders without staff checks.",
        "Never mark an order paid from a screenshot alone; check the money has arrived in your account.",
    ],
    body=f"""
<h2 id="what-is-raast">What Is Raast and How Does Raast Payment Integration Work?</h2>
<p>Raast is the State Bank of Pakistan's instant payment system. It moves money between bank accounts, and accounts at participating wallets and microfinance banks, in seconds. People can use a Raast ID, usually their mobile number linked to their bank account, instead of a long account number.</p>
<p>For businesses, the State Bank introduced a person-to-merchant service. In a press release dated 6 December 2023, the State Bank listed four ways shops can be paid: a unified QR code, a Raast alias like a phone number, an IBAN, or a request-to-pay sent to the buyer. It also told banks not to charge buyers for paying this way.</p>
<p>Raast payment integration on a website means letting customers choose Raast or bank transfer at checkout, then confirming the payment so the order can be packed.</p>

<h2 id="manual-vs-automated">Should You Use a Manual or Automated Set-Up?</h2>
<table>
<tr><th>Factor</th><th>Manual set-up</th><th>Automated set-up</th></tr>
<tr><td>How it works</td><td>Checkout shows your Raast ID, IBAN or QR; you confirm each payment</td><td>Your bank or provider confirms payment and updates the order</td></tr>
<tr><td>Time to start</td><td>About a day</td><td>Weeks, depending on approval and integration</td></tr>
<tr><td>Staff time</td><td>Someone checks every payment</td><td>Little</td></tr>
<tr><td>Risk of error</td><td>Higher: wrong amounts, fake screenshots</td><td>Lower</td></tr>
<tr><td>Best for</td><td>Up to a few dozen transfer orders a day</td><td>Higher volumes or round-the-clock sales</td></tr>
</table>
<p>Ask your bank, and your payment gateway if you have one, whether they offer Raast merchant acceptance for online checkout and what it costs to integrate.</p>

<h2 id="manual-flow">How Does a Manual Raast Checkout Work?</h2>
<p>A manual flow uses your store's built-in "bank transfer" payment method. On WooCommerce this is a standard option; on Shopify it is a manual payment method. A good flow looks like this:</p>
<ol>
<li><strong>Customer chooses Raast or bank transfer</strong> at checkout and places the order. The order is saved as "awaiting payment".</li>
<li><strong>The thank-you page and email show</strong> your Raast ID, account title, IBAN and a QR code, plus the exact amount and order number.</li>
<li><strong>The customer pays</strong> from their banking app, adding the order number in the payment note if the app allows.</li>
<li><strong>The customer sends a screenshot</strong> on WhatsApp, or uploads it through a form linked to the order.</li>
<li><strong>Your team checks the bank account</strong>, finds the matching amount and reference, and marks the order paid.</li>
<li><strong>The customer gets a confirmation</strong> message with the expected delivery date.</li>
</ol>
<p>Set a time limit, such as 24 hours, after which unpaid orders are cancelled and stock is released.</p>

<h2 id="reconciliation">How Do You Reconcile Payments Without Mistakes?</h2>
<p>Reconciliation means matching each payment in your bank account with the right order. It is where manual set-ups go wrong. Follow these steps every day:</p>
<ol>
<li>Download or view the day's incoming transactions from your bank.</li>
<li>Filter your store's orders by "awaiting payment".</li>
<li>Match each payment by amount, sender name and order number.</li>
<li>Mark matched orders paid and note the bank reference in the order.</li>
<li>Message customers whose payment is short, extra or missing.</li>
<li>Keep a simple log of unmatched payments until resolved.</li>
</ol>
<p>Use one bank account for store payments only. Mixing personal and store payments makes matching much harder.</p>

<h2 id="fraud">How Do You Avoid Fake Payment Screenshots?</h2>
<p>Fake screenshots are a known trick in Pakistani online selling. A screenshot proves nothing until the money is in your account. Protect yourself:</p>
<ul>
<li>never dispatch until the payment appears in your own bank app or statement</li>
<li>check the amount, time and sender name, not only the transaction ID on the image</li>
<li>be extra careful with high-value orders placed late at night</li>
<li>train staff that "the customer is in a hurry" is never a reason to skip the check</li>
</ul>

<h2 id="example">A Worked Example: Reducing COD Returns With Raast</h2>
<p>Illustrative example, not a real client. A home-décor store offers Rs 150 off for orders paid by Raast. Customers who pay first rarely refuse delivery, so returned parcels on those orders fall. The discount costs less than a returned parcel, which carries delivery charges both ways. Test a small discount on your own store and compare return rates by payment method. Our guide to <a href="/digital/blog/cod-website-fake-orders-pakistan">reducing COD fake orders and returns</a> covers other ways to do this.</p>

<h2 id="what-we-build">How We Add Raast and Bank Transfer Checkout</h2>
<p>As part of our online store package, from {P['store']}, we set up a Raast and bank transfer option with clear payment instructions, a QR code on the thank-you page and email, an "awaiting payment" order status, a WhatsApp link for payment proof and automatic cancellation of unpaid orders. Where your bank or provider offers automated Raast confirmation for online checkout, we quote the integration in the written scope. See our <a href="/digital/ecommerce-development">online store development</a> service.</p>

<h2 id="next-step">Questions to Ask Your Bank</h2>
<ol>
<li>Can I accept Raast merchant payments for online orders?</li>
<li>Is there an automated confirmation or API for websites?</li>
<li>What are the merchant charges, if any?</li>
<li>Can I get a dedicated account and QR code for store payments?</li>
</ol>
<p>For the wider picture, read our <a href="/digital/blog/payment-gateways-pakistan-compared">payment gateway comparison</a> and <a href="/digital/blog/start-online-store-pakistan">how to start an online store in Pakistan</a>.</p>
""",
    faqs=[
        ("What is Raast in simple words?",
         "Raast is the State Bank of Pakistan's instant payment system. It moves money between bank accounts in seconds, using a Raast ID such as a mobile number or an IBAN. Its merchant service lets businesses accept payments by QR code, alias, IBAN or request-to-pay, which suits online stores and shops."),
        ("Can I accept Raast payments on my website?",
         "Yes. The simplest way is to show your Raast ID, IBAN and QR code at checkout, then confirm each payment manually against your bank account. For automatic confirmation, ask your bank or payment provider whether it offers Raast merchant acceptance for online checkout and what integration it supports."),
        ("Does Raast charge customers a fee?",
         "According to the State Bank of Pakistan's press release of 6 December 2023, banks and other regulated entities cannot charge customers any fee for using Raast payment options. Merchant charges may apply depending on your bank or provider, so ask them for their current terms in writing before you set it up."),
        ("How do I confirm a bank transfer payment for an online order?",
         "Check that the money has arrived in your own bank account before you dispatch. Match the payment by amount, sender name and the order number in the payment note. A screenshot sent by the customer is useful as a reference, but it is not proof of payment on its own."),
        ("Is Raast better than cash on delivery for an online store?",
         "For the seller, often yes: you receive the money before dispatch, so refused deliveries and fake orders fall. Many customers still prefer cash on delivery, especially with a new brand. Offer both, and consider a small discount or faster dispatch for customers who pay through Raast."),
        ("Raast se online store par payment kaise lein?",
         "Checkout par apna Raast ID, IBAN aur QR code dikhayen. Customer apni banking app se payment kare aur order number note mein likhe. Phir apne bank account mein check karein ke paisay aa gaye hain, sirf screenshot par bharosa na karein, aur order ko paid mark kar ke dispatch karein."),
    ],
    sources=[
        ("State Bank of Pakistan — Press release on Raast P2M, 6 December 2023", "https://www.sbp.org.pk/press/2023/Pr-06-Dec-2023.pdf"),
        ("State Bank of Pakistan — Homepage", "https://www.sbp.org.pk/"),
        ("Shopify Help Center — Third-party payment providers", "https://help.shopify.com/en/manual/payments/third-party-providers"),
        ("WhatsApp Help Center — How to use click to chat", "https://faq.whatsapp.com/5913398998672934"),
        ("WooCommerce — Extensions marketplace", "https://woocommerce.com/products/"),
    ],
    method=("Raast's merchant payment modes and the no-customer-fee rule come from the State Bank of Pakistan's press release of 6 December "
            "2023, opened 29 October 2026. The checkout and reconciliation steps are the flow we set up for stores. The discount example "
            "is illustrative. Store prices are our own published package."),
    related=["start-online-store-pakistan", "payment-gateways-pakistan-compared", "cod-website-fake-orders-pakistan",
             "stripe-paypal-pakistan-website"],
    service_links=[("/digital/ecommerce-development", "Stores with Raast and bank transfer checkout"), ("/digital/contact", "Get help setting up Raast")],
    cta="Want Raast payments on your store?",
    wa="Hi%2C%20I%20read%20your%20Raast%20payment%20guide%20and%20need%20help%20setting%20it%20up",
)
