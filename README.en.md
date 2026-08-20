# Academic Research Planning Skills

A set of independently installable and composable Codex skills for turning research ideas, paper evidence, module transfer, and thesis delivery into auditable work plans.

## Five entry skills

1. [direction-feasibility-foundation-map](./skills/direction-feasibility-foundation-map/SKILL.md): assess direction feasibility, foundations, support, resources, and minimum-pilot exit gates.
2. [purpose-driven-paper-decomposition](./skills/purpose-driven-paper-decomposition/SKILL.md): decompose papers by research purpose into tasks, baselines, modules, interfaces, and experiment evidence.
3. [variable-granularity-abc-research-architecture](./skills/variable-granularity-abc-research-architecture/SKILL.md): redraw A/B/C around the current claim and separate inherited, changed, and new work.
4. [three-domain-module-search-dataflow-adaptation](./skills/three-domain-module-search-dataflow-adaptation/SKILL.md): search across general, in-domain, and adjacent domains while checking dataflow and train/deploy contracts.
5. [innovation-workload-dual-axis](./skills/innovation-workload-dual-axis/SKILL.md): map innovation evidence and auditable workload to experiments, chapters, and delivery requirements on separate axes.

## Recommended order

1. Choosing a direction: direction-feasibility-foundation-map
2. Working from concrete papers: purpose-driven-paper-decomposition
3. Freezing a baseline and contribution boundary: variable-granularity-abc-research-architecture
4. Transferring modules: three-domain-module-search-dataflow-adaptation
5. Planning paper or thesis delivery: innovation-workload-dual-axis

Each skill can be copied into a Codex skills directory independently or composed through the dependency relationships described below.

## Repository layout

~~~text
.
├── README.md
├── README.en.md
├── INDEX.md
├── DIGEST.md
├── GLOSSARY.md
└── skills/
    ├── direction-feasibility-foundation-map/
    ├── purpose-driven-paper-decomposition/
    ├── variable-granularity-abc-research-architecture/
    ├── three-domain-module-search-dataflow-adaptation/
    └── innovation-workload-dual-axis/
~~~

Each skill directory contains:

- SKILL.md: runtime rules, trigger boundaries, and execution steps
- agents/openai.yaml: display name and default invocation prompt
- test-prompts.json: trigger, decoy, and boundary cases
- test-results.md: independent routing validation results

## Output contract

All five entry skills require the user to:

- freeze the decision and comparison object for the current task;
- separate facts, assumptions, pending checks, and stop conditions;
- keep evidence, rights, versions, interfaces, changes, controls, and ablations auditable;
- avoid turning metric gains, paper counts, or experience-based claims into automatic contribution, policy, or guarantees;
- report missing inputs and next actions instead of fabricating a conclusion.

## Public boundary

This repository provides executable work frameworks. It does not replace institutional rules, journal requirements, legal review, or real experiments. Current rules, rights, data, code, and reproducibility conditions must be checked against the latest authoritative material. No local paths, raw caches, internal audit files, or unprocessed intermediate artifacts are included.

## Validation

All five skills pass structural validation. Each skill passes its six routing cases, for 30/30 overall.

See [INDEX.md](./INDEX.md) for the relationship map and learning order, [DIGEST.md](./DIGEST.md) for the method digest, and [GLOSSARY.md](./GLOSSARY.md) for shared terminology.
