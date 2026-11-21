"""Builds /pra-registration (service landing page) from the aop-tax-return.html shell, like content/dnfbp-service/build.py.
Facts from the PRA texts listed in content/pra-2026/pra_common.py (checked 21 November 2026). Fee Rs 5,000 as on /pricing."""
import html, json, re, sys
sys.path.insert(0, "/home/user/kam/content/pra-2026")
from pra_common import S_ACT4, S_RULES, S_MAN, S_LOGIN, S_ATL, B

ROOT = "/home/user/kam"
BASE = "https://kambohassociates.com"
SLUG = "pra-registration"
URL = f"{BASE}/{SLUG}"
E = html.escape
TITLE = "PRA Registration in Punjab, Done for You | Rs 5,000"
DESC = "PRA registration done for you on PRA IRIS: documents checked, Form PST-01 filed, certificate followed up. PRA charges nothing; our fee is Rs 5,000."
H1 = "PRA Registration Service in Punjab: Filed on PRA IRIS for a Fixed Rs 5,000"
WA = "https://wa.me/923284675162?text=" + "Assalam%20o%20Alaikum%2C%20PRA%20registration%20karwani%20hai."
L = 'style="color:#0D9488;font-weight:600"'

FAQS = [
    ("Who must register with PRA?", "Section 25(1) of the Punjab Sales Tax on Services Act 2012: anyone who provides a taxable service from an office or place of business in Punjab, or is otherwise required by the Act, rules or a PRA notification. Others may register voluntarily under section 26."),
    ("Does PRA charge a registration fee?", "No. Rule 15 of the Punjab Sales Tax on Services (Registration and De-registration) Rules 2012 makes registration and de-registration free of any fee or service charge."),
    ("How much do you charge for PRA registration?", "Rs 5,000 fixed, as published on our pricing page. If you need an FBR NTN first, that is Rs 2,000 more."),
    ("What documents are needed?", "CNIC, FBR NTN, the address of each business place with how it is held (and the landlord's CNIC or NTN if rented), its electricity reference number, each business bank account, and the services you provide (Form PST-01)."),
    ("How long does PRA registration take?", "Rule 3 gives a provisional certificate immediately on applying and the final Form PST-03 certificate after verification, preferably within thirty days."),
    ("I am already registered with FBR. Do I need this?", "Rule 10 registered existing FBR taxpayers with PRA automatically, with P+NTN. We check the Taxpayer Profile Inquiry first and apply only if you are not found."),
    ("I received a PRA notice. Can you help?", "Yes. Section 27 requires advance notice and a hearing before compulsory registration. We read the notice, advise whether registration applies, and file on the notice route or prepare your reply."),
]
SOURCES = [S_ACT4, S_RULES, S_MAN, S_LOGIN, S_ATL]

GUIDES = [
    (B["proc"], "PRA registration process on IRIS, step by step"),
    (B["docs"], "PRA registration documents: the Form PST-01 checklist"),
    (B["fee"], "PRA registration fee: free under rule 15"),
    (B["who"], "Who must register with PRA (section 25)"),
    (B["sole"], "PRA registration for sole proprietors"),
    (B["cert"], "PRA registration certificate (PST-03)"),
    (B["ver"], "PRA NTN verification and profile inquiry"),
    (B["fbr"], "Already on FBR? P+NTN and rule 10"),
    (B["comp"], "PRA compulsory registration notice and e-Enrolment"),
    (B["chg"], "Changes, suspension and de-registration"),
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
    svc = {"@context": "https://schema.org", "@type": "Service", "@id": f"{URL}#service", "name": "PRA Registration Service",
           "serviceType": "Punjab Revenue Authority sales tax on services registration", "description": DESC, "url": URL, "provider": org,
           "areaServed": [{"@type": "City", "name": "Lahore"}, {"@type": "State", "name": "Punjab"}], "offers": {"@type": "Offer", "price": "5000", "priceCurrency": "PKR", "url": "https://kambohassociates.com/pricing"},
           "audience": {"@type": "BusinessAudience", "audienceType": "Service providers in Punjab: sole proprietors, firms and companies"},
           "hasOfferCatalog": {"@type": "OfferCatalog", "name": "PRA registration services", "itemListElement": [
               {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in
               ("PRA registration on PRA IRIS", "FBR NTN registration", "Change of PRA registration particulars", "Reply to a PRA compulsory registration notice", "PRA de-registration")]}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
        {"@type": "ListItem", "position": 2, "name": "Services", "item": f"{BASE}/#services"},
        {"@type": "ListItem", "position": 3, "name": "PRA Registration Service", "item": URL}]}
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in (svc, faq, bc))
    og = (f'<meta property="og:type" content="website"/>\n<meta property="og:title" content="{E(TITLE)}"/>\n'
          f'<meta property="og:description" content="{E(DESC)}"/>\n<meta property="og:url" content="{URL}"/>\n'
          f'<meta name="twitter:card" content="summary_large_image"/>\n<meta name="twitter:title" content="{E(TITLE)}"/>\n'
          f'<meta name="twitter:description" content="{E(DESC)}"/>\n')
    s = t.index('<script type="application/ld+json">'); e = t.index('<meta property="og:image"', s)
    t = t[:s] + lds + og + t[e:]

    guides = "".join(f'<li><a href="{h}" {L}>{E(x)}</a></li>' for h, x in GUIDES)
    faqh = "".join(f'<div class="faq-item"><div class="faq-q">{E(q)} <i class="fas fa-plus"></i></div><div class="faq-a">{E(a)}</div></div>' for q, a in FAQS)
    srcs = "; ".join(f'<a href="{u}" target="_blank" rel="noopener" {L}>{E(n)}</a>' for n, u in SOURCES)
    body = f'''<section class="page-hero">
  <div class="container">
    <div class="hero-badge"><i class="fas fa-landmark"></i> &nbsp; Punjab Revenue Authority Registration</div>
    <h1>{E(H1)}</h1>
<div class="tldr-box" style="background:linear-gradient(135deg,rgba(20,184,166,.08),rgba(20,184,166,.04));border:1.5px solid rgba(20,184,166,.35);border-radius:12px;padding:16px 20px;margin:0 0 24px"><p style="margin:0;color:#0F172A"><strong>Short answer:</strong> If you provide a taxable service from an office or place of business in Punjab, section 25 of the Punjab Sales Tax on Services Act 2012 requires PRA registration. PRA charges nothing (rule 15). We prepare and file it on PRA IRIS for a fixed Rs 5,000 and follow up to the certificate.</p></div>
    <p>Send your CNIC and one line about your service on WhatsApp. We check your FBR record, prepare Form PST-01, file on PRA IRIS and send you the certificate.</p>
    <div class="hero-btns">
      <a href="{WA}" class="btn-wa" target="_blank" rel="noopener"><i class="fab fa-whatsapp"></i> WhatsApp Us</a>
      <a href="tel:+923284675162" class="btn-outline"><i class="fas fa-phone"></i> Call 0328-4675162</a>
    </div>
  </div>
</section>
<div class="stats-bar"><div class="container"><div class="stats-row">
  <div class="stat-item"><div class="stat-num">Rs 5,000</div><div class="stat-lbl">Fixed Fee</div></div>
  <div class="stat-item"><div class="stat-num">Rs 0</div><div class="stat-lbl">PRA Charge (Rule 15)</div></div>
  <div class="stat-item"><div class="stat-num">FBR</div><div class="stat-lbl">Registered</div></div>
  <div class="stat-item"><div class="stat-num">2008</div><div class="stat-lbl">Est. Since</div></div>
</div></div></div>
<section class="section">
  <div class="container">
    <div class="section-label">Who Needs It</div>
    <h2 id="who-needs-pra" class="section-title">Who Needs PRA Registration</h2>
    <p class="section-sub">Section 25(1): anyone who provides a taxable service from an office or place of business in Punjab, or is otherwise required by the Act, the rules or a PRA notification. Section 26 allows voluntary registration.</p>
    <div class="services-grid">
      {card("fa-user", "teal", "Sole Proprietors", 'One-person service businesses register as individuals, under the owner&rsquo;s CNIC and NTN, with the trade name on each business place. See <a href="' + B["sole"] + '" ' + L + '>PRA for sole proprietors</a>.')}
      {card("fa-building", "gold", "Firms and Companies", 'AOPs and companies register with their registration or incorporation number and their partners or directors. Several centrally billed branches can share one registration (rule 2(2)).')}
      {card("fa-map-location-dot", "navy", "Businesses From Other Provinces", 'Services rendered in Punjab need a separate Punjab registration, even if you are registered in another province (rule 2(4)).')}
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">What We Do</div>
    <h2 id="whats-included" class="section-title">What Our PRA Registration Service Includes</h2>
    <div class="services-grid">
      {card("fa-magnifying-glass", "teal", "Status Check", "We search PRA&rsquo;s Taxpayer Profile Inquiry first: rule 10 may have registered you already with P+NTN.")}
      {card("fa-id-card", "gold", "FBR Record Check", "PRA IRIS copies your basic details from FBR and locks them, so we correct FBR first. New NTN: Rs 2,000.")}
      {card("fa-file-lines", "navy", "Form PST-01 Prepared", "Principal service, other activities, every business place with its electricity reference, and every business bank account.")}
      {card("fa-laptop", "teal", "Filed on PRA IRIS", "Submitted online with you confirming the codes sent to your mobile and email. Provisional certificate on filing (rule 3(1)).")}
      {card("fa-certificate", "gold", "Follow-Up to PST-03", "We answer verification queries until the Form PST-03 certificate is issued (rule 3(2)).")}
      {card("fa-envelope-open-text", "navy", "Notices and Changes", "Compulsory registration notices (section 27), changes of particulars (rule 11) and de-registration (rule 5), at a fixed fee confirmed first.")}
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-label">How It Works</div>
    <h2 id="how-it-works" class="section-title">How PRA Registration Works With Us</h2>
    <div class="steps-grid">
      <div class="step-card"><div class="step-num">1</div><h3>WhatsApp Your Details</h3><p>CNIC, NTN (if any), one line about your service, your business address, a recent electricity bill, rent agreement or ownership papers, and a bank account certificate.</p></div>
      <div class="step-card"><div class="step-num">2</div><h3>We Prepare and File</h3><p>We check FBR, prepare Form PST-01 and file on PRA IRIS. You confirm the codes on your phone and receive the provisional certificate.</p></div>
      <div class="step-card"><div class="step-num">3</div><h3>Certificate Issued</h3><p>We follow up through verification until PRA issues your Form PST-03 certificate, and tell you to show the number on your invoices (rule 2(5)).</p></div>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-label">Fee and Risks</div>
    <h2 id="fee-and-risks" class="section-title">Fee, and the Cost of Getting It Wrong</h2>
    <p class="section-sub"><strong>Fee:</strong> Rs 5,000 fixed for PRA registration; Rs 2,000 more only if you need an FBR NTN. PRA itself charges nothing (rule 15). Both fees are on our <a href="/pricing" {L}>pricing page</a>.</p>
    <ul style="max-width:820px;margin:24px auto 0;padding-left:20px;line-height:1.8;color:var(--text-2)">
      <li>A person required to register who does not apply can be registered compulsorily by PRA after notice and a hearing (section 27).</li>
      <li>A wrong principal service or missing branch means a change application later (rule 11).</li>
      <li>Invoices issued while a registration is suspended give your customers no tax credit (rule 8).</li>
      <li>Collecting PRA tax that was not payable must be paid to the Government (section 17).</li>
    </ul>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:860px">
    <div class="section-label">Guides</div>
    <h2 id="guides" class="section-title">PRA Registration Guides</h2>
    <ul style="margin:24px 0 0;padding-left:20px;line-height:1.9">{guides}</ul>
    <p style="margin-top:16px;font-size:.88rem;color:var(--text-3)">Sources: {srcs}. Facts checked 21 November 2026. Serving Lahore from our Awan Town office, and businesses across Punjab online.</p>
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
    <h2 id="get-pra-registered">Get PRA-Registered With Kamboh Associates</h2>
    <p>Rs 5,000 fixed. PRA charges nothing. Replies within office hours.</p>
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
        sm = sm.replace("</urlset>", f"  <url>\n    <loc>{URL}</loc>\n    <lastmod>2026-11-21</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.9</priority>\n  </url>\n</urlset>", 1)
        open(f"{ROOT}/sitemap.xml", "w", encoding="utf-8").write(sm)
    print(SLUG, len(TITLE), len(DESC))


if __name__ == "__main__":
    main()
