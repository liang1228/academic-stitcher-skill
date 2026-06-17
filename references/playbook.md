# Paper Tailor Playbook

Use this reference when a task needs deeper structure than the main `SKILL.md`.

## Table Of Contents

- [Diagnostic Questions](#diagnostic-questions)
- [Paper Matrix Fields](#paper-matrix-fields)
- [Story Patterns](#story-patterns)
- [Document-Derived Graduate Workflow](#document-derived-graduate-workflow)
- [Grey Vocabulary Map](#grey-vocabulary-map)
- [Opening Report Scaffold](#opening-report-scaffold)
- [SCI Paper Skeleton](#sci-paper-skeleton)
- [Fair Evidence Rules](#fair-evidence-rules)
- [Section Templates](#section-templates)
- [Red Flags](#red-flags)
- [Preferred Response Style](#preferred-response-style)

## Diagnostic Questions

Ask or infer:

1. What is the user's target: thesis pass, course paper, SCI, conference, top venue, rebuttal, or outline?
2. What does the user already have: baseline, code, dataset, metric table, figures, draft, or only papers?
3. What is the inherited paper family?
4. What is the proposed delta?
5. What evidence can be produced without fabrication?
6. What claim is too large for the current evidence?

## Paper Matrix Fields

Use these columns for literature triage:

| Column | What to extract |
| --- | --- |
| Paper identity | title, year, venue, link |
| Task/data | task definition, dataset, metric |
| Baseline | inherited model, classical method, or common pipeline |
| Delta | module, loss, data process, architecture change, objective, analysis |
| Claimed bottleneck | what weakness the paper says it solves |
| Mechanism | why the delta should solve that weakness |
| Evidence | main result, ablation, robustness, qualitative example |
| Borrowable piece | what can be reused as cited inspiration |
| Risk | mismatch, compute cost, weak evidence, likely reviewer objection |

## Story Patterns

### Pattern A: Baseline Has A Blind Spot

- Existing methods perform well globally but fail on `[case]`.
- The failure happens because `[mechanism]`.
- Add `[delta]` to expose/correct/regularize `[mechanism]`.
- Prove with subgroup metrics, ablation, and error examples.

### Pattern B: Two Streams Are Both Needed

- A captures `[signal 1]`; B captures `[signal 2]`.
- Prior work treats them separately or fuses them naively.
- The proposed method aligns/fuses/gates them at `[stage]`.
- Prove with single-stream ablation, naive-fusion ablation, and complexity comparison.

### Pattern C: Simple Method Wins By Targeting The Venue

- The target venue values reliability, clarity, or application fit more than novelty theater.
- Use a modest delta but provide clean experiments, clear writing, and reproducibility.
- Avoid claiming top-level novelty; claim practical improvement, robustness, or easier deployment.

### Pattern D: Bad Results Become A Bounded Claim

- If the main metric is weak, look for honest subcases, robustness, cost, interpretability, or failure analysis.
- Do not invent or massage data.
- Reposition the work as diagnostic, negative-result, workshop, thesis, or follow-up plan if the evidence cannot support a full paper.

## Document-Derived Graduate Workflow

This section distills the added graduate survival, advisor Q&A, opening-report, small-paper, and SCI-template documents into reusable rules. Keep grey phrases as vocabulary, but convert risky tactics into transparent, attributable, evidence-bound work.

### Target Backward Planning

- Start from the user's exit target: graduation only, job, PhD application, scholarship, advisor requirement, or publication goal.
- Translate the target into a minimum viable research product: thesis workload, small paper, SCI submission, opening report, or only a defensible research plan.
- Use the gap between the desired CV and the current CV to choose tasks. Prefer tasks that produce durable evidence: reproduced baseline, paper matrix, experiment table, figure, draft section, or advisor-approved plan.
- Do not default to "publish a paper" when it does not serve the user's graduation, PhD, job, or advisor constraint.

### Advisor And Contribution Alignment

- Do not tell the advisor "I want to write a paper" as an empty request. Bring a concrete work package: literature map, baseline reproduction, dataset audit, candidate module list, draft outline, or preliminary table.
- Clarify contribution and authorship expectations early, especially before a first collaborative paper.
- Treat advisor style and lab inheritance as constraints. If lab lineage, senior code, or dataset access exists, verify permission and attribution before building on it.
- Convert conflict or uncertainty into a decision memo: current evidence, options, cost, risk, recommendation, and what decision is needed from the advisor.

### Feasible Topic Selection

- Prefer directions with public datasets, established metrics, comparable papers, and at least one reproducible baseline when the deadline is tight.
- Use private or newly collected data only when access, labeling, ethics, cleaning, and evaluation resources are real.
- Avoid "from-zero" topics with no survey, no benchmark, no comparable method, no metric, and no implementation path unless the user explicitly wants exploratory research and accepts the risk.
- If no direct survey exists, inspect adjacent surveys. If even adjacent structure is absent, downgrade publication ambition and define the work as exploratory.

### Baseline And Module Assembly

- Treat the baseline as the inherited frame: task, dataset, preprocessing, architecture, objective, and evaluation protocol.
- Treat a module as a separable component that can be removed, replaced, or measured in ablation.
- Choose baselines by reproducibility and task fit, not only venue prestige. Recent strong papers are useful only if their code, data, or protocol can be reconstructed.
- Keep a module only when it has three links: source/citation, compatibility with the baseline, and a mechanism that predicts a measurable improvement.
- Turn A+B into a research claim by naming the baseline failure mode, why the module should address it, and what evidence will test the claim.

## Grey Vocabulary Map

Retain the user's source vocabulary so the skill can recognize the domain, but use the safe interpretation in the actual plan.

| Grey phrase | Safe interpretation | Boundary |
| --- | --- | --- |
| 缝论文 / 学术裁缝 | Literature-driven module integration with attribution | No hidden copying, fake novelty, or uncredited reuse |
| 水文 / 保毕业 | Graduation-focused, low-risk paper with bounded claims | Do not fabricate data, citations, or contribution |
| 编故事 / 论文包装 | Problem-mechanism-evidence narrative | Do not invent a fake problem or hide contradictory evidence |
| 科研 trick | Legitimate research craft: search strategy, fair tuning, ablation design, visualization, writing clarity | No selective weakening, undisclosed cherry-picking, or false randomness |
| 造航母 | From-zero, high-risk topic without existing data, metrics, baselines, or literature | Downgrade ambition unless resources and time are real |
| 胶水技能 | Engineering skill needed to integrate baseline and module | Integration must be reproducible and documented |
| 挑 SOTA | Define a comparison set matching task, data, date, venue, and reproducibility | Do not pick only weak baselines while implying full SOTA coverage |
| 只答不辩 | Defense posture: acknowledge feedback, record decisions, revise plan | Do not evade substantive methodological objections |

## Opening Report Scaffold

Use this when the user asks for a thesis proposal, opening report, advisor-facing plan, or defense PPT.

| Part | What To Produce | Evidence Check |
| --- | --- | --- |
| Topic basis | Field background, task pressure, and why the problem matters now | 2-3 surveys or recent representative papers |
| Research status | Domestic/foreign or field-level method families, not a paper-by-paper dump | Grouped paper matrix with strengths and limits |
| Research significance | Scientific value plus practical value, stated modestly | No claim beyond available task/data evidence |
| Research content | 2-4 concrete research questions or work packages | Each has input, method, output, and evaluation |
| Research objective | What will be demonstrated by the end | Must be achievable within time and resources |
| Key problems | Bottlenecks that the method must solve | Each maps to a module, experiment, or risk plan |
| Method route | Pipeline, baseline, delta, training/inference, and figure plan | Shapes, data flow, and dependencies are clear |
| Feasibility | Data, code, compute, preliminary result, and advisor/lab support | Missing resources are listed as risks |
| Innovation | New combination, new adaptation, new evidence, or new application | Must be specific and attributable |
| Schedule | Literature, reproduction, module design, experiments, writing, revision, defense | Time boxes include buffer for failed runs |
| References | Real, relevant references | No fake citations or filler references |

Write opening reports as feasible commitments, not fantasy promises. If the source material encourages exaggeration or "only answer, do not debate" behavior, reframe it as: listen to committee feedback, record decisions, and revise the plan.

## SCI Paper Skeleton

Use this section when the user wants a compact SCI-style paper plan.

| Section | Narrative Job | Minimum Content |
| --- | --- | --- |
| Abstract | Compress field, gap, method, evidence, and contribution | One sentence each for problem, method, result, implication |
| Introduction | Lead from field pressure to specific gap | Motivation, failure mode, why existing work is insufficient, contributions |
| Related Work | Establish lineage and gap | Task lineage, baseline lineage, module lineage, unresolved gap |
| Method / Approach | Explain how the delta enters the baseline | Overall pipeline, baseline recap, module mechanics, objective, complexity |
| Experiments | Test every claim | Dataset, metrics, baselines, main result, ablation, robustness, case study |
| Analysis | Explain why the result happened | Module contribution, failure cases, sensitivity, qualitative examples |
| Conclusion | State what was shown and what remains limited | No new claims not supported earlier |

Keep the section order conventional unless the target venue requires otherwise. Fix source typos and informal names before producing user-facing text.

## Fair Evidence Rules

Use these rules to convert grey source suggestions into compliant research practice.

- **Baseline selection**: define the selection rule before comparing: same task, same dataset, recent enough, reproducible or directly reported, and representative of the target venue level.
- **Reported vs reproduced numbers**: label which results are copied from original papers and which are reproduced locally. Do not mix them silently.
- **Hyperparameters**: tune baselines and proposed methods fairly under comparable budgets. Do not intentionally weaken a baseline to create a gap.
- **Ablation**: test each separable component alone and in combination when meaningful. If components only make sense jointly, state that and include a grouped ablation plus a rationale.
- **Case study**: select qualitative examples by a stated rule. If examples are curated, call them curated and include at least one failure or borderline case.
- **SOTA language**: use "compared with selected baselines" unless the comparison actually covers the strongest recent systems under the same protocol.
- **Negative evidence**: failed runs, unstable gains, or non-significant deltas should become limitations, robustness checks, or a narrower claim.

## Section Templates

### Related Work

Group by argumentative role:

1. `Task lineage`: what problem family the work belongs to.
2. `Baseline lineage`: what the method inherits.
3. `Delta lineage`: where the module or idea comes from.
4. `Gap`: why existing combinations are insufficient.

Avoid summarizing every paper equally. Every paragraph should push the reader toward the proposed method.

### Method

Use this order:

1. Problem formulation.
2. Overall pipeline.
3. Baseline recap in one compact paragraph.
4. Proposed delta with input/output shapes.
5. Training objective or inference procedure.
6. Complexity and implementation details.

### Experiments

Match every claim to evidence:

| Claim | Required evidence |
| --- | --- |
| Better performance | main table with fair baselines |
| Module is useful | ablation removing or replacing it |
| Robustness | noise, split, domain, or sensitivity test |
| Efficiency | parameter/FLOP/time comparison |
| Interpretability | qualitative examples tied to the mechanism |

## Red Flags

- The method name changes but the operation is identical to a cited paper.
- The story says "solves X" but no experiment measures X.
- The contribution list names three modules but the ablation only supports one.
- The introduction promises top-venue novelty while the experiments only support a thesis-level result.
- The user wants "降重" without a real conceptual delta.
- The user wants to hide missing data, failed reproduction, or private-data provenance.

## Preferred Response Style

Be concrete and slightly skeptical. Use the user's actual papers and results. If the evidence is thin, say so and give the next experiment or narrower venue/story that would make the work defensible.
