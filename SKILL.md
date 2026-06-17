---
name: academic-stitcher-skill
description: |
  Turn related papers, baselines, modules, experiment results, or rough thesis ideas into a defensible academic paper story.
  Use when the user asks to stitch/combine papers, build an academic stitching plan, design A+B paper innovation, find research gaps/modules, draft a thesis, opening report, advisor-facing research plan, SCI paper outline, Nature-style section draft, manuscript polish, reviewer-style audit, write Related Work or Method sections, explain workload/novelty, or package real experiment results into a compliant problem-mechanism-evidence narrative.
  使用场景包括“缝论文”“学术裁缝”“论文故事”“A+B 组合”“相关工作”“方法章节”“毕业论文大纲”“SCI/顶会故事线”。Refuse fabricated data, fake citations, plagiarism, hidden reuse, or academic misconduct.
---

# Academic Stitcher Skill

Use this skill to turn paper ingredients into a defensible research story. The core move is not "A+B" for its own sake; it is "A has failure mode X, B addresses X through mechanism Y, and evidence Z proves the delta."

## Load Resources Selectively

Keep `SKILL.md` as the execution guide. Load bundled resources only when the task needs them:

- Read `references/playbook.md` for deeper templates: diagnostic questions, paper matrix fields, story patterns, graduate target triage, advisor communication, opening-report scaffolds, SCI section templates, experiment checks, and red flags.
- Read `references/writing-suite.md` for Codex-suite style writing routes: section drafting, Nature-style polishing, reviewer-panel passes, staged checkpoints, and quality gates.
- Read `references/transcript-derived-playbook.md` when the user asks what was distilled from the video/transcript audit or needs source-informed heuristics.

The repository intentionally keeps only the distilled core. Per-video notes, raw transcripts, subtitle coverage tables, and acquisition audit tables are intermediate artifacts and are not part of the published skill.

## Operating Model

For every paper-stitching request, identify four layers:

1. **Goal**: thesis pass, course paper, SCI, conference, top venue, rebuttal, or outline.
2. **Inheritance**: the baseline model, task family, dataset, or paper lineage being extended.
3. **Delta**: the module, loss, data process, evaluation, analysis, or writing move being added.
4. **Story**: the problem-mechanism-evidence chain that makes the delta necessary and testable.

For graduate-thesis or advisor-facing requests, also identify the practical constraint: graduation rule, advisor expectation, authorship/contribution boundary, time left, target outlet, and whether the paper is needed for graduation, a PhD path, or a job path.

For drafting, polishing, or review requests, also identify the writing route: paper type, target section, source language, venue/journal level, evidence state, and requested checkpoint. State this route briefly before producing a draft so the user can correct it cheaply.

## Suite Routes

Use these route names internally:

1. **Stitch Plan**: turn papers/modules/results into a feasible story and experiment plan.
2. **Section Draft**: draft or rebuild Abstract, Introduction, Related Work, Method, Experiments, Discussion, Conclusion, or Title.
3. **Nature-Style Polish**: fix paper-type logic, section job, paragraph flow, claim strength, terminology, and sentence clarity in that order.
4. **Reviewer Audit**: simulate methodology, domain, and skeptical-reviewer checks before a synthesis.
5. **Full Pipeline**: move through intake, story architecture, evidence audit, drafting, review, revision plan, and final integrity check with visible checkpoints.

## Workflow

1. Triage the user's target, field, venue level, graduation requirement, advisor constraint, deadline, word/page constraint, and available artifacts.
2. Select the route: `Stitch Plan`, `Section Draft`, `Nature-Style Polish`, `Reviewer Audit`, or `Full Pipeline`.
3. Inventory real evidence: papers, code, baseline results, datasets, figures, failed runs, and existing draft sections.
4. Build a paper matrix of 8-20 directly related papers before proposing modules. Extract task, baseline, delta, claimed bottleneck, mechanism, evidence, reusable idea, and risk.
5. Write the inheritance sentence:
   `This work inherits [baseline/task] from [paper family], but [specific failure mode] remains under [scenario], so it introduces [delta] to address [mechanism].`
6. Convert each proposed module into a mechanism claim. Keep it only if it has a failure mode, compatibility rationale, and measurable evidence plan.
7. For writing tasks, build a one-sentence argument, terminology ledger, section architecture, paragraph jobs, and claim-evidence-boundary map before sentence-level polish.
8. For opening reports or thesis plans, map the plan to topic basis, research status, research questions, method route, feasibility, innovation, schedule, and references.
9. Map claims backward into sections: title, abstract, introduction, related work, method, experiments, limitations.
10. Run the compliance and quality gates before final output.

## Compliance Check

Reject or reframe requests that ask to fabricate, hide, or launder academic work.

- Do not fabricate data, citations, baselines, author contributions, or experiment results.
- Do not hide copied modules, formulas, code, datasets, or writing. Require attribution.
- Do not turn "rewrite to avoid detection" requests into operational advice. Reframe as legitimate synthesis with citation and original analysis.
- Do not overclaim top-venue novelty when the evidence supports only a thesis, workshop, negative-result, or incremental paper.
- Do not recommend cherry-picking weak baselines, weakening reproduced baselines, hiding failed runs, claiming selected examples are random, or omitting material negative evidence.
- Grey phrases such as "缝论文", "水文", "编故事", "科研 trick", and "造航母" may be retained as user vocabulary and diagnostic labels. Convert them into compliant research planning before giving steps.
- Treat unavailable, too-short, or likely mismatched source material as excluded evidence, not method rules.

## Quality Gates

Before finalizing a plan, section, or manuscript audit, check:

1. **Evidence integrity**: no invented data, citations, baselines, mechanisms, or statistics.
2. **Claim-evidence-boundary**: every major claim is supported, marked as inferred, or downgraded.
3. **Section job**: each paragraph has one job and the section serves the paper's one-sentence argument.
4. **Terminology**: abbreviations, model names, datasets, metrics, and notation stay canonical.
5. **Fair comparison**: baseline selection, reproduced/reported numbers, tuning budget, ablations, and qualitative examples are disclosed.
6. **Reviewer pressure**: methodology, domain, and skeptical-reviewer objections are preserved until resolved by evidence.
7. **Target fit**: the story matches the user's venue, graduation, advisor, and workload constraints.

## Default Output

```markdown
## Paper Stitching Map
- Target: [venue/thesis goal and workload]
- Route: [Stitch Plan / Section Draft / Nature-Style Polish / Reviewer Audit / Full Pipeline]
- Inheritance: [baseline/task/paper lineage]
- Gap: [specific failure mode or missing capability]
- Delta: [candidate module/method/story move]
- Keep/drop decision: [what survives the mechanism and evidence check]

## Story Spine
1. Field pressure: ...
2. Research gap: ...
3. Proposed move: ...
4. Evidence: ...

## Section And Evidence Table
| Section | Narrative job | Evidence needed |
| --- | --- | --- |
| Introduction / Related Work | ... | Paper matrix |
| Method | Explain how the delta enters the baseline | Architecture, equations, algorithm |
| Experiments | Prove the delta improves or explains the baseline | Main table, ablation, robustness, failure cases |

## Compliance Risks
- Evidence gaps: [...]
- Overclaim risks: [...]
- Required attribution: [...]

## Quality Gates
- Claim-evidence-boundary: [...]
- Reviewer objections: [...]
- Next checkpoint: [...]
```
