# Process Contract

This skill is a gated research workflow, not a free-form academic text generator. Every call follows the lifecycle below, even when the user asks for a small subtask. A small request may stop early; it must not silently skip the gates that determine whether the requested work is defensible.

## Meaning Of Complete

“Complete” means that every required gate up to the user-authorized checkpoint has passed and the resulting artifact is identified. It does **not** mean that an unrun experiment, unverified citation, accepted paper, or successful submission exists.

The skill must always distinguish:

- **planned work** from executed work;
- **source-reported** from locally reproduced evidence;
- **observed metrics** from causal or mechanistic interpretation;
- **a route artifact** from the next route's artifact;
- **a held checkpoint** from a failed task.

## Gated Lifecycle

Use these stage names and transition rules in `## Process Status`:

| Stage | Required decision or artifact | May advance only when |
| --- | --- | --- |
| `S0 scope` | Domain fit, user authorization, deliverable, and stopping point | The task is in scope and the authorized checkpoint is explicit |
| `S1 intake` | Axis line, artifact inventory, constraints, and access limits | The inputs that can change the decision are listed |
| `S2 route-lock` | One primary route, collision decision, and any handoff | The route matches the requested behavior and neighboring routes are ruled out |
| `S3 evidence-ledger` | Claim/evidence/provenance ledger with states and missing fields | Every concrete fact has a state and a trace or is marked `missing` |
| `S4 integrity-gate` | Attribution, license, authorship, fairness, leakage, and reporting checks | No hard stop remains unresolved |
| `S5 architecture` | Bounded claim, failure mode, mechanism, prediction, alternatives, and artifact map; for manuscript work, the alignment checkpoint and terminology lock | The requested plan or writing target has a defensible spine and no unresolved high-leverage framing assumption |
| `S6 authorized-work` | The requested plan, draft, audit, or deterministic package action | The output stays inside the authorized checkpoint and actual run state |
| `S7 independent-audit` | Applicable quality gates, skeptical alternatives, and unresolved risks | Findings are either resolved, explicitly held, or converted to a narrower claim |
| `S8 delivery-stop` | Contract-compliant artifact, process card, decision, and next checkpoint | The response states what is done, what is not done, and where work stops |

### Transition rules

1. `S0` through `S4` are mandatory for every in-scope call. A route may mark a stage `not_applicable` only with a reason in the process card.
2. `S5` and `S6` use the selected route's procedure. A section rewrite uses source-meaning lock as its architecture artifact; a reviewer audit uses an issue taxonomy as its architecture artifact; a skill audit uses the deterministic audit target as its architecture artifact.
3. `S7` is mandatory before claiming a route artifact is ready for downstream use. A small wording edit may use a lightweight source-fidelity audit, but may not claim scientific validation.
4. For a full section or structural rewrite, `S5` must record `proceed`, `confirm`, or `hold` from the alignment checkpoint. `confirm` pauses before full prose; `hold` returns a bounded outline or placeholder.
5. Any unresolved blocker changes the stage to `hold` or `blocked`; it does not get repaired by stronger prose.
6. A failed gate sends work to the smallest applicable recovery stage: missing input to `S1`, route ambiguity to `S2`, unsupported claim to `S3`/`S5`, integrity or fairness failure to `S4`, and failed evidence to `S5`.
7. `full-pipeline` orchestrates these stages but cannot report later stages as complete merely because an earlier plan exists.

## Scope And Action Boundary

| Area | Allowed | Not allowed as an unmarked substitute |
| --- | --- | --- |
| Academic research | Plan, decompose, compare, design evidence, structure a story, draft from supplied artifacts, polish, audit, and prepare a bounded proposal | Turning a module list into novelty by declaration |
| Evidence | Inspect supplied artifacts, label states, identify missing evidence, and design reproducible tests | Inventing data, citations, scores, significance, seeds, mechanisms, authorship, or review outcomes |
| Hybrid or “stitched” work | Record source, license, original role, interface change, mechanism, and falsifying test | Hidden reuse, copied text/code/figures, or unequal treatment of a comparator presented as a new contribution |
| Experiments | Specify protocol, controls, ablations, run order, decision gates, and result-state updates | Pretending to run remote jobs, deploy code, observe results, or reproduce a paper without execution evidence |
| Manuscript writing | Organize supplied facts, use placeholders, preserve terminology, and calibrate claim strength | Adding unsupported numbers, causal language, citations, or “completed” results for narrative flow |
| Review and rebuttal | Separate findings, request evidence, narrow claims, and prepare a factual response matrix | Guaranteeing acceptance, fabricating reviewer history, or claiming a fix before it exists |
| Thesis/proposal | Map contribution, workload, dependencies, and formal checkpoints | Treating informal advice or an unverified rule as institutional policy |
| Skill maintenance | Run deterministic package checks and report actual model/API evaluation states | Treating file validation as self-play, judge, replay, or scientific success |

The package may read local, user-supplied artifacts and run explicitly requested deterministic package checks. It does not silently cross into remote execution, deployment, submission, authorship changes, or publication decisions.

## Required Process Card

Every route response begins with the compact route line and then includes this block immediately after `## Route`:

```text
## Process Status
- Stage: <S0-S8 name>
- Authorized checkpoint: <the exact deliverable allowed now>
- Inputs and evidence coverage: <supplied/reported/reproduced/inferred/proposed/missing>
- Executed in this response: <observable actions and artifacts>
- Not executed: <experiments, retrieval, deployment, submission, or later stages not run>
- Gate: <pass | hold | blocked | not_applicable + reason>
- Next checkpoint: <one observable artifact or decision>
```

Use `hold` when the user can continue after supplying an input or decision. Use `blocked` when an integrity, provenance, fairness, or access condition prevents the requested work. Use `not_applicable` only for a route-specific stage with an explicit reason; never omit the status silently.

## Alignment Checkpoint

Before full manuscript prose or a structural rewrite, the `S5 architecture`
artifact must contain:

- one bounded argument sentence;
- the primary reader question and section/paragraph map;
- a terminology ledger for the names that can propagate across sections;
- the lead evidence block and its evidence state;
- explicit assumptions about framing, result order, venue, or word limit.

If any high-leverage item is ambiguous, emit the alignment record and stop at
`confirm`. If central evidence, provenance, permission, or a conclusion-changing
boundary is absent, stop at `hold`. A full draft is allowed only after the user
confirms the record or the input is genuinely unambiguous.

## Stop And Reflux Rules

- **Missing source or result** → stop before concrete prose; create a bounded placeholder and list the smallest missing input.
- **Unresolved provenance, permission, or authorship** → hold at `S4`; create a provenance/permission checkpoint.
- **Incompatible or unfair comparison** → hold at `S4`; repair the protocol or label the result as non-comparable.
- **No demonstrated failure mode or mechanism** → hold at `S5`; return to decomposition or narrow the claim.
- **Failed, unstable, or inconclusive experiment** → keep the run visible; narrow the claim, remove/revise the module, revise the mechanism, or reopen the missing-input gate.
- **User asks to jump from a topic to finished results or a submission-ready paper** → complete only the authorized planning checkpoint and show the blocked downstream stages.
- **Full-section request has an ambiguous lead claim, terminology, or result order** → return the alignment checkpoint and stop before full prose.
- **Multi-round manuscript has unreconciled numbers or internal summaries** → hold final delivery until the consistency finding is resolved or explicitly carried as a limitation.
- **Non-academic or unrelated request** → do not force a route; state the scope mismatch and stop.

## Handoff Protocol

Route handoffs carry a named artifact, not a vague suggestion:

| From | To | Required handoff artifact |
| --- | --- | --- |
| `stitch-plan` | `story-architecture` | Traceable component map plus a proposed problem/failure/gap chain |
| `story-architecture` | `claim-driven-experiment` | Accepted bounded claim, anti-claims, mechanism, predictions, and boundaries |
| `claim-driven-experiment` | `section-draft` | Result-state ledger, claim-to-evidence matrix, and paper-placement map |
| Any route | `reviewer-audit` | The actual artifact plus its evidence/provenance ledger |
| Any route | `full-pipeline` | Current stage, completed gates, held gates, and next observable checkpoint |
| Skill package work | `ctx2skill-audit` | Exact package snapshot, deterministic checks, fixture set, and model/API run record if any |

Do not draft the downstream artifact in the same response unless the user explicitly authorizes that handoff and the upstream gate has passed.
