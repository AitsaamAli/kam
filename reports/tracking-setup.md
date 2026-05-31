# SEO Tracking Setup — KambohAssociates.com
**Date:** 2026-05-31

---

## 1. Google Search Console

**Setup Steps:**
1. Go to search.google.com/search-console
2. Add property: https://kambohassociates.com
3. Verify via HTML tag in `<head>` of index.html
4. Submit sitemap: https://kambohassociates.com/sitemap.xml

**Weekly Queries to Monitor:**
- "tax consultant Lahore" — target: Page 1, Top 3
- "NTN registration Pakistan" — target: Page 1
- "income tax return filing Pakistan" — target: Page 1
- "filer vs non-filer Pakistan" — target: Featured Snippet
- "how to become active taxpayer Pakistan" — target: Position Zero

**Monthly Actions:**
- Check Coverage tab for crawl errors
- Check Core Web Vitals tab for LCP/INP/CLS issues
- Download top performing queries CSV and update content

---

## 2. Google Analytics 4

**Key Events to Configure:**

| Event Name | Trigger | Goal |
|------------|---------|------|
| whatsapp_click | Click on WhatsApp button | Lead |
| phone_call | Click on phone number | Lead |
| contact_form_submit | Form submission on contact section | Conversion |
| blog_read_50pct | User scrolls 50% of blog post | Engagement |
| calculator_used | User completes tax calculation | Tool usage |

**Custom Dimensions:**
- Page type: homepage / service / blog / calculator
- User intent: informational / commercial
- Traffic source: organic / social / direct / referral

---

## 3. Rank Tracking (Free Tools)

**Google Search Console** — Free, most accurate for your site
- Check "Performance" → "Search results" weekly
- Filter by country: Pakistan

**SERPWatcher by Mangools** (paid, ~$29/month)
- Track 30 keywords daily
- Mobile vs desktop split

**Ubersuggest** — Free tier available
- Track 3 keywords for free

---

## 4. Core Web Vitals Monitoring

**Check monthly at:**
- PageSpeed Insights: pagespeed.web.dev
- Test both mobile and desktop
- Target scores: Performance 90+, Accessibility 90+, SEO 100

**Current expected scores** (estimate based on audit):
- LCP: Medium (PNG images, no WebP = slow) → Target: Convert to WebP
- INP: Good (minimal JS)
- CLS: Good (fixed widths on most elements)

---

## 5. Monthly SEO Checklist

### Week 1 — Technical Health
- [ ] Check Google Search Console for new errors
- [ ] Check any 404 errors and fix redirects
- [ ] Review top 10 queries — any new opportunities?
- [ ] Check Core Web Vitals for regressions

### Week 2 — Content
- [ ] Publish one new cluster article from content plan
- [ ] Update 1 existing blog with fresh data (new FBR numbers, etc.)
- [ ] Add internal links from new post to service pages

### Week 3 — Authority
- [ ] Add 1-2 new business directory citations
- [ ] Reply to all Google reviews
- [ ] Post 1 Google Business Profile update
- [ ] Check for new link opportunities in GSC

### Week 4 — Analysis
- [ ] Review monthly ranking changes
- [ ] Compare traffic month-over-month
- [ ] Update keywords.md with new opportunities found
- [ ] Plan next month's content topic
