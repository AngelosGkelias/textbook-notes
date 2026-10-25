---
name: textbook-notes
description: Create or expand textbook-quality study notes from university lecture slides, PDFs, readings, or existing notes using Typst, with full source coverage, worked explanations, technical verification, and teaching visuals. Use for substantive learning documents and illustrated editions, rather than brief summaries or presentation decks.
metadata:
  short-description: Verified engineering textbook notes with Typst
---

# Textbook Notes

Create a coherent learning document that students can learn from without constantly consulting the slides. Maximize conceptual understanding per page: expand according to difficulty and missing prerequisites, keep simple concepts concise, and consolidate repetition without losing substantive coverage. Use precise academic English, useful mathematics, and connected explanations; impose no word, page, or figure quotas.
Default to **English**, including captions and figure labels, unless the user requests another language. Teach visually throughout: relevant diagrams, graphs, images, and worked visual examples belong beside the explanations from the first complete draft.

## Working defaults

- **Typst first.** Use Typst for the book, ordinary mathematics, tables, and native diagrams. Use exact plotting/drawing tools when they express the material better. Use LaTeX only for a concrete requirement that is impractical in Typst, preferably for a standalone asset embedded into the Typst book. Existing LaTeX sources or ordinary equations alone do not justify switching the whole document. See [visuals-and-build.md](references/visuals-and-build.md) for the hybrid route.
- **Route work by difficulty.** Use only models and reasoning settings advertised by the current environment. Prefer economical capabilities for extraction, mapping, organization, and straightforward drafting; stronger reasoning for difficult mathematics, engineering derivations, schematics, and chapters; reserve the strongest capabilities for exceptional problems or consequential independent checks. Respect explicit model preferences and budgets. Use internal subagents when parallel work materially improves quality or efficiency; small projects can stay with one agent. See [delegation.md](references/delegation.md) when choosing workers or reviewers. Never claim a model, effort, or delegation that was not used.
- **Verify proportionately.** Important equations, derivations, circuits, and worked examples require checks of intermediate steps, units, signs, assumptions, limits, and diagram meaning. Compilation and fluent prose do not establish correctness. Read [technical-verification.md](references/technical-verification.md) for engineering material; use independent review selectively and stop when its evidence-based completion criteria are met.
- **Preserve inputs.** Never overwrite supplied slides, readings, or existing notes. Author in a separate project folder and create a clearly named new PDF for revisions. Keep editable sources and provenance with the output.
- **Respect source notation.** Retain the slides' symbols, subscripts, signs, labels, units, and named conventions; explain them where introduced and maintain a notation key. When a clearer or disambiguated symbol is needed, show its mapping to the original. Do not silently normalize conflicting conventions. Add nearby slide references and explicit, justified corrections. See [authoring.md](references/authoring.md).

## 1. Establish scope and a teaching plan

Inspect the supplied materials and any existing editable sources. Identify the intended audience, prerequisite gaps, requested depth, and language from context; ask only if a missing decision materially changes the work. Keep the supplied topic/chapter numbering when it helps source navigation, and do not invent missing course chapters.

Inventory every source, including its page/slide count and hash. Extract text with explicit **1-based source PDF page markers**; distinguish printed slide numbers if different. Inspect rendered pages for equations, notation, images, and scanned material: extracted text is a navigation aid, not ground truth. The helper `scripts/source_assets.py inventory` creates a PDF inventory, numbered text, and a hash baseline. Use format-appropriate readers for non-PDF sources.

Build a chapter outline and coverage map spanning the **entire** source, including late sections and appendices that teach substantive material. Pair the topic plan with a visual plan: which relationships need a schematic, curve, image, spatial comparison, process diagram, timeline, or annotated worked example? Select every distinct relevant teaching visual, avoiding repeated progressive-build versions. Set no arbitrary figure quota.

For a new document, read [authoring.md](references/authoring.md) before drafting. For an existing-notes expansion, read it for notation/corrections and preserve the requested content: use an editable working copy where possible; with PDF-only material choose faithful reconstruction or inserted figure pages while retaining the original text and logical sequence. Verify preservation rather than assuming successful compilation proves it.

## 2. Set up the project and delegate

Copy `assets/typst-starter/` into the work project when useful. Adapt the title, source map, styles, and chapter files; remove the starter's demonstration content from the deliverable. Compile a small representative section early to verify mathematics, fonts, figures, and references before authoring every chapter.

Choose direct work for a small or tightly coupled project. For large, separable projects, delegate disjoint chapters or tasks, sized by conceptual workload and dependencies rather than page count. The lead author owns the shared theme, main book, notation/correction registers, build, and integration. Each worker owns explicit chapter files, an asset prefix, and separate coverage/visual/verification records. Escalate difficult explanations or uncertainties without restarting already satisfactory work.

Read [delegation.md](references/delegation.md) when dispatching workers. Give each worker the raw source, source-page map, teaching/visual objectives, shared Typst interface, ownership, and a precise completion contract. Workers must read their full assigned source, write connected explanations and worked examples, inspect their **actual rendered crops**, and report unresolved uncertainties. A list of recommended figures or an uncompiled outline is not a completed chapter.

## 3. Produce the complete V1

V1 is a compiled, end-to-end textbook draft containing all planned chapters, substantial explanations, worked methods/calculations, notation definitions, source references, useful original/source figures, recap, common mistakes, and answered self-tests. Build visuals into V1; do not defer them to an optional later pass. A provisional draft may still need editing, but must be complete enough to assess coverage and teaching quality. Save a source/PDF checkpoint of V1 before refinement; the final edition remains the deliverable unless a checkpoint is requested.

Explain why each model or method works, when it applies, and how to use it. Define assumptions, signs, scales, boundary conditions, and units. Distinguish mathematical identities, approximate models, empirical relationships, and illustrative simplifications, as well as source examples, simulations, measurements, and technology-specific values. Verify important intermediate calculations as well as results; maintain a compact record of consequential checks and unresolved issues.

Expand incomplete slides with clearly identified supplemental explanations. Preserve course terminology and notation. Use targeted authoritative references for unfamiliar or consequential additions and suspected source errors, subject to the user's source constraints; a broad research phase is unnecessary. Do not invent data, measurements, citations, or certainty. See [authoring.md](references/authoring.md) for attribution and corrections.

Put references beside the relevant claims, formulas, examples, and figures. Record material errors or ambiguity in a compact correction register with source location, original statement/notation, corrected interpretation, and rationale. Cross-reference corrections locally; never silently repair a slide or treat a suspected extraction error as a confirmed slide error.

## 4. Integrate the visual teaching pass

Read [visuals-and-build.md](references/visuals-and-build.md) while extracting or creating figures. Keep a visual manifest linking each included image to its source page and crop, or to its generator, parameters, and assumptions. Use per-worker records to avoid concurrent writes to shared manifests.

For each crop, render the **crop itself** and inspect it before marking it ready. Include complete axes, units, legends, polarity marks, circuit connections, scale bars, and annotations. Remove stray paragraph fragments and avoid empty exercise fields. Choose a completed source version or redraw in English when a clean crop cannot preserve the teaching content. `scripts/source_assets.py crop` produces a PDF crop, PNG preview/inclusion asset, and provenance record; review it at final display size.

Create missing figures when they clarify mechanisms, trade-offs, model limits, comparisons, or a worked result. Select exact plotting, diagram, timing, or circuit-aware tools using [visuals-and-build.md](references/visuals-and-build.md). Check connections, labels, directions, polarities, timing, and plotted values against the described system before polishing appearance. Technical plots and schematics require exact structure and data rather than image generation. Use generated imagery only where an illustrative picture actually helps, and label it appropriately. Explain in the caption what the reader should notice, and connect the visual to the prose. Break dense source matrices into readable panels when needed. Avoid tiny labels, distant floats, decorative graphics, or full-slide screenshots standing in for explanation.

Integrate worker chapters, reconcile notation and duplicate material, and resolve source/figure discrepancies. The orchestrator independently reviews delivered figure sheets and representative full-size assets; a worker's “done” report is evidence to inspect, not a replacement for review.

## 5. Validate and deliver

Compile the latest sources and inspect compiler diagnostics. Resolve missing assets/glyphs, broken references, incorrect numbering, and clipped or overlapping material. Verify substantive coverage against the source map, close consequential technical findings with evidence, and confirm that no later chapter or figure placeholder was omitted. Reconcile overlapping explanations, use cross-references for repeated prerequisites, and remove examples or graphics that add no new understanding.

Render the final PDF into bounded contact sheets with `scripts/review_pdf.py`, inspect every page at overview scale, and open dense, changed, or suspicious pages and new figures at readable resolution. Check figure/caption agreement, notation, source references, table integrity, legibility, page flow, and chapter transitions. Use automated text/geometry checks as support, not proof of visual or technical correctness. After a material fix, rebuild and review the affected output. Finish once substantive coverage, technical accuracy, and readable layout are satisfied; do not add content or repeat unchanged checks without a concrete reason.

Verify original input hashes (`source_assets.py verify`). For an illustrated revision, also compare prose/equations or preserved PDF pages, accounting explicitly for approved corrections. Deliver the new PDF and an editable, reproducible project with figure generators/data, build commands, dependency/font versions, source mapping, and relevant verification evidence. Briefly state scope and material limitations, including any unresolved source ambiguity or unavailable check. Do not label unchecked material as verified or silently modify the original document.
