"""Builds /dnfbp-compliance-services (service landing page) from the aop-tax-return.html shell.
Facts reuse the DNFBP guides in content/dnfbp-2026/posts.py (checked 9 November 2026 against FBR, FMU and SRO texts)."""
import html, json, re, sys
sys.path.insert(0, "/home/user/kam/content/dnfbp-2026")
from posts import S_INTRO, S_REGS, S_FAQ23, S_950, S_1497, S_GOAML

ROOT = "/home/user/kam"
BASE = "https://kambohassociates.com"
SLUG = "dnfbp-compliance-services"
URL = f"{BASE}/{SLUG}"
E = html.escape
TITLE = "DNFBP Compliance Services in Pakistan | Kamboh Associates"
DESC = "DNFBP compliance done for you: FBR registration, goAML, AML/CFT policy, CDD forms and inspection support for real estate agents, jewellers and accountants."
H1 = "DNFBP Compliance Services: FBR Registration, goAML and AML/CFT Set-Up"
WA = "https://wa.me/923284675162?text=" + "Assalam%20o%20Alaikum%2C%20DNFBP%20registration%20aur%20compliance%20chahiye."
L = 'style="color:#0D9488;font-weight:600"'

FAQS = [
    ("Who has to register as a DNFBP with FBR?", "FBR supervises real estate agents (including builders and developers when they deal in property), dealers in precious metals and stones who take cash of Rs 2 million or more in a transaction, and accountants not regulated by ICAP or ICMAP when they carry out the listed activities."),
    ("What does DNFBP compliance involve after registration?", "Appointing a compliance officer, a written risk assessment and AML/CFT policy, customer due diligence, sanctions screening, reporting suspicious and large cash transactions to the FMU on goAML, and keeping records for the required period."),
    ("What is the penalty for not complying?", "The AML/CFT Sanctions Rules 2020 (S.R.O. 950(I)/2020) allow penalties of up to Rs 100 million per violation, and significant sanctions are published with the business name."),
    ("Is goAML registration separate from FBR registration?", "Yes. DNFBP registration is done with FBR on IRIS; goAML is the Financial Monitoring Unit's reporting portal, which needs its own registration."),
    ("How much does DNFBP compliance cost with Kamboh Associates?", "A fixed fee, confirmed on WhatsApp before any work starts, based on your category and the size of your business."),
    ("Which FBR office handles DNFBPs in my city?", "S.R.O. 1497(I)/2026 (2 September 2026) sets the jurisdiction of DNFBP authorities. Our city guides explain which directorate covers Lahore, Karachi, Islamabad, Peshawar and Quetta."),
]
SOURCES = [S_INTRO, S_REGS, S_FAQ23, S_950, S_1497, S_GOAML]

GUIDES = [
    ("/blogs/dnfbp-registration-pakistan", "DNFBP registration in Pakistan: the full guide"),
    ("/blogs/real-estate-agent-dnfbp-registration-aml-pakistan", "Real estate agents and developers"),
    ("/blogs/jeweller-dnfbp-registration-aml-pakistan", "Jewellers and dealers in precious metals and stones"),
    ("/blogs/accountant-dnfbp-registration-aml-pakistan", "Accountants"),
    ("/blogs/goaml-registration-dnfbp-pakistan", "goAML registration step by step"),
    ("/blogs/aml-cft-compliance-programme-dnfbp-pakistan", "Building an AML/CFT compliance programme"),
]
CITIES = [
    ("/blogs/dnfbp-registration-lahore-punjab", "Lahore and Punjab"), ("/blogs/dnfbp-registration-karachi-sindh", "Karachi and Sindh"),
    ("/blogs/dnfbp-registration-islamabad-rawalpindi", "Islamabad and Rawalpindi"), ("/blogs/dnfbp-registration-peshawar-kp", "Peshawar and KP"),
    ("/blogs/dnfbp-registration-quetta-balochistan", "Quetta and Balochistan"),
]


def card(icon, col, h, p):
    return f'<div class="svc-card"><div class="svc-icon svc-icon-{col}"><i class="fas {icon}"></i></div><h3>{h}</h3><p>{p}</p></div>'


def main():
    t = open(f"{ROOT}/aop-tax-return.html", encoding="utf-8").read()
    t = re.sub(r"<title>.*?</title>", f"<title>{E(TITLE)}</title>", t, count=1)
    t = re.sub(r'<meta name="description" content="[^"]*"/>', f'<meta name="description" content="{E(DESC)}"/>', t, count=1)
    t = re.sub(r'<link rel="canonical" href="[^"]*"/>', f'<link rel="canonical" href="{URL}"/>', t, count=1)
    for prop, val in (("og:title", TITLE), ("og:description", DESC), ("og:url", URL)):
        t = re.sub(rf'<meta property="{prop}" content="[^"]*"/>', f'<meta property="{prop}" content="{E(val)}"/>', t, count=1)
    for nm, val in (("twitter:title", TITLE), ("twitter:description", DESC)):
        t = re.sub(rf'<meta name="{nm}" content="[^"]*"/>', f'<meta name="{nm}" content="{E(val)}"/>', t, count=1)

    org = {"@type": "AccountingService", "@id": f"{BASE}/#organization", "name": "Kamboh Associates", "url": BASE, "telephone": "+92-328-4675162",
           "address": {"@type": "PostalAddress", "streetAddress": "Shop No 34, Rizwan Block Market, opposite Rizwan Park, Awan Town",
                       "addressLocality": "Lahore", "addressRegion": "Punjab", "postalCode": "54660", "addressCountry": "PK"}}
    svc = {"@context": "https://schema.org", "@type": "Service", "@id": f"{URL}#service", "name": "DNFBP Compliance Services",
           "serviceType": "DNFBP registration and AML/CFT compliance", "description": DESC, "url": URL, "provider": org,
           "areaServed": [{"@type": "City", "name": "Lahore"}, {"@type": "Country", "name": "Pakistan"}],
           "audience": {"@type": "BusinessAudience", "audienceType": "Real estate agents, builders and developers, dealers in precious metals and stones, accountants"},
           "hasOfferCatalog": {"@type": "OfferCatalog", "name": "DNFBP compliance services", "itemListElement": [
               {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in
               ("DNFBP registration on IRIS", "goAML registration with FMU", "Risk assessment and AML/CFT policy", "CDD forms and staff training note", "Inspection and letter replies")]}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
        {"@type": "ListItem", "position": 2, "name": "Services", "item": f"{BASE}/#services"},
        {"@type": "ListItem", "position": 3, "name": "DNFBP Compliance Services", "item": URL}]}
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in (svc, faq, bc))
    og = (f'<meta property="og:type" content="website"/>\n<meta property="og:title" content="{E(TITLE)}"/>\n'
          f'<meta property="og:description" content="{E(DESC)}"/>\n<meta property="og:url" content="{URL}"/>\n'
          f'<meta name="twitter:card" content="summary_large_image"/>\n<meta name="twitter:title" content="{E(TITLE)}"/>\n'
          f'<meta name="twitter:description" content="{E(DESC)}"/>\n')
    s = t.index('<script type="application/ld+json">'); e = t.index('<meta property="og:image"', s)
    t = t[:s] + lds + og + t[e:]

    guides = "".join(f'<li><a href="{h}" {L}>{E(x)}</a></li>' for h, x in GUIDES)
    cities = " &middot; ".join(f'<a href="{h}" {L}>{E(x)}</a>' for h, x in CITIES)
    faqh = "".join(f'<div class="faq-item"><div class="faq-q">{E(q)} <i class="fas fa-plus"></i></div><div class="faq-a">{E(a)}</div></div>' for q, a in FAQS)
    srcs = "; ".join(f'<a href="{u}" target="_blank" rel="noopener" {L}>{E(n)}</a>' for n, u in SOURCES)
    body = f'''<section class="page-hero">
  <div class="container">
    <div class="hero-badge"><i class="fas fa-shield-halved"></i> &nbsp; DNFBP &amp; AML/CFT Compliance</div>
    <h1>{E(H1)}</h1>
<div class="tldr-box" style="background:linear-gradient(135deg,rgba(20,184,166,.08),rgba(20,184,166,.04));border:1.5px solid rgba(20,184,166,.35);border-radius:12px;padding:16px 20px;margin:0 0 24px"><p style="margin:0;color:#0F172A"><strong>Short answer:</strong> Real estate agents, builders and developers dealing in property, dealers in precious metals and stones taking cash of Rs 2 million or more in a transaction, and accountants not regulated by ICAP or ICMAP must register with FBR as DNFBPs and run an AML/CFT programme. We register you on IRIS and goAML, write your risk assessment and policy, set up customer due diligence, and support you in FBR inspections, from our Awan Town office in Lahore and online across Pakistan.</p></div>
    <p>Registering is the easy part. FBR inspections test whether the policy, the customer files and goAML access actually exist. We set up all of it, sized to your business.</p>
    <div class="hero-btns">
      <a href="{WA}" class="btn-wa" target="_blank" rel="noopener"><i class="fab fa-whatsapp"></i> WhatsApp Us</a>
      <a href="tel:+923284675162" class="btn-outline"><i class="fas fa-phone"></i> Call 0328-4675162</a>
    </div>
  </div>
</section>
<div class="stats-bar"><div class="container"><div class="stats-row">
  <div class="stat-item"><div class="stat-num">FBR</div><div class="stat-lbl">Registered</div></div>
  <div class="stat-item"><div class="stat-num">Mon&ndash;Sat</div><div class="stat-lbl">Office Hours</div></div>
  <div class="stat-item"><div class="stat-num">IRIS + goAML</div><div class="stat-lbl">Both Portals</div></div>
  <div class="stat-item"><div class="stat-num">2008</div><div class="stat-lbl">Est. Since</div></div>
</div></div></div>
<section class="section">
  <div class="container">
    <div class="section-label">Who We Serve</div>
    <h2 id="who-must-comply" class="section-title">Which Businesses Must Comply</h2>
    <p class="section-sub">FBR supervises three groups of Designated Non-Financial Businesses and Professions under the Anti-Money Laundering Act, 2010 and FBR's AML/CFT Regulations.</p>
    <div class="services-grid">
      {card("fa-house", "teal", "Real Estate Agents, Builders and Developers", 'Agents, and builders or developers when they deal in property for clients. See our <a href="/blogs/real-estate-agent-dnfbp-registration-aml-pakistan" ' + L + '>real estate guide</a>.')}
      {card("fa-gem", "gold", "Jewellers and Dealers in Precious Metals and Stones", 'Dealers who take cash of Rs 2 million or more in a transaction. See our <a href="/blogs/jeweller-dnfbp-registration-aml-pakistan" ' + L + '>jewellers guide</a>.')}
      {card("fa-calculator", "navy", "Accountants", 'Accountants not regulated by ICAP or ICMAP, when they carry out the listed activities. See our <a href="/blogs/accountant-dnfbp-registration-aml-pakistan" ' + L + '>accountants guide</a>.')}
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">What We Do</div>
    <h2 id="whats-included" class="section-title">What Our DNFBP Service Includes</h2>
    <div class="services-grid">
      {card("fa-magnifying-glass", "teal", "Category Check", "Confirmation of whether, and in which category, your business is a DNFBP before anything is filed.")}
      {card("fa-id-card", "gold", "FBR Registration on IRIS", "DNFBP registration with owners, beneficial owners and the compliance officer declared.")}
      {card("fa-network-wired", "navy", "goAML Registration", "Registration on the FMU's goAML portal, including the authority letter, so reports can be filed on time.")}
      {card("fa-file-shield", "teal", "Risk Assessment and Policy", "A written risk assessment and AML/CFT policy that matches how your business actually works.")}
      {card("fa-user-check", "gold", "CDD Forms and Training Note", "Customer due diligence forms your staff can use, and a short training note on red flags and screening.")}
      {card("fa-envelope-open-text", "navy", "Letters and Inspections", "Replies to DNFBP letters and support during FBR inspection requests.")}
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-label">How It Works</div>
    <h2 id="how-it-works" class="section-title">How DNFBP Compliance Works With Us</h2>
    <div class="steps-grid">
      <div class="step-card"><div class="step-num">1</div><h3>Tell Us About Your Business</h3><p>On WhatsApp or at our office: what you sell or do, how customers pay, your NTN and the owners. We confirm your category and quote a fixed fee before work starts.</p></div>
      <div class="step-card"><div class="step-num">2</div><h3>Registration on IRIS and goAML</h3><p>We prepare and submit the DNFBP registration with FBR, then register you on goAML with the FMU.</p></div>
      <div class="step-card"><div class="step-num">3</div><h3>Your Compliance File</h3><p>You receive the risk assessment, AML/CFT policy, CDD forms and training note, ready for an FBR inspection.</p></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">Fee and Risks</div>
    <h2 id="fee-and-risks" class="section-title">Fee, and the Cost of Getting It Wrong</h2>
    <p class="section-sub"><strong>Fee:</strong> a fixed fee, confirmed on WhatsApp before any work starts, based on your category and size. Related published fees, such as NTN registration (Rs 2,000), are on our <a href="/pricing" {L}>pricing page</a>.</p>
    <ul style="max-width:820px;margin:24px auto 0;padding-left:20px;line-height:1.8;color:var(--text-2)">
      <li>The AML/CFT Sanctions Rules 2020 allow penalties of up to Rs 100 million per violation.</li>
      <li>Significant sanctions are published with the business name.</li>
      <li>A business without goAML access cannot file a required report on time.</li>
    </ul>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:860px">
    <div class="section-label">Guides</div>
    <h2 id="guides" class="section-title">Read the Rules First</h2>
    <ul style="margin:24px 0 0;padding-left:20px;line-height:1.9">{guides}</ul>
    <p style="margin-top:16px"><strong>Your city:</strong> {cities}.</p>
    <p style="margin-top:16px;font-size:.88rem;color:var(--text-3)">Sources: {srcs}. Facts checked 9 November 2026. Serving Lahore from our Awan Town office, and businesses across Pakistan online.</p>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">FAQ</div>
    <h2 id="common-questions" class="section-title">Common Questions</h2>
    <div class="faq-list">{faqh}</div>
  </div>
</section>
<section class="cta-strip">
  <div class="container">
    <h2 id="get-dnfbp-compliant">Get DNFBP-Compliant With Kamboh Associates</h2>
    <p>Registration, goAML and a compliance file that holds up in an FBR inspection. Replies within office hours.</p>
    <div class="cta-btns">
      <a href="{WA}" class="btn-white" target="_blank" rel="noopener"><i class="fab fa-whatsapp"></i> WhatsApp Now</a>
      <a href="tel:+923284675162" class="btn-ghost-white"><i class="fas fa-phone"></i> 0328-4675162</a>
    </div>
  </div>
</section>
'''
    s = t.index('<section class="page-hero">'); e = t.index('</section>', t.index('<section class="cta-strip">')) + len('</section>\n')
    t = t[:s] + body + t[e:]
    open(f"{ROOT}/{SLUG}.html", "w", encoding="utf-8").write(t)
    sm = open(f"{ROOT}/sitemap.xml", encoding="utf-8").read()
    if f"<loc>{URL}</loc>" not in sm:
        sm = sm.replace("</urlset>", f"  <url>\n    <loc>{URL}</loc>\n    <lastmod>2026-11-20</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.9</priority>\n  </url>\n</urlset>", 1)
        open(f"{ROOT}/sitemap.xml", "w", encoding="utf-8").write(sm)
    print(SLUG, len(TITLE), len(DESC))


if __name__ == "__main__":
    main()
