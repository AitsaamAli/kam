# Kamboh Associates Digital: Writer Brief for Blog Posts #201–#300

**Version:** 4.0, 30 October 2026
**For:** a Claude (Claude Code) session writing the next 100 web development guides for `kambohassociates.com/digital/blog`
**Prepared by:** the Kamboh Associates Digital SEO and content team. This team wrote, audited and published posts #1–#200, which are live.

---

## 0. How to use this brief (read first)

You are writing blog posts that will be published as they are delivered. Each post you deliver is a Python file in an exact format. The site's build script turns it into a page with schema, so **the format must be exact** and **every rule below is a hard requirement**.

Work happens in **5 parts**. The owner will ask you for one part at a time ("Write Part 1"). Do only the part asked.

| Part | Posts | Clusters | Count |
|---|---|---|---|
| Part 1 | #201–#220 | V (websites by profession) | 20 |
| Part 2 | #221–#240 | V (last 5), W (your situation, first 15) | 20 |
| Part 3 | #241–#260 | W (last 5), X (charges), Y (Roman Urdu, first 3) | 20 |
| Part 4 | #261–#280 | Y (rest), Z (support), AA (cities, first 6) | 20 |
| Part 5 | #281–#300 | AA (rest), AB (this or that) | 20 |

For each part:
1. Set up the workspace (section 4). This is needed once only.
2. Write the posts **five at a time**. After every five, run the auditor and fix every FAIL before writing the next five.
3. When all posts in the part pass, run the clustering audit (section 10) and write the part report (section 12).
4. Deliver one zip file: `kad-part-N.zip`. It contains `posts/*.py` for that part and `PART-N-REPORT.md`.

Do not skip the audit. Do not deliver a post that shows FAIL. If a rule seems impossible for a post, say so in the report rather than breaking the rule.


### 0.1 Lessons from earlier batches (read before writing anything)

Earlier batches were published, audited and partly rebuilt. Every problem below happened once. The auditor now fails a post for each of them, so avoid them from the start.

| Problem seen before | Rule now |
|---|---|
| Pages were delivered as HTML and pushed to GitHub. They linked to the tax site 300 times and used the wrong logo and design. | Deliver **only `posts/*.py` files and the part report**. Never write HTML, never push to GitHub, and never touch any other file. The team builds the pages with the site template. |
| Link text was cut mid-word ("...Compared With Hiri", "...Registrar Without"). | Write link text as a short, complete, natural phrase (for example "our guide to transferring a domain"). Never paste a title and truncate it. The auditor fails cut-off or dangling link text. |
| "What We Would Build for You" appeared word for word in 72 posts, and "What does it cost?" in 13. | Every H2 must be specific to the post's topic (for example "Our Solar Installer Website Package"). Generic headings fail, and so does any H2 already used by a published guide or by another post in your batch. |
| Seven FAQ questions appeared word for word in two posts. | Every FAQ question must be new. The auditor checks all 1,325 published questions and your batch. |
| The same closing sentence was pasted into several posts. | No sentence of 12 or more words may appear in two posts. Phrase overlap with any other post must stay under 3%. |
| Prices were typed as text (for example "Rs 40,500"). | Our prices only ever appear as `{P['...']}` inside an f-string. Typed price text fails. |
| Titles in one cluster shared the same shape ("Website Design X: Shops, Schools, Clinics"). | Vary title shapes within a cluster. The auditor warns about similar titles. |
| One source link was dead (404). | Open every source on the day you write. Use only working, official pages. |
| Cluster lists had only 2 terms. | Write 5–8 real cluster terms per post. |

**Done means:**
- the auditor shows `0 failing` for the whole part
- every warn line has been fixed or explained in the report
- the report includes the fact log

---

## 1. Who you are writing for, and why

**The business.** Kamboh Associates is a firm in Lahore, Pakistan, established in 2008. Its main business is a tax consultancy. **Kamboh Associates Digital** is its separate web development service line. It builds business websites, online stores and web applications for clients in Pakistan, the Gulf, the UK and North America.

**The reader.** A business owner or manager who wants a website, online store or web app and is deciding what to buy, from whom, and for how much. Readers include:
- a clinic owner in Lahore
- a clothing brand on Instagram
- a Sialkot exporter
- a UK agency looking for a white-label team
- a Dubai shop owner

They are not developers. Write for an intelligent person with no technical background.

**The job of every post:**
1. Answer the searcher's question better than anything else on page 1 of Google.
2. Be the answer that AI assistants (Google AI Overviews, ChatGPT, Gemini, Perplexity) quote.
3. Earn trust, then point the reader to the matching service page or a WhatsApp enquiry.

**The competition:**

| Competitor | Weakness |
|---|---|
| Ezitech, Webo Creators, Progriso, Digital Sita, FMEOS | Generic copy, contradictory prices, thin FAQs, no sources, doorway city pages |
| SyncDigital | UAE only |

We win with:
- depth
- one consistent price list
- dated, sourced facts
- Pakistan-specific detail (COD, couriers, JazzCash/Easypaisa, .pk domains, Urdu, slow mobile data)
- honesty

---

## 2. Facts you may state, and claims you must never make

### 2.1 Approved business facts (use these exactly)

**Identity and contact**

| Fact | Value |
|---|---|
| Name in body text | "Kamboh Associates Digital", or "we" and "our team" |
| Parent | Kamboh Associates, Lahore, established 2008 |
| Office | Shop No 34 Rizwan Block Market, opposite Rizwan Park, Awan Town, Lahore 54660, Pakistan |
| Phone / WhatsApp | 0328-4675162 (+92 328 4675162) |
| Email | info@kambohassociates.com |
| Office hours | Monday to Saturday 9:00 AM to 6:00 PM; Friday 9:00 AM to 12:30 PM (Pakistan time, UTC+5) |

**How we work**
- We publish fixed starting prices (section 2.2).
- Every project starts with a written scope and fixed price before any deposit.
- We work on milestone payments: a deposit of usually 30–40% after the scope is approved, a mid-project payment and the balance on delivery.
- The domain and hosting are registered in the client's name, and the client owns the code after final payment.
- Maintenance is optional and priced separately.
- We reply to a WhatsApp enquiry with a scope and price within one business day.
- We work with clients in Pakistan, the Gulf, the UK and North America.
- Overseas clients are invoiced in Pakistani rupees and pay by international bank transfer in milestones.

### 2.2 Our prices (PKR). Quote them only through the `P` dictionary

```python
P = {
    "landing": "Rs 22,500",
    "starter": "Rs 40,500",
    "business": "Rs 85,500",
    "store": "Rs 157,500",
    "app": "Rs 360,000",
    "app_range": "Rs 360,000 to Rs 1,350,000",
    "maint": "Rs 7,200",
}
```

In post files write `{P['starter']}` and so on inside an f-string. **Never type our prices as plain numbers.** If a price changes, every post must update automatically.

**What each key means**

| Key | Meaning |
|---|---|
| `landing` | landing page |
| `starter` | small website, up to 5 pages |
| `business` | business website, up to 10 pages |
| `store` | online store |
| `app` | web application starting price |
| `app_range` | web application range |
| `maint` | maintenance per month |

**Settled market facts.** Use these figures where they fit. They are already researched and sourced in the live guides, so link to that post when you use them.

| Fact | Value | Link to |
|---|---|---|
| Business website (template) | Rs 20,000–80,000 | `website-price-in-pakistan` |
| Business website (custom design) | Rs 80,000–250,000 | `website-price-in-pakistan` |
| Online store | Rs 80,000–600,000 | `website-price-in-pakistan` |
| Hosting and domain | roughly Rs 8,000–25,000 a year | `website-price-in-pakistan` |
| Shared hosting in Pakistan | Rs 5,500–15,000 a year | `domain-and-hosting-price-in-pakistan` |
| .pk domain (PKNIC) | Rs 2,100 a year from 1 August 2026, billed for two years | `domain-and-hosting-price-in-pakistan` |
| Shopify Basic | $29 a month billed yearly ($39 monthly) | `shopify-store-price-in-pakistan` |
| Shopify Grow | $79 ($105 monthly) | `shopify-store-price-in-pakistan` |
| Shopify Advanced | $299 ($399 monthly) | `shopify-store-price-in-pakistan` |
| Shopify Payments | not available in Pakistan | `shopify-store-price-in-pakistan` |
| Shopify third-party gateway fee | 2% / 1% / 0.6% by plan; COD orders carry no Shopify fee | `shopify-store-price-in-pakistan` |
| Wallet and card gateway fees (reported) | about 1.5–3% per transaction | `payment-gateways-pakistan-compared` (#34) |
| Time difference | Pakistan is 4 hours ahead of the UK in British Summer Time, 5 in winter, and 1 hour ahead of the UAE all year | `website-cost-uk`, `website-cost-dubai` |

### 2.3 Never write any of these (automatic rejection)

- **Invented clients or proof:**
  - client names, testimonials, reviews, case-study results or "we built X for Y"
  - numbers of clients, websites or projects
  - awards, certifications, partner badges or team size
  - **Illustrative examples are fine if labelled.** For example: "A typical Lahore clinic might…" or "Example figures, not a real client."
- **Unsourced figures:** statistics, percentages or market sizes without a source you have verified. If you cannot source a number, describe the point without it.
- **Guarantees and false promises:**
  - guarantees of Google rankings, traffic, sales or AI mentions
  - claims that we are "the best", "No. 1" or "the leading" company
- **Named people:** do not name any staff member.
- **Tax content.** The tax side of the business is a separate site. See section 3.
- **Dangerous advice:** legal, medical or financial advice beyond what a website buyer needs. Where a regulation applies, name the regulator, link its official site and tell the reader to check current rules with them.
- **Generic AI filler.** Section 6.6 lists the banned phrases.

---

## 3. Separation from the tax site (hard rules)

The web development section must look and behave like a separate business line, so that Google never mixes it with the tax site.

1. **Titles and H1s must not contain** any of these words: tax, taxes, FBR, NTN, STRN, filer, non-filer, ATL, return, returns, SECP, withholding, WHT, GST, "sales tax", income, salary, IRIS.
2. **Body text must not discuss** tax, filing, NTN, FBR, SECP or company registration. Where a business needs paperwork, as in #81, say "your accountant or tax adviser" and move on.
3. **Internal links** may only point to:
   - the 8 service pages in section 5.3
   - other guides at `/digital/blog/<slug>` from the slug list in section 9
   - **never** to `/`, `/blogs`, or any tax page
4. **External links** go only in the `sources` list, and in the body only for official sources (section 7).

---

## 4. Workspace setup (do this once)

Create this folder:

```
kad-blog/
  prices.py          (copy from section 2.2, wrapped as: P = {...})
  audit_posts.py     (copy from Appendix A, unchanged)
  published_index.json (index of the 200 published guides; the auditor needs it; comes in the kit)
  posts/             (your post files go here)
```

`prices.py` must contain exactly:

```python
"""Single source of truth for published web-development prices (must match digital/pricing.html)."""

P = {
    "landing": "Rs 22,500",
    "starter": "Rs 40,500",
    "business": "Rs 85,500",
    "store": "Rs 157,500",
    "app": "Rs 360,000",
    "app_range": "Rs 360,000 to Rs 1,350,000",
    "maint": "Rs 7,200",
}
```

Test the setup: `python3 audit_posts.py posts` should run and report 0 posts. If you received the kit zip, everything above is already in place.

---

## 5. File format (exact)

### 5.1 File name and header

- **Name:** `<cluster letter><number>_<short_name>.py`, for example `c23_wp_shopify_custom.py` or `d34_payment_gateways.py`. Use the cluster letter from section 9.
- **Header:** every file starts with exactly these lines:

```python
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    ...
)
```

### 5.2 Fields (all required, in this order)

| Field | Type | Rule |
|---|---|---|
| `order` | int | The post number (201–300) |
| `slug` | str | **Exactly** the slug in section 9 |
| `title` | str | ≤ 60 characters. Contains every main word of the primary keyword. Keyword near the start. Different from `h1` |
| `h1` | str | 35–95 characters. Contains the keyword. Can be longer and more descriptive than the title |
| `crumb` | str | 2–6 word short name for breadcrumbs and covers, e.g. "Shopify vs WooCommerce" |
| `description` | str | **110–165 characters**. Contains the keyword. States the answer or promise, plus what the reader gets. No quotes |
| `keyword` | str | The primary keyword from section 9, exactly |
| `cluster` | list | 5–8 related search terms: synonyms, questions, Roman Urdu variants. **Never** another post's primary keyword |
| `category` | str | Exactly the category in section 9 |
| `published`, `updated` | str | Today's date, `YYYY-MM-DD` |
| `published_h`, `updated_h` | str | The same date as `29 October 2026` |
| `answer` | str | **40–60 words.** Answers the main question directly in the first sentence, starting with or containing the keyword. Include a number (price, time, count) when one exists |
| `takeaways` | list | **Exactly 5** one-sentence key points |
| `body` | str | HTML in a triple-quoted string (rules in 5.4). Use an f-string (`f"""..."""`) only if you insert `{P[...]}` |
| `faqs` | list of tuples | `("Question?", "Answer.")`. Spokes: 6–8. Pillars (#201, #226, #258): 8–10. Answers 40–60 words, plain text, self-contained |
| `sources` | list of tuples | 3–9 entries of `("Publisher — Page title (what it supports)", "https://...")`, from section 7 |
| `method` | str | 25–90 words: how this guide was researched (sources used, what is our own pricing, what is illustrative) |
| `related` | list | 3–5 slugs: the cluster pillar plus 2–4 siblings (section 9) |
| `service_links` | list of tuples | 1–2 entries of `("/digital/...", "Label")`, from section 5.3 |
| `cta` | str | A short question that opens the closing CTA box, e.g. "Planning an online store?" |
| `wa` | str | URL-encoded WhatsApp pre-fill, **must start with** `Hi%2C%20I%20read%20your%20`. Example: `Hi%2C%20I%20read%20your%20Shopify%20vs%20WooCommerce%20guide%20and%20need%20a%20quote` |

### 5.3 Allowed service pages

| Path | Page |
|---|---|
| `/digital` | Home |
| `/digital/business-websites` | Business websites |
| `/digital/ecommerce-development` | Online stores |
| `/digital/web-app-development` | Web apps |
| `/digital/pricing` | Prices |
| `/digital/web-development-lahore` | Lahore team |
| `/digital/contact` | Quote |
| `/digital/blog` | Blog index |

### 5.4 Body HTML rules

**Allowed tags only:**
- headings: `<h2 id="kebab-id">`, `<h3>`
- text: `<p>`, `<strong>`, `<em>`, `<a href="...">`
- lists: `<ul>`, `<ol>` (`<ol start="5">` allowed), `<li>`
- tables: `<table>`, `<tr>`, `<th>`, `<td>`, and `<td class="price">` for a price cell

**Forbidden:**
- `h1`, `img`, `div`, `span`, `br`, `script`, `style`
- inline `style=`
- `target=` or `rel=` on links
- `colspan`, `&nbsp;`
- emojis

**H2s:**
- Every H2 has a unique kebab-case `id`.
- These ids are reserved and must not be used: `faqs`, `sources`, `key-takeaways`, `how-we-researched`, `keep-reading`.
- Spokes need at least 5 H2s and pillars at least 6.
- At least 2 H2s are questions ending in "?". Ideally most are.
- One H2 contains the primary keyword.

**Tables:**
- At least one table per post.
- The first row is all `<th>`.
- Every row has the same number of cells.
- Keep tables to 2–4 columns so they read on phones.

**Links in the body:**
- at least 2 links to other guides, as `/digital/blog/<slug>`
- at least 1 link to a service page from 5.3
- use descriptive anchor text, never "click here"

**Length** (body only, excluding answer, takeaways and FAQs):
- spokes 600–1,300 words
- pillars 1,000–2,200 words

**Do not include in the body** an FAQ section, sources, author box or CTA. The build adds them from the other fields.

### 5.5 Python gotchas

- In an f-string, write dictionary keys with single quotes: `{P['store']}`. Never put a literal `{` or `}` in an f-string.
- Escape any double quote inside a double-quoted string, or use single quotes.
- FAQ answers that use `P` must be f-strings: `f"... {P['starter']} ..."`.
- Keep files UTF-8. Use plain apostrophes (').

### 5.6 Reference example: a live post in the exact format

Post #17 is shown in full below. It was written before this brief raised the minimums, so **new posts must also meet the higher bars in 5.2 and 5.4**: at least 600 body words, at least 2 question H2s, and a service-page link in the body. Copy its format and tone, not its words.

```python
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prices import P

POST = dict(
    order=17,
    slug="who-owns-your-website",
    title="Who Owns Your Website? Domain, Hosting and Code",
    h1="Who Owns Your Website? Domain, Hosting and Code Ownership Explained",
    crumb="Who Owns Your Website",
    description="Who owns your website: how to check who controls your domain, hosting, code and Google accounts, the warning signs of lock-in, and how to take back control.",
    keyword="who owns my website",
    cluster=["website ownership", "domain ownership check", "developer holding my domain",
             "get website back from developer", "website lock-in"],
    category="Hiring a Developer",
    published="2026-10-28", published_h="28 October 2026",
    updated="2026-10-28", updated_h="28 October 2026",
    answer=("Who owns your website depends on whose name is on six things: the domain, the hosting account, the code and design, the admin "
            "login, the business email and your Google accounts. If any of them sits in your developer's name, they control that part. "
            "Check each one today and move it into your own name."),
    takeaways=[
        "Website ownership is six separate things, not one.",
        "The domain matters most: whoever controls it controls your website and email.",
        "Paying for a website does not automatically transfer ownership; the agreement and account names decide it.",
        "Add your developer as a user on your accounts instead of letting them own the accounts.",
        "If a developer refuses to hand over access, start with the domain registrar and your written agreement.",
    ],
    body="""
<h2 id="six-parts">Who Owns My Website? The Six Parts</h2>
<table>
<tr><th>Part</th><th>What it is</th><th>Should be registered to</th></tr>
<tr><td>Domain</td><td>Your address, such as yourbusiness.pk</td><td>You, with your email as the contact</td></tr>
<tr><td>Hosting</td><td>The server account where files live</td><td>You, paid from your card or account</td></tr>
<tr><td>Code and design</td><td>Files, theme and custom work</td><td>You, after final payment, by agreement</td></tr>
<tr><td>Admin login</td><td>WordPress, Shopify or app administrator</td><td>You as owner; developer as a separate user</td></tr>
<tr><td>Business email</td><td>info@yourbusiness.pk mailboxes</td><td>You, on an account you control</td></tr>
<tr><td>Google accounts</td><td>Analytics, Search Console, Business Profile</td><td>You as owner; developer added as a user</td></tr>
</table>

<h2 id="check">How to Check Who Owns Each Part</h2>
<ol>
<li><strong>Domain:</strong> look up your domain on ICANN's lookup tool for generic domains, or ask your registrar. For .pk domains, check the contact details with your registrar or PKNIC. The registrant name and email should be yours.</li>
<li><strong>Hosting:</strong> can you log in to the hosting control panel yourself? Who receives the renewal invoice?</li>
<li><strong>Admin login:</strong> do you have an administrator or store-owner account, not only an editor account?</li>
<li><strong>Google accounts:</strong> in Analytics, Search Console and your Business Profile, check that you are listed as owner.</li>
<li><strong>Code:</strong> do you have a recent full backup or access to the code repository?</li>
</ol>

<h2 id="warning-signs">Warning Signs of Website Lock-in</h2>
<ul>
<li>You receive hosting or domain renewal requests from the developer, not from the provider.</li>
<li>You have never logged in to your own site's admin panel.</li>
<li>The developer says the theme or system is "theirs" and cannot be moved.</li>
<li>Monthly fees continue, but you cannot get a list of what they cover.</li>
<li>Your business email stops working whenever an invoice is late.</li>
</ul>

<h2 id="paid-not-owned">Paying for a Website Is Not the Same as Owning It</h2>
<p>Many owners assume that paying for a site means owning it. In practice, ownership depends on whose name is on the accounts and on what your agreement says about the code and design. Copyright in creative and software work generally starts with whoever creates it, unless an agreement transfers it. That is why our <a href="/digital/blog/website-development-contract-checklist">contract checklist</a> includes a clear ownership clause that applies once the final payment is made.</p>

<h2 id="right-setup">The Right Set-up From Day One</h2>
<p>The safest pattern is simple: you create the accounts in your name and add your developer as a user. Google Analytics, Search Console and Business Profile all let owners add other users with limited permissions and remove them later. WordPress has user roles for this, and Shopify lets store owners add staff accounts. When the project ends, you remove the developer's access; nothing needs to be "transferred".</p>

<h2 id="take-back">How to Take Back Control</h2>
<ol>
<li><strong>Ask politely in writing</strong> for each login and the domain transfer code, referring to your agreement.</li>
<li><strong>Start with the domain.</strong> If it is registered to you, the registrar can help you regain access to it.</li>
<li><strong>Request a full backup</strong> of files and database, or the code repository transfer.</li>
<li><strong>Claim your Google accounts</strong> through each service's ownership verification process.</li>
<li><strong>Set up new hosting</strong> in your name and restore the backup there.</li>
</ol>
<p>If the domain itself is registered to the developer, recovery is harder; this is why it must be in your name from the start. Our <a href="/digital/blog/website-handover-checklist">handover checklist</a> lists everything you should receive at launch.</p>
""",
    faqs=[
        ("How do I know if I own my website?",
         "Check six things: the domain registrant, the hosting account, your admin login, your business email, ownership of Google Analytics, Search Console and Business Profile, and a copy of the code. If every one of them is in your name and you can log in yourself, you control your website."),
        ("Can a web developer keep my domain name?",
         "If the domain was registered in the developer's name, they control it, which is why it should always be registered to you. If it is registered to you but they hold the login, contact the registrar to recover access. Your written agreement and payment records help if there is a dispute."),
        ("Who owns the copyright of my website design?",
         "Copyright in creative and software work generally starts with whoever creates it, unless an agreement transfers it. A good website contract states that the client owns the design, code and content after final payment. Without that clause, ownership can be unclear, so add it before the project starts."),
        ("Should my developer have access to my Google accounts?",
         "Yes, but as an added user, not as the owner. Create Analytics, Search Console and Business Profile in your own account, then add the developer with the permissions they need. When the project or contract ends, you simply remove their access, and you keep all the data and history."),
        ("Meri website ka maalik kaun hai, kaise check karoon?",
         "Dekhein ke domain kis ke naam par register hai, hosting ka bill kis ko aata hai, aur kya aap khud admin panel mein login kar sakte hain. Google Analytics aur Search Console mein bhi owner aap hon. Agar koi cheez developer ke naam par hai, to usay abhi apne naam par muntaqil karwayen."),
        ("What should I do if my developer refuses to hand over my website?",
         "Ask in writing for each login and the domain transfer code, referring to your agreement and payments. Contact the domain registrar if the domain is in your name. Request a backup, set up hosting in your name and claim your Google accounts through their verification process. Get legal advice for serious disputes."),
    ],
    sources=[
        ("ICANN — Registrants' benefits and responsibilities", "https://www.icann.org/resources/pages/benefits-2013-09-16-en"),
        ("ICANN Lookup — check domain registration details", "https://lookup.icann.org/"),
        ("Google Analytics Help — Add, edit and delete users", "https://support.google.com/analytics/answer/9305788"),
        ("Google Search Console Help — Manage owners, users and permissions", "https://support.google.com/webmasters/answer/7687615"),
        ("Google Business Profile Help — Add or remove owners and managers", "https://support.google.com/business/answer/3403100"),
        ("WordPress.org — Roles and capabilities", "https://wordpress.org/documentation/article/roles-and-capabilities/"),
        ("WIPO — Copyright", "https://www.wipo.int/copyright/en/"),
    ],
    method=("The six-part checklist reflects the ownership problems we see when clients move to us from other developers. Account steps follow "
            "the official help pages for ICANN, Google Analytics, Search Console, Business Profile and WordPress. The copyright point "
            "follows WIPO's general overview and is not legal advice for any specific dispute."),
    related=["website-handover-checklist", "website-development-contract-checklist", "domain-and-hosting-price-in-pakistan",
             "how-to-choose-web-development-company"],
    service_links=[("/digital/business-websites", "Business websites you fully own"), ("/digital/contact", "Get help recovering access")],
    cta="Not sure who controls your website?",
    wa="Hi%2C%20I%20read%20your%20website%20ownership%20guide%20and%20need%20help%20checking%20mine",
)
```

---

## 6. Writing standard

### 6.1 Structure of every post (body)

1. **Opening H2 that restates the main question** and contains the keyword (for example "How Much Does a Clinic Website Cost in Pakistan?"). Its first paragraph expands the answer box with the "why".
2. **Comparison or decision table** early, in the first or second section.
3. **3–6 middle sections**, each adding something concrete:
   - a step
   - a number with its source
   - a checklist
   - a worked example (labelled as illustrative)
   - a Pakistan-specific detail
   - a mistake to avoid
4. **"What we would build for you"**: a short section that applies the topic to our service. It quotes `P` prices, explains what the package includes and links the matching service page.
5. **Questions to ask / checklist / next step**: a practical closing section with links to 2+ sibling guides.

### 6.2 Voice

- **Write plainly.** Use short sentences in the active voice. Write "you" for the reader and "we" for Kamboh Associates Digital.
- **Spelling:** British (organise, colour, licence as noun), matching the live posts.
- **Be specific, not hyped.** Write "loads in under 3 seconds on a 4G phone" rather than "lightning fast". Write "costs Rs 85,500" rather than "affordable".
- **Be honest about trade-offs.** Say when a cheaper option, a freelancer, Shopify or doing nothing is the better choice. This builds trust and is quoted by AI systems.
- **Use local detail where true:**
  - cash on delivery
  - TCS, Leopards, PostEx and Trax couriers
  - JazzCash, Easypaisa, PayFast and Raast payments
  - .pk domains
  - Urdu and Roman Urdu speakers
  - load-shedding
  - mid-range Android phones on mobile data
  - WhatsApp as the main sales channel

### 6.3 SEO rules

- One primary keyword per post, never shared (section 9 assigns them).
- **Keyword placement**, all checked by the auditor:
  - title
  - H1
  - description
  - the first 100 words (the answer box counts)
  - one H2
- **Variants:**
  - Use the cluster terms naturally in H2s, H3s and FAQ questions.
  - Do not stuff: the exact primary keyword should appear about 3–6 times in the whole post.
- **Intent match** (section 9 gives the intent):
  - C (commercial): compare options and prices
  - I (informational): teach and explain
  - L (local): real local facts, never a city-name swap
  - T (transactional): the steps to buy or start

### 6.4 AEO rules (answer engines and featured snippets)

- **Answer box:** 40–60 words, the answer in sentence one, a number if possible, no "In this guide we will…".
- **Question H2s** mirror real searches ("How much…", "Which is better…", "Do I need…").
- **Short definitions:** a one-sentence definition right after an H2 that names a concept ("A payment gateway is…").
- **Lists and tables** carry steps and comparisons; Google lifts these directly.
- **FAQs:**
  - questions people actually ask
  - answers of 40–60 words that make sense on their own, without "as mentioned above"
  - one FAQ in **Roman Urdu** for every post with Pakistan as an audience, e.g. "Clinic ki website banwane mein kitna kharcha aata hai?", answered in Roman Urdu

### 6.5 GEO rules (being cited by AI assistants)

- **Quotable facts:** state facts as standalone sentences with the source and date, e.g. "As of 1 August 2026, PKNIC charges Rs 2,100 a year for a .pk domain."
- **Consistent entity:** describe us exactly as in section 2.1, never differently.
- **Original value:** each post must contain at least one thing competitors do not have:
  - a decision table
  - a checklist
  - a template
  - a cost worked example
  - a scenario comparison
- **Cite primary sources:** Google, W3C, official payment providers, regulators. Avoid other agencies' blogs, except for market price ranges.
- **Neutral comparisons:** a fair comparison is more likely to be cited than a sales pitch.

### 6.6 Banned phrases (the auditor fails these)

"in today's digital world / fast-paced world", "in the digital age", "look no further", "unlock the power", "unleash", "game-changer", "elevate your", "seamless", "cutting-edge", "delve", "navigating the", "it's important to note", "in conclusion", "ever-evolving", "robust solution", "one-stop", "whether you're a", "take your business to the next level", "embark", "tapestry", "landscape of", "realm of", "harness the".

Also avoid:
- more than 6 em dashes per post
- "not X, but Y" constructions
- rhetorical openers

### 6.7 E-E-A-T

The build adds an author box, a disclosure and dates. Your `method` field must honestly say:
- which sources you used
- which numbers are our published prices
- which examples are illustrative

### 6.8 Special rules by cluster

- **Industries (cluster E) and regulated topics.** For clinics, dental, pharmacy and law firms, name the regulator and link its official site in `sources`:
  - PMDC (pmdc.pk) for doctors and dentists
  - DRAP (drap.gov.pk) for medicines
  - the Pakistan Bar Council (pakistanbarcouncil.org) for lawyers

  Tell readers to confirm current advertising and privacy rules with them. Do not state specific legal rules you cannot source. Patient and client privacy must be discussed.
- **Local (cluster F).**
  - Our only office is in Lahore. For other cities, say clearly that we work with businesses there remotely through WhatsApp and video calls, with an optional visit to our Lahore office.
  - Never imply an office in that city.
  - Each local post must contain at least 3 real, specific local facts about the city's businesses: its industries, markets, export sectors and buyer behaviour. These must be general knowledge or sourced. Do not invent statistics.
  - Never reuse paragraphs between city posts; Google treats that as doorway pages.
- **Overseas (cluster G).**
  - Write for UK, Gulf, US and Canadian buyers.
  - Prices stay in PKR; you may say "roughly" in GBP or AED only with a dated conversion and a source.
  - Cover the time-zone overlap, contracts, IP, payments and communication honestly.
- **#81, overseas Pakistanis.** Cover the website, domain, hosting, payments and online setup only. Any paperwork goes to "your accountant or adviser". Use no tax words at all.
- **E-commerce payments (cluster D).**
  - Gateway fees, onboarding documents and settlement times change. Quote only figures you can source with a date, and otherwise say "check the provider's current rates".
  - Never say Stripe or Shopify Payments works for Pakistan-registered businesses. They do not, and posts #3 and #35 explain the legal alternatives.


### 6.9 Rules for the clusters in this brief (#201–#300)

These posts follow how the Kamboh Associates tax site grew: many specific, long-tail pages, each answering one exact situation.

- **V, websites by profession.**
  - One profession per post.
  - Show what that profession's customers search for, the pages and features it needs, and a package from `P`.
  - Health and legal professions: name the regulator, link its official site, and make no outcome claims.
  - Never reuse paragraphs between profession posts.
- **W, your situation.**
  - Write for one precise starting point.
  - Open by restating the situation in the reader's words, then give the exact path: steps, costs and risks.
  - Link the general guide on the topic for background.
- **X, charges.**
  - State our own price only where it exists in `P`.
  - For anything else, explain what drives the cost and quote third-party prices only from official pages, with the date checked.
  - Never invent a market rate. If none can be sourced, say so and show the cost drivers in a table.
- **Y, Roman Urdu guides.**
  - Title, H1, answer, takeaways, body and FAQs are written in simple Roman Urdu, as people type it.
  - Technical words stay in English (website, domain, hosting, SEO).
  - Use the same structure, sources and audit rules. The keyword must appear in the title, H1, description, first 100 words and one H2.
  - The `description` may mix Roman Urdu and English.
  - Do not translate an English post line by line. Write for the Roman Urdu searcher.
- **Z, support and availability.** State only what is true:
  - office hours are Monday to Saturday 9:00 AM to 6:00 PM and Friday 9:00 AM to 12:30 PM (Pakistan time), and Sunday closed
  - never write 24/7 or a guaranteed response time
  - explain how requests are handled instead
- **AA, more cities.**
  - Our only office is in Lahore. Say plainly that we work remotely and that clients can visit Lahore.
  - Each post must contain at least 3 real, specific local business facts.
  - Do not invent statistics.
  - Never share paragraphs between city posts.
- **AB, this or that.**
  - Give a short, fair comparison with a "choose this if" table.
  - Use the same fairness rules as the platform comparisons.

---

## 7. Sources

**Use only:**
- URLs from the approved list below, or
- official pages you have opened yourself and confirmed load (HTTP 200) on the day you write. List every such new URL in the part report so we can verify it.

Never cite a page you have not opened. Never guess a deep link.

**Approved source list** (all checked 29 October 2026):

- https://baymard.com/lists/cart-abandonment-rate
- https://business.whatsapp.com/products/business-platform
- https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations_en
- https://datareportal.com/reports/digital-2026-pakistan
- https://developer.chrome.com/docs/lighthouse/overview
- https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps
- https://developer.wordpress.org/advanced-administration/security/backup/
- https://developer.wordpress.org/advanced-administration/security/hardening/
- https://developers.google.com/search/docs/appearance/ai-features
- https://developers.google.com/search/docs/appearance/page-experience
- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- https://developers.google.com/search/docs/appearance/structured-data/local-business
- https://developers.google.com/search/docs/crawling-indexing/301-redirects
- https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
- https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/fundamentals/do-i-need-seo
- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://easypaisa.com.pk/
- https://faq.whatsapp.com/5913398998672934
- https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries-and-regions
- https://help.shopify.com/en/manual/payments/third-party-providers
- https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/
- https://laravel.com/docs
- https://letsencrypt.org/
- https://lookup.icann.org/
- https://nextjs.org/docs
- https://nodejs.org/en/about
- https://owasp.org/www-project-top-ten/
- https://pagespeed.web.dev/
- https://pakistanbarcouncil.org/
- https://pknic.net.pk/
- https://pknic.net.pk/how-to-pay.html
- https://pmdc.pk/
- https://postex.pk/
- https://schema.org/
- https://schema.org/LocalBusiness
- https://search.google.com/test/rich-results
- https://sellercenter.daraz.pk/
- https://stripe.com/global
- https://support.google.com/analytics/answer/9267735
- https://support.google.com/analytics/answer/9305788
- https://support.google.com/business/answer/3403100
- https://support.google.com/business/answer/7039811
- https://support.google.com/business/answer/7107242
- https://support.google.com/webmasters/answer/7687615
- https://support.google.com/webmasters/answer/9128668
- https://trax.pk/
- https://validator.schema.org/
- https://web.archive.org/
- https://web.dev/articles/cls
- https://web.dev/articles/inp
- https://web.dev/articles/lcp
- https://web.dev/articles/vitals
- https://web.dev/explore/progressive-web-apps
- https://wise.com/
- https://wix.com/upgrade/website
- https://woocommerce.com/products/
- https://wordpress.org/about/requirements/
- https://wordpress.org/documentation/article/roles-and-capabilities/
- https://www.agilealliance.org/glossary/mvp/
- https://www.agilealliance.org/glossary/user-stories/
- https://www.facebook.com/business/help/
- https://www.gov.uk/service-manual/agile-delivery
- https://www.icann.org/resources/pages/benefits-2013-09-16-en
- https://www.leopardscourier.com/
- https://www.nngroup.com/articles/ecommerce-product-pages/
- https://www.nngroup.com/articles/usability-101-introduction-to-usability/
- https://www.ontario.ca/page/about-accessibility-laws
- https://www.payoneer.com/
- https://www.paypal.com/pk/home
- https://www.pknic.net.pk/
- https://www.pseb.org.pk/
- https://www.shopify.com/pricing
- https://www.squarespace.com/pricing
- https://www.tcsexpress.com/
- https://www.w3.org/International/questions/qa-html-dir
- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/fundamentals/accessibility-intro/
- https://www.w3.org/WAI/standards-guidelines/wcag/
- https://www.wipo.int/copyright/en/

**Homepages you may cite** for what the organisation is, but not for specific figures (their deep pages block automated checks): https://www.sbp.org.pk/, https://www.jazzcash.com.pk/, https://gopayfast.com/, https://www.drap.gov.pk/, https://www.pta.gov.pk/, https://www.cloudflare.com/.

---

## 8. Workflow for each post

1. **Understand the intent.** Read the row in section 9: keyword, intent, audience, angle and must-include points.
2. **Research.** Search the keyword and look at what ranks. Note what the top results miss, then plan to cover it. Collect 3–9 sources from section 7.
3. **Outline.**
   - title, H1 and description with the keyword
   - 5–9 H2s, 2 or more of them questions, one containing the keyword
   - the table
   - the original-value item
   - the "What we would build for you" section
4. **Write** the answer, takeaways, body, FAQs and method to the rules in sections 5 and 6.
5. **Self-review** against the checklist in section 11.
6. **Run the auditor:** `python3 audit_posts.py posts`. Fix every FAIL. Read every warn and fix it unless you have a reason, which goes in the report.
7. **Log** in your working notes:
   - every fact with a number, and its source
   - every illustrative example
   - any new source URL

---

## 9. The 100 posts: assignments

**Intent codes**

| Code | Meaning |
|---|---|
| C | Commercial |
| I | Informational |
| L | Local |
| T | Transactional |

**Audience codes**

| Code | Meaning |
|---|---|
| PK | Pakistan |
| OS | Overseas |

**Link column:** the main service page for the body link and `service_links`.

**Related:** always include the cluster pillar (marked **P**) plus 2–4 same-cluster siblings. Where natural, also include one guide from #1–#200.

**Already published (#1–#200).** Link to these where relevant. Never reuse their primary keywords.

| # | Slug | Primary keyword | Category |
|---|---|---|---|
| 1 | `website-price-in-pakistan` | `website price in pakistan` | Costs & Budgets |
| 2 | `ecommerce-website-price-in-pakistan` | `ecommerce website price in pakistan` | Costs & Budgets |
| 3 | `shopify-store-price-in-pakistan` | `shopify store price pakistan` | Costs & Budgets |
| 4 | `wordpress-website-price-in-pakistan` | `wordpress website price in pakistan` | Costs & Budgets |
| 5 | `web-app-development-cost-in-pakistan` | `web application development cost pakistan` | Costs & Budgets |
| 6 | `website-maintenance-charges-in-pakistan` | `website maintenance charges pakistan` | Costs & Budgets |
| 7 | `domain-and-hosting-price-in-pakistan` | `domain hosting price pakistan` | Costs & Budgets |
| 8 | `landing-page-design-cost-in-pakistan` | `landing page price pakistan` | Costs & Budgets |
| 9 | `website-cost-uk` | `how much does a website cost uk` | Costs & Budgets |
| 10 | `website-cost-dubai` | `website development cost dubai` | Costs & Budgets |
| 11 | `website-redesign-cost` | `website redesign cost` | Costs & Budgets |
| 12 | `why-website-quotes-vary` | `why website prices vary` | Costs & Budgets |
| 13 | `how-to-choose-web-development-company` | `how to choose web development company` | Hiring a Developer |
| 14 | `best-web-development-company-lahore` | `best web development company in lahore` | Hiring a Developer |
| 15 | `freelancer-vs-agency-vs-software-house` | `freelancer vs agency website` | Hiring a Developer |
| 16 | `website-development-contract-checklist` | `website development contract` | Hiring a Developer |
| 17 | `who-owns-your-website` | `who owns my website` | Hiring a Developer |
| 18 | `fixed-price-vs-hourly-web-development` | `fixed price vs hourly web development` | Hiring a Developer |
| 19 | `website-brief-template` | `website brief template` | Hiring a Developer |
| 20 | `web-developer-portfolio-red-flags` | `check web developer portfolio` | Hiring a Developer |
| 21 | `website-milestone-payments` | `website advance payment` | Hiring a Developer |
| 22 | `website-handover-checklist` | `website handover checklist` | Hiring a Developer |
| 23 | `wordpress-vs-shopify-vs-custom-website` | `wordpress vs shopify` | Platforms & Comparisons |
| 24 | `shopify-vs-woocommerce-pakistan` | `shopify vs woocommerce pakistan` | Platforms & Comparisons |
| 25 | `wix-vs-custom-website-pakistan` | `wix vs custom website` | Platforms & Comparisons |
| 26 | `nextjs-vs-wordpress` | `nextjs vs wordpress` | Platforms & Comparisons |
| 27 | `laravel-vs-nodejs-web-apps` | `laravel vs node` | Platforms & Comparisons |
| 28 | `website-or-mobile-app-first` | `website or app for business` | Platforms & Comparisons |
| 29 | `pwa-vs-native-app-pakistan` | `pwa vs native app` | Platforms & Comparisons |
| 30 | `headless-cms-vs-wordpress` | `headless cms vs wordpress` | Platforms & Comparisons |
| 31 | `template-vs-custom-website-design` | `template vs custom website` | Platforms & Comparisons |
| 32 | `best-hosting-for-pakistan-websites` | `best hosting for pakistan website` | Platforms & Comparisons |
| 33 | `start-online-store-pakistan` | `start online store pakistan` | E-commerce in Pakistan |
| 34 | `payment-gateways-pakistan-compared` | `payment gateway pakistan` | E-commerce in Pakistan |
| 35 | `stripe-paypal-pakistan-website` | `stripe pakistan alternative` | E-commerce in Pakistan |
| 36 | `raast-bank-transfer-website-payments` | `raast payment integration` | E-commerce in Pakistan |
| 37 | `cod-website-fake-orders-pakistan` | `cod website pakistan` | E-commerce in Pakistan |
| 38 | `courier-integration-online-store-pakistan` | `courier api integration pakistan` | E-commerce in Pakistan |
| 39 | `daraz-vs-own-website` | `daraz vs own website` | E-commerce in Pakistan |
| 40 | `instagram-whatsapp-shop-to-website` | `instagram shop to website` | E-commerce in Pakistan |
| 41 | `product-page-checklist-pakistan` | `product page best practices` | E-commerce in Pakistan |
| 42 | `clothing-brand-website-pakistan` | `clothing brand website pakistan` | E-commerce in Pakistan |
| 43 | `dropshipping-website-pakistan` | `dropshipping website pakistan` | E-commerce in Pakistan |
| 44 | `multi-vendor-marketplace-website-cost` | `multi vendor marketplace development` | E-commerce in Pakistan |
| 45 | `clinic-website-design-pakistan` | `clinic website design pakistan` | Websites by Industry |
| 46 | `dental-clinic-website` | `dental clinic website` | Websites by Industry |
| 47 | `law-firm-website-design-pakistan` | `law firm website design pakistan` | Websites by Industry |
| 48 | `school-website-design-pakistan` | `school website design pakistan` | Websites by Industry |
| 49 | `restaurant-website-online-ordering-pakistan` | `restaurant website online ordering pakistan` | Websites by Industry |
| 50 | `real-estate-website-pakistan` | `real estate website pakistan` | Websites by Industry |
| 51 | `exporter-website-b2b-pakistan` | `export company website` | Websites by Industry |
| 52 | `b2b-catalogue-website-manufacturers` | `b2b catalogue website` | Websites by Industry |
| 53 | `salon-spa-booking-website` | `salon booking website` | Websites by Industry |
| 54 | `gym-website-pakistan` | `gym website pakistan` | Websites by Industry |
| 55 | `pharmacy-website-pakistan` | `pharmacy website pakistan` | Websites by Industry |
| 56 | `travel-agency-website-pakistan` | `travel agency website pakistan` | Websites by Industry |
| 57 | `construction-company-website` | `construction company website` | Websites by Industry |
| 58 | `ngo-donation-website-pakistan` | `ngo website pakistan` | Websites by Industry |
| 59 | `hotel-guest-house-booking-website` | `hotel website booking engine` | Websites by Industry |
| 60 | `logistics-company-website` | `logistics company website` | Websites by Industry |
| 61 | `web-development-company-karachi` | `web development company karachi` | Local Guides |
| 62 | `web-development-company-islamabad` | `web development company islamabad` | Local Guides |
| 63 | `website-design-sialkot-exporters` | `website design sialkot` | Local Guides |
| 64 | `web-development-faisalabad-textile` | `web development faisalabad` | Local Guides |
| 65 | `website-design-gujranwala-manufacturers` | `website design gujranwala` | Local Guides |
| 66 | `web-development-multan` | `web development multan` | Local Guides |
| 67 | `website-design-peshawar` | `website design peshawar` | Local Guides |
| 68 | `ecommerce-website-lahore-retail-brands` | `ecommerce website lahore` | Local Guides |
| 69 | `clinic-website-lahore` | `clinic website lahore` | Local Guides |
| 70 | `website-designer-near-me-lahore` | `website designer near me` | Local Guides |
| 71 | `hire-pakistani-web-developers` | `hire pakistani web developers` | Working With Overseas Clients |
| 72 | `white-label-web-development-pakistan` | `white label web development` | Working With Overseas Clients |
| 73 | `dedicated-developer-vs-fixed-project` | `dedicated developer model` | Working With Overseas Clients |
| 74 | `offshore-team-time-zones-lahore` | `offshore team time zone` | Working With Overseas Clients |
| 75 | `outsourcing-website-ip-nda-code-ownership` | `outsourcing contract ip ownership` | Working With Overseas Clients |
| 76 | `pay-web-developer-in-pakistan` | `pay developer in pakistan` | Working With Overseas Clients |
| 77 | `arabic-rtl-website-development` | `arabic website development` | Working With Overseas Clients |
| 78 | `shopify-developer-uae-saudi` | `shopify developer uae` | Working With Overseas Clients |
| 79 | `uk-small-business-website-offshore` | `web design uk small business` | Working With Overseas Clients |
| 80 | `small-business-website-canada-offshore` | `website for small business canada` | Working With Overseas Clients |
| 81 | `overseas-pakistanis-business-website-setup` | `start business in pakistan from abroad website` | Working With Overseas Clients |
| 82 | `mvp-development-startups` | `mvp development company` | Working With Overseas Clients |
| 83 | `get-business-website-on-google` | `website on google` | Getting Found Online |
| 84 | `google-business-profile-pakistan` | `google business profile pakistan` | Getting Found Online |
| 85 | `seo-ready-website-checklist` | `seo friendly website development` | Getting Found Online |
| 86 | `ai-search-visibility-for-business` | `ai search visibility for business` | Getting Found Online |
| 87 | `schema-markup-business-websites` | `schema markup for business websites` | Getting Found Online |
| 88 | `website-speed-pakistan-mobile` | `website speed optimization` | Getting Found Online |
| 89 | `website-visitors-no-enquiries` | `website no enquiries` | Getting Found Online |
| 90 | `whatsapp-button-website-leads` | `whatsapp button website` | Getting Found Online |
| 91 | `website-hacked-what-to-do` | `website hacked what to do` | Fix a Problem |
| 92 | `website-security-checklist-small-business` | `website security checklist` | Fix a Problem |
| 93 | `website-down-check` | `website down check` | Fix a Problem |
| 94 | `new-website-without-losing-google-traffic` | `website redesign without losing traffic` | Fix a Problem |
| 95 | `website-slow-on-mobile` | `website slow on mobile` | Fix a Problem |
| 96 | `website-backups-small-business` | `website backup` | Fix a Problem |
| 97 | `how-long-to-build-a-website` | `how long to build a website` | Planning & Launch |
| 98 | `pages-for-small-business-website` | `pages for business website` | Planning & Launch |
| 99 | `website-accessibility-basics` | `website accessibility basics` | Planning & Launch |
| 100 | `website-launch-checklist` | `website launch checklist` | Planning & Launch |
| 101 | `website-developer-allama-iqbal-town-lahore` | `website developer iqbal town lahore` | Local Guides |
| 102 | `website-designer-wahdat-road-awan-town` | `website designer wahdat road` | Local Guides |
| 103 | `website-design-samanabad-lahore` | `website design samanabad` | Local Guides |
| 104 | `web-development-company-johar-town` | `web development company johar town` | Local Guides |
| 105 | `website-design-model-town-lahore` | `website design model town lahore` | Local Guides |
| 106 | `web-design-gulberg-lahore` | `web design gulberg lahore` | Local Guides |
| 107 | `website-developer-dha-lahore` | `website developer dha lahore` | Local Guides |
| 108 | `website-design-bahria-town-lahore` | `website design bahria town lahore` | Local Guides |
| 109 | `website-for-hall-road-electronics-traders` | `hall road shop website` | Local Guides |
| 110 | `website-for-anarkali-ichhra-retailers` | `anarkali shop website` | Local Guides |
| 111 | `website-for-sundar-industrial-estate-manufacturers` | `manufacturer website lahore` | Local Guides |
| 112 | `lahore-web-design-prices-by-area` | `web design prices lahore` | Local Guides |
| 113 | `ai-chatbot-for-business-website-cost-pakistan` | `ai chatbot for website pakistan` | AI and Automation |
| 114 | `whatsapp-business-api-cost-pakistan` | `whatsapp business api pakistan` | AI and Automation |
| 115 | `google-ai-mode-small-business-website` | `google ai mode small business` | AI and Automation |
| 116 | `ai-website-builder-vs-web-developer` | `ai website builder vs developer` | AI and Automation |
| 117 | `automate-website-leads-whatsapp-email` | `automate website leads` | AI and Automation |
| 118 | `ai-product-descriptions-online-store` | `ai product descriptions` | AI and Automation |
| 119 | `ai-customer-support-website-build-or-buy` | `ai customer support for website` | AI and Automation |
| 120 | `website-data-privacy-when-using-ai` | `website ai privacy` | AI and Automation |
| 121 | `ai-search-optimisation-checklist-local-business` | `ai search optimisation checklist` | AI and Automation |
| 122 | `school-management-system-cost-pakistan` | `school management system price in pakistan` | Software and Web Apps |
| 123 | `clinic-management-software-pakistan` | `clinic management software pakistan` | Software and Web Apps |
| 124 | `pos-and-inventory-web-app-pakistan` | `pos software price in pakistan` | Software and Web Apps |
| 125 | `booking-system-development-cost` | `online booking system cost` | Software and Web Apps |
| 126 | `lms-for-academies-pakistan` | `lms development pakistan` | Software and Web Apps |
| 127 | `real-estate-crm-pakistan` | `real estate crm pakistan` | Software and Web Apps |
| 128 | `society-management-system-pakistan` | `society management system pakistan` | Software and Web Apps |
| 129 | `distributor-inventory-order-portal` | `dealer order portal` | Software and Web Apps |
| 130 | `customer-portal-development` | `customer portal development` | Software and Web Apps |
| 131 | `saas-product-development-pakistan` | `saas development company pakistan` | Software and Web Apps |
| 132 | `web-app-maintenance-cost` | `web app maintenance cost` | Software and Web Apps |
| 133 | `ecommerce-seo-pakistan-store` | `ecommerce seo pakistan` | E-commerce in Pakistan |
| 134 | `abandoned-cart-recovery-whatsapp` | `abandoned cart recovery` | E-commerce in Pakistan |
| 135 | `eid-sale-website-readiness` | `sale season website readiness` | E-commerce in Pakistan |
| 136 | `shopify-apps-pakistan-stores` | `shopify apps pakistan` | E-commerce in Pakistan |
| 137 | `store-shipping-rates-and-delivery-page` | `shipping policy page` | E-commerce in Pakistan |
| 138 | `return-refund-policy-online-store-pakistan` | `refund policy online store pakistan` | E-commerce in Pakistan |
| 139 | `product-photography-for-online-store` | `product photography for website` | E-commerce in Pakistan |
| 140 | `ga4-ecommerce-tracking-setup` | `ga4 ecommerce tracking` | E-commerce in Pakistan |
| 141 | `international-shipping-from-pakistan-store` | `sell internationally from pakistan website` | E-commerce in Pakistan |
| 142 | `wholesale-b2b-store-pakistan` | `wholesale website pakistan` | E-commerce in Pakistan |
| 143 | `migrate-woocommerce-to-shopify-or-back` | `woocommerce to shopify migration` | E-commerce in Pakistan |
| 144 | `website-cost-saudi-arabia` | `website development cost saudi arabia` | Working With Overseas Clients |
| 145 | `website-cost-qatar` | `website design cost qatar` | Working With Overseas Clients |
| 146 | `website-cost-usa-small-business` | `small business website cost usa` | Working With Overseas Clients |
| 147 | `hire-shopify-developer-pakistan` | `hire shopify developer pakistan` | Working With Overseas Clients |
| 148 | `hire-wordpress-developer-pakistan` | `hire wordpress developer pakistan` | Working With Overseas Clients |
| 149 | `agency-overflow-development-partner` | `development partner for agencies` | Working With Overseas Clients |
| 150 | `eu-gdpr-website-checklist-offshore` | `gdpr website checklist` | Working With Overseas Clients |
| 151 | `homepage-content-guide` | `homepage content` | Content and Conversion |
| 152 | `about-us-page-that-builds-trust` | `about us page` | Content and Conversion |
| 153 | `service-page-structure` | `service page structure` | Content and Conversion |
| 154 | `show-prices-on-website-or-not` | `show prices on website` | Content and Conversion |
| 155 | `reviews-testimonials-on-website` | `testimonials on website` | Content and Conversion |
| 156 | `stock-photos-vs-real-photos` | `stock photos vs real photos` | Content and Conversion |
| 157 | `urdu-english-bilingual-website` | `bilingual website urdu english` | Content and Conversion |
| 158 | `contact-forms-that-convert` | `contact form best practices` | Content and Conversion |
| 159 | `trust-signals-for-small-business-website` | `website trust signals` | Content and Conversion |
| 160 | `website-copywriting-cost-pakistan` | `website content writing pakistan` | Content and Conversion |
| 161 | `transfer-domain-to-new-registrar` | `transfer domain name` | Fix a Problem |
| 162 | `move-website-to-new-hosting` | `move website to new host` | Fix a Problem |
| 163 | `business-email-on-own-domain-pakistan` | `business email pakistan` | Fix a Problem |
| 164 | `email-going-to-spam-fix` | `emails going to spam` | Fix a Problem |
| 165 | `ssl-certificate-https-explained` | `ssl certificate for website` | Fix a Problem |
| 166 | `cloudflare-for-small-business-website` | `cloudflare for small business` | Fix a Problem |
| 167 | `website-uptime-monitoring` | `website uptime monitoring` | Fix a Problem |
| 168 | `wordpress-updates-safely` | `update wordpress safely` | Fix a Problem |
| 169 | `too-many-wordpress-plugins` | `too many wordpress plugins` | Fix a Problem |
| 170 | `hosting-renewal-price-traps` | `hosting renewal cost` | Fix a Problem |
| 171 | `wordpress-vs-webflow` | `wordpress vs webflow` | Platforms & Comparisons |
| 172 | `wix-vs-wordpress` | `wix vs wordpress` | Platforms & Comparisons |
| 173 | `free-website-vs-paid-website` | `free website vs paid website` | Platforms & Comparisons |
| 174 | `custom-code-vs-no-code-website` | `custom code vs no code` | Platforms & Comparisons |
| 175 | `flutter-vs-react-native-vs-pwa` | `flutter vs react native` | Platforms & Comparisons |
| 176 | `shopify-vs-daraz-storefront` | `shopify vs daraz` | Platforms & Comparisons |
| 177 | `website-discovery-meeting-what-to-expect` | `website discovery meeting` | Hiring a Developer |
| 178 | `how-to-give-website-design-feedback` | `website design feedback` | Hiring a Developer |
| 179 | `website-change-requests-cost` | `website change request` | Hiring a Developer |
| 180 | `website-testing-before-sign-off` | `website user acceptance testing` | Hiring a Developer |
| 181 | `website-maintenance-contract-checklist` | `website maintenance contract` | Hiring a Developer |
| 182 | `website-project-delays-why` | `website project delays` | Hiring a Developer |
| 183 | `non-technical-owner-managing-developer` | `manage web developer` | Hiring a Developer |
| 184 | `taking-over-website-from-old-developer` | `take over website from developer` | Hiring a Developer |
| 185 | `architect-interior-designer-website` | `interior designer website` | Websites by Industry |
| 186 | `wedding-event-planner-website` | `wedding planner website` | Websites by Industry |
| 187 | `photographer-portfolio-website` | `photographer website` | Websites by Industry |
| 188 | `car-rental-website-pakistan` | `car rental website pakistan` | Websites by Industry |
| 189 | `tuition-academy-website` | `academy website pakistan` | Websites by Industry |
| 190 | `furniture-brand-online-store` | `furniture website pakistan` | Websites by Industry |
| 191 | `jewellery-store-website-pakistan` | `jewellery website pakistan` | Websites by Industry |
| 192 | `home-bakery-cafe-website` | `bakery website` | Websites by Industry |
| 193 | `printing-press-website` | `printing press website` | Websites by Industry |
| 194 | `immigration-consultant-website` | `study abroad consultant website` | Websites by Industry |
| 195 | `software-house-own-website` | `software house website` | Websites by Industry |
| 196 | `website-budget-planner-first-year` | `website budget` | Planning & Launch |
| 197 | `when-to-upgrade-your-website` | `when to upgrade website` | Planning & Launch |
| 198 | `website-roi-small-business` | `website roi` | Planning & Launch |
| 199 | `google-ads-landing-page-pakistan` | `google ads landing page` | Planning & Launch |
| 200 | `meta-ads-to-website-or-whatsapp` | `meta ads website or whatsapp` | Planning & Launch |

**Cluster pillars** (every spoke puts its pillar in `related`):

| Cluster | Pillar |
|---|---|
| V | #201 |
| W | #226 |
| Y | #258 |
| X | #1 |
| Z | #101 |
| AA | #14 |
| AB | #23 |

Pillars #1, #14, #23 and #101 are already published.

**Cluster V: Websites by profession (Lahore).** Tax-site pattern: 'tax consultant for doctors in Lahore'. Here: one page per profession NOT already covered by clusters E and T. Each must show what that profession's customers search for, the pages and features it needs, and a package from P. Lahore is the main market; mention we work across Pakistan remotely.

**Cluster W: Your situation: specific starting points.** Tax-site pattern: 'return filing when you resigned mid-year'. Here: one page per real situation a business owner is in. Each gives the exact path for that situation, not a general guide.

**Cluster X: Charges and price checks.** Tax-site pattern: 'wealth-statement-filing-charges-pakistan'. Here: exact price pages for small, specific jobs. Quote our own price only when it exists in P; otherwise explain what drives cost and give sourced third-party prices with dates. Never invent a rate.

**Cluster Y: Roman Urdu guides.** Tax-site pattern: Roman Urdu slugs and titles for how people actually type. Title and H1 in Roman Urdu; body in simple Roman Urdu with English technical words; FAQs in Roman Urdu. Same structure, sources and audit rules. Never duplicate an English post's primary keyword.

**Cluster Z: Support, availability and working with us.** Tax-site pattern: 'weekend tax consultant availability'. Only state what is true: office hours Monday to Saturday 9:00 AM to 6:00 PM, Friday 9:00 AM to 12:30 PM, Sunday closed. Never claim 24/7 or guaranteed response times.

**Cluster AA: More Pakistani cities (with real local angles).** Tax-site pattern: 'income-tax-filing-<city>' for 100+ cities. We only add cities with a genuine business angle and say plainly that we work remotely from Lahore. Each must include at least 3 real local business facts and no shared paragraphs.

**Cluster AB: This or that: everyday choices.** Tax-site pattern: '-vs-' comparison pages. Short, decisive comparisons for choices small owners face. Fair, with a clear 'choose X if' table.

### Part 1: posts #201–#220

| # | Slug (exact) | File prefix | Category | Topic and angle | Primary keyword | Cluster seeds (expand to 5–8) | Intent | Aud | Link | Must include |
|---|---|---|---|---|---|---|---|---|---|---|
| 201 | `website-for-solar-installers-pakistan` | `v201_` | Websites by Profession | Website for Solar Installers: Quotes, Projects and Net-Metering Enquiries (PILLAR) | `solar company website pakistan` | solar installer website lahore; solar panel company website design; solar quotation form website; solar business website | C | PK | /digital/business-websites | Quote calculator form, project gallery with system sizes, brands carried, after-sales; link all V posts |
| 202 | `online-quran-academy-website` | `v202_` | Websites by Profession | Online Quran Academy Website: Trial Classes, Time Zones and Fees | `online quran academy website` | quran teaching website; online quran classes website design; quran academy for overseas students | C | PK/OS | /digital/web-app-development | Overseas students, time-zone class schedules, trial booking, payments from abroad, female tutors page |
| 203 | `hostel-website-lahore` | `v203_` | Websites by Profession | Hostel Website for Lahore Girls' and Boys' Hostels: Rooms, Rules and Bookings | `hostel website lahore` | girls hostel website; hostel booking website pakistan; student hostel website design | C | PK | /digital/business-websites | Room types, safety and rules, location near universities, visit booking, parents' trust |
| 204 | `marquee-wedding-hall-website` | `v204_` | Websites by Profession | Marquee and Wedding Hall Website: Dates, Packages and Virtual Tours | `wedding hall website` | marquee website lahore; banquet hall website design; event venue booking website | C | PK | /digital/web-app-development | Availability calendar, package menus, capacity, photo/video tours, booking deposit |
| 205 | `catering-company-website` | `v205_` | Websites by Profession | Catering Company Website: Menus, Per-Head Pricing and Event Enquiries | `catering website pakistan` | caterers website lahore; catering business website design; event catering menu website | C | PK | /digital/business-websites | Per-head menu builder, event types, tasting booking, food-safety note |
| 206 | `home-services-website-ac-electrician` | `v206_` | Websites by Profession | Website for Home Services: AC Repair, Electricians and Plumbers | `home services website pakistan` | ac repair website; electrician website lahore; plumber website design | C | PK | /digital/business-websites | Service areas map, call/WhatsApp first, booking slots, pricing ranges, reviews |
| 207 | `diagnostic-lab-website` | `v207_` | Websites by Profession | Diagnostic Lab Website: Test Prices, Home Sampling and Reports Online | `diagnostic lab website` | laboratory website pakistan; online lab reports website; home sample collection booking | C | PK | /digital/web-app-development | Test catalogue, home-sampling booking, secure report download, privacy; regulator note |
| 208 | `veterinary-clinic-website` | `v208_` | Websites by Profession | Veterinary Clinic Website: Appointments, Pet Services and Emergencies | `veterinary clinic website` | vet clinic website lahore; pet clinic website design; pet grooming booking website | C | PK | /digital/business-websites | Appointment booking, emergency hours, services, pet shop add-on |
| 209 | `optician-eyewear-store-website` | `v209_` | Websites by Profession | Optician and Eyewear Store Website: Frames, Prescriptions and Try-On | `eyewear store website` | optician website pakistan; glasses online store; spectacles shop website | C | PK | /digital/ecommerce-development | Frame catalogue, prescription upload, eye-test booking, privacy |
| 210 | `physiotherapy-clinic-website` | `v210_` | Websites by Profession | Physiotherapy Clinic Website: Conditions, Sessions and Home Visits | `physiotherapy clinic website` | physiotherapist website lahore; physio home visit booking | C | PK | /digital/business-websites | Condition pages written carefully, session booking, home visits, regulator note |
| 211 | `psychologist-therapist-website` | `v211_` | Websites by Profession | Psychologist and Therapist Website: Privacy-First Booking | `psychologist website` | therapist website pakistan; counselling website design; online therapy booking | C | PK/OS | /digital/business-websites | Confidential enquiry forms, online sessions, careful claims, privacy section |
| 212 | `nutritionist-dietitian-website` | `v212_` | Websites by Profession | Nutritionist and Dietitian Website: Plans, Consultations and Payments | `dietitian website` | nutritionist website pakistan; diet plan website; online diet consultation | C | PK/OS | /digital/business-websites | Plan pages, online consultations, payments, no health-outcome claims |
| 213 | `montessori-daycare-website` | `v213_` | Websites by Profession | Montessori and Daycare Website: Admissions, Safety and Parent Updates | `montessori website` | daycare website lahore; preschool website design; montessori admission form | C | PK | /digital/business-websites | Admissions, safety and staff info, gallery consent, parent communication |
| 214 | `driving-school-website` | `v214_` | Websites by Profession | Driving School Website: Course Packages, Slots and Female Instructors | `driving school website` | driving school lahore website; driving lessons booking | C | PK | /digital/web-app-development | Packages, slot booking, licence-process info linking to official sources only |
| 215 | `car-showroom-used-car-dealer-website` | `v215_` | Websites by Profession | Car Showroom and Used Car Dealer Website: Stock, Inspections and Leads | `car dealer website pakistan` | used car showroom website; car dealership website lahore | C | PK | /digital/web-app-development | Stock listings with filters, inspection reports, finance enquiry, WhatsApp leads; no vehicle tax content |
| 216 | `auto-workshop-website` | `v216_` | Websites by Profession | Auto Workshop and Car Service Website: Booking and Price Lists | `car workshop website` | auto repair website lahore; car service booking website | C | PK | /digital/business-websites | Service menu, booking, pick-and-drop, before/after photos |
| 217 | `cctv-security-installer-website` | `v217_` | Websites by Profession | CCTV and Security Installer Website: Packages, Site Surveys and Support | `cctv company website` | security system installer website; cctv installation lahore website | C | PK | /digital/business-websites | Package comparison, site-survey booking, brands, support plans |
| 218 | `pest-control-company-website` | `v218_` | Websites by Profession | Pest Control Company Website: Services, Safety and Fast Bookings | `pest control website` | fumigation company website lahore; termite control website | C | PK | /digital/business-websites | Service pages, safety info, booking, commercial contracts |
| 219 | `tile-sanitary-showroom-website` | `v219_` | Websites by Profession | Tile and Sanitary Showroom Website: Catalogue, Brands and Dealer Prices | `tiles showroom website` | sanitary store website pakistan; tile catalogue website | C | PK | /digital/ecommerce-development | Large catalogue, price on request, showroom visit, contractor accounts |
| 220 | `mobile-repair-shop-website` | `v220_` | Websites by Profession | Mobile Repair Shop Website: Repair Prices, Bookings and Warranty | `mobile repair website` | phone repair shop website lahore; mobile repair booking | C | PK | /digital/business-websites | Repair price table by model, booking, warranty terms, pickup |

### Part 2: posts #221–#240

| # | Slug (exact) | File prefix | Category | Topic and angle | Primary keyword | Cluster seeds (expand to 5–8) | Intent | Aud | Link | Must include |
|---|---|---|---|---|---|---|---|---|---|---|
| 221 | `tailor-made-to-measure-website` | `v221_` | Websites by Profession | Tailor and Made-to-Measure Website: Measurements and Online Orders | `tailor website` | boutique stitching website; online tailoring pakistan; measurement form website | C | PK | /digital/ecommerce-development | Measurement forms, fabric choice, delivery dates, WhatsApp follow-up |
| 222 | `bridal-makeup-artist-website` | `v222_` | Websites by Profession | Bridal Makeup Artist Website: Portfolio, Packages and Date Booking | `makeup artist website` | bridal makeup website lahore; salon bridal package website | C | PK | /digital/business-websites | Portfolio with consent, packages, date booking with deposit |
| 223 | `it-training-institute-website` | `v223_` | Websites by Profession | IT Training Institute Website: Courses, Batches and Admissions | `training institute website` | computer institute website lahore; course registration website | C | PK | /digital/web-app-development | Course pages, batch schedules, registration and fee payment; no job-guarantee claims |
| 224 | `packers-movers-website` | `v224_` | Websites by Profession | Packers and Movers Website: Quotes, Routes and Trust | `packers and movers website` | moving company website pakistan; house shifting website | C | PK | /digital/business-websites | Quote form by volume and route, insurance info only if real, reviews |
| 225 | `printing-and-signage-shop-website` | `v225_` | Websites by Profession | Signage and Panaflex Shop Website: Quotes and Project Gallery | `signage company website` | panaflex printing website lahore; sign board company website | C | PK | /digital/business-websites | Quote by size, gallery, site measurement booking; distinct from #194 printing press |
| 226 | `website-when-you-only-sell-on-whatsapp` | `w226_` | Planning & Launch | You Only Sell on WhatsApp: When and How to Add a Website (PILLAR) | `whatsapp business to website` | whatsapp only business; sell on whatsapp and website; whatsapp catalogue to website | C | PK | /digital/business-websites | Decision guide, keeping WhatsApp at the centre, step plan, cost; link all W posts |
| 227 | `website-without-logo-or-brand` | `w227_` | Planning & Launch | No Logo or Brand Yet? How to Start Your Website Anyway | `website without logo` | need logo before website; logo and website together; start website no branding | I | PK | /digital/business-websites | What you need minimum, temporary wordmark, when to invest in branding |
| 228 | `urgent-website-in-one-week` | `w228_` | Planning & Launch | Need a Website in One Week? What Is Realistic | `urgent website` | website in 7 days; fast website development; quick website lahore | C | PK/OS | /digital/business-websites | What can be done in a week (landing page), what cannot, honest timeline |
| 229 | `website-under-25000-rupees` | `w229_` | Planning & Launch | What Can You Get for a Website Under Rs 25,000? | `website under 25000` | cheap website pakistan; low budget website; website kam budget mein | C | PK | /digital/pricing | Honest options (one-page, builder, freelancer) and their limits; our P['landing'] |
| 230 | `developer-disappeared-mid-project` | `w230_` | Planning & Launch | Your Developer Disappeared Mid-Project: What to Do Now | `developer disappeared` | web developer not responding; freelancer ran away with money; unfinished website | I | PK/OS | /digital/contact | Recover accounts, assess work done, restart plan; link #17 #184 |
| 231 | `website-not-showing-on-google` | `w231_` | Planning & Launch | Website Not Showing on Google After Launch? Causes and Fixes | `new website not on google` | site not indexed; website not in google search; new website not appearing | I | PK/OS | /digital/business-websites | Search Console checks, noindex, robots, sitemap, time to index; distinct from #83 |
| 232 | `google-site-may-be-hacked-warning` | `w232_` | Planning & Launch | Google Says 'This Site May Be Hacked': How to Remove the Warning | `this site may be hacked` | remove hacked warning google; google security issues report; site hacked warning | I | PK/OS | /digital/pricing | Security Issues report, cleanup, review request; distinct from #91 |
| 233 | `rebrand-website-after-business-name-change` | `w233_` | Planning & Launch | Changed Your Business Name? Rebranding Your Website Without Losing Customers | `rebrand website` | business name change website; new domain after rebrand; rebranding seo | I | PK/OS | /digital/business-websites | Domain change, redirects, profiles, announcements; link #94 |
| 234 | `switch-com-to-pk-domain` | `w234_` | Planning & Launch | Switching From .com to .pk (or Back): Is It Worth It? | `change domain extension` | move from .com to .pk; .pk vs .com switch; change website domain seo | C | PK | /digital/pricing | SEO risks, redirects, email, PKNIC facts; link #7 |
| 235 | `add-online-payments-to-existing-website` | `w235_` | Planning & Launch | Adding Online Payments to Your Existing Website | `add payment gateway to website` | accept payments on existing website; jazzcash on wordpress site; payment integration existing site | C | PK | /digital/ecommerce-development | Options by platform, gateway onboarding, testing; link #34 |
| 236 | `add-urdu-to-english-website` | `w236_` | Planning & Launch | Adding Urdu to an Existing English Website | `add urdu to website` | translate website to urdu; urdu version of website; multilingual wordpress urdu | C | PK | /digital/business-websites | Plugins vs separate pages, RTL, hreflang, translation quality; link #157 |
| 237 | `add-blog-to-business-website` | `w237_` | Planning & Launch | Adding a Blog to Your Business Website: Is It Worth It? | `add blog to website` | business blog benefits; blog for small business seo; should my website have a blog | C | PK/OS | /digital/business-websites | When a blog helps, topics that bring buyers, time cost; honest about AI Mode |
| 238 | `multi-location-business-website` | `w238_` | Planning & Launch | Website for a Business With Several Branches or Cities | `multi location website` | branch pages website; multiple locations seo; franchise website structure | C | PK | /digital/business-websites | Branch pages that are not doorways, Google Business Profiles per branch, schema |
| 239 | `franchise-website-structure` | `w239_` | Planning & Launch | Franchise Website: One Brand, Many Owners | `franchise website` | franchise business website pakistan; franchise locator website | C | PK | /digital/web-app-development | Central vs local content, store locator, lead routing to franchisees |
| 240 | `home-based-business-website` | `w240_` | Planning & Launch | Website for a Home-Based Business: Privacy, Trust and Delivery | `home based business website` | ghar se business website; home business online pakistan; women home business website | C | PK | /digital/business-websites | Keeping home address private, trust signals, delivery and COD |

### Part 3: posts #241–#260

| # | Slug (exact) | File prefix | Category | Topic and angle | Primary keyword | Cluster seeds (expand to 5–8) | Intent | Aud | Link | Must include |
|---|---|---|---|---|---|---|---|---|---|---|
| 241 | `student-startup-first-website` | `w241_` | Planning & Launch | Student Startup's First Website: What to Build on a Small Budget | `startup website` | first website for startup; student business website; startup landing page pakistan | C | PK | /digital/business-websites | Landing page first, validation, what to postpone; link #82 |
| 242 | `phone-only-bookings-to-online` | `w242_` | Planning & Launch | Taking Bookings Only by Phone? Moving to Online Booking Step by Step | `online booking for small business` | phone bookings to online; appointment booking website small business | C | PK | /digital/web-app-development | Hybrid phone + online, reminders, staff adoption; link #125 |
| 243 | `split-website-into-two-brands` | `w243_` | Planning & Launch | One Website or Two? When to Split Separate Businesses Online | `separate websites for two businesses` | two brands one website; split website; sub-brand website | C | PK/OS | /digital/business-websites | Decision table, SEO effects, cost; why we keep our web and tax sections separate as a worked example |
| 244 | `second-website-for-export-market` | `w244_` | Planning & Launch | A Second Website for Export Buyers: When It Makes Sense | `export website separate` | international buyer website; separate export site; b2b export website pakistan | C | PK | /digital/business-websites | Language, currency, trust, domain choice; link #51 #142 |
| 245 | `inherited-family-business-website` | `w245_` | Planning & Launch | Taking Over the Family Business: Modernising Its Website | `family business website` | old family business online; modernise family shop website | C | PK | /digital/business-websites | Respecting the old name, account recovery, staged modernisation |
| 246 | `logo-and-website-package-price` | `x246_` | Costs & Budgets | Logo and Website Package Price in Pakistan | `logo and website package` | logo and website price pakistan; branding and website package; logo design with website | C | PK | /digital/pricing | What a package should include, separate vs bundle, our P prices; logo pricing only if sourced |
| 247 | `shopify-store-setup-charges` | `x247_` | Costs & Budgets | Shopify Store Setup Charges in Pakistan: What Is Included | `shopify store setup charges` | shopify setup price pakistan; shopify store design charges | C | PK | /digital/ecommerce-development | Setup scope table, apps and theme costs from Shopify, our P['store']; link #3 |
| 248 | `wordpress-website-fix-charges` | `x248_` | Costs & Budgets | WordPress Website Fix Charges: Errors, Updates and Broken Pages | `wordpress fix charges` | wordpress repair cost pakistan; fix wordpress error price | C | PK/OS | /digital/pricing | What drives cost, hourly vs fixed, our maintenance P['maint'] |
| 249 | `website-speed-optimisation-charges` | `x249_` | Costs & Budgets | Website Speed Optimisation Charges: What You Pay For | `website speed optimization price` | page speed service cost; speed up website charges | C | PK/OS | /digital/pricing | Scope tiers, before/after measurement, avoid 'score-only' work; link #88 #95 |
| 250 | `website-migration-charges` | `x250_` | Costs & Budgets | Website Migration Charges: Moving Hosts or Platforms | `website migration cost` | website transfer charges; platform migration price | C | PK/OS | /digital/pricing | Small vs large migration, risk items, testing; link #162 #143 |
| 251 | `domain-renewal-charges-pakistan` | `x251_` | Costs & Budgets | Domain Renewal Charges in Pakistan: .pk, .com.pk and .com | `domain renewal price pakistan` | pk domain renewal fee; com domain renewal cost | C | PK | /digital/pricing | PKNIC rates (dated), .com registrar renewal from official pages, renewal traps |
| 252 | `ssl-certificate-price-pakistan` | `x252_` | Costs & Budgets | SSL Certificate Price in Pakistan: Free vs Paid | `ssl certificate price pakistan` | paid ssl vs free ssl; ssl cost for website | C | PK | /digital/pricing | Let's Encrypt free, when paid OV/EV matters, official sources; link #166 |
| 253 | `business-email-price-per-user-pakistan` | `x253_` | Costs & Budgets | Business Email Price per User in Pakistan (Google Workspace, Zoho) | `business email price pakistan` | google workspace price per user; zoho mail price pakistan | C | PK | /digital/pricing | Official pricing pages with dates, currency, what you get; distinct from #163 (choice) by focusing on per-user cost |
| 254 | `website-audit-charges` | `x254_` | Costs & Budgets | Website Audit Charges: What a Proper Audit Covers | `website audit cost` | seo audit price pakistan; website review service | C | PK/OS | /digital/contact | Audit scope table, deliverables, what free tools cover |
| 255 | `malware-removal-charges` | `x255_` | Costs & Budgets | Website Malware Removal Charges and What Is Included | `malware removal cost` | hacked website cleanup price; website virus removal | C | PK/OS | /digital/pricing | Cleanup scope, prevention, maintenance link; link #91 #205 |
| 256 | `product-upload-charges-online-store` | `x256_` | Costs & Budgets | Product Upload Charges for Online Stores: Per Item or Per Batch? | `product upload charges` | product listing service pakistan; shopify product upload price | C | PK | /digital/ecommerce-development | What a listing includes (photos, variants, SEO), per-item vs batch, quality checks |
| 257 | `website-urdu-translation-charges` | `x257_` | Costs & Budgets | Website Urdu Translation Charges: Words, Pages and Quality | `website translation urdu cost` | english to urdu website translation price | C | PK | /digital/business-websites | Per-word vs per-page, machine vs human, review step; link #157 #211 |
| 258 | `website-kaise-banwayein` | `y258_` | Roman Urdu Guides | Website Kaise Banwayein? Step by Step Mukammal Guide (PILLAR) | `website kaise banwayein` | website banwane ka tareeqa; apni website kaise banaye; business ki website kaise banti hai | I/C | PK | /digital/business-websites | Qadam ba qadam: maqsad, domain, hosting, design, content, launch; P prices; link all Y posts |
| 259 | `online-store-kaise-banayein` | `y259_` | Roman Urdu Guides | Online Store Kaise Banayein? Pakistan Mein Mukammal Tareeqa | `online store kaise banayein` | online dukaan kaise kholein; ecommerce website kaise banaye | I/C | PK | /digital/ecommerce-development | Products, COD, courier, payment, launch; link #33 |
| 260 | `website-ka-mahana-kharcha` | `y260_` | Roman Urdu Guides | Website Ka Mahana Kharcha Kitna Hota Hai? | `website ka mahana kharcha` | website ki monthly fees; hosting ka kharcha; website chalane ka kharcha | C | PK | /digital/pricing | Domain, hosting, maintenance, email ka saalana/mahana hisaab; link #6 #7 |

### Part 4: posts #261–#280

| # | Slug (exact) | File prefix | Category | Topic and angle | Primary keyword | Cluster seeds (expand to 5–8) | Intent | Aud | Link | Must include |
|---|---|---|---|---|---|---|---|---|---|---|
| 261 | `ghar-baithe-online-business-website` | `y261_` | Roman Urdu Guides | Ghar Baithe Online Business Ke Liye Website | `ghar baithe online business` | ghar se online kaam website; online business shuru karna | C | PK | /digital/business-websites | Privacy, delivery, WhatsApp, chhota budget; no earning promises |
| 262 | `google-maps-par-dukaan-kaise-add-karein` | `y262_` | Roman Urdu Guides | Google Maps Par Apni Dukaan Kaise Add Karein? | `google maps par dukaan` | google map par business add karna; google business profile kaise banaye | I | PK | /digital/web-development-lahore | Business Profile steps (official), verification; link #84 |
| 263 | `whatsapp-se-order-wali-website` | `y263_` | Roman Urdu Guides | WhatsApp Se Order Lene Wali Website Kaise Banwayein? | `whatsapp se order wali website` | whatsapp par order lene wali website; whatsapp button website par | C | PK | /digital/business-websites | Order button, catalogue, pre-filled messages; link #90 #201 |
| 264 | `domain-kya-hota-hai` | `y264_` | Roman Urdu Guides | Domain Kya Hota Hai Aur Kaise Lein? | `domain kya hota hai` | domain name kaise kharidein; .pk domain kaise lein | I | PK | /digital/pricing | Asaan wazahat, PKNIC rates (dated), apne naam par register karna |
| 265 | `hosting-kya-hoti-hai` | `y265_` | Roman Urdu Guides | Hosting Kya Hoti Hai? Kaunsi Hosting Lein? | `hosting kya hoti hai` | web hosting kya hai; sasti hosting pakistan | I | PK | /digital/pricing | Asaan wazahat, shared vs VPS, renewal ka dhoka; link #32 |
| 266 | `website-aur-app-mein-farq` | `y266_` | Roman Urdu Guides | Website Aur App Mein Kya Farq Hai? Pehle Kya Banwayein? | `website aur app mein farq` | app ya website; mobile app banwana chahiye | I/C | PK | /digital/web-app-development | Asaan comparison table; link #28 |
| 267 | `shopify-store-kaise-banayein` | `y267_` | Roman Urdu Guides | Shopify Store Kaise Banayein? Pakistan Ke Liye Guide | `shopify store kaise banaye` | shopify par dukaan kholna; shopify pakistan mein kaise chalayein | I/C | PK | /digital/ecommerce-development | Plan, COD, apps, payments ki haqeeqat; link #3 |
| 268 | `jazzcash-easypaisa-website-par` | `y268_` | Roman Urdu Guides | JazzCash Aur Easypaisa Website Par Kaise Lagayein? | `jazzcash website par` | easypaisa payment website; online payment website par lagana | I | PK | /digital/ecommerce-development | Merchant account, documents (sirf official), testing; link #34 |
| 269 | `website-ki-seo-kaise-karein` | `y269_` | Roman Urdu Guides | Apni Website Ki SEO Kaise Karein? Shuruati Guide | `website ki seo kaise karein` | seo kaise karte hain; google par website upar kaise laye | I | PK | /digital/business-websites | Basics, Search Console, content; no ranking promises; link #85 |
| 270 | `saturday-website-support-lahore` | `z270_` | Working With Us | Website Help on Saturdays in Lahore: When We Are Open | `saturday website support lahore` | weekend web developer lahore; website support saturday | L/T | PK | /digital/web-development-lahore | Exact hours, Sunday closed, how to reach us, what to do on Sunday |
| 271 | `urgent-website-fix-same-day` | `z271_` | Working With Us | Urgent Website Problem? How We Handle Same-Day Requests | `urgent website fix` | website down urgent help; same day website repair lahore | T | PK/OS | /digital/pricing | Triage process, what can be fixed fast, honest no-promise wording; link #93 |
| 272 | `overseas-client-support-hours` | `z272_` | Working With Us | Support Hours for Overseas Clients: UK, Gulf and North America | `website support overseas clients` | offshore support hours; developer support time zone | I | OS | /digital/contact | Overlap table from UTC+5, email/WhatsApp routes; link #74 |
| 273 | `online-meeting-or-office-visit` | `z273_` | Working With Us | Online Meeting or Office Visit: Choosing How to Start Your Project | `web developer meeting online` | video call web designer; meet web developer office lahore | I | PK/OS | /digital/contact | What each suits, how to book, what to bring; link #177 |
| 274 | `website-support-in-urdu` | `z274_` | Working With Us | Website Support in Urdu and Punjabi: Talk to Us in Your Language | `website support urdu` | urdu speaking web developer; web designer urdu support | T | PK/OS | /digital/contact | Languages we use, written scopes in English and Urdu, training in Urdu |
| 275 | `website-design-sargodha` | `aa275_` | Local Guides | Website Design for Sargodha Businesses: Citrus, Agri and Retail | `website design sargodha` | web developer sargodha; kinnow export website | L/C | PK | /digital/business-websites | Kinnow/citrus exporters, agri dealers, education; remote working |
| 276 | `website-design-bahawalpur` | `aa276_` | Local Guides | Website Design for Bahawalpur Businesses | `website design bahawalpur` | web developer bahawalpur; bahawalpur business website | L/C | PK | /digital/business-websites | Agri, cotton, education, tourism (Derawar Fort area), remote working |
| 277 | `website-design-sahiwal` | `aa277_` | Local Guides | Website Design for Sahiwal Businesses: Dairy, Agri and Clinics | `website design sahiwal` | web developer sahiwal; dairy business website | L/C | PK | /digital/business-websites | Dairy and livestock, agri dealers, clinics |
| 278 | `website-design-kasur-khussa-leather` | `aa278_` | Local Guides | Kasur Businesses Online: Khussa, Leather and Food Brands | `website design kasur` | kasur khussa online store; leather business website kasur | L/C | PK | /digital/ecommerce-development | Khussa makers, leather tanneries, Kasur food brands; close to Lahore office |
| 279 | `website-design-gujrat-furniture-fans` | `aa279_` | Local Guides | Gujrat Manufacturers Online: Furniture and Fans | `website design gujrat` | gujrat furniture website; fan manufacturer website gujrat | L/C | PK | /digital/business-websites | Furniture and electric fan industry, dealer networks, overseas families |
| 280 | `website-design-wazirabad-cutlery` | `aa280_` | Local Guides | Wazirabad Cutlery Makers: Websites for Export Buyers | `website design wazirabad` | cutlery manufacturer website; knife exporter website pakistan | L/C | PK | /digital/business-websites | Cutlery and knife export, B2B catalogues; link #51 |

### Part 5: posts #281–#300

| # | Slug (exact) | File prefix | Category | Topic and angle | Primary keyword | Cluster seeds (expand to 5–8) | Intent | Aud | Link | Must include |
|---|---|---|---|---|---|---|---|---|---|---|
| 281 | `website-design-chiniot-furniture` | `aa281_` | Local Guides | Chiniot Furniture Workshops: Catalogue Websites That Sell | `chiniot furniture website` | chinioti furniture online; wooden furniture website pakistan | L/C | PK | /digital/ecommerce-development | Carved wood furniture, custom orders, delivery across Pakistan; link #190 |
| 282 | `website-design-sheikhupura` | `aa282_` | Local Guides | Website Design for Sheikhupura Industries and Traders | `website design sheikhupura` | web developer sheikhupura; industrial company website sheikhupura | L/C | PK | /digital/business-websites | Industrial estates near Lahore, rice trade, office visit is close |
| 283 | `website-design-hyderabad-sindh` | `aa283_` | Local Guides | Website Design for Hyderabad Businesses: Bangles, Retail and Clinics | `website design hyderabad pakistan` | web developer hyderabad sindh; bangles business website | L/C | PK | /digital/business-websites | Bangle industry, retail markets, healthcare; remote working |
| 284 | `website-design-sukkur` | `aa284_` | Local Guides | Website Design for Sukkur and Upper Sindh Businesses | `website design sukkur` | web developer sukkur; dates export website | L/C | PK | /digital/business-websites | Dates trade (Khairpur region), agri, retail |
| 285 | `website-design-abbottabad` | `aa285_` | Local Guides | Website Design for Abbottabad: Schools, Hotels and Tourism | `website design abbottabad` | web developer abbottabad; hotel website galiyat | L/C | PK | /digital/business-websites | Schools and colleges, hotels for Galiyat tourism, seasonal demand |
| 286 | `website-design-mardan` | `aa286_` | Local Guides | Website Design for Mardan Businesses | `website design mardan` | web developer mardan; mardan business online | L/C | PK | /digital/business-websites | Agri (tobacco/sugarcane belt), retail, education; Pashto/Urdu customers |
| 287 | `website-design-rahim-yar-khan` | `aa287_` | Local Guides | Website Design for Rahim Yar Khan Businesses | `website design rahim yar khan` | web developer rahim yar khan; agri business website | L/C | PK | /digital/business-websites | Cotton and sugar belt, agri inputs, healthcare |
| 288 | `website-design-jhelum` | `aa288_` | Local Guides | Website Design for Jhelum Businesses and Overseas Families | `website design jhelum` | web developer jhelum; overseas pakistani business jhelum | L/C | PK/OS | /digital/business-websites | Strong overseas links, remittance-funded businesses, remote management; link #81 |
| 289 | `website-design-mirpur-ajk` | `aa289_` | Local Guides | Website Design for Mirpur Businesses Run From the UK | `website design mirpur` | mirpur azad kashmir website; uk pakistani business mirpur | L/C | PK/OS | /digital/business-websites | UK diaspora owners, property and retail, remote management, time zones |
| 290 | `website-vs-facebook-page` | `ab290_` | Platforms & Comparisons | Website vs Facebook Page: Do You Need Both? | `website vs facebook page` | facebook page enough for business; website or facebook | C | PK | /digital/business-websites | Ownership, reach, trust, cost; choose-if table |
| 291 | `website-vs-google-business-profile-only` | `ab291_` | Platforms & Comparisons | Website vs Google Business Profile Alone | `website vs google business profile` | is google business profile enough; gbp without website | C | PK | /digital/web-development-lahore | What GBP does well, where a site adds value; link #84 |
| 292 | `linktree-vs-website` | `ab292_` | Platforms & Comparisons | Link-in-Bio Page vs Your Own Website | `link in bio vs website` | linktree vs website; instagram bio link website | C | PK | /digital/business-websites | Limits of link pages, ownership, SEO; link #40 |
| 293 | `whatsapp-catalogue-vs-online-store` | `ab293_` | Platforms & Comparisons | WhatsApp Catalogue vs Online Store | `whatsapp catalogue vs website` | whatsapp business catalogue limits; whatsapp shop vs ecommerce | C | PK | /digital/ecommerce-development | Product limits, checkout, discovery; choose-if table; link #201 |
| 294 | `free-hosting-vs-paid-hosting` | `ab294_` | Platforms & Comparisons | Free Hosting vs Paid Hosting: The Hidden Costs | `free hosting vs paid hosting` | is free hosting safe; free web hosting pakistan | C | PK | /digital/pricing | Ads, limits, security, ownership; link #170 |
| 295 | `pk-vs-com-pk-domain` | `ab295_` | Platforms & Comparisons | .pk vs .com.pk Domain: Which Should You Register? | `pk vs com.pk` | .com.pk domain; which pk domain to choose | C | PK | /digital/pricing | PKNIC facts (dated), brand and email, register both? |
| 296 | `one-page-vs-multi-page-website` | `ab296_` | Platforms & Comparisons | One-Page Website vs Multi-Page: Which Fits Your Business? | `one page vs multi page website` | single page website pros cons; how many pages website | C | PK/OS | /digital/business-websites | SEO, clarity, cost; choose-if table; link #8 #98 |
| 297 | `website-subscription-vs-one-time-build` | `ab297_` | Platforms & Comparisons | Monthly Website Subscription vs One-Time Build | `website subscription vs one time` | website on monthly payment; rent a website pakistan | C | PK | /digital/pricing | 3-year cost comparison, ownership, exit; our one-time + optional maintenance model |
| 298 | `theme-marketplace-vs-custom-design` | `ab298_` | Platforms & Comparisons | Buying a Ready Theme vs Paying for Custom Design | `buy theme vs custom design` | themeforest theme vs custom; premium theme pakistan | C | PK/OS | /digital/business-websites | Licences, updates, bloat, when a theme is right; link #31 |
| 299 | `canva-website-vs-wordpress` | `ab299_` | Platforms & Comparisons | Canva Website vs WordPress for a Small Business | `canva website vs wordpress` | canva website builder; is canva website good for business | C | PK | /digital/business-websites | Limits, SEO, domain, growth path |
| 300 | `agency-retainer-vs-pay-per-task` | `ab300_` | Platforms & Comparisons | Monthly Retainer vs Pay-Per-Task Website Support | `website retainer vs pay per task` | website support plan vs hourly; maintenance retainer | C | PK/OS | /digital/pricing | Which suits which site, cost scenarios illustrative; link #6 #181 |

---

## 10. Clustering audit (run after each part)

When all posts in the part pass the auditor, check the part as a set and record the results in the report.

1. **Cannibalisation.**
   - Each primary keyword is used by exactly one post.
   - No cluster term equals another post's primary keyword. The auditor checks this across the files in `posts/`.
   - Also compare your primary keywords against the 22 published keywords listed in section 9.
2. **Intent separation.** For posts that look similar, write one sentence each in the report showing how their intent and angle differ. Pairs to check:
   - #24 Shopify vs WooCommerce and #2 e-commerce prices
   - #88 speed strategy and #95 slow-site fixes
   - #45 clinic websites and #69 Lahore clinics
3. **Internal link graph.**
   - Every post links up to its pillar.
   - The pillar links down to at least 5 of its spokes in the body or in `related`.
   - Every post has at least 2 links to siblings.
   - No post is left without an internal link pointing to it inside the part.

   Draw this as a table: post, links out, links in.
4. **Coverage.** For each cluster, list the main sub-questions a buyer has and show which post answers each. Flag any gap.
5. **Uniqueness.** No paragraph or sentence of 15+ words appears in two posts. Check by searching your own files.
6. **Consistency.** Every mention of our prices uses `P`, and every market figure matches section 2.2 or has its own source.

---

## 11. Self-review checklist (every post, before the auditor)

- [ ] **Answer box:** the first sentence answers the question, with the keyword and a number.
- [ ] **Intent:** the post matches its intent code. Commercial posts compare options; informational posts teach.
- [ ] **Body length:** 600–1,300 words for a spoke, 1,000–2,200 for a pillar. Every section adds a fact, number, step or example; nothing is filler.
- [ ] **Structure:**
  - [ ] at least one table
  - [ ] at least one original-value item
  - [ ] a "What we would build for you" section with `P` prices
- [ ] **Pakistan or market detail:** specific and true.
- [ ] **Facts:**
  - [ ] every number has a source or is labelled illustrative
  - [ ] no invented clients, counts or awards
  - [ ] no ranking guarantees
- [ ] **Separation:** no tax words or topics, and no links outside `/digital` except sources.
- [ ] **FAQs:**
  - [ ] real questions, 40–60 word standalone answers
  - [ ] a Roman Urdu FAQ if the audience includes PK
- [ ] **Sources:** 3–9, all opened and working.
- [ ] **Links:** 2+ sibling guide links and 1+ service link in the body; `related` includes the pillar.
- [ ] **Tone:**
  - [ ] plain British English
  - [ ] no banned phrases
  - [ ] honest trade-offs stated
- [ ] **Readability:** the post reads well on a phone, with short paragraphs (2–4 sentences) and tables of 4 columns or fewer.

---

## 12. Part report (`PART-N-REPORT.md`), delivered with each zip

1. **Auditor output:** the full output of `python3 audit_posts.py posts`. It must end with `0 failing`.
2. **Post table:** #, slug, primary keyword, body words, FAQs, sources, and the original-value item.
3. **Fact log:** every numeric or factual claim from a third party, as claim | post | source URL | date checked.
4. **Illustrative examples:** one line each.
5. **New source URLs** not in the approved list, each with the date it was opened.
6. **Clustering audit:** the results of section 10, points 1–6.
7. **Open questions:** anything you were unsure about. Flag rather than guess.

---

## 13. What happens after delivery

The Kamboh Associates Digital team audits every part before publishing:
- re-runs the auditor
- builds the pages and runs the site guard (separation and schema checks)
- checks every source and fact
- reads each post for accuracy and tone
- runs mobile and Lighthouse tests

Posts that fail come back with a list of fixes. Following this brief exactly means no rework.

---

## Appendix A: `audit_posts.py` (copy exactly, do not modify)

```python
"""Kamboh Associates Digital: blog post auditor (v4, posts #201-#300). Needs published_index.json in the same folder.

Usage (from the kad-blog folder):   python3 audit_posts.py posts
Checks every posts/*.py file against the house standard and prints PASS/FAIL per post.
A post may be delivered only when it shows PASS with zero FAIL lines.
"""
import glob
import importlib.util
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# Every slug that exists or is planned (posts 1-100). related[] may only use these.
SLUGS = {
    1: "website-price-in-pakistan", 2: "ecommerce-website-price-in-pakistan", 3: "shopify-store-price-in-pakistan",
    4: "wordpress-website-price-in-pakistan", 5: "web-app-development-cost-in-pakistan", 6: "website-maintenance-charges-in-pakistan",
    7: "domain-and-hosting-price-in-pakistan", 8: "landing-page-design-cost-in-pakistan", 9: "website-cost-uk", 10: "website-cost-dubai",
    11: "website-redesign-cost", 12: "why-website-quotes-vary", 13: "how-to-choose-web-development-company",
    14: "best-web-development-company-lahore", 15: "freelancer-vs-agency-vs-software-house", 16: "website-development-contract-checklist",
    17: "who-owns-your-website", 18: "fixed-price-vs-hourly-web-development", 19: "website-brief-template",
    20: "web-developer-portfolio-red-flags", 21: "website-milestone-payments", 22: "website-handover-checklist",
    23: "wordpress-vs-shopify-vs-custom-website", 24: "shopify-vs-woocommerce-pakistan", 25: "wix-vs-custom-website-pakistan",
    26: "nextjs-vs-wordpress", 27: "laravel-vs-nodejs-web-apps", 28: "website-or-mobile-app-first", 29: "pwa-vs-native-app-pakistan",
    30: "headless-cms-vs-wordpress", 31: "template-vs-custom-website-design", 32: "best-hosting-for-pakistan-websites",
    33: "start-online-store-pakistan", 34: "payment-gateways-pakistan-compared", 35: "stripe-paypal-pakistan-website",
    36: "raast-bank-transfer-website-payments", 37: "cod-website-fake-orders-pakistan", 38: "courier-integration-online-store-pakistan",
    39: "daraz-vs-own-website", 40: "instagram-whatsapp-shop-to-website", 41: "product-page-checklist-pakistan",
    42: "clothing-brand-website-pakistan", 43: "dropshipping-website-pakistan", 44: "multi-vendor-marketplace-website-cost",
    45: "clinic-website-design-pakistan", 46: "dental-clinic-website", 47: "law-firm-website-design-pakistan",
    48: "school-website-design-pakistan", 49: "restaurant-website-online-ordering-pakistan", 50: "real-estate-website-pakistan",
    51: "exporter-website-b2b-pakistan", 52: "b2b-catalogue-website-manufacturers", 53: "salon-spa-booking-website",
    54: "gym-website-pakistan", 55: "pharmacy-website-pakistan", 56: "travel-agency-website-pakistan",
    57: "construction-company-website", 58: "ngo-donation-website-pakistan", 59: "hotel-guest-house-booking-website",
    60: "logistics-company-website", 61: "web-development-company-karachi", 62: "web-development-company-islamabad",
    63: "website-design-sialkot-exporters", 64: "web-development-faisalabad-textile", 65: "website-design-gujranwala-manufacturers",
    66: "web-development-multan", 67: "website-design-peshawar", 68: "ecommerce-website-lahore-retail-brands",
    69: "clinic-website-lahore", 70: "website-designer-near-me-lahore", 71: "hire-pakistani-web-developers",
    72: "white-label-web-development-pakistan", 73: "dedicated-developer-vs-fixed-project", 74: "offshore-team-time-zones-lahore",
    75: "outsourcing-website-ip-nda-code-ownership", 76: "pay-web-developer-in-pakistan", 77: "arabic-rtl-website-development",
    78: "shopify-developer-uae-saudi", 79: "uk-small-business-website-offshore", 80: "small-business-website-canada-offshore",
    81: "overseas-pakistanis-business-website-setup", 82: "mvp-development-startups", 83: "get-business-website-on-google",
    84: "google-business-profile-pakistan", 85: "seo-ready-website-checklist", 86: "ai-search-visibility-for-business",
    87: "schema-markup-business-websites", 88: "website-speed-pakistan-mobile", 89: "website-visitors-no-enquiries",
    90: "whatsapp-button-website-leads", 91: "website-hacked-what-to-do", 92: "website-security-checklist-small-business",
    93: "website-down-check", 94: "new-website-without-losing-google-traffic", 95: "website-slow-on-mobile",
    96: "website-backups-small-business", 97: "how-long-to-build-a-website", 98: "pages-for-small-business-website",
    99: "website-accessibility-basics", 100: "website-launch-checklist",
}
SLUGS.update({101: "website-developer-allama-iqbal-town-lahore", 102: "website-designer-wahdat-road-awan-town", 103: "website-design-samanabad-lahore", 104: "web-development-company-johar-town", 105: "website-design-model-town-lahore", 106: "web-design-gulberg-lahore", 107: "website-developer-dha-lahore", 108: "website-design-bahria-town-lahore", 109: "website-for-hall-road-electronics-traders", 110: "website-for-anarkali-ichhra-retailers", 111: "website-for-sundar-industrial-estate-manufacturers", 112: "lahore-web-design-prices-by-area", 113: "ai-chatbot-for-business-website-cost-pakistan", 114: "whatsapp-business-api-cost-pakistan", 115: "google-ai-mode-small-business-website", 116: "ai-website-builder-vs-web-developer", 117: "automate-website-leads-whatsapp-email", 118: "ai-product-descriptions-online-store", 119: "ai-customer-support-website-build-or-buy", 120: "website-data-privacy-when-using-ai", 121: "ai-search-optimisation-checklist-local-business", 122: "school-management-system-cost-pakistan", 123: "clinic-management-software-pakistan", 124: "pos-and-inventory-web-app-pakistan", 125: "booking-system-development-cost", 126: "lms-for-academies-pakistan", 127: "real-estate-crm-pakistan", 128: "society-management-system-pakistan", 129: "distributor-inventory-order-portal", 130: "customer-portal-development", 131: "saas-product-development-pakistan", 132: "web-app-maintenance-cost", 133: "ecommerce-seo-pakistan-store", 134: "abandoned-cart-recovery-whatsapp", 135: "eid-sale-website-readiness", 136: "shopify-apps-pakistan-stores", 137: "store-shipping-rates-and-delivery-page", 138: "return-refund-policy-online-store-pakistan", 139: "product-photography-for-online-store", 140: "ga4-ecommerce-tracking-setup", 141: "international-shipping-from-pakistan-store", 142: "wholesale-b2b-store-pakistan", 143: "migrate-woocommerce-to-shopify-or-back", 144: "website-cost-saudi-arabia", 145: "website-cost-qatar", 146: "website-cost-usa-small-business", 147: "hire-shopify-developer-pakistan", 148: "hire-wordpress-developer-pakistan", 149: "agency-overflow-development-partner", 150: "eu-gdpr-website-checklist-offshore", 151: "homepage-content-guide", 152: "about-us-page-that-builds-trust", 153: "service-page-structure", 154: "show-prices-on-website-or-not", 155: "reviews-testimonials-on-website", 156: "stock-photos-vs-real-photos", 157: "urdu-english-bilingual-website", 158: "contact-forms-that-convert", 159: "trust-signals-for-small-business-website", 160: "website-copywriting-cost-pakistan", 161: "transfer-domain-to-new-registrar", 162: "move-website-to-new-hosting", 163: "business-email-on-own-domain-pakistan", 164: "email-going-to-spam-fix", 165: "ssl-certificate-https-explained", 166: "cloudflare-for-small-business-website", 167: "website-uptime-monitoring", 168: "wordpress-updates-safely", 169: "too-many-wordpress-plugins", 170: "hosting-renewal-price-traps", 171: "wordpress-vs-webflow", 172: "wix-vs-wordpress", 173: "free-website-vs-paid-website", 174: "custom-code-vs-no-code-website", 175: "flutter-vs-react-native-vs-pwa", 176: "shopify-vs-daraz-storefront", 177: "website-discovery-meeting-what-to-expect", 178: "how-to-give-website-design-feedback", 179: "website-change-requests-cost", 180: "website-testing-before-sign-off", 181: "website-maintenance-contract-checklist", 182: "website-project-delays-why", 183: "non-technical-owner-managing-developer", 184: "taking-over-website-from-old-developer", 185: "architect-interior-designer-website", 186: "wedding-event-planner-website", 187: "photographer-portfolio-website", 188: "car-rental-website-pakistan", 189: "tuition-academy-website", 190: "furniture-brand-online-store", 191: "jewellery-store-website-pakistan", 192: "home-bakery-cafe-website", 193: "printing-press-website", 194: "immigration-consultant-website", 195: "software-house-own-website", 196: "website-budget-planner-first-year", 197: "when-to-upgrade-your-website", 198: "website-roi-small-business", 199: "google-ads-landing-page-pakistan", 200: "meta-ads-to-website-or-whatsapp"})
SLUGS.update({201: "website-for-solar-installers-pakistan", 202: "online-quran-academy-website", 203: "hostel-website-lahore", 204: "marquee-wedding-hall-website", 205: "catering-company-website", 206: "home-services-website-ac-electrician", 207: "diagnostic-lab-website", 208: "veterinary-clinic-website", 209: "optician-eyewear-store-website", 210: "physiotherapy-clinic-website", 211: "psychologist-therapist-website", 212: "nutritionist-dietitian-website", 213: "montessori-daycare-website", 214: "driving-school-website", 215: "car-showroom-used-car-dealer-website", 216: "auto-workshop-website", 217: "cctv-security-installer-website", 218: "pest-control-company-website", 219: "tile-sanitary-showroom-website", 220: "mobile-repair-shop-website", 221: "tailor-made-to-measure-website", 222: "bridal-makeup-artist-website", 223: "it-training-institute-website", 224: "packers-movers-website", 225: "printing-and-signage-shop-website", 226: "website-when-you-only-sell-on-whatsapp", 227: "website-without-logo-or-brand", 228: "urgent-website-in-one-week", 229: "website-under-25000-rupees", 230: "developer-disappeared-mid-project", 231: "website-not-showing-on-google", 232: "google-site-may-be-hacked-warning", 233: "rebrand-website-after-business-name-change", 234: "switch-com-to-pk-domain", 235: "add-online-payments-to-existing-website", 236: "add-urdu-to-english-website", 237: "add-blog-to-business-website", 238: "multi-location-business-website", 239: "franchise-website-structure", 240: "home-based-business-website", 241: "student-startup-first-website", 242: "phone-only-bookings-to-online", 243: "split-website-into-two-brands", 244: "second-website-for-export-market", 245: "inherited-family-business-website", 246: "logo-and-website-package-price", 247: "shopify-store-setup-charges", 248: "wordpress-website-fix-charges", 249: "website-speed-optimisation-charges", 250: "website-migration-charges", 251: "domain-renewal-charges-pakistan", 252: "ssl-certificate-price-pakistan", 253: "business-email-price-per-user-pakistan", 254: "website-audit-charges", 255: "malware-removal-charges", 256: "product-upload-charges-online-store", 257: "website-urdu-translation-charges", 258: "website-kaise-banwayein", 259: "online-store-kaise-banayein", 260: "website-ka-mahana-kharcha", 261: "ghar-baithe-online-business-website", 262: "google-maps-par-dukaan-kaise-add-karein", 263: "whatsapp-se-order-wali-website", 264: "domain-kya-hota-hai", 265: "hosting-kya-hoti-hai", 266: "website-aur-app-mein-farq", 267: "shopify-store-kaise-banayein", 268: "jazzcash-easypaisa-website-par", 269: "website-ki-seo-kaise-karein", 270: "saturday-website-support-lahore", 271: "urgent-website-fix-same-day", 272: "overseas-client-support-hours", 273: "online-meeting-or-office-visit", 274: "website-support-in-urdu", 275: "website-design-sargodha", 276: "website-design-bahawalpur", 277: "website-design-sahiwal", 278: "website-design-kasur-khussa-leather", 279: "website-design-gujrat-furniture-fans", 280: "website-design-wazirabad-cutlery", 281: "website-design-chiniot-furniture", 282: "website-design-sheikhupura", 283: "website-design-hyderabad-sindh", 284: "website-design-sukkur", 285: "website-design-abbottabad", 286: "website-design-mardan", 287: "website-design-rahim-yar-khan", 288: "website-design-jhelum", 289: "website-design-mirpur-ajk", 290: "website-vs-facebook-page", 291: "website-vs-google-business-profile-only", 292: "linktree-vs-website", 293: "whatsapp-catalogue-vs-online-store", 294: "free-hosting-vs-paid-hosting", 295: "pk-vs-com-pk-domain", 296: "one-page-vs-multi-page-website", 297: "website-subscription-vs-one-time-build", 298: "theme-marketplace-vs-custom-design", 299: "canva-website-vs-wordpress", 300: "agency-retainer-vs-pay-per-task"})
PILLARS = {1, 13, 23, 33, 45, 71, 83, 101, 113, 122, 151, 201, 226, 258}
SERVICE_PATHS = {"/digital", "/digital/business-websites", "/digital/ecommerce-development", "/digital/web-app-development",
                 "/digital/pricing", "/digital/web-development-lahore", "/digital/contact", "/digital/blog"}
CATEGORIES = {"Costs & Budgets", "Hiring a Developer", "Platforms & Comparisons", "E-commerce in Pakistan", "Websites by Industry",
              "Local Guides", "Working With Overseas Clients", "Getting Found Online", "Fix a Problem", "Planning & Launch", "AI and Automation", "Software and Web Apps", "Content and Conversion", "Websites by Profession", "Roman Urdu Guides", "Working With Us"}
# Words that must never appear in a title or H1 (keeps the web section separate from the tax site).
FORBIDDEN_TITLE = r"\b(tax|taxes|fbr|ntn|strn|filer|non-filer|atl|return|returns|secp|withholding|wht|gst|sales tax|income|salary|audit notice|iris)\b"
# Phrases that mark generic AI filler; any hit is a FAIL.
FILLER = ["in today's digital", "in today's fast-paced", "in the digital age", "in this day and age", "look no further",
          "unlock the power", "unleash", "game-changer", "game changer", "elevate your", "seamless", "cutting-edge",
          "delve", "navigating the", "it's important to note", "it is important to note", "in conclusion", "ever-evolving",
          "robust solution", "one-stop", "whether you're a", "take your business to the next level", "embark", "tapestry",
          "landscape of", "realm of", "harness the"]
STOP = {"in", "the", "a", "an", "my", "to", "for", "vs", "of", "and", "on", "with", "your", "is", "how", "what", "do", "does"}
REQUIRED = ["order", "slug", "title", "h1", "crumb", "description", "keyword", "cluster", "category", "published", "published_h",
            "updated", "updated_h", "answer", "takeaways", "body", "faqs", "sources", "method", "related", "service_links", "cta", "wa"]


def strip(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def words(s):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.,%-]*", strip(s)))


def has_kw(kw, text):
    ws = [w for w in re.findall(r"[a-z0-9]+", kw.lower()) if w not in STOP]
    t = re.sub(r"[-–]", " ", text.lower())
    return all(re.search(r"\b" + re.escape(w) + r"s?\b", t) or (w == "ecommerce" and "e commerce" in t) for w in ws)


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.POST


def audit(p):
    f, w = [], []  # FAIL, WARN
    for k in REQUIRED:
        if k not in p:
            f.append(f"missing field: {k}")
    if f:
        return f, w
    n = p["order"]
    if SLUGS.get(n) != p["slug"]:
        f.append(f"slug must be '{SLUGS.get(n)}' for post #{n}")
    if len(p["title"]) > 60:
        f.append(f"title {len(p['title'])} chars (max 60)")
    if not 110 <= len(p["description"]) <= 165:
        f.append(f"description {len(p['description'])} chars (110-165)")
    if p["title"] == p["h1"]:
        f.append("title and h1 must differ")
    if not 35 <= len(p["h1"]) <= 95:
        w.append(f"h1 {len(p['h1'])} chars (aim 35-95)")
    for fld in ("title", "h1"):
        if re.search(FORBIDDEN_TITLE, p[fld].lower()):
            f.append(f"forbidden word in {fld}: {re.search(FORBIDDEN_TITLE, p[fld].lower()).group(0)}")
    if p["category"] not in CATEGORIES:
        f.append(f"unknown category '{p['category']}'")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", p["published"]) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", p["updated"]):
        f.append("dates must be YYYY-MM-DD")
    kw = p["keyword"]
    body = p["body"]
    first100 = " ".join(strip(p["answer"] + " " + body).split()[:100])
    h2s = re.findall(r'<h2 id="([^"]+)">([\s\S]*?)</h2>', body)
    for where, txt in (("title", p["title"]), ("h1", p["h1"]), ("description", p["description"]), ("first 100 words", first100),
                       ("an H2", " ".join(t for _, t in h2s))):
        if not has_kw(kw, txt):
            f.append(f"keyword '{kw}' not in {where}")
    a = words(p["answer"])
    if not 40 <= a <= 60:
        f.append(f"answer {a} words (40-60)")
    if not re.search(r"\d", p["answer"]):
        w.append("answer has no number; add a price, time or count if one exists")
    if len(p["takeaways"]) != 5:
        f.append(f"{len(p['takeaways'])} takeaways (exactly 5)")
    pillar = n in PILLARS
    bw = words(body)
    lo, hi = (1000, 2200) if pillar else (600, 1300)
    if not lo <= bw <= hi:
        f.append(f"body {bw} words ({lo}-{hi} for {'pillar' if pillar else 'spoke'})")
    if len(h2s) < (6 if pillar else 5):
        f.append(f"{len(h2s)} H2s (min {6 if pillar else 5})")
    ids = [i for i, _ in h2s]
    if len(ids) != len(set(ids)):
        f.append("duplicate H2 id")
    for i in ids:
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", i) or i in {"faqs", "sources", "key-takeaways", "how-we-researched", "keep-reading"}:
            f.append(f"bad or reserved H2 id '{i}'")
    q = sum(1 for _, t in h2s if t.strip().endswith("?"))
    if q < 2:
        f.append(f"only {q} question-style H2s (min 2)")
    if "<table>" not in body:
        f.append("no comparison table")
    for t in re.findall(r"<table>([\s\S]*?)</table>", body):
        rows = re.findall(r"<tr>([\s\S]*?)</tr>", t)
        if not rows or "<th>" not in rows[0]:
            f.append("table first row must be <th> headers")
        cols = {len(re.findall(r"<t[hd][ >]", r)) for r in rows}
        if len(cols) > 1:
            f.append("table rows have different column counts")
    if re.search(r"<h1|<img|<script|<style|<div|<span|style=|<br|&nbsp;", body, re.I):
        f.append("body uses a forbidden tag or attribute (h1, img, script, style, div, span, br, inline style)")
    for tag in ("p", "ul", "ol", "li", "table", "tr", "td", "th", "h2", "h3", "strong", "a"):
        if len(re.findall(rf"<{tag}[ >]", body)) != body.count(f"</{tag}>"):
            f.append(f"unbalanced <{tag}> tags")
    internal = re.findall(r'href="(/[^"]*)"', body)
    for h in internal:
        if not (h in SERVICE_PATHS or (h.startswith("/digital/blog/") and h[len("/digital/blog/"):] in SLUGS.values())):
            f.append(f"internal link not allowed: {h}")
    blog_links = {h for h in internal if h.startswith("/digital/blog/")}
    if len(blog_links) < 2:
        f.append(f"{len(blog_links)} links to other guides in the body (min 2)")
    if not any(h in SERVICE_PATHS for h in internal):
        f.append("no link to a service page in the body")
    if re.search(r'href="https?://(www\.)?kambohassociates\.com', body):
        f.append("use relative /digital links, not full kambohassociates.com URLs")
    if re.search(r'target=|rel=', body):
        f.append("do not add target/rel to body links")
    nf = len(p["faqs"])
    if not ((8 if pillar else 6) <= nf <= (10 if pillar else 8)):
        f.append(f"{nf} FAQs ({'8-10' if pillar else '6-8'})")
    for qq, aa in p["faqs"]:
        aw = words(aa)
        if not 40 <= aw <= 60:
            f.append(f"FAQ answer {aw} words (40-60): {qq[:50]}")
        if "<" in aa:
            f.append(f"FAQ answer must be plain text: {qq[:50]}")
        if not qq.endswith("?"):
            f.append(f"FAQ question must end with '?': {qq[:50]}")
    if not 3 <= len(p["sources"]) <= 9:
        f.append(f"{len(p['sources'])} sources (3-9)")
    for t, u in p["sources"]:
        if not u.startswith("https://") or "kambohassociates.com" in u:
            f.append(f"bad source url: {u}")
    if not 3 <= len(p["related"]) <= 5:
        f.append(f"{len(p['related'])} related slugs (3-5)")
    for s in p["related"]:
        if s not in SLUGS.values() or s == p["slug"]:
            f.append(f"related slug not allowed: {s}")
    for path, label in p["service_links"]:
        if path not in SERVICE_PATHS:
            f.append(f"service link not allowed: {path}")
    if not 5 <= len(p["cluster"]) <= 8:
        f.append(f"{len(p['cluster'])} cluster terms (5-8)")
    if not p["wa"].startswith("Hi%2C%20I%20read%20your%20") or " " in p["wa"]:
        f.append("wa must be URL-encoded and start with Hi%2C%20I%20read%20your%20")
    if not 25 <= words(p["method"]) <= 90:
        f.append(f"method {words(p['method'])} words (25-90)")
    alltext = " ".join([p["title"], p["h1"], p["description"], p["answer"], " ".join(p["takeaways"]), body, p["method"]] +
                       [x + " " + y for x, y in p["faqs"]]).lower()
    for ph in FILLER:
        if ph in alltext:
            f.append(f"filler phrase: '{ph}'")
    if alltext.count("—") > 6:
        w.append(f"{alltext.count('—')} em dashes; use full stops and commas instead")
    if re.search(r"\b(guarantee|guaranteed)\b.{0,40}\b(rank|ranking|first page|#1)\b", alltext):
        w.append("mentions guaranteed rankings; fine only as a warning to readers, never as our promise")
    if re.search(r"\b\d{2,5}\+?\s+(clients|websites built|projects delivered|happy customers)\b", alltext):
        f.append("unverified client/project count; remove it")
    return f, w


# ---------------- v4 checks: lessons from earlier batches ----------------
import hashlib, html as _html, json as _json
from itertools import combinations as _comb
try:
    from prices import P as _P
except Exception:
    _P = {}
_INDEX_FILE = os.path.join(HERE, "published_index.json")
_IDX = _json.load(open(_INDEX_FILE)) if os.path.exists(_INDEX_FILE) else {"posts": {}, "h2": [], "faq": [], "sentences": [], "grams12": []}
_PUB_H2, _PUB_FAQ = set(_IDX["h2"]), set(_IDX["faq"])
_PUB_SENT, _PUB_G12 = set(_IDX["sentences"]), set(_IDX["grams12"])
_PUB_KW = {v["keyword"].lower() for v in _IDX["posts"].values()}
_PUB_H1 = {k: v["h1"] for k, v in _IDX["posts"].items()}
GENERIC_H2 = {"what we would build for you", "what does it cost", "how we help", "how we can help", "our approach",
              "which should you choose", "conclusion", "final thoughts", "summary", "introduction", "overview",
              "what about customer data", "what privacy points apply", "questions to answer before you decide",
              "what should the contract cover", "why choose us", "next steps", "get started"}
DANGLING = {"with", "without", "and", "or", "the", "a", "an", "to", "of", "for", "in", "on", "from", "your", "vs", "by", "at", "is"}


def _norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", _html.unescape(re.sub(r"<[^>]+>", " ", s)).lower())).strip()


def _h(s):
    return hashlib.sha1(s.encode()).hexdigest()[:16]


def _text(p):
    return " ".join([p["answer"], p["body"], " ".join(a for _, a in p["faqs"])])


def v4_checks(posts, folder):
    """posts: list of (filename, POST). Returns {filename: (fails, warns)}."""
    out = {n: ([], []) for n, _ in posts}
    if any(f.endswith((".html", ".htm")) for f in os.listdir(folder)):
        for n in out:
            out[n][0].append("HTML files found in the posts folder: deliver .py post files only")
    h1s = dict(_PUB_H1)
    h1s.update({p["slug"]: p["h1"] for _, p in posts})
    h2_seen, faq_seen, sent_seen, grams = {}, {}, {}, {}
    for n, p in posts:
        F, W = out[n]
        raw = open(os.path.join(folder, n), encoding="utf-8").read()
        if p.get("slug") in _IDX["posts"]:
            F.append("slug already published")
        if p.get("keyword", "").lower() in _PUB_KW:
            F.append("primary keyword already used by a published guide")
        for c in p.get("cluster", []):
            if c.lower() in _PUB_KW:
                F.append(f"cluster term '{c}' is a published guide's primary keyword")
        for k, v in _P.items():
            if v in raw:
                F.append(f"price typed as text ({v}); use {{P['{k}']}} in an f-string")
        for _, t in re.findall(r'<h2 id="([^"]+)">([\s\S]*?)</h2>', p["body"]):
            nt = _norm(t)
            if nt in GENERIC_H2:
                F.append(f"generic H2 '{t.strip()}': make it specific to this topic")
            elif nt in _PUB_H2:
                F.append(f"H2 already used by a published guide: '{t.strip()}'")
            h2_seen.setdefault(nt, []).append(n)
        for q, _ in p["faqs"]:
            nq = _norm(q)
            if nq in _PUB_FAQ:
                F.append(f"FAQ question already used by a published guide: '{q}'")
            faq_seen.setdefault(nq, []).append(n)
        for m in re.finditer(r'<a href="([^"]+)">([^<]*)</a>', p["body"]):
            href, anc = m.group(1), _html.unescape(m.group(2))
            words_ = anc.split()
            if anc != anc.strip() or not words_:
                F.append(f"link text has leading/trailing space or is empty: '{anc}'")
                continue
            if len(words_) < 2:
                W.append(f"one-word link text '{anc}': prefer a descriptive phrase")
            if words_[-1].lower() in DANGLING:
                F.append(f"link text ends mid-phrase ('{words_[-1]}'): '{anc}'")
            if href.startswith("/digital/blog/"):
                tgt = h1s.get(href.rsplit("/", 1)[-1], "")
                if tgt and tgt.startswith(anc) and len(anc) < len(tgt) and tgt[len(anc)].isalpha():
                    F.append(f"link text is a cut-off copy of the target title: '{anc}'")
            if href.startswith("http") and not href.startswith("https://"):
                F.append(f"external link must be https: {href}")
        text = _text(p)
        for s in re.split(r"(?<=[.!?])\s+", _html.unescape(re.sub(r"<[^>]+>", " ", text))):
            ns = _norm(s)
            if len(ns.split()) >= 12:
                hs = _h(ns)
                if hs in _PUB_SENT:
                    F.append(f"sentence copied from a published guide: '{s.strip()[:80]}'")
                sent_seen.setdefault(hs, set()).add(n)
        w = _norm(text).split()
        g = {_h(" ".join(w[i:i + 12])) for i in range(len(w) - 11)}
        grams[n] = g
        if g:
            share = len(g & _PUB_G12) / len(g)
            if share > 0.03:
                F.append(f"{share:.1%} of 12-word phrases also appear in published guides (max 3%)")
    for nt, names in h2_seen.items():
        if len(set(names)) > 1:
            for n in set(names):
                out[n][0].append(f"H2 text repeated in another post of this batch: '{nt}'")
    for nq, names in faq_seen.items():
        if len(names) > 1:
            for n in set(names):
                out[n][0].append(f"FAQ question repeated in this batch: '{nq}'")
    for hs, names in sent_seen.items():
        if len(names) > 1:
            for n in names:
                out[n][0].append("a 12+ word sentence is repeated in another post of this batch")
    for (a, ga), (b, gb) in _comb(grams.items(), 2):
        if ga and gb:
            r = len(ga & gb) / min(len(ga), len(gb))
            if r > 0.03:
                out[a][0].append(f"{r:.1%} phrase overlap with {b} (max 3%)")
                out[b][0].append(f"{r:.1%} phrase overlap with {a} (max 3%)")
    def toks(t):
        return set(re.findall(r"[a-z0-9]+", t.lower())) - {"in", "the", "a", "and", "for", "of", "to", "your", "website", "websites", "pakistan", "lahore"}
    for (a, pa), (b, pb) in _comb(posts, 2):
        ta, tb = toks(pa["title"]), toks(pb["title"])
        shape = lambda t: re.sub(r"[A-Za-z]+", "w", t.split(":")[-1]) if ":" in t else ""
        if ta and tb and len(ta & tb) / len(ta | tb) > 0.5:
            out[a][1].append(f"title very similar to {b}")
        if ":" in pa["title"] and shape(pa["title"]) == shape(pb["title"]) and pa["title"].split(":")[-1].count(",") >= 1:
            out[a][1].append(f"title has the same 'X: A, B, C' shape as {b}; vary it")
    return out


def main():
    folder = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "posts")
    posts, fails = [], 0
    for path in sorted(glob.glob(os.path.join(folder, "*.py"))):
        try:
            posts.append((os.path.basename(path), load(path)))
        except Exception as e:
            print(f"FAIL {os.path.basename(path)}: does not load: {e}")
            fails += 1
    # cross-post checks: unique keyword/title/description/h1, cluster terms not stealing another post's keyword
    seen = defaultdict(list)
    for name, p in posts:
        for k in ("keyword", "title", "description", "h1", "slug"):
            seen[(k, p.get(k, "").lower())].append(name)
    keywords = {p.get("keyword", "").lower(): name for name, p in posts}
    cluster_owner = defaultdict(list)
    for name, p in posts:
        for c in p.get("cluster", []):
            cluster_owner[c.lower()].append(name)
    extra = v4_checks(posts, folder)
    for name, p in posts:
        f, w = audit(p)
        f += extra[name][0]; w += extra[name][1]
        for (k, v), names in seen.items():
            if name in names and len(names) > 1 and v:
                f.append(f"duplicate {k} with {', '.join(x for x in names if x != name)}")
        for c in p.get("cluster", []):
            if c.lower() in keywords and keywords[c.lower()] != name:
                f.append(f"cluster term '{c}' is the primary keyword of {keywords[c.lower()]} (cannibalisation)")
            if len(cluster_owner[c.lower()]) > 1:
                w.append(f"cluster term '{c}' also used by {', '.join(x for x in cluster_owner[c.lower()] if x != name)}")
        print(f"{'PASS' if not f else 'FAIL'}  #{p.get('order', '?'):>3} {name}")
        for x in f:
            print(f"      FAIL  {x}")
        for x in w:
            print(f"      warn  {x}")
        fails += bool(f)
    print(f"\n{len(posts)} posts checked, {fails} failing.")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
```
