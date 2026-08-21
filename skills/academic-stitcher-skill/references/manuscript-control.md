# Manuscript Control Reference

This is a reusable control layer for evidence-bound scientific writing. It is
distilled from multi-layer writing, review, and revision architectures. It is
not journal policy, a peer-review guarantee, or a substitute for field-specific
reporting requirements.

## When to load

Load this reference before substantive work when the task involves:

- creating or rebuilding a named section;
- restructuring, translating, or polishing a multi-round manuscript;
- deciding what belongs in the main text, a caption, Methods, source data, or SI;
- auditing reviewer concerns or preparing a revision-response matrix;
- placing observed experiment blocks into a paper or a full-pipeline manuscript phase.

For a short sentence-level edit with no change to argument, evidence, or
terminology, use only the relevant source-fidelity checks.

## 1. Alignment checkpoint before full prose

Create this compact record before drafting a full section or making a structural
rewrite:

| Field | Required content |
| --- | --- |
| bounded argument | `In [system/problem], we show or test [advance] using [approach], supported by [evidence], with [boundary]` |
| primary reader question | The first decision the reader must be able to answer, such as relevance, novelty, trust, reuse, or meaning |
| section and paragraph map | One job per paragraph, with the lead result or transition named |
| terminology lock | Canonical names for methods, models, datasets, metrics, variables, and abbreviations |
| lead evidence | The result or source block that carries the central inference, with its evidence state |
| assumptions | Inferred framing choices, target audience, venue, word limit, or result ordering |

Decision rules:

1. **Proceed** when the central claim, evidence, boundary, terminology, and
   section job are explicit and no high-leverage assumption remains.
2. **Confirm** when the work is otherwise feasible but the lead claim, reader,
   terminology, result ordering, or paragraph architecture is ambiguous. Show the
   compact record and ask at most three targeted questions before full prose.
3. **Hold** when central evidence, provenance, permission, or a required
   boundary is missing. Return a bounded outline or placeholder instead of prose
   that sounds complete.

Do not use a confirmation request to ask about details that are already clear.
Do not continue into a full draft after a `confirm` or `hold` decision unless the
user supplies the decision or explicitly authorizes the bounded checkpoint.

## 2. Terminology ledger

Lock vocabulary before drafting and update it deliberately during revision:

| Concept | Canonical form | Forbidden or ambiguous variants | Definition / distinction | First-use location | Status |
| --- | --- | --- | --- | --- | --- |
| method or model |  |  |  |  | proposed / locked |
| dataset or sample |  |  |  |  | proposed / locked |
| metric or statistic |  |  |  |  | proposed / locked |
| variable or physical object |  |  |  |  | proposed / locked |
| abbreviation or symbol |  |  |  |  | proposed / locked |

One name must not silently alternate between two concepts. A variant may remain
only when it is a real distinction, and that distinction must be recorded. A
translation or polish pass preserves the ledger unless the user explicitly
changes the terminology.

## 3. Result allocation and the shortest sufficient chain

Classify a result by its function in this paper, not by the name of the analysis:

| Class | Keep or route when | Default destination |
| --- | --- | --- |
| `core_discovery` | Advances the central conclusion | Main text |
| `necessary_support` | The reader needs it to accept the core result | Main text, concise |
| `qualification` | Changes the scope, direction, or interpretation | Main text when material, otherwise SI |
| `robustness` | Tests an alternate seed, estimator, threshold, or specification without changing the conclusion | SI with a stable pointer |
| `heterogeneity` | Variation is itself part of the central claim | Main text when central, otherwise SI |
| `provenance_detail` | Documents data, preprocessing, implementation, or traceability | Methods, source data, repository, or SI |
| `alternative_inference` | Tests the same claim through another inferential route | SI unless it changes acceptance of the claim |
| `edge_case` | Defines a failure boundary that changes how the claim must be read | Main text when material, otherwise SI |

Then build the minimum ordered chain that lets the reader understand the
observation, see the decisive comparison or mechanism evidence, judge the main
uncertainty, and understand any conclusion-changing boundary. Keep the complete
analysis record available, but do not compress away contradictory or
conclusion-changing evidence.

Use the following placement rule:

- **Main text** states what was found, the decisive support, and what it means.
- **Caption** defines what the display shows and how to read it.
- **Methods/source data** preserves reproducibility and provenance detail.
- **SI or appendix** carries non-central robustness, extended diagnostics, and
  implementation detail with stable pointers.

Every new sentence must pass a deletion check: state its function, locate an
existing sentence with the same function, and prefer replacement, combination,
compression, or relocation before appending.

## 4. Consistency sweep after multi-round editing

This is a retrospective audit. It does not replace the preventive terminology
ledger. Inspect findings before changing text; mechanical counts are detectors,
not automatic corrections.

Run the passes in this order:

1. **Numbers and design reconciliation** — sample counts, factors, splits,
   denominators, metric precision, intervals, units, and table-to-text values.
2. **Claims versus the paper's own evidence** — superlatives, causal verbs,
   generalization, exceptions, overlapping uncertainty, and abstract/conclusion
   summaries.
3. **Terminology and notation** — method names, acronyms, variables, physical
   objects, statistics, capitalization, spelling, tense, and hyphenation.
4. **Cross-references and placement** — figures, tables, equations, captions,
   Methods, source data, SI, and downstream documents such as response letters.
5. **Redundancy** — prose that repeats a display or a nearby sentence without
   adding evidence, boundary, or interpretation.

Each finding records `location`, `observed variants`, `likely distinction`,
`evidence to inspect`, `decision`, and `verification`. Do not normalize two
terms merely because they look similar. Do not report a headline as consistent
until it can be derived from the stated design and the authoritative table or
artifact.

## 5. Independent review and synthesis boundary

When the route asks for multiple review lenses:

1. Build one immutable packet from the supplied artifact, verified anchors,
   assessment boundary, missing-file inventory, and common criteria.
2. Define each lens before reading or drafting its findings. Do not put a shared
   interpretation or another lens's concerns into the packet.
3. Record each issue with a stable local ID, severity, `claim_pointer`,
   `evidence_pointer`, why it matters, and a resolution test.
4. Freeze each lens report before synthesis. Preserve genuine overlap and
   disagreement; do not edit reports to create artificial diversity.
5. Synthesize only after freezing. A consensus label requires independently
   grounded support from more than one lens; a consequential single-lens concern
   remains visible with its provenance.

If the environment cannot provide separate contexts, label the result as a
same-context multi-lens audit. Never call it mutually blind peer review.
Do not invent reviewer identities, missing locations, editor decisions, or
concerns merely to fill a quota.

## 6. Revision action and readiness tracker

Map every reviewer or advisor item to an action, work status, evidence, and
readiness. Keep the following dimensions separate:

| Dimension | Examples |
| --- | --- |
| action | `ACCEPT_TEXT`, `CLARIFY_EXISTING`, `ADD_CITATION`, `SOFTEN_CLAIM`, `ACCEPT_ANALYSIS`, `ACCEPT_EXPERIMENT`, `PARTIAL`, `DISAGREE`, `OUT_OF_SCOPE`, `AUTHOR_INPUT_NEEDED`, `BLOCKING` |
| work status | `VERIFIED_DONE`, `REPORTED_DONE_UNVERIFIED`, `TODO_TEXT`, `TODO_ANALYSIS`, `TODO_EXPERIMENT`, `TODO_AUTHOR_CONFIRM`, `NOT_FEASIBLE`, `PROPOSED_DISAGREEMENT` |
| verification | Inspectable revised text, analysis output, figure/table, source record, approval, or explicit absence |
| package readiness | `ready_to_submit`, `draft_with_placeholders`, `needs_author_input`, or `blocked` |

`VERIFIED_DONE` requires an inspectable artifact and a location or record that
can be checked. A drafted reply is not proof that a manuscript or experiment
changed. If the author reports completion without the artifact, use
`REPORTED_DONE_UNVERIFIED`. Use `ready_to_submit` only when no blocker or
placeholder remains and every claimed completed action is verified.

## 7. Compact audit record

For a full section, Results restructure, or revision package, preserve at least:

- the alignment decision and terminology lock;
- the source/claim/evidence trace;
- the result-allocation and shortest-chain record when applicable;
- the deletion or relocation log;
- consistency findings and their verification state;
- reviewer or revision issue IDs, action, work status, and readiness;
- the exact unresolved input and the next observable checkpoint.

The prose remains the deliverable. The audit record is the smallest trail needed
to show why a sentence, result, concern, or status is allowed to appear.
