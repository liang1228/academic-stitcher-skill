# Paper Type: algorithmic

Use for models, modules, pipelines, optimization methods, and AI/ML systems.

## Reader Question

Does the system improve the target outcome under a fair protocol, and does the evidence isolate why?

## Required Architecture

`task -> baseline failure -> changed component -> predicted mechanism -> matched comparison -> attribution -> boundary`

## Baseline Gate

- Same task, data split, metric definition, and evaluation protocol where possible.
- Code/data availability, license, environment, and resource feasibility checked before adoption.
- Include strong and relevant comparators, not only easy-to-beat systems.
- If a published result cannot be reproduced, report both the published and reproduced values with conditions; use the reproducible value as the experimental starting point only with the discrepancy visible.

## Module Change Ledger

For every claimed component, record source, original role, interface, actual modification, expected mechanism, and the experiment that can falsify the claim. Renaming or wrapping an unchanged component is not a contribution.

## Experiment Gate

- Main comparisons use matched data, metrics, preprocessing, and disclosed budgets.
- Tuning policies are comparable; do not optimize the proposed method while leaving baselines under-tuned.
- Ablations test one claim at a time. If removing a module improves performance, report the result and revise or remove the claim; do not merge components to conceal the failure.
- Use repeated runs, uncertainty, robustness, sensitivity, complexity, and failure cases when relevant.
- Label curated examples and material negative results.

## Weak Or Mixed Results

Narrow the claim, diagnose conditions, change the design, or stop. A real efficiency, robustness, or interpretability contribution may be reported only when directly measured. Do not relabel an unmeasured benefit or hide required runtime, resource, or counterevidence.
