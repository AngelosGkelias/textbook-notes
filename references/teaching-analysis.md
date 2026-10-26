# Concept-level teaching analysis

Read after inspecting the sources and before authoring. The output is a working teaching specification, not another textbook. Reuse it for section authoring, review, and resumption.

## Understand before allocating effort

Inventory the complete source once, recording content hashes and 1-based PDF pages (and printed numbers if different). Read text and visually inspect pages; record inspected ranges so an interruption does not cause another full read. Expand equations, graphical annotations, tables, and diagrams until their meaning is readable. Extraction failures or blank text are unresolved inspection tasks, not grounds for exclusion. For non-PDF sources use stable slide, section, cell, timestamp, or figure identifiers.

Identify distinct technical learning objectives: a mechanism, relationship, assumption, derivation, procedure, interpretation, limitation, or meaningful comparison. One heading can hide several; repeated builds can teach one. Consolidate related objectives when their prerequisite/reasoning chain is shared, while retaining each distinct requirement and all source locations. Keep unresolved interpretations visible.

Ask what a student must understand and do, why it matters, what prior knowledge it requires, which steps the lecturer probably supplied orally, and how one could tell whether the student understood. Infer gaps from the reasoning required, not from the amount of source text. Add necessary prerequisites without expanding into an unrelated course.

## One compact, auditable specification

Use a Markdown table with short linked detail blocks, or JSON/YAML if it helps an actual tool. Choose one representation; do not maintain duplicate manifests. A row/block per coherent concept group contains:

| Field | Required content |
|---|---|
| ID and source | Stable concept ID; file/hash and exact page/region or equivalent location; all consolidated occurrences |
| Objective and significance | What the learner should understand/use and why it matters |
| Prerequisites | Concept IDs or assumed prior knowledge; bridge/explanation location for gaps |
| Importance / difficulty | Separate low/medium/high judgments with a short reason when non-obvious |
| Teaching requirements / depth | Required mechanism/intuition, mathematical or procedural steps, assumptions, limits and misconceptions; concise, developed, or deep with the reason |
| Visuals / examples | Essential, valuable optional, redundant, unnecessary, or unsuitable visuals with teaching question and disposition; necessary example/contrast, or reason none is needed |
| Understanding evidence | Target action or teach-back question and the key elements a successful answer must contain |
| Destination / state | Section/anchor and evidence locations; analyzed, authored, checked, reviewed, or unresolved |

Use shared prerequisite and notation entries instead of repeating them in every row. “None needed” is valid when justified by the concept. Do not turn the fields into a demand for a derivation, figure, example, or separate paragraph for every definition. Keep detail only where it changes authoring or review decisions.

For an essential graph, name the specific relationships, regions, or parameter comparisons the learner must interpret, and choose source reuse/crop versus a justified replacement. “Add graph” or “explain curve” is not a sufficient teaching requirement.

Pair this with a terse page/range disposition index: concept IDs, consolidated into IDs, or non-substantive exclusion with reason. Every page must be accounted for, including the last; a range is suitable only if its disposition is uniform. A page index cannot certify that every concept on a page was found. During review, inspect the raw page for unrecorded relationships and graphical content as well as checking mapped IDs.

## Two independent allocation judgments

**Curricular importance:** centrality to stated/inferred learning objectives, prerequisite role, connections to later concepts, problem-solving relevance, and significance in the subject.

**Explanatory difficulty:** required reasoning steps, missing prerequisite links, subtle or counterintuitive behavior, interacting mechanisms, hidden assumptions, common misconceptions, and difficulty interpreting mathematics or diagrams.

Use both rather than a single numeric score:

| Importance | Difficulty | Typical treatment |
|---|---|---|
| High | High | Full causal/derivation chain, necessary prerequisite bridge, discriminating example, essential visuals, deeper independent checks |
| High | Low | Clear concise explanation, meaningful use/relationship check; do not inflate familiar definitions |
| Low | High | Bounded but sufficient explanation of the difficult part; provide a usable local prerequisite or cross-reference |
| Low | Low | Concise complete treatment, perhaps grouped with related concepts |

A brief source remark can be central and difficult. A long slide sequence can be repetition. Neither slide count nor visual prominence determines either judgment. Depth should resolve a concrete student difficulty, not fill a length target.

## Teaching architecture and section acceptance

Order concepts so prerequisites are available before use. Teach shared foundations once and cross-reference them; preserve topic numbering where helpful for navigation. Group concepts with strong dependencies; record essential links across sections and allocate review effort to high-risk links. This architecture is a view of the same specification, not a second administrative artifact.

Choose appropriate understanding criteria per concept. Examples: trace a mechanism and predict a changed condition; derive a relation and name its assumptions; interpret graph regions and a parameter change; reconstruct schematic connectivity; execute a procedure and explain a failure case; calculate with units; compare alternatives under a stated objective. A simple definition may need only a correct distinction and use case. Several criteria may be needed for a coupled system.

Before marking a section checked, answer its selected questions using only the chapter and declared audience prerequisites. Point to the exact explanation, intermediate step, worked result, or interpreted visual supporting the answer. If one must supply missing knowledge mentally, that is a teaching gap. Do not add all possible educational devices mechanically. Mark unresolved criteria and repair the local section; do not proceed on a heading-only coverage claim.

For a calculation or procedure objective, include a criterion that tests use on a representative instance when symbolic reconstruction alone would not demonstrate use. A correct derivation can still leave the student unable to select inputs, execute the method, or interpret the result. Choose an example for that specific gap rather than demanding numerical examples for every formula.

Check prerequisites introduced by your own notation and explanations, not just those visible in the source. A student who can substitute into a formula may still lack the meaning of its variables, operators, averages, or model quantities; probe that meaning where it affects use.

Persist the specification with the source hash, audience assumption, and relevant dependencies. On source changes compare page-level evidence or affected ranges, preserve unchanged work, and update affected concepts and dependents. Do not reuse an acceptance result after its explanation, figure, or prerequisite changed. See [model-routing.md](model-routing.md) for resumption and resource limits.
