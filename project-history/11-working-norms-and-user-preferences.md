# Working Norms & User Preferences

These are corrections and confirmed preferences the user has given across sessions. Follow these without being asked again — re-litigating them wastes the user's time.

## 1. Never touch existing blog files when the task is "write new content"
When asked to write/add new blogs, only **create** new files. Never edit, reformat, or "fix" an existing blog file unless the user **explicitly** asks for a fix on that specific file. This applies even if you notice something wrong while working nearby — flag it, don't silently fix it, unless it's the kind of clear defect covered by rule 6 below (in which case, still prefer flagging over silent action when it's a live, published page).
*(Exception already exercised: when the user explicitly asked to rewrite a specific thin pillar page before adding a new cluster, e.g. "pelha uk per jo blogs ha usko rewrite karo" — that's an explicit ask, not a violation of this rule.)*

## 2. Always re-verify word count as the literal last step before commit
Not from an earlier check earlier in the same editing session. A file was once committed under the 2000-word target because a later small edit wasn't re-verified. Treat "word count ≥ 2000" as a hard gate checked in the *same tool call* as the final pre-commit validation, alongside JSON-LD validity and tag-balance.

## 3. Flag before publishing content naming a blocked/restricted platform
Before writing live, public content that names a specific foreign platform/service, check whether it's blocked or legally/morally controversial in Pakistan. If so, use a clarifying question to the user rather than silently proceeding as originally scoped OR silently dropping/renaming the topic unilaterally. Offer options (skip and replace / write as scoped / write a de-named generic version) — don't presume the answer. This applies to actual publishing decisions, not internal planning-doc topic names (a topic name in a planning list doesn't need flagging until it's about to become published content). Once flagged and answered for a given topic, don't re-ask on later batches of the same content project.

## 4. Never fabricate a tax rate, fee, deadline, or statistic
This has been said explicitly and repeatedly (originally: "NEVER invent tax rates, FBR figures, deadlines — flag to figures-to-verify.csv instead"). If a number isn't in `09-verified-facts-and-figures.md` and hasn't been freshly verified with a citable source this session, hedge in the text rather than presenting an invented precise figure as fact. This is treated as a hard content-integrity rule, not a style preference — violating it is a genuine risk to a real business's credibility and to Google's "scaled content abuse" spam policy exposure.

## 5. No images (`og:image`) on blog pages
Explicit instruction from early in the project: "NAHI IMAGES NAHI LAGNI" — do not add images to blog content. The site is deliberately SVG/icon-font-based rather than raster-image-heavy.

## 6. When you find a real defect on a live page while doing unrelated work, fix it (with a brief note) rather than ignoring it
Distinct from rule 1 (which is about *scope* — don't go looking for things to change in unrelated files). If you're already editing a file and discover something broken (duplicated section, broken schema, wrong date, contradicting numbers), fix it as part of the same pass and mention it briefly — this has been the consistent pattern across every content-rewrite session and has never been pushed back on. The distinction: rule 1 says don't *go looking* in files outside your current task's scope; this rule says don't *ignore* a defect you land on while doing legitimate work in a file.

## 7. Prefer flagging/asking over silent unilateral judgment calls on anything business-risk-adjacent
Beyond the blocked-platform case (rule 3), this shows up generally: when something is a genuine judgment call with real consequences for a live business (a design/brand decision, a content-safety question, a decision to touch a known-defective-but-live page), use `AskUserQuestion` rather than deciding silently. Purely mechanical/technical fixes (broken links, malformed JSON-LD, truncated titles) don't need this — those are unambiguous bugs, just fix them.

## 8. The user writes in a Roman-Urdu/English mix — match that register in responses and in content
Both conversational replies to the user and the actual blog content should use the site's established Roman-Urdu-plus-English-technical-terms voice (see any recently-written blog for the exact register), not formal English or pure Urdu script.

## 9. Auto-mode / autonomous work bias
When working under "auto mode" instructions (self-paced, minimal check-ins), bias toward making the reasonable call and continuing rather than stopping to ask — but this does NOT override rules 3 and 7 above (content-safety and business-risk judgment calls still get a question). The balance point used successfully across this project: proceed autonomously through mechanical/technical work and well-defined multi-step content production; stop and ask only for genuinely blocked situations (unclear instruction, a real design/brand tradeoff, a content-safety flag).

## 10. When a task is described in relative/vague terms, verify actual current state before acting
E.g. "next country" required re-reading the priority report rather than guessing; "is X done" claims should be checked against the live word-count script rather than trusting a stale memory list. Several memory/planning documents in this project have gone stale relative to actual git history — always sanity-check a specific factual claim against the live repo before asserting it as current fact (this is also why `project-history/00-INDEX.md` explicitly warns about staleness).

## 11. Commit discipline
- Small, per-batch or per-file commits with descriptive messages, not one giant commit for a multi-day project.
- Never `git push --force`, never skip hooks, never amend a published commit — create a new commit to fix a mistake instead (this project has done this correctly every time a bug was found post-commit, e.g. the duplicated-section bug fix in `df02d4e8`).
- Only commit/push when the work is actually validated (word count, uniqueness, JSON-LD, broken-links) — not as a "let me just save progress" habit mid-task.
