# Section: Title

## Job

Signal the task, method or finding, and scope without overclaiming.

## Checks

- Avoid vague novelty words.
- Keep the core object visible.
- If the result is bounded, include the setting or population.
- For thesis/proposal work, prefer clear scope over journal-style compression.

## Naming Patterns (Video-Derived)

### Common Title Structures

| Pattern | Template | Example |
|---------|----------|---------|
| Method + Task | `[Method] for [Task]` | Dual-Concept Detection for Video Captioning |
| Method + Task + Domain | `[Method] for [Task] in [Domain]` | Attention-Augmented VLP for Medical Image Retrieval |
| Finding-led | `[Finding]: [Method] for [Task]` | Beyond Averaging: Weighted Ensemble for Cross-Modal Retrieval |
| Module-led | `[Module Name]: [Subtask] with [Technique]` | DCD: Dual Concept Detection via Contrastive Learning |

> Source: BV1rDMHzTEEd (011), BV1W5EAzLErh (007)

### What Makes a Good vs Bad Title

**Good titles:**
- Make the core module or technique name visible (e.g., include your renamed B or C module)
- Signal scope (dataset, domain, task) so readers can self-select
- Use the naming convention of the target journal/conference
- If the method name is novel (e.g., you renamed DCD to ECD), put it first

**Bad titles:**
- Overclaim with words like "universal", "general-purpose", "complete solution" without evidence
- Hide the core object behind abstraction
- Use vague novelty words: "novel", "advanced", "improved" without specifying what
- Copy the title structure of a single paper too closely (signals potential plagiarism)

> Source: BV1npKfzPEuC (012), BV1W5EAzLErh (007)

### Module Naming Strategy

- When you modify someone else's module, add a "prime" or swap one letter to distinguish: DCD becomes ECD, TSN becomes TSN+
- The change can be small (e.g., replacing mean pooling with weighted pooling) -- the name signals novelty regardless
- The renamed module should appear in the title or abstract to anchor your contribution
- In Chinese academic context, the module name often becomes the thesis title anchor for defense presentations

> Source: BV1W5EAzLErh (007), BV1npKfzPEuC (012)

### How to Signal Scope

- If your work targets a specific subtask (e.g., video captioning, not all video understanding), state it explicitly
- For conference papers (7 pages), scope is narrow by design -- title should match
- For journal papers (11+ pages), a slightly broader scope framing is acceptable
- For thesis work, prefer clear scope over journal-style compression -- the title should match Chapter 3/4 content

### Common Mistakes

1. **Title too broad**: "A Deep Learning Approach for Video Understanding" -- scope is undefined
2. **Title too narrow**: "Fine-Tuning CLIP on MSVD with Cosine Similarity" -- reads like a lab log
3. **No method signal**: "Video Captioning Revisited" -- reader cannot tell what you contributed
4. **Reusing baseline title pattern**: If CLIP4Caption exists, do not title your paper "CLIP4Caption-Plus"
