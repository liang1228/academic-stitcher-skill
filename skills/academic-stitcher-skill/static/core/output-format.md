# Output Contracts

The first non-empty line is:

`Route: <route>; paper_type=<paper_type>; section=<section or none>; language=<language>`

Use the smallest matching contract. Do not append unrelated generic sections.

## stitch-plan

1. `## Route`
2. `## Paper Stitching Map`
3. `## Claim-Evidence Map`
4. `## Next Work Packages`
5. `## Quality Gates`
6. `## Missing Inputs`

## section-draft

1. `## Route`
2. `## Section Outline`
3. `## Source Trace`
4. `## Draft`
5. `## Claim-Evidence Map`
6. `## Missing Inputs`

## nature-polish

1. `## Route`
2. `## Diagnosis`
3. `## Revised Draft`
4. `## Change Log`
5. `## Source And Claim Risks`
6. `## Missing Inputs`

## story-architecture

1. `## Route`
2. `## Story Spine`
3. `## Problem, Failure Mode, And Gap`
4. `## Design Principle And Mechanism Chain`
5. `## Claim-Evidence-Boundary Map`
6. `## Section, Figure, And Experiment Order`
7. `## Reviewer Stress Test`
8. `## Missing Inputs`

## reviewer-audit

1. `## Independent Reviewer: Methodology`
2. `## Independent Reviewer: Domain`
3. `## Independent Reviewer: Skeptical`
4. `## Independent Reviewer: Integrity`
5. `## Editorial Synthesis`
6. `## Revision Roadmap`

## full-pipeline

1. `## Route`
2. `## Current Stage`
3. `## Evidence Ledger`
4. `## Work Plan`
5. `## Quality Gates`
6. `## Next Checkpoint`

## ctx2skill-audit

1. `## Ctx2Skill Audit`
2. `## Failure Taxonomy`
3. `## Replay Gate`

When `ctx2skill-audit` is asked to simulate another route, use the simulated route's compact line and headings first. Add `## Behavior Notes` only afterward and only if the prompt requests an explanation.

If a field lacks evidence, write a bounded placeholder such as `[missing: matched baseline result]` instead of completing it imaginatively.
