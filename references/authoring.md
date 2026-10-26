# Integrated section authoring

Read when writing a new section or expanding existing notes. Start from the compact specification in [teaching-analysis.md](teaching-analysis.md), not a slide-by-slide expansion or a whole-book first-draft milestone.

## Bring each section to teaching adequacy

Use the assigned objectives, prerequisites, depth, and understanding criteria to decide what to explain. Establish the problem and intuition, develop the mechanism/model and necessary reasoning, and show use or limits where needed. This is a teaching logic, not a mandatory repeated chapter template. Simple definitions can be concise; subtle relationships may require sustained explanation even if the source gives them one sentence.

Author explanations, derivations, examples, and essential figures together. Make missing intermediate steps explicit: connect each consequential equality or procedural decision to the definition, assumption, rule, or mechanism that justifies it. Explain what equations mean, not only how to manipulate them. Supply a local prerequisite bridge or a precise cross-reference before relying on undeclared knowledge. Preserve source traceability when changing the teaching order.

Choose examples that teach distinct reasoning, expose a misconception, or test a meaningful boundary; remove examples that merely substitute new numbers. Teach a procedure with inputs, assumptions/region checks, intermediate decisions, result, and interpretation. Label new values illustrative. Solve unfinished source examples under stated conditions or explain why missing data prevent a unique answer. Deliberate exercises need answers or solution guidance; empty source fields are not completed teaching graphics.

Use connected precise academic prose and appropriate mathematics rather than inflated formality. Recaps, common-mistake notes, and answered self-tests are useful when they synthesize or test the material; they are not compulsory boilerplate for every section. Define shared concepts once and cross-reference them. Density means understanding per page, not smaller type or omitted reasoning.

Before marking a section checked, use its selected teach-back/application criteria and point to the supporting passages, intermediate steps, examples, and figures. Apply [technical-verification.md](technical-verification.md) to consequential claims and worked results. Build and inspect the section with the actual assets using [visuals-and-build.md](visuals-and-build.md). A satisfactory section may still need independent review, but should not knowingly defer its core teaching to later generic passes. Revisit it only for an identified gap, review finding, or changed dependency.

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

Use the concept specification and page-disposition index as the coverage record; do not create another topic-only manifest. Every substantive objective needs a destination and evidence that its teaching criteria are fulfilled. Covers, dividers, and true duplicates can be excluded/consolidated with reasons; lower-priority technical content remains covered concisely. Inspect late source sections and graphical content for concepts the plan missed. See [pedagogical-review.md](pedagogical-review.md) for the source-to-output audit.

For expansion of existing notes, preserve the requested explanations, calculations, equations, and useful figures. Changes for a confirmed source error should be explicit and recorded. Compare editable chapter content outside added figure calls where practical; a PDF byte hash proves preservation of the input, not of its content in the new edition. With a PDF-only original, retaining original pages and inserting Typst-created teaching pages is an option when faithful reflow is unreliable; update navigation and make additions identifiable. Filling a teaching gap does not authorize replacing unrelated satisfactory material.
