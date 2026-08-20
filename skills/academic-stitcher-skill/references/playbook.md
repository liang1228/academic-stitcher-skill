# Research Planning Playbook

## Contents

1. Constraint intake
2. Comparable-paper matrix
3. Research architecture
4. Baseline gate
5. Module compatibility and change ledger
6. Evidence plan
7. Proposal/thesis planning
8. Grey vocabulary
9. Stop rules

## 1. Constraint Intake

Ask only questions that change the plan:

- What decision or deliverable is due, and when?
- What current official rule, venue, advisor, or collaboration constraint applies?
- What artifacts exist: papers, code, data, results, figures, draft, reviewer comments?
- What can actually be accessed and reproduced?
- Which evidence is reported, reproduced, proposed, or missing?
- What is the minimum viable research product if the preferred plan fails?

## 2. Comparable-Paper Matrix

| Paper/system | Task/setting | Baseline | Delta | Claimed mechanism | Data/protocol | Evidence | Reusable part | Provenance/risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Do not compare only paper titles or headline metrics. Record the conditions that make numbers comparable.

## 3. Research Architecture

Use this sentence as a test, not as mandatory prose:

`Under [setting], inherited approach [A] fails at [X]. We change [B] through [Y], which predicts [measurable effect Z]. We will test this under [protocol] and limit the claim to [boundary].`

Reject the architecture if any link is missing:

- X is not demonstrated or plausibly grounded.
- B cannot be implemented or attributed.
- Y does not predict an observable difference.
- Z cannot be measured fairly.
- The boundary is broader than the evidence.

## 4. Baseline Gate

| Check | Question | Decision |
| --- | --- | --- |
| Task fit | Same target and setting? | adopt / reference only / reject |
| Protocol fit | Compatible data, split, metric, preprocessing? | adopt / adapt with disclosure / reject |
| Availability | Code/data/materials available and permitted? | reproduce / request / replace |
| Reproduction | Can the claimed behavior be rerun? | formal baseline / reported reference |
| Currency | Does it cover strong current alternatives? | add comparator / justify scope |
| Resource fit | Can it be evaluated within budget? | adopt / reduce scope / reject |

When paper and reproduction values differ, keep both visible and investigate before comparing a new method.

## 5. Module Compatibility And Change Ledger

| Module | Source/license | Original input/output | New interface | Actual change | Mechanism | Falsifying test |
| --- | --- | --- | --- | --- | --- | --- |

Search may span general tools, the same domain, and a nearby domain, but transfer is justified by interface and mechanism—not name similarity.

Keep/drop rule:

- **Keep**: attributable, compatible, feasible, and independently testable.
- **Revise**: useful idea but interface, provenance, or mechanism is incomplete.
- **Drop**: unchanged relabeling, unavailable implementation, incompatible assumptions, or no fair falsifying test.

## 6. Evidence Plan

| Claim | Primary test | Comparator/control | Robustness/uncertainty | Cost/failure evidence | Stop/go rule |
| --- | --- | --- | --- | --- | --- |

Prefer tests that can disconfirm the story. If a module does not contribute, remove or reframe it. Do not redesign the ablation only to preserve the original claim.

## 7. Proposal And Thesis Planning

Separate two axes:

- **Contribution axis** — what new, bounded claim is supported and by which evidence.
- **Workload axis** — which complete research units and dependencies satisfy the current thesis process.

Modules, claimed innovations, papers, accepted papers, and workload units are not interchangeable counts.

For each milestone, specify:

| Gate | Required artifact | Evidence state | Allowed change | Approval/source |
| --- | --- | --- | --- | --- |

Use current institutional documents and recorded advisor decisions. Prior cohorts and informal counts are context, not policy.

## 8. Grey Vocabulary

| Phrase | Safe operational translation |
| --- | --- |
| A+B / 缝论文 | attributable reuse plus a meaningful change and fair evidence |
| 编故事 / 包装 | organize a problem–method–evidence narrative without changing facts |
| 保毕业 / 水论文 | minimum viable, defensible research under current formal requirements |
| 造航母 | resource-infeasible scope requiring reduction or a different topic |
| 降重 | clarify concepts and rewrite attributed material; never conceal copying |
| 只答不辩 | listen and record first, then verify and respond with evidence |

## 9. Stop Rules

Stop planning or drafting when:

- required evidence is being invented;
- provenance, permission, or authorship is unresolved;
- comparison depends on deliberately weaker treatment of alternatives;
- the proposed “novelty” is only renaming or undisclosed reuse;
- material negative evidence would need to be hidden;
- submission or similarity-detection evasion is requested.

Return the nearest compliant work package instead.
