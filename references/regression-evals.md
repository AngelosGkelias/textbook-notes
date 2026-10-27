# Small general-purpose regression evaluations

For skill maintenance, not an extra phase in textbook projects. The fixtures sample numerical reasoning, optimization, scientific graphs, inference, dimensions, concurrency, and resumable source coverage. They test decisions and teaching evidence rather than a particular course or wording.

## Generate isolated raw inputs

Run `python SKILL/evals/make_fixtures.py --out /tmp/notes-eval-UNIQUE` with an available Python containing reportlab. This creates a seven-page synthetic source packet and a 144-page imported resumption project. No API calls, new toolchain, or full textbook run is needed. Existing production helpers and template assets have separate mechanical tests in `evals/test_package.py`.

It also creates `comparison/author/` and `comparison/review/`, each with the same two-page source. Use `--case comparison` to generate only these small cases. Give them to separate fresh sessions: authoring receives only its raw source/request; review receives its source, existing notes/figure, specification, acceptance record and request. The review inputs deliberately contain a wrong redundancy decision; keep that fact and the rubric hidden from the reviewer. For a blind handoff, copy only production skill instructions/assets into a separate skill snapshot, excluding `evals/`, this maintenance reference and its entrypoint link; keep graders, generators and other cases outside the evaluator's input directory.

Give an evaluator only the candidate skill, generated raw sources and request.txt, plus an isolated output directory. Do not expose `evals/rubric.json`, fixture generator code, intended answers, or previous findings before it acts. For resumption, supply its state and accepted artifacts as raw project context. The state is explicitly synthetic imported evidence, not a claim that an earlier model actually processed 144 pages.

For the micro task require the teaching specification to be saved before the sections; freeze it to distinguish successful initial analysis from retrospective planning. The request explicitly selects Markdown plus figure assets so pedagogical testing is independent of compiler availability. Preserve the initial analysis even if later corrections are needed.

## Grade observable results

After the run, use [../evals/rubric.json](../evals/rubric.json). For each case record analysis pass/fail, content pass/fail, exact source/destination evidence, and defect/repair. Cases cover:

1. Brief but important convergence concept.
2. Omitted intermediate optimization reasoning.
3. Essential scientific graph and interpretation.
4. Redundant graph and irrelevant decoration.
5. Unstated probability prerequisites.
6. Detectable equation/units inconsistency.
7. Substantive late appendix topic.
8. Large-source completeness and selective reuse after a source change.
9. Comparison-graph preservation versus a same-topic illustration and optional mathematical extension.
10. Review of an incorrect specification and acceptance claim despite correct comparison prose and calculus.

Read actual notes, equations, source pages, and figure assets. Do not grade by keywords, headings, length, or model self-reports. Verify worked values independently. For the resumption case compare initial/final artifact hashes, changed concept/dependency state, complete page dispositions, and actual source-read operations where exposed. Hashing input bytes is expected and does not count as semantic reprocessing. Logs alone cannot prove absence of unobserved reads; report that limit if tool traces are unavailable.

Add an adversarial review check by giving a reviewer a copy with a derivation step, graph interpretation, or late concept removed while leaving its heading and coverage claim intact. Keep the alteration hidden from the reviewer. Pass only if it reports the concrete gap with source/destination evidence; fix the affected section and recheck that criterion. One bounded review can cover these faults; several premium reviewers are unnecessary.

## Compare routing only when feasible

Use the same raw micro task on at most a small number of runtime-available candidate model/effort settings in isolated contexts. Inspect quality before resource use; compare duration and actual exposed input/output/reasoning/cache tokens or usage deltas. Subscription consumption is unknown without suitable telemetry; wall time is not a quota measure. A single successful small trial is evidence for those tasks, not a general ranking or a guarantee.

Economy and Balanced routes are useful candidates; a strongest-model trial is unnecessary unless a demonstrated failure justifies it. Record actual chosen settings, constraints, pass/fail and observed costs; leave missing measurements unknown. If dispatch/usage telemetry is unavailable, run the feasible behavioral/mechanical checks and state which comparison was not performed. Do not launch a full textbook to test routing.
