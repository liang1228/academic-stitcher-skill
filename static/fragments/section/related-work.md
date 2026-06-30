# Section: Related Work

## Job

Show lineage and establish the unresolved gap without dumping paper summaries.

## Structure

1. Task lineage.
2. Baseline or method family.
3. Delta/module lineage.
4. Remaining gap.

## Checks

- Every paragraph should push toward the proposed method.
- Do not exaggerate weaknesses in prior work.
- Attribute borrowed components explicitly.
- Separate survey claims from direct paper evidence.

## Organizing by Argument Role (Video-Derived)

Use "总分分[总]" (general-specific-specific-[general]). Organize by the argument role each body of work plays, NOT by paper order.

### The A/B/C Module Lineage Mapping

| Paragraph Group | Content | Argument Role |
|----------------|---------|---------------|
| Group 1: Overview | Introduce field broadly; state existing limitations | Establish the gap |
| Group 2: Module A lineage | Trace your base model development (e.g., VLP -> CLIP) | Show the foundation |
| Group 3: Module B/C lineage | Trace auxiliary module development (e.g., attention, detection) | Show integrated components |
| Group 4 (optional): Summary | Recap development; re-state remaining gap | Bridge to your method |

> Source: BV1rPGdz3E2V (005), BV1fW4y1W7dS

### Concrete Template

**Group 1 - Overview:**
"Recent advances in [field] have [progress]. However, existing methods suffer from [limitation], which motivates our approach. We review progress along [direction A], [direction B], and [direction C]."

**Group 2 - Module A lineage:**
"For [module A task], [Author1] proposed [method] but suffered from [limitation]. [Author2] introduced [improvement] by [mechanism]. Our work extends this line by [modification]."

**Group 3 - Module B/C lineage:**
"Regarding [module B task], early approaches [description]. [Author] proposed [method] for [issue]. Despite improvements, [remaining gap]. Our [Module B/C] addresses this by [mechanism]."

> Source: BV1rPGdz3E2V (005), BV1fW4y1W7dS

### Connecting Each Paragraph to Your Method

Three connection strategies:

1. **Problem lead-in**: End each paragraph by naming a limitation your method addresses
2. **Method bridge**: End with a hint at your approach ("This motivates us to integrate [module]")
3. **Gap escalation**: Limitations compound to create urgency for your method

### Different Evidence State Strategies

| Situation | Strategy |
|-----------|----------|
| Heavy borrowing from one source | Dedicate a full paragraph; be explicit about modifications |
| Modules from diverse sources | Group by function, not source; show they haven't been combined before |
| Prior work very close to yours | Acknowledge similarity; position your specific difference |

### Common Mistakes

1. **Paper-order listing**: References 1, 2, 3... without thematic organization
2. **No argumentative thread**: Summarizing papers without connecting to YOUR work
3. **Including irrelevant work**: Every cited paper must relate to a module you use
4. **No logical transitions**: Paragraphs should flow with "Building on this," "In contrast"
5. **Exaggerating weaknesses**: Saying prior work "completely fails" when it merely has limitations
6. **Missing recent work**: Include papers from the last 2-3 years

### Chinese Academic Context

- In Chinese theses, related work often appears as a subsection of Chapter 1 ("国内外研究现状")
- The "总分分总" structure is standard in Chinese academic writing
- Each paper summary should be one sentence, connected by logical transitions
