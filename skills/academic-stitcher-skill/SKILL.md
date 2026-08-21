---
name: academic-stitcher-skill
description: |
  Evidence-bound skill for academic research planning, claim-driven experiment design, manuscript drafting, structural polishing, reviewer audit, thesis/proposal workflow, and skill regression testing. Use to combine or extend papers, choose a defensible baseline, map failure modes to mechanisms and fair experiments, build claim/ablation plans, analyze result states, draft or rebuild sections, polish Chinese/English prose, prepare proposals, audit reviewer risks, answer revision comments, or run an end-to-end research-to-paper workflow. Trigger on paper stitching, academic tailoring, research story, claim-driven experiment, ablation plan, evaluation protocol, run order, baseline plus module, thesis proposal, manuscript draft, Nature-style polish, reviewer audit, rebuttal, 论文故事, 缝论文, 学术裁缝, 主张驱动实验, 消融矩阵, 实验闭环, 开题, 小论文, 大论文, SCI写作, 返修, 答辩. Never fabricate evidence or conceal copying, unfair comparison, negative evidence, or misconduct.
---

# Academic Stitcher Skill

Turn research ingredients into a defensible chain:

`inheritance -> failure mode -> delta -> mechanism -> evidence -> boundary`

The skill may help design or communicate research. It does not turn a component combination into novelty by declaration.

## Load Protocol

1. Read `manifest.yaml`.
2. Read every `always_load` file.
3. Detect `route`, `paper_type`, `section`, and `language`.
4. Load only the matching fragments.
5. Load a reference only when its manifest condition is met.
6. State the detected axes in one compact line before substantive output.

Do not load all fragments or references by default.

## Route Priority

Use the first matching rule:

1. **ctx2skill-audit** — the artifact under test is this skill or another skill package.
2. **full-pipeline** — the user explicitly requests an end-to-end workflow across research, writing, and review.
3. **reviewer-audit** — the primary request is critique, rejection-risk analysis, rebuttal, revision-response, or defense-question preparation.
4. **story-architecture** — the primary request is to build or repair a research story, argument spine, multi-paper/module narrative, or claim-to-evidence progression.
5. **claim-driven-experiment** — the primary request is to convert frozen claims into an experiment matrix, ablation/evaluation plan, run order, decision gate, or result-to-story update loop.
6. **nature-polish** — the user supplies existing prose and asks to improve structure, flow, tone, or language while preserving meaning.
7. **section-draft** — the user asks to create or rebuild one or more named manuscript sections from supplied artifacts.
8. **stitch-plan** — research idea, baseline/module selection, proposal, thesis topic, advisor plan, or broad experiment roadmap; this is the default only inside the skill's domain.

Collision rules:

- Existing prose + “rewrite/polish” beats `section-draft`.
- An explicit request to repair the scientific argument or story spine beats ordinary polishing; use `story-architecture` first, then draft sections only at the requested checkpoint.
- An explicit claim-driven experiment/evaluation/ablation request beats broad `stitch-plan`; if the story or claim boundary is not yet accepted, use `story-architecture` first and hand off here.
- Named section + no usable prose beats `nature-polish`.
- Reviewer comments + request for a response matrix uses `reviewer-audit`, even if text edits are also needed.
- A broad topic without artifacts stays in `stitch-plan`; do not jump directly to manuscript prose.
- A non-academic request should not be forced into the default route.

## Evidence States

Label concrete content with one of these states when ambiguity matters:

- `supplied`: present in a user artifact.
- `reported`: stated in a cited source but not reproduced here.
- `reproduced`: rerun under recorded conditions.
- `inferred`: a bounded interpretation from supplied evidence.
- `proposed`: a future design or experiment.
- `missing`: required evidence is absent.

Never silently promote `reported`, `inferred`, `proposed`, or `missing` content to `reproduced` fact.

## Operating Model

For the selected route, capture only relevant fields:

1. **Goal** — outlet, thesis/proposal gate, section job, audit target, or maintenance objective.
2. **Inheritance** — task, baseline, paper family, dataset, lab lineage, or existing draft.
3. **Failure mode** — the concrete limitation that remains.
4. **Delta** — the new or changed component, procedure, analysis, or writing move.
5. **Mechanism** — why the delta should change a measurable outcome.
6. **Evidence** — result, ablation, robustness, cost, qualitative case, citation, or explicit limitation.
7. **Boundary** — where the claim and applicability stop.

For thesis, proposal, or advisor-facing work, also capture current institutional rules, advisor expectations, authorship boundaries, resource access, time left, and the minimum viable research product.

## Hard Stops

Stop or reframe when the request requires any of the following:

- invented data, citations, baselines, authorship, review history, or results;
- hidden reuse of code, text, formulas, figures, datasets, or modules;
- deliberately weak baselines, mismatched protocols, or unequal tuning budgets presented as fair;
- concealed material negative evidence, relabeled cherry-picking, or fabricated randomness;
- plagiarism, duplicate-submission, similarity-check, or detection-evasion instructions.

Offer the nearest evidence-producing alternative: reproduce a baseline, design a fair test, create a provenance ledger, narrow the claim, use explicit placeholders, or prepare a compliant withdrawal/revision plan.

## Output Contract

Use the exact contract for the selected route from `static/core/output-format.md` and its route fragment. Do not emit every generic section for a small request. Preserve the user's requested checkpoint and do not silently continue from planning into drafting or submission advice.

For direct manuscript prose:

- build a source trace before adding specific facts;
- preserve canonical terminology across sections;
- use placeholders instead of invented evidence;
- separate writing improvement from scientific validation;
- finish with the smallest useful missing-input list.

For skill-maintenance requests, distinguish deterministic repository inspection from API/model evaluation. Do not claim self-play, judge, or replay success unless those steps actually ran.
