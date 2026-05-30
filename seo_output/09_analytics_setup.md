# TASK 9 — ANALYTICS & TRACKING SETUP
# kambohassociates.com | Tax Consultancy | Lahore, Pakistan
# Generated: 2026-05-30

---

## A) GOOGLE ANALYTICS 4 SETUP

### Step 1: Create GA4 Property
1. Go to analytics.google.com
2. Click Admin → Create Property
3. Property Name: `Kamboh Associates`
4. Country: Pakistan | Currency: Pakistani Rupee (PKR)
5. Industry: Finance
6. Click Next → Create

### Step 2: Get Your Measurement ID
- After creating, go to Admin → Data Streams → Web
- Add stream: `kambohassociates.com`
- Copy your **Measurement ID** (format: `G-XXXXXXXXXX`)

### Step 3: Install GA4 on Every Page

Add this code in the `<head>` section of ALL HTML pages, BEFORE the closing `</head>` tag:

```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX', {
    'page_location': window.location.href,
    'page_title': document.title,
    'send_page_view': true
  });
</script>
```

Replace `G-XXXXXXXXXX` with your actual Measurement ID.

**Files to update (add GA4 code):**
- index.html
- blogs.html
- All 24 blog HTML pages (use Node.js batch script below)

### Node.js Batch Script to Add GA4 to All Pages
```javascript
const fs = require('fs');
const path = require('path');

const GA_CODE = `<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>`;

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));
files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  if (!content.includes('G-XXXXXXXXXX')) {
    content = content.replace('</head>', GA_CODE + '\n</head>');
    fs.writeFileSync(file, content);
    console.log('Updated:', file);
  }
});
```
Run: `node add_ga4.js` from the project root directory.

---

## B) CONVERSION EVENTS TO TRACK

### 1. Phone Number Click
```javascript
document.querySelectorAll('a[href^="tel:"]').forEach(function(link) {
  link.addEventListener('click', function() {
    gtag('event', 'phone_click', {
      'event_category': 'Contact',
      'event_label': this.href
    });
  });
});
```

### 2. WhatsApp Button Click
```javascript
document.querySelectorAll('a[href*="wa.me"]').forEach(function(link) {
  link.addEventListener('click', function() {
    gtag('event', 'whatsapp_click', {
      'event_category': 'Contact',
      'event_label': 'WhatsApp'
    });
  });
});
```

### 3. Email Click
```javascript
document.querySelectorAll('a[href^="mailto:"]').forEach(function(link) {
  link.addEventListener('click', function() {
    gtag('event', 'email_click', {
      'event_category': 'Contact',
      'event_label': this.href
    });
  });
});
```

### 4. CTA Button Click (Get Quote / Consult Now)
```javascript
document.querySelectorAll('.btn-primary, .cta-btn, [data-cta]').forEach(function(btn) {
  btn.addEventListener('click', function() {
    gtag('event', 'cta_click', {
      'event_category': 'Engagement',
      'event_label': this.textContent.trim()
    });
  });
});
```

### 5. Time on Page (2+ Minutes = Engaged User)
```javascript
setTimeout(function() {
  gtag('event', 'engaged_user', {
    'event_category': 'Engagement',
    'event_label': document.title,
    'value': 120
  });
}, 120000); // 2 minutes
```

### 6. Blog Article Read (75% Scroll)
```javascript
let fired75 = false;
window.addEventListener('scroll', function() {
  const scrolled = (window.scrollY + window.innerHeight) / document.body.scrollHeight;
  if (scrolled >= 0.75 && !fired75) {
    fired75 = true;
    gtag('event', 'article_read', {
      'event_category': 'Blog',
      'event_label': document.title
    });
  }
});
```

**Add all event tracking code** just before `</body>` in index.html and blogs.html.

---

## C) GOOGLE SEARCH CONSOLE SETUP

### Step 1: Add Property
1. Go to search.google.com/search-console
2. Click Add Property
3. Enter: `https://kambohassociates.com`
4. Choose verification method

### Verification Methods (Pick One):
**Option A — HTML Tag (Easiest for Static Sites)**
- GSC provides a meta tag: `<meta name="google-site-verification" content="XXXXX"/>`
- Add it in `<head>` of index.html
- Click Verify in GSC

**Option B — DNS Verification**
- GSC provides a TXT record
- Add it in your domain DNS settings (Namecheap / GoDaddy / etc.)
- Usually takes 30 minutes

### Step 2: Submit Sitemap
1. In GSC, go to Sitemaps
2. Enter: `https://kambohassociates.com/sitemap.xml`
3. Click Submit
4. Google will start crawling within 24-72 hours

### Step 3: Submit Individual URLs (New Blog Pages)
1. GSC → URL Inspection
2. Enter each new blog URL
3. Click "Request Indexing"
4. Do this for all 5 new pages:
   - https://kambohassociates.com/youtube-monetization-tax-pakistan
   - https://kambohassociates.com/tiktok-creator-tax-pakistan
   - https://kambohassociates.com/digital-marketing-agency-tax-pakistan
   - https://kambohassociates.com/software-house-tax-pakistan
   - https://kambohassociates.com/secp-vs-sole-proprietorship-pakistan

---

## D) MONTHLY SEO REPORTING TEMPLATE

| Metric | Where to Find | Target | Notes |
|--------|-------------|--------|-------|
| Organic Sessions | GA4 → Reports → Acquisition | +20% MoM | Main growth metric |
| New Users | GA4 → Overview | +15% MoM | New audience growth |
| Bounce Rate | GA4 → Engagement | < 65% | Lower = better |
| Avg Session Duration | GA4 → Engagement | > 2 min | Content quality |
| Pages/Session | GA4 → Engagement | > 2 | Internal linking |
| Goal Completions (Calls) | GA4 → Events | +10% MoM | Revenue metric |
| WhatsApp Clicks | GA4 → Events | +10% MoM | Key conversion |
| Top Landing Pages | GA4 → Landing Pages | Track changes | SEO wins |
| Clicks (GSC) | Search Console → Performance | +15% MoM | Visibility |
| Impressions (GSC) | Search Console → Performance | +20% MoM | Reach |
| Average Position | Search Console → Performance | Aim for < 20 | Rankings |
| CTR (Click-Through Rate) | Search Console → Performance | > 3% | Title/desc quality |
| Top Queries | Search Console → Queries | Track new ones | Keyword opportunities |
| Index Coverage | GSC → Index → Coverage | 0 errors | Technical health |
| Core Web Vitals | GSC → Experience | All green | Page speed |
| Mobile Usability | GSC → Experience | 0 errors | Mobile SEO |
| Backlinks | Ahrefs free / Moz | +5/month | Authority building |
| Domain Authority | Moz free | Improving | Long-term |
| Keyword Rankings | Ubersuggest free | Track top 20 | SEO progress |
| Google Business Views | GMB Insights | +10% MoM | Local SEO |

---

## E) WEEKLY SEO TASK CHECKLIST

### Every Monday
- [ ] Check Google Search Console for new errors (Coverage tab)
- [ ] Check for manual actions or penalties
- [ ] Review top performing pages last week
- [ ] Check keyword position changes (top 10 keywords)

### Every Wednesday
- [ ] Publish or update 1 blog post
- [ ] Add 1 Google My Business post
- [ ] Reply to all Google reviews (positive + negative)
- [ ] Check for new backlinks (Ahrefs free)

### Every Friday
- [ ] Check Core Web Vitals report in GSC
- [ ] Review WhatsApp + phone click events in GA4
- [ ] Update GMB hours / info if anything changed
- [ ] Add internal links from new blog to older related posts

### Every Month (1st Week)
- [ ] Full monthly report (all metrics above)
- [ ] Check sitemap for any new pages to add
- [ ] Review and update meta descriptions for low CTR pages
- [ ] Submit any new URLs to GSC for indexing
- [ ] Check and respond to all citation mentions online
- [ ] Request Google reviews from happy clients that month
