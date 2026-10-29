---
name: textbook-notes2
description: Create or expand self-contained university textbook notes from slides, PDFs, readings, or existing notes, using Typst by default. Use for substantial learning documents that need explanations, derivations, worked examples, and teaching visuals, rather than brief summaries or slide decks.
metadata:
  short-description: Self-contained, verified university notes with Typst
---

# Textbook Notes 2

Sources define the curriculum, not the amount of explanation needed. Cover every distinct substantive concept, including appendices and late material. Teach toward what the student must be able to explain or do; headings and formulas alone do not establish coverage. Default to English and Typst unless the user specifies otherwise. Extend a working project rather than restarting it.

## Workflow

1. **Map the collection.** Inventory the original inputs with hashes and stable locations. Survey the entire source, including every PDF page visually, to locate topics, graphical content, notation, and prerequisites. An overview is for navigation; inspect details at readable resolution before interpreting them. PDF helpers are in [visuals-and-build.md](references/visuals-and-build.md).
2. **Plan the next chapter.** Follow [teaching-analysis.md](references/teaching-analysis.md): inspect its full source scope and refine one compact teaching specification. Keep later chapters provisional, ordered by prerequisites.
3. **Write and check sections.** Use [authoring.md](references/authoring.md) for explanations and attribution, and [visuals-and-build.md](references/visuals-and-build.md) for figures and Typst. Develop reasoning, examples, and essential visuals together. Compile a representative section early.
4. **Review the evidence.** Apply [review.md](references/review.md) to the raw source, specification, and actual notes. Check coverage, teachability, and technical accuracy as distinct questions. Repair failed criteria and affected dependencies before accepting the section.
5. **Integrate and deliver.** Reconcile notation and cross-references, compile current sources, inspect the final PDF, and verify input hashes. Deliver the PDF and reproducible editable project with asset provenance, build commands, and material limitations.

Repeat chapter by chapter. Completion requires a disposition for every source page, a destination and fulfilled learning criteria for every substantive concept, supported consequential results, interpreted essential visuals, and a readable current PDF. Localize unresolved ambiguities; if work remains, save its exact scope instead of claiming completion.

For resumption, resource modes, or authorized delegation, read [execution.md](references/execution.md). For skill maintenance only, read [regression-evals.md](references/regression-evals.md).
