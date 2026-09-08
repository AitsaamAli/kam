# Accuracy protocol — run before finalizing any deliverable

This is not optional polish. A confident-sounding wrong recommendation
(a bad redirect rule, an invented ranking number, a schema type that
doesn't actually exist) costs more than it saves. Run this before calling
any deliverable done — single-role or workflow, report or code.

## 1. Tag every factual claim

Before finalizing, every number, date, or "this is how it works" claim in
the deliverable must be one of three things, and should read that way to
the user (explicitly labeled where it matters, not buried):

- **Verified** — came from the project's real files, the user's own data,
  or a live search/fetch you actually ran this session. State the source.
- **Estimated** — an industry-standard range or a reasoned guess (e.g.
  keyword volume without a paid tool). Say it's an estimate, plainly, next
  to the number — not once at the top and then presented as fact for the
  rest of the document.
- **Assumption** — something you inferred because the brief didn't say.
  State the assumption in one line so the user can correct it.

If a claim doesn't fit any of the three cleanly, that's a signal to cut it
or soften it, not to state it anyway.

## 2. Verify what's actually checkable, don't skip it because it's easy to skip

- Any claim about a *current* platform rule, algorithm behavior, or
  eligibility (rich-result types, an AI platform's citation behavior, a
  CMS plugin's current feature set) — if search/fetch is available, check
  it this session rather than trusting KNOWLEDGE.md's snapshot. If it
  isn't available, say so plainly per KNOWLEDGE.md's staleness protocol —
  don't silently present the snapshot as current.
- Any code (schema JSON-LD, redirects, robots.txt rules) — mentally trace
  it against the actual project structure found in Step 0 before handing
  it over. A redirect rule that references a URL pattern that doesn't
  exist in this project is a real error, not a stylistic choice.
- Any claim about a competitor, or about what a real source currently
  says — don't state it from memory if it's checkable and the stakes are
  real (a comparison page claim, a competitor teardown). Check it or label
  it as unverified.

## 3. Internal consistency check across specialists

Before treating a multi-role session (a workflow, or several roles run
back to back) as complete, check that later specialists didn't silently
contradict earlier ones — a common real failure mode:
- Does the content plan actually match the keyword clusters that were
  built, or did it drift back to generic topics?
- Does the architecture proposal match the URL structure the technical
  auditor already found working, or does it recommend restructuring
  something that isn't actually broken?
- Does a later role's recommendation assume a budget/tool the operator
  context says isn't available?

If something doesn't line up, flag it and reconcile it — don't hand over
two deliverables that quietly disagree.

## 4. QA-lead gate for anything that ships or gets implemented

Route through qa-lead's checklist (ROLES.md) before:
- Any code gets written into real project files.
- Any content is treated as ready to publish.
- Any report is the final deliverable of a workflow (not a single quick
  question — use judgment on when this level of ceremony is warranted).

qa-lead's job here specifically: check that every claim above is properly
tagged, that the internal consistency check was actually done, and that
nothing in the deliverable overstates what was actually verified.

## 5. Say what you didn't verify

Ending a deliverable with a short, honest line on what's still unverified
or estimated (if anything) is not a weakness — it's what separates a
professional handoff from a confident-sounding guess. A veteran says "the
volume estimates on this cluster are directional, confirm with real
Search Console data once this ranks" rather than presenting a made-up
number as fact.
