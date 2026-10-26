# Adaptive model use and resumption

Read when choosing execution mode, model/effort, review allocation, or resuming a project. This is a routing policy, not a fixed model configuration or a claim about any subscription allowance.

## Discover once, choose per task

Use the current runtime's tool contracts or exposed catalogue to resolve actual models, valid efforts, delegation controls, and concurrency. Refresh after an environment change or capability rejection. Public model listings do not prove account access. Preserve explicit user constraints and current configuration when overrides are unavailable; do not pretend to switch the orchestrator or change global settings. Record actual choices and limitations briefly in the project work log.

Default to a capable economical orchestrator and direct work. Administrative coordination does not justify the most expensive model or highest effort. Use deterministic tools before assigning mechanical work to a model. Select the least costly adequate model and effort using task complexity, uncertainty, importance, and observed checks. Treat model capability and reasoning effort as separate decisions.

| Task | Initial allocation | Evidence for escalation |
|---|---|---|
| Extraction, inventories, file organization, mechanical mappings, formatting, routine scripts | Local scripts; economical model at low supported effort for bounded interpretation | OCR/math ambiguity, conflicting notation, failed extraction/check |
| Concept teaching analysis, architecture, ordinary explanations and section validation | Capable economical model at moderate effort | Hidden prerequisites, difficult mechanism, weak teach-back result, important uncertain dependency |
| Complex derivation, ambiguous source, demanding schematic, difficult cross-topic reasoning | Stronger reasoning, bounded to that problem; raise effort if needed | Failed reconstruction/limits, coupled assumptions, consequential unresolved claim |
| Routine coverage audit and simple concept review | Lightweight source-to-output check; reuse accepted section evidence | Unmapped source content or mismatch with teaching specification |
| Consequential pedagogical/technical finding | Independent capable reviewer, stronger only for the difficult question | Concrete failure requiring deeper reasoning; no automatic premium panel |

Task examples, not mandates: a runtime may offer a general model such as Sol for moderate/high effort substantive work, an economical Luna for tightly specified transformations, and Astra for exceptional problems. Resolve availability and valid settings afresh rather than hardcoding those names. These examples assert no prices or guaranteed rankings.

Escalate with a concrete failed criterion, source region, attempted reasoning/check, and desired result. After a focused escalation, return routine work to its normal route. Do not repeatedly escalate unchanged prompts without new evidence; isolate the uncertainty, try an independent check, or record what evidence is missing. A stronger model's confidence alone does not close the issue.

Current [official reasoning guidance](https://developers.openai.com/api/docs/guides/deployment-checklist) describes the usage/effort trade-off. Runtime-supported settings and representative task results control the choice here; API prices or token counts cannot be translated into subscription quota consumption without actual telemetry.

## Optional execution modes

| Mode | Allocation and review |
|---|---|
| Economy | Prefer scripts and one capable agent; low supported effort for simple tasks; concise reusable analysis; concentrate intensive independent reasoning on difficult/consequential material. All concepts, essential explanations/figures, complete coverage audit, and consequential accuracy checks remain required. |
| Balanced (default) | Moderate effort for substantive analysis/authoring, selective stronger capability for hard problems, bounded independent teaching/technical review. Delegate only when net benefit is credible. |
| Maximum quality (explicit request) | Permit deeper reasoning, more challenging transfer probes and broader independent review where valuable. Still avoid redundant context ingestion, fixed review loops, or gratuitous figures. |

Modes do not authorize omissions, unverified factual claims, or silent downgrades of essential teaching. Do not ask for a mode when the default is sufficient.

## Spend context deliberately

Delegate only when a task is meaningfully separable and parallelism or independence outweighs coordination and repeated context cost. Estimate qualitatively whether workers would all reread the same large deck or require shared conceptual context; a single capable agent can be more efficient. Use disjoint bounded sources plus shared prerequisite/notation summaries, with access to raw evidence when needed. Do not automatically spawn a team because the project is large or use expensive agents for administration. See [delegation.md](delegation.md) if dispatching.

Keep project state in the inventory, teaching specification, and one concise work/review log. Record source hashes, inspected ranges, accepted concept/section anchors, figure provenance and generator inputs, check results, actual routing, and unresolved next actions. Reuse tool-generated hash/provenance records; do not copy source text into multiple reports. Store a dependency digest or equivalent relation between accepted work and its source ranges, prerequisites, section files, figure inputs, and checks.

On resume, compare hashes before reading/authoring. Unchanged sources, accepted sections, rendered assets, and checks remain valid for the same dependencies. If one file changed, compare page/range evidence where feasible; invalidate the affected concepts and their dependents, not the whole source corpus. Uncertain change boundaries require inspecting the changed source, not reprocessing every unchanged file. A changed source need not invalidate unrelated sections; changed audience assumptions can invalidate prerequisite treatment. Preserve accepted sections after interruption or usage exhaustion.

When a source changes, its old visual-inspection flags are stale for changed or unproven pages. Equal extracted text does not establish equal diagrams or annotations. Reuse page inspection only with matching page/render evidence; otherwise visually inspect those pages before attaching an inspected status to the new hash. Sampling the first/last pages cannot certify uninspected pages. Keep text extraction, visual inspection, and teaching acceptance states distinguishable.

Use telemetry only when exposed and relevant. Record observed duration, model/effort, token/cache statistics, or account-limit changes when available, labeling unavailable fields unknown. Concurrent account usage may confound quota deltas. Never infer remaining allowance from plan price or fabricate a cost estimate. If completion cannot fit a stated hard limit, save a resumable state with exact remaining concepts, sections, checks, and commands; do not call incomplete work complete.

For routing comparisons use the same small raw task and rubric, keeping answers isolated. Compare pass/fail teaching and technical outcomes first, then observed resource use. Test alternatives only when likely to inform allocation; do not spend more benchmarking than the routing decision warrants. [Regression evaluations](regression-evals.md) provide a compact protocol.
