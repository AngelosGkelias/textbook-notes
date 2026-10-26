---
name: textbook-notes
description: Create or expand self-contained university textbook notes from lecture slides, PDFs, readings, or existing notes using Typst, with concept-level teaching analysis, complete substantive coverage, technical verification, and essential teaching visuals. Use for substantive learning documents rather than brief summaries or presentation decks.
metadata:
  short-description: Self-contained, verified university notes with Typst
---

# Textbook Notes

Act as a university textbook author. Sources define the substantive curriculum; their brevity does not define sufficient explanation. Optimize understanding, accuracy, and efficient model use, without word, page, or figure quotas. Cover every distinct substantive concept, including late material; lower priority permits concision, never silent omission. Default to English unless requested otherwise.

Use **Typst first**, retaining working templates, source tools, and styling. Preserve original inputs, source notation, nearby citations, explicit correction tracking, and editable, reproducible output. Use an existing project when available; do not restart satisfactory work.

## Workflow

1. **Comprehend the complete source.** Inventory sources and hashes; extract page-marked text and visually inspect every page, including equations, graphs, schematics, tables, and annotations. Text extraction is a navigation aid. Expand dense or ambiguous regions to readable resolution. Account for appendices and the source's end. For PDFs, use `scripts/source_assets.py inventory`; use format-appropriate readers otherwise.
2. **Analyze concepts before writing.** Read [teaching-analysis.md](references/teaching-analysis.md). Identify mechanisms, relationships, assumptions, methods, and limitations within slides rather than treating headings as concepts. Maintain one compact teaching specification with source locations, prerequisites, required explanation/reasoning, depth, visual/example decisions, and observable understanding criteria. Assess curricular importance and explanatory difficulty independently.
3. **Arrange the teaching architecture.** Use that same specification to order prerequisites, group related concepts, allocate explanation effort, and choose section boundaries. Keep traceability when reordering or consolidating. No separate large planning document is required. Discover runtime capabilities and choose **Balanced** by default using [model-routing.md](references/model-routing.md); Economy and Maximum quality change resource allocation, not substantive requirements. Direct work is the default; read [delegation.md](references/delegation.md) only when delegation is useful and permitted.
4. **Author and validate each section together.** Read [authoring.md](references/authoring.md). Explain mechanisms, assumptions, derivations, examples, and essential visuals together; validate the section against its teaching specification before marking it complete. Read [visuals-and-build.md](references/visuals-and-build.md) for figures/build setup and [technical-verification.md](references/technical-verification.md) for consequential technical checks. Compile a representative section early to test the toolchain. Revisit completed sections only for an identified defect or changed dependency.
5. **Review teaching and technical accuracy independently.** Read [pedagogical-review.md](references/pedagogical-review.md). Compare raw sources, teaching specifications, and actual chapters; audit all substantive coverage and probe understanding with targeted teach-back questions. Use a separate reviewer where available and justified, with deeper review for difficult or consequential concepts. Technical reconstruction and teaching review are distinct from PDF checks. Repair affected sections and their dependents; disclose self-review if an independent reviewer is unavailable.
6. **Integrate, compile, and deliver.** Reconcile notation, cross-references, coverage, corrections, and dependencies. Compile current sources, resolve diagnostics, inspect every final PDF page at overview scale and dense/changed pages and figures at readable resolution using `scripts/review_pdf.py`. Verify input hashes with `source_assets.py verify`. Deliver the PDF plus reproducible sources, included asset provenance/generators, build commands, and material limitations.

## Completion and resource discipline

A concept is complete when the notes enable the appropriate action—explain, reconstruct, derive, interpret, calculate, apply, compare, or predict—with evidence at a destination location. A name, equation, figure, citation, heading match, fluent prose, or successful compile alone is insufficient. See the analysis and review references for how to choose and test these actions.

Preserve essential source visuals or replace them with demonstrably clearer equivalents. Each included figure answers a specific educational question; create it beside its explanation. Verify scientific axes, behavior, assumptions and data provenance, and schematic connectivity and meaning. Do not fabricate measurements or quantitative relationships.

Use scripts for mechanical work and the least costly adequate model/effort for reasoning. Escalate bounded hard problems on evidence. Persist hash-linked inventories, teaching specifications, accepted sections, assets, and check results; resume by invalidating only changed dependencies. Do not create a mandatory full-document first draft, PDF checkpoint, separate visual pass, fixed rewrite cycle, automatic agent team, or blanket maximum-effort setting.

Finish when every source page has a disposition, every substantive concept has fulfilled teaching requirements, essential visuals and consequential technical checks have evidence, pedagogical findings are resolved, and the latest PDF is readable. Localize unresolved ambiguities explicitly; do not label affected material verified. If resources prevent completion, preserve progress and report exact remaining concepts/sections/checks rather than reducing essential explanation or claiming completion.

For skill maintenance, use [regression-evals.md](references/regression-evals.md); these small evaluations are separate from ordinary textbook production.
