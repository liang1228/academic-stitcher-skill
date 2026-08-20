# Route: section-draft

Use to create or substantially rebuild one or more named manuscript sections from supplied notes, figures, tables, results, citations, or an approved plan.

Do not use when the primary task is line/flow improvement of usable existing prose; use `nature-polish` instead.

## Procedure

1. Load every requested section fragment.
2. State each section's job and one-sentence argument.
3. Build a source trace before prose. Use `direct`, `reported`, `reproduced`, `inferred`, `proposed`, or `missing`.
4. Assign one job per paragraph.
5. Draft only details supported by the trace; retain placeholders for absent evidence.
6. Return a claim-evidence-boundary map and the smallest missing-input list.

## Contract

Use the `section-draft` headings from `static/core/output-format.md` exactly. A `Draft` may contain placeholders; it must not make missing results sound complete.
