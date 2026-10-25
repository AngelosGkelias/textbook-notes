# Adaptive model routing and delegation

Read when selecting models, dispatching workers, or assigning a scoped independent review.

## Discover capabilities and match the work

Inspect the current session's tool descriptions or exposed model catalogue for available models, capability descriptions, valid reasoning settings, and delegation limits. Use that runtime evidence, not remembered model families, version ordering, or a public API catalogue as proof of account access. Do not bake model IDs or mandatory effort levels into this skill or its project templates. Discover once per project and refresh only after a capability rejection or environment change.

Choose a supported model/effort pair for each task using the following roles, which are decision criteria rather than literal model names:

| Work | Preferred capability | Escalation signal |
|---|---|---|
| Text extraction, source inventory, coverage mapping, organization, routine drafting | Economical model; deterministic tools for mechanical work | OCR ambiguity, missing mathematical structure, conflicting notation, or technical interpretation beyond straightforward transcription |
| Difficult chapter, multistep derivation, device/circuit reasoning, complex schematic | Stronger reasoning model with a supported effort appropriate to the problem | Coupled assumptions, failed checks, nontrivial approximation, or unresolved physical/logical contradiction |
| Particularly difficult problem or independent verification of consequential material | Strongest available reasoning capabilities when justified | Use for the bounded problem or review scope; do not automatically assign the whole book |

Model capability and effort are separate choices: maximal effort on an economical model is not a substitute for stronger reasoning on difficult material. Use the runtime's capability/cost descriptions and observed results; do not invent exact prices, performance rankings, or latency estimates. Prefer the least costly adequate route, accounting for repeated context and coordination overhead, while putting technical correctness and teaching quality first. Routine scripts need no extra agent.

Honor the user's explicit model, effort, provider, and budget restrictions. If a requested capability is unavailable, state the limitation and follow any authorized fallback; ask only when substituting would violate a constraint. If discovery or overrides are unavailable, keep the current permitted model/settings and state that limitation instead of guessing. Never silently downgrade an explicit preference, imply unsupported settings, change global configuration, or invoke a separate paid provider to implement routing. Under a hard budget, prioritize consequential checks and report unfinished work rather than claiming complete verification.

When a model override requires a fresh context, supply a self-contained assignment. Use only fields and effort values accepted by the current tool; omit overrides when keeping the current configuration is appropriate. Record the actual choice and short rationale in the project work log, not in textbook prose.

## Decide whether to delegate and establish ownership

Work directly on a small or tightly coupled project. Use subagents when separable work materially reduces elapsed time or improves quality enough to justify setup and integration. For large projects with independent chapters, delegate chapter groups or bounded tasks and centralize integration. A short but unusually difficult derivation can justify one reviewer without a writing team. Use internal subagents rather than new sidebar chats; if unavailable, execute the same responsibilities sequentially and disclose the limitation.

Choose concurrency from available slots, workload, budget, and dependencies, with no mandatory team size or page threshold. Group related topics where cross-dependencies are strong; equal PDF chunks may have very different workloads. A worker should return a specific hard question for escalation, not restart a satisfactory chapter on a more expensive model. Avoid recursive delegation unless the lead explicitly allocates scope and capacity.

Orchestrator owns main.typ, theme.typ, global notation/correction policy, shared manifests, and the final build. Workers own disjoint chapter files, prefixed assets/generators, and separate chapter manifests/reports. Workers can compile an isolated chapter harness, but must not race to write the shared book or final output. Send substantive uncertainty and difficult figure requests back early; do not wait until the chapter is otherwise finished.

## Worker assignment contract

Fill in actual paths and chapter/topic scope. Send this information in ordinary prose:

> Create the assigned chapter(s) of textbook-style notes using the supplied skill and raw sources. Read your entire assigned source, including late sections. Default to English unless the task states otherwise. Preserve and explain source notation; verify equations and graphics against rendered pages. You own the listed chapter files, asset prefix, and chapter manifest only. The orchestrator owns shared files and final integration.
>
> Produce complete connected explanations, model assumptions and limits, checked worked examples, useful source and original visuals, nearby source-page references, a notation key where needed, corrections with evidence where justified, and answered self-tests. Scale explanation to conceptual difficulty, consolidate repeated material, and label supplemental content and illustrative numbers. Use the agreed Typst chapter interface. Do not stop at an outline, crop-coordinate proposal, or a list of suggested images. No arbitrary word, page, or figure quota replaces substantive coverage.
>
> Review every assigned source page/range. For each relevant distinct graphic, include it near its explanation or record a reason it is consolidated or excluded. Render and inspect every actual crop, preserving labels, axes, units, signs, connections, and complete tables. Do not infer crop correctness from the full slide alone. Replace an unsuitable crop with a completed source version or a clean original illustration. View newly drawn figures and compile your isolated chapter before handoff where tooling allows.
>
> Apply technical-verification.md to important equations, intermediate calculations, assumptions, and diagram semantics; retain concise evidence and limitations. Ask the orchestrator for help with difficult diagrams, notation conflicts, unclear technical claims, or source errors; include the source location and concrete insertion anchor. Finish by reporting edited files, included figure assets, coverage/dispositions, notation choices, supplemental references, corrections/uncertainties, and the exact validation performed. State any unverified items explicitly.

Also provide the skill path, source paths/page markers, intended audience/depth, project language, exported theme wrapper/functions, chapter/section heading levels, consistent asset paths, figure conventions, source numbering convention, output paths, source constraints, research permissions, budget limits, and relevant shared prerequisites/notation. Existing notes expansions additionally identify which content must be preserved and which changes are authorized.

## Handoff and independent review

A ready chapter has actual assets and source, not promised future files. Record whether a figure was inspected as a crop, whether it remains legible at intended size, and which assumptions its caption explains. For a technical ambiguity, the report distinguishes “checked”, “interpreted”, and “unresolved”.

The orchestrator checks chapter coverage and spot-checks the difficult formulas, examples, corrections, and all delivered figure sheets. Give special attention to late source sections, sign conventions, tiny plot labels, cropped annotations, and empty source exercises. Review the integrated PDF because correct isolated chapters can still produce bad global numbering or distant figures.

For technically demanding or consequential material, use a scoped independent reviewer when it adds confidence: difficult derivations, source corrections, coupled circuits, or a claim central to later chapters are good candidates. Give raw source pages, actual equations/diagrams, assumptions, and relevant authoritative references, without a desired verdict. Have the reviewer reconstruct critical steps or produce a counterexample and report concrete findings with locations and evidence; agreement with the writer is not a correctness check. Use the strongest available reasoning only where the difficulty warrants it.

Normally perform one scoped review, resolve findings, and recheck the affected material. Broaden or repeat review only for new evidence, changed dependencies, or a specific unresolved defect. Apply the completion criteria in [technical-verification.md](technical-verification.md); do not add reviewers or ask for repeated generic approval after the checks pass.

Runtime behavior can be checked in the [official subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents) when needed; the current session's tool contract determines which controls and models are usable here.
