# Route: story-architecture

Use when the user wants to build or repair a defensible research story: combine multiple papers or modules around one problem, explain why a hybrid design is necessary, organize an Introduction/Method/Discussion argument, or turn an evidence set into a coherent claim progression.

This route organizes facts; it does not manufacture a motivating problem after seeing a favorable result. “Story” means a problem–method–evidence argument with visible uncertainty and attribution.

## Procedure

1. **Freeze the audience and decision**
   - Record the reader, venue or thesis checkpoint, paper type, current evidence state, and the one decision the story must support.
   - If the user has only a topic or module list, keep the central claim `proposed` and do not write completed-result language.

2. **Build the story spine**
   - `situation/pressure -> inherited baseline -> concrete failure mode -> unresolved gap -> design principle -> delta/module -> mechanism -> measurable prediction -> evidence -> boundary`.
   - For a hybrid paper, attach every inherited component to its source and every new or adapted component to an actual change and a validation item.
   - A component may enter the method only when its role in the spine is more specific than “it improved the score”.

3. **Separate claim states**
   - Mark each link `supplied`, `reported`, `reproduced`, `inferred`, `proposed`, or `missing`.
   - Keep author claims, reproduced results, structural hypotheses, and future experiments in separate rows.
   - If the failure mode, mechanism, or attribution cannot be supported, narrow the story or return to the missing evidence instead of smoothing the transition.

4. **Map the argument to the paper**
   - Introduction: pressure, failure, gap, and the bounded question.
   - Related Work: lineage and why the selected combination closes a specific gap rather than a paper list.
   - Method: inherited A, changed B/C, interfaces, mechanism, and prediction.
   - Experiments: one claim per primary control, ablation, robustness/cost check, or failure case.
   - Discussion/Conclusion: interpretation, alternative explanations, limitations, and the exact claim that remains supported.

5. **Run the reviewer stress test**
   - Remove each module mentally: does the stated failure or prediction change?
   - Ask whether the gap was selected after the result, whether another explanation fits the result, whether a baseline received unequal treatment, and whether a negative result was omitted.
   - Check that every transition has a citation, artifact, experiment, or explicit `missing`/`proposed` label.

6. **Stop at the authorized checkpoint**
   - Return a spine and section/experiment map when the user asks for architecture.
   - Draft prose only when the user explicitly requests a named section and supplies enough evidence; then hand off to `section-draft`.

## Handoffs

- If the papers have not been decomposed into traceable components, request or hand off to `purpose-driven-paper-decomposition` before fixing the story.
- If the inherited/new boundary is unstable, use `variable-granularity-abc-research-architecture` before writing contribution language.
- If a transferred module's interface or train/deploy contract is unresolved, use `three-domain-module-search-dataflow-adaptation` before treating it as part of the mechanism.
- If the story is being used to plan thesis workload or chapters, add `innovation-workload-dual-axis` after the claim boundary is frozen.

## Contract

Use the `story-architecture` headings from `static/core/output-format.md` exactly. The first line must identify the route and axes. `## Story Spine` must contain one bounded central claim plus the chain that supports it. `## Claim-Evidence-Boundary Map` must distinguish missing evidence from proposed work. `## Reviewer Stress Test` must include at least one alternative explanation or failure condition for a hybrid claim.

## Boundary

- Do not turn “编故事/包装” into fabricated significance, hidden reuse, selective reporting, or post-hoc motivation.
- Do not treat a better aggregate metric as proof that every module or mechanism belongs in the story.
- Do not use this route for fiction, general presentation storytelling, ordinary translation, or sentence-level polishing.
- If the user asks for a named section after the spine is accepted, use `section-draft` with the story map as its approved plan.
