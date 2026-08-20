# Academic Research Planning Skills

一组可独立安装、可组合使用的 Codex skills，用于把研究想法、论文证据、模块迁移和论文交付转化为可核查的工作计划。

## 五个入口

1. [direction-feasibility-foundation-map](./skills/direction-feasibility-foundation-map/SKILL.md)：判断研究方向是否具备文献、基础、传承和资源条件，并设置最小试点与退出门。
2. [purpose-driven-paper-decomposition](./skills/purpose-driven-paper-decomposition/SKILL.md)：按研究目的拆解论文中的任务、基线、模块、接口和实验证据。
3. [variable-granularity-abc-research-architecture](./skills/variable-granularity-abc-research-architecture/SKILL.md)：按当前主张重画 A/B/C，区分继承、改动和新增贡献。
4. [three-domain-module-search-dataflow-adaptation](./skills/three-domain-module-search-dataflow-adaptation/SKILL.md)：跨通用域、本领域和相似领域搜索模块，核对数据流与训练/部署契约。
5. [innovation-workload-dual-axis](./skills/innovation-workload-dual-axis/SKILL.md)：把创新证据与可核查工作量分轴映射到实验、章节和交付要求。

## 推荐使用顺序

1. 还在选方向：direction-feasibility-foundation-map
2. 已有论文对象：purpose-driven-paper-decomposition
3. 需要冻结基线与贡献边界：variable-granularity-abc-research-architecture
4. 需要迁移模块：three-domain-module-search-dataflow-adaptation
5. 需要安排论文交付：innovation-workload-dual-axis

这些 skill 可以单独复制到 Codex skills 目录，也可以按上面的依赖关系组合调用。

## 仓库结构

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

每个 skill 目录包含：

- SKILL.md：运行时规则、触发边界和执行步骤
- agents/openai.yaml：显示名称与默认调用提示
- test-prompts.json：触发、诱饵和边界测试
- test-results.md：独立路由验证结果

## 输出契约

五个入口都要求：

- 先固定用户当前要做的决定和比较对象；
- 区分事实、假设、待核验项和停止条件；
- 保留证据、许可、版本、接口、改动、对照和消融记录；
- 不把指标提升、论文数量或经验性说法直接升级为贡献、政策或保证；
- 在关键信息缺失时输出缺口与下一步，而不是补造结论。

## 公开边界

仓库只提供可执行的工作框架，不替代学校规章、期刊要求、法律判断或真实实验。涉及当前制度、许可、数据、代码和复现条件时，应回到相应的最新正式材料核验。仓库不包含本机路径、原始缓存、内部审计文件或未整理的中间产物。

## 验证

五个 skill 均通过结构校验；每个 skill 的 6 条路由测试均通过，总计 30/30。

更多关系图与学习顺序见 [INDEX.md](./INDEX.md)，方法精华见 [DIGEST.md](./DIGEST.md)，术语说明见 [GLOSSARY.md](./GLOSSARY.md)。
