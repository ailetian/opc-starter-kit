# 工具适配说明

> opc-starter-kit 是基于 Markdown 的 Skill，不依赖任何特定 AI 工具平台。
> 所有文档使用通用术语，任何支持 Skill 系统的 AI 编程工具均可直接使用。

---

## 通用术语

| 通用术语 | 说明 |
|---------|------|
| 架构上下文文档 | 项目根目录下的持久化架构文档，每次 AI 编程会话的起点 |
| AI 编程工具 | 泛指所有 AI 辅助编程工具 |
| AI 对话 | 泛指所有 AI 聊天/对话界面 |
| 项目记忆文件 | 持久化项目上下文文件 |
| 子窗口 | 新开一个 AI 对话窗口执行独立任务 |

---

## Skill 安装

opc-starter-kit 基于 Markdown，不依赖特定平台的扩展机制：

1. 将 `SKILL.md` 放置在项目的 AI 工具可读取的位置
2. 将 `references/` 和 `scripts/` 目录一并复制
3. 确保 AI 工具能在对话中读取 `SKILL.md`
4. 支持 Skill 系统的工具，将整个目录放到对应的 skills 目录即可

### 状态和产出文件

生成的文件与平台无关：
- `.opc-state.json` — 项目根目录的状态文件
- `docs/` — 所有阶段产出
- 纯文本/Markdown/JSON，任何工具都能读取

---

## 术语转换检查表

在将 opc-starter-kit 部署到新平台时，检查：

- [ ] 所有文档中没有出现 "Claude" 特指术语
- [ ] "AI 编程工具" 替代了 "Claude Code"
- [ ] "AI 对话" 替代了 "Claude Chat"
- [ ] "架构上下文文档" 替代了 "CLAUDE.md"
- [ ] "项目记忆文件" 替代了 "CLAUDE.md"
- [ ] 没有引用 MCP（Model Context Protocol）作为特指
- [ ] 文档中引用的文件路径与当前平台兼容
