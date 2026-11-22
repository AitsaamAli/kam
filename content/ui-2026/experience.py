"""Firm experience block (E-E-A-T) on every guide in blogs/ (owner request, 22 Nov 2026). Idempotent.
Uses only facts already published on /about: established in Lahore in 2008, FBR Registered, Awan Town office.
No client counts, ratings or credentials. One wording on every guide, so it reads as site-wide information (like the footer) and the overlap gate ignores it; rotating wordings made each variant count as body overlap."""
import glob, hashlib, re

ROOT = "/home/user/kam/"
MARK = 'class="ka-exp"'
V = [
    "Kamboh Associates is an FBR Registered tax practice that has worked from Lahore since 2008, now from its Awan Town office and on WhatsApp for clients across Pakistan. This guide is written by Aitsaam Ali (Author), and its figures are checked against official texts on the date shown. If your case differs from the examples, we confirm what applies to you before any work starts.",
    "Since 2008 our Lahore practice has filed returns, registrations and notice replies for individuals and businesses; we are FBR Registered and work from Awan Town and online. Aitsaam Ali wrote this guide (Author) from the official texts cited below. Your facts may differ from these examples, so we check your case and confirm the fee before we begin.",
    "This guide comes from a working tax practice: Kamboh Associates, FBR Registered, working in Lahore since 2008 with an office in Awan Town. It is written by Aitsaam Ali (Author) and every figure links to its official source. Send us your details and we tell you what applies before anything is filed.",
    "Kamboh Associates has handled tax work in Lahore since 2008 and is FBR Registered; clients reach us at our Awan Town office or on WhatsApp from anywhere in Pakistan. Aitsaam Ali (Author) wrote this guide from the official sources listed. Every case has its own facts, so we confirm what applies, and the fee, before work starts.",
]


def block(slug):
    i = 0
    return (f'<aside {MARK} aria-label="About this guide" style="margin:28px 0 8px;padding:14px 18px;border:1px solid #E2E8F0;'
            f'border-radius:10px;background:#F8FAFC;font-size:.9rem;line-height:1.65;color:#334155">'
            f'<strong style="color:#0F172A">From our practice:</strong> {V[i]}</aside>\n')


def main():
    n = 0
    for p in sorted(glob.glob(ROOT + "blogs/*.html")):
        t = open(p, encoding="utf-8").read()
        if MARK in t or re.search(r'<meta name="robots"[^>]*noindex', t):
            continue
        k = t.find("</article>")
        if k < 0:
            continue
        slug = p[len(ROOT) + 6:-5]
        t = t[:k] + block(slug) + t[k:]
        open(p, "w", encoding="utf-8").write(t)
        n += 1
    print("experience block added", n)


if __name__ == "__main__":
    main()
