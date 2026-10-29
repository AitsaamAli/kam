# Kamboh Associates Digital: Writer Brief for Blog Posts #23–#100

**Version:** 1.0, 29 October 2026
**For:** a Claude (Claude Code) session writing the remaining 78 web development guides for `kambohassociates.com/digital/blog`
**Prepared by:** the Kamboh Associates Digital SEO and content team. This team wrote and audited posts #1–#22, which are live.

---

## 0. How to use this brief (read first)

You are writing blog posts that will be published as they are delivered. Each post you deliver is a Python file in an exact format. The site's build script turns it into a page with schema, so **the format must be exact** and **every rule below is a hard requirement**.

Work happens in **4 parts**. The owner will ask you for one part at a time ("Write Part 1"). Do only the part asked.

| Part | Posts | Clusters | Count |
|---|---|---|---|
| Part 1 | #23–#42 | C (platforms), D (e-commerce, first half) | 20 |
| Part 2 | #43–#62 | D (rest), E (industries), F (first two local) | 20 |
| Part 3 | #63–#82 | F (rest of local), G (overseas clients) | 20 |
| Part 4 | #83–#100 | H (getting found), I (fix a problem), J (planning and launch) | 18 |

For each part:
1. Set up the workspace (section 4). This is needed once only.
2. Write the posts **five at a time**. After every five, run the auditor and fix every FAIL before writing the next five.
3. When all posts in the part pass, run the clustering audit (section 10) and write the part report (section 12).
4. Deliver one zip file: `kad-part-N.zip`. It contains `posts/*.py` for that part and `PART-N-REPORT.md`.

Do not skip the audit. Do not deliver a post that shows FAIL. If a rule seems impossible for a post, say so in the report rather than breaking the rule.

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

**Settled market facts.** Use these figures where they fit. They are already researched and sourced in posts #1–#22, so link to that post when you use them.

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

Test the setup: `python3 audit_posts.py posts` should run and report 0 posts.

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
| `order` | int | The post number (23–100) |
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
| `faqs` | list of tuples | `("Question?", "Answer.")`. Spokes: 6–8. Pillars (#23, #33, #45, #71, #83): 8–10. Answers 40–60 words, plain text, self-contained |
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
  - the Pakistan Bar Council (pbc.org.pk) for lawyers

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

---

## 7. Sources

**Use only:**
- URLs from the approved list below, or
- official pages you have opened yourself and confirmed load (HTTP 200) on the day you write. List every such new URL in the part report so we can verify it.

Never cite a page you have not opened. Never guess a deep link.

**Approved source list** (all checked 29 October 2026):

- https://baymard.com/lists/cart-abandonment-rate
- https://business.whatsapp.com/products/business-platform
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
- https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites
- https://easypaisa.com.pk/
- https://faq.whatsapp.com/5913398998672934
- https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries-and-regions
- https://help.shopify.com/en/manual/payments/third-party-providers
- https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/
- https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/
- https://laravel.com/docs
- https://letsencrypt.org/
- https://lookup.icann.org/
- https://nextjs.org/docs
- https://nodejs.org/en/about
- https://owasp.org/www-project-top-ten/
- https://pagespeed.web.dev/
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
- https://www.pbc.org.pk/
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

## 9. The 78 posts: assignments

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

**Related:** always include the cluster pillar (marked **P**) plus 2–4 same-cluster siblings. Where natural, also include one guide from #1–#22.

**Already published (#1–#22).** Link to these where relevant. Never reuse their primary keywords.

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

**Cluster pillars** (every spoke puts its pillar in `related`):

| Clusters | Pillar |
|---|---|
| C | #23 |
| D | #33 |
| E | #45 |
| F | #14 (published) |
| G | #71 |
| H | #83 |
| I | #83 |
| J | #23 or #83, whichever fits |

### Part 1: posts #23–#42

| # | Slug (exact) | File prefix | Category | Topic and angle | Primary keyword | Cluster seeds | Intent | Aud | Link | Must include |
|---|---|---|---|---|---|---|---|---|---|---|
| 23 | `wordpress-vs-shopify-vs-custom-website` | `c23_` | Platforms & Comparisons | WordPress vs Shopify vs custom: which should a Pakistani business choose? (PILLAR) | `wordpress vs shopify` | best platform for website pakistan; wordpress or shopify for small business; custom website vs wordpress; website platform comparison | C | PK | /digital/business-websites | Decision tree by business type (brochure, store, booking, portal); 3-way table of build cost, running cost, editing, SEO, payments in Pakistan; link down to #24-#32 |
| 24 | `shopify-vs-woocommerce-pakistan` | `c24_` | Platforms & Comparisons | Shopify vs WooCommerce for Pakistani stores | `shopify vs woocommerce pakistan` | woocommerce or shopify; shopify vs wordpress for online store; best ecommerce platform pakistan | C | PK | /digital/ecommerce-development | COD, JazzCash/Easypaisa and courier support on each; total 3-year cost table using settled Shopify figures; when each wins |
| 25 | `wix-vs-custom-website-pakistan` | `c25_` | Platforms & Comparisons | Wix and Squarespace vs a custom website in Pakistan | `wix vs custom website` | squarespace vs custom website; website builder vs developer; wix pakistan payment | C | PK | /digital/business-websites | Local payment limits, USD billing, SEO and ownership limits; when a builder is honestly enough |
| 26 | `nextjs-vs-wordpress` | `c26_` | Platforms & Comparisons | Next.js vs WordPress for a business website | `nextjs vs wordpress` | headless website vs wordpress; react website vs wordpress; fastest website platform | C | PK/OS | /digital/web-app-development | Speed, editing, hosting cost and hiring trade-offs; who should not choose Next.js |
| 27 | `laravel-vs-nodejs-web-apps` | `c27_` | Platforms & Comparisons | Laravel vs Node.js for business web apps | `laravel vs node` | php vs node for web app; best backend for web application; laravel developers pakistan | C | PK/OS | /digital/web-app-development | Explain for non-developers; hiring pool and long-term maintenance in Pakistan; decision table by app type |
| 28 | `website-or-mobile-app-first` | `c28_` | Platforms & Comparisons | Website or mobile app first? A small-business decision guide | `website or app for business` | do i need an app for my business; website vs mobile app cost; app banwana chahiye ya website | C | PK | /digital/web-app-development | Reach, cost and maintenance comparison; scenarios where an app is worth it; link #29 |
| 29 | `pwa-vs-native-app-pakistan` | `c29_` | Platforms & Comparisons | Progressive web app vs native app for Pakistani users | `pwa vs native app` | progressive web app pakistan; pwa benefits; installable website | C | PK | /digital/web-app-development | Data cost and low-end Android storage; offline use; app store fees; MDN/web.dev sources |
| 30 | `headless-cms-vs-wordpress` | `c30_` | Platforms & Comparisons | Headless CMS vs WordPress: do you need it? | `headless cms vs wordpress` | what is a headless cms; headless website cost; when to use headless cms | I/C | OS | /digital/web-app-development | Plain definition; when headless is overkill for a small business; cost and team implications |
| 31 | `template-vs-custom-website-design` | `c31_` | Platforms & Comparisons | Template vs custom design: what you really get | `template vs custom website` | custom website design cost; premium theme vs custom design; website template pakistan | C | PK | /digital/business-websites | Side-by-side table of what each includes; licences; how to spot a theme sold as custom; link #4 and #12 |
| 32 | `best-hosting-for-pakistan-websites` | `c32_` | Platforms & Comparisons | Best hosting for Pakistani websites: local vs international servers | `best hosting for pakistan website` | hosting in pakistan vs international; web hosting pakistan comparison; cloud hosting for business pakistan | C | PK | /digital/business-websites | Latency to Pakistani visitors, PKR vs USD billing, support, renewal pricing, backups; how to test speed from Pakistan; link #7 |
| 33 | `start-online-store-pakistan` | `d33_` | E-commerce in Pakistan | How to start an online store in Pakistan: complete 2026 guide (PILLAR) | `start online store pakistan` | online store kaise shuru karein; start ecommerce business pakistan; online business website pakistan; how to sell online in pakistan | I/C | PK | /digital/ecommerce-development | End-to-end steps: products, platform, domain, payments, COD, couriers, policies, launch, marketing; budget table using P and settled figures; link to every D spoke |
| 34 | `payment-gateways-pakistan-compared` | `d34_` | E-commerce in Pakistan | Payment gateways in Pakistan compared: JazzCash, Easypaisa, PayFast and banks | `payment gateway pakistan` | jazzcash payment gateway for website; easypaisa merchant account; best payment gateway for ecommerce pakistan; online payment integration pakistan | C | PK | /digital/ecommerce-development | Comparison table: what each supports, typical documents, fees ONLY where sourced and dated, settlement notes; say 'check current rates' otherwise |
| 35 | `stripe-paypal-pakistan-website` | `d35_` | E-commerce in Pakistan | Stripe and PayPal in Pakistan: what actually works for your website | `stripe pakistan alternative` | paypal pakistan website; receive international payments website pakistan; stripe not available pakistan | I | PK/OS | /digital/ecommerce-development | Honest, legal options only; Stripe Global page as source; overseas-registered company route explained without tax detail |
| 36 | `raast-bank-transfer-website-payments` | `d36_` | E-commerce in Pakistan | Raast and bank transfers on your website: how to set them up | `raast payment integration` | raast for business; bank transfer checkout; manual payment confirmation website | I | PK | /digital/ecommerce-development | What Raast is (SBP homepage as source), checkout flow for transfer payments, order confirmation and reconciliation steps |
| 37 | `cod-website-fake-orders-pakistan` | `d37_` | E-commerce in Pakistan | Cash on delivery websites: how to cut fake orders and returns | `cod website pakistan` | fake orders cod; reduce cod returns; order confirmation whatsapp | I | PK | /digital/ecommerce-development | Order-verification flow (WhatsApp/SMS confirm, address checks, partial advance), return-cost worked example labelled illustrative |
| 38 | `courier-integration-online-store-pakistan` | `d38_` | E-commerce in Pakistan | Courier integration for online stores (TCS, Leopards, PostEx, Trax) | `courier api integration pakistan` | courier booking from website; shipping integration pakistan; postex integration shopify | I | PK | /digital/ecommerce-development | Feature comparison (booking, tracking, COD remittance) from each courier's official site; no invented fees |
| 39 | `daraz-vs-own-website` | `d39_` | E-commerce in Pakistan | Daraz vs your own website: where should you sell? | `daraz vs own website` | sell on daraz or own store; marketplace vs own website; daraz seller commission | C | PK | /digital/ecommerce-development | Margin maths example labelled illustrative; control of customer data and brand; using both |
| 40 | `instagram-whatsapp-shop-to-website` | `d40_` | E-commerce in Pakistan | Instagram and WhatsApp to website: moving your shop online properly | `instagram shop to website` | whatsapp order website; instagram business to online store; social media shop website | C | PK | /digital/ecommerce-development | Step-by-step migration plan; keeping WhatsApp ordering; catalogue sync; what changes for customers |
| 41 | `product-page-checklist-pakistan` | `d41_` | E-commerce in Pakistan | Product pages that sell: a Pakistani store checklist | `product page best practices` | product description examples; ecommerce product page checklist; urdu product description | I | PK | /digital/ecommerce-development | Checklist table; photos, size charts, delivery and COD info, reviews; English/Roman Urdu copy examples; NN/g source |
| 42 | `clothing-brand-website-pakistan` | `d42_` | E-commerce in Pakistan | Clothing brand website in Pakistan: features, cost and launch plan | `clothing brand website pakistan` | fashion brand website pakistan; lawn collection website; clothing store website cost | C | PK | /digital/ecommerce-development | Size charts, stock per size, season launches (lawn/eid) with traffic spikes, P['store'] package; launch timeline |

### Part 2: posts #43–#62

| # | Slug (exact) | File prefix | Category | Topic and angle | Primary keyword | Cluster seeds | Intent | Aud | Link | Must include |
|---|---|---|---|---|---|---|---|---|---|---|
| 43 | `dropshipping-website-pakistan` | `d43_` | E-commerce in Pakistan | Dropshipping website in Pakistan: what works practically | `dropshipping website pakistan` | dropshipping in pakistan; dropshipping store cost; local dropshipping suppliers | I/C | PK | /digital/ecommerce-development | Realistic margins example labelled illustrative, COD and returns risk, supplier reliability; no income promises |
| 44 | `multi-vendor-marketplace-website-cost` | `d44_` | E-commerce in Pakistan | Multi-vendor marketplace website: cost and features | `multi vendor marketplace development` | marketplace website cost; build a marketplace like daraz; multi vendor ecommerce | C | PK/OS | /digital/web-app-development | Commission and payout flows, vendor onboarding, P['app_range']; phased MVP; link #82 |
| 45 | `clinic-website-design-pakistan` | `e45_` | Websites by Industry | Website for doctors and clinics in Pakistan: features, booking and cost (PILLAR) | `clinic website design pakistan` | doctor website pakistan; hospital website design; online appointment booking clinic; clinic website cost | C | PK | /digital/business-websites | Booking, doctor profiles, PMDC registration display, patient privacy, Google Business Profile; package table with P; link to E spokes |
| 46 | `dental-clinic-website` | `e46_` | Websites by Industry | Dental clinic website: treatments, before/after galleries and booking | `dental clinic website` | dentist website design; dental website features; dental clinic online booking | C | PK/OS | /digital/business-websites | Treatment pages, consent for patient photos, privacy, regulator note (PMDC) |
| 47 | `law-firm-website-design-pakistan` | `e47_` | Websites by Industry | Law firm website in Pakistan: professional, compliant and credible | `law firm website design pakistan` | lawyer website pakistan; advocate website; legal services website | C | PK | /digital/business-websites | Practice-area pages, careful claims, Pakistan Bar Council homepage source; tell readers to check advertising rules |
| 48 | `school-website-design-pakistan` | `e48_` | Websites by Industry | School and academy website: admissions, fees and parent portal | `school website design pakistan` | academy website; online admission form school; parent portal pakistan | C | PK | /digital/web-app-development | Admissions flow, fee schedule pages, notices, parent portal scope with P['app']; Urdu option |
| 49 | `restaurant-website-online-ordering-pakistan` | `e49_` | Websites by Industry | Restaurant website with online ordering (without marketplace commission) | `restaurant website online ordering pakistan` | restaurant online ordering system; food delivery website; restaurant website cost | C | PK | /digital/ecommerce-development | Commission maths example labelled illustrative (no invented marketplace %), menu, delivery zones, WhatsApp orders |
| 50 | `real-estate-website-pakistan` | `e50_` | Websites by Industry | Real estate website in Pakistan: listings, leads and WhatsApp | `real estate website pakistan` | property portal website; real estate agent website; property listing website cost | C | PK | /digital/web-app-development | Listing structure, lead routing to agents, WhatsApp, map/area pages; avoid any property-tax content |
| 51 | `exporter-website-b2b-pakistan` | `e51_` | Websites by Industry | Exporter website: winning foreign buyers | `export company website` | b2b website for exporters; exporter website design; website for international buyers | C | PK | /digital/business-websites | RFQ forms, catalogue SEO, certifications display (only real ones), English for buyers, time-zone contact info |
| 52 | `b2b-catalogue-website-manufacturers` | `e52_` | Websites by Industry | Manufacturer B2B catalogue website: features that bring orders | `b2b catalogue website` | manufacturer website; product catalogue website; distributor portal | C | PK | /digital/business-websites | Spec sheets, downloadable catalogues, distributor login, enquiry routing; difference from #51 stated |
| 53 | `salon-spa-booking-website` | `e53_` | Websites by Industry | Salon and spa website with booking | `salon booking website` | spa website design; beauty salon website pakistan; online booking salon | C | PK | /digital/web-app-development | Booking with deposits, reminders to cut no-shows, service menu and prices, WhatsApp |
| 54 | `gym-website-pakistan` | `e54_` | Websites by Industry | Gym website: memberships, classes and payments | `gym website pakistan` | fitness club website; gym membership system; class booking website | C | PK | /digital/web-app-development | Membership plans, class schedules, payment options, member portal scope |
| 55 | `pharmacy-website-pakistan` | `e55_` | Websites by Industry | Pharmacy website: product catalogue and WhatsApp ordering | `pharmacy website pakistan` | online pharmacy website; medical store website; medicine ordering website | C | PK | /digital/ecommerce-development | Prescription-item handling, DRAP homepage as source, tell readers to confirm current rules; catalogue and WhatsApp ordering |
| 56 | `travel-agency-website-pakistan` | `e56_` | Websites by Industry | Travel agency website: packages, visa pages and enquiries | `travel agency website pakistan` | tour company website; umrah package website; travel booking website | C | PK | /digital/business-websites | Package pages, enquiry forms, trust signals, honest note about not processing visas online unless licensed |
| 57 | `construction-company-website` | `e57_` | Websites by Industry | Construction company website: projects, tenders and trust | `construction company website` | builder website pakistan; contractor website; construction portfolio website | C | PK | /digital/business-websites | Project portfolio structure, capability statements, tender documents download, safety and credentials (real only) |
| 58 | `ngo-donation-website-pakistan` | `e58_` | Websites by Industry | NGO and trust website: donations, reports and transparency | `ngo website pakistan` | donation website; charity website design; online donation pakistan | C | PK | /digital/web-app-development | Donation options (sourced), annual reports, transparency pages, donor privacy |
| 59 | `hotel-guest-house-booking-website` | `e59_` | Websites by Industry | Hotel and guest house website: direct bookings | `hotel website booking engine` | guest house website; hotel booking website pakistan; direct booking website | C | PK | /digital/web-app-development | Booking engine options, OTA commission comparison only with sourced %, rooms and rates pages |
| 60 | `logistics-company-website` | `e60_` | Websites by Industry | Logistics and courier company website: tracking and quotes | `logistics company website` | freight company website; tracking system website; courier company website | C | PK | /digital/web-app-development | Tracking integration, quote calculator, B2B account pages, scope with P['app'] |
| 61 | `web-development-company-karachi` | `f61_` | Local Guides | Web development in Karachi: what importers and online sellers need | `web development company karachi` | website design karachi; ecommerce website karachi; web developer karachi | L/C | PK | /digital/contact | Real Karachi business facts (port-based trade, large online seller base, courier hubs), how we work remotely from Lahore |
| 62 | `web-development-company-islamabad` | `f62_` | Local Guides | Web development in Islamabad and Rawalpindi: consultants, NGOs and tenders | `web development company islamabad` | website design islamabad; web developer rawalpindi; ngo website islamabad | L/C | PK | /digital/contact | Real twin-city facts (consultancies, NGOs, government-facing suppliers), donor reporting needs, remote working |

### Part 3: posts #63–#82

| # | Slug (exact) | File prefix | Category | Topic and angle | Primary keyword | Cluster seeds | Intent | Aud | Link | Must include |
|---|---|---|---|---|---|---|---|---|---|---|
| 63 | `website-design-sialkot-exporters` | `f63_` | Local Guides | Sialkot exporters: websites that win international buyers | `website design sialkot` | web development sialkot; sialkot exporter website; sports goods website | L/C | PK | /digital/business-websites | Sialkot export sectors (sports goods, surgical instruments, leather), B2B buyer needs, link #51 |
| 64 | `web-development-faisalabad-textile` | `f64_` | Local Guides | Faisalabad textile businesses: B2B websites and catalogues | `web development faisalabad` | website design faisalabad; textile company website; fabric catalogue website | L/C | PK | /digital/business-websites | Textile and garment manufacturing base, catalogue and RFQ needs, link #52 |
| 65 | `website-design-gujranwala-manufacturers` | `f65_` | Local Guides | Gujranwala manufacturers: product catalogue websites | `website design gujranwala` | web development gujranwala; manufacturer website gujranwala | L/C | PK | /digital/business-websites | Local manufacturing sectors (fans, cutlery, sanitary ware), dealer networks, catalogue needs |
| 66 | `web-development-multan` | `f66_` | Local Guides | Multan businesses online: agri, mango exports and retail | `web development multan` | website design multan; agri business website; mango export website | L/C | PK | /digital/business-websites | Agri dealers, mango exporters, retail; seasonal export buyers |
| 67 | `website-design-peshawar` | `f67_` | Local Guides | Peshawar traders: websites for wholesale and cross-border trade | `website design peshawar` | web development peshawar; wholesale website; marble company website | L/C | PK | /digital/business-websites | Wholesale markets, marble and handicraft trade, Urdu/Pashto-speaking customers, remote working |
| 68 | `ecommerce-website-lahore-retail-brands` | `f68_` | Local Guides | Lahore retail brands: from mall stores to online | `ecommerce website lahore` | online store lahore; boutique website lahore; fashion website lahore | L/C | PK | /digital/ecommerce-development | Lahore fashion and boutique retail, launch-day traffic, store pickup option, office visit possible, link #42 |
| 69 | `clinic-website-lahore` | `f69_` | Local Guides | Lahore clinics in DHA, Johar Town and Model Town: getting booked online | `clinic website lahore` | doctor website lahore; clinic seo lahore; online appointment lahore | L/C | PK | /digital/business-websites | Map pack, reviews, area pages done honestly, link #45 and #84; distinct from #45 (local discovery focus) |
| 70 | `website-designer-near-me-lahore` | `f70_` | Local Guides | Website designer near me (Lahore): how to pick and what to expect | `website designer near me` | web designer lahore; website company near me; meet web developer lahore | L/T | PK | /digital/web-development-lahore | Office visit, Google Business Profile check, response times, what a first meeting covers; link #14 |
| 71 | `hire-pakistani-web-developers` | `g71_` | Working With Overseas Clients | Hiring web developers from Pakistan: costs, risks and how to do it safely (PILLAR) | `hire pakistani web developers` | outsource web development pakistan; offshore web development; pakistani developers for hire; web development outsourcing | C | OS | /digital/contact | Risk checklist, contracts, IP, payments, time zones, communication; honest trade-offs; link to all G spokes |
| 72 | `white-label-web-development-pakistan` | `g72_` | Working With Overseas Clients | White-label web development: how agencies work with a Pakistani team | `white label web development` | white label website agency; reseller web development; outsourced web development for agencies | C/T | OS | /digital/contact | NDA, QA process, sample workflow, branding rules, communication cadence |
| 73 | `dedicated-developer-vs-fixed-project` | `g73_` | Working With Overseas Clients | Dedicated developer vs fixed project: which model fits your agency? | `dedicated developer model` | hire dedicated developer; dedicated team vs project based; monthly developer retainer | C | OS | /digital/web-app-development | Cost scenarios labelled illustrative, management overhead, link #18 |
| 74 | `offshore-team-time-zones-lahore` | `g74_` | Working With Overseas Clients | Time zones and communication: working with a Lahore team from the UK, US and Gulf | `offshore team time zone` | working hours overlap pakistan; communicate with offshore developers; lahore time zone | I | OS | /digital/contact | Overlap-hour table (UK summer/winter, US East/West, UAE, Saudi) computed from UTC+5, meeting cadence |
| 75 | `outsourcing-website-ip-nda-code-ownership` | `g75_` | Working With Overseas Clients | IP, NDA and code ownership when outsourcing a website | `outsourcing contract ip ownership` | nda for software development; who owns code outsourcing; ip assignment clause | C | OS | /digital/contact | Clause examples in plain English, WIPO source, not legal advice; link #16 #17 |
| 76 | `pay-web-developer-in-pakistan` | `g76_` | Working With Overseas Clients | How overseas clients pay a Pakistani agency (wire, Wise, Payoneer) | `pay developer in pakistan` | send money to pakistan developer; pay pakistani freelancer; international payment to pakistan agency | I | OS | /digital/pricing | Steps for each method from official sites, invoice in PKR, milestone schedule; no tax content |
| 77 | `arabic-rtl-website-development` | `g77_` | Working With Overseas Clients | Arabic (RTL) website development for Gulf businesses | `arabic website development` | rtl website design; bilingual arabic english website; arabic website cost | C | OS | /digital/business-websites | RTL checklist, W3C dir guidance, hreflang, fonts, translation; link #10 |
| 78 | `shopify-developer-uae-saudi` | `g78_` | Working With Overseas Clients | Shopify experts for UAE and Saudi stores: payments and shipping | `shopify developer uae` | shopify store uae; shopify saudi arabia; shopify expert dubai | C | OS | /digital/ecommerce-development | Gulf payments and shipping from Shopify Help sources, Arabic store, link #3 #24 |
| 79 | `uk-small-business-website-offshore` | `g79_` | Working With Overseas Clients | UK small business websites: offshore quality without agency prices | `web design uk small business` | small business website uk; affordable web design uk; outsource website uk | C | OS | /digital/business-websites | UK GDPR basics (ICO source), cookie consent, accessibility, link #9 |
| 80 | `small-business-website-canada-offshore` | `g80_` | Working With Overseas Clients | Canadian small business website: building with an offshore team | `website for small business canada` | web design canada small business; outsource website canada; aoda website | C | OS | /digital/business-websites | AODA basics (Ontario source), bilingual EN/FR note, time zones |
| 81 | `overseas-pakistanis-business-website-setup` | `g81_` | Working With Overseas Clients | Overseas Pakistanis starting a business back home: website and online setup | `start business in pakistan from abroad website` | overseas pakistani online business; manage website in pakistan from abroad; remote business setup pakistan | C | OS | /digital/contact | Website, domain (.pk via PKNIC facts), hosting, payments, WhatsApp, remote management ONLY; any paperwork -> 'your accountant or adviser'; zero tax words |
| 82 | `mvp-development-startups` | `g82_` | Working With Overseas Clients | MVP development for startups: scope, cost and a 6-week plan | `mvp development company` | mvp development cost; minimum viable product web app; startup mvp pakistan | C/T | OS | /digital/web-app-development | Week-by-week plan table, scope cuts, P['app'], Agile Alliance MVP source |

### Part 4: posts #83–#100

| # | Slug (exact) | File prefix | Category | Topic and angle | Primary keyword | Cluster seeds | Intent | Aud | Link | Must include |
|---|---|---|---|---|---|---|---|---|---|---|
| 83 | `get-business-website-on-google` | `h83_` | Getting Found Online | How to get your business website on Google (Pakistan guide) (PILLAR) | `website on google` | google par business kaise laye; get website indexed; business on google search; how to show website on google | I | PK | /digital/business-websites | Indexing (Search Console, sitemap), Business Profile, reviews, content, links; 30-day plan table; link to all H spokes |
| 84 | `google-business-profile-pakistan` | `h84_` | Getting Found Online | Google Business Profile for Pakistani businesses: setup and verification | `google business profile pakistan` | google my business pakistan; verify business on google maps; google maps listing | I | PK | /digital/web-development-lahore | Setup and verification steps from Google Help, common Pakistan issues (address format, phone), reviews |
| 85 | `seo-ready-website-checklist` | `h85_` | Getting Found Online | SEO-ready website: the 15 things built in before launch | `seo friendly website development` | seo ready website; technical seo checklist; website seo basics | C | PK/OS | /digital/business-websites | 15-point checklist table with schema example in plain words; Google SEO starter guide source |
| 86 | `ai-search-visibility-for-business` | `h86_` | Getting Found Online | Getting your business mentioned by ChatGPT, Gemini and AI Overviews | `ai search visibility for business` | generative engine optimization; appear in ai overviews; chatgpt business mention | I | PK/OS | /digital/business-websites | Google AI features doc source, entity consistency, quotable facts, llms.txt explained; no guarantees |
| 87 | `schema-markup-business-websites` | `h87_` | Getting Found Online | Schema markup for business websites explained simply | `schema markup for business websites` | local business schema; structured data for small business; faq schema | I | PK/OS | /digital/business-websites | Plain explanation, which types matter (Organization, LocalBusiness, FAQPage, Product, BreadcrumbList), validators; no code blocks (describe fields in a table) |
| 88 | `website-speed-pakistan-mobile` | `h88_` | Getting Found Online | Website speed for Pakistani mobile users: what actually matters | `website speed optimization` | core web vitals; page speed pakistan; mobile website speed | I | PK | /digital/business-websites | Core Web Vitals thresholds from web.dev, testing on 4G and mid-range Android, priorities; strategy angle (differs from #95) |
| 89 | `website-visitors-no-enquiries` | `h89_` | Getting Found Online | Website gets visitors but no enquiries: 12 fixes | `website no enquiries` | website traffic no leads; website not converting; increase website enquiries | I | PK/OS | /digital/contact | 12-fix conversion audit table, WhatsApp/call buttons, forms, trust signals, link #90 |
| 90 | `whatsapp-button-website-leads` | `h90_` | Getting Found Online | WhatsApp leads from your website: buttons, pre-filled messages and tracking | `whatsapp button website` | whatsapp chat button; click to chat link; track whatsapp clicks ga4 | I | PK | /digital/business-websites | wa.me link format (WhatsApp FAQ source), pre-filled message examples, GA4 event tracking steps (Google Help source) |
| 91 | `website-hacked-what-to-do` | `i91_` | Fix a Problem | My website was hacked: the first 24 hours | `website hacked what to do` | hacked website recovery; website malware removal; wordpress site hacked | I | PK/OS | /digital/pricing | Hour-by-hour steps table, who to contact, restore from backup, Google Search Console security issues; P['maint'] |
| 92 | `website-security-checklist-small-business` | `i92_` | Fix a Problem | Website security checklist for small businesses | `website security checklist` | secure website tips; wordpress security checklist; small business website security | I | PK/OS | /digital/pricing | Checklist table (updates, passwords, 2FA, backups, SSL, access), OWASP and WordPress hardening sources |
| 93 | `website-down-check` | `i93_` | Fix a Problem | Website down? How to find the cause in 10 minutes | `website down check` | why is my website not opening; website not working; site down for me | I | PK/OS | /digital/pricing | Diagnostic flow: domain expiry, DNS, hosting, SSL, plugin errors; who to call for each |
| 94 | `new-website-without-losing-google-traffic` | `i94_` | Fix a Problem | Moving to a new website without losing Google traffic | `website redesign without losing traffic` | website migration seo; redirect map; change website without losing ranking | I | PK/OS | /digital/business-websites | Redirect map template table, Google site-move sources; distinct from #11 (process, not cost) |
| 95 | `website-slow-on-mobile` | `i95_` | Fix a Problem | Website slow on mobile? Causes and fixes | `website slow on mobile` | website slow kyun hai; slow website fix; website loading slow; speed up wordpress site | I | PK | /digital/business-websites | Cause -> fix table (images, hosting, plugins, fonts, scripts), before/after example labelled illustrative; troubleshooting angle (differs from #88) |
| 96 | `website-backups-small-business` | `i96_` | Fix a Problem | Website backups: how often and where | `website backup` | website backup frequency; 3-2-1 backup rule; how to backup website | I | PK/OS | /digital/pricing | 3-2-1 rule for small businesses, frequency by site type table, test restores; WordPress backup source |
| 97 | `how-long-to-build-a-website` | `j97_` | Planning & Launch | How long does it take to build a website? Realistic timelines | `how long to build a website` | website development time; website kitne din mein banti hai; website project timeline | I | PK/OS | /digital/pricing | Timeline table by type (landing, starter, business, store, app) matching our packages, what delays projects |
| 98 | `pages-for-small-business-website` | `j98_` | Planning & Launch | What pages does a small business website need? | `pages for business website` | business website pages list; website sitemap example; essential website pages | I | PK/OS | /digital/business-websites | Page lists by industry (clinic, shop, consultant, manufacturer), what each page must contain |
| 99 | `website-accessibility-basics` | `j99_` | Planning & Launch | Website accessibility (WCAG) basics for business owners | `website accessibility basics` | wcag checklist; accessible website design; ada website compliance | I | OS | /digital/business-websites | 10-point checklist from W3C WCAG 2.2, why it helps SEO and sales, legal notes only with sources (UK, Ontario) |
| 100 | `website-launch-checklist` | `j100_` | Planning & Launch | Website launch checklist: 40 checks before going live | `website launch checklist` | go live checklist; pre launch website checklist; website testing checklist | I/T | PK/OS | /digital/contact | 40 checks grouped (content, SEO, speed, security, forms, tracking, legal, backups) in tables; link #22 #85 |

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
"""Kamboh Associates Digital: blog post auditor.

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
PILLARS = {1, 13, 23, 33, 45, 71, 83}
SERVICE_PATHS = {"/digital", "/digital/business-websites", "/digital/ecommerce-development", "/digital/web-app-development",
                 "/digital/pricing", "/digital/web-development-lahore", "/digital/contact", "/digital/blog"}
CATEGORIES = {"Costs & Budgets", "Hiring a Developer", "Platforms & Comparisons", "E-commerce in Pakistan", "Websites by Industry",
              "Local Guides", "Working With Overseas Clients", "Getting Found Online", "Fix a Problem", "Planning & Launch"}
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
    for name, p in posts:
        f, w = audit(p)
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
