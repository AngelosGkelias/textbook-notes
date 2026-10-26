# Visual teaching, Typst, and reproducible builds

Read when extracting/creating figures or configuring the book build.

## Project and Typst route

A practical project has main.typ, theme.typ, chapters/, figures/source/, figures/original/, source-inventory/, review/, and a final output directory. These are project files, not extra instructions in the installed skill. Keep source files immutable and final PDFs outside the source-input set.

`assets/typst-starter/` is a small working starting point with a book theme, source notes, teaching callout, and an image figure helper. It demonstrates a chapter, math, a vector visual, and answered self-tests. Replace the sample content, customize the source map, and use separate chapter files. Apply the exported document wrapper with a `show` rule, as in the starter: importing a module with top-level `set` rules does not apply those rules to the caller. Each worker's isolated harness must apply the same wrapper so assets and typography are tested consistently. Use Typst math syntax deliberately: for example, `v_C (t)` keeps the function argument on the baseline; confirm attachments in the render rather than copying LaTeX syntax mechanically. Agree on heading levels before dispatch: one level-1 heading per chapter, level-2 sections, then level-3 subsections. Keep chapter breaks in the shared theme; avoid manual section breaks that strand a paragraph or half an example on a nearly empty page. Book headings can be reset with Typst counters when original chapter numbers are nonconsecutive; keep this numbering decision centralized.

Prefer available local/bundled tools; inspect the installed Typst version and compile a representative sample. A CLI build is `typst compile --root PROJECT PROJECT/main.typ PROJECT/output/notes.pdf`. If only Python bindings are available, use their supported compile API. Keep fonts locally available, avoid unnecessary package dependencies, and do not assume an untested template or remote package works.

Typst handles ordinary mathematical notation, aligned equations, tables, cross-references, and figures; these do not justify LaTeX fallback. Select figure tools by what must be represented accurately, using the tools actually available:

| Need | Preferred route | Required semantic check |
|---|---|---|
| Layout, equations, notation, tables | Typst | Correct symbols, attachments, units, references, and table meaning in the render |
| Numerical or analytical graphs | Matplotlib or another exact plotting tool, exported to a compatible vector/raster format | Reproducible equations/data, units/scales, parameter values and key-point/limit checks |
| Block diagrams, architectures, state/process graphs | SVG, native Typst shapes/drawing libraries, or Graphviz | Direction, labels, state transitions, buses and topology match the explanation |
| Transistor, analog, or logic schematics | Available circuit-aware drawing/EDA tools; controlled SVG/Typst geometry for simple schematics | Named-node/terminal connectivity, junctions versus crossings, device orientation, inversion, reference directions and power/body connections |
| Timing diagrams | Available timing-diagram tools or exact SVG/Typst/plotting code driven by explicit events | Edges, clock phases, delays, sampling instants and signal relationships match the worked trace |
| Specialized figure requiring a mature TeX-only package | Standalone LaTeX asset, only when the Typst-centered alternatives are impractical | Compile and inspect the asset, verify semantics, then embed a compatible PDF/SVG/PNG |

Examples of specialized routes include schematic editors, circuit drawing libraries, and waveform generators; their availability and export support must be checked, not assumed. A circuit simulator can validate a specified model/netlist but does not itself establish that the drawn circuit has the same connections. Do not install a large toolchain for a simple figure if a verifiable local route suffices. Only move the whole book to LaTeX when a substantial book-level requirement cannot reasonably be met by Typst plus standalone assets; record the concrete reason. Explicit user format instructions take precedence.

Supported image formats and PDF embedding restrictions depend on the installed compiler and export target; consult the official references below when needed. Test direct PDF embedding before relying on it; PNG is the portable source-crop default, and SVG is useful for exact new vector art. A PDF crop box can conceal original slide text visually while leaving it extractable. Inspect final searchable text when embedding a source PDF; if hidden slide paragraphs leak, use the rendered crop instead.

Official references for version-specific behavior:

- [Image formats and PDF restrictions](https://typst.app/docs/reference/visualize/image/)
- [Figures, captions, placement, and numbering](https://typst.app/docs/reference/model/figure/)
- [Headings and numbering](https://typst.app/docs/reference/model/heading/)
- [PDF export and standards](https://typst.app/docs/reference/pdf/)

## Source inventory and crop helper

The helpers require Python 3.10+, `pypdf`, Pillow for review sheets, and Poppler (`pdftoppm`). Prefer bundled dependencies or a project environment rather than changing global packages. Run `python scripts/source_assets.py --help` from the installed skill path for command details. Use explicit input files, not a recursive PDF glob that may include generated output.

- `inventory --out WORK/source-inventory SOURCE.pdf ...` records resolved paths, hashes, page geometry/rotation, text character counts, and page-numbered text. Flag near-empty extracted pages for visual/OCR review; empty extraction does not mean empty teaching content.
- `verify WORK/source-inventory/inventory.json` checks all original input hashes again.
- `crop --source SOURCE.pdf --page 12 --bounds 0.1 0.2 0.9 0.8 --out WORK/figures/source` takes normalized left/top/right/bottom bounds relative to the upright visible page. It produces a crop PDF, 300-dpi PNG, and individual JSON provenance. Filenames incorporate source content, page, bounds, and DPI so a revised crop cannot silently reuse a stale preview. The helper accounts for PDF page rotation and visible crop-box origins.

Inspect the full page first, choose a box, generate it, then inspect the **resulting PNG**. An in-range box is not a valid crop by itself. Keep a small safety margin around all meaningful marks. A source diagram that extends across a paragraph may need multiple crops or an original redraw. Do not keep clipped table rows, partial equations, random text strokes, or blank exercise fields merely to maximize a source-figure count.

Use per-figure/per-worker provenance records instead of letting several workers append one JSON file concurrently. At integration, collect only included assets and record the teaching purpose, destination, caption, and review state. For new figures record the generating code/tool, source relationship, equations/parameters/data, units, and assumptions.

## Visual selection and teaching decisions

Classify source and proposed visuals during concept analysis, then realize selected figures alongside their explanations:

| Class | Decision |
|---|---|
| Essential | Needed to interpret, reconstruct, or use a substantive concept; preserve the source figure or replace with a demonstrably clearer equivalent retaining all relevant semantics |
| Valuable but optional | Adds a distinct insight; include when its benefit justifies space and production/review effort |
| Redundant | Same teaching content already represented; consolidate and retain the best version |
| Unnecessary | No meaningful educational question answered; exclude |
| Unsuitable or misleading | Incorrect, incomplete, illegible, or implies unsupported conclusions; repair/replace if essential, otherwise exclude with reason |

Record the teaching question and disposition in the concept specification, linking included assets to their provenance; avoid a duplicate planning manifest. Prioritize mechanisms, mathematical relationships, system architecture, circuit connectivity, causality, operating regions, timing/state changes, parameter sensitivity, design trade-offs, and comparative performance when present. A full slide screenshot or generic flowchart cannot stand in for explanation. Avoid redrawing an already clear source figure just to make it original. If replacement is necessary, explain which learning-relevant feature it improves and verify that no source relationship was lost.

For an important scientific graph, explain the axes (variables, units, normalization and scale), curve behavior, assumptions, meaningful regions/key points, parameter dependencies, and conclusions the student may draw. Include those dependencies when supported by the source/model; identify unavailable information rather than inventing it. Say how a changed condition affects the relationship and why when that is part of the objective. A caption alone is rarely enough for a difficult graph.

Distinguish measured data, simulated data, analytical curves, and illustrative sketches. Preserve legitimate scales and uncertainty where supplied. Do not fabricate measurements, data fits, or unsupported quantitative relations. Store data/model and parameters with generated plots, check representative points/limits against calculations, and label illustrative assumptions. Familiar mathematical geometry also needs correct domains, orientation, and labels.

For an engineering diagram, first establish its semantic specification: component/terminal/node list, Boolean function/truth table, state transitions, or timed event sequence as appropriate. This can be a few lines in the generator or manifest, not a separate formal schema. Generate the drawing from that specification where possible. Trace connections and behaviors against the source and prose using [technical-verification.md](technical-verification.md). Pay particular attention to junction dots, wire crossings, bus widths, ground/reference nodes, transistor/body connections, inversion bubbles, arrow meaning, and clock phases. Neither attractive layout nor successful syntax validation proves the diagram represents the described system.

Inspect every new/revised figure and actual crop at readable resolution and final display size. Recheck semantic details after edits and after embedding. If a tool cannot express the required connections or symbols faithfully, change tools or simplify with explicit limitations; never retain a plausible-looking but incorrect schematic. Image generation is unsuitable for authoritative circuits, logic, timing, mathematical plots, or other exact engineering structure. It may supply clearly labeled conceptual illustrations when those actually aid learning.

Captions should tell the reader what to infer and state the relevant conditions, plus a source or original-illustration label. Introduce or interpret the figure in the adjacent prose. A new visual should add understanding rather than duplicate an existing table without a teaching reason. Dense matrices are often better as several panels; a zoomable image is not automatically readable at book scale. Prefer figure labels around 8–10 pt or larger at final size, and increase space or split panels rather than shrinking them to satisfy a page-count target.

## Final review helper

`python scripts/review_pdf.py NOTES.pdf --out WORK/review` records basic PDF diagnostics, renders all pages at overview resolution, and groups page images into bounded contact sheets. Use `--pages 3,7-10` for an affected-page rerun and `--scale 1600` when inspecting finer layout. For crop/new-figure sheets, use `python scripts/review_pdf.py --images CROP.png NEW-FIGURE.png --out WORK/review/figures`. Read its report; it does not prove correctness or detect every overlap.

Rendering produces review inputs, not a completed visual review. The report records rendered pages/assets with visual review pending; record actual inspection and findings in the project review notes. An affected-page rerun supplements the full-document inspection rather than replacing it.

Inspect all page sheets, then open dense/new/suspicious pages and all new or revised figure assets at readable resolution. Review axes and symbols at their actual display size, caption agreement, broken tables, float distance, heading orphans, excessively sparse pages, and source reference accuracy. Check compiler diagnostics, unresolved references, missing glyphs, and unexpected extracted slide paragraphs. A figure-only page may legitimately have little searchable text, so short-page heuristics need visual interpretation.

## Reproducible delivery

Keep editable Typst sources, included source crops and provenance, generated figure code/data or editable schematic files, and any check scripts used as technical evidence. Record the actual build and figure-generation commands, compiler/tool/package versions, required fonts, project-relative asset paths, and any seeds or external data dependencies. The starter's demonstration curve can be regenerated with `python generate_demo_curve.py` from its folder. Replace its demo content for real books.

Compile from the recorded project root using the current included assets, regenerating changed figures. Check that no unrecorded temporary/worker paths or missing fonts/packages are required. Pin dependencies when necessary for a repeatable build; avoid new remote packages when available local tools suffice. If a required tool or package is unavailable, preserve the editable project and identify the uncompleted build/check rather than claiming success or silently changing the requested authoring system.

For preservation, verify source hashes and compare the new edition's prose/equations with the original editable content outside figure additions. With intentionally retained original PDF pages, compare those page contents separately from the new illustration pages. Explain deliberate corrections instead of hiding differences in normalization. Deliver the final compiled PDF with the reproducible source project; keep diagnostic intermediates separate from deliverables.
