# Route: ctx2skill-audit

Use to evaluate, distill, regression-test, or improve a skill package. The skill repository is the artifact under test, not source material for a paper.

## Modes

- **Deterministic audit** — inspect files, manifest paths, frontmatter, scripts, banned artifacts, and static route fixtures.
- **Behavior simulation** — answer a sample prompt exactly as the target route should answer it.
- **Model evaluation** — run challenger/reasoner/judge/replay only when the required framework and model API are actually available.

## Procedure

1. Build a context pack from `SKILL.md`, `manifest.yaml`, core rules, matching fragments, references, and relevant scripts.
2. Generate hard tasks that require skill-specific routing or contracts, plus easy regressions and sibling-route lures.
3. Define binary rubrics for trigger, route, evidence state, compliance, output headings, and progressive disclosure.
4. Keep evaluators blind to the intended fix when possible.
5. Classify failures as routing, content, output-contract, constraint, reasoning, task-understanding, or evaluation-integrity failures.
6. Make the smallest reusable update; do not patch only the expected answer.
7. Re-run hard tasks, easy regressions, package validation, and artifact scans.

## Behavior Simulation Contract

When asked how this skill should answer a sample request:

1. output the simulated route's compact detection line first;
2. follow that route's exact heading sequence;
3. put any compliance stop inside the target contract rather than a preceding meta heading;
4. add `## Behavior Notes` only after the simulated response and only when requested.

## Evidence Boundary

Do not claim full self-play, judge success, or replay selection unless model calls and outputs exist. Process exit code alone is not a behavioral pass.

## Contract

For audit mode, use the `ctx2skill-audit` headings from `static/core/output-format.md`. For behavior simulation, use the simulated route contract instead.
