import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=120,
    slug='website-data-privacy-when-using-ai',
    title='Website AI Privacy: Customer Data and AI Tools',
    h1='Customer Data, Privacy and AI Tools on Your Website: A Practical Guide to Website AI Privacy',
    crumb='Website AI Privacy',
    description='Website AI privacy in practice: what never to send to AI tools, consent and notice wording, retention of chat logs, provider settings and the regulators to follow.',
    keyword='website ai privacy',
    cluster=['chatbot data privacy', 'customer data protection website pakistan', 'gdpr chatbot'],
    category='AI and Automation',
    published='2026-10-30',
    published_h='30 October 2026',
    updated='2026-10-30',
    updated_h='30 October 2026',
    answer="Good website AI privacy means sending AI tools only the data they need, telling visitors clearly when AI handles their messages, keeping chat logs for a fixed period such as 90 days, and choosing provider settings that keep customer data out of model training where possible. UK and EU visitors bring GDPR duties.",
    takeaways=["Never paste CNIC numbers, card details, passwords or health records into AI tools.", "Tell visitors in plain words when an AI tool reads or answers their messages.", "Set a retention period for chat logs and lead data, and actually delete on schedule.", "Check each AI provider's data-use and retention settings before connecting customer data.", "For UK and EU visitors, follow the ICO and EU regulators' guidance; for Pakistan, ask your adviser about current law."],
    body=f"""
<h2 id="why">Why Does Website AI Privacy Matter for a Small Business?</h2>
<p>Once a website has a chatbot, an AI writing tool connected to its forms, or an automation that sends enquiries to an AI service, customer data starts travelling to more places. A visitor typing a question into a chat box may include their phone number, home address, a child's school or a medical concern. Website AI privacy is about knowing where that information goes, keeping as little of it as possible, and being honest with visitors about it.</p>
<p>This is a practical guide, not legal advice. Laws differ by country and change, so treat it as a checklist to discuss with your adviser. It accompanies our pillar guide to <a href="/digital/blog/ai-chatbot-for-business-website-cost-pakistan">AI chatbots for business websites</a>.</p>

<h2 id="never-send">What Should You Never Send to AI Tools?</h2>
<table>
<tr><th>Data</th><th>Why to keep it out</th></tr>
<tr><td>CNIC, passport and other ID numbers</td><td>Identity theft risk if logs leak</td></tr>
<tr><td>Card numbers, bank details, passwords, OTPs</td><td>Direct financial risk; payment pages should handle these</td></tr>
<tr><td>Health and medical details</td><td>Special category data under GDPR; highly sensitive everywhere</td></tr>
<tr><td>Children's personal details</td><td>Extra protection expected in most regimes</td></tr>
<tr><td>Staff HR files and salaries</td><td>Confidential and unrelated to customer service</td></tr>
<tr><td>Full customer lists</td><td>Rarely needed for an AI task; send only the fields required</td></tr>
</table>
<p>Configure chat widgets to warn visitors not to share such details, and where possible mask numbers that look like card or CNIC numbers before they reach the AI service.</p>

<h2 id="notice">How Should You Tell Visitors?</h2>
<p>Put a one-line notice at the top of the chat window, for example: "This assistant uses AI to answer questions. Please do not share card, ID or health details. Messages are kept for 90 days. Ask for a person at any time." Then explain the same points in your privacy policy: what you collect through chat and forms, why, which service providers process it, how long you keep it and how people can ask for deletion. The ICO's guidance on explaining decisions made with AI is a useful reference on transparency.</p>

<h2 id="consent">Do You Need Consent?</h2>
<p>It depends on the purpose and the law that applies. Answering a question someone has asked is different from using their messages for marketing. Under UK and EU data protection law, organisations need a lawful basis for processing, which is not always consent; marketing messages usually need clear opt-in. Keep marketing permission separate from chat: an unticked box such as "Send me offers on WhatsApp" is clearer than assuming agreement because someone asked a question.</p>

<h2 id="retention">How Long Should You Keep Chat Logs?</h2>
<p>Only as long as you need them. Many small businesses can keep chat transcripts for a few months to resolve disputes and improve answers, then delete them. Pick a period, write it in your privacy policy, and set the deletion to run automatically. Remember copies: logs may sit in the chat tool, the AI provider, your email and your automation tool. Our <a href="/digital/blog/automate-website-leads-whatsapp-email">lead automation guide</a> covers mapping where data travels.</p>

<h2 id="providers">What Should You Check With AI Providers?</h2>
<ul>
<li>Whether business data sent through the API is used to train models, and how to opt out if so.</li>
<li>How long the provider retains inputs and outputs, and where it stores them.</li>
<li>Whether a data processing agreement is available.</li>
<li>Who on your side has access to the account, with two-step verification turned on.</li>
</ul>
<p>Read these on the provider's official policy pages, not in marketing material, and note the date you checked.</p>

<h2 id="regulators">Which Rules Apply to You?</h2>
<p>If you serve people in the UK, the ICO publishes guidance on AI and data protection. EU visitors bring the GDPR, overseen by national regulators and the European Data Protection Board. In Pakistan, the Prevention of Electronic Crimes Act 2016 covers some data misuse, and a dedicated personal data protection law has been under discussion for years; ask your adviser about its current status before relying on any summary. Businesses serving the Gulf should check local rules in each country.</p>

<h2 id="security">What Basic Security Steps Help?</h2>
<p>Use HTTPS on every page, restrict who can read chat logs, keep plugins updated and log administrator access. AI features add new risks such as prompt injection, where a user tries to make the assistant reveal hidden instructions or data; OWASP's list of risks for large language model applications explains these. Our <a href="/digital/blog/ai-customer-support-website-build-or-buy">AI support guide</a> covers handover and limits.</p>

<h2 id="build">How We Build Privacy In</h2>
<p>In the AI features we build as web apps, from {P['app']}, we send the AI only the fields it needs, add chat notices, set retention periods and keep your accounts in your name. See <a href="/digital/web-app-development">web app development</a>.</p>
""",
    faqs=[
        ('What customer data should never go into an AI chatbot?',
         "Keep out CNIC and passport numbers, card and bank details, passwords and one-time codes, health information, children's details and full customer lists. Warn visitors in the chat window not to share them, and where possible mask numbers that look like card or ID numbers before they reach the AI service."),
        ('Do I need to tell visitors that a chatbot uses AI?',
         "Being open about it is good practice and expected under UK and EU guidance on transparency. A one-line notice in the chat window, plus a section in your privacy policy explaining what is collected, which providers process it and how long it is kept, covers the basics."),
        ('How long should a business keep chatbot logs?',
         "Only as long as needed to resolve queries, handle disputes and improve answers, often a few months for a small business. Choose a period, state it in your privacy policy and automate deletion. Remember copies held by the chat tool, the AI provider, email and automation tools."),
        ('Does GDPR apply to a Pakistani business website?',
         "It can apply when you offer goods or services to people in the UK or EU or monitor their behaviour online. Overseas-focused Pakistani businesses should take advice. The ICO and the European Data Protection Board publish official guidance on what organisations need to do."),
        ("Do AI providers train their models on my customers' data?",
         "It depends on the provider, product and settings. Read the provider's official data-use and retention pages, check whether business or API data is used for training, choose opt-out settings where offered, and note the date you checked because these policies change."),
        ('What is prompt injection and should a small business worry?',
         "Prompt injection is when someone types instructions designed to make an AI assistant ignore its rules or reveal hidden data. Limit what the assistant can access, never give it secrets, and test it with tricky inputs. OWASP lists this among the main risks for AI applications."),
        ('Chatbot mein customer ka data mehfooz kaise rakhein?',
         "Customer se CNIC, card number ya bimari ki tafseel chat mein na mangwayen. Chat ke upar likh dein ke AI jawab deta hai aur messages kitne din rakhe jayenge. Purane chat logs waqt par delete karein, aur AI company ki privacy settings check karke training wala option band karein."),
    ],
    sources=[('ICO — Artificial intelligence guidance index', 'https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/'), ('ICO — UK GDPR guidance and resources', 'https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/'), ('European Data Protection Board', 'https://www.edpb.europa.eu/'), ('OWASP — Top 10 for Large Language Model Applications', 'https://owasp.org/www-project-top-10-for-large-language-model-applications/'), ('Google Search Central — Using generative AI content', 'https://developers.google.com/search/docs/fundamentals/using-gen-ai-content')],
    method="Regulator references come from the ICO's AI guidance index, checked 30 October 2026, and the EDPB site. The Pakistan law note states only that PECA 2016 exists and a dedicated data protection law has been discussed; readers are directed to an adviser. The 90-day figure is an example, not a rule. This is not legal advice.",
    related=['ai-chatbot-for-business-website-cost-pakistan', 'automate-website-leads-whatsapp-email', 'ai-customer-support-website-build-or-buy', 'whatsapp-business-api-cost-pakistan'],
    service_links=[('/digital/pricing', 'Our published prices'), ('/digital/web-app-development', 'Web app development')],
    cta='Adding AI but worried about customer data?',
    wa='Hi%2C%20I%20read%20your%20website%20AI%20privacy%20guide',
)
