# Knowledge base — read before answering as any specialist

This is the accumulated judgment of a 20+ year practitioner in each
department, not a checklist to recite. Every role in ROLES.md should apply
the relevant section below as lived experience — including the parts where
experience means knowing when the textbook answer is wrong for THIS project.
Numbers here are real industry benchmarks; still verify against the actual
project data found in Step 0 rather than assuming they apply blindly.

## Read this before trusting any number or date below

This file is a snapshot, not a live feed. SEO, AEO and GEO are among the
fastest-moving disciplines in software — Google runs multiple core updates
a year, AI platforms change citation behavior monthly, and a "2023 update"
mentioned below may since have been superseded. Treat every specific
threshold, date, or "as of" claim in this file as **last known, not
current truth**:

- If a web search tool is available in this session, verify any claim that
  is time-sensitive or high-stakes (a specific algorithm rule, a current
  rich-result eligibility, a current platform behavior) before presenting
  it to the user as fact — especially before it drives an implementation
  decision like removing schema or changing a redirect strategy.
- If no search tool is available (common in Claude Code / offline project
  work), say so plainly when a claim matters: "this was accurate as of my
  last check, worth confirming with a quick search since this changes
  often" — rather than stating it with false confidence.
---

## WordPress & page-builder reality (most common stack for Pakistani/South Asian SMBs)

A large share of small-business websites in this market run WordPress with
Elementor/WPBakery/Divi and WooCommerce, not a custom framework. This
changes what's actually achievable:

- **Yoast vs Rank Math**: Rank Math's free tier covers more schema types
  (Product, FAQ, HowTo, LocalBusiness) than Yoast's free tier, which is why
  it's become the more common choice for SMB sites in this market since
  ~2021. If the site already has one installed, work with it rather than
  recommending a migration unless there's a real reason.
- **Page builders bloat HTML and hurt CWV** — Elementor/WPBakery generate
  deeply nested div structures and load their own CSS/JS bundles per page,
  which is the single most common cause of poor LCP/INP on WordPress SMB
  sites. Real fixes that don't require a rebuild: a caching plugin
  (WP Rocket or the free LiteSpeed Cache if on LiteSpeed hosting),
  image compression (ShortPixel/Imagify), disabling unused builder
  widgets/animations, and moving off shared hosting with poor TTFB —
  cheap shared hosting (common for budget-constrained Pakistani projects)
  is often the actual bottleneck, not the code.
- **WooCommerce category/attribute URLs** create faceted-navigation
  duplicate-content risk fast (color/size filters generating crawlable
  URLs) — the practical fix on WordPress is usually noindexing filtered
  URL patterns via Rank Math/Yoast's URL pattern rules rather than
  fighting WooCommerce's URL structure directly.
- **Don't assume a rebuild is the answer.** A veteran's real judgment call
  on a WordPress SMB site: 80% of technical issues are fixable with
  caching + image optimization + a good SEO plugin + hosting upgrade, at a
  fraction of the cost of a framework migration. Only recommend leaving
  WordPress when the project has genuinely outgrown it (real scale, real
  engineering team, real performance ceiling already hit after the above).

---

## Urdu, Roman Urdu & RTL — specifics most playbooks skip

This matters directly for Pakistan-market and other South Asian projects
and is rarely covered in generic (US-centric) SEO material.

- **Urdu script vs Roman Urdu are different languages to search engines.**
  A page in Urdu script (اردو) and a page in Roman Urdu ("kya haal hai")
  target completely different query sets — people search both, often for
  the same intent, and neither substitutes for the other. Decide
  deliberately which one (or both, as separate pages, never mixed on one
  page) based on where the audience actually types, not which is easier
  to write. Younger, urban, mobile-first audiences frequently type Roman
  Urdu even when they'd read Urdu script comfortably — check real query
  data (Search Console query report, if available) rather than assuming.
- **hreflang and lang attribute:** Urdu script content uses `lang="ur"`
  and needs `dir="rtl"` on the html or content container — Roman Urdu
  content is still Latin script left-to-right and should use `lang="ur"`
  only if truly Urdu-language content transliterated, otherwise `lang="en"`
  is often more accurate since Roman Urdu is technically English-alphabet
  code-switched text. This is a genuinely debated edge case — when unsure,
  match what the page actually reads as to a native speaker.
- **RTL layout bugs are a real, common technical debt item** on sites that
  bolt on Urdu/Arabic as an afterthought — check that navigation, forms,
  icons (arrows especially), and number formatting actually mirror
  correctly in RTL mode, not just that text renders right-to-left. This is
  a `js-seo`/`architecture`/`web-dev` handoff, not just a translation task.
- **Keyword research tools under-serve Urdu.** Most volume-estimate tools
  (even paid ones) have thin or unreliable data for Urdu-script queries
  compared to English. Treat Urdu-script volume estimates as directional
  only, weight Google Autocomplete/People Also Ask/Related Searches
  (sampled directly, in-language) and real Search Console query data more
  heavily than third-party tool volume numbers for this language.
- **Voice and AI-assistant behavior in Urdu is meaningfully behind
  English** — Google Assistant, Siri and most AI chat interfaces have
  weaker Urdu support than English or Arabic. For GEO work specifically,
  weight English-language content higher for AI-answer visibility even for
  a Pakistan-first brand, since that's still where AI platforms understand
  and cite most reliably as of this writing — flag this trade-off
  explicitly to the client rather than assuming Urdu GEO will perform like
  English GEO.

---

## Keyword clustering — the real methodology, not just a list

A "keyword list" is not a cluster. A cluster is a group of queries that
should be served by the SAME page because they share intent and Google
already treats them as the same topic. Building clusters wrong is the
single most common reason a keyword research deliverable never turns into
traffic — it produces either cannibalization (5 pages competing for one
intent) or dilution (1 page trying to rank for 5 different intents).

**The real clustering process, in order:**

1. **Seed collection.** Pull the raw query universe from free sources
   (per the operator's budget constraints, assume no paid tool):
   Google Autocomplete (type the seed + each letter a-z), People Also Ask
   (sample 3-4 levels deep, PAA nests), Related Searches at the bottom of
   the SERP, Google Trends "related queries", and — once the site has any
   history — the real Search Console query report, which is the single
   most reliable source because it shows queries Google has *already*
   started associating with the site.

2. **SERP-overlap clustering (the actual test that matters).** For each
   candidate pair of keywords, check the top 10 results for both. If 4+ of
   the same URLs appear for both queries, Google considers them the same
   topic — cluster them together, one page serves both. If overlap is
   weak (0-2 shared URLs), they're different intents even if the words
   look similar — keep them as separate pages/clusters. This single check
   prevents the most common real-world mistake: writing two separate blog
   posts for "invoice software" and "billing software" when Google already
   treats them as one topic, splitting authority across both instead of
   ranking either well.

3. **Intent-layer check.** Within a SERP-confirmed cluster, confirm the
   dominant intent (informational / commercial-investigation / transactional
   / navigational) matches what the page is meant to do. A cluster that's
   SERP-similar but split across two intents (e.g. "best invoice software"
   = commercial-investigation vs "invoice software login" = navigational)
   still needs separate pages even with some URL overlap — use judgment,
   not the mechanical rule alone.

4. **Pillar/supporting hierarchy.** Within each topic area, identify one
   pillar (the broad, higher-volume, harder query) and the supporting
   clusters underneath it (narrower, more specific, easier to rank first).
   New/low-authority sites should sequence supporting clusters first —
   they rank faster and build the topical relevance and internal links the
   pillar page later benefits from. This sequencing decision belongs to
   this role; topical-authority builds the entity map, this role decides
   the realistic ranking order given the project's current authority.

5. **One cluster, one target page, one primary internal-link path.** Every
   finished cluster needs: a single target URL (existing or planned), and
   the 2-3 other clusters that should link to it. Handing off a cluster
   list without this mapping leaves architecture and brief-writer
   guessing — always include it.

**Deliverable shape for keyword-research when clustering (supersedes the
generic table in ROLES.md for this specific task):** cluster name → pillar
or supporting → SERP-overlap evidence (which shared URLs confirmed it) →
representative queries → intent → target URL (existing/new) → internal
links in → priority given current site authority.

A deliverable existing is not the same as it working. Rough success signal
per department, to hold roles accountable to rather than just checklist
completion:

- **Technical**: the specific issue is gone from Search Console coverage
  /Core Web Vitals report on a re-check, not just "fix applied."
  **Content**: the page ranks page-1 for its target cluster within a
  realistic window (weeks for a low-competition long-tail, months for
  competitive head terms) — if it doesn't after enough time has passed,
  that's a signal to revisit the brief or the SERP read, not just publish
  more.
  **AEO/GEO**: the exact target snippet/PAA/AI-answer slot is actually won
  when checked, not just "formatted correctly and hoped for."
  **Off-page**: the link is live, indexed, and from a real, checkable page
  — not just "outreach sent."
  **Analytics/CRO**: the metric it targeted moved, and the move survives
  a sanity check against seasonality/external causes, not just "dashboard
  built."

A veteran's real edge is knowing which 20% of the checklist actually moves
the needle for this specific project, and saying "skip the rest for now" —
not running every tactic on every project. Apply that judgment explicitly:
state what you are deliberately not doing and why.

---

## Technical SEO

**Core Web Vitals thresholds (2024+ standard, INP replaced FID in March 2024):**
LCP good ≤2.5s, needs improvement ≤4s. INP good ≤200ms, needs improvement
≤500ms. CLS good ≤0.1, needs improvement ≤0.25. These are the 75th
percentile of real user visits (field data, CrUX), not lab scores — a page
that looks fast in Lighthouse can still fail field CWV on real 3G-ish
connections in markets like Pakistan, India, Southeast Asia, Africa. For
projects targeting those markets specifically test on throttled 4G, not
just fast fiber.

**Crawl budget** matters at real scale — sites under roughly 10k
indexable URLs rarely have a crawl-budget problem; Googlebot will find
everything. Above 100k+ URLs (large ecommerce, marketplaces, classifieds)
it becomes real: fix via robots.txt disallow on faceted/session params,
noindex low-value pages rather than blocking them from crawl (blocking hides
the noindex signal), and canonical consolidation before touching sitemaps.

**JS rendering:** Google generally renders client-side JS within its crawl
queue now, but the rendering queue is a second wave — content in an
unrendered initial HTML can lag indexing by days on lower-authority
domains. AI crawlers (GPTBot, ClaudeBot, PerplexityBot) are much less
reliable at JS rendering than Googlebot — assume they read raw HTML only
unless proven otherwise. This is the single biggest reason SSR/SSG matters
more for GEO than it now does for classic SEO.

**International / hreflang, the real failure patterns:**
- hreflang must be reciprocal (if A points to B, B must point back to A)
  and self-referencing (A includes A) or Google ignores the whole cluster —
  this is the #1 real-world hreflang bug.
- x-default is for the language/country selector page or the closest
  generic fallback, not automatically the English version.
- Country ≠ language. /en-pk/ (English, Pakistan) and /en-us/ (English, US)
  are different hreflang values from /ur-pk/ (Urdu, Pakistan) — don't
  conflate targeting a country with targeting a language.
- ccTLD (.pk, .ae) sends the strongest geo-signal but fragments authority
  across domains — for a project without resources to build authority per
  domain separately, subdirectory (site.com/pk/) usually outperforms
  subdomain or ccTLD in the first 2-3 years.
- Currency/price display alone is not enough for regional relevance —
  local payment methods, local case studies, and local search phrasing
  (not just translation) drive the actual ranking and trust signal.

**Migrations:** the real-world failure mode is not the redirect map, it's
sequencing. Correct order: stage and test the redirect map on a subset →
update internal links to point directly at new URLs (don't rely on
redirects for internal links) → launch with 301s live before DNS cutover
completes → submit new sitemap immediately → keep old sitemap live and
submitted for 2-4 weeks so Google finds the redirects faster → monitor
Search Console coverage report daily for the first 2 weeks, weekly after.
Expect a visible dip even on a clean migration — 2-6 weeks is normal, 3+
months means something is actually wrong (usually thin/mismatched
redirect targets or lost internal links).

**Schema:** the highest-leverage types by real eligibility impact are
Product, Organization, FAQPage (note: Google restricted FAQ rich results
to authoritative government/health sites in 2023 — don't oversell FAQ
schema's SERP impact anymore, but it still helps AI answer extraction),
Article/NewsArticle, BreadcrumbList, LocalBusiness, and Review/AggregateRating
(only mark up reviews genuinely on the page — this is one of the most
common manual-action triggers). HowTo lost most rich-result surfaces in
2023 — implement for machine understanding/GEO, not for a snippet.

---

## AEO — Answer Engine Optimisation

Featured snippets and PAA still run on classic Google ranking + extraction
mechanics: the passage needs to sit high enough to rank (top 5, usually)
AND be formatted as a direct, self-contained answer in the first sentence
after the heading. Definition-style queries want a 40-60 word direct
answer; list/step queries want an actual ordered/unordered list Google can
lift; comparison queries want a table.

Real pattern from experience: writing the answer paragraph immediately
under an H2/H3 that echoes the query phrasing (not keyword-stuffed, just
natural) outperforms burying the answer in paragraph 4 even when the rest
of the page is stronger. Snippet real estate rewards structural discipline
more than raw authority once you're already ranking on page 1.

FAQPage rich results are now restricted mostly to well-established
government/health sites (2023 Google update) — for most commercial
projects the FAQ schema is still worth implementing for AI extraction and
voice, just don't promise the client rich-result snippets from it anymore.

---

## GEO — Generative Engine Optimisation

This is the newest discipline and the playbook is still forming, but the
patterns that already hold up:

**LLMs cite differently than Google ranks.** They lean heavily on: (1)
Wikipedia and Wikidata for entity facts, (2) Reddit and forum discussions
for "real experience" style answers — Reddit content has been especially
prominent in Google's AI Overviews and in ChatGPT browsing since 2024, (3)
comparison/listicle content from mid-authority sites, (4) the brand's own
site for direct factual claims about itself (pricing, features), and (5)
structured/original data sources (studies, surveys) far more than
generic marketing copy.

**Getting cited is a different game from getting ranked.** A page can rank
poorly in classic search and still get pulled into an AI answer if it is
the clearest, most extractable, most specific source for that exact
sub-claim. Optimize individual passages for extractability (a clear claim,
a number, a named source) rather than optimizing the whole page for one
target keyword.

**Practical GEO checklist that actually moves outcomes:**
- Make sure GPTBot, ClaudeBot, Google-Extended, PerplexityBot are not
  blocked in robots.txt unless the client deliberately wants to opt out of
  AI training/citation (some publishers do, for licensing reasons — that's
  a real, valid business decision, surface it rather than assuming yes).
- Publish an llms.txt at the root — an emerging, not-yet-universal
  convention, low cost, real upside as adoption grows.
- Get the brand's Wikipedia/Wikidata presence accurate — most AI systems'
  "knowledge panel"-style facts about a brand trace back here.
- Answer the exact prompts real buyers type into AI assistants (from
  prompt-research) directly on-site, in extractable Q&A blocks.
- Comparison and "alternatives to X" pages are disproportionately pulled
  into AI answers for consideration-stage prompts — this is one of the
  highest-leverage content types in GEO right now.
- Track visibility by literally running the prompts monthly across
  ChatGPT, Gemini, Perplexity, Claude and logging mention/position/
  sentiment — there is no reliable third-party tracking tool yet that
  beats manual testing for accuracy as of 2026.

**What doesn't work (seen fail repeatedly):** keyword-stuffing for AI the
way one would for 2010s Google; buying "AI SEO" link packages promising
guaranteed ChatGPT citations (no legitimate mechanism exists for this);
treating GEO as separate from having genuinely citable, accurate,
well-sourced content — the fundamentals of E-E-A-T matter MORE for GEO,
not less, because an LLM's whole judgment of "citable" runs on the same
authority/consistency signals.

---

## Content & E-E-A-T

E-E-A-T (Experience, Expertise, Authoritativeness, Trust) is not a ranking
factor Google directly scores — it's the lens Google's quality raters and,
increasingly, its ranking systems use to approximate it. In practice, the
signals that actually correlate with rankings holding up through core
updates: named authors with real credentials and a bio, first-hand
experience markers (original photos, specific details a copier wouldn't
have, "I tested this" framing where genuinely true), external validation
(the author or brand mentioned elsewhere, not just self-published claims),
and content that doesn't over-promise relative to the site's actual
authority in that space (a brand-new finance blog making aggressive
investment claims is exactly the pattern the Helpful Content and core
updates since 2022 have targeted).

**YMYL (Your Money or Your Life)** categories — health, finance, legal,
safety — get held to a materially higher bar. For projects in these
categories, author medical/financial credentials, citations to primary
sources, and a visible review/editorial process matter far more than
elsewhere, and thin AI-generated content without genuine expert review is
a real risk of being specifically targeted by quality updates.

**Content decay is real and predictable** — most content peaks 3-6 months
after publish then decays without maintenance. A refresh cadence (update
stats, add new sections, fix outdated claims) on the top 20% of traffic-
driving pages every 6-12 months usually outperforms constant new
publishing on a thin budget.

---

## Off-page & Link Building

**Risk-scaled reality, not theory:** guest posting on genuinely relevant
sites with editorial standards is fine; guest posting through paid
"guest post package" resellers is a Google Search Console manual action
waiting to happen, especially post-2023's more aggressive link spam
detection. Digital PR (real coverage from real journalists, earned through
genuine newsworthy angles) is the highest-durability tactic and the one
that actually held up across every major link-spam update since Penguin.

**For international/multi-market projects:** link authority from one
country's local publications generally has limited direct transfer value
to another market's rankings — build authority per target market rather
than assuming one global campaign covers all regions in a multi-region
rollout.

**Unlinked mention reclamation** is consistently the highest ROI-per-hour
off-page tactic that gets skipped — the brand is already mentioned, the
ask is trivial (add a link), and conversion rate on outreach is far higher
than cold link building.

---

## Analytics, CRO & Attribution

**GA4 reality check:** GA4's default attribution model (data-driven) and
its session/engagement definitions differ meaningfully from Universal
Analytics — don't port UA-era benchmarks over directly. Server-side
tagging (via GTM server container) is increasingly necessary as browser
ad/tracking blockers and iOS privacy changes degrade client-side signal —
for projects with real ad spend riding on the data, this is worth the
engineering cost.

**Attribution honesty:** last-click attribution systematically
undervalues top-of-funnel SEO/content work and overvalues brand/direct
traffic that content actually generated. When forecasting SEO's
contribution, say plainly that attribution models undercount organic's
real influence on conversions that get credited to direct or paid brand
search, rather than presenting last-click numbers as the full picture.

**CRO fundamentals that hold across markets:** trust signals (reviews,
security badges, clear contact info) matter disproportionately more in
markets/categories with lower brand trust in ecommerce generally — this is
a real, common conversion blocker for newer brands in markets like
Pakistan, India, and MENA where card-not-present fraud concerns are
higher; offering cash-on-delivery or well-known local payment methods
(easypaisa, JazzCash, etc. for Pakistan) often moves conversion more than
any copy change.

---

## International / multi-market project patterns (lived experience)

- **Don't assume translation = localisation.** A literal translation of
  US-market copy into Urdu/Arabic/other reads as foreign and hurts trust.
  Real localisation changes examples, currency, cultural references, and
  frequently the entire argument structure (what convinces a US buyer and
  a Gulf buyer are often genuinely different claims, not just different
  words).
- **Phase market rollouts.** Trying to launch content + links + technical
  work across 5 markets simultaneously with a small team produces mediocre
  results everywhere. The veteran move: pick the 1-2 highest-opportunity
  markets, get them genuinely strong, then replicate the proven playbook —
  not run everything thin across everywhere at once.
- **Local search behavior differs by market** — voice search and mobile-
  first behavior is disproportionately higher in some emerging markets;
  WhatsApp/social-commerce driven discovery matters more than pure organic
  search in some categories/regions (Pakistan D2C is a real example) —
  don't apply a US-market-shaped SEO playbook unmodified.
- **Regulatory/compliance varies** — GDPR (EU), data residency rules, and
  local advertising regulations differ by market; flag this to the client
  rather than assuming one global compliance posture covers every region.
  None of this is legal advice — for anything regulatory that carries real
  risk (data residency, consumer protection law, ad regulation), say
  plainly that a local lawyer should confirm it, rather than presenting a
  specialist's summary as compliance sign-off.
- **Currency and budget realism** — link building, paid tools, and content
  costs that are trivial in USD-denominated budgets can be genuinely
  prohibitive in PKR/local-currency budgets; a veteran scales the
  recommended tactics to the real budget rather than recommending an
  enterprise playbook to a bootstrapped project.

---

## Judgment calls a 20-year practitioner makes that a junior doesn't

- Says "this will take 6-9 months to show results" honestly instead of
  promising fast wins, and separates the quick technical fixes (which can
  show impact in weeks) from the content/authority work (which genuinely
  takes quarters).
- Refuses tactics that risk a manual action or algorithmic penalty even
  when the client asks for them, and explains the real risk rather than
  just saying no.
- Knows when NOT to do something on the checklist — e.g., doesn't recommend
  a full technical overhaul for a 40-page brochure site with no crawl
  budget problem; doesn't recommend an aggressive link campaign for a site
  that isn't ready content-wise to earn/keep that authority.
- Distinguishes correlation from causation in reporting — a ranking jump
  right after a core update rollout might be the update, not the work
  done; says so rather than claiming credit for everything positive.
- Scales recommendations to the team size and budget actually available
  (found in the brief/constraints), not to an idealized enterprise team.
