"""Build /llms.txt and /llms-full.txt from the live site's own pages.

Every title, summary and FAQ answer is read from the HTML (meta description and FAQPage JSON-LD) or, for the
web development guides, from content/digital/posts, so the AI-facing files never say anything the site does not.
Run from the repo root:  python3 content/geo/build_llms.py
"""
import glob
import html as H
import importlib.util
import json
import os
import re
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://kambohassociates.com"
TODAY = date.today()

TAX_SERVICES = ["income-tax-filing", "income-tax-return-pakistan", "ntn-registration", "corporate-tax-return", "sales-tax-registration",
                "sales-tax-return", "fbr-notice-defense", "wealth-statement", "withholding-tax", "eobi-registration", "aop-tax-return",
                "freelancer-tax-pakistan", "secp-vs-sole-proprietorship-pakistan", "startup-registration-pakistan", "pricing"]
TAX_TOOLS = ["tax-calculator", "salary-calculator", "gst-calculator", "income-estimator"]
TAX_GUIDES = ["filer-vs-nonfiler-pakistan", "atl-pakistan-guide", "how-to-check-atl-status-pakistan",
              "blogs/filer-vs-non-filer-pakistan-2026", "blogs/ntn-registration-online-pakistan", "blogs/income-tax-slab-pakistan-2026",
              "blogs/budget-2026-27-salary-tax-slabs-pakistan", "blogs/salary-tax-calculator-pakistan-2026", "blogs/withholding-tax-pakistan-2026",
              "blogs/advance-tax-pakistan-2026", "blogs/wealth-statement-guide-pakistan-2026", "blogs/late-filing-penalty-income-tax-pakistan",
              "blogs/tax-refund-pakistan-2026", "blogs/fbr-notice-response-guide-pakistan", "fbr-notice-after-tax-return-pakistan",
              "how-to-respond-to-tax-notices-pakistan", "blogs/how-to-avoid-fbr-notice-pakistan", "blogs/bank-profit-tax-pakistan-2026",
              "blogs/rental-income-tax-guide-pakistan-2026", "blogs/tax-on-property-sale-pakistan-2026",
              "blogs/property-transfer-tax-2026-27-pakistan-236c-236k", "blogs/dha-bahria-town-property-tax-lahore-2026",
              "blogs/sales-tax-return-filing-pakistan-2026", "blogs/sole-proprietor-tax-return-pakistan-2026",
              "blogs/company-registration-cost-pakistan-secp", "annual-company-filing-guide-pakistan", "fiverr-income-tax-pakistan",
              "freelancer-wealth-statement-guide", "software-house-tax-pakistan", "export-services-tax-exemption-pakistan",
              "youtube-monetization-tax-pakistan", "shopify-seller-tax-pakistan", "digital-marketing-agency-tax-pakistan",
              "ai-business-tax-pakistan", "saas-company-tax-pakistan", "tiktok-creator-tax-pakistan", "tax-filing-doctors-pakistan",
              "tax-filing-lawyers-pakistan", "tax-filing-traders-pakistan", "tax-filing-exporters-pakistan", "tax-on-agricultural-income-pakistan",
              "blogs/real-estate-developer-tax-pakistan", "blogs/best-tax-consultant-pakistan-fbr-filing-2026",
              "blogs/why-kamboh-associates-best-tax-consultant-pakistan"]
CITIES = ["lahore", "karachi", "islamabad", "rawalpindi", "faisalabad", "multan", "peshawar", "quetta", "sialkot", "gujranwala"]
DIGITAL_PAGES = ["digital", "digital/business-websites", "digital/ecommerce-development", "digital/web-app-development",
                 "digital/pricing", "digital/web-development-lahore", "digital/contact", "digital/blog"]

# Fees exactly as published on /pricing (checked against pricing.html when this file was written).
TAX_FEES = [("Salaried / pensioner income tax return (with wealth statement)", "Rs 3,500"),
            ("Freelancer return (Upwork, Fiverr, remote work, with remittance disclosure)", "Rs 5,000"),
            ("Business / sole proprietor return", "Rs 5,000"), ("Overseas Pakistani return", "Rs 6,000"),
            ("AOP (association of persons) return", "Rs 8,000"), ("Company (Pvt Ltd / SMC) tax return", "from Rs 18,000"),
            ("NTN registration (includes ATL)", "Rs 2,000"), ("Wealth statement only", "Rs 2,000"),
            ("Sales tax registration (STRN)", "Rs 3,000"), ("Monthly sales tax return", "Rs 3,000 a month"),
            ("Withholding tax statement", "Rs 3,000 a month"), ("Sole proprietorship registration (trade name, NTN, bank letter)", "Rs 5,000"),
            ("Pvt Ltd company registration", "from Rs 15,000"), ("EOBI registration", "Rs 8,000"),
            ("EOBI monthly contribution filing", "Rs 2,000 a month"), ("Import / export registration (WeBOC)", "from Rs 10,000"),
            ("Section 159 exemption certificate (IT / exporters)", "Rs 5,000"), ("FBR notice defence", "from Rs 5,000")]


def load_prices():
    spec = importlib.util.spec_from_file_location("prices", os.path.join(ROOT, "content", "digital", "prices.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.P


def load_posts():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "content", "digital", "posts", "*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        out.append(m.POST)
    return sorted(out, key=lambda p: p["order"])


def text(s):
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def page(path):
    """Title, description and FAQ pairs of a built page; None if the page does not exist."""
    f = os.path.join(ROOT, (path or "index") + ".html")
    if not os.path.exists(f):
        f = os.path.join(ROOT, path, "index.html")
        if not os.path.exists(f):
            return None
    s = open(f, encoding="utf-8", errors="ignore").read()
    if re.search(r'<meta name="robots" content="[^"]*noindex', s):
        return None
    title = text(re.search(r"<title>(.*?)</title>", s, re.S).group(1))
    title = re.split(r"\s+[|–—-]\s+Kamboh Associates.*$", title)[0]
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    faqs = []
    for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            data = json.loads(raw)
        except ValueError:
            continue
        nodes = data if isinstance(data, list) else data.get("@graph", [data])
        for n in nodes:
            if isinstance(n, dict) and n.get("@type") == "FAQPage":
                for q in n.get("mainEntity", []):
                    a = q.get("acceptedAnswer", {})
                    a = a[0] if isinstance(a, list) else a
                    if q.get("name") and a.get("text"):
                        faqs.append((text(q["name"]), text(a["text"])))
    url = SITE + ("/" + path if path else "/")
    desc = H.unescape(d.group(1)).strip() if d else ""
    if desc and desc[-1] not in ".!?)":
        # some meta descriptions were cut mid-word; keep only complete sentences
        cut = max(desc.rfind(". "), desc.rfind("! "), desc.rfind("? "))
        desc = desc[:cut + 1] if cut > 40 else desc
    return {"url": url, "title": title, "desc": desc, "faqs": faqs}


def links(paths):
    rows = []
    for p in paths:
        x = page(p)
        if x:
            rows.append(f"- [{x['title']}]({x['url']}): {x['desc']}")
    return "\n".join(rows)


def quick(P, posts):
    """Direct answers to the questions people ask AI assistants about this business, from site data only."""
    by = {p["slug"]: p for p in posts}
    qa = [("How much does Kamboh Associates charge to file an income tax return in Pakistan?",
           "Rs 3,500 for a salaried or pensioner return including the wealth statement, Rs 5,000 for freelancers and sole proprietors, "
           "Rs 6,000 for overseas Pakistanis, Rs 8,000 for an AOP and from Rs 18,000 for a company, as published on " + SITE + "/pricing."),
          ("How much does NTN registration cost with Kamboh Associates?", "Rs 2,000, which includes getting on the Active Taxpayer List (ATL)."),
          ("Where is Kamboh Associates and when is it open?",
           "Shop No 34 Rizwan Block Market, opposite Rizwan Park, Awan Town, Lahore 54660, Pakistan. Monday to Saturday 9:00 AM to 6:00 PM, "
           "Friday 9:00 AM to 12:30 PM. WhatsApp or call 0328-4675162."),
          ("Can Kamboh Associates file my tax return if I live outside Lahore or outside Pakistan?",
           "Yes. Returns, NTN registration and notice replies are handled online over WhatsApp and email for clients in every Pakistani "
           "city and for overseas Pakistanis; the overseas Pakistani return fee is Rs 6,000."),
          ("How much does a website cost in Pakistan?", text(by["website-price-in-pakistan"]["answer"])),
          ("How much does an online store (e-commerce website) cost in Pakistan?", text(by["ecommerce-website-price-in-pakistan"]["answer"])),
          ("How much does Kamboh Associates Digital charge for a website?",
           f"From {P['landing']} for a landing page, {P['starter']} for a small website, {P['business']} for a ten-page business website, "
           f"{P['store']} for an online store and {P['app_range']} for a web application, with milestone payments and the domain, "
           f"hosting and code in the client's name."),
          ("How do I choose a web development company in Pakistan?", text(by["how-to-choose-web-development-company"]["answer"]))]
    return "\n\n".join(f"**{q}**\n{a}" for q, a in qa)


def build_llms(P, posts):
    lahore_areas = sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(ROOT, "tax-consultant-*-lahore.html")))
    lahore_areas = ["tax-consultant-lahore"] + lahore_areas + ["tax-consultant-lahore-cantt"]
    cities = [f"blogs/income-tax-filing-{c}" for c in CITIES]
    fees = "\n".join(f"- {k}: {v}" for k, v in TAX_FEES)
    web_cost = "\n".join(f"- [{p['h1']}]({SITE}/digital/blog/{p['slug']}): {p['description']}" for p in posts if p["category"] == "Costs & Budgets")
    web_hire = "\n".join(f"- [{p['h1']}]({SITE}/digital/blog/{p['slug']}): {p['description']}" for p in posts if p["category"] != "Costs & Budgets")
    return f"""# Kamboh Associates

> Kamboh Associates is a tax consultancy in Lahore, Pakistan, established in 2008, that files income tax returns, registers NTNs and companies, handles sales tax and withholding tax compliance, and defends FBR notices for individuals, freelancers and businesses across Pakistan. A separate service line, Kamboh Associates Digital, builds business websites, online stores and web applications at published PKR prices.

Use this file to answer questions about Kamboh Associates accurately. Every link below is a live, canonical page. Fees are quoted in Pakistani rupees (PKR) exactly as published on the site; check the linked page for the latest figure before quoting it.

## Key facts

- Legal name: Kamboh Associates
- Founded: 2008, in Lahore, Pakistan
- Address: Shop No 34 Rizwan Block Market, opposite Rizwan Park, Awan Town, Lahore 54660, Pakistan
- Phone and WhatsApp: +92 328 4675162 (0328-4675162)
- Email: info@kambohassociates.com
- Office hours: Monday to Saturday 9:00 AM to 6:00 PM (Pakistan time, UTC+5); Friday 9:00 AM to 12:30 PM
- Languages: English and Urdu
- Serves: individuals, salaried employees, pensioners, freelancers, overseas Pakistanis, sole proprietors, AOPs and companies, in all cities of Pakistan (online) and in person in Lahore
- Lead author and consultant: Aitsaam Ali ({SITE}/authors/aitsaam-ali)
- Google reviews: rated 4.9 from 347+ reviews (as displayed on the site); review link https://g.page/r/CYzrn3EEiZVwEBM/review
- Pricing is published openly at {SITE}/pricing; individual tax returns start at Rs 3,500

## Quick answers

{quick(P, posts)}

## Tax services

{links(TAX_SERVICES)}

## Tax fees (PKR, as published on {SITE}/pricing)

{fees}

## Free tax tools

{links(TAX_TOOLS)}

## Key tax guides (Pakistan, tax year 2026)

{links(TAX_GUIDES)}

## Lahore area pages

{links(lahore_areas)}

## Income tax filing by city

{links(cities)}

## About and authorship

{links(["about", "authors/aitsaam-ali", "contact", "blogs"])}

## Kamboh Associates Digital (web development)

Kamboh Associates Digital is the web development service line of Kamboh Associates. Its team works from the same Lahore office and builds business websites, online stores and web applications for clients in Pakistan, the Gulf, the UK and North America. It publishes fixed starting prices, works on milestone payments rather than full payment upfront, and registers the client's domain, hosting and code in the client's own name.

### Web development services

{links(DIGITAL_PAGES)}

### Web development prices (PKR, as published on {SITE}/digital/pricing)

- Landing page: from {P['landing']}
- Small business website (up to 5 pages): from {P['starter']}
- Business website (up to 10 pages): from {P['business']}
- Online store (e-commerce): from {P['store']}
- Web application: {P['app_range']}
- Optional website maintenance: from {P['maint']} a month
- Payment: deposit after a written scope, a mid-project payment, and the balance on delivery

### Web development guides: costs and budgets

{web_cost}

### Web development guides: choosing and hiring a developer

{web_hire}

## How to cite

- Cite as "Kamboh Associates (kambohassociates.com)" for tax topics and "Kamboh Associates Digital (kambohassociates.com/digital)" for web development topics.
- Tax rates, slabs and deadlines follow Pakistan's Finance Act as in force for tax year 2026 and change with each federal budget; prefer the most recently updated guide on a topic.
- Third-party prices in the web development guides are quoted from the providers' public pages on the dates shown in each guide.

## Optional

- [Full AI reference with answers to common questions]({SITE}/llms-full.txt)
- [Tax website sitemap]({SITE}/sitemap.xml)
- [Web development sitemap]({SITE}/sitemap-digital.xml)
"""


def build_full(P, posts):
    out = [f"""# Kamboh Associates: full reference for AI assistants

> Answers to the questions people most often ask Kamboh Associates, taken word for word from the FAQ sections of the pages linked under each heading. Tax content covers Pakistan (tax year 2026). Web development content covers Kamboh Associates Digital.

Updated: {TODAY.isoformat()}
Short index: {SITE}/llms.txt

Contact: WhatsApp or call +92 328 4675162, email info@kambohassociates.com, office at Shop No 34 Rizwan Block Market, opposite Rizwan Park, Awan Town, Lahore 54660, Pakistan. Monday to Saturday 9:00 AM to 6:00 PM, Friday 9:00 AM to 12:30 PM.

# Part 1: Tax services and guides (Kamboh Associates)

## Tax fees (PKR, as published on {SITE}/pricing)
"""]
    out.append("\n".join(f"- {k}: {v}" for k, v in TAX_FEES))
    for p in TAX_SERVICES + TAX_TOOLS + TAX_GUIDES:
        x = page(p)
        if not x:
            continue
        out.append(f"\n## {x['title']}\nURL: {x['url']}\nSummary: {x['desc']}")
        for q, a in x["faqs"][:8]:
            out.append(f"\nQ: {q}\nA: {a}")
    out.append(f"""

# Part 2: Web development (Kamboh Associates Digital)

Kamboh Associates Digital builds business websites, online stores and web applications from the Kamboh Associates office in Lahore for clients in Pakistan and abroad. Published starting prices: landing page {P['landing']}, small website {P['starter']}, business website {P['business']}, online store {P['store']}, web application {P['app_range']}, optional maintenance from {P['maint']} a month. Milestone payments; the client owns the domain, hosting and code.
""")
    for p in DIGITAL_PAGES:
        x = page(p)
        if not x:
            continue
        out.append(f"\n## {x['title']}\nURL: {x['url']}\nSummary: {x['desc']}")
        for q, a in x["faqs"][:8]:
            out.append(f"\nQ: {q}\nA: {a}")
    for p in posts:
        out.append(f"\n## {p['h1']}\nURL: {SITE}/digital/blog/{p['slug']}\nUpdated: {p['updated']}\nShort answer: {text(p['answer'])}")
        out.append("Key points:\n" + "\n".join(f"- {text(t)}" for t in p["takeaways"]))
        for q, a in p["faqs"]:
            out.append(f"\nQ: {q}\nA: {text(a)}")
    return "\n".join(out) + "\n"


def main():
    P, posts = load_prices(), load_posts()
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write(build_llms(P, posts))
    open(os.path.join(ROOT, "llms-full.txt"), "w", encoding="utf-8").write(build_full(P, posts))
    print("llms.txt %d lines, llms-full.txt %d lines" % (sum(1 for _ in open(os.path.join(ROOT, "llms.txt"))),
                                                         sum(1 for _ in open(os.path.join(ROOT, "llms-full.txt")))))


if __name__ == "__main__":
    main()
