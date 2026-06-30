# Section: Discussion

## Job

Explain what the evidence means, how it relates to prior work, and where the claim stops.

## Structure

1. Main interpretation.
2. Why the mechanism is plausible.
3. Relation to prior work.
4. Practical or theoretical implication.
5. Limitations and future work.

## Checks

- Use hedging for indirect mechanisms.
- Do not introduce new untested contributions.
- Make the boundary explicit.

## Interpreting Results Without Overclaiming (Video-Derived)

Discussion content is often woven into the experiment section's analysis. When a dedicated section exists:

| Element | What to Do | Example Phrasing |
|---------|-----------|------------------|
| Main finding | State what results show, not what you hoped | "[Module B] contributes primarily to [specific metric]" |
| Mechanism | Explain WHY, grounded in design | "This improvement is attributable to [mechanism]" |
| Prior work | Connect to Related Work papers | "This aligns with [Author]'s observation that [finding]" |
| Scope | State where claims do NOT apply | "This advantage diminishes when [condition]" |

> Source: BV1rDMHzTEEd (011), BV1Lgt7eMEZd

### Relating to Prior Work

1. **Recall the gap**: "In Section 2, we identified [limitation]. Our results demonstrate that [method] addresses this by [evidence]"
2. **Compare mechanisms**: "Unlike [Prior Method] which [mechanism], our approach [different mechanism]"
3. **Acknowledge overlap**: "While [Author] reported [similar result], our analysis reveals [additional insight]"

### Limitation Framing Rules

**Good framing:**
- "Our method assumes [X], which may not hold when [Y]" -- honest boundary
- "Degraded performance on [condition] suggests [insight]" -- limitation as insight
- "Future work could explore [direction] to address [limitation]" -- forward-looking

**Bad framing:**
- "Our method is not perfect" -- too vague
- "We could not run more experiments due to time" -- reveals weakness without insight
- Limitations that apply to ALL methods, not just yours

### Different Evidence State Strategies

| State | Strategy |
|-------|----------|
| Strong, consistent results | Focus on WHY it works and field implications; brief limitations |
| Mixed results | Address divergences honestly; frame as insights about [factor] |
| Weak results | Focus on what experiments REVEALED; frame as exploratory |

### Common Mistakes

1. **Introducing new results**: Discussion interprets existing results only
2. **Repeating the experiment section**: Interpret meaning, don't restate numbers
3. **Overclaiming**: "solves [X]" vs "partially addresses [X]"
4. **Ignoring negative results**: If ablation showed a module didn't help, discuss why

### Chinese Academic Context

- In Chinese theses, discussion is often combined with the experiment chapter
- Chinese CS journal papers rarely have standalone discussion; analysis is embedded in experiment paragraphs
- When standalone discussion is required, ensure "本章小结" restates key insights
