# Shared Glossary

> Working definitions for the core story/writing/experiment skill and five specialist skills. These are operational terms, not institutional rules or universal claims.

## Research story and manuscript architecture

- **Story spine**: a bounded argument linking pressure, inherited baseline, failure mode, gap, design principle, mechanism, prediction, evidence, and boundary.
- **Central claim**: the smallest sentence the paper must support; it is not a list of modules or a headline metric.
- **Failure mode**: the concrete limitation of the inherited approach that motivates a change and predicts an observable difference.
- **Design principle**: the reason a change should address the failure mode; it must be more specific than “add a stronger module”.
- **Claim–evidence–boundary map**: a ledger connecting each claim to its evidence state and the conditions where it stops applying.
- **Research story**: an evidence-preserving organization of a research argument, not post-hoc motivation, hidden reuse, or invented results.
- **Claim ladder**: one dominant claim, optional supporting claims, and anti-claims that the experiment plan must distinguish and test.
- **Claim–evidence–experiment matrix**: a ledger connecting each claim to its evidence state, primary test, comparator/control, decisive ablation, failure check, uncertainty, and paper placement.

## Research direction and foundations

- **Research direction**: a problem domain that can sustain questions, resources, experiments, and deliverables; it is broader than a single title or topic.
- **Foundation map**: a gap map covering general theory, domain theory, experimental technique, data, equipment, implementation, and reproducibility.
- **Activity signal**: recent literature activity or an equivalent signal that a problem remains active. It is not sufficient by itself to prove feasibility.
- **Support signal**: available supervision, handoff, code, data, infrastructure, or community support that can reduce execution risk.
- **Resource hard gate**: a blocking check for rights, data access, versions, equipment, compute, code, preprocessing, or a minimum runnable condition.
- **Minimum pilot**: the smallest time-boxed task that can test the map, resources, and reproducibility before a long-term commitment.

## Paper evidence and architecture

- **Reading purpose**: the decision the current paper pass must support, such as reproduction, comparison, component extraction, or contribution review.
- **Four-entry evidence route**: using abstract, introduction, method/framework, and experiments/ablations for different evidence jobs rather than writing a shorter abstract.
- **Baseline**: the comparison object that carries the current main task under a stated claim boundary.
- **A/B/C architecture**: a relative decomposition in which A is the current baseline and B/C are changes or modules to explain, replace, remove, or validate.
- **Variable granularity**: the fact that A/B/C roles can move when the claim, comparison object, or reuse boundary changes.
- **Historical attribution**: the record of who introduced, implemented, or validated a component; changing a label does not erase that history.
- **Contribution boundary**: the smallest set of independently supported changes that can be described as a candidate contribution.

## Module transfer and validation

- **Three-domain search**: separate candidate pools for general, in-domain, and adjacent-domain mechanisms.
- **Dataflow**: the full path from task input to output, including semantics, shapes, timing, preprocessing, training signals, deployment inputs, and resource contracts.
- **B-prime/C-prime**: a transferred component with explicit interface or mechanism changes and new validation; renaming or a score increase is insufficient.
- **Train/deploy contract**: the information available during training versus deployment; a training-only label cannot silently become an inference dependency.
- **Single-module control**: an isolated comparison that identifies the effect and cost of one change before composition.
- **Ablation**: a comparison that removes or changes a component to test causality, not just a best-result table.
- **Decision gate**: a predeclared stop/go condition that determines whether the next experiment stage is justified.
- **Failure reflux**: the explicit update from a failed or inconclusive run back to a narrower claim, removed module, revised mechanism, or missing-input checkpoint.
- **Run state**: the operational status of a run, such as planned, running, observed, failed, or reproduced; it is separate from the evidence state of a claim.

## Evidence, delivery, and stop conditions

- **Evidence chain**: a reviewable connection among claims, materials, code, data, controls, ablations, limitations, and versions.
- **Rights/access check**: an explicit record of permission, license, privacy, access, or redistribution constraints.
- **Version ledger**: the exact code, data, preprocessing, environment, and configuration used for a claim.
- **Innovation axis**: new problem framing, mechanism, or independently supported claim.
- **Workload axis**: implementable, recorded, and reviewable deliverables such as reproduction, engineering migration, experiments, negative results, and chapters.
- **Stop condition**: a predeclared condition that triggers continuation, a time-boxed pilot, narrowing, redesign, or stopping.
- **Pending**: the correct state when required evidence or a current formal rule has not been checked. It is not permission to infer a result.
- **Ground-truth protocol**: the recorded source of target labels or reference values and the same evaluation procedure applied to every comparator.

## Operating reminders

1. Do not equate public access with unrestricted use.
2. Do not equate open code with successful reproduction.
3. Do not equate module count, paper count, acceptance, or metric gains with innovation or workload.
4. Do not turn an unverified experience-based threshold into a current institutional rule.
5. Keep the claim, evidence state, cost, limitation, and next action visible in every output.
