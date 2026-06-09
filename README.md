# Academic Stitcher Skill (学术缝合技能库)

本仓库是一个严格遵循 [Datawhale《如何写出好的 Skill》指南](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra08-%E5%A6%82%E4%BD%95%E5%86%99%E5%87%BA%E5%A5%BD%E7%9A%84Skill.md) 构建的 AI Agent 技能模块。

## 简介

**Academic Stitcher Skill** 旨在帮助 AI Agent 执行“科学创新缝合（Scientific Innovation Stitching）”工作流。通过将目标研究课题（Target）解构为对象（Object）、方法（Method）和场景（Scenario），并引入新技术催化剂（Catalyst），生成具有创新性的学术研究思路。

## 仓库结构

本仓库采用 AI 优化的三级分层架构，确保 Agent 能以最低的 Token 成本获取最精准的指令：

- **`SKILL.md` (入口文件)**: 
  - 包含 YAML frontmatter 元数据，定义技能激活触发条件。
  - 包含核心指令（Imperative Mood），规定 Agent 的行为边界及反模式（Anti-patterns）。
- **`scripts/stitcher.py` (执行脚本)**: 
  - 确定性助手脚本。负责解析论文摘要、结构化 JSON 输出以及验证输入完整性，减少 AI 在格式处理上的不确定性。
- **`references/stitching_rules.md` (参考资料)**: 
  - 详细阐述“A+B 模型”逻辑。当 Agent 需要深入理解对象、方法、场景的解构原则时调用。
- **`assets/example_templates.json` (产出模板)**: 
  - 提供高质量的缝合思路示例，作为 Few-shot 模板引导 Agent 生成符合学术标准的创新构思。

## 如何使用

AI Agent 在加载此技能后，应遵循以下流程：

1. **识别需求**: 当用户提出“帮我写论文开题报告”或“有哪些研究新思路”时，通过 `SKILL.md` 的描述自动触发。
2. **解构与验证**: 调用 `scripts/stitcher.py` 对输入的课题进行结构化拆解。
3. **知识参考**: 参考 `references/stitching_rules.md` 中的原则，确保“缝合”逻辑具备科学合理性。
4. **生成产出**: 参考 `assets/example_templates.json` 的格式，输出 3 个针对具体痛点的创新研究点。

## 贡献与规范

本仓库所有变更须严格遵守 Skill 设计原则：
- **简洁性**: 不包含任何对 AI 无用的冗余文档（如人类阅读的安装指南）。
- **确定性**: 脆弱操作（如复杂格式解析）必须通过脚本锁定。
- **祈使句**: 指令部分统一使用祈使语气，消除歧义。
