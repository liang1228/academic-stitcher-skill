# Section: Experiments

## Job
Test every major claim under fair comparison.

## Evidence Ladder
1. Dataset, split, metric, protocol.
2. Baseline selection rule.
3. Main result.
4. Ablation.
5. Robustness or sensitivity.
6. Complexity or efficiency.
7. Qualitative case and failure case.

## Checks
- Label reported versus reproduced numbers.
- Do not weaken baselines.
- Do not call selected examples random unless selection was random.
- Include limitations when deltas are unstable.

## 4-Part Experiment Structure (Video-Derived)

### Part 1: Configuration
| Element | What to Include | Strategy |
|---------|----------------|----------|
| Datasets | Name, size, domain, split | From top-tier papers |
| Metrics | 2-4 per domain convention | Follow convention |
| Implementation | Hardware, framework, hyperparams | Match target journal |
| Training | Batch size, LR, epochs | Mimic recent papers |
> Source: BV1rDMHzTEEd (011), BV1fW4y1W7dS

### Part 2: Comparison Experiments
| Rule | Rationale |
|------|-----------|
| Baselines slightly below top-tier | Beat them convincingly |
| 2-3 recent papers (last 2-3 years) | Shows current awareness |
| 1-2 weaker baselines | Makes numbers look better |
| Reported numbers from originals | Label: "reported" vs "reproduced" |
| Same dataset/split for all | Fair comparison |
> Source: BV1fW4y1W7dS, BV1rDMHzTEEd (011)
Bold best results. Good results need minimal explanation; bad results MUST have a reason.

### Part 3: Ablation Studies
| Variant | Description | Purpose |
|---------|-------------|---------|
| Full model | All modules | Baseline |
| w/o Module B | Remove B | Proves B necessary |
| w/o Module C | Remove C | Proves C necessary |
| w/o B and C | Remove both | Combined effect |
**Critical rule:** If removing a module IMPROVES performance, merge it with its adjacent module so it can only be ablated as a whole.
> Source: BV1fW4y1W7dS

### Part 4: Qualitative / Visualization
Side-by-side with baseline; compare against ground truth; pick examples demonstrating advantage.

### Weak Result Strategies
| Situation | Strategy |
|-----------|----------|
| One weak metric | Do not highlight; focus on strong metrics |
| One weak dataset | Attribute to dataset characteristics |
| Baseline outperforms on one | Acknowledge and explain |
| Marginal improvement | Reframe as efficiency |
| Runtime is worse | Omit unless required |
> Source: BV1rDMHzTEEd (011), BV1fW4y1W7dS

### Common Mistakes
1. **Too few baselines**: 4-5 for journals; 3-4 for conferences
2. **Unfair comparison**: Different splits or preprocessing
3. **No explanation for bad results**: Every below-average number needs a reason
4. **Ablation without purpose**: Each must test a specific claim
5. **Claiming SOTA without baselines**: "SOTA" is relative to your set

### Chinese Academic Context
- Chinese journals often require 3-5 datasets (more than Western conferences)
- Master's thesis experiments run 20-40 pages with all four parts
- "本章小结" must restate key findings with specific numbers
