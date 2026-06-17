# Ctx2Skill Evaluation Playbook

Use this reference when maintaining `academic-stitcher-skill` with a Ctx2Skill-style loop. The goal is to expose gaps in the skill, then make the smallest reusable update that improves future behavior without bloating the default context.

## Table Of Contents

- [Adapted Loop](#adapted-loop)
- [Context Pack](#context-pack)
- [Challenger Tasks](#challenger-tasks)
- [Rubric Dimensions](#rubric-dimensions)
- [Failure Taxonomy](#failure-taxonomy)
- [Update Rules](#update-rules)
- [Replay Gate](#replay-gate)
- [Observed Replay Seed](#observed-replay-seed)

## Adapted Loop

1. **Challenger**: create hard, context-grounded tasks that require this skill's router, evidence rules, grey-vocabulary conversion, and reviewer gates.
2. **Reasoner**: answer the tasks using only the current skill and the task context.
3. **Judge**: score each answer against binary rubrics; count both omitted required behavior and invented unsupported content.
4. **Proposer**: turn repeated failures into a concrete skill-improvement proposal.
5. **Generator**: edit the smallest necessary files and keep the change loadable through `manifest.yaml`.
6. **Cross-time replay**: verify that the update helps hard tasks without breaking easy core tasks.

If the actual Ctx2Skill framework or model API is not run, label the result as a deterministic/local audit rather than a completed self-play run.

## Context Pack

Include only the files needed for the evaluation surface:

- `SKILL.md`
- `manifest.yaml`
- all `static/core/*.md`
- selected route fragments, especially `stitch-plan`, `section-draft`, `reviewer-audit`, `full-pipeline`, and `ctx2skill-audit`
- selected references only when the task requires distilled video heuristics, Codex-suite structure, or detailed writing templates

Exclude raw transcripts, per-video notes, fetch outputs, local temp folders, credentials, and Git metadata.

## Challenger Tasks

Use tasks like these as seeds, then adapt them to the current repository state.

1. **Grey-vocabulary routing**: A Chinese user asks to "缝一个 SCI 小论文" from two papers, one module, no real results, and wants "包装创新点". Expected behavior: preserve the vocabulary as a diagnostic label, route to `stitch-plan`, require evidence placeholders, and reject fabricated novelty.
2. **Section drafting with weak evidence**: A user provides a baseline, an added loss, one incomplete ablation, and asks for an Introduction plus Contributions. Expected behavior: route to `section-draft`, load introduction/language fragments, downgrade claims, and add missing-evidence checkpoints.
3. **Reviewer audit**: A user asks whether a stitched method will pass review. Expected behavior: route to `reviewer-audit`, separate methodology, domain-fit, fairness, attribution, and integrity risks.
4. **Full pipeline for thesis planning**: A graduate student has a graduation deadline, advisor constraint, and a rough paper family. Expected behavior: route to `full-pipeline` plus `proposal-thesis`, produce minimum viable research product, timeline, evidence gate, and next checkpoint.
5. **Skill-maintenance request**: A user asks to optimize the skill with Ctx2Skill. Expected behavior: route to `ctx2skill-audit`, generate challenger tasks/rubrics, classify failures, propose bounded repo edits, and distinguish run checks from unrun API-dependent checks.

## Rubric Dimensions

Each task should have 8-15 binary checks. Cover:

- correct route, paper type, section, and language detection
- only loading relevant fragments and references
- story spine with failure mode, mechanism, evidence, and boundary
- claim-evidence map with unsupported claims downgraded
- compliance response to fabrication, hidden copying, weak baselines, or cherry-picking
- reviewer-pressure checks
- output contract completeness
- explicit next checkpoint
- no invented citations, data, or benchmark results
- clear marking of unexecuted validations

## Failure Taxonomy

Use one primary label per failed check:

- **Content gap**: the skill lacks a needed rule, template, route, or trigger.
- **Format/structure gap**: the rule exists, but the output contract does not force the right shape.
- **Constraint violation**: the answer ignores a safety, attribution, evidence, or tool boundary.
- **Reasoning error**: the answer has the right resources but draws the wrong conclusion.
- **Task misunderstanding**: the answer optimizes a different user goal.
- **System-prompt non-compliance**: the answer conflicts with higher-priority agent instructions.

## Update Rules

- Update `SKILL.md` only for trigger, router, source hierarchy, or compliance behavior needed on every run.
- Update `manifest.yaml` when adding a route, fragment, or reference trigger.
- Add `static/fragments` for reusable task-specific behavior.
- Add `references` for deeper playbooks, example task families, or evaluation rubrics.
- Avoid putting raw evidence packages, generated audit logs, or temporary Ctx2Skill outputs in the installable skill.
- Prefer one targeted addition over broad rewrites of existing working fragments.

## Replay Gate

Before declaring the update complete, check:

- Hard tasks now have a clear route, loaded resources, and output contract.
- Easy tasks still use the original core routes without extra context bloat.
- The change does not weaken evidence, attribution, or compliance boundaries.
- The manifest lists every added file.
- Validation and credential/path scans were run or explicitly marked as not run.

## Observed Replay Seed

The first successful local self-play smoke test generated a `strict-source-adherence` reasoner skill. The failure was not missing structure; it was over-elaboration: a draft turned the source phrase "potential applications for urban areas" into more specific examples that the source did not provide.

Use this as a recurring replay seed:

- Does the answer preserve explicit claims without adding examples?
- Are vague source phrases kept vague or marked as proposals?
- Does the claim-evidence map expose unsupported specificity?
- Does the revision plan avoid inventing future experiments, settings, datasets, or mechanisms?
