# Teaching, source notation, and V1

Read this before a new textbook draft, or when resolving notation and corrections in an existing document.

## Turn source material into a learning sequence

Start with the supplied learning objectives and substantive topic coverage. Reorder only when it improves prerequisite flow, and keep a source mapping so the reader can navigate back. Identify what the learner must already know; provide concise bridging explanations where the source assumes a missing prerequisite. Do not fabricate a missing chapter or imply outside material came from the slides.

A useful chapter normally establishes the problem and intuition, develops the mechanism/model, explains its equations and assumptions, works a representative example, shows alternatives or limits, and ends with a recap, common mistakes, and self-tests with brief answers. Adapt this shape to the subject. The goal is connected, teachable prose with useful mathematics and images, not a fixed word count, repeated boilerplate, or a slide-by-slide translation.

Allocate space by conceptual difficulty and prerequisite needs, not slide count. A terse derivation may need several intermediate steps and an annotated diagram; several repetitive slides may need one clear paragraph. Define a shared concept once, then cross-reference it rather than duplicating explanations. Use equations, truth tables, or compact comparisons when they communicate more clearly than long prose, but explain the meaning of each important result. Density means useful understanding per page, not smaller type, omitted reasoning, or compressed algebra that students cannot follow.

Choose examples that teach distinct reasoning, expose a misconception, or test a meaningful boundary. Remove extra examples that merely substitute new numbers. Keep an intuition → formal model → practical application progression where appropriate, with explicit transitions between ideas. Recaps synthesize rather than replaying the chapter. Answered self-tests should check understanding and transfer as well as calculation. Prefer clear, technically precise academic English over inflated formality.

Teach a procedure through a worked example with inputs, units, region/assumption checks, intermediate steps, result, and interpretation. Follow [technical-verification.md](technical-verification.md) for mathematical and engineering checks. Label new numbers as illustrative; do not give invented constants, fabricated measurements, or a smooth fitted line the authority of source data. If a slide leaves an exercise unfinished, solve it with stated assumptions or mark a deliberate exercise and give its answer. If missing conditions prevent a unique answer, explain the underdetermination and give conditional answers or identify the missing data. Avoid reproducing empty fields as completed explanatory graphics.

## Source notation is part of the content

For each important symbol, preserve its exact visible form: case, Greek/Latin alphabet, bold/vector treatment, bars, subscripts, superscripts, sign, indexing, reference node, and units. Explain it on first use, even if it appears in a global notation table. Define acronym labels inside diagrams and plots. Use a short local notation key when a chapter introduces many symbols; consolidate genuinely shared symbols in the front matter or appendix.

A notation register can have these columns:

| Source location | Source symbol | Meaning and units | Convention/assumption | Notes symbol or mapping |
|---|---|---|---|---|

Do not silently rewrite an unfamiliar source symbol to the notation you normally use. If one symbol means two things, disambiguate locally and give an explicit mapping. If different decks use different sign or normalization conventions, state each convention and the translation before combining equations. Distinguish physical versus normalized quantities, threshold versus thermal quantities, direction of current versus carrier motion, total-edge activity versus charging-event activity, and analogous subject-specific ambiguities **when present in the material**.

OCR and PDF extraction often lose minus signs, overbars, prime marks, fractions, and indices. Inspect the actual page before declaring a contradiction or correction. A diagram's polarity and orientation can resolve an apparent textual ambiguity. Validate notation in the final render as well as the source markup.

## References and corrections

Use short, nearby references such as “Source: devices.pdf, PDF pp. 14–18.” Source locations always refer to the supplied file, not newly generated book pages. If printed slide numbering differs, explain the mapping once and record both numbers when needed. Figure captions identify source file and page plus “cropped” or “adapted”; newly created graphics say “original illustrative model/schematic” or a more precise description. Cite original data if a new plot redraws it.

Keep a compact correction register for meaningful source errors and unresolved ambiguities:

| Source file/page | Original statement or symbol | Correction/interpretation | Reason/evidence | Status |
|---|---|---|---|---|

Verify a suspected error against the rendered source and a reproducible calculation or relevant authoritative reference before correcting it. Explain a confirmed arithmetic, dimensional, sign, or logical correction near the affected material and in the register. Preserve enough of the original wording/equation to identify what changed. For ambiguity, state the interpretation and why it fits, and mark uncertainty rather than asserting a definitive correction. Distinguish a source error, extraction error, pedagogical simplification, and alternate convention. Avoid inventing corrections to populate the register; if none are needed, say so or omit the register.

## Supplemental knowledge without false attribution

Fill missing prerequisite links, derivation steps, intuition, and applicability conditions when needed for a self-contained chapter. Preserve the course's terminology and notation, explaining any mapping from outside references. Keep additions relevant to the course's objectives rather than inventing missing course chapters.

Distinguish a direct source claim, an explanation/derivation supplied by the notes, and an externally supported addition. A short nearby “Supplemental explanation”, “Derived here under …”, or “Illustrative example” label, or a clearly scoped section note, is enough; avoid distracting labels on every sentence. A source-page citation must not imply that new assumptions, numerical values, or derivations appeared on that page. Mark redrawn plots and schematics as source adaptations or original explanatory models as appropriate.

Research is targeted to a concrete gap or uncertainty. Verify unfamiliar or consequential technical additions against reputable textbooks, primary papers/standards, or official manufacturer, architecture, language, or operating-system documentation when available and permitted. Read the supporting passage, check its conditions/conventions and relevance, and record the actual edition/section/page or stable URL; include a version for implementation-specific claims. Search snippets and other model responses are not verification. Familiar bridging algebra can be verified by derivation without a broad external search.

Never fabricate citations, textbook editions, page numbers, measurements, device parameters, or simulation results. Use explicit illustrative assumptions for new numerical examples. If an authoritative reference is inaccessible or external research is restricted, use supplied evidence and direct checks where sufficient, label remaining uncertainty, and leave consequential unsupported claims conditional or unresolved. Do not silently correct a source or imply a reference was consulted when it was not. Research a conflict only far enough to resolve it or explain what remains unknown; no obligatory bibliography or broad research phase is required for each lecture.

## Coverage and preservation

Maintain a lightweight coverage map with source page ranges, substantive topic, destination section, relevant visuals, and used/consolidated/excluded disposition. Review the end of every source, not only its early or easy sections. Exclude covers, repeated dividers, exact/progressive duplicates, and unrelated material for a stated reason; text-only slides can be covered by prose without an image.

For a new book, V1 contains every intended chapter and a substantive visual treatment. Use the V1 review to find weak explanation, missing prerequisite links, notation conflicts, weak examples, and unillustrated relationships. Do not release placeholders or unanswered self-tests as a finished textbook.

For expansion of existing notes, preserve the requested explanations, calculations, equations, and useful figures. Changes for a confirmed source error should be explicit and recorded. Compare editable chapter content outside added figure calls where practical; a PDF byte hash only proves preservation of the original input, not preservation of its content in the new edition. With a PDF-only original, retaining original pages and inserting Typst-created illustration pages is an option when faithful reflow is unreliable; update navigation and make added pages identifiable.
