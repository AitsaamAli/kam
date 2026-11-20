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

## Blog standards (owner's decisions, Nov 2026)
- Length: topic blogs at least 1,600–1,700 words of real content (no padding); city/regional pages at least 1,250. Longer is fine when the facts support it.
- Every blog is informational *and* commercial: a "done for you" box near the top and a service section (what we do, risks of DIY, how it works, fee) with a WhatsApp CTA. Use only fees published on /pricing; otherwise "fixed fee confirmed before work starts".
- Do not promote sales tax (STRN, sales tax returns) in new blogs; the firm is focusing on DNFBP and sole proprietorship clients.
- No doorway pages: city pages only where there are genuinely local facts (e.g. one per FBR DNFBP directorate), overlap with other pages under 15%.
- No duplicate or thin content: check every new blog against all site pages (not only the gate set) before publishing, and avoid topics an existing page already targets.
- Facts only from FBR's own texts (Income Tax Ordinance PDF amended to the latest date, SROs, FBR/FMU guidance), quoted to the section.

## Site-wide parts (Nov 2026)
- Fees in body text must match /pricing: `content/seo-quickwins/fees_fix.py` (rules for known wrong fees; unpublished fees become "fixed fee confirmed before work starts").
- One footer on every tax page (`ka-footer`, with NAP, hours and GBP link), set by `content/ui-2026/apply.py`. `content/seo-quickwins/footer_nap.py` is superseded.
- Service pages use WebPage + Service schema, not BlogPosting: `content/seo-quickwins/service_schema.py`.
- DNFBP service page: `content/dnfbp-service/build.py` -> `/dnfbp-compliance-services`.
- Homepage stats are static text (no JS counters, no unverifiable % or turnaround claims).
- Design layer (owner approved Nov 2026): `content/ui-2026/apply.py` (idempotent) gives every tax page one menu, a slow top strip of client messages (pausable, no turnaround claims), the shared `/assets/ka-ui.css` + `/assets/ka-ui.js`, one Call/WhatsApp bar on phones, equal-size WhatsApp/Call button pairs, an "On this page" box on guides and the "Short answer" label. Run it after building new pages; bump `V` in it when the assets change. Do not add turnaround claims ("24-hour", "same-day", "30 minutes").

## Keyword research
- Do not use Semrush (no paid API units). Use the Search Console exports the owner provides, the site's sitemap, and free Google suggestions (`https://suggestqueries.google.com/complete/search?client=firefox&gl=pk&hl=en&q=...`).

## Tax facts in use (check before reuse)
- TY2026 return deadline: 31 Oct 2026.
- s.182 late filing (ITO amended to 30.06.2026, Finance Act 2026): higher of 0.1% of tax payable or Rs 1,000 per day; min Rs 10,000 (75%+ salary income) or Rs 50,000 (others); max 200% of tax payable; reduced 75%/50%/25% if filed within 1/2/3 months of the due date. "Tax payable" = higher of assessed tax or tax of the last year filed on time.
- s.182A ATL surcharge: Rs 25k individual / 50k AOP / 100k company.
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
