# Quality Gates

Apply only gates relevant to the selected route.

## Evidence Gate

- Every major claim maps to supplied, reported, reproduced, inferred, proposed, or missing evidence.
- Numbers, datasets, applications, mechanisms, and novelty claims are traceable.
- A plan or expected result is never written as an observed result.

## Process Completeness Gate

- The response identifies the current `S0`–`S8` stage and the exact user-authorized checkpoint.
- Scope, intake, route lock, evidence inventory, and integrity/fairness checks are either passed or explicitly marked `hold`, `blocked`, or `not_applicable` with a reason.
- `Executed in this response` and `Not executed` are both present; deterministic file checks are not described as scientific execution.
- The response names one observable next checkpoint and does not silently continue into a downstream route.

## Provenance And Citation Gate

- Reused components have source, license/permission, original role, actual change, and attribution.
- Citations use a DOI, arXiv ID, repository record, or stable URL when precision matters.
- Unverified citations remain `[unverified]`; do not invent support.

## Fair Comparison Gate

- Comparators address the same task under compatible data, split, metric, and evaluation protocol.
- Tuning and compute budgets are disclosed and reasonably matched.
- Reported and reproduced numbers are not mixed silently.
- Material negative results, failed runs, and resource costs are not hidden.

## Reproducibility Gate

- Record code/data version, environment, randomization, preprocessing, and run count as applicable.
- Use repeated runs or uncertainty estimates when the claim depends on unstable differences.
- An open repository is evidence of availability, not proof of correctness.

## Claim-Driven Experiment Gate

- Every retained experiment block names the claim it can support or weaken.
- The primary test, comparator/control, decisive ablation, and failure/robustness check are explicit.
- Success criteria, failure interpretation, run order, cost, seeds/uncertainty, and paper placement are recorded before results are used.
- Evaluation uses the task's actual ground truth and the same protocol for every comparator; failed, missing, and unstable runs remain visible.
- Results are labeled planned, running, observed, failed, or reproduced; observed results do not silently become causal explanations.

## Source-Fidelity Gate

- Each paragraph has one job and no unsupported specificity.
- Terminology and notation stay consistent across sections.
- Polishing preserves scientific meaning and uncertainty.

## Manuscript Control Gate

- Full prose or structural rewriting has an alignment record, terminology lock,
  lead evidence, and a `proceed` decision, or it stops at `confirm`/`hold`.
- Results are classified by function and allocated across main text, captions,
  Methods/source data, and SI without hiding conclusion-changing evidence.
- Every requested addition passes a deletion or replacement check before it is
  appended to a paragraph.
- Multi-round manuscripts reconcile numbers and claims against the paper's own
  design, tables, figures, and authoritative artifacts before style cleanup.
- Consistency findings are inspected and verified individually; the checker is
  not treated as an automatic correction engine.

## Review Independence And Revision Gate

- Review lenses use the same immutable supplied packet and are defined before
  their findings; reports are frozen before synthesis.
- Issues carry stable IDs, severity, claim/evidence pointers, why the issue
  matters, and a resolution test.
- Revision actions, work status, verification evidence, and package readiness
  remain separate. `VERIFIED_DONE` requires an inspectable artifact.
- Same-context multi-lens output is not described as mutually blind review.

## Reviewer Gate

- Methodology, domain, skeptical, editorial, and integrity findings remain distinguishable.
- Every critical issue has a concrete resolution path or a narrower claim.
- Response language is factual and professional; politeness never overrides evidence.

## Output Contract Gate

- The compact route line is first.
- `## Process Status` immediately follows `## Route` and contains the required fields from the process contract.
- Mandatory route headings appear in the documented order.
- No meta-analysis or extra heading precedes a requested behavior simulation.
- The answer stops at the user's checkpoint.

## Packaging Gate

- Keep credentials, raw transcripts, acquisition artifacts, cloned repositories, evaluation logs, and generated caches out of a released skill package.
- Do not claim API/self-play/judge success from a deterministic file check.
