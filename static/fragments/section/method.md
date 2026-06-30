# Section: Method

## Job
Explain how the proposed delta enters the inherited baseline and why it should address the failure mode.

## Structure
1. Problem formulation.
2. Baseline recap.
3. Overall pipeline.
4. Proposed delta with input/output and placement.
5. Objective, training, inference, or algorithm.
6. Complexity and implementation details.

## Checks
- Define symbols before use.
- Name module compatibility with the baseline.
- Connect each design choice to a measurable claim.

## Data-Flow Description Pattern (Video-Derived)
Describe the model along the data flow (input to output) using "先总后分" (general-first, then specific).

### Section Layout
| Subsection | Content | Style |
|------------|---------|-------|
| Overview (3.1) | Name model, list components, reference figure | Storytelling |
| Module A (3.2) | Input -> processing -> output with formulas | Objective facts |
| Module B (3.3) | Input -> processing -> output with formulas | Objective facts |
| Module C (3.4) | YOUR modification -- the innovation point | Storytelling |
| Loss/Training (3.5) | Loss function, optimizer, training details | Formulas |
> Source: BV1ut34zuEfS (013), BV1Lgt7eMEZd, BV1cpx7eGEyY, BV1fW4y1W7dS

### Overview Template
"Our proposed [Method Name] consists of [N] components: [A], [B], [C], and [D]. As shown in Fig. X, given input [X], we apply [A] to [purpose]. The output passes to [B] which [mechanism]. Finally, [C] produces the final [output]."

### Module Description (Input -> Process -> Output)
"Given input X = {x1, x2, ...}, [Module] performs [operation] to obtain Y.
    Y = f(X; theta)                          (Eq. N)
where [define variables]. [Plain-text explanation]."
> Source: BV1cpx7eGEyY, BV1fW4y1W7dS

### Borrowed vs Novel Modules
| Module Type | Strategy | Citation |
|-------------|----------|----------|
| Borrowed (unchanged) | Brief + cite; skip for short papers | Cite original |
| Borrowed with modification | Describe original, then state change | Cite + note |
| Novel (your contribution) | Full: motivation, math, rationale | Your own |
> Source: BV1ut34zuEfS (013), BV1Lgt7eMEZd

### Formula Rules
- Define every symbol before first use; number equations sequentially
- Follow each formula with "where X denotes..., Y represents..."
- Common modules (Transformer, LayerNorm) need not be re-derived

### Evidence State Strategies
| State | Strategy |
|-------|----------|
| Mostly borrowed | More time on overview motivation; novelty is the combination |
| One strong novel module | Allocate most space to it; borrowed modules brief |
| Multiple small modifications | Frame as "refinement"; novelty is the combination |

### Common Mistakes
1. **Jumping into details**: Start with overview and architecture figure
2. **No architecture figure**: Mandatory for journals and theses
3. **Describing generic modules**: Do not explain Transformer -- cite or put in Ch. 2
4. **No connection to problem**: Each module should reference which problem it addresses

### Chinese Academic Context
- Chinese theses: "总体思路" (overall approach) + "模型结构" (model structure)
- Architecture figure must be vector graphic, never a screenshot
- "本章小结" must restate what the model does and why
