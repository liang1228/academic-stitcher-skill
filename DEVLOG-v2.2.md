# Dev Log: v2.2 蒸馏大更新

> 日期: 2026-06-30
> 工作内容: 从 B 站字幕 + 3 个外部 skill 蒸馏并合成到 academic-stitcher-skill

---

## 背景

academic-stitcher-skill v2.1.10 架构完整（router + manifest + progressive loading），但 fragment 内容普遍薄弱（大部分只有 10-20 行）。现有的 `transcript-derived-playbook.md` 仅从 75 个视频蒸馏出 6 条粗规则。

本次工作目标：用 nuwa-skill 的蒸馏方法论，从 149 个 B 站字幕文件 + 3 个外部 skill 仓库重新蒸馏，补全所有薄弱 fragment。

---

## Phase 1: 字幕筛选

- 从 `E:\workspace\bilibili_subtitles\` 的 524 个字幕文件中，用 Python 脚本按关键词分类筛选
- 筛选出 149 个学术写作相关文件，分 8 个类别：
  - 学术裁缝 (63)、毕业大论文 (37)、研究规划 (21)、选刊投稿 (14)、论文阅读 (5)、实验设计 (4)、答辩盲审 (3)、AI 辅助 (2)
- 输出到 `filtered/` 目录 + `manifest.json`
- 筛选脚本: `filter_academic.py`

## Phase 2: 多维度蒸馏

借鉴 nuwa-skill 的 6-agent 并行研究模式，adapt 为 3 个并行蒸馏 agent：

### Agent A: 写作方法论 + 章节模板
- 读取: 学术裁缝系列 + 毕业大论文逐章 (35+ 文件)
- 产出: `distill/A-writing-methodology.md` (20 KB)
- 核心发现:
  - A+B+C 结构模型 (论文可解构为基准+模块+模块)
  - 读论文方法: 逐段逐部分，非逐字逐句
  - 只看一区和四区论文
  - 先找模块拼上去，再编故事
  - 写作顺序: 方法→实验→相关工作→引言→摘要→总结

### Agent B: 话术映射 + 实验设计
- 读取: 实验设计 + 选刊投稿 + 学术裁缝关键文件 (28 文件)
- 产出: `distill/B-rhetoric-experiment.md` (312 行, 21 KB)
- 核心发现:
  - 12 组灰色话术→合规表达映射
  - 信息不对称原则 ("你知道的，审稿人不一定知道")
  - 消融实验策略 (模块无效时合并描述)
  - 7 种审稿人攻击向量

### Agent C: 投稿生涯 + 答辩盲审
- 读取: 答辩盲审 + AI辅助 + 研究规划 + 选刊投稿 (22 文件)
- 产出: `distill/C-submission-defense.md` (325 行, 27 KB)
- 核心发现:
  - 答辩"只答不辩"原则
  - PPT "图多字少" + "挖坑"策略
  - 盲审比例淘汰制 (~30% 不通过)
  - ChatGPT 使用工作流 (英文 prompt, 1000 字限制)
  - 研究生年度规划路线图

### 蒸馏方法论 (adapted from nuwa-skill)
- **三重验证**: 跨视频复现(3+) + 生成力 + 排他性
- **置信度标注**: direct / inferred / needs-verification
- **BVID 来源追溯**: 每条规则标注来源视频

## Phase 3: 合成到 Skill Fragment

用 3 个并行 agent 将蒸馏结果写入现有 fragment 文件：

### Section Fragments (8 个)
| 文件 | 之前 | 之后 | 新增内容 |
|------|------|------|---------|
| title.md | 15 行 | 64 行 | 命名模式、好坏标题对比 |
| abstract.md | 15 行 | 66 行 | 4 句摘要框架、摘要 vs 结论区别 |
| introduction.md | 15 行 | 77 行 | 漏斗结构、One-Sentence Argument |
| related-work.md | 15 行 | 78 行 | A/B/C 模块谱系映射 |
| method.md | 15 行 | 70 行 | 数据流描述模式、先总后分 |
| experiments.md | 15 行 | 76 行 | 4 部分实验结构、消融策略 |
| discussion.md | 15 行 | 71 行 | 解释框架、局限性表述 |
| conclusion.md | 15 行 | 74 行 | 摘要 vs 结论区别、贡献复述 |

### Route Fragments
| 文件 | 之前 | 之后 | 新增内容 |
|------|------|------|---------|
| reviewer-audit.md | 14 行 | 82 行 | 7 种审稿人角色、攻击向量、回复策略 |
| nature-polish.md | 20 行 | 73 行 | 中英转写规则、声明动词校准 |
| full-pipeline.md | 20 行 | 66 行 | 9 个 stage 的具体动作和质量门 |

### 其他 Fragment
| 文件 | 之前 | 之后 | 新增内容 |
|------|------|------|---------|
| algorithmic.md | 20 行 | 71 行 | 消融策略、基线选择、数据集原则 |
| zh-cn.md | 11 行 | 80 行 | 灰色话术映射 12 组、中文写作模式 |
| transcript-derived-playbook.md | 47 行 | 191 行 | 重写: 7 核心规则 + 话术 + 实验 + 投稿 |

## Phase 3b: 外部 Skill 合入

探索 3 个外部仓库，提取不冲突的增量内容：

### nature-skills (Yuan1z0825)
| 增量 | 写入位置 | 冲突检查 |
|------|---------|---------|
| Terminology Ledger | stance.md | ✅ 无冲突，扩展已有 section |
| Reader Cognitive Model (5 问) | workflow.md | ✅ 无冲突，新增 section |
| AI Traffic-Light 伦理分级 | stance.md | ✅ 无冲突，新增 section |
| Failure-Mode Diagnosis 优先级 | nature-polish.md | ⏭️ 已有相同内容，跳过 |
| One-Sentence Argument | introduction.md | ✅ 无冲突，新增 section |
| Paragraph-to-Job Mapping | quality-gates.md | ✅ 无冲突，新增 subsection |

### academic-research-skills-codex (Imbad0202)
| 增量 | 写入位置 | 冲突检查 |
|------|---------|---------|
| 7 种审稿人角色 | reviewer-audit.md | ✅ 无冲突，新增 table |
| Citation Verification Gate | quality-gates.md | ✅ 无冲突，新增 gate |

### Auto-claude-code-research-in-sleep (wanshuiyin)
| 增量 | 写入位置 | 冲突检查 |
|------|---------|---------|
| Dual-Axis Control | workflow.md | ✅ 无冲突，新增 section |
| 5 层审计链概念 | ctx2skill-evaluation.md | ✅ 仅概念借鉴 |

### 不合入的内容 (有冲突)
| 内容 | 来源 | 原因 |
|------|------|------|
| Research Wiki (持久化知识图谱) | ARIS | 需要基础设施，超出 skill 范围 |
| No Autonomous Research | ARS | 与 stitch-plan 路由冲突 |
| No Paper2X Auto-Generation | ARS | 范围限制 |
| Material Passport 完整实现 | ARS | 架构差异过大，仅借鉴概念 |
| Mandatory Confirmation Gate | nature-skills | 与自主流程冲突，改为"建议确认点" |

---

## 最终结果

### 统计
- 18 个文件修改，+975 行，-68 行
- 25 个 manifest 路径全部验证通过
- Git commit: `b1220f0`

### 知识来源汇总
| 来源 | 文件数 | 产出 |
|------|--------|------|
| B 站字幕 (慧研格真) | 149 个筛选, 85+ 个精读 | 3 个蒸馏文档 (68 KB) |
| nature-skills | 读取 15+ 文件 | 5 个增量规则 |
| academic-research-skills | 读取 10+ 文件 | 2 个增量规则 |
| ARIS | 读取 10+ 文件 | 1 个增量规则 |

### 待后续改进
- [ ] 补充 `paper_type/*.md` (research, methods, review, proposal-thesis 仍较薄)
- [ ] 补充 `stitch-plan.md` route fragment
- [ ] 新增 rebuttal route fragment
- [ ] 新增 figure/table 指导 fragment
- [ ] 添加完整工作示例 (examples/)
- [ ] 跑 Ctx2Skill 自评估验证
