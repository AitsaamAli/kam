#!/usr/bin/env python3
"""Owner's instruction (6 Nov 2026): say 'FBR Registered' instead of 'FBR Certified', and promise replies within
office hours instead of within 30 minutes. URLs and slugs are left untouched. Applies to tax-site pages,
llms files and the builders/templates under content/ so later rebuilds keep the wording."""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NB = r"(?<![\w/-])"
RULES = [
    (NB + r"FBR CERTIFIED", "FBR REGISTERED"),
    (NB + r"FBR Certified", "FBR Registered"),
    (NB + r"FBR certified", "FBR registered"),
    (NB + r"FBR-Certified", "FBR-Registered"),
    (NB + r"FBR-certified", "FBR-registered"),
    (NB + r"Non-Certified(?![\w-])", "Unregistered"),
    (NB + r"non-certified(?![\w-])", "unregistered"),
    (r"within 30 minutes of your first message", "during office hours"),
    (r"[Ww]e respond within 30 minutes during business hours", "We respond during office hours"),
    (r"Average response: under 30 minutes", "Replies within office hours"),
    (r"hear back within 30 minutes", "hear back within office hours"),
    (r"Free consultation within 30 minutes", "Free consultation within office hours"),
    (r"(confirm your exact deadline</strong>\s*)within 30 minutes|(confirm your exact deadline\s*)within 30 minutes", r"\1\2within office hours"),
    (r">\s*Within 30 minutes\s*<", ">During office hours<"),
    (r'(<div class="highlight-num">)30min(</div><div class="highlight-label">)WhatsApp Response Time', r"\1Mon&ndash;Sat\2WhatsApp replies in office hours"),
    (r"\b(first read|assess|assess it|review|exact requirement) within 30 minutes", r"\1 within office hours"),
    (r"((?:[Rr]eply|[Rr]eplies|[Rr]esponse|[Rr]espond|assessment|quote|[Ee]xpert|guidance|WhatsApp|answer)[^.<>\"]{0,25}?)\s(?:within|in under|inside|in)\s30\s?minutes",
     r"\1 within office hours"),
]


def files():
    out = [f for f in glob.glob("**/*.html", recursive=True) if not f.startswith(("node_modules/", "digital/", "content/digital"))]
    out += ["llms.txt", "llms-full.txt"]
    out += [f for f in glob.glob("content/**/*", recursive=True)
            if f.endswith((".py", ".html", ".md")) and not f.startswith("content/digital") and "claims_fix" not in f and os.path.isfile(f)]
    return out


def main():
    os.chdir(ROOT)
    changed = 0
    for f in files():
        if not os.path.exists(f):
            continue
        t = open(f, encoding="utf-8", errors="ignore").read()
        n = t
        for a, b in RULES:
            n = re.sub(a, b, n)
        if n != t:
            open(f, "w", encoding="utf-8").write(n)
            changed += 1
    print("files changed", changed)


if __name__ == "__main__":
    main()
