# Academic Research Planning Skills — Method Digest

> A concise reader guide to the core story/writing/experiment workflow and five specialist workflows. It is a method reference, not a policy, publication guarantee, or experimental result.

The common problem is not a lack of papers or ideas. It is the failure to convert a research idea into a bounded, reproducible, and explainable sequence of decisions. The core skill organizes the story, claim-to-experiment bridge, and manuscript lifecycle; the five specialist skills test whether the direction can carry the work, read papers as evidence-bearing components, freeze inherited and new boundaries, adapt modules along real contracts, and separate innovation from delivery workload.

## 0. Build the story from evidence, not after the result

For a hybrid paper, use one bounded spine:

`pressure -> inherited baseline -> failure mode -> gap -> design principle -> mechanism -> prediction -> evidence -> boundary`

Each transition needs a source, artifact, experiment, or explicit `missing`/`proposed` state. The story route maps that spine to Introduction, Related Work, Method, Experiments, Discussion, and Conclusion, then stress-tests alternative explanations, omitted negative evidence, and post-hoc motivation. It turns “讲好故事” into argument architecture without turning it into fabricated significance.

## 1. Close the claim–experiment loop

Once the central story is accepted, do not jump from a mechanism sentence to a benchmark wishlist. Use `claim-driven-experiment` to freeze one dominant claim, supporting/anti-claims, minimum convincing evidence, and a matrix linking each claim to a primary test, fair comparator, decisive ablation, robustness or failure check, uncertainty, stop/go rule, and paper placement.

Use the compact order `sanity -> baseline -> main -> decision -> polish`. Keep `planned`, `running`, `observed`, `failed`, and `reproduced` as run states, separate from `supplied`, `reported`, `reproduced`, `inferred`, `proposed`, and `missing` evidence states. If a central gate fails, preserve the result and reflux it into a narrower claim, a removed module, a revised mechanism, or a missing-input checkpoint. Never change the gap after seeing the result just to keep the original story.

## 2. Make the research entry a feasible commitment

A direction should be evaluated with separate activity, support, and resource signals. A busy literature area does not compensate for missing theory, equipment, data access, implementation capacity, or handoff. A foundation map should list the gaps by type and identify which one blocks the first runnable task.

Use a minimum pilot when the evidence is incomplete. The pilot must have a deadline, a runnable task, a success definition, and an exit decision. A missing review can be replaced temporarily by other evidence, but it must remain a gap rather than being silently treated as proof.

## 3. Read papers according to the decision they must support

A paper pass should begin with a purpose: reproduce, compare, extract components, check attribution, or prepare a design. Abstract and introduction help locate the task and claims; methods and figures expose components, interfaces, dependencies, and dataflow; experiments and ablations test whether a claimed component was actually enabled, removed, or isolated; code, appendices, preprocessing, splits, and versions resolve implementation conflicts.

The output is not a shorter abstract. It is a component-and-evidence table with inputs, outputs, states, conflicts, and pending checks.

## 4. Let A/B/C move with the claim boundary

A, B, and C are not permanent identities. One complete system can become another study's baseline, while a small preprocessing change can be the only new unit. The current claim, comparison object, inclusion boundary, rights, version, actual code changes, and independent validation must be frozen before contribution language is written.

If code, controls, ablations, or attribution evidence are missing, the component can remain a structural hypothesis. It must not be described as an established contribution merely because it appears in a diagram or improves a metric.

## 5. Transfer modules through contracts, not names

Search candidate mechanisms in general, in-domain, and adjacent-domain pools. Then place each candidate on the actual input-to-output path and record semantics, shapes, timing, preprocessing, training-only signals, deployment inputs, dependencies, rights, and cost.

A B-prime or C-prime label requires an explicit adaptation and new validation. A shape match, a similar paper title, or a better aggregate score is not enough. Start with a reversible single-module control, disclose side effects, and reject the transfer when it changes the task or depends on unavailable information.

## 6. Separate innovation from workload

Innovation asks what new problem, mechanism, or independently supported claim is present. Workload asks what was implemented, reproduced, migrated, measured, documented, and made reviewable. One experiment can support both axes, but its role must be recorded separately.

Paper count, module count, acceptance, or a verbal threshold cannot substitute for an evidence matrix. When a current institutional requirement is missing, keep the rule state pending, identify the document to check, and continue only with conditional planning.

## Common traps

1. **A project larger than its resources**: shrink the question or time-box a pilot before adding more components.
2. **Linear reading without evidence structure**: route each paper section to a specific decision and retain conflicts.
3. **Renaming or stacking as contribution**: require actual mechanism/interface change and isolated validation.
4. **Public data or open code treated as automatically usable**: verify rights, versions, access, preprocessing, and reproducibility.
5. **Counts replacing judgment**: split innovation, workload, overlap, and delivery evidence into separate ledgers.
6. **Experiment wishlist replacing inference**: remove runs that cannot change a claim decision; add the control or failure test that can.
7. **Failed runs disappearing from the story**: preserve them and state whether they narrow, redesign, or stop the claim.

## Three rules to keep

1. Prove that the work can run under the available constraints before arguing that it is novel.
2. Treat A/B/C as a claim-relative evidence boundary, not a relabeling shortcut.
3. Turn every central claim into a testable evidence contract before drafting result prose.
4. Keep innovation, workload, evidence state, and current formal requirements in separate ledgers.
