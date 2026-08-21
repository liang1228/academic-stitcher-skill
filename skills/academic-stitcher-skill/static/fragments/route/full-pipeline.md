# Route: full-pipeline

Use only when the user explicitly asks for end-to-end research-to-paper support. This route orchestrates other routes; it does not require every stage in one response.

Before Stage 1, pass the common `S0 scope` through `S4 integrity-gate` stages. Each stage below must leave an observable artifact and a pass/hold decision; a later stage cannot be reported as complete when an earlier gate is held.

## Stages

1. Intake and current-rule constraints.
2. Comparable-paper matrix and provenance inventory.
3. Inheritance/failure/delta/mechanism architecture.
4. Feasibility, integrity, and fair-evidence gate.
5. Experiment and analysis plan.
6. Section architecture and source trace.
7. Draft or polish at the authorized checkpoint.
8. Independent reviewer audit and response plan.
9. Final evidence, formatting, disclosure, and packaging checks.

## Gate Rules

- A later stage cannot repair a failed evidence or integrity gate by rhetoric.
- Venue and institutional rules must be current and explicitly sourced.
- Baseline selection must be comparable, not merely favorable.
- Drafting begins only when the required evidence state is clear.
- Formatting quality matters but never outranks scientific correctness.
- Stop after the user's named checkpoint. If none is named, complete the current stage and propose the next gate.

## Contract

Use the `full-pipeline` headings from `static/core/output-format.md`, including the process card. `Current Stage` must say what has and has not been executed. `Next Checkpoint` must require an observable artifact or decision.

## Boundary

- This route coordinates stages; it does not make unrun stages complete by producing a plan.
- A held evidence, integrity, provenance, or fairness gate blocks downstream drafting and submission language.
- Stop at the named user checkpoint and expose the next observable artifact.
