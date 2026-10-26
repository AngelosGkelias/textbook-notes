# Independent pedagogical review

Read when reviewing completed sections or integrating the book. This evaluates whether the chapter teaches; [technical-verification.md](technical-verification.md) evaluates whether its claims are correct, and [visuals-and-build.md](visuals-and-build.md) covers rendered layout. None substitutes for the others.

## Evidence and independence

Compare three actual artifacts: the original source (including rendered graphical content), the concept teaching specification, and the generated chapter with its figures. A worker summary or section-heading list is insufficient. Review the specification itself for concepts it failed to identify; otherwise an incomplete plan can certify an incomplete book.

Use an independent reviewer for a bounded teaching review where available and warranted. Give raw source ranges, audience assumptions, the specification, actual chapter/figures, and source constraints; do not supply a desired verdict or the author's self-certification. The reviewer may also perform technical checks, but must report teaching evidence separately. Independence does not require a premium model or several reviewers of every simple definition.

Guarantee a complete source-to-output audit, with lightweight review of straightforward material and intensive probes for high difficulty/importance, uncertain source interpretation, dense figures, and consequential dependencies. The full audit may be partitioned across section reviews and integrated once; it need not re-ingest the book. Every page/range and every substantive concept must be accounted for. Review graphical annotations and late sections explicitly.

If delegation is unavailable or disallowed, use a separate review context if the runtime offers one; otherwise perform an explicit source-first adversarial review after authoring and disclose that it is self-review. Reconstruct expected learning requirements from the source before comparing the author's claims. Do not present this as independent certification. Model agreement and source-heading matches are not evidence of adequacy.

## Find teaching failures

For each reviewed concept ask whether the chapter enables its selected understanding actions. Look for:

- Omitted substantive concepts, including relationships or limitations hidden within a slide.
- Names, definitions, formulas, or displayed diagrams standing in for an explanation.
- Missing intermediate reasoning, prerequisites, derivation conditions, and misleading simplifications.
- Missing examples needed to apply a method or distinguish a common misconception.
- Essential graphs omitted, cropped incompletely, or displayed without interpretation.
- Technically correct figures that do not answer the teaching question.
- Unexplained relationships, operating regions, parameter dependencies, or trade-offs.
- Excessive attention to easy/repetitive material while central difficult ideas remain compressed.

Select teach-back questions that discriminate understanding rather than recall: “Why does this step follow?”, “Reconstruct the connections and trace this input”, “What changes if this assumption is relaxed?”, “Derive this result from the preceding model”, “Interpret this graph region”, “Apply the method to this nearby case”. Use the actions and key-answer elements in the specification, adding a probe where its criteria are weak. Do not demand every action of every concept.

Attempt answers from the chapter and declared prerequisites alone. Cite the passages/figure labels/intermediate steps that make the answer possible; explain what is missing when they do not. A plausible answer supplied by the reviewer's own subject knowledge does not establish teachability. Technical accuracy of the answer must also be checked when consequential.

## Report and repair locally

Use one concise findings list, incorporated into the existing section/project record:

| Concept and source location | Destination anchor/figure | Concrete failure and evidence | Required local repair | Closure evidence |
|---|---|---|---|---|

Give the failed question or omitted relationship, not “needs more depth”. Distinguish a missing essential explanation from optional enrichment. If no failure is found, retain representative teach-back evidence and audit scope rather than a generic approval.

Repair the affected section and any prerequisite/dependent passages whose meaning changes. Update a defective specification; otherwise reuse it. Recheck the failed criterion and dependent technical results, then review affected rendered pages after compilation. Broaden review only when a finding reveals a systematic blind spot or a new dependency problem. Do not restart satisfactory chapters or repeat full-document reviews without new evidence.

Close the teaching review only when substantive coverage is complete, selected understanding criteria have evidence in the output, essential visuals are interpreted, and no known material teaching gap remains. Keep source ambiguities and incomplete checks explicit and local. Under a resource limit, retain accepted work and identify the exact remaining concepts and review scope; an unfinished review is not a pass.
