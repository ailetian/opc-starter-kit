# 工具适配映射表

> 本节提供 opc-starter-kit 在不同 AI 工具平台上的概念映射和使用说明。
> 遵循 De-Claude-ification 策略（参见 REQUIREMENTS.md §11.3）。

---

## 通用术语映射

opc-starter-kit 使用以下通用术语替代特定平台的专有名词：

| 通用术语 | 说明 |
|---------|------|
| 架构上下文文档 | 项目根目录下的持久化架构文档，每次 AI 编程会话的起点 |
| AI 编程工具 | 泛指所有 AI 辅助编程工具 |
| AI 对话 | 泛指所有 AI 聊天/对话界面 |
| 项目记忆文件 | 持久化项目上下文文件 |
| 子窗口 | 新开一个 AI 对话窗口执行独立任务 |

---

## 平台适配说明

### your AI coding tool（百度）

| opc-starter-kit 概念 | your AI coding tool 等效 |
|---------------|------------|
| AI 编程工具 | your AI coding tool IDE 插件 / 快码 |
| AI 对话 | your AI coding tool 对话框 |
| 项目记忆文件 | 项目目录下的 `.your AI coding tool/project-memory.md` |
| 子窗口 | 打开新 your AI coding tool 会话 |
| Skill 安装路径 | `.your AI coding tool/skills/opc-starter-kit/` |

### DeepSeek

| opc-starter-kit 概念 | DeepSeek 等效 |
|---------------|-------------|
| AI 编程工具 | DeepSeek Coder |
| AI 对话 | DeepSeek Chat 界面 |
| 项目记忆文件 | 项目目录下的上下文文件（需手动管理） |
| 子窗口 | 新开 Chat 会话 |

### 通义灵码（Tongyi Lingma）

| opc-starter-kit 概念 | 通义灵码等效 |
|---------------|------------|
| AI 编程工具 | 通义灵码 IDE 插件 |
| AI 对话 | 通义灵码对话窗口 |
| 项目记忆文件 | 项目上下文文件（通过 `.lingma` 目录管理） |
| 子窗口 | 新开对话 |

### Kimi

| opc-starter-kit 概念 | Kimi 等效 |
|---------------|---------|
| AI 编程工具 | Kimi 代码助手 |
| AI 对话 | Kimi Chat 界面 |
| 项目记忆文件 | 上传项目文件作为上下文 |
| 子窗口 | 新开会话 |

### Cursor

| opc-starter-kit 概念 | Cursor 等效 |
|---------------|------------|
| AI 编程工具 | Cursor IDE |
| AI 对话 | Cursor Chat / Composer |
| 项目记忆文件 | `.cursorrules` / `.cursor/rules/` |
| 子窗口 | 新开 Composer 会话 |

### GitHub Copilot / Copilot Chat

| opc-starter-kit 概念 | Copilot 等效 |
|---------------|-------------|
| AI 编程工具 | GitHub Copilot |
| AI 对话 | Copilot Chat |
| 项目记忆文件 | `.github/copilot-instructions.md` |
| 子窗口 | 新开 Chat 会话 |

### Windsurf

| opc-starter-kit 概念 | Windsurf 等效 |
|---------------|-------------|
| AI 编程工具 | Windsurf IDE |
| AI 对话 | Cascade 对话 |
| 项目记忆文件 | `.windsurfrules` |
| 子窗口 | 新开 Cascade 会话 |

---

## Skill 安装通用说明

opc-starter-kit 是一个基于 Markdown 的 Skill 文件，不依赖特定平台的扩展机制。

### 通用安装步骤

1. 将 `SKILL.md` 放置在你的项目的 AI 工具可读取的位置
2. 将 `references/` 目录和 `scripts/` 目录一并复制
3. 确保 AI 工具能够在对话中读取 `SKILL.md` 的内容
4. 在支持 Skill 系统的工具（如 your AI coding tool）中，将整个目录放到 `.your AI coding tool/skills/opc-starter-kit/`

### 状态和产出文件

`opc-starter-kit` 生成的文件与平台无关：
- `.opc-state.json` — 项目根目录的状态文件
- `docs/` — 所有阶段产出
- 这些文件是纯文本/Markdown/JSON，任何工具都能读取

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