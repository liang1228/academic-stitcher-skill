# Academic Writing Suite

This reference compresses external academic-writing skill patterns into one Codex-native route. It is distilled structure, not copied upstream content. It keeps the repository core-only: no upstream examples, raw transcripts, tests, scripts, or local acquisition artifacts.

## Source-Informed Design

- `Master-cai/Research-Paper-Writing-Skills`: section-by-section drafting, paragraph-flow checks, claim-evidence alignment, and reviewer-facing presentation.
- `Yuan1z0825/nature-skills`: dynamic routing by paper type, section, language, journal level, Nature-style drafting/polishing, terminology control, and evidence-first claim discipline.
- `Imbad0202/academic-research-skills-codex`: Codex suite structure: a root router, workflow modes, inline role passes, checkpoints, reviewer independence, and quality gates.

## Route Selection

Detect and state these axes before drafting or polishing:

| Axis | Values To Consider |
| --- | --- |
| Goal | thesis pass, SCI paper, conference paper, Nature-style manuscript, rebuttal, proposal, advisor memo |
| Route | Stitch Plan, Section Draft, Nature-Style Polish, Reviewer Audit, Full Pipeline |
| Paper type | research, methods, algorithmic, hypothesis, review, thesis/proposal |
| Section | title, abstract, introduction, related work, method, experiments/results, discussion, conclusion |
| Language | Chinese notes, mixed Chinese-English notes, English draft |
| Evidence state | no data, reproduced baseline, preliminary table, full result set, draft manuscript |
| Checkpoint | intake only, outline, draft, audit, revision roadmap, final check |

If the user supplies only a broad topic, start with scoping questions and a paper matrix instead of drafting a full outline. If the user already has results or a draft, route directly to section architecture, polishing, or reviewer audit.

## Inline Role Passes

Run these as internal passes. Do not claim that separate agents were spawned unless the user explicitly requested subagents.

1. **Intake**: identify target, constraints, artifacts, missing evidence, and misconduct boundaries.
2. **Structure Architect**: write the one-sentence argument: `In [problem], we show [advance] using [approach], supported by [evidence], within [boundary].`
3. **Evidence Auditor**: build the paper matrix, terminology ledger, and claim-evidence-boundary map.
4. **Draft Writer**: draft paragraphs from evidence outward. One paragraph has one job.
5. **Reviewer Panel**: separately check methodology, domain fit, and skeptical objections before synthesis.
6. **Revision Coach**: turn unresolved risks into experiments, citations, text edits, or a narrower claim.

For a full pipeline, stop visibly at the requested checkpoint. Never silently continue past an intake, outline, integrity gate, review gate, or final check when the user asked for that boundary.

## Section Moves

### Abstract

Use a compact sequence: field/problem -> gap -> approach -> strongest evidence -> contribution and boundary. Do not invent numbers, datasets, or novelty. If results are missing, mark the result sentence as a placeholder.

### Introduction

Default funnel: field pressure -> task or setting -> prior attempts -> unresolved technical challenge -> proposed move -> why it should work -> contribution and evidence preview.

For method-heavy papers, pick one framing:

- task then application;
- application first;
- general task to specific setting;
- open with technical challenge;
- new task with decomposed challenges;
- pipeline or module contribution.

Avoid presenting a naive baseline only so the paper can look improved. Frame the real bottleneck, the mechanism, and the evidence that will test it.

### Related Work

Organize by argumentative role:

1. task lineage;
2. baseline or method family;
3. borrowed module or concept lineage;
4. unresolved gap.

Synthesize groups instead of listing papers one by one. Every paragraph should help the reader understand why the current delta is necessary.

### Method

Use this order:

1. problem formulation and notation;
2. baseline recap only as much as needed;
3. overall pipeline;
4. proposed delta with input/output, placement, and mechanism;
5. objective, training, inference, or algorithmic procedure;
6. complexity, implementation detail, and reproducibility boundary.

### Experiments And Results

Bind each claim to an experiment:

| Claim Type | Minimum Evidence |
| --- | --- |
| Better performance | fair main table with stated baseline rule |
| Module usefulness | ablation removing or replacing the module |
| Robustness | split, domain, noise, sensitivity, or stress test |
| Efficiency | parameter, FLOP, memory, or runtime comparison |
| Mechanism | qualitative case, subgroup metric, failure analysis, or visualization |

Separate reported numbers from reproduced numbers. If examples are curated, call them curated.

### Discussion And Conclusion

State what was shown, why it matters, where it is limited, and what remains unresolved. Do not introduce unsupported new contributions in the conclusion.

## Nature-Style Polish

Diagnose before editing sentences. Fix in this order:

`paper type -> section job -> paragraph logic -> claim/evidence/boundary -> sentence polish`

Use these local rules:

- Build a terminology ledger on first contact: model names, datasets, metrics, abbreviations, notation, and canonical translations.
- Calibrate verbs to evidence strength: strong direct evidence can support "show" or "demonstrate"; indirect trends need "suggest" or "indicate"; untested mechanisms need "may" or "could".
- Remove or bound universal novelty claims such as "first", "unique", "unprecedented", "complete", "always", and "never" unless the evidence and literature audit really support them.
- For Chinese-to-English work, give polished English first, then short Chinese notes explaining major structural choices.
- Do not sentence-polish a structurally wrong section as if style alone would fix the paper.

## Reviewer Audit

Run independent checks before editorial synthesis:

| Reviewer Lens | Questions |
| --- | --- |
| Methodology | Is the design testable, controlled, reproducible, and fairly compared? |
| Domain | Does the problem matter in the target field, and are the baselines current enough? |
| Skeptical reviewer | What would make a reviewer reject this despite polished writing? |
| Integrity | Are citations, data, authorship, reused code, and negative evidence disclosed? |

Preserve dissenting or skeptical findings until they are resolved by evidence, a revision, or an explicitly narrower claim.

## Quality Gates

Before final output, report only gates that materially affect the request:

1. **Scope gate**: target, venue, deadline, and workload are realistic.
2. **Evidence gate**: every major claim has evidence, an inference label, or a placeholder.
3. **Citation gate**: reused ideas, modules, datasets, and numbers have attribution requirements.
4. **Fairness gate**: baselines, tuning budgets, ablations, and qualitative examples are not cherry-picked or hidden.
5. **Flow gate**: each paragraph has one job and connects to the paper's one-sentence argument.
6. **Reviewer gate**: methodology, domain, and skeptical objections are listed with actions.
7. **Packaging gate**: raw transcripts, upstream examples, acquisition tables, and other intermediate artifacts stay out of the published skill or user-facing manuscript unless explicitly needed.

## Output Patterns

For section drafting:

```markdown
## Writing Route
- Paper type:
- Section:
- Language:
- Target:
- Evidence state:

## Section Outline
- ...

## Draft
...

## Claim-Evidence Map
| Claim | Evidence | Status | Boundary |
| --- | --- | --- | --- |

## Missing Inputs
- ...

## Quality Gates
- ...
```

For review/audit:

```markdown
## Independent Reviewer: Methodology
...

## Independent Reviewer: Domain
...

## Independent Reviewer: Skeptical
...

## Editorial Synthesis
...

## Revision Roadmap
...
```
