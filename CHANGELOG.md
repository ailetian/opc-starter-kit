# Changelog

All notable changes to opc-starter-kit skill.

---

## v2.0 (2026-05-25)

### Added
- **YAML frontmatter** in SKILL.md with `name` and `description` fields
- **references/ 目录** — 8个详细参考文件：
  - `stage-1-ideation.md` — 想法阶段详细操作指南
  - `stage-2-mvp.md` — MVP阶段详细操作指南（含安全审查清单）
  - `stage-3-launch.md` — 发布阶段详细操作指南（含安全合规升级）
  - `stage-4-scale.md` — 规模化阶段详细操作指南（含组织职能扩张和GTM）
  - `anti-confirmation.md` — 反方代言人策略模板（四种红队角色+完整话术库）
  - `exit-criteria.md` — 各阶段退出标准判定规则及边界情况处理
  - `questioning-guide.md` — 引导式提问模板（故事式+三角验证+各阶段专用话术）
  - `tool-adaptations.md` — 多平台工具适配映射表
- **scripts/ 目录** — 4个自动化Python脚本：
  - `init_state.py` — 状态文件初始化/恢复
  - `update_state.py` — 状态文件更新
  - `scan_docs.py` — 扫描docs/推断阶段
  - `create_task_file.py` — 生成子窗口任务文件
- **assets/templates/ 目录** — 8个文档内容模板（含填写指引和完成示例）：
  - `problem-statement.md`, `architecture-context.md`, `scope-doc.md`, `metrics-framework.md`
  - `interview-guide.md`, `pmf-assessment.md`, `bottleneck-audit.md`, `moat-narrative.md`
- **evals/evals.json** — 20个测试用例覆盖所有核心流程
- **CHANGELOG.md** — 版本历史记录
- **进度感知系统**：每个阶段微任务完成后展示"进入前 vs 现在"进展摘要
- **事后诊断模式**：对已建造产品的项目倒序检查跳过的验证环节
- **一页纸功能**：生成可分享的项目当前状态摘要
- **盲审报告**：生成剥离身份信息的匿名评审包
- **时间感知**：阶段完成过快时触发提醒
- **内部一致性检测**：阶段转换时交叉比对关键假设
- **护城河积分卡**：三维度量化追踪护城河深度
- **被动触发检测**：在非opc对话中轻量提醒高危行为
- **决策日志自动维护**：关键选择自动追加到decisions.md
- **证据锚点**：关键判定节点提示可选硬证据上传

### Changed
- **统一版本号为 v2.0** — REQUIREMENTS.md 版本声明从 v1.0 更新为 v2.0
- **文件命名统一** — 文档引用从编号命名（如 `01-problem-statement.md`）改为无编号命名（如 `problem-statement.md`）
- **SKILL.md 添加 YAML frontmatter** — 包含 `name: opc-starter-kit` 和 `description` 字段
- **SKILL.md 命令表补全** — 添加 `opc 启动`、`opc 生成盲审报告`、`opc 处理盲审反馈`、`opc 重新验证假设`
- **状态文件添加 skill_version 字段** — 值为 "2.0"
- **安全模块增强** — MVP阶段添加编码前安全审查提醒（P13），发布阶段添加安全合规升级模块（P20）
- **skill.md 行数优化** — 阶段详细内容提取到 references/，核心文件保持约420行
- **README/README.zh-CN** — 更新文件结构图反映实际目录

### Fixed
- **[CRITICAL] SKILL.md 定位错误** — 在项目根目录创建 SKILL.md（大写），解决CI lint全部失败的问题
- **[CRITICAL] YAML frontmatter 缺失** — 添加符合REQ 11.4要求的frontmatter
- **[HIGH] 版本号不一致** — REQUIREMENTS.md (v1.0) 和 skill.md (v2.0) 统一为 v2.0
- **[HIGH] 36%承诺内容缺失** — references/ (8文件)、scripts/ (4脚本)、assets/templates/ (8模板)、evals/ 全部补充
- **[MEDIUM] 文件命名冲突** — 统一使用无编号命名
- **[MEDIUM] 命令表不一致** — SKILL_USER_GUIDE.md 和 skill.md 命令表同步

---

## v1.0 (Initial Release)

- 核心四阶段门控机制（想法 → MVP → 发布 → 规模化）
- 红队/绿队关卡制
- 故事式提问方法论
- 三角验证机制
- 基础状态管理和文档产物系统
- 6个UI/报告模板