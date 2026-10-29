# Figures and reproducible Typst builds

## Select visuals by learning purpose

Record each consequential visual decision in the teaching specification:

- **Essential:** needed to interpret, reconstruct, or use a concept. Reuse the source or replace it with a clearer equivalent preserving its learning-relevant relationships.
- **Optional:** adds a distinct insight worth its production and review effort.
- **Redundant:** the same relationships survive at an identified destination. Sharing a topic does not establish redundancy.
- **Unnecessary or unsuitable:** no teaching purpose, or misleading/incomplete/illegible. Repair or replace if essential; otherwise exclude with a reason.

Do not redraw a clear source figure merely for originality. Missing equations or calibration data need not prevent reuse of a qualitative source graph. A single-model illustration cannot replace a comparison whose crossover, relative timing, or parameter behavior is the objective.

Interpret figures in adjacent prose. For graphs, explain axes, units/normalization, relevant regions, key points, parameter effects, and supported conclusions. Distinguish measurements, simulation, analytical curves, and illustrative sketches. Preserve supplied uncertainty and avoid inferring unsupported quantitative relationships.

Use exact plotting tools for scientific graphs. Use SVG, Graphviz, Typst geometry, or suitable engineering tools for diagrams; establish nodes/terminals, state transitions, Boolean behavior, or timed events before drawing. Keep generating equations/data, parameters, assumptions, and editable inputs. Image generation is unsuitable for authoritative plots, circuits, logic, timing, or other exact structure. Technical checks are in [review.md](review.md).

Captions state the inference and relevant conditions, with source file/page and “cropped” or “adapted,” or an original illustrative-model label. Inspect every new/revised figure and crop at readable resolution and final display size. Preserve all meaningful marks; split dense panels instead of shrinking labels. Roughly 8–10 pt is a useful minimum label size at book scale.

## PDF helpers

Run these from the installed skill directory, substituting actual project paths. Dependencies: Python 3.10+, `pypdf`, Pillow, and Poppler (`pdftoppm`). Prefer available bundled/project dependencies.

```sh
python scripts/source_assets.py inventory --out PROJECT/source-inventory SOURCE.pdf
python scripts/source_assets.py crop --source SOURCE.pdf --page 12 --bounds 0.1 0.2 0.9 0.8 --out PROJECT/figures/source
python scripts/source_assets.py verify PROJECT/source-inventory/inventory.json
```

Inventory records hashes, geometry/rotation, and page-marked text. Give explicit inputs so generated PDFs do not enter the source set; keep originals immutable. Existing baselines are not overwritten.

Crop bounds are normalized left/top/right/bottom on the upright visible page, using 1-based PDF pages. The helper handles rotation/crop-box offsets and produces PDF, PNG, and JSON provenance with content-dependent filenames. Inspect the full page before choosing bounds, then the resulting PNG. Embed PNG crops by default: a cropped PDF can retain hidden searchable slide text. If using PDF embedding, test compiler support and inspect extracted output text for leakage.

## Typst setup

Reuse an existing project or copy `assets/typst-starter/`, replacing its demonstration content. Keep chapters, source/original figures, inventory, and review files separate from final deliverables. Apply the exported wrapper using `#show: textbook.with(...)`; importing a module's top-level `set` rules does not apply them to its caller. Use one level-1 heading per chapter and centralize chapter numbering/breaks in the theme.

Check the installed compiler and fonts with a representative build:

```sh
typst compile --root PROJECT PROJECT/main.typ PROJECT/output/notes.pdf
```

If only Python bindings are available, use their supported compile API. Test supported image formats and math attachments in the render; Typst syntax differs from LaTeX. Keep dependencies local where practical. Use a standalone TeX asset for a specialized figure when needed; move the whole book to LaTeX only for a concrete book-level requirement that Typst plus assets cannot reasonably meet. Preserve the editable project if tooling blocks a build.

For version-specific questions, consult official [image](https://typst.app/docs/reference/visualize/image/), [figure](https://typst.app/docs/reference/model/figure/), [heading](https://typst.app/docs/reference/model/heading/), or [PDF export](https://typst.app/docs/reference/pdf/) documentation as needed.

## Inspect and deliver

```sh
python scripts/review_pdf.py PROJECT/output/notes.pdf --out PROJECT/review
python scripts/review_pdf.py PROJECT/output/notes.pdf --pages 3,7-10 --scale 1600 --out PROJECT/review/changed
python scripts/review_pdf.py --images CROP.png FIGURE.png --out PROJECT/review/figures
```

The report and contact sheets are review inputs; rendering leaves inspection pending. Inspect every final page at overview scale, then dense/changed/suspicious pages and figures at readable resolution. Check symbols, captions, tables, placement, orphans, sparse pages, diagnostics, missing glyphs, and unresolved references. Record actual inspection findings; text-length heuristics cannot judge figure-heavy pages.

Deliver current PDF, editable Typst sources, included crop provenance, figure generators/data or editable diagrams, and consequential check scripts. Record actual build/generation commands, tool versions, fonts, dependencies, and seeds where relevant. Rebuild from the recorded root with project-relative asset paths and current assets; eliminate dependencies on temporary worker paths. Keep diagnostic intermediates out of deliverables.
