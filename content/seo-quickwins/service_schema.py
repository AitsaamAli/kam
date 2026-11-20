"""Service landing pages carried BlogPosting/Article schema. Retype those nodes as WebPage (keeps author, dates, publisher),
drop the self-referencing mainEntityOfPage and point mainEntity at the page's Service node (Nov 2026). Guides keep BlogPosting."""
import json, re
BASE = "https://kambohassociates.com"
PAGES = ["income-tax-filing", "ntn-registration", "wealth-statement", "sales-tax-return", "sales-tax-registration", "import-export-registration",
         "fbr-notice-defense", "company-registration-consultant-lahore", "corporate-tax-consultant-lahore", "eobi-registration", "corporate-tax-return",
         "withholding-tax", "ntn-registration-gulberg-lahore", "fbr-consultant-near-me-lahore", "sales-tax-consultant-lahore",
         "income-tax-consultant-dha-lahore", "gst-registration-lahore", "tax-filing-bahria-town-lahore", "income-tax-return-filing-lahore",
         "wealth-statement-consultant-lahore", "aop-tax-return", "tax-exemption-certificate", "business-advisory", "ntn-registration-lahore",
         "atl-registration-lahore", "pricing"]
total = 0
for slug in PAGES:
    f = f"{slug}.html"; t = open(f, encoding="utf-8").read(); url = f"{BASE}/{slug}"; n = 0
    def fix(m):
        global total
        nonlocal_n = []
        try:
            d = json.loads(m.group(1))
        except Exception:
            return m.group(0)
        items = d if isinstance(d, list) else [d]
        changed = False
        for o in items:
            if isinstance(o, dict) and o.get("@type") in ("BlogPosting", "Article"):
                o["@type"] = "WebPage"; o["@id"] = url; o["url"] = url
                o.pop("mainEntityOfPage", None); o.pop("articleSection", None); o.pop("wordCount", None)
                changed = True; total += 1
        return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + '</script>' if changed else m.group(0)
    t2 = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix, t, flags=re.S)
    if t2 != t:
        open(f, "w", encoding="utf-8").write(t2)
print("nodes retyped", total)
