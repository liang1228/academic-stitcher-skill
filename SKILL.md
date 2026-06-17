---
name: academic-stitcher-skill
description: |
  Structured academic paper-stitching and manuscript-writing skill. Use when the user asks to combine or extend papers, build an A+B research idea, design a defensible thesis/SCI/conference paper story, create an opening report or advisor-facing plan, draft or polish Nature-style manuscript sections, write Related Work/Method/Experiments/Discussion, simulate reviewer objections, or convert rough modules/results into a claim-evidence-boundary narrative. Trigger on English or Chinese requests such as paper stitching, academic tailor, research story, A+B idea, thesis proposal, manuscript draft, Nature-style writing, 论文故事, 缝论文, 学术裁缝, 小论文, 开题, 相关工作, 方法章节, SCI写作. Refuse fabricated data, fake citations, hidden copying, plagiarism, weakened baselines, undisclosed cherry-picking, or academic misconduct.
---

# Academic Stitcher Skill

Use this skill to turn paper ingredients into a defensible research story. The core move is not "A+B" for its own sake; it is "A has failure mode X, B addresses X through mechanism Y, and evidence Z proves the delta."

## Router Protocol

Follow this protocol for every request.

1. Read `manifest.yaml`.
2. Read every file listed under `always_load`.
3. Detect the request axes from the manifest:
   - `route`: stitch-plan, section-draft, nature-polish, reviewer-audit, or full-pipeline.
   - `paper_type`: research, methods, algorithmic, review, or proposal-thesis.
   - `section`: title, abstract, introduction, related-work, method, experiments, discussion, or conclusion.
   - `language`: zh-cn or en.
4. State the detected route in one compact line before producing substantive work.
5. Load only the matching `static/fragments/...` files. Do not load every fragment.
6. Use `references/` only on demand, following `manifest.yaml` reference triggers.

If the request supplies only a broad topic, route to scoping and paper-matrix work before drafting. If the user already has results, figures, or a draft, route directly to section architecture, polishing, or reviewer audit.

## Source Hierarchy

Apply sources in this priority order:

1. User-provided artifacts, data, drafts, advisor constraints, venue rules, and current results.
2. Core stance/workflow/output rules from `static/core/`.
3. Route, paper-type, section, and language fragments selected by `manifest.yaml`.
4. Deep references in `references/` when the selected task needs more templates or distilled heuristics.

Do not invent missing evidence. If a claim, baseline, dataset, citation, statistic, or mechanism is absent, write a placeholder, downgrade the claim, or ask for the missing input.

## Operating Model

For every task, identify:

1. **Goal**: thesis pass, proposal, SCI, conference, top venue, rebuttal, advisor memo, or manuscript section.
2. **Inheritance**: the baseline, paper family, task, dataset, lab lineage, or method tradition being extended.
3. **Delta**: the module, loss, data process, evaluation, writing move, or contribution being added.
4. **Mechanism**: why the delta should address the failure mode.
5. **Evidence**: main result, ablation, robustness, complexity, qualitative case, citation, or explicit limitation.
6. **Boundary**: where the claim stops.

For graduate-thesis or advisor-facing requests, also capture graduation rule, advisor expectation, authorship boundary, time left, target outlet, and minimum viable research product.

## Compliance Boundary

Reject or reframe requests that ask to fabricate, hide, or launder academic work.

- Do not fabricate data, citations, baselines, author contributions, experiment results, or peer-review history.
- Do not hide copied modules, formulas, code, datasets, figures, or writing. Require attribution.
- Do not give operational advice for plagiarism, detection evasion, weakened baselines, fake randomness, or selective omission of material negative evidence.
- Grey phrases such as "缝论文", "水文", "编故事", "科研 trick", and "造航母" may be retained as vocabulary and diagnostic labels. Convert them into transparent, attributable, evidence-bound research planning.

## Default Output

Use the output format from `static/core/output-format.md`. At minimum include:

```markdown
## Route
- Route:
- Paper type:
- Section:
- Target:
- Evidence state:

## Story Spine
1. Field pressure:
2. Failure mode:
3. Proposed move:
4. Mechanism:
5. Evidence:
6. Boundary:

## Claim-Evidence Map
| Claim | Evidence | Status | Boundary |
| --- | --- | --- | --- |

## Quality Gates
- Evidence:
- Citation/attribution:
- Fair comparison:
- Reviewer pressure:
- Next checkpoint:
```
