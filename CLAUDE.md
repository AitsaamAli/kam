# Kamboh Associates site (kambohassociates.com)

Static HTML site on Vercel. Tax site at the root; a separate web-development section under `/digital`. `/*.md`, `/*.py` and `content/` are excluded from the deploy (`.vercelignore`).

## Standing rules (owner's decisions)
- Tax site and `/digital` stay separate: no cross-links, and no tax terms in `/digital` titles or H1s.
- Do not change existing titles, meta descriptions, canonicals, robots tags, H1s or URLs unless the task asks for it.
- Aitsaam Ali is credited only as "Author". Never claim a tax-consultant licence, credential or role for him. Figures are "from FBR".
- Say "FBR Registered", never "FBR Certified". Replies are promised "within office hours" (Mon–Sat 9:00–18:00, Fri 9:00–12:30, Sun closed). Never claim 24/7.
- Keep existing review and rating text as it is. Google Business Profile has 84 reviews. No fake reviews, no grey-hat or black-hat SEO.
- Every fact must come from an official source (FBR, IRIS, SECP, FMU, provincial authorities). Link the source and give the date it was checked. If a fact cannot be verified, leave it out.
- Report to the owner in Roman Urdu, briefly.

## Tax facts in use (check before reuse)
- TY2026 return deadline: 31 Oct 2026.
- s.182 late filing: 0.1%/day, max 50%, min Rs 40,000 (Rs 5,000 for low-salary cases).
- s.182A ATL surcharge: Rs 25k individual / 50k AOP / 100k company.
- Salaried slabs TY2027: 0 / 1% / 6,000+11% / 116,000+20% / 316,000+25% / 541,000+29% / 976,000+32% / 1,424,000+35% above 7m.

## Tooling
- New tax blogs: copy the generator pattern in `content/dnfbp-2026/` or `content/late-filing-2026/` (`posts.py` + `build.py`). These update `blogs.html` and `sitemap.xml`.
- Then add the slugs to `TAX_GUIDES` in `content/geo/build_llms.py` and run it.
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
