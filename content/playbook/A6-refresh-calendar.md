# A6. Yearly refresh calendar (playbook, 22 Nov 2026)

Why: competitors still show "file before 30 September 2026" banners in November. A dated, correct page beats them on freshness and trust. Every refresh follows the CLAUDE.md fact rules (official source, date checked) and changes `dateModified` only when content really changed.

| When | Trigger | Pages to refresh | What to check |
|---|---|---|---|
| June (budget week) | Federal and provincial budgets; Finance Bills | `/pricing` (fees only if owner changes them), salary/business/property/vehicle calculators, `CLAUDE.md` "Tax facts in use" | New slabs and rates once the Finance Act is passed, not the bill |
| 1 July | Finance Act in force; new ITO PDF on FBR | All guides quoting rates: 236C/236K, 231B/234, bank profit, salary slabs, s.182/182A | Re-read the ITO "amended up to" PDF; update the facts list first, then pages |
| July–August | Return season opens; IRIS form for the new tax year | Return-filing guides, `income-tax-filing-*`, ATL guides | Due date (s.118: 30 September unless FBR extends), IRIS form changes |
| September | Deadline month; possible FBR extension | Homepage strip, deadline guides, late-filing pages | Only state an extension after FBR announces it |
| October / November | Extended deadline passes | Late-filer guides, Form ATL-U pages, s.182/182A calculators | Remove "before the deadline" copy the day after it passes |
| January | Mid-year | PRA/SRB/KPRA registration pages, DNFBP pages | Provincial rate notices, PRA/FBR SROs since July |
| Every month | New SROs and circulars | `llms.txt` / `llms-full.txt` rebuild, IndexNow ping for changed pages | `python3 content/geo/build_llms.py`, `content/geo/indexnow.py` |

Rules:
1. Update `CLAUDE.md` "Tax facts in use" first; then the pages that quote those facts.
2. Never move dates forward without a real content change (Google treats fake freshness as spam).
3. Remove expired banners and "before the deadline" wording the day after a deadline.
