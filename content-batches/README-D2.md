# Part 3 — Batch D2 (posts D06–D10)

## Is ZIP mein kya hai
```
posts/p-d06.js  Wealth Statement Revise Karna
posts/p-d07.js  Return Reject Ya Invalid Ho Gaya
posts/p-d08.js  Wealth Reconciliation Match Nahi Ho Rahi
posts/p-d09.js  IRIS Profile Mein Ghalat Detail
posts/p-d10.js  Ghalat Tax Year Mein Return File Ho Gaya
batch-D2.js     posts ko ek array mein jama karta hai
validate.js     validator (11 checks)
wire-snippets.js  blogs.html + sitemap.xml snippets
```

## Nateeja
```
5 posts, 0 errors, 0 warnings
2000-2022 words har post
Highest pairwise overlap: 1.0% (threshold 15%)
```

## Chalane ka tareeqa
```bash
node validate.js batch-D2.js
# cross-batch check ke liye — jab sab parts mil jayein:
# node validate.js batch-C1.js batch-C2.js batch-D1.js batch-D2.js batch-D3.js
node wire-snippets.js batch-D2.js
```

## Yeh batch D01–D05 se kaise juda hai

Yeh Section D (Filing Corrections) ka doosra hissa hai. D01–D05 pehle deliver ho chuke hain
(revised return, return correction options, IRIS errors, Section 7E, backlog catch-up).
D06–D10 usi thread ko aage barhate hain: wealth statement revision, invalid returns,
reconciliation fixing, profile updates, aur galat tax year — sab ek doosre se related
lekin har ek ka apna alag, differentiated angle hai (jaisa D01–D05 ke README mein bataya gaya tha).

Cross-links D01–D05 ki taraf already lage hain (jaise D06 → D01 revised-return,
D07 → D03 IRIS-errors, D08 → D02 aur D06, D09 → fbr-notice-guide, D10 → D01 aur D02).

## Baqi Section D
D11–D15 (5 posts) abhi baqi hain — poora Section D (15/15) mukammal hone ke baad
Section E (NTN + First-Return bundles) shuru hoga. Poora 65-post plan
`plan-sections-C-to-H.md` mein hai (Part 1 ki ZIP mein).
