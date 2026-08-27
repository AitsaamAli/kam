# Kamboh Associates — Business Overview

## Who they are
- **Name:** Kamboh Associates
- **Business:** Tax consultancy / regulatory compliance firm, Pakistan
- **Founded:** 2008
- **Based in:** Lahore (serves clients remotely nationwide — "no office visit needed")
- **Credentials:** FBR Certified, SECP Registered, ISO 9001:2015
- **Author/owner byline used across the site:** Aitsaam Ali
- **Contact:** WhatsApp `0328-4675162` (used in every CTA button sitewide, format `https://wa.me/923284675162?text=...`), email `info@kambohassociates.com`

## Core services (what they actually sell — keep all content grounded in these)
- Income tax return filing (individual & business)
- NTN registration
- Sales tax / STRN registration
- SECP company registration (Pvt Ltd, SMC, AOP/Partnership)
- Corporate tax return filing
- Wealth statement preparation
- FBR notice response / audit defense
- EOBI registration
- Withholding tax (WHT) compliance
- Import/export registration (WeBOC/TDAP)
- Tax exemption certificates (Section 159)
- Section 8 tax clearance certificates (for people leaving Pakistan)
- Overseas Pakistani / non-resident tax compliance (NTN, non-resident returns, property tax while abroad)
- Visa-related FBR documentation (NTN, tax returns, wealth statement) for UK/Australia/Canada/Germany/etc. visa applicants

## Real, current trust stats (live on homepage as of 2026-08-27 — verify via `grep` before reusing if this doc is old)
- **5,000+** satisfied clients
- **312+** verified client reviews, **4.9/5** rating (`ratingValue: "4.9"` in AggregateRating schema)
- These numbers were normalized sitewide in commit `cbef6f9c` ("fix: normalize inconsistent review/client-count numbers sitewide") after an earlier conflict (180 vs 300 reviews shown on different pages) — if you ever see a page showing a different number, that's a regression, not a new source of truth. Always check `index.html`'s live numbers as the canonical source.

## Real fee schedule (safe to reuse — never invent a price not on this list)
See `09-verified-facts-and-figures.md` for the full, current list. Headline figures used repeatedly across blog CTAs:
- NTN registration: Rs. 2,000
- Individual pending tax return (per year): Rs. 3,500–5,000
- Wealth statement: Rs. 2,500
- STRN / sales tax registration: Rs. 3,000
- SECP Pvt Ltd company registration: Rs. 15,000 (indicative)
- Corporate tax return: Rs. 15,000
- FBR notice response: Rs. 5,000
- Section 8 tax clearance certificate: Rs. 5,000

## Brand voice / tone used across all content
- Written primarily in **Roman Urdu mixed with English technical terms** (the site's actual audience-facing voice) — see any recently-written blog in `blogs/` for the exact register.
- Direct, practical, consultant-to-client tone — not academic. Explains *why* a rule matters practically, not just what the rule is.
- Every blog ends with a WhatsApp CTA box driving to a real service, and a "Related" sidebar linking to genuinely related pages (not filler links).

## Design system in one line
Navy (`#0F172A`) + gold (`#D4AF37`/`#E4C158`/`#B8860C`) + teal (`#14B8A6`/`#0D9488`) — "bold gold-foil" premium look, applied sitewide as of August 2026. Full detail in `03-design-system-and-branding.md`.
