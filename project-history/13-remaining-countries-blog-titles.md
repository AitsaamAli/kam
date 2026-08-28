# Remaining Countries — Finalized Blog Titles (Not Yet Written)

Updated 2026-08-28. This is the title-level plan for every country cluster still to be written. **Germany, Italy, and USA are now DONE** (see `06-content-strategy-projects.md` "Status as of 2026-08-28" for what was actually built and where) — removed from this file. What's below is genuinely still unwritten.

When picked up, follow the production process documented in `06-content-strategy-projects.md` and `08-production-pipeline-and-tools.md`. **Read the note at the bottom of this file first** — the Germany/Italy/USA batch was drafted by an external Claude session and taught a real lesson about verifying externally-sourced content before publishing it.

## Canada (Tier 1, rank 4 — de-prioritized for approval-rate reasons, but still a real opportunity)
No existing 5-post cluster; existing pillar (`canada-immigration-fbr-tax-return-pakistan-2026.html`) is at 1,533 words (already expanded once) — check current word count before deciding whether it needs another pass. **Note the priority report's caution: Canada's approval rate has collapsed to ~38%, so don't lead a content push with this country.**
1. **Canada Study Permit — FBR Tax Documents & GIC Financial Evidence Checklist** (Guaranteed Investment Certificate as primary proof, parents'/sponsor's FBR returns as source-of-funds support)
2. **Canada Express Entry & PNP — NTN, Tax Returns & Settlement Funds Guide** (CRS points, settlement funds requirement, provincial nomination specifics)
3. **Canada Start-Up Visa & Owner-Operator LMIA — SECP, Audited Accounts & FBR Requirements for Entrepreneurs**
4. **Canada Visitor & Super Visa — Wealth Statement & Proof of Ties to Pakistan** (Super Visa is specifically for parents/grandparents of Canadian residents — a distinct, high-value angle)
5. **Moving to Canada — What Happens to Your Pakistan Tax Filing, NTN & FBR Status After You Leave**

## Ireland (Tier 1, rank 6 — smaller pool but rising approval trend)
No pillar page exists yet (0 dedicated pages) — needs a **new pillar page** first.
1. **Ireland Student Visa — FBR Tax Documents & Financial Evidence Checklist** (€10,000 living-cost proof + bank statements)
2. **Ireland Critical Skills Employment Permit — NTN, Tax Returns & Sponsorship Guide**
3. **Ireland Start-Up Entrepreneur Programme (STEP) — SECP, Audited Accounts & FBR Requirements for Entrepreneurs**
4. **Ireland Visitor Visa — Wealth Statement & Proof of Ties to Pakistan**
5. **Moving to Ireland — What Happens to Your Pakistan Tax Filing, NTN & FBR Status After You Leave** (also worth covering the 24-month Third Level Graduate post-study work permit as a hook within this post)

## Tier 2 — Gulf countries (Saudi Arabia, UAE, Qatar): a DIFFERENT structure, not the 5-post visa-type pattern
Per the priority report, these visas are employer-sponsored with no proof-of-funds step, so the student/skilled/business/visitor/post-move template doesn't fit — Germany, Italy, and USA all independently confirmed this same pattern (no-proof-of-funds visa routes need a different content structure, not a forced fit). The real commercial angle here is **ongoing compliance after arrival**, aimed at the huge existing population of Pakistani workers already there (530,256 to Saudi in 2025 alone). Suggested titles for this distinct cluster (not yet planned in detail — this is a starting point, not a finalized list):
1. **NTN Registration for Overseas Pakistanis in Saudi Arabia/UAE/Qatar — Why You Still Need One**
2. **Filer Status From Abroad — How Gulf-Based Pakistanis Get on the ATL Without Visiting Pakistan**
3. **Sending Money Home From Saudi/UAE/Qatar — Remittance Documentation & Section 111 Risk**
4. **Buying Property in Pakistan While Working in the Gulf — NTN, Filer Status & the Real Tax Savings**
5. **Coming Back to Pakistan After Years in the Gulf — Reactivating Your Filer Status & Wealth Statement**

## Tier 3 remaining — Spain, Greece, Portugal (Italy is done, see above)
**Read `10-known-issues-and-open-items.md` item #1 before touching this group** — Spain/Greece/Portugal's existing pillar pages overlap each other 17.5-36%. Fix that overlap first; don't add a new cluster on top of it. Italy's cluster (done 2026-08-28) deliberately did NOT touch these three files, so it hasn't made the overlap worse, but it also hasn't fixed it — still open.

## Suggested order if resuming this project
1. Fix the Spain/Greece/Portugal overlap (see `10-known-issues-and-open-items.md`) — do this before any Tier 3 expansion
2. Canada — full cluster (deprioritized for approval-rate reasons, but still real search volume, and the pillar already exists)
3. Ireland — new pillar + cluster, smaller pool but genuinely zero existing coverage
4. Gulf (Saudi/UAE/Qatar) — a separate project with its own distinct content structure, largest raw audience of any tier

## Lesson from the 2026-08-28 Germany/Italy/USA batch — read before trusting any externally-drafted content package again
That batch was drafted by an external Claude session (not this repo's Claude Code session) and delivered as zip files of `.js` data objects matching this project's generator format, each with a detailed README claiming specific validation had already been done (word counts, tag balance, uniqueness percentages, fact-verification notes). **The work was genuinely excellent** — real fresh web research with explicit hedging discipline, several factual corrections to this very history folder (see `09-verified-facts-and-figures.md`), and it caught a real pre-existing bug in the live Italy pillar (it wrongly claimed FBR documents are needed for Italy's Decreto Flussi work-visa route).

But **one claim in the USA package's README could not be verified**: it said uniqueness had been cross-checked against a "Canada cluster" file (`05-moving-to-canada.js`) that does not exist anywhere — not in that zip, not in this repo, not anywhere findable on the local disk. This was flagged rather than silently trusted or silently dropped.

**How to apply next time:** treat an externally-drafted package's own self-reported validation (word counts, uniqueness percentages, "already checked against X") as a claim to independently re-verify, not a fact to trust — re-run the actual word-count/tag-balance/uniqueness-check scripts yourself on the generated output before publishing, and if a README references a comparison file, confirm that file actually exists before accepting the claimed result. Most of this particular batch's claims turned out accurate when independently re-checked — but one didn't, and it would not have been caught without checking.
