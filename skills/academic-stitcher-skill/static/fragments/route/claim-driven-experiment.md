# Route: claim-driven-experiment

Use when the user explicitly asks to turn a frozen research claim or story into an experiment plan, ablation/evaluation matrix, fair comparison protocol, run order, compute budget, decision gates, or a result-to-claim update loop.

This route designs and audits the evidence bridge. It does not pretend to have run code, deploy remote jobs, or observe results. Implementation and deployment belong to the project execution environment; this route returns the contract those actions must satisfy.

## Procedure

## Claim Ladder

1. **Freeze the claim ladder**
   - State one dominant mechanism-level claim, optional supporting claims, and the anti-claims that must be ruled out.
   - Limit the primary story to the smallest claim set that the available budget can defend.
   - For each claim, state the minimum convincing evidence and the evidence state: `supplied`, `reported`, `reproduced`, `inferred`, `proposed`, or `missing`.

## Claim-Evidence-Experiment Matrix

2. **Build the claim–evidence–experiment matrix**
   Record at least:

   | Claim | State | Primary test | Comparator/control | Decisive ablation | Robustness/failure check | Metric/uncertainty | Stop/go rule |
   | --- | --- | --- | --- | --- | --- | --- | --- |

   - A run must name the belief it can change; remove benchmark decoration that cannot affect a decision.
   - Use the task's actual ground truth and one compatible protocol for every comparator.
   - Keep reported numbers separate from locally reproduced numbers.

## Experiment Blocks

3. **Create compact experiment blocks**
   Use only the blocks needed by the claim:
   - **M0 Sanity** — data split, preprocessing, metric correctness, leakage check, and a fast toy/overfit check.
   - **M1 Baseline** — reproduce the strongest fair baseline before interpreting a delta.
   - **M2 Main** — test the proposed method on the primary setting and record cost as well as the decisive metric.
   - **M3 Decision** — isolate the claimed component, test simplicity or alternative explanations, and run the ablation that could falsify the mechanism.
   - **M4 Polish** — robustness, uncertainty, qualitative failures, and appendix checks only after the central gate passes.

   For every block, specify the claim tested, why it exists, dataset/split/task, systems and controls, metrics, setup and seeds, success criterion, failure interpretation, expected artifact, priority, and paper placement.

## Run Order And Decision Gates

4. **Order the runs and gates**
   - Put sanity before expensive runs, baseline before main, and decisive ablations before optional polish.
   - Separate `MUST-RUN` evidence from `NICE-TO-HAVE` evidence.
   - Record cost, turnaround, dependencies, stop/go condition, and the smallest recovery action for each milestone.
   - Never let a later positive result repair an earlier failed fairness, leakage, provenance, or baseline gate.

## Analysis And Failure Reflux

5. **Predeclare analysis and failure reflux**
   - Distinguish `planned`, `running`, `observed`, `failed`, and `reproduced` run states from the evidence states of claims.
   - State seed count, uncertainty summary, effect size or practical threshold, outlier handling, and the source of ground truth before reading the result.
   - Preserve failed, unstable, and inconclusive runs. If a claim fails, narrow the claim, remove the module, revise the mechanism, or return to the missing input; do not change the gap after seeing the result.
   - An observed metric difference supports an empirical statement. A causal/mechanistic statement still needs the relevant control, ablation, or alternative-explanation test.

## Paper Placement

6. **Place the evidence in the paper**
   - Main paper: the anchor result and the minimum controls needed for the central claim.
   - Appendix: useful robustness or implementation detail that does not carry the main inference.
   - Cut or defer: attractive but non-decisive runs that consume budget without changing a reviewer decision.
   - Map each retained block to a figure/table and to the exact sentence it supports; do not write a result paragraph before its evidence state is known.

## Handoffs

- If the pressure, failure mode, gap, or central claim is not frozen, use `story-architecture` first.
- If the baseline or candidate modules are not traceable, use `stitch-plan`, `purpose-driven-paper-decomposition`, or `variable-granularity-abc-research-architecture` first.
- If the transfer contract is unresolved, use `three-domain-module-search-dataflow-adaptation` before designing the main comparison.
- After real results exist, use `reviewer-audit` to test alternative explanations and `section-draft` only at the requested writing checkpoint.
- For thesis or proposal workload, add `innovation-workload-dual-axis` after the claim and evidence gates are frozen.

## Contract

Use the `claim-driven-experiment` headings from `static/core/output-format.md` exactly. The matrix must contain at least one primary test and one falsifying or narrowing check for every central claim. `Analysis And Failure Reflux` must distinguish planned evidence from observed evidence and state what happens if the central gate fails.

## Boundary

- Do not fabricate results, seeds, confidence, statistical significance, or successful runs.
- Do not select only favorable seeds, delete failed runs, substitute another model's output for ground truth, or weaken a comparator to protect the story.
- Do not call a score difference a mechanism proof without the relevant control or ablation.
- Do not use this route for generic software QA, remote deployment instructions, or sentence-level polishing.
