# Changelog

## v1.5
- Added `ACCURACY-PROTOCOL.md` — mandatory pre-finalize check for every
  deliverable: every claim tagged verified/estimated/assumption, live-
  checkable claims actually verified when a search/fetch tool is
  available, code traced against the real project structure, and
  multi-role sessions checked for internal contradictions before being
  treated as complete.
- qa-lead's mandate now explicitly runs this protocol rather than a
  generic "check for errors" pass.
- SKILL.md Step 3 now routes every deliverable through it before treating
  the work as finished.

## v1.4
- Added `CADENCE.md` — a compounding twice-a-week 8-week growth program
  (foundation → keyword clustering → content → AEO → GEO → links → results
  review), followed by a maintenance-mode rotation driven by real results
  rather than a fixed script.
- Added `briefs/growth-tracker.md` — a persistent state file so running the
  team on a schedule advances each time instead of repeating the same
  audit twice a week.
- Added a real keyword-clustering methodology to KNOWLEDGE.md — SERP-
  overlap clustering (the actual mechanical test), intent-layer checks,
  pillar/supporting sequencing for low-authority sites, and the internal-
  linking handoff — replacing "just a keyword list" with an actual site
  architecture input.
- Added explicit expectation-setting: no guaranteed "maximum traffic,"
  realistic 3-6 month timeline for real growth, stated plainly in both
  CADENCE.md and to the user.

## v1.3
- Added `OPERATOR-CONTEXT.md` — durable facts about this operator's real
  constraints (near-zero budget, ~$5/mo database ceiling, Pakistani market,
  Roman Urdu communication, "must not feel AI-generated" quality bar) and
  known active projects, so specialists calibrate to reality by default
  instead of recommending enterprise-scale budgets or generic advice.
- SKILL.md Step 1 now reads this file every session before the brief.

## v1.2
- Added WordPress/page-builder-specific technical knowledge (most common
  real-world stack for SMB sites in this market) — caching, page-builder
  CWV bloat, Yoast vs Rank Math, WooCommerce faceted URL handling.
- Added Urdu / Roman Urdu / RTL SEO section — script vs Roman Urdu as
  different query languages, hreflang/lang/dir specifics, RTL layout bugs,
  weak Urdu keyword-tool data, weaker Urdu support in AI/voice assistants.
- Added a "how to know a role's work actually succeeded" section per
  department, so QA and the user can judge outcomes, not just delivery.
- Added explicit "hands off to" notes on the most overlap-prone role pairs
  (keyword-research/intent-serp, content-strategist/topical-authority,
  architecture/migration, llm-visibility/hallucination-monitor) to stop
  duplicated or conflicting work between adjacent roles.

## v1.1
- Removed a dead, unused `roles/` folder from the package.
- Added a staleness-verification protocol to KNOWLEDGE.md — treat all
  dates/thresholds as last-known, verify via search when available, say
  plainly when they can't be verified in this session.
- Fixed brief-detection logic — a `<placeholder>` value no longer counts
  as an answered brief field.
- Scoped the whole package explicitly to websites — added a stop-and-say-so
  rule if it's ever dropped into a pure application/product codebase with
  no public-facing site.
- Deliverables now save with a date prefix so re-running a role doesn't
  silently overwrite an earlier version.
- Added a language-matching rule (respond in the user's language; produce
  target-market content in the target language).
- Added a rule to say plainly when a role needs a live check (search/fetch)
  that isn't available in this session, instead of inventing a result.

## v1.0
- Initial release: SKILL.md, ROLES.md (60 roles / 11 departments),
  WORKFLOWS.md (6 sequences), KNOWLEDGE.md (veteran-level reference),
  brief template.
