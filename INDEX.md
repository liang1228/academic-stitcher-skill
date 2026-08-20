# Academic Research Planning Skills — Index

> One evidence-bound core plus five independent specialist skills for research stories, research planning, evidence decomposition, architecture boundaries, module adaptation, and paper delivery.

## Shared material

- [Method digest](./DIGEST.md)
- [Shared glossary](./GLOSSARY.md)

## Skill list

### Core story and manuscript workflow

- [academic-stitcher-skill](./skills/academic-stitcher-skill/SKILL.md): route hybrid-paper stories, section construction, structural polishing, reviewer audit, proposals, and full research-to-paper workflows.

### Direction and feasibility

- [direction-feasibility-foundation-map](./skills/direction-feasibility-foundation-map/SKILL.md): evaluate activity, foundations, support, resources, and minimum-pilot gates.

### Paper evidence and research architecture

- [purpose-driven-paper-decomposition](./skills/purpose-driven-paper-decomposition/SKILL.md): extract task, baseline, module, interface, and experiment evidence according to the reading goal.
- [variable-granularity-abc-research-architecture](./skills/variable-granularity-abc-research-architecture/SKILL.md): distinguish inherited, changed, added, and historically attributed components at the current granularity.

### Module transfer and dataflow

- [three-domain-module-search-dataflow-adaptation](./skills/three-domain-module-search-dataflow-adaptation/SKILL.md): search candidates across three domain scopes and validate B-prime/C-prime adaptation along the real dataflow.

### Contribution and delivery

- [innovation-workload-dual-axis](./skills/innovation-workload-dual-axis/SKILL.md): map contribution evidence and auditable workload to experiments, chapters, and delivery objects on separate axes.

## Recommended sequence

1. If the user asks for a research story, manuscript structure, review, or full workflow, start with academic-stitcher-skill.
2. If the direction or resources are uncertain, use direction-feasibility-foundation-map.
3. If the paper set is known, use purpose-driven-paper-decomposition to freeze the reading goal and evidence.
4. If inherited and new work are mixed, use variable-granularity-abc-research-architecture.
5. If the baseline is stable and a module must be transferred, use three-domain-module-search-dataflow-adaptation.
6. If the architecture is bounded and delivery must be planned, use innovation-workload-dual-axis.

## Relationship map

`mermaid
graph LR
    S["Research story/writing core"] -->|orchestrates| F["Direction feasibility"]
    S -->|orchestrates| P["Purpose-driven decomposition"]
    S -->|orchestrates| A["Variable-granularity A/B/C"]
    S -->|orchestrates| M["Three-domain module adaptation"]
    S -->|orchestrates| W["Innovation/workload dual axis"]
    F["Direction feasibility"] -->|composes-with| P["Purpose-driven decomposition"]
    F -.->|contrasts-with| P
    P -->|depends-on| A["Variable-granularity A/B/C"]
    P -->|composes-with| M["Three-domain module adaptation"]
    A -->|composes-with| M
    A -->|composes-with| W["Innovation/workload dual axis"]
    W -->|depends-on| A
`

## Shared operating rules

- A relationship in this map is a routing aid, not a claim that one skill can complete the next skill's work.
- Every result should show evidence state, unresolved assumptions, rights or access constraints, and the next verification action.
- Missing formal rules remain pending; no experience-based threshold can substitute for a current formal requirement.
- The skills are not institutional policy, publication guarantees, or independent experimental proof.

Each skill keeps its own trigger tests and validation record under skills/<skill-name>/.
