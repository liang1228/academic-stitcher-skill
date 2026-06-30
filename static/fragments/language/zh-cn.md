# Language: Chinese Or Chinese Notes

Use when the source notes or final explanation are Chinese or mixed Chinese-English.

## Rules

- Preserve Chinese user vocabulary as diagnostic labels when useful.
- Convert grey wording into compliant research planning.
- When drafting English from Chinese notes, translate intent and argument, not clause order.
- Keep short Chinese notes after English prose to explain major structural choices.
- Do not preserve colloquial exaggeration in manuscript-facing text.

---

## Grey Vocabulary Conversion (灰色话术合规映射)

When source material uses colloquial or grey-area Chinese terms, convert them to compliant academic expressions before they reach manuscript text.

| Grey / Colloquial Term | Compliant Academic Expression | When to Apply | BVID Sources |
| --- | --- | --- | --- |
| 缝论文 / 学术裁缝 | Modular combinatorial innovation (adapting proven modules to a new task or domain) | When describing baseline + module assembly strategy | BV1mK411C7WH, BV1ne41157Gn, BV1fV4y1B72F |
| 水论文 | Efficient production of compliant papers (leveraging validated module combinations with domain adaptation) | When discussing rapid paper output for graduation requirements | BV1fP411F7ke, BV1st4y1w7u5, BV1dg411p7QP |
| 造航母 | Undertaking an overly ambitious research scope (beyond master's-level feasibility) | When flagging unrealistic advisor assignments | BV19jCrYsEoE, BV18Ve6zvEBT |
| 数据美化 | Systematic parameter tuning and evaluation configuration optimization | When adjusting experiments for better results within reasonable bounds | BV19jCrYsEoE, BV1dg411p7QP |
| 编故事 | Constructing a coherent research narrative (problem framing and contribution storytelling) | When packaging technical work as a logical academic contribution | BV1ne41157Gn, BV1cH4y1j742, BV1fP411F7ke |
| 营造信息差 | Selective information presentation (favorable details emphasized, unfavorable details omitted) | When describing叙述策略 in manuscript writing | BV1Ns4y197EM, BV1fV4y1B72F, BV1dg411p7QP |
| 复刻别人想法 | Adapting established approaches from prior work to a new domain | When identifying transferable modules or methods | BV1ne41157Gn, BV1vt4y1T7sy |
| 堆叠 | Composing multiple modules from different papers into one framework | When single-module improvement is insufficient | BV1ne41157Gn, BV1vt4y1T7sy |
| 炼丹 | Systematic hyperparameter search and experimental tuning | When describing parameter optimization in AI/ML work | BV1LK9ZYYErM |
| 开源=造假 (ironic) | Implies unverified claims -- note that unclaimed results cannot be independently reproduced | As a cautionary note, never in manuscript text | BV1LK9ZYYErM, BV19jCrYsEoE |
| 仿造同行写 | Emulating the structure and style of published work in the same field | When establishing the paper's structural template | BV1st4y1w7u5, BV12M4y1J737 |

## Chinese Academic Writing Patterns (中文学术写作范式)

(BVID sources: BV1fW4y1W7dS, BV1ut34zuEfS, BV12WJ6zoEa6, BV1dzNWewExA)

These patterns appear consistently across Chinese academic instruction and should be followed in Chinese-language manuscripts or Chinese drafts of English papers.

### Abstract Pattern (摘要范式)

1. [领域背景] 领域做了什么，有什么重要性
2. [发现问题] 但是存在什么问题（创新点在这里）
3. [解决方法] 因此提出了XX方法，通过ABC模块解决了这些问题
4. [结果] 大量实验表明，方法在XX指标上取得了优异性能

**Key constraint**: 摘要与结论不能用完全相同的语句，必须换一种说法表达相同意思。

### Introduction Pattern (引言范式)

1. 领域描述（1-2段）：用通俗语言，不加引用
2. 问题引入（带引用）：随着发展出现了问题A、B、C
3. 解决方法：通过以下三点/模块解决了这些问题
4. 结果概述：实验表明性能有提升

**Key constraint**: 必须用可视化例子来展示问题，不能只有文字描述。

### Related Work Pattern (相关工作范式)

采用"总-分-分[总]"结构：总述段→按A/B/C模块分别介绍发展史→[可选]总结段。

**Key constraint**: 不介绍与论文无关的工作；每段发展史中要指出前人存在的问题。

### Method Writing Pattern (方法写作范式)

按数据流从输入到输出客观描述，先总后分：概述整体架构→分模块介绍每个组件。

### Conclusion Pattern (结论范式)

结论管"方法+实验"：阐述做了什么、怎么做的、效果如何。不需要再讲背景和前人工作。

## Common Expressions and Their Compliant Versions

| Informal / Risky Chinese | Compliant Replacement | Context |
| --- | --- | --- |
| 我们发现了最好的模块组合 | 经过系统性实验验证，所提出的模块组合在目标指标上取得了显著提升 | Abstract / Conclusion |
| 这个方法比别人的强 | 本方法在XX指标上优于现有方法Y% | Results comparison |
| 我们的SOTA | 我们的方法达到了当前最佳性能（在所评估的方法范围内） | Performance claims |
| 前人的方法都不行 | 现有方法在XX方面存在不足/忽略了XX问题 | Introduction framing |
| 实验数据是调出来的 | 通过系统性超参数搜索确定了最优配置 | Experiment section |
| 编一个合理的理由 | 为方法选择提供理论依据和实验证据 | Justification statements |
