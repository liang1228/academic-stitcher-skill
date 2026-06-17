# Quality Gates

Use only the gates relevant to the current request.

## Evidence Gate

- Every major claim maps to data, citation, figure, experiment, or explicit limitation.
- Unsupported claims are marked as `needs evidence`, `inferred`, or downgraded.
- Specific examples, mechanisms, applications, datasets, baselines, and future work must be either source-grounded or explicitly labeled as proposals.
- Vague user notes should remain bounded; do not make them sound more precise than the source.

## Citation And Attribution Gate

- Reused ideas, modules, code, datasets, formulas, figures, and distinctive wording require attribution.
- Do not cite papers the user has not actually read when precision matters; flag verification needs.

## Fair Comparison Gate

- Baselines match task, data, protocol, date, and venue level.
- Reported and reproduced numbers are not mixed silently.
- Tuning budgets, ablations, qualitative cases, and failed runs are disclosed.

## Flow Gate

- Each paragraph has one job: context, gap, approach, result, comparison, mechanism, implication, or limitation.
- The topic sentence states the job.
- Each sentence has a cause, contrast, consequence, refinement, or example relation to the previous one.

## Reviewer Gate

- Methodology objections are separated from domain objections.
- Skeptical-reviewer concerns are not erased by majority tone.
- Every high-risk objection becomes an experiment, citation check, text edit, or narrower claim.

## Packaging Gate

- Keep raw transcripts, subtitle tables, upstream examples, cloned repos, and acquisition artifacts out of the published skill unless the user explicitly requests an evidence package.
