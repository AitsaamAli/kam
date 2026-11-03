import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=250,
    slug="website-migration-charges",
    title="Website Migration Cost: Moving Hosts or Platforms",
    h1="Website Migration Cost: Moving to a New Host or a New Platform Without Breaking Things",
    crumb="Website Migration Cost",
    description="What drives website migration cost: small host moves versus platform changes, the risk items that need care, testing, redirects and what to agree before starting.",
    keyword="website migration cost",
    cluster=["website transfer charges", "platform migration price", "host migration price",
             "store platform change cost", "migration testing checklist"],
    category="Costs & Budgets",
    published="2026-11-03", published_h="3 November 2026",
    updated="2026-11-03", updated_h="3 November 2026",
    answer=(f"Website migration cost depends mainly on what moves. Moving a small site to a new host is usually a short, low-risk job. "
            f"Moving platforms, such as WooCommerce to Shopify, involves products, customers, orders, URLs and redirects, and takes much longer. "
            f"Risk items such as email, payments and SEO need testing. Store rebuilds start at {P['store']}."),
    takeaways=[
        "Host moves keep the same site; platform moves rebuild it elsewhere, which costs far more.",
        "The risk items are email, DNS, payments, forms, SEO redirects and customer accounts.",
        "Agree the scope in writing: what data moves, what is rebuilt and what is tested.",
        "A full backup before the move and a testing checklist after it protect you from losses.",
        "Plan the switch-over for a quiet time and keep the old setup running until the new one is confirmed.",
    ],
    body=f"""
<h2 id="types">Two Kinds of Migration</h2>
<p>People use "migration" for two very different jobs. A <strong>host migration</strong> moves the same website, such as a WordPress site, from one hosting company to another. The site looks and works the same afterwards. A <strong>platform migration</strong> moves the business to different software, such as from WooCommerce to Shopify or from Wix to WordPress. That is effectively a rebuild with data transfer. Website migration cost differs enormously between the two, so be clear which one you need. Our guide to <a href="/digital/blog/move-website-to-new-hosting">moving a website to new hosting</a> covers the first, and our guide to <a href="/digital/blog/migrate-woocommerce-to-shopify-or-back">migrating between WooCommerce and Shopify</a> covers a common platform move.</p>

<h2 id="small-large">What Separates a Small Migration From a Large One?</h2>
<table>
<tr><th>Factor</th><th>Small migration</th><th>Large migration</th></tr>
<tr><td>Type</td><td>Same platform, new host</td><td>New platform</td></tr>
<tr><td>Size</td><td>A few pages, a small database</td><td>Hundreds of products, thousands of orders and customers</td></tr>
<tr><td>Email</td><td>Email stays with its current provider</td><td>Mailboxes move too</td></tr>
<tr><td>URLs</td><td>Stay the same</td><td>Change, so every one needs a redirect</td></tr>
<tr><td>Integrations</td><td>A contact form</td><td>Payments, couriers, ERP, marketing tools</td></tr>
<tr><td>Design</td><td>Unchanged</td><td>New theme, rebuilt on the new platform</td></tr>
</table>

<h2 id="risks">Which Risk Items Need the Most Care?</h2>
<ul>
<li><strong>Email:</strong> changing DNS can interrupt email if MX records are not copied exactly.</li>
<li><strong>DNS and SSL:</strong> the domain must point to the new server with HTTPS working from the first minute.</li>
<li><strong>Payments:</strong> gateways may need new credentials or approval on a new platform.</li>
<li><strong>Forms and notifications:</strong> contact forms and order emails often stop working after a move until mail settings are fixed.</li>
<li><strong>SEO:</strong> changed URLs without redirects lose rankings; Google's site move guidance explains the steps.</li>
<li><strong>Customer accounts and passwords:</strong> on platform moves, passwords usually cannot be transferred, so customers need a reset invitation.</li>
</ul>

<h2 id="testing">What Should Be Tested After a Migration?</h2>
<ol>
<li>Every page template loads on mobile and desktop, with HTTPS.</li>
<li>Forms send to the right inbox and WhatsApp.</li>
<li>Test orders go through with each payment method, and order emails arrive.</li>
<li>Old URLs redirect to the right new pages.</li>
<li>Email sends and receives on the business domain.</li>
<li>Analytics, Search Console and pixels record visits.</li>
</ol>
<p>Our <a href="/digital/blog/website-testing-before-sign-off">testing checklist before sign-off</a> covers more checks.</p>

<h2 id="agree">What Should You Agree Before Starting?</h2>
<p>Write down what data moves (pages, products, customers, orders, reviews, blog posts), what is rebuilt, which integrations are reconnected, who handles DNS and email, how long the old site stays live, and what testing happens before switch-over. A full backup must be taken before anything changes. Agree a quiet time for the switch, such as early in the week, outside your sales peaks.</p>

<h2 id="price">What Drives Website Migration Cost?</h2>
<p>Host migrations of small sites are usually short jobs, often included for clients on maintenance from {P['maint']} a month. Platform migrations are priced like a new build plus data transfer: store migrations start from our store package at {P['store']}, and business sites from our business package at {P['business']}. Very large catalogues, custom integrations or complex customer data add time. We quote after reviewing the current site and the target platform. See our <a href="/digital/pricing">published prices</a>.</p>

<h2 id="timing">Choosing When to Switch</h2>
<p>Avoid switching during your busiest periods, such as Eid sales for a clothing store or admissions season for a school. Lower DNS time-to-live settings a day before the switch so the change spreads quickly, make the switch early in a working week, and have the developer available for the first days afterwards. For stores, pause new product uploads during the final data transfer so nothing is missed, and announce a short maintenance window if orders must be paused.</p>

<h2 id="after">After the Migration</h2>
<p>Keep the old hosting for a short period until everything is confirmed, then cancel it. Watch Search Console for crawl errors, check orders and enquiries daily for the first two weeks, and fix any missed redirects quickly.</p>
""",
    faqs=[
        ("What is the difference between a host migration and a platform migration?",
         "A host migration moves the same website to a new hosting company, so it looks and works the same afterwards. A platform migration moves the business to different software, such as WooCommerce to Shopify, which is effectively a rebuild with data transfer and costs much more."),
        ("What can go wrong when migrating a website?",
         "Email can stop if MX records are not copied, HTTPS may fail, payment gateways may need new credentials, forms and order emails often break, changed URLs without redirects lose rankings, and customer passwords usually cannot move between platforms. Each needs planning and testing."),
        ("How do I avoid losing SEO during a platform migration?",
         "Map every old URL to its new equivalent and set up 301 redirects, keep page titles and content where possible, submit the new sitemap, and watch Search Console for errors in the weeks after launch. Google's site move documentation explains the full process."),
        ("Can customer accounts be moved to a new store platform?",
         "Customer names, emails, addresses and order history can usually be imported, but passwords normally cannot be moved, because platforms store them in encrypted form. Plan to send customers a friendly invitation to reset their password on the new store after the switch."),
        ("What should a website migration quote include?",
         "It should list what data moves, what is rebuilt, which integrations are reconnected, who handles DNS and email, the backup before work starts, the testing checklist, the switch-over date and how long the old site stays live. Without this, costs and risks are unclear."),
        ("How much does a website migration cost?",
         f"A small host move is usually a short job, often included for clients on maintenance from {P['maint']} a month. Platform migrations are priced like a new build plus data transfer, starting from our store package at {P['store']} for online stores and our business package at {P['business']} for business sites."),
        ("Website ko nayi hosting ya platform par shift karne ka kharcha kitna hai?",
         "Agar sirf hosting badalni hai to aam tor par chhota kaam hai. Agar platform badalna hai, jaise WooCommerce se Shopify, to products, customers, orders, URLs aur redirects sab muntaqil hote hain aur kharcha zyada hai. Pehle poora backup lein aur shift ke baad email, payment aur forms test karein."),
    ],
    sources=[
        ("Google Search Central: Site moves with URL changes", "https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes"),
        ("Google Search Central: Site moves without URL changes", "https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes"),
        ("WordPress Developer Resources: Moving WordPress", "https://developer.wordpress.org/advanced-administration/upgrade/migrating/"),
        ("Google Search Central: Redirects and Google Search", "https://developers.google.com/search/docs/crawling-indexing/301-redirects"),
        ("WordPress Developer Resources: Backups", "https://developer.wordpress.org/advanced-administration/security/backup/"),
    ],
    method="We separated host and platform migrations, used Google's site move documentation and WordPress's migration and backup guides, and listed the risk items we check on every move. Prices come from our published packages rather than market rates. Sources checked on 3 November 2026.",
    related=["move-website-to-new-hosting", "migrate-woocommerce-to-shopify-or-back", "website-testing-before-sign-off", "new-website-without-losing-google-traffic"],
    service_links=[("/digital/pricing", "Our published prices"), ("/digital/contact", "Get a written quote")],
    cta="Planning to move your website and want nothing to break?",
    wa="Hi%2C%20I%20read%20your%20guide%20on%20website%20migration%20costs.%20I%20would%20like%20a%20quote.",
)
