# Route: section-draft

Use to create or substantially rebuild one or more named manuscript sections from supplied notes, figures, tables, results, citations, or an approved plan.

Do not use when the primary task is line/flow improvement of usable existing prose; use `nature-polish` instead.

## Procedure

1. Load every requested section fragment and `references/manuscript-control.md`.
2. State each section's job, one-sentence argument, primary reader question, and terminology lock.
3. Run the alignment checkpoint. If the lead claim, result order, or terminology is ambiguous, stop at `confirm` before full prose.
4. Build a source trace before prose. Use `supplied`, `reported`, `reproduced`, `inferred`, `proposed`, or `missing`.
5. For Results or a full manuscript, classify result blocks and allocate them before writing.
6. Assign one job per paragraph and apply the deletion check to additions.
7. Draft only details supported by the trace; retain placeholders for absent evidence.
8. Return a claim-evidence-boundary map, consistency findings when applicable, and the smallest missing-input list.

## Contract

Use the `section-draft` headings from `static/core/output-format.md` exactly, including the process card. A `Draft` may contain placeholders; it must not make missing results sound complete.

## Boundary

- Draft only from the supplied source trace or an approved upstream artifact.
- Do not add results, citations, causal mechanisms, authorship, or certainty that the trace does not support.
- If the source trace is incomplete, stop at a bounded draft with placeholders and a missing-input checkpoint.
