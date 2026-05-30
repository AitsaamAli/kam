# TASK 5 — TECHNICAL SEO CHECKLIST
# kambohassociates.com | Tax Consultancy | Lahore, Pakistan
# Generated: 2026-05-30

---

## 50-POINT TECHNICAL SEO CHECKLIST

| # | Issue | How to Check | How to Fix | Priority | Status |
|---|-------|-------------|------------|----------|--------|
| 1 | HTTPS enabled | Check URL bar | Vercel auto-HTTPS ✅ | HIGH | ✅ DONE |
| 2 | www → non-www redirect | Browser test | Vercel handles auto | HIGH | ✅ DONE |
| 3 | sitemap.xml exists | /sitemap.xml | ✅ Created | HIGH | ✅ DONE |
| 4 | robots.txt exists | /robots.txt | ✅ Created | HIGH | ✅ DONE |
| 5 | Sitemap submitted to Google | Search Console | Submit at GSC | HIGH | ❌ TODO |
| 6 | Sitemap submitted to Bing | Bing Webmaster | Submit at BWC | MEDIUM | ❌ TODO |
| 7 | Canonical tags on all pages | Grep `rel="canonical"` | All blog pages have it ✅ | HIGH | ✅ DONE |
| 8 | Title tags 50-60 chars | Screaming Frog | See 02_meta_tags.md | HIGH | ✅ DONE |
| 9 | Meta descriptions 145-160 chars | Screaming Frog | See 02_meta_tags.md | HIGH | ✅ DONE |
| 10 | H1 on every page (one only) | Browser DevTools | All pages have H1 ✅ | HIGH | ✅ DONE |
| 11 | Open Graph tags on all pages | View source | All pages have OG ✅ | MEDIUM | ✅ DONE |
| 12 | Twitter Card tags | View source | All pages have TC ✅ | LOW | ✅ DONE |
| 13 | LocalBusiness schema | schema.org validator | Homepage has it ✅ | HIGH | ✅ DONE |
| 14 | FAQPage schema | schema.org validator | Homepage + blogs ✅ | HIGH | ✅ DONE |
| 15 | BreadcrumbList schema | schema.org validator | Homepage has it ✅ | MEDIUM | ✅ DONE |
| 16 | WebSite SearchAction schema | schema.org validator | ✅ Just added | MEDIUM | ✅ DONE |
| 17 | Organization schema | schema.org validator | ✅ Just added | MEDIUM | ✅ DONE |
| 18 | AggregateRating schema | schema.org validator | ✅ Just added | MEDIUM | ✅ DONE |
| 19 | Image alt tags on all images | Grep `alt=` | All blog images have alt ✅ | HIGH | ✅ DONE |
| 20 | Images under 200KB each | Check file size | Compress with squoosh.app | HIGH | ❌ TODO |
| 21 | WebP format for images | Check extension | Convert PNG→WebP | MEDIUM | ❌ TODO |
| 22 | Lazy loading on images | Grep `loading="lazy"` | All blog images have it ✅ | MEDIUM | ✅ DONE |
| 23 | Mobile responsive | Chrome DevTools | Responsive design ✅ | HIGH | ✅ DONE |
| 24 | Viewport meta tag | View source | Present ✅ | HIGH | ✅ DONE |
| 25 | Page speed > 80 (mobile) | pagespeed.web.dev | Optimize images first | HIGH | ❌ TODO |
| 26 | Page speed > 90 (desktop) | pagespeed.web.dev | Already fast on Vercel | MEDIUM | ❌ TODO |
| 27 | No broken internal links | Screaming Frog | Check all href values | HIGH | ❌ TODO |
| 28 | No broken external links | Screaming Frog | Remove or update | MEDIUM | ❌ TODO |
| 29 | 404 page exists | /fake-page | Design custom 404 | MEDIUM | ❌ TODO |
| 30 | Internal links between blogs | Manual check | Add cross-links | HIGH | ❌ TODO |
| 31 | Font preload / preconnect | View source | Google Fonts preconnect ✅ | MEDIUM | ✅ DONE |
| 32 | CSS minification | Vercel | Vercel auto-minifies | MEDIUM | ✅ DONE |
| 33 | JS minification | Vercel | Vercel auto-minifies | MEDIUM | ✅ DONE |
| 34 | No render-blocking resources | PageSpeed Insights | Fonts async load | MEDIUM | ✅ DONE |
| 35 | Geo tags (meta) | View source | All pages have geo ✅ | MEDIUM | ✅ DONE |
| 36 | Lang attribute on html tag | View source | `lang="en"` present ✅ | MEDIUM | ✅ DONE |
| 37 | Favicon exists | Browser tab | Check /favicon.ico | MEDIUM | ❌ TODO |
| 38 | Apple touch icon | View source | Add `<link rel="apple-touch-icon">` | LOW | ❌ TODO |
| 39 | Structured data errors | search.google.com/test | Test after deploy | HIGH | ❌ TODO |
| 40 | No duplicate content | Copyscape or manual | All blog content unique ✅ | HIGH | ✅ DONE |
| 41 | URL structure clean (kebab-case) | Check URLs | All URLs kebab-case ✅ | HIGH | ✅ DONE |
| 42 | No www/non-www duplicate | Redirect test | Vercel handles ✅ | HIGH | ✅ DONE |
| 43 | Google Search Console verified | GSC dashboard | Submit & verify | HIGH | ❌ TODO |
| 44 | Bing Webmaster Tools verified | BWC dashboard | Submit & verify | MEDIUM | ❌ TODO |
| 45 | Google Analytics 4 installed | Source code | Add GA4 snippet | HIGH | ❌ TODO |
| 46 | Core Web Vitals check | CrUX report | Check after GA install | HIGH | ❌ TODO |
| 47 | Blog posts have author info | Blog pages | Add author byline | MEDIUM | ❌ TODO |
| 48 | Blog posts have date published | Blog pages | Add publish date | MEDIUM | ❌ TODO |
| 49 | Internal search works | Test /blogs?q= | JS search in blogs ✅ | LOW | ✅ DONE |
| 50 | WhatsApp click-to-chat | Test WA button | Present on all pages ✅ | HIGH | ✅ DONE |

---

## PRIORITY ACTION: Image Optimization

Current images are PNG (uncompressed). Converting to WebP reduces size 60-80%.

```
Tool: squoosh.app (free, no install needed)
1. Open squoosh.app in browser
2. Upload each PNG
3. Select WebP format, quality 80%
4. Download and replace in /images/ folder
5. Update <img src> references: .png → .webp
```

---

## CORE WEB VITALS TARGETS

| Metric | Target | What Affects It |
|--------|--------|----------------|
| LCP (Largest Contentful Paint) | < 2.5s | Hero image, fonts |
| CLS (Cumulative Layout Shift) | < 0.1 | Image dimensions, fonts |
| INP (Interaction to Next Paint) | < 200ms | JS execution |

**For Pakistan Mobile Users (slow 4G):**
- Images must be WebP + lazy loaded ✅ (lazy already done)
- Hero section: no large background image
- Fonts: preconnect already ✅
- JS: minimal, inline ✅

---

## QUICK WINS (Do This Week)

1. **Verify Google Search Console** — Submit sitemap → Google indexes new pages within 7 days
2. **Install GA4** — Track which pages get traffic first
3. **Add favicon** — Professional appearance + browser tab branding
4. **Compress images** — Use squoosh.app, biggest impact on page speed
5. **Internal linking** — Add links between related blog posts
