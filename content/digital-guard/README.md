# Web Development Isolation Guard

The tax site (about 1,700 pages) is the business. Web-development work under `/digital` must never change it, link into it, compete with it for keywords, or send Google mixed signals. This folder is the "isolation team": a set of rules plus a script that enforces them.

## Rules

1. **Tax pages are frozen.** Web work changes only:
   - `digital/`
   - `content/digital*/`
   - `sitemap-digital.xml`
   - the 7 `/digital` lines removed from `sitemap.xml`
   - one `Sitemap:` line in `robots.txt`
2. **No new links between the sections.**
   - `/digital` pages link only to other `/digital` pages, external sites, images, and the Privacy and Terms pages.
   - No tax page gets a new link to `/digital`. The homepage link that existed before the guard is frozen in `baseline.json`.
3. **No keyword overlap.** `/digital` titles and H1s never use tax terms (tax, NTN, STRN, FBR, filer, ATL, SECP, wealth statement, withholding, sales tax, income tax, IRIS, GST), so web pages never compete with tax pages in Google.
4. **Separate identity.**
   - `/digital` pages have their own top bar, menu, footer and sidebar.
   - Schema uses the entity `Kamboh Associates Digital` (`/digital#organization`), linked to the parent company. It never uses a LocalBusiness address.
5. **Separate sitemap.** `/digital` URLs live only in `sitemap-digital.xml`, which is referenced from `robots.txt`.
6. **Quality.**
   - Unique titles and descriptions across the whole site.
   - One H1 per page.
   - Valid JSON-LD, with FAQ schema only for FAQs visible on the page.
   - Under 15% text overlap with any other page.
   - Self canonical and never noindex.

## How to use

```
python3 content/digital/shell.py          # apply the web-development header, footer, schema and sitemap to /digital pages
python3 content/digital-guard/guard.py    # must print "Clear to push" before any commit
```

A failing guard means the change does not ship.
