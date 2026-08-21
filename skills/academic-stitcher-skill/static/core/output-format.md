# Output Contracts

The first non-empty line is:

`Route: <route>; paper_type=<paper_type>; section=<section or none>; language=<language>`

Use the smallest matching contract. Do not append unrelated generic sections.

Every contract includes `## Route` followed immediately by `## Process Status`. The process status block is mandatory even for a small request:

```text
## Process Status
- Stage: <S0-S8 name>
- Authorized checkpoint: <exact deliverable allowed now>
- Inputs and evidence coverage: <states and coverage>
- Executed in this response: <observable actions/artifacts>
- Not executed: <unrun work and later stages>
- Gate: <pass | hold | blocked | not_applicable + reason>
- Next checkpoint: <one observable artifact or decision>
```

## stitch-plan

1. `## Route`
2. `## Process Status`
3. `## Paper Stitching Map`
4. `## Claim-Evidence Map`
5. `## Next Work Packages`
6. `## Quality Gates`
7. `## Missing Inputs`

## section-draft

1. `## Route`
2. `## Process Status`
3. `## Section Outline`
4. `## Source Trace`
5. `## Draft`
6. `## Claim-Evidence Map`
7. `## Missing Inputs`

For a full or structurally ambiguous section, put the alignment checkpoint and
its `proceed`, `confirm`, or `hold` decision in `## Section Outline`. Do not emit
full `## Draft` prose while the decision is `confirm` or `hold`.

## nature-polish

1. `## Route`
2. `## Process Status`
3. `## Diagnosis`
4. `## Revised Draft`
5. `## Change Log`
6. `## Source And Claim Risks`
7. `## Missing Inputs`

For multi-round or multi-section polishing, include consistency-sweep findings
and verification state in `## Diagnosis` or `## Change Log`.

## story-architecture

1. `## Route`
2. `## Process Status`
3. `## Story Spine`
4. `## Problem, Failure Mode, And Gap`
5. `## Design Principle And Mechanism Chain`
6. `## Claim-Evidence-Boundary Map`
7. `## Section, Figure, And Experiment Order`
8. `## Reviewer Stress Test`
9. `## Missing Inputs`

## claim-driven-experiment

1. `## Route`
2. `## Process Status`
3. `## Claim Ladder`
4. `## Claim-Evidence-Experiment Matrix`
5. `## Experiment Blocks`
6. `## Run Order And Decision Gates`
7. `## Analysis And Failure Reflux`
8. `## Paper Placement`
9. `## Missing Inputs`

## reviewer-audit

1. `## Route`
2. `## Process Status`
3. `## Independent Reviewer: Methodology`
4. `## Independent Reviewer: Domain`
5. `## Independent Reviewer: Skeptical`
6. `## Independent Reviewer: Integrity`
7. `## Editorial Synthesis`
8. `## Revision Roadmap`

Each concern in the reviewer sections or roadmap should carry a stable local ID,
severity, claim/evidence pointer, resolution test, action, work status, and
verification/readiness state when response mode is requested.

## full-pipeline

1. `## Route`
2. `## Process Status`
3. `## Current Stage`
4. `## Evidence Ledger`
5. `## Work Plan`
6. `## Quality Gates`
7. `## Next Checkpoint`

## ctx2skill-audit

1. `## Route`
2. `## Process Status`
3. `## Ctx2Skill Audit`
4. `## Failure Taxonomy`
5. `## Replay Gate`

When `ctx2skill-audit` is asked to simulate another route, use the simulated route's compact line and headings first. Add `## Behavior Notes` only afterward and only if the prompt requests an explanation.

If a field lacks evidence, write a bounded placeholder such as `[missing: matched baseline result]` instead of completing it imaginatively.
