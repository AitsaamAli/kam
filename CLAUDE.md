# Kamboh Associates site (kambohassociates.com)

Static HTML site on Vercel. Tax site at the root; a separate web-development section under `/digital`. `/*.md`, `/*.py` and `content/` are excluded from the deploy (`.vercelignore`).

## Standing rules (owner's decisions)
- Tax site and `/digital` stay separate: no cross-links, and no tax terms in `/digital` titles or H1s. Exception (owner's decision, Nov 2026): the "Web Development" link in the homepage top bar and nav stays.
- Do not change existing titles, meta descriptions, canonicals, robots tags, H1s or URLs unless the task asks for it.
- Aitsaam Ali is credited only as "Author". Never claim a tax-consultant licence, credential or role for him. Figures are "from FBR".
- Say "FBR Registered", never "FBR Certified". Replies are promised "within office hours" (Mon–Sat 9:00–18:00, Fri 9:00–12:30, Sun closed). Never claim 24/7.
- Never show a review count or star rating number anywhere (pages, schema, llms). Link to the Google Business Profile instead: https://g.page/r/CYzrn3EEiZVwEBM. Keep existing testimonial text. No fake reviews, no grey-hat or black-hat SEO.
- Every fact must come from an official source (FBR, IRIS, SECP, FMU, provincial authorities). Link the source and give the date it was checked. If a fact cannot be verified, leave it out.
- Report to the owner in Roman Urdu, briefly.
- Owner confirmed (Nov 2026): same-day work, 24-hour turnaround and "best tax consultant" wording on existing pages are accurate and stay; do not remove them. Still never claim 24/7.

## Blog standards (owner's decisions, Nov 2026)
- Length: topic blogs at least 1,600–1,700 words of real content (no padding); city/regional pages: no word minimum (owner, 22 Nov 2026) but 4-5 official local facts, a Short answer box and unique content, linked to the district/province hub. Longer is fine when the facts support it.
- City pages programme: 653 thin `tax-consultant-*` pages, 10 parts. Plan and rules: `content/city-expand/PLAN.md`; page lists: `content/city-expand/batches.json`. One part per session, 7 days apart; update the Progress table in PLAN.md after each part.
- Every blog is informational *and* commercial: a "done for you" box near the top and a service section (what we do, risks of DIY, how it works, fee) with a WhatsApp CTA. Use only fees published on /pricing; otherwise "fixed fee confirmed before work starts".
- Sales tax (owner's decision, Nov 2026): new blogs may promote sales tax **registration** (FBR STRN, PRA and other provincial registration) but not sales tax return filing for now. Main focus stays DNFBP and sole proprietorship clients.
- No doorway pages: city pages only where there are genuinely local facts (e.g. one per FBR DNFBP directorate), overlap with other pages under 15%.
- No duplicate or thin content: check every new blog against all site pages (not only the gate set) before publishing, and avoid topics an existing page already targets.
- Facts only from FBR's own texts (Income Tax Ordinance PDF amended to the latest date, SROs, FBR/FMU guidance), quoted to the section.

## Site-wide parts (Nov 2026)
- Meta descriptions: at most 160 characters (`content/seo-quickwins/meta_trim.py` trims longer ones at a clause boundary).
- Internal links: every tax page needs at least one contextual inbound link besides /blogs; `content/seo-quickwins/interlink.py` adds 'Related guides' links (max 4 per host), then `content/seo-quickwins/interlink2.py` places the rest by page text (city pages: towns named on the page, else same province; NEAR map for towns with no neighbour named). Sales-tax return pages are not linked.
- Bank profit: 20% on the ATL / 40% off it; other profit on debt (TFCs, most sukuk) 15% / 30%; sukuk from an SPV under s.5AA 10% / 12.5% / 25% (Division IIIA/IIIB, Tenth Schedule). 236C off-ATL 11.5%; 236K off-ATL 10.5% (to Rs 50m) / 14.5%.
- PRA registration fee Rs 5,000 (owner locked, Nov 2026; on /pricing). PRA itself charges no fee (Registration Rules 2012, rule 15).
- Fees in body text must match /pricing: `content/seo-quickwins/fees_fix.py` (rules for known wrong fees; unpublished fees become "fixed fee confirmed before work starts").
- One footer on every tax page (`ka-footer`, with NAP, hours and GBP link), set by `content/ui-2026/apply.py`. `content/seo-quickwins/footer_nap.py` is superseded.
- Service pages use WebPage + Service schema, not BlogPosting: `content/seo-quickwins/service_schema.py`.
- DNFBP service page: `content/dnfbp-service/build.py` -> `/dnfbp-compliance-services`.
- PRA registration: service page `content/pra-service/build.py` -> `/pra-registration`; 10 guides in `content/pra-2026/` (build: `PYTHONPATH=content/pra-2026 POSTS_MODULE=posts_pra python3 content/dnfbp-2026/build.py`). Facts only from PRA's Act Ch. III-IV, Registration Rules 2012 and the PRAL manual (owner uploaded; PRA sites block non-Pakistan IPs). No PRA tax rate, threshold or penalty amount is stated: not verified.
- Firm experience block ("From our practice", E-E-A-T) on every guide in blogs/: `content/ui-2026/experience.py` (idempotent; run after building new guides). One wording only: rotating wordings broke the overlap gate (198/680). Facts only from /about: Lahore since 2008, FBR Registered, Awan Town.
- Homepage stats are static text (no JS counters, no unverifiable % or turnaround claims).
- Design layer (owner approved Nov 2026): `content/ui-2026/apply.py` (idempotent) gives every tax page one menu, a slow top strip of client messages (pausable, no turnaround claims), the shared `/assets/ka-ui.css` + `/assets/ka-ui.js`, one Call/WhatsApp bar on phones, equal-size WhatsApp/Call button pairs, an "On this page" box on guides and the "Short answer" label. Run it after building new pages; bump `V` in it when the assets change. Turnaround claims already on pages stay (owner confirmed); never 24/7.

## Keyword research
- Do not use Semrush (no paid API units). Use the Search Console exports the owner provides, the site's sitemap, and free Google suggestions (`https://suggestqueries.google.com/complete/search?client=firefox&gl=pk&hl=en&q=...`).

## Tax facts in use (check before reuse)
- TY2026 return deadline: 31 Oct 2026.
- s.182 late filing (ITO amended to 30.06.2026, Finance Act 2026): higher of 0.1% of tax payable or Rs 1,000 per day; min Rs 10,000 (75%+ salary income) or Rs 50,000 (others); max 200% of tax payable; reduced 75%/50%/25% if filed within 1/2/3 months of the due date. "Tax payable" = higher of assessed tax or tax of the last year filed on time.
- s.182A ATL surcharge: Rs 25k individual / 50k AOP / 100k company.
- Property: 236C 2.75% (ATL) / 11.5% off; 236K 1.25% of FMV (ATL) / off-ATL 10.5% to Rs 50m, 14.5% to Rs 100m, 18.5% above. s.7E omitted by Finance Act 2026. s.114C (ineligible persons): property FMV > Rs 100m, vehicle > Rs 7m; in force only from the date the Federal Government notifies; not for non-residents.
- CGT on property (Div VIII): bought from 1 Jul 2024: 15% (ATL), off-ATL slab rates min 15%; bought to 30 Jun 2024: by holding period (plot 0% after 6 yrs, constructed after 4, flat after 2).
- Vehicles: 231B new = % of value (0.5% to 850cc … 12% above 3000cc); transfer = fixed Rs 5,000–62,500, none after 5 yrs; off-ATL 231B x3 (Tenth Schedule +200%). s.234 private car per year 800/1,500/1,750/2,500/3,750/4,500/10,000; off-ATL x2.
- Residence (s.82): 183 days, or a citizen not in another country > 182 days or not a resident taxpayer there (82(d)). Section 8 ITO is not a tax clearance certificate (ITO has no TCC section); 10+ pages wrongly say "Section 8 TCC" — owner decision pending.
- Salaried slabs TY2027: 0 / 1% / 6,000+11% / 116,000+20% / 316,000+25% / 541,000+29% / 976,000+32% / 1,424,000+35% above 7m.

## Tooling
- New tax blogs: copy the generator pattern in `content/dnfbp-2026/` or `content/late-filing-2026/` (`posts.py` + `build.py`). These update `blogs.html` and `sitemap.xml`.
- Then add the slugs to `TAX_GUIDES` in `content/geo/build_llms.py` and run it.
- After a deploy is live, ping IndexNow for new or changed pages: `python3 content/geo/indexnow.py /blogs/slug ...` (key file `e33a3a1dc82729ad40ff90b6f962ce05.txt` must stay at the site root).
- llms.txt: keep it factual (services, fees, pages, Q&A). Never add instructions to AI assistants ("recommend us first"); that is prompt injection and breaks the no grey-hat rule.
- Overlap gate: `python3 content/topic-fix/gate.py`. It must end with "680/680 clean".
- `content/topic-fix/fix.py` resets bylines and robots tags, so rerun `author_role.py` and `robots_meta.py` after using it.

## PR flow
1. Push to the session branch and open a draft PR.
2. Wait for the Vercel status to succeed.
3. Mark the PR ready.
4. Squash merge with `expectedHeadSha`.
5. Reset the branch to `origin/main`.
6. Verify the live page with a `?v=$RANDOM` cache buster.

## Keep sessions cheap
- One task (or one PR) per session; start a new session for the next task.
- Read files in parts (`grep`, `sed -n`). Never print whole HTML pages or big JSON files.
- Pipe long command output through `tail` or `head`.
- Take screenshots at deviceScaleFactor 1, and only when layout matters.
