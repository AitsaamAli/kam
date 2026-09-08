# Workflows

Standard sequences. Run each role in order, feeding it the real output of
the roles before it as context, plus what Step 0 found in the project. Save
each role's output under `briefs/deliverables/` as you go, per SKILL.md
Step 4.

## onboard — New project, first pass
The full opening sweep before anything else happens.
1. head-search
2. strategy-director
3. competitor-intel
4. keyword-research
5. tech-auditor
6. llm-visibility
7. content-strategist
8. qa-lead

## ai-sprint — AI visibility sprint
Get the project appearing inside AI answers.
1. prompt-research
2. llm-visibility
3. ai-crawler
4. citation-source
5. knowledge-graph
6. comparison-pages
7. hallucination-monitor
8. qa-lead

## tech-check — Technical health check
Everything under the hood, in one pass, against the real codebase.
1. tech-auditor
2. cwv-engineer
3. js-seo
4. architecture
5. schema-engineer
6. log-analyst
7. qa-lead

## content-engine — Content engine setup
From audience to a brief a writer can execute, against real content gaps.
1. icp-research
2. keyword-research
3. topical-authority
4. content-strategist
5. brief-writer
6. eeat-lead
7. qa-lead

## answer-push — Answer engine push
Snippets, PAA, voice, zero-click, against real target queries.
1. intent-serp
2. snippet-paa
3. faq-qa
4. voice-search
5. serp-features
6. qa-lead

## local-push — Local market push
For a project with a real physical footprint.
1. gbp
2. citation-manager
3. multi-location
4. intent-serp
5. qa-lead

---

To run one: tell Claude "run the ai-sprint workflow" (or describe the goal
and let Claude pick the closest workflow). Claude should confirm the
sequence, then execute role by role, showing each deliverable before moving
to the next unless told to run it all silently and report at the end.
