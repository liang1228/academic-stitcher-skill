# Paper Type: Algorithmic

Use for models, modules, pipelines, optimization methods, or AI/ML systems.

## Reader Question

Does the system perform under fair comparison, and why does the added component help?

## Argument Chain

Task -> baseline failure -> proposed module/pipeline -> mechanism -> main comparison -> ablation -> robustness/efficiency.

## Required Evidence

- Baseline selection rule.
- Main table under matched protocol.
- Ablation for each claimed component.
- Complexity, runtime, or parameter cost when relevant.
- Failure cases or sensitivity analysis.

---

## Baseline Selection Rules

(BVID sources: BV19jCrYsEoE, BV1vt4y1T7sy, BV1ne41157Gn, BV1fV4y1B72F, BV1dg411p7QP, BV12M4y1J737)

- **Same domain first**: find baselines in the same task domain; if unavailable, move to the nearest analogous domain.
- **Recency filter**: prefer baselines from the last 2-3 years; very old models (e.g., YOLOv3 for 2025 work) undermine credibility.
- **Must be open-source and reproducible**: check for code links in the last line of the abstract; confirm the code is complete and runnable before committing.
- **Credibility bracket**: always include at least one recent top-venue baseline (even if you only "almost" beat it) and a few mid/low-tier comparisons; never compare only against weak methods.
- **Strategic selection**: among published methods, pick those whose numbers are most favorable to your case; top venues also use selective reporting of representative methods rather than exhaustive comparison.
- **Baseline parameter parity is not required**: different models legitimately use different batch sizes, learning rates, and random seeds; the baseline may use less favorable settings while your method uses optimized ones.

## Ablation Strategy

(BVID sources: BV1fV4y1B72F, BV1fW4y1W7dS, BV1rDMHzTEEd)

- **Required monotonicity**: a well-formed ablation should show A < A+B < A+B+C, proving each added module contributes positively.
- **When ablation fails (module removal improves results)**: merge the problematic module with its neighbor into a single described unit so it can only be removed as a whole. Reframe the combination as one integrated component.
- **Per-configuration tuning**: when ablation relations do not hold, tune each configuration separately (many runs per config, pick best/worst appropriately) -- this is technically permissible in many ML subfields.
- **Ablation granularity**: remove one module at a time, then pairs, then show the full model; always include a "no proposed modules" baseline row.
- **Supplement with parameter sensitivity**: show how key hyperparameters (layers, weights, thresholds) affect performance; this fills ablation tables when module removal is impractical.

## Dataset Principles

(BVID sources: BV19jCrYsEoE, BV18Ve6zvEBT)

- **Prefer public over private datasets**: public datasets allow direct module stitching and fast iteration; private datasets introduce data-processing complexity and increase risk of dead ends.
- **Follow domain conventions**: check what datasets the target venue's recent papers use and mirror that selection.
- **Alignment with baselines**: ensure the same train/val/test split and preprocessing are used across all compared methods; reference the split protocol from the baseline paper.
- **Data description**: copy dataset descriptions from top-venue papers (paraphrase to avoid direct duplication).

## Performance Presentation

(BVID sources: BV15u411x7iE, BV14c411A75s, BV1dg411p7QP, BV18Ve6zvEBT)

- **Metric calculation flexibility**: when the field lacks a single standard for metric computation (e.g., image cropping range, normalization), choose the calculation that yields the most favorable numbers -- as long as it is defensible.
- **Preprocessing sensitivity**: small changes in preprocessing (e.g., cropping from [-1, 1] to [-1, -0.5]) can significantly affect metrics like SSIM; explore these variations.
- **Hardware and seed variation**: different GPUs and random seeds produce different results; use this to your advantage when reproducing baselines.
- **Selective reporting is common**: even top venues select representative methods for comparison rather than including every published variant.
- **Always bold the best result** in comparison tables; follow the target venue's formatting convention.

## Weak Result Handling

(BVID sources: BV1LK9ZYYErM, BV19jCrYsEoE, BV1fV4y1B72F)

- **Iterate over module combinations**: performance stagnation is normal; use combinatorial search over different module stacks until a positive delta appears.
- **Do not abandon the paper for weak results**: keep adding/swapping modules using the stitching methodology until a viable combination is found.
- **Reframe weak dimensions**: if a metric shows no improvement, downplay it or omit it (unless the field mandates it); emphasize the metrics where your method excels.
- **Negative result placement**: unfavorable numbers can be placed in appendices, footnotes, or qualitative discussion sections rather than main comparison tables.
- **Reproducibility caveat**: when claiming results, be precise about what was measured; do not fabricate numbers, but strategic presentation of real results is standard practice.
