# academic-stitcher-skill

> English README | [中文说明](README.md)

`academic-stitcher-skill` is a structured Codex skill for academic paper planning, manuscript drafting, Nature-style polishing, and reviewer-facing self-audit. It turns papers, baselines, modules, thesis constraints, draft sections, and experiment results into a defensible problem-mechanism-evidence narrative.

The repository follows the router-style design of [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills): a lean `SKILL.md`, a declarative `manifest.yaml`, always-loaded `static/core` files, task-specific `static/fragments`, and deeper `references` loaded only when needed. It also preserves the local distilled knowledge from paper-stitching and graduate-research planning materials.

## Table Of Contents

- [Design Goals](#design-goals)
- [Repository Layout](#repository-layout)
- [Skill Flow](#skill-flow)
- [Routes](#routes)
- [Typical Use Cases](#typical-use-cases)
- [Out Of Scope](#out-of-scope)
- [Installation](#installation)
- [Validation](#validation)
- [Output Contract](#output-contract)
- [Design Lineage](#design-lineage)
- [Maintenance Rules](#maintenance-rules)

## Design Goals

- **Structured skill flow**: route paper planning, section drafting, Nature-style polishing, reviewer audit, and full-pipeline work explicitly.
- **Progressive disclosure**: keep `SKILL.md` compact and load only the fragments relevant to the current request.
- **Evidence-first writing**: every major claim must map to data, citation, experiment, figure, or explicit limitation.
- **Compliant synthesis**: treat phrases such as "paper stitching" as user vocabulary, then convert them into transparent, attributable, reproducible research planning.
- **Bilingual usability**: support Chinese research notes, Chinese thesis/proposal contexts, and English manuscript prose.

## Repository Layout

```text
academic-stitcher-skill/
├── SKILL.md
├── manifest.yaml
├── README.md
├── README.en.md
├── agents/
│   └── openai.yaml
├── static/
│   ├── core/
│   │   ├── stance.md
│   │   ├── workflow.md
│   │   ├── quality-gates.md
│   │   └── output-format.md
│   └── fragments/
│       ├── route/
│       ├── paper_type/
│       ├── section/
│       └── language/
└── references/
    ├── playbook.md
    ├── writing-suite.md
    └── transcript-derived-playbook.md
```

## Skill Flow

The skill works as a router:

1. Read `manifest.yaml`.
2. Load the `always_load` core files.
3. Detect the request axes: `route`, `paper_type`, `section`, and `language`.
4. Load only the matching fragments under `static/fragments`.
5. Read `references/` only when deeper templates, source-informed rules, or video-distilled heuristics are needed.
6. Run quality gates for evidence, attribution, fair comparison, flow, reviewer pressure, and packaging.

## Routes

| Route | Purpose |
| --- | --- |
| `stitch-plan` | Research idea, A+B module design, thesis topic, proposal, advisor plan, experiment roadmap |
| `section-draft` | Title, abstract, introduction, related work, method, experiments, discussion, conclusion |
| `nature-polish` | Structural polishing, Nature-style English, Chinese-to-English manuscript prose, overclaim control |
| `reviewer-audit` | Methodology, domain, skeptical-reviewer, and integrity checks |
| `full-pipeline` | Intake, paper matrix, story architecture, evidence gate, drafting, audit, revision roadmap |

## Typical Use Cases

- Turn several related papers into a realistic small-paper or SCI story.
- Decide whether a baseline plus one module forms a defensible contribution.
- Build an opening-report research plan with feasible work packages.
- Convert experiment tables and notes into Introduction, Method, or Experiments sections.
- Polish Chinese notes into bounded English manuscript prose.
- Stress-test a manuscript from a reviewer perspective.
- Translate advisor constraints into a concrete research roadmap.

## Out Of Scope

This skill does not help with:

- fabricated data, citations, experiments, authorship, or peer-review history;
- plagiarism, rewriting to evade detection, or hidden reuse;
- intentionally weak baselines or unfair comparison;
- false random sampling claims for curated examples;
- hiding failed experiments, negative evidence, or data provenance;
- packaging unsupported speculation as top-venue novelty.

## Installation

### Recommended Codex Prompt

```text
Install the Codex skill from:
https://github.com/liang1228/academic-stitcher-skill.git
Preserve the full folder structure, including manifest.yaml, static/, references/, and agents/.
```

### Manual Installation

Copy the entire repository folder into your Codex skills directory:

```text
~/.codex/skills/academic-stitcher-skill
```

On Windows:

```text
%USERPROFILE%\.codex\skills\academic-stitcher-skill
```

Do not copy only `SKILL.md`; the router depends on `manifest.yaml`, `static/`, `references/`, and `agents/openai.yaml`.

## Validation

Use the validator bundled with `skill-creator`:

```powershell
$env:PYTHONUTF8='1'
python <skill-creator>\scripts\quick_validate.py <academic-stitcher-skill>
```

Expected result:

```text
Skill is valid!
```

## Output Contract

A complete response should usually include:

- selected route and paper type;
- story spine;
- claim-evidence-boundary map;
- section, experiment, or revision work packages;
- evidence gaps;
- compliance risks;
- reviewer objections;
- next checkpoint.

For English manuscript work, return polished English first. If the source material is Chinese, add concise Chinese notes explaining structural decisions.

## Design Lineage

- [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills): router-style layout, manifest axes, static fragments, and quality gates.
- [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills): section-level writing, paragraph flow, and claim-evidence alignment.
- [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex): Codex suite orchestration, inline role passes, and reviewer independence.
- Local project distillation: paper positioning, inheritance chains, module stitching, compliance translation of grey vocabulary, and graduate-research scenarios.

