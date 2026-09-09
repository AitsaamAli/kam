# Part 1 — Sections C-H Plan + Batch C1 (posts C01-C05)

## Is ZIP mein kya hai

```
plan-sections-C-to-H.md    <- sab 65 posts ke finalized titles + slugs + 13-part batch plan
posts/p-c01.js ... p-c05.js <- 5 mukammal posts (generator data objects)
batch-C1.js                 <- posts ko ek array mein jama karta hai
validate.js                 <- validator (11 checks)
wire-snippets.js            <- blogs.html + sitemap.xml ke ready snippets print karta hai
README.md                   <- yeh file
```

## Repo mein kahan rakhna hai

`C:\Users\786\Desktop\kam` mein `content-batches\` folder bana kar poora ZIP wahan khol dein.
Yeh files site ka hissa nahi banti — yeh production input hain. `blogs/*.html` khud generator banata hai.

## Chalane ka tareeqa

```bash
cd C:\Users\786\Desktop\kam\content-batches

# 1) validate (sirf yeh batch)
node validate.js batch-C1.js

# 2) cross-batch overlap — agle parts ke baad SAB batch files ek sath dein
node validate.js batch-C1.js batch-C2.js batch-D1.js

# 3) HTML banayein apne maujooda MINIFIED-family generator se
node your-generator.js batch-C1.js

# 4) blogs.html + sitemap.xml ke snippets
node wire-snippets.js batch-C1.js
```

**Ahem:** HTML shell is ZIP mein shamil nahi hai — jaan bujh kar. MINIFIED-family ka asal CSS
repo ke maujooda country-cluster generator mein hai. Usay yahan dobara likhna ghalat hota,
kyunke halki si tabdeeli bhi baqi 35 files se template drift bana deti. Data object ki shape
`08-production-pipeline-and-tools.md` wale schema se bilkul match karti hai — seedha plug ho jayega.

## Validator kya check karta hai

| # | Check | Threshold |
|---|---|---|
| 1 | Required fields + types | schema ke mutabiq |
| 2 | Word count | >= 2000 |
| 3 | HTML tag balance | div/table/tr/td/th/ul/li/p/h2/h3/strong/em/span/a |
| 4 | TOC anchor resolution | dono taraf (toc -> body, body -> toc) |
| 5 | JSON serializability | pass/fail |
| 6 | Non-ASCII scan | sirf allowlisted typographic chars |
| 7 | FAQ count | >= 5, q/a dono non-empty |
| 8 | Slug uniqueness + format | lowercase/digits/hyphen |
| 9 | WhatsApp number | 923284675162 |
| 10 | Banned phrases | "late filer", og:image, dark-mode CSS |
| 11 | 6-word shingle overlap | >= 15% = HIGH OVERLAP |

Check #3 khaas tor par `.ib` aur `.wb` callout boxes ka woh purana unclosed-div bug pakadta hai
jo pichle batches mein baar baar aaya tha. Check #10 is liye hai ke Finance Act 2026 ke baad
"late filer" category maujood nahi rahi.

## Batch C1 ka nateeja

```
=== 5 posts, 0 errors, 0 warnings ===

  2715  sirf-rental-income-tax-return-filing-pakistan-2026
  2427  joint-property-co-owner-tax-return-share-pakistan-2026
  2509  wirasat-inherited-property-wealth-statement-return-pakistan-2026
  2347  prize-bond-lottery-jeet-tax-return-declaration-pakistan-2026
  2384  salary-rental-business-multiple-income-tax-return-pakistan-2026

Highest pairwise overlap: 1.2%  (threshold 15%)
```

## Editorial faisle jo is batch mein liye gaye

- **Koi bhi tax rate ya slab body mein nahi.** Har jagah mechanism samjhaya gaya hai aur reader ko
  FBR ke maujooda Withholding Tax Rate Card ya firm ki taraf bheja gaya hai. Wajah wohi hai jo
  pichle batch mein thi — Finance Act har saal figures badal deta hai aur post purani ho jati hai.
- **Non-filer ka farq "double" nahi likha gaya.** Sirf "numaya zyada" aur "Finance Act 2026 ke baad
  pehle se barh chuka" likha hai, kyunke asal gap 4-7 guna nikla tha. (Yeh wohi cheez hai jo abhi
  31 country cluster posts par live theek karni baqi hai.)
- **Filing deadline 30 September** likhi gayi hai, 30 June nahi.
- **ATL rozana update** hota hai, "har Monday" nahi — SRO 1638(I)/2024 ke mutabiq.
- **Fees sirf real schedule se:** return Rs. 3,500-5,000, wealth statement Rs. 2,500,
  NTN Rs. 2,000, STRN Rs. 3,000. Corporate return ka zikr jaan bujh kar nahi kiya —
  live site (Rs. 20,000) aur planning docs (Rs. 15,000) mein abhi tak farq hai, woh pehle
  reconcile hona chahiye.
- **Do related links badle gaye.** C01 aur C02 se ek ek link aise posts par ja raha tha jo abhi
  likhe nahi gaye (C10 aur E07). Unki jagah `/fbr-notice-guide-pakistan` daal diya hai taake yeh
  batch akele bhi publish ho to koi broken link na bane. Jab Part 2 aur Part 6 aayenge, tab
  cross-links wapas add kar lenge.

## Publish se pehle (project ka standard gate)

1. `node validate.js` sab batch files ke sath — 0 errors.
2. Generator se HTML banaein.
3. `blogs.html` ke **dono** mechanism update karein (JS array + static alphabetical list).
4. `sitemap.xml` mein `<url>` blocks daalein.
5. `site-health-check.js` chalaein — `/pricing` aur chaaron pillar pages ka canonical confirm karein.
6. Word count **commit se theek pehle** dobara verify karein.
7. Chhota, per-batch commit.

## Aage kya

Part 2 = C06-C10 (`batch-C2.js`). Poora 13-part schedule `plan-sections-C-to-H.md` ke aakhir mein hai.
