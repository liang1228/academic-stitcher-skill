# academic-stitcher-skill

> 中文说明 | [English README](README.en.md)

`academic-stitcher-skill` 是一个面向 Codex 的结构化学术写作 Skill。它把“缝论文 / 论文故事 / A+B 组合 / 研究生开题 / SCI 写作 / Nature-style polishing / 预审稿”统一成一条可执行的 Skill flow：先识别目标与证据，再构建问题-机制-证据链，最后输出章节、实验、审稿风险和下一步工作包。

该仓库参考了 [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) 的 router-style 结构，吸收了其 `manifest.yaml`、`static/core`、`static/fragments`、按需加载和质量门思路；同时保留本项目从 “缝论文 / 论文故事”材料中蒸馏出的研究规划、论文包装、灰色话术合规转译与研究生场景经验。

## 目录

- [设计目标](#设计目标)
- [仓库结构](#仓库结构)
- [Skill Flow](#skill-flow)
- [Routes](#routes)
- [适用场景](#适用场景)
- [不适用场景](#不适用场景)
- [安装方式](#安装方式)
- [验证](#验证)
- [输出标准](#输出标准)
- [设计来源](#设计来源)
- [维护原则](#维护原则)

## 设计目标

- **结构化技能流**：把论文构思、章节写作、Nature-style 润色、审稿自检和全流程管线拆成明确 route。
- **渐进式加载**：`SKILL.md` 只做路由；常用规则放入 `static/core`；细分场景放入 `static/fragments`；深层模板放入 `references`。
- **证据优先**：每个 claim 都必须绑定数据、引用、实验、图表或显式 limitation。
- **合规研究转译**：保留“缝论文”等用户语言作为触发词，但执行层只给透明、可引用、可复现、可辩护的方案。
- **中英双语可用**：支持中文研究笔记、中文开题/毕业场景，以及英文 manuscript prose。

## 仓库结构

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

`SKILL.md` 会先读取 `manifest.yaml`，再按需加载文件：

1. **Always load**：`static/core/stance.md`、`workflow.md`、`quality-gates.md`、`output-format.md`。
2. **Detect axes**：识别 `route`、`paper_type`、`section`、`language`。
3. **Load fragments**：只读取匹配的 route / paper type / section / language fragment。
4. **Use references on demand**：只有任务需要更深模板、灰色话术映射、视频蒸馏依据或 Codex-suite 细节时才读 `references/`。
5. **Run quality gates**：证据、引用、对比公平性、段落流、审稿压力和发布包装边界。

## Routes

| Route | 用途 |
| --- | --- |
| `stitch-plan` | 论文方向、A+B 模块、研究生开题、导师计划、实验路线 |
| `section-draft` | 摘要、引言、相关工作、方法、实验、讨论、结论等章节写作 |
| `nature-polish` | 结构润色、Nature-style 英文、中文笔记转英文、过度声称降级 |
| `reviewer-audit` | 方法学、领域适配、怀疑型审稿人、诚信风险预审 |
| `full-pipeline` | 从 intake 到文献矩阵、故事线、证据门、写作、审稿、修改路线的全流程 |

## 适用场景

- “我有几篇论文，帮我缝一个能写的小论文方向。”
- “我有 baseline 和一个模块，帮我判断能不能组成 SCI 故事。”
- “帮我写开题报告的研究内容、技术路线和创新点。”
- “把这些实验结果组织成 Introduction / Method / Experiments。”
- “把中文草稿润色成 Nature-style 英文。”
- “从审稿人视角挑这篇论文的硬伤。”
- “导师让我做个方向，帮我拆成可执行 work packages。”

## 不适用场景

本 skill 不提供以下帮助：

- 伪造数据、引用、实验结果、作者贡献或审稿历史。
- 隐藏复制、洗稿、降重规避、绕过检测。
- 故意挑弱 baseline、削弱复现实验、假称案例随机。
- 隐瞒失败实验、负结果或数据来源。
- 把没有证据的想法包装成 top-venue novelty。

## 安装方式

### Codex 推荐方式

让 Codex 安装该仓库：

```text
Install the Codex skill from:
https://github.com/liang1228/academic-stitcher-skill.git
Preserve the full folder structure, including manifest.yaml, static/, references/, and agents/.
```

### 手动方式

把整个仓库目录复制到你的 Codex skills 目录下，例如：

```text
~/.codex/skills/academic-stitcher-skill
```

Windows 用户可放到：

```text
%USERPROFILE%\.codex\skills\academic-stitcher-skill
```

复制时不要只复制 `SKILL.md`。本 skill 依赖 `manifest.yaml`、`static/`、`references/` 和 `agents/openai.yaml`。

## 验证

使用 `skill-creator` 的校验脚本：

```powershell
$env:PYTHONUTF8='1'
python <skill-creator>\scripts\quick_validate.py <academic-stitcher-skill>
```

通过后应看到：

```text
Skill is valid!
```

## 输出标准

默认输出应包含：

- route 与 paper type；
- story spine；
- claim-evidence-boundary map；
- section / experiment / revision work packages；
- evidence gaps；
- compliance risks；
- reviewer objections；
- next checkpoint。

对于英文稿件，先给 polished English；如果输入来自中文笔记，再附简短中文结构说明。

## 设计来源

- [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)：router-style skill layout、manifest axes、static fragments、quality gates。
- [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)：分章节写作、段落流、claim-evidence alignment。
- [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex)：Codex suite orchestration、inline role passes、reviewer independence。
- 本项目 B 站视频与逐字稿蒸馏：论文定位、继承链、模块拼接、灰色话术合规转译和研究生实用场景。

## 维护原则

- 新增常用规则优先进入 `static/core` 或 `static/fragments`。
- 大模板、细节表、来源型总结进入 `references/`。
- 不把原始字幕、逐视频笔记、抓取表、上游 examples/tests/scripts 放进主仓库。
- `SKILL.md` 保持精炼，只做触发、路由和边界。
- 每次重大修改后运行 `quick_validate.py` 和路径/凭据残留扫描。
