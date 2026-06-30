# Section: Abstract

## Job

Compress the entire paper into problem, gap, approach, evidence, contribution, and boundary.

## Structure

1. Field or problem.
2. Specific gap.
3. Proposed approach.
4. Strongest result or evidence.
5. Implication and boundary.

## Checks

- Do not invent numbers or datasets.
- Do not claim broad novelty unless the literature matrix supports it.
- Make evidence visible, not just the method name.

## 4-Sentence Abstract Framework (Video-Derived)

| Sentence | Role | Template |
|----------|------|----------|
| S1: Background | Domain | "[Domain] has achieved significant progress in [task], playing a critical role in [application]." |
| S2: Gap | Problem | "However, existing methods suffer from [problem A], [problem B], and [problem C], leading to [consequence]." |
| S3: Approach | Method | "To address these issues, we propose [Method Name], integrating [Module B] for [purpose] and [Module C] for [purpose]." |
| S4: Evidence | Results | "Extensive experiments on [datasets] demonstrate [metric] improvement over state-of-the-art, validating each component." |

> Source: BV1fW4y1W7dS, BV12WJ6zoEa6 (009)

### Abstract vs Conclusion: Critical Difference

| Aspect | Abstract | Conclusion |
|--------|----------|------------|
| Covers | Introduction + Method | Method + Experiments |
| Framing | Why we did this (gap-driven) | What we found (evidence-driven) |
| Background | Brief field context | None |
| Results | Strongest single number | Summary of all findings |
| Future work | Omit or one sentence | Include 2-3 directions |

The abstract is a concentrate of introduction + method; the conclusion is a concentrate of method + experiments. A+B module descriptions must NOT use identical phrasing in both -- rephrase every sentence.

> Source: BV12WJ6zoEa6 (009), BV1fW4y1W7dS

### Common Abstract Mistakes

1. **Too much background**: More than one sentence on field context wastes space
2. **No specific gap**: "Existing methods have limitations" without naming them
3. **Method name without mechanism**: "We propose X" without saying what X does
4. **Vague results**: "Good performance" without numbers or comparison targets
5. **Repeating the title**: The abstract should add information, not restate the title
6. **Identical phrasing with conclusion**: Reviewers will notice and penalize

### Different Evidence State Strategies

| Evidence State | Strategy |
|---------------|----------|
| Strong (clear improvement on all metrics) | Lead with the best metric number; can claim "state-of-the-art" |
| Mixed (good on most, weak on 1-2) | Report aggregate improvement; omit weak metrics from abstract |
| Weak (marginal gains) | Focus on a different strength: efficiency, interpretability, or specific sub-task; use "competitive" instead of specific numbers |

### Chinese Academic Context

- Chinese journal abstracts require both Chinese and English versions; the Chinese must be a faithful translation, not a different summary
- Master's thesis abstracts in Chinese typically run 300-500 characters; keep English within 150-250 words
