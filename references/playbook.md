# Paper Tailor Playbook

Use this reference when a task needs deeper structure than the main `SKILL.md`.

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
