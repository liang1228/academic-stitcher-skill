# 学术裁缝课程：补充 RIA++ Skills

这是 `academic-stitcher-skill` 的独立补充包，包含从课程材料、B 站公开视频字幕和补充文档中筛选并验证的 5 个窄域方法 skill。

## 包含内容

- `supplement-skills/INDEX.md`：技能索引、关系图和推荐使用顺序
- `supplement-skills/DIGEST.md`：面向读者的精华说明
- `supplement-skills/GLOSSARY.md`：共享术语词典
- 五个子目录：每个目录均包含 `SKILL.md`、`agents/openai.yaml`、`test-prompts.json` 和 `test-results.md`

## 五个入口

1. `direction-feasibility-foundation-map`：研究方向可行性与基础地图
2. `purpose-driven-paper-decomposition`：按目的拆解论文证据
3. `variable-granularity-abc-research-architecture`：可变粒度 A/B/C 研究架构
4. `three-domain-module-search-dataflow-adaptation`：三域模块搜索与数据流适配
5. `innovation-workload-dual-axis`：创新—工作量双轴论文架构

## 使用方式

这些目录是独立 skill，不覆盖仓库根目录的通用 `academic-stitcher-skill`。按用户问题选择对应子目录安装或复制到 Codex skills 目录；需要组合时，先读 `supplement-skills/INDEX.md`，再按依赖关系调用。

## 证据边界

本包蒸馏的是可执行方法框架，不是学校政策、发表保证或独立复现实验。课程 ASR、B 站 AI 字幕、PDF 导出/OCR 和讲者自述均保留相应复核边界；原始视频、字幕缓存、文档原件、候选全文和本地审计缓存不随包发布。

## 验证

五个 skill 均包含应触发、诱饵和边界测试；阶段 4 独立盲测结果为 30/30 通过。每个 `SKILL.md` 均按 Codex skill 结构校验通过。
