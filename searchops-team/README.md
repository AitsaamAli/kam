# SearchOps Team — kaise use karein

Ye folder aik "skill package" hai — 60 SEO/AEO/GEO specialists ki
instructions, text files ki shakl mein. Ismein koi app ya server nahi hai;
ye sirf Claude ke liye directions hain.

## Setup (ek dafa, har naye project mein)

1. `searchops-team` folder ko apne project ke root mein paste kar dein.
   - Claude Code use kar rahe hain to: seedha project folder mein daal dein.
   - Claude.ai (web/app) use kar rahe hain to: is poore folder ko project
     ke files ke saath upload kar dein, ya Claude Code/Desktop use karein
     taake Claude khud project ki files parh sake.
2. Claude ko bolein: **"searchops-team/SKILL.md parho aur is project ko
   study karo"**

Bas. Claude khud project ki files, content, aur agar mojood ho to
keyword/analytics data parh lega, phir usi ke mutabiq kaam karega —
generic jawab nahi dega.

## Roz mara istemal

- Kisi khaas specialist se kaam lena ho:
  **"Technical Auditor chalao is project par"**
  ya
  **"Schema Engineer se product pages ka schema likhwao"**

- Poori team ka pehla pass chahiye ho (naya project):
  **"onboard workflow chalao"**

- **Hafte mein 2 dafa regular chalana ho** (growth ke liye):
  **"searchops-team/CADENCE.md ke hisab se aaj ka session chalao"**
  Ye system 8 hafton ka pehla cycle chalata hai (foundation → keywords →
  content → AI visibility → links → results review), phir har session
  `growth-tracker.md` dekh kar decide karta hai ke agla sabse zaroori kaam
  kya hai — dobara wahi cheez nahi karta, aage badhta hai.

- AI answers (ChatGPT/Gemini/Perplexity) mein nazar aana ho:
  **"ai-sprint workflow chalao"**

- Kisi masla ka pata nahi kis specialist ka kaam hai:
  **"ye page rank kyun nahi kar raha, jo bhi specialist chahiye chalao"**
  — Claude khud `ROLES.md` se sahi banda chun lega.

Har role ka poora detail `ROLES.md` mein hai, aur 6 ready workflows
`WORKFLOWS.md` mein hain.

`KNOWLEDGE.md` mein 20+ saal ke tajurbekar practitioner ki deep knowledge
hai — real Core Web Vitals thresholds, hreflang ke asal bugs, migration ki
sahi sequence, GEO (AI answers) ki working tactics, aur international/
multi-market projects (Pakistan, Gulf, wagera) ke real patterns. Har
specialist iska relevant hissa parh kar apna kaam karta hai — isi liye
jawab generic textbook advice nahi lagta, balke asal experience jaisa
lagta hai.

`OPERATOR-CONTEXT.md` mein aapke apne kaam karne ka tareeqa mehfooz hai —
budget (near-zero, ~$5/mo ceiling), market (Pakistan, Urdu/Roman Urdu),
aur quality bar ("AI-generated" na lage, commercial-grade ho). Har
specialist ye default maan kar chalta hai, jab tak current project ki
brief kuch alag na kahe.

`ACCURACY-PROTOCOL.md` har deliverable ko final hone se pehle check karta
hai — har number/claim ko verified, estimated, ya assumption tag lagta
hai, code ko real project ke against trace karta hai, aur multi-role
sessions mein specialists ek dosre se contradict to nahi kar rahe ye check
karta hai. Iski wajah se jitna zyada aap chalao, output utna hi zyada
bharosemand rehta hai — sirf zyada nahi, sahi bhi.

## Brief

`briefs/current.md` mein project ki basic info hai — business, audience,
competitors, goal, constraints. Claude jo khud project se pata laga sakta
hai woh khud bhar dega; baqi aap se poochega. Jab project badle (naya
market, naya goal), ye file khud update kar dein ya Claude ko update karne
ko kahein.

## Kaam ka record

Jo bhi report ya strategy specialist banata hai, woh
`briefs/deliverables/` mein save hoti rehti hai — taake agli baar Claude
(ya koi doosra specialist) pichla kaam parh kar aage badhe, dobara se
shuru na kare.

## Zaroori baat

1. **Ye sirf websites ke liye hai** — marketing site, content site,
   ecommerce, SaaS ki landing/docs site, blog. Apne product ke internal
   app code (jaise POS app ki screens) mein mat daalein — sirf uski
   marketing website mein.
2. **KNOWLEDGE.md ki cheezein time-sensitive hain.** SEO/AEO/GEO har mahine
   badalta hai — jo thresholds/dates ismein likhi hain woh snapshot hain,
   guaranteed current fact nahi. Agar Claude ke paas web search on ho to
   woh khud verify karega; agar na ho, to aap khud confirm kar lein
   critical decisions se pehle (jaise schema hatana ya redirect strategy).
3. **Koi bhi system "guaranteed max traffic" nahi de sakta.** Google/AI
   platforms decide karte hain, aur asal results iss par depend karte hain
   ke content actually publish hota hai, technical fixes actually
   implement hote hain, aur consistency maintain hoti hai. Real, sustained
   traffic mein aam tor par 3-6 mahine lagte hain naye/kam-authority site
   ke liye — cadence system isi hisab se banaya gaya hai, koi shortcut
   nahi hai.

Real numbers (Search Console, analytics, server logs) inke paas khud se
nahi aate; jo data aap paste ya upload karenge, wahi istemal hoga. Jhoothay
figures kabhi nahi banaye jayenge.
