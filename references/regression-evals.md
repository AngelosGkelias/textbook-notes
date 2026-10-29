# Skill maintenance evaluations

These fixtures test behavior, not an extra production phase. Run helper/package regressions with:

```sh
python evals/test_package.py
python evals/make_fixtures.py --out /tmp/notes-eval-UNIQUE
```

The generator needs reportlab. It creates a seven-page teaching packet, a 144-page synthetic imported resumption project, and separate two-page comparison authoring/review cases. Use `--case comparison` for only the latter. Requests choose Markdown and figure assets so teaching tests do not depend on Typst availability.

For independent forward tests, copy production instructions/assets into an isolated skill snapshot without `evals/`, this reference, or its entrypoint link. Give the evaluator only that snapshot, the relevant raw case files and request, and an isolated output directory. Do not reveal generator code, [rubric.json](../evals/rubric.json), other cases, expected answers, or prior findings. Preserve initial analysis before authoring; record later changes separately. Keep comparison authoring and seeded review in fresh contexts.

Afterward, grade analysis and content separately against the rubric using actual source/output anchors, equations, and figure assets. Verify worked values independently; do not grade wording, length, headings, or self-reported completion. The cases cover missing reasoning/prerequisites, scientific graphs, source errors, late content, false acceptance, and selective resumption.

For resumption, compare artifact hashes, invalidated dependencies, page dispositions, and exposed source-read operations. Input hashing is not semantic reprocessing. Equal text or sampled endpoints cannot establish current visual inspection for all pages. State the limit if tool traces are unavailable.

Use small representative cases for model/effort comparisons only when the result would inform allocation. Compare teaching/technical outcomes before exposed resource use; leave unavailable measurements unknown. A bounded test supports its tested behavior, not a general quality ranking.
