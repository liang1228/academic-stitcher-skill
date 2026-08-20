# Manuscript Writing And Review Suite

## Contents

1. Source trace
2. Story spine
3. Section jobs
4. Evidence-dependent writing order
5. Paragraph construction
6. Structural polishing
7. Multi-lens review
8. Revision-response matrix
9. Whole-document consistency

## 1. Source Trace

Build before adding concrete details:

| Source/artifact | Exact support | Planned sentence/claim | Evidence state | Boundary |
| --- | --- | --- | --- | --- |

Allowed states: `supplied`, `reported`, `reproduced`, `inferred`, `proposed`, `missing`.

## 2. Story Spine

Before drafting sections, write one bounded argument:

`pressure -> inherited baseline -> failure mode -> gap -> design principle -> mechanism -> prediction -> evidence -> boundary`

For a hybrid paper, keep a second ledger:

| Story link | Component/paper | Actual support | State | What would falsify or narrow it? |
| --- | --- | --- | --- | --- |

Do not fill a missing transition with stronger prose. If a module has no failure mode, mechanism, or independent evidence, keep it out of the central claim or label it as a proposed exploratory branch.

Once the spine is accepted and the user asks how to test it, hand off to `claim-driven-experiment`: convert each central link into a claim, primary test, control/ablation, failure interpretation, and paper placement before drafting result prose.

## 3. Section Jobs

| Section | Primary job | Common failure |
| --- | --- | --- |
| Title | signal object, move/finding, and scope | unsupported novelty or hidden object |
| Abstract | compress gap, approach, material evidence, boundary | proposal written as completed result |
| Introduction | justify the study from sourced gap | problem invented after module selection |
| Related Work | establish lineage, close overlap, unresolved gap | favorable paper list or paper-order dump |
| Method | expose inheritance, change, interface, procedure | inherited work presented as new |
| Experiments | test claims fairly and transparently | weak baselines, hidden cost, non-comparable metrics |
| Discussion | interpret, compare explanations, bound claims | causal overreach or buried negative evidence |
| Conclusion | state supported finding and limit | new claim or expanded scope |

## 4. Evidence-Dependent Writing Order

There is no universal section order. Choose by evidence state:

- **Completed study**: freeze method/protocol and results first; then write interpretation, introduction, abstract, and conclusion.
- **Proposal**: write problem, constraints, planned method, and evidence plan in future tense; do not manufacture a results section.
- **Revision**: update the evidence and claim maps before polishing affected prose.
- **Translation/polish**: source trace and terminology ledger precede rewriting.

## 5. Paragraph Construction

Each paragraph has one job:

`topic claim -> support -> interpretation/connection -> boundary or transition`

Not every paragraph requires all four sentences, but each concrete statement must keep its evidence state. Split paragraphs that carry unrelated jobs.

## 6. Structural Polishing

Run passes in this order:

1. section job and argument order;
2. paragraph roles and transitions;
3. claim strength versus evidence;
4. terminology, notation, units, and citation anchors;
5. sentence clarity, concision, and grammar.

Maintain a change log:

| Change | Level | Reason | Scientific meaning preserved? | Needs author check? |
| --- | --- | --- | --- | --- |

## 7. Multi-Lens Review

Run independently:

- methodology: design, controls, metrics, statistics, reproducibility, cost;
- domain: relevance, terminology, comparators, close prior work, venue fit;
- skeptical: alternative explanations, overclaims, failure cases;
- integrity: provenance, citations, reuse, data, authorship, material counterevidence;
- editorial synthesis: priority and minimal correction path.

Severity levels:

- **blocker** — invalidates a central claim, comparison, provenance, or submission requirement;
- **major** — materially weakens interpretation or reproducibility;
- **minor** — clarity, presentation, or local completeness;
- **suggestion** — optional improvement.

## 8. Revision-Response Matrix

| Comment | What it asks | Validity | Action | Evidence | Changed location | Response status |
| --- | --- | --- | --- | --- | --- | --- |

- Copy the comment accurately.
- State what changed and where only after the change exists.
- For disagreement, use data, literature, rule text, or a scoped alternative.
- Professional tone does not require accepting an incorrect or unethical request.
- Do not add irrelevant citations or conceal unavailable materials to appear compliant.

## 9. Whole-Document Consistency

Before delivery, check:

- title/abstract/introduction/conclusion claim scope;
- terminology, notation, dataset, metric, and sample counts;
- method implementation versus diagrams and formulas;
- experiment tables versus prose and appendix;
- reported versus reproduced results;
- contribution statements versus provenance ledger;
- limitations and material negative results;
- venue/institution disclosures and required files.
