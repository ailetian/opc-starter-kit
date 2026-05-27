# opc-starter-kit 专业测试报告

> 测试日期：2026-05-25 | 测试范围：全局深度审计 | 测试方法：需求文档对照 + 代码审查 + 结构完整性 + 内容一致性

---

## A. 执行摘要

1. **[CRITICAL] SKILL.md 架构错位且命名不一致。** 实际技能文件位于 `.your AI coding tool/skills/opc-starter-kit/skill.md`（小写、嵌套），而 README、lint workflow 和 REQUIREMENTS.md 均引用项目根目录的 `SKILL.md`（大写）。CI lint 流程会全面失败，用户按 README 操作找不到技能文件。

2. **[CRITICAL] 缺少 YAML frontmatter。** `skill.md` 以 `# opc-starter-kit — AI 创业纪律技能` 开头，没有 YAML frontmatter。lint workflow 的 `head -1 SKILL.md | grep -q "^---"` 检查会失败。REQ 11.4 要求的 `description` 字段缺失。

3. **[HIGH] 36% 的承诺内容缺失（17 个文件/目录）。** `references/`（8 文件）、`scripts/`（4 脚本）、`assets/templates/`（8 模板）、`evals/`、`CHANGELOG.md`、`assets/images/` 均不存在。

4. **[HIGH] 版本号不一致。** REQUIREMENTS.md 声明 v1.0，skill.md 声明 v2.0，但无 CHANGELOG.md 说明变化。

5. **[MEDIUM] 文件命名规范冲突。** README/REQUIREMENTS.md 使用编号文件名（如 `01-problem-statement.md`），而 skill.md 实现使用无编号文件名（如 `problem-statement.md`）。

6. **[MEDIUM] skill.md 接近 500 行上限（443 行），且未将详细阶段指导拆分到 references/**。

---

## B. 详细发现

### B1. 结构完整性测试

#### [CRITICAL] SKILL.md 定位错误
- **需求规格**：REQUIREMENTS.md §11.1 规定 `SKILL.md` 位于项目根目录，≤500 行
- **README 描述**：README.md 第 203 行列出 `SKILL.md` 位于根目录
- **CI 检查**：`.github/workflows/lint-skill.yml` 检查根目录 `SKILL.md` 的行数、frontmatter、Claude 术语
- **实际**：`SKILL.md`（大写/根目录）不存在；实际文件是 `.your AI coding tool/skills/opc-starter-kit/skill.md`（小写/嵌套）
- **影响**：CI 完全不可用；用户按文档找不到文件
- **建议**：在项目根目录创建 `SKILL.md`，或在 `.your AI coding tool/skills/opc-starter-kit/` 下创建大写 `SKILL.md`，并更新所有文档和 CI 路径

#### [HIGH] 缺少 references/ 目录（8 个文件）
- **需求**：REQUIREMENTS.md §11.1 / README.md 文件结构图 / lint-skill.yml 第 40-49 行
- **缺失文件**：
  - `references/stage-1-ideation.md`
  - `references/stage-2-mvp.md`
  - `references/stage-3-launch.md`
  - `references/stage-4-scale.md`
  - `references/anti-confirmation.md`
  - `references/exit-criteria.md`
  - `references/questioning-guide.md`
  - `references/tool-adaptations.md`
- **影响**：skill.md 中所有阶段细节都内联在 443 行中，无法将内容拆分以降低行数；无工具适配映射表
- **建议**：创建 `references/` 目录，从 skill.md 第 3 节提取各阶段详细内容到对应文件，skill.md 保留简要概述和指针

#### [HIGH] 缺少 scripts/ 目录（4 个 Python 脚本）
- `scripts/init_state.py` — 状态文件初始化/恢复
- `scripts/update_state.py` — 状态文件更新
- `scripts/scan_docs.py` — 扫描 docs/ 推断阶段
- `scripts/create_task_file.py` — 生成任务文件
- **影响**：所有状态管理需 AI 手动进行，易出错且不一致；状态文件恢复逻辑缺失
- **建议**：实现这 4 个脚本，这是 skill 正确运行的基础设施

#### [HIGH] 缺少 assets/templates/ 目录（8 个文档模板）
- `problem-statement.md`、`architecture-context.md`、`scope-doc.md`、`metrics-framework.md`
- `interview-guide.md`、`pmf-assessment.md`、`bottleneck-audit.md`、`moat-narrative.md`
- **注意**：这些是**文档内容模板**（用户产出的空白模板），不是现有 `.your AI coding tool/skills/opc-starter-kit/templates/` 中的 UI/报告模板
- **建议**：创建 `assets/templates/` 并填充所有 8 个模板

#### [MEDIUM] 缺少其他文件
- `evals/evals.json` — 无测试/评估基础设施
- `CHANGELOG.md` — 无版本历史记录
- `assets/images/` — 缺少流程图的目录

#### [HIGH] lint-skill.yml CI 完全不可用
- **行数检查**（第 23 行）：检查 `SKILL.md`（根目录）— 文件不存在 → 失败
- **Frontmatter 检查**（第 32 行）：检查 `head -1 SKILL.md` — 文件不存在 → 失败
- **References 检查**（第 40-49 行）：检查 8 个 references/ 文件 — 全部不存在 → 8 个警告
- **Claude 术语检查**（第 64-77 行）：检查 `SKILL.md references/` — 目录不存在 → 失败
- **Templates 检查**（第 85-94 行）：检查 8 个 assets/templates/ 文件 — 全部不存在 → 8 个警告

---

### B2. skill.md 内容审计

#### [CRITICAL] 缺少 YAML frontmatter
- **需求**：REQUIREMENTS.md §11.4 要求 `---` 开头的 YAML frontmatter，包含 `description` 字段覆盖触发场景
- **实际**：第 1 行 `# opc-starter-kit — AI 创业纪律技能`，第 6、25 行的 `---` 是 markdown 水平线而非 YAML 分隔符
- **建议**：添加如下 frontmatter：
```yaml
---
name: opc-starter-kit
description: >-
  AI创业纪律检查站，面向一人公司创始人。验证创业想法、判定产品市场匹配度、
  判断当前阶段、规避AI时代创业陷阱。基于Anthropic创始人行动手册(2026.05)，
  通过红队/绿队关卡制贯穿想法-MVP-发布-规模化四个阶段。
---
```

#### [PASS] De-Claude-ification 检查 — skill.md 无违规
- 搜索 `CLAUDE.md`、`Claude Code`、`Claude Cowork`、`Claude Chat`、`MCP` — **0 匹配**
- skill.md 使用 "AI 编程工具" 等通用术语，符合 REQ 11.3

#### [MEDIUM] skill.md 行数管理
- 当前 443 行，在 500 行限制内但接近上限
- 第 3 节（四阶段详细规范，第 174-283 行）共约 110 行，应提取到 references/
- 提取后 skill.md 可降至约 330 行

#### [PASS] 核心行为规则（第 0 节，6 条规则）完整
1. 门控优先于建造 ✓
2. 证据优先于直觉 ✓
3. 仪式感优先于效率 ✓
4. 诚实优先于讨好 ✓
5. 产物优先于对话 ✓
6. 保持边界 ✓

#### [PASS] 禁止行为清单（第 8 节，7 项）覆盖关键场景
- 绿队未通过不引导建造 ✓
- AI 生成的模拟对话不作真实验证 ✓
- 不跳过红队关卡 ✓
- 不用"你做得好"替代证据审查 ✓
- 不输出超过 500 字无产物 ✓
- 不对自我欺骗保持沉默 ✓
- 不替代人工客户访谈等 ✓

#### [MEDIUM] 27 个失败模式防御覆盖情况
skill.md 对各阶段均有红队+绿队+微交付+通关报告，但防御机制描述高度压缩于 references/（缺失），无法验证深度。详见 B4。

---

### B3. 文档一致性审计

#### [HIGH] 版本号冲突
| 文件 | 声明版本 |
|------|---------|
| REQUIREMENTS.md 第 3 行 | `v1.0` |
| REQUIREMENTS.md 第 637 行 | `"skill_version": "1.0"` |
| skill.md 第 4 行 | `v2.0` |
| SKILL_USER_GUIDE.md 第 15、244 行 | `v2.0` |
| README.md | 未声明版本 |
| QUICK_START.md | 未声明版本 |

- **问题**：REQUIREMENTS.md（规格）和 skill.md（实现）版本号不一致，无法确定哪个版本是权威的
- **建议**：统一为 v2.0，同步更新 REQUIREMENTS.md；创建 CHANGELOG.md 记录 v1.0 → v2.0 变化

#### [MEDIUM] 文件命名不一致
| README.md / REQUIREMENTS.md | skill.md 实现 |
|------|------|
| `docs/01-problem-statement.md` | `docs/problem-statement.md` |
| `docs/02-competitive-map.md` | `docs/competitive-map.md` |
| `docs/03-interview-guide.md` | `docs/interview-guide.md` |
| `docs/05-problem-hypothesis.md` | `docs/problem-hypothesis.md` |
| `docs/06-architecture-context.md` | `docs/architecture-context.md` |
| `docs/07-scope-doc.md` | `docs/scope-doc.md` |
| ... | ... |

- **问题**：README 和 REQUIREMENTS 使用编号文件名，skill.md 实现使用无编号文件名
- **影响**：用户按 README 查找 `docs/01-problem-statement.md`，但 skill 生成的是 `docs/problem-statement.md`
- **建议**：统一使用无编号命名（更简洁），更新 README 和 REQUIREMENTS 中的引用

#### [MEDIUM] 命令表不一致
SKILL_USER_GUIDE.md 命令表比 skill.md 多出以下命令：
- `opc 启动` — 仅 SKILL_USER_GUIDE.md 有
- `opc 生成盲审报告` — 仅 SKILL_USER_GUIDE.md 有
- `opc 处理盲审反馈` — 仅 SKILL_USER_GUIDE.md 有
- `opc 重新验证假设` — 仅 SKILL_USER_GUIDE.md 有

skill.md 的命令表应补全这些命令。

#### [MEDIUM] 文件结构描述不一致
README.md 文件结构图（第 196-234 行）和 README.zh-CN.md（第 196-235 行）描述的结构与 `.your AI coding tool/skills/opc-starter-kit/` 实际结构不同：
- 两个 README 描述的是项目根目录的扁平结构
- 实际有一个 `.your AI coding tool/skills/opc-starter-kit/` 子目录包含了 skill.md 和 templates/

---

### B4. 功能完整性审计 — 27 个失败模式防御

#### 想法阶段（9 个失败模式）

| # | 需求 | skill.md 覆盖 | 红队关卡 | 绿队关卡 | 交付物 |
|---|------|-------------|---------|---------|--------|
| P1 | 先验证再建造 | §3.1 + §8 禁止项 | ✓ | ✓ 绿队 | ✓ |
| P2 | 过早规模化 | §3.1 退出标准 | ✓ | ✓ | ✓ |
| P3 | 确认偏误 | §3.1 红队关卡 | ✓ | — | ✓ |
| P4 | 问题陈述模糊 | §3.1 步骤1 | — | — | ✓ |
| P5 | 竞品忽视 | §3.1 步骤2 | ✓ | — | ✓ |
| P6 | 访谈问错问题 | §3.1 步骤3 | — | — | ✓ |
| P7 | 访谈后解释偏差 | §3.1 步骤4 | — | — | ✓ |
| P8 | 过度等待确定性 | §3.1 退出标准 | — | ✓ | ✓ |
| P9 | 方案对应错误问题 | §3.1 步骤4 + 三角验证 | — | — | ✓ |

#### MVP 阶段（8 个失败模式）

| # | 需求 | skill.md 覆盖 | 红队关卡 | 绿队关卡 | 交付物 |
|---|------|-------------|---------|---------|--------|
| P10 | Agentic 技术债 | §3.2 步骤1 | — | — | ✓ |
| P11 | 假 PMF | §3.2 步骤4 | ✓ | ✓ Sean Ellis | ✓ |
| P12 | 范围蔓延 | §3.2 步骤2 + 范围压力测试 | — | — | ✓ |
| P13 | 不安全代码 | 缺失明确触发 | — | — | — |
| P14 | 无架构上下文 | §3.2 步骤1 | — | — | ✓ |
| P15 | 未保存项目记忆 | §3.2 步骤1 + 文档自动保存 | — | — | ✓ |
| P16 | 发布后追踪度量 | §3.2 步骤3 | — | — | ✓ |
| P17 | 反馈解释偏差 | §3.2 步骤4 隐含 | — | — | 部分 |

#### 发布阶段（4 个失败模式）

| # | 需求 | skill.md 覆盖 | 红队关卡 | 绿队关卡 | 交付物 |
|---|------|-------------|---------|---------|--------|
| P18 | 技术债到期 | §3.3 步骤1 | — | ✓ | ✓ |
| P19 | 创始人瓶颈 | §3.3 步骤2 | — | ✓ | ✓ |
| P20 | 安全与合规 | 缺失 | — | — | — |
| P21 | 还没准备好就扩张 | §3.3 隐含 | — | — | 部分 |

#### 规模化阶段（6 个失败模式）

| # | 需求 | skill.md 覆盖 | 红队关卡 | 绿队关卡 | 交付物 |
|---|------|-------------|---------|---------|--------|
| P22 | 运营放手 | §3.4 步骤2 | — | ✓ | ✓ |
| P23 | 扩张技术运营 | §3.4 隐含 | — | — | 部分 |
| P24 | 扩张组织职能 | 缺失 | — | — | — |
| P25 | GTM 职能缺失 | §3.4 隐含 | — | ✓ | 部分 |
| P26 | 领域知识未外化 | §3.4 步骤1 | — | — | ✓ |
| P27 | 护城河不够深 | §3.4 步骤3 | ✓ 护城河压力测试 | ✓ | ✓ |

**总结**：27 个失败模式中，skill.md 明确覆盖约 **23 个（85%）**，但 "安全与合规"（P13、P20）和 "组织职能"（P24）的防御仍然薄弱或缺失。

---

### B5. De-Claude-ification 审计

对 **skill 核心文件**（`.your AI coding tool/skills/opc-starter-kit/skill.md`、`README.md`）的审计结果：

| 文件 | CLAUDE.md | Claude Code | Claude Cowork | Claude Chat | MCP |
|------|-----------|-------------|---------------|-------------|-----|
| skill.md | 0 | 0 | 0 | 0 | 0 |
| opc-starter-kit/README.md | 0 | 0 | 0 | 0 | 0 |

**核心运行文件通过 De-Claude-ification 检查。**

其他文件中出现 Claude 术语的位置均为以下合理场景：
- **README.md 第 186-188 行 / README.zh-CN.md 第 187-189 行**：De-Claude-ification 策略说明本身 — 可接受
- **REQUIREMENTS.md 第 1056-1058 行**：§11.3 策略说明 — 可接受
- **FAILURE_MODES.md 第 197 行**：解释手册原文中的 CLAUDE.md 概念 — 可接受
- **anthropic_opc手册.txt**：源材料（Anthropic 手册中文翻译）— 大量 Claude 术语属正常，这是原文而非 skill

**无实质违规。**

---

### B6. 可用性与质量审计

#### [PASS] 首次用户入口清晰
- `opc` 无参数 → 读状态 → 仪表盘 → 下一步指引
- `opc 启动` → 初始化新项目
- `opc 我有个想法` → 从想法阶段开始

#### [PASS] 错误处理定义
- 状态文件丢失 → 扫描 docs/ 推断阶段（§7.3）
- docs/ 不可写 → 临时输出 + 权限提示（REQUIREMENTS §9.1）
- 非 SaaS 项目 → 调整 PMF 指标（§7.2）
- 用户来回切换阶段 → 记录 + 3次后引导（REQ-ERR-05）

#### [MEDIUM] 模板质量问题
现有 6 个模板（`stage-map-template.md` 等）是"模板的模板"——包含占位符但无具体填充示例。缺少"完成示例"帮助用户理解期望产出。

#### [MEDIUM] 缺少测试基础设施
`evals/evals.json` 不存在。无自动化测试、无回归测试、无行为验证。

#### [PASS] 用户体验设计
- 故事式提问（§5）设计精良 — 不问数字，引出故事
- 三角验证机制 — 故事+数字+反例交叉验证
- 进展摘要 — 每步展示"进入前 vs 现在"
- 决策日志 — 自动追溯关键选择
- 被动触发检测 — 在非 opc 对话中轻量提醒

---

### B7. 状态管理审计

#### skill.md 状态文件 schema（§1）vs REQUIREMENTS.md 状态文件示例

| 字段 | skill.md (§1) | REQUIREMENTS.md (§7.2) | 一致？ |
|------|-------------|----------------------|--------|
| `current_stage` | ✓ | `phase` | **不一致** |
| `project_type` | ✓ | `project_type` | ✓ |
| `risk_profile` | ✓ | `risk_profile`（结构不同） | **部分** |
| 被动触发拒绝计数 | `opc_passive_nudge_rejected_count` | 缺失 | — |
| `skill_version` | 缺失 | ✓（REQ-EVO-06） | **缺失** |

**建议**：统一使用 `current_stage`（更明确）；添加 `skill_version` 字段；同步 risk_profile 结构。

---

## C. 优化建议

### 优先级 1 — 必须立即修复（阻塞性）

1. **创建项目根目录 `SKILL.md`**，并添加 YAML frontmatter
   - 将 `.your AI coding tool/skills/opc-starter-kit/skill.md` 内容提升到根目录
   - 添加 `description`、`name` 等 frontmatter 字段
   - 同步更新 lint-skill.yml 中的路径

2. **创建 `references/` 目录及 8 个参考文件**
   - 将 skill.md 第 3 节的阶段详细内容提取到对应的 `stage-N-xxx.md`
   - skill.md 缩减到 ~330 行，仅保留入口逻辑、调度、通用规则
   - 编写 `anti-confirmation.md`（反方代言人策略模板）、`exit-criteria.md`（退出标准判定规则）

3. **实现 `scripts/` 中的 4 个 Python 脚本**
   - `scan_docs.py` 是最关键的——状态文件丢失时的恢复逻辑
   - `create_task_file.py` ——子窗口模式的核心依赖

4. **统一版本号为 v2.0**，更新 REQUIREMENTS.md 版本声明

### 优先级 2 — 高优先级（影响可用性）

5. **创建 `assets/templates/` 中的 8 个文档模板**
   - 每个模板包含：章节结构 + 填写指引 + 完成示例

6. **统一文件命名规范** — 使用无编号命名（如 `problem-statement.md`），更新 README 引用

7. **创建 `evals/evals.json`** — 包含至少以下测试用例：
   - 新项目初始化 → 正确进入想法阶段
   - 5 次访谈后 → 绿队关卡触发
   - PMF 判定 → Sean Ellis 测试 + 假阳性排查
   - 跳过环节 → 决策日志记录 + 后续阶段提醒
   - 非 SaaS 项目 → PMF 指标调整

8. **补全 skill.md 中的安全与合规模块**
   - 在 MVP 阶段添加明确的安全审查提醒（P13）
   - 在发布阶段添加安全与合规升级模块（P20）

### 优先级 3 — 中优先级（改进质量）

9. **创建 `CHANGELOG.md`** — 记录 v1.0 → v2.0 的变化

10. **为现有模板添加完整示例** — 用户需要看到"填写后是什么样的"

11. **补全 skill.md 命令表** — 添加 `opc 启动`、`opc 生成盲审报告` 等命令

12. **添加 `skill_version` 到状态文件 schema**

13. **创建 `assets/images/` 并添加流程图**

14. **编写 `references/tool-adaptations.md`** — DeepSeek、Kimi、通义灵码等工具映射

---

## D. 综合评分卡

| 维度 | 评分 | 说明 |
|------|------|------|
| **结构完整性** | 3/10 | 36% 的承诺文件缺失；SKILL.md 错位；CI 完全不可用 |
| **skill.md 内容质量** | 7/10 | 核心逻辑设计精良，覆盖 85% 失败模式，但缺少 frontmatter，安全模组薄弱 |
| **文档质量** | 7/10 | 需求文档详尽（1148 行），用户指南清晰，但版本号、文件命名、命令表均有不一致 |
| **功能完整性** | 5/10 | 核心门控机制完整，但 references/ 和 scripts/ 缺失导致实现不完整，安全模块空白 |
| **可用性设计** | 7/10 | 故事式提问、三角验证、被动触发检测设计出色；但模板缺少示例，无测试基础设施 |
| **生产就绪度** | 3/10 | 缺少 CI 基础设施、测试评估、脚本自动化、文档模板；当前状态无法部署 |

**综合评分：5.3/10**

---

## E. 核心优势（值得保留并发扬的）

1. **四阶段门控设计**：想法 → MVP → 发布 → 规模化的红队/绿队关卡机制设计精良，直接映射 27 个失败模式
2. **故事式提问方法论**：不问数字引故事、反向提取数据、三角验证——这是差异化竞争力
3. **增强功能前瞻性强**：事后诊断、一页纸、盲审报告、时间感知、内部一致性检测——这些 v2.0 增强功能切实解决 OPC 创始人的痛点
4. **De-Claude-ification 执行到位**：核心运行文件零违规
5. **需求文档详尽**：1148 行 REQUIREMENTS.md 为后续开发提供了扎实基础

---

## F. 文件缺失清单（完整）

```
[缺失] SKILL.md (项目根目录)
[缺失] references/stage-1-ideation.md
[缺失] references/stage-2-mvp.md
[缺失] references/stage-3-launch.md
[缺失] references/stage-4-scale.md
[缺失] references/anti-confirmation.md
[缺失] references/exit-criteria.md
[缺失] references/questioning-guide.md
[缺失] references/tool-adaptations.md
[缺失] scripts/init_state.py
[缺失] scripts/update_state.py
[缺失] scripts/scan_docs.py
[缺失] scripts/create_task_file.py
[缺失] assets/templates/problem-statement.md
[缺失] assets/templates/architecture-context.md
[缺失] assets/templates/scope-doc.md
[缺失] assets/templates/metrics-framework.md
[缺失] assets/templates/interview-guide.md
[缺失] assets/templates/pmf-assessment.md
[缺失] assets/templates/bottleneck-audit.md
[缺失] assets/templates/moat-narrative.md
[缺失] evals/evals.json
[缺失] CHANGELOG.md
[缺失] assets/images/ 目录
```

**共计：1 个核心文件 + 8 个参考文件 + 4 个脚本 + 8 个文档模板 + 1 个评估文件 + 1 个变更日志 + 1 个目录 = 24 项缺失**

---

*报告由测试 agent 自动生成 | 基于 REQUIREMENTS.md (v1.0) 与 skill.md (v2.0) 交叉验证*