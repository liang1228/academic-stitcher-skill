# Section: experiments

## Job

Test each major claim under a fair, transparent, and reproducible protocol.

## Evidence Ladder

1. Dataset/corpus/population, split, metric, and protocol.
2. Comparator inclusion rule and implementation source.
3. Main result under matched conditions.
4. Ablation or component attribution.
5. Robustness, sensitivity, uncertainty, or alternative explanations.
6. Runtime, compute, sample, annotation, or other relevant cost.
7. Qualitative and failure cases with selection method disclosed.

## Comparison Ledger

| Method | Result state | Data/protocol | Tuning budget | Source/version | Comparable? |
| --- | --- | --- | --- | --- | --- |

## Checks

- Separate reported from reproduced numbers.
- Include strong, relevant comparators; do not choose only weak baselines.
- Use compatible preprocessing, metrics, and tuning effort, or disclose differences.
- If an ablation contradicts a component claim, revise/remove the claim rather than hiding the result.
- Do not call hand-picked cases random.
- Report material negative results and resource trade-offs.
- Do not infer mechanism from a single aggregate improvement.
