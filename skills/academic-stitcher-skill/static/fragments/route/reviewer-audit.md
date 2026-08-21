# Route: reviewer-audit

Use for pre-submission review, rejection-risk analysis, reviewer-response planning, rebuttal, advisor review, or defense-question preparation.

## Independent Lenses

1. **Methodology** — protocol, controls, metrics, statistics, ablations, reproducibility, cost.
2. **Domain** — relevance, comparator currency, terminology, prior-work positioning, venue fit.
3. **Skeptical** — hidden assumptions, alternative explanations, overclaims, failure cases.
4. **Integrity** — citations, data provenance, reused code/modules, authorship, material negative evidence.

Build one immutable packet from the supplied artifact, verified anchors, scope
boundary, and missing-file inventory. Define the lenses before drafting findings,
keep each lens's concerns out of the others, and freeze the reports before
synthesis. Preserve a minority concern until evidence resolves it or the claim
is narrowed. If the environment cannot isolate contexts, label the output a
same-context multi-lens audit rather than mutually blind peer review.

## Audit Mode

For each issue, record a stable local ID, severity, exact location or
`not assessable`, `claim_pointer`, `evidence_pointer`, why it matters, a
resolution test, and the smallest corrective action. Do not invent a concern to
fill a quota.

## Response Mode

When comments or defense questions are supplied, build:

| Comment/question | Interpretation | Decision | Action | Evidence | Manuscript location |
| --- | --- | --- | --- | --- | --- |

In response mode, also track `work_status`, `verification_evidence`, and
`package_readiness`. A drafted reply is not proof that the manuscript,
experiment, or figure changed. Use `VERIFIED_DONE` only for an inspectable
artifact; otherwise use an unverified or pending status and stop finalization if
the missing artifact is central.

Accept valid criticism, correct errors, and explain changes precisely. If a request conflicts with evidence, ethics, feasibility, or scope, respond professionally with data or a bounded alternative. Do not add irrelevant citations, hide unavailable code, or claim a change was made before it exists.

## Contract

Use the `reviewer-audit` headings from `static/core/output-format.md`, including the process card. Put the response matrix inside `Revision Roadmap` when operating in response mode.

## Boundary

- Audit the supplied artifact and evidence; do not certify acceptance or reproduce an absent experiment.
- Keep methodology, domain, skeptical, editorial, and integrity findings separate until synthesis.
- Do not claim a revision, new result, citation, or code change exists before it is observable.
