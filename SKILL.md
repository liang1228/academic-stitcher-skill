---
name: academic-stitcher-skill
description: |
  Turn related papers, baselines, modules, experiment results, or rough thesis ideas into a defensible academic paper story.
  Use when the user asks to stitch/combine papers, build an academic stitching plan, design A+B paper innovation, find research gaps/modules, draft a thesis or SCI paper outline, write Related Work or Method sections, explain workload/novelty, or package real experiment results into a compliant problem-mechanism-evidence narrative.
  使用场景包括“缝论文”“学术裁缝”“论文故事”“A+B 组合”“相关工作”“方法章节”“毕业论文大纲”“SCI/顶会故事线”。Refuse fabricated data, fake citations, plagiarism, hidden reuse, or academic misconduct.
---

# Academic Stitcher Skill

Use this skill to turn paper ingredients into a defensible research story. The core move is not "A+B" for its own sake; it is "A has failure mode X, B addresses X through mechanism Y, and evidence Z proves the delta."

## Load Resources Selectively

Keep `SKILL.md` as the execution guide. Load bundled resources only when the task needs them:

- Read `references/playbook.md` for deeper templates: diagnostic questions, paper matrix fields, story patterns, section templates, and red flags.
- Read `references/transcript-derived-playbook.md` when the user asks what was distilled from the video/transcript audit or needs source-informed heuristics.

The repository intentionally keeps only the distilled core. Per-video notes, raw transcripts, subtitle coverage tables, and acquisition audit tables are intermediate artifacts and are not part of the published skill.

## Operating Model

For every paper-stitching request, identify four layers:

1. **Goal**: thesis pass, course paper, SCI, conference, top venue, rebuttal, or outline.
2. **Inheritance**: the baseline model, task family, dataset, or paper lineage being extended.
3. **Delta**: the module, loss, data process, evaluation, analysis, or writing move being added.
4. **Story**: the problem-mechanism-evidence chain that makes the delta necessary and testable.

## Workflow

1. Triage the user's target, field, venue level, deadline, word/page constraint, and available artifacts.
2. Inventory real evidence: papers, code, baseline results, datasets, figures, failed runs, and existing draft sections.
3. Build a paper matrix of 8-20 directly related papers before proposing modules. Extract task, baseline, delta, claimed bottleneck, mechanism, evidence, reusable idea, and risk.
4. Write the inheritance sentence:
   `This work inherits [baseline/task] from [paper family], but [specific failure mode] remains under [scenario], so it introduces [delta] to address [mechanism].`
5. Convert each proposed module into a mechanism claim. Keep it only if it has a failure mode, compatibility rationale, and measurable evidence plan.
6. Map claims backward into sections: title, abstract, introduction, related work, method, experiments, limitations.
7. Run the compliance check before final output.

## Compliance Check

Reject or reframe requests that ask to fabricate, hide, or launder academic work.

- Do not fabricate data, citations, baselines, author contributions, or experiment results.
- Do not hide copied modules, formulas, code, datasets, or writing. Require attribution.
- Do not turn "rewrite to avoid detection" requests into operational advice. Reframe as legitimate synthesis with citation and original analysis.
- Do not overclaim top-venue novelty when the evidence supports only a thesis, workshop, negative-result, or incremental paper.
- Treat unavailable, too-short, or likely mismatched source material as excluded evidence, not method rules.

## Default Output

```markdown
## Paper Stitching Map
- Target: [venue/thesis goal and workload]
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
```
