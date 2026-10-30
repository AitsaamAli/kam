import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=114,
    slug='whatsapp-business-api-cost-pakistan',
    title='WhatsApp Business API in Pakistan: Costs and Setup',
    h1='WhatsApp Business API in Pakistan: Costs, Setup and Connecting It to Your Website',
    crumb='WhatsApp Business API',
    description="How the WhatsApp Business API works in Pakistan: Meta's per-message charging, provider fees, the free app vs the API, and order alerts from your website.",
    keyword='whatsapp business api pakistan',
    cluster=['whatsapp api price pakistan', 'whatsapp business api provider pakistan', 'whatsapp automation for business'],
    category='AI and Automation',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="The WhatsApp Business API in Pakistan is charged by Meta per delivered template message, by category: marketing, utility or authentication. Replies to customers inside the 24-hour service window are free. Pakistan has its own rate on Meta's rate card. Providers may add platform fees, and most small shops still do fine with the free app.",
    takeaways=["The free WhatsApp Business app suits most small Pakistani businesses with one or two staff answering.", "The API is for automation: order alerts, many agents, chatbots and links with your website or store.", "Since 1 July 2025 Meta charges per delivered template message, by category, with Pakistan priced as its own market.", "Free-form replies inside the 24-hour customer service window cost nothing from Meta.", "Check Meta's official rate card for current Pakistan rates; they change only at the start of a quarter."],
    body=f"""
<h2 id="app-or-api">Do You Need the WhatsApp Business API in Pakistan, or Is the App Enough?</h2>
<p>Most Pakistani shops, clinics and service firms run on the free WhatsApp Business app, and for many of them that is the right choice. The app gives you a business profile, a catalogue, quick replies, labels and an away message, and it works on a phone plus a few linked devices. The WhatsApp Business API, which Meta now calls the WhatsApp Business Platform, is a different product. It has no phone app of its own; software talks to it, so you need either a provider's dashboard or a custom system to use it.</p>
<p>Move to the API when one phone is no longer enough: when several agents must answer from one number, when you want automatic order confirmations from your online store, when a chatbot should answer first, or when you need messages to be logged in your own system. Our <a href="/digital/blog/ai-chatbot-for-business-website-cost-pakistan">AI chatbot guide</a> explains when automated replies make sense at all.</p>

<table>
<tr><th>Need</th><th>Free Business app</th><th>Business API</th></tr>
<tr><td>One or two people replying</td><td>Yes</td><td>Possible, usually unnecessary</td></tr>
<tr><td>Many agents on one number</td><td>Limited</td><td>Yes, through a dashboard</td></tr>
<tr><td>Automatic order and delivery updates</td><td>No</td><td>Yes, with approved templates</td></tr>
<tr><td>Chatbot answering first</td><td>No</td><td>Yes</td></tr>
<tr><td>Cost from Meta</td><td>Free</td><td>Per delivered template message</td></tr>
</table>

<h2 id="pricing">How Does Meta Charge for the API?</h2>
<p>Meta's developer documentation, checked on 30 October 2026, says the platform moved to per-message pricing on 1 July 2025. You pay when a template message is delivered, and the charge depends on two things: the message category and the recipient's country code. There are three paid categories:</p>
<ul>
<li><strong>Marketing:</strong> offers, announcements, abandoned basket reminders.</li>
<li><strong>Utility:</strong> updates about something the customer already did, such as an order confirmation or delivery update.</li>
<li><strong>Authentication:</strong> one-time passcodes for logging in.</li>
</ul>
<p>When a customer messages you, a 24-hour customer service window opens. Inside it, your free-form replies are not charged, and Meta's documentation also says utility templates sent inside an open window are free. People who reach you through a Click to WhatsApp ad or a Facebook Page call-to-action open a longer free entry-point window of 72 hours, under the conditions Meta sets out.</p>
<p>Pakistan is listed as its own market in Meta's rate cards, with separate rates per category. Volume tiers apply to utility and authentication messages and reset monthly. We do not quote a rupee figure here, because Meta publishes rates in its rate card files and changes them only on the first day of a quarter; check the current card before you budget.</p>

<h2 id="providers">What Do Providers Charge on Top?</h2>
<p>You can connect to the API directly through Meta's Cloud API, or through a business solution provider that supplies a shared inbox, template tools and a chatbot builder. Providers set their own platform fees, usually monthly, sometimes per agent and sometimes with a markup on messages. Ask any provider for three numbers in writing: the monthly platform fee, whether they add anything on top of Meta's message charges, and what happens to your number and chat history if you leave.</p>

<h2 id="setup">What Does Setting It Up Involve?</h2>
<ol>
<li>A verified Meta Business portfolio in your company's name.</li>
<li>A phone number not already active on the WhatsApp app, or one you migrate over.</li>
<li>A display name that matches your business, approved by Meta.</li>
<li>Message templates for anything you send first, each approved and placed in a category.</li>
<li>A payment method on the WhatsApp account for template charges.</li>
<li>Software to send and receive: a provider's dashboard or your own system.</li>
</ol>
<p>Customers must have opted in to receive messages from you. A tick box at checkout that says what you will send, such as order updates on WhatsApp, is a clear way to collect that agreement.</p>

<h2 id="store">How Do Order Notifications from a Website Work?</h2>
<p>When an order is placed on your store, the website calls the API with an approved utility template, such as "Your order 1042 is confirmed, total Rs 4,500, expected delivery Thursday". Later events, dispatch and delivery, trigger further templates. For cash on delivery stores, a confirmation message that asks the customer to reply can reduce wasted dispatches, though results vary by product and customer. Connecting this is integration work on the store; see our guide to fake COD orders and <a href="/digital/blog/automate-website-leads-whatsapp-email">lead automation guide</a> for the wider flow.</p>

<h2 id="mistakes">What Mistakes Should You Avoid?</h2>
<ul>
<li>Sending marketing to people who only agreed to order updates; users can block or report you, which can affect your number's quality rating.</li>
<li>Labelling promotional messages as utility; Meta can reclassify templates.</li>
<li>Putting your only business number on a provider without a clear exit plan.</li>
<li>Skipping a human handover when a chatbot cannot help.</li>
</ul>

<h2 id="cost-to-build">What Would We Charge to Connect It?</h2>
<p>A WhatsApp click-to-chat button with pre-filled messages comes with every website we build, from {P['starter']}. Connecting the API to an online store for order alerts, or building a shared inbox or bot, is custom work quoted after we see your flow; larger systems fall into our web app range from {P['app']}. Meta's message charges are paid by you directly to Meta or through your provider. See our <a href="/digital/web-app-development">web app development</a> page.</p>
""",
    faqs=[
        ('How much does the WhatsApp Business API cost in Pakistan?',
         "Meta charges per delivered template message, with separate Pakistan rates for marketing, utility and authentication messages listed in its official rate card. Free-form replies inside the 24-hour service window are free. Providers may add platform fees. Check Meta's current rate card before budgeting, because rates change each quarter."),
        ('Is the WhatsApp Business app free in Pakistan?',
         "Yes. The WhatsApp Business app is free to download and use. It suits small businesses with one or a few people replying. Charges apply only on the API, where Meta bills businesses for delivered template messages such as order updates, offers and login codes."),
        ('What is the 24-hour customer service window?',
         "When a customer sends you a message, a 24-hour window opens. During it you can reply with free-form messages at no charge from Meta, and utility templates sent inside the window are also free according to Meta's documentation. Outside the window you need an approved template."),
        ('Do I need a provider to use the WhatsApp API?',
         "No. You can use Meta's Cloud API directly, but you then need software to send and receive messages. Providers supply a ready dashboard, inbox and bot builder for a fee. A developer can also build those features into your own website or system."),
        ('Can my online store send WhatsApp order confirmations automatically?',
         "Yes, through the API. Your store sends an approved utility template when an order is placed, shipped or delivered. Customers must have agreed to receive these messages, for example through a clearly worded tick box at checkout. Setting it up is integration work on the store."),
        ('Can I keep my existing WhatsApp number for the API?',
         "Often yes, but a number active on the app must be moved over, and how chat history is handled depends on the method used. Back up important chats first and confirm the exact process with your provider or developer before switching your main business number."),
        ('WhatsApp Business API Pakistan mein kitne ka hai?',
         "Meta har deliver hone wale template message ka charge leta hai, aur Pakistan ke rates marketing, utility aur authentication ke liye alag hain. Customer ke message ke baad 24 ghante tak jawab muft hain. Provider apni fee alag le sakta hai. Budget se pehle Meta ka taaza rate card zaroor dekhein."),
    ],
    sources=[('Meta for Developers — WhatsApp Business Platform pricing', 'https://developers.facebook.com/docs/whatsapp/pricing'), ('Meta for Developers — WhatsApp Cloud API overview', 'https://developers.facebook.com/docs/whatsapp/cloud-api'), ('WhatsApp Business — Business Platform', 'https://business.whatsapp.com/products/business-platform'), ('WhatsApp Help Center — How to use click to chat', 'https://faq.whatsapp.com/5913398998672934')],
    method="Charging rules come from Meta's WhatsApp pricing documentation, checked 30 October 2026: per-message pricing since 1 July 2025, three paid categories, the 24-hour and 72-hour windows, Pakistan as its own market. No Pakistan rupee rate is quoted because the figures sit in Meta's rate card files. Our prices come from the published list.",
    related=['ai-chatbot-for-business-website-cost-pakistan', 'automate-website-leads-whatsapp-email', 'ai-customer-support-website-build-or-buy'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/web-app-development', 'Web app development')],
    cta='Need order alerts on WhatsApp?',
    wa='Hi%2C%20I%20read%20your%20WhatsApp%20Business%20API%20guide',
)
