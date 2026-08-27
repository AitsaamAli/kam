# Blog Content Inventory & Rewrite Method

## Current scale (verify against live repo — this is a 2026-08-27 snapshot)
- 1,282 files in `blogs/`
- 1,439 URLs in `sitemap.xml`
- 141 root-level `.html` pages

## The core standing rule: 2000+ words per blog
Every blog on this site is held to a **2000+ word standard** (measured as visible text inside `<article>`, tags stripped). This has been the target since the "Master Prompt v4" era and remains the bar for every new/rewritten page. A quick word-count script:
```js
// from c:/Users/786/Desktop/kam
const fs = require('fs');
function countWords(html) {
  html = html.replace(/<script[\s\S]*?<\/script>/gi,' ').replace(/<style[\s\S]*?<\/style>/gi,' ');
  const artMatch = html.match(/<article[^>]*>([\s\S]*?)<\/article>/i);
  const content = artMatch ? artMatch[1] : (html.match(/<body[^>]*>([\s\S]*?)<\/body>/i)||[null,html])[1];
  return content.replace(/<[^>]*>/g,' ').replace(/&[a-zA-Z#0-9]+;/g,' ').split(/\s+/).filter(Boolean).length;
}
const files = fs.readdirSync('blogs').filter(f=>f.endsWith('.html'));
const results = files.map(f => [f, countWords(fs.readFileSync('blogs/'+f,'utf8'))]).sort((a,b)=>b[1]-a[1]);
// e.g. filter for a priority tier:
const tier = results.filter(([f,wc])=>wc>=1300&&wc<2000);
console.log(tier.length, 'files under 2000 words');
```
**Always re-run this word-count check as the literal last step before `git commit`** — not from an earlier check in the same editing session (a file was once committed at 1953 words because a later small edit pass wasn't re-verified). If a count reads 1900-1999, add one more real paragraph — don't round up mentally.

## What's already been fully written / rewritten (do not duplicate or redo — check here first)

### 1. The original abroad/overseas-Pakistani FBR pillar series (10 blogs, 2026-07-15)
`fbr-tax-clearance-abroad-pakistan-guide-2026.html` (pillar), `pending-fbr-tax-returns-abroad-jana-pakistan-2026.html`, `italy-jane-se-pehle-fbr-tax-return-pakistan-2026.html`, `canada-immigration-fbr-tax-return-pakistan-2026.html`, `uk-visa-fbr-tax-return-pakistan-2026.html`, `spain-visa-fbr-tax-return-pakistan-2026.html`, `germany-visa-fbr-tax-return-pakistan-2026.html`, `australia-visa-fbr-tax-clearance-pakistan-2026.html`, `fbr-non-resident-status-182-day-rule-pakistan-2026.html`, `section-8-tax-clearance-certificate-abroad-pakistan.html`. Later extended with `greece-visa-fbr-tax-return-pakistan-2026.html` and `portugal-visa-fbr-tax-return-pakistan-2026.html` (2026-07-23).

### 2. The country-cluster expansion (2026-08-25/27, most recent work — see `06-content-strategy-projects.md` for full strategy)
- **UK pillar rewritten** to 2000+ words (938→2128 words, commit `72ce9607`, bug-fixed in `df02d4e8`) + **5 new UK cluster posts** (commit `64d93148`): `uk-student-visa-fbr-tax-documents-pakistan-2026.html`, `uk-skilled-worker-visa-ntn-tax-returns-pakistan-2026.html`, `uk-business-investor-visa-secp-fbr-pakistan-2026.html`, `uk-visitor-visa-wealth-statement-pakistan-2026.html`, `uk-after-moving-tax-filing-ntn-fbr-status-pakistan-2026.html`.
- **Australia pillar rewritten** (929→1936 words) + **5 new Australia cluster posts** (commit `e4e08af3`): `australia-student-visa-fbr-gte-financial-evidence-pakistan-2026.html`, `australia-skilled-visa-189-190-491-fbr-tax-returns-pakistan-2026.html`, `australia-business-investor-visa-secp-fbr-pakistan-2026.html`, `australia-visitor-visa-wealth-statement-pakistan-2026.html`, `australia-after-moving-tax-filing-ntn-fbr-status-pakistan-2026.html`.
- **Not yet done, per the priority report:** Germany (2nd-fastest-growing student volume, thin coverage) and Italy (fresh 2025-26 bilateral labor-migration news hook, thinner tax-doc angle) are the next two recommended country clusters. Canada is explicitly de-prioritized (student visa approval collapsed to ~38%). See `06-content-strategy-projects.md` for the full tier ranking and reasoning.

### 3. The two big topic-gap content pushes (100 topics each, see `06-content-strategy-projects.md` for full detail)
- **Informational 100-topic plan** (`content-gap-100-new-blog-topics.md`): **100% complete** as of 2026-08-17 — 92 new pages written, 8 topics satisfied by pre-existing pages.
- **Commercial/local-intent 100-topic plan** (`commercial-local-100-blog-topics.md`): **26/100 done** (Sections A+B — city "Best Tax Consultant" pages + corporate/registration/sales-tax/SME service pages). Sections C-K (74 topics) not started — pick up from there if asked to continue this specific project.

### 4. The general thin-blog rewrite marathon (large, ongoing-until-recently effort)
A huge number of individually-named files were rewritten from <2000 words to 2000+ across many sessions in July-August 2026 — see `git log --grep="^fix: rewrite"` or `--grep="^fix: expand"` for the full list (dozens of commits, one file per commit, e.g. `tax-for-engineers-pakistan-2026.html`, `mutual-fund-tax-pakistan-2026.html`, `fbr-audit-procedure-pakistan-2026.html`, etc.). An older curated memory list claiming "47 done" is stale and undercounts significantly — **trust the word-count script output over any static list**, since scores of additional files have been rewritten since that list was last updated.

## What's still thin / not yet done
As of the last full rescan (2026-08-01 era): **1,068 of then-1,138 blog files were under 2000 words.** Breakdown at that time: 17 files at 1700-1999, 130 at 1300-1699, 32 at 800-1299, 798 at 400-799 (**mostly ~212 near-duplicate city pages**: `income-tax-filing-<city>.html` ×90, `ntn-registration-<city>.html` ×122 — deliberately NOT batch-padded, see below), 91 under 400 words. Many of the 1300-1999 tier have since been completed (dozens of rewrite commits), but **re-run the word-count script fresh rather than trusting this exact breakdown** — it's a stale snapshot and a lot of the 100-topic/country-cluster work has also happened since.

**Deliberately deferred, not forgotten:** the ~798 near-duplicate city pages were explicitly excluded from the rewrite priority queue — mechanically padding hundreds of city-name-swapped pages risks Google's "scaled content abuse" spam policy (see `04-seo-technical-history.md`). If ever revisited, it needs a genuinely differentiated angle per city, not a template fill.

## The recurring "generic extra-content" bug pattern (important — read before rewriting any thin file)
Most files in the thin-blog rewrite queue carry a specific bug, not just a low word count: a **generic, non-topic-specific filler block** copy-pasted across dozens of files — a boilerplate "Overview" H2 + filer-vs-non-filer table + "Who Is Affected"/"How to Stay Compliant" section, a fake 3-question FAQ ("How can Kamboh Associates help", "What is the fee", "Is this online"), and/or a "Why Choose Kamboh Associates" company-boilerplate block. Combined, this can be 30-50%+ of a file's word count while adding near-zero real information about the page's actual topic.

**The correct fix is NOT to pad the word count further — strip the filler and replace with genuinely unique, topic-specific content.** This typically means writing 2-4 new substantive H2 sections from scratch per file, not just adding a paragraph. Budget accordingly.

**Watch for these sub-patterns while working through the queue:**
- **Full topic-mismatch bug** (worse than filler): the *entire visible body* is a different topic's boilerplate with the target keyword crudely substituted into headers — e.g. an H2 reading "Property Tax Filing in Homemakers" (grammatically wrong when you substitute the topic in). Confirmed on `tax-for-housewives-homemakers-pakistan.html`, `house-rent-allowance-tax-pakistan.html`, `tax-on-car-purchase-pakistan.html`, `pension-tax-pakistan-2026.html` before they were fixed. **Signal: an H2 that reads grammatically wrong when you mentally substitute the page's actual topic. When spotted, full rewrite from scratch, not a patch.**
- **Duplicate/contradictory section:** genuine topic-specific content exists, but a second "extra-content" section repeats the same table/facts with *different, conflicting* numbers (found on `tax-on-cryptocurrency-pakistan-2026.html`, `withholding-tax-pakistan-2026.html`). Remove the redundant/wrong duplicate, don't just add more.
- **Real content hidden in JSON-LD only:** the visible FAQ is generic, but the JSON-LD `FAQPage` schema has genuine topic-specific Q&A that isn't shown to users. Check schema for salvageable content before writing from scratch.
- **Genuinely-fine-but-thin:** some files are already well-written and topic-specific, just short — these only need 1-2 new genuine sections added, nothing removed.
**Always read the actual body first** to figure out which of these categories a given file is in before deciding whether to rewrite fully or extend.

## Cross-file duplication clusters — plan the differentiation angle BEFORE writing
Several small clusters of similarly-titled pages exist where overlapping content is a real risk. When touching any of these, check what angle the sibling page(s) already use and pick a genuinely different one:
- **Crypto:** `cryptocurrency-tax-fbr-pakistan.html` = legal/regulatory-status angle (done). `tax-on-cryptocurrency-pakistan-2026.html` = practical gain-computation angle (done). `crypto-tax-pakistan-2026.html` = compliance/reporting angle (if/when reached).
- **FBR Section 122 notices:** `fbr-notice-section-122-pakistan.html` = legal-mechanics angle (done). `fbr-section-122-notice-pakistan.html` = practical response/procedure angle (if/when reached).
- **Minimum tax:** `turnover-tax-pakistan-2026.html` = comparison-test mechanics angle (done). `minimum-tax-section-113-pakistan.html` = should take an enforcement/industry-rate-table angle instead (if/when reached).
- **Overseas Pakistani cluster** (8 sibling files, angles already assigned — see file for exact mapping, most are done): investment (done, RDA-as-access-channel framing), property (done, POA/NOC/repatriation), general filing process (done, nil-return/catchup), tax-clearance-abroad (done), pending-returns-before-leaving (done), Canada-specific (done as part of the country-cluster work), RDA account-mechanics-itself, remittances-specifically, NICOP-identity-angle.
- **IRIS portal:** `fbr-iris-portal-guide-pakistan.html` = navigation/PSID/ATL angle (done). `fbr-iris-2-guide-2026-pakistan.html` = should take an "IRIS 2.0 specific changes" angle (if/when reached).
- **Consultant/location marketing pages** (different genre + different HTML template from educational blogs — multi-line formatted, NOT single-line minified; the `rewrite-apply.js` automation script fails on these, hand-edit only): `best-tax-consultant-karachi-2026.html` (done, SRB/export/trading angle), `best-tax-consultant-near-me-pakistan.html` (how-to-evaluate/red-flags angle), `best-tax-consultant-pakistan.html` (national/multi-city angle), `affordable-tax-consultant-pakistan.html` (pricing-transparency angle), `online-tax-consultant-pakistan.html` (remote-service-specifics angle), `small-business-tax-consultant-pakistan.html`/`sme-tax-consultant-pakistan.html` (SME-specific needs — differentiate these two from each other too).

**General rule for any new topic that's even slightly close to an existing page:** run the uniqueness-check tool (`08-production-pipeline-and-tools.md`) against it before writing, and pick a deliberately different angle rather than discovering overlap after the fact.

## Established canonical facts to stay consistent with across property-tax content
Section 236C = 2.75% filer / 5.5% non-filer. Section 236K = 1.25% filer / 2.5% non-filer. Capital Gains Tax = 15%→0% sliding by holding period (exempt beyond 6 years). Non-filer CGT = double the filer rate. If rewriting or referencing property tax anywhere, these must match — several early rewrites had to fix self-contradicting rate tables where different sections of the same page disagreed.
