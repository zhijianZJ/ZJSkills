# Learning Architect

[English](README.en.md)

**版本 1.0.0 · 84 tests · MIT**

把模糊的学习目标转化为可验证、可调整的个性化学习系统。

## 它解决什么问题

课程清单通常不会回答三个关键问题：目标究竟需要哪些能力、当前差距有什么证据、条件变化后应该从哪里重算。Learning Architect 从目标、基础、时间和约束出发，设计能力模型、项目阶梯、阶段路线、周度行动与评估关卡，并把事实、自述、证据、推断和假设分开记录。

它帮助你提高学习决策、能力证据和持续调整的质量，但不保证 Offer、转岗、晋升、收入或其他由外部主体决定的结果。

## 快速开始

在支持 Skills 的 AI 工具中启用 `learning-architect`，然后直接说明目标与约束：

```text
请使用 Learning Architect 帮我设计个性化学习系统。
我的目标是：在六个月内具备 AI Agent 工程师岗位所需的可验证能力。
我的基础是：会使用 Python 完成基础脚本。
我每周可投入：12 小时。
我的主要约束是：预算有限，希望项目优先。
请先询问会改变路线的关键信息，不要直接推荐课程。
```

第一次使用、继续规划和重新规划的提示词见[新手入门](docs/getting-started.md)。

## 安装

将仓库中的 Skill 目录复制到 Codex Skills 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./learning-architect "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后，在新任务中明确要求使用 `Learning Architect`。其他支持 Skills 的工具可按各自的本地 Skill 安装方式导入同一目录。

## 你会得到什么

- 一份包含目标、基础证据、容量、约束与风险的学习者画像；
- 从目标结果反推的能力树与前置依赖；
- 以真实产物和评分标准为核心的项目阶梯；
- 分阶段路线、下一周计划与明确的通过关卡；
- 可追溯的结构化状态，以及在目标、约束或证据变化后的版本化更新；
- 可复用的 Domain Pack 契约，仓库内置 AI Agent 工程师领域包。

## 工作方式

```text
发现 → 目标分析 → 差距分析 → 能力设计 → 课程设计
→ 项目设计 → 路线图 → 周度计划 → 阶段测评 → 结果准备 → 持续优化
```

每个阶段都有进入条件、产物与关卡。证据不足时，系统会标记假设或请求补充信息；项目或测评未通过时，它会定位最早的因果缺口，只重算受影响的下游部分。

## 完整文档

- [新手入门](docs/getting-started.md)：第一次使用、继续与重新规划；
- [完整使用手册](docs/usage-guide.md)：工作流、结构化状态、证据判断与安全边界；
- [使用场景与提示词](docs/examples.md)：四类典型目标的完整示例；
- [Domain Pack 扩展指南](docs/domain-pack-guide.md)：数据契约、能力依赖、项目原型与验证要求；
- [English documentation](README.en.md)：英文项目入口。

## 项目结构

| 位置 | 用途 |
| --- | --- |
| [`learning-architect/SKILL.md`](learning-architect/SKILL.md) | 核心运行契约与工作流路由 |
| [`learning-architect/references/`](learning-architect/references/) | 发现、能力、课程、项目、测评与优化引擎 |
| [`learning-architect/assets/`](learning-architect/assets/) | Schema、模板与 Domain Pack |
| [`learning-architect/scripts/`](learning-architect/scripts/) | 离线学习系统验证器 |
| [`tests/learning-architect/`](tests/learning-architect/) | 84 项回归测试及有效、无效样例 |
| [`docs/`](docs/) | 中英文使用与扩展文档 |

## 贡献

欢迎修正文档、报告可复现问题或提交符合数据契约的新 Domain Pack。提交前请阅读[贡献指南](CONTRIBUTING.md)，并遵守证据、隐私、品牌中立和禁止隐藏推广的边界。

## 发起与维护

由 ZJSkills（智建）发起并维护。

## 许可证

本项目采用 [MIT 许可证](LICENSE)。
