# 27 Failure Modes Guarded by opc-starter-kit

> Extracted and refined from **Anthropic The Founder's Playbook (May 2026)** — Anthropic's official guide for building AI-native one-person companies. Chinese translation by 花叔 (Huashu) x Claude Code, for personal study only.
>
> 提炼封装自 **Anthropic 创始人行动手册（2026.05）**——Anthropic 官方发布的、面向 AI-Native 一人公司的创始人行动指南。中文译本来自花叔 x Claude Code，仅供个人学习与内部研究使用，不做商业发行。

---

## Ideation Stage — 9 Failure Modes / 想法阶段 — 9 个失败模式

### #1: Treating "building" as "validation" / 把"造"误当作"验证"

> 当技术障碍被移除，激情冲昏头的创始人很可能跳过创业旅程里最重要的工作：验证自己的想法是不是人们真正需要、也真正会用的方案。即便在当下的 agentic 编程时代之前，也有 42% 的创业公司失败，是因为做了没人想要的东西。
> —— Anthropic 创始人行动手册 Ch.3「想法阶段·挑战」，花叔译本

**Data**: 42% startup failure rate; with AI, it's only going higher.

**Typical scenario**:
Have an idea → Let AI write code → Built it → Nobody wants it

**How this skill defends**:
When you say "help me write code," the skill first checks whether the current stage's exit criteria have been met. If not, it redirects you to the validation process instead of jumping into building.

---

### #2: Premature scaling / 过早规模化

> 在还没有真正验证一条产品路径值得投入之前，你就已经把自己锁在这条路径上。Agentic 编程助手太强大了，执行很容易跑在问题-方案匹配验证之前，而你根本没意识到自己已经偏航。
> —— Anthropic 创始人行动手册 Ch.3「想法阶段·挑战」，花叔译本

**Typical scenario**:
You start building full features before confirming problem-solution fit. AI happily generates code for an unvalidated direction.

**How this skill defends**:
Any attempt to enter the next stage's work before exit criteria are met triggers an active warning and redirects you back to the current stage.

---

### #3: Confirmation bias + AI amplifier / 确认偏误加外挂

> 确认偏误一直是创业里的职业病：创始人天然对自己的想法充满热情。现在 AI 工具给确认偏误加了很强的外挂。让 AI 验证你的创业想法，它能找出佐证；让它估算潜在市场，它能找到让 TAM 看起来值得融资的数字。一个不问难题的创始人，现在能比以往任何时候都更快构建出一套精致、看似研究充分的坏点子论据，自己还觉得是在做尽调。
> —— Anthropic 创始人行动手册 Ch.3「客观性丧失」，花叔译本

**Typical scenario**:
You ask AI to validate your idea → It finds supporting evidence → You feel like you've done due diligence → Actually, you're self-deceiving.

**How this skill defends**:
Mandatory devil's advocate at every stage. The AI must write the most compelling counter-arguments from the opponent's perspective, with at least 3 dimensions and 3 specific arguments per dimension.

---

### #4: Vague problem statement / 问题陈述模糊

> "大家做报销很头痛"是观察；"中型公司的财务经理每周要花 4 个小时以上核对报销提交，因为现有工具不和会计软件打通"才是一个可被测试的假设。
> —— Anthropic 创始人行动手册 Ch.3「想法阶段·目标」，花叔译本

**Typical scenario**:
You describe the problem in general terms → No way to test if it's real → Build a solution for an undefined problem.

**How this skill defends**:
On first idea input, the skill guides you to transform vague observations into testable hypotheses: Who + How frequent + How severe + Current workaround.

---

### #5: Competitor neglect / 竞品忽视

> 创业公司有一种特有现象叫"竞品忽视"：你太专注自己的愿景和执行，于是系统性低估了同一赛道里别人在做什么。
> —— Anthropic 创始人行动手册 Ch.3「市场研究与竞争格局梳理」，花叔译本

**Typical scenario**:
You list competitors → Only the weakest ones → Conclude you're unique → Actually, stronger competitors already solve the problem better.

**How this skill defends**:
Forces a 4-layer competitive landscape (direct/indirect/potential acquirers/adjacent players). For each competitor, writes "why they would win" arguments — not the easiest-to-refute version.

---

### #6: Asking the wrong interview questions / 访谈问错问题

> 新手创始人最常犯的错，是问一个泛泛的未来式开放问题，比如"你会用这样的东西吗？"而不是追问相关的过去，比如"跟我讲讲你上一次处理这个问题的过程"。
> —— Anthropic 创始人行动手册 Ch.3「问什么」，花叔译本

**Typical scenario**:
Users say "yes, I'd use that" → You think you have validation → Actually, people are just being polite or speculating.

**How this skill defends**:
Reviews your draft interview questions, flags leading, future-oriented, too-broad, and social-desirability-bias questions, and provides corrected versions.

---

### #7: Post-interview interpretation bias / 访谈后解释偏差

Based on the playbook's Ch.3 guidance on post-interview analysis: founders tend to fit data into what they want to hear rather than what the data actually shows.

**Typical scenario**:
5 interviews done → You notice confirming evidence more → Conclude the hypothesis is validated → Actually, disconfirming evidence was there but you ignored it.

**How this skill defends**:
Every 5 interviews, produces two lists: evidence supporting the hypothesis vs. evidence challenging it. If the first list is noticeably longer, asks: "Is this asymmetry from the data itself, or from what you were hoping to find?"

---

### #8: Over-waiting for certainty / 过度等待确定性

> 一味等待确定本身就是一种失败模式。但你需要足够多的质性证据，让投入做 MVP 看起来是有理有据的决定，而不是一次信仰行动。
> —— Anthropic 创始人行动手册 Ch.3「想法阶段·退出标准」，花叔译本

**Typical scenario**:
You keep doing more interviews → Never feel "ready" → Never start building → The window closes.

**How this skill defends**:
Exit criteria explicitly state: "You will never have 100% certainty." Helps distinguish "sufficient signal" from "leap of faith."

---

### #9: Solving the original assumed problem, not the validated one / 方案对应的是最初假设的问题而非验证后的问题

> 不是你最初假设的问题，而是验证过程里浮现出来的那一个。两者有时相同，但并不总是。
> —— Anthropic 创始人行动手册 Ch.3「想法阶段·退出标准」，花叔译本

**Typical scenario**:
You validate the problem → The real problem is different → You design a solution for the original assumption → Product solves the wrong problem.

**How this skill defends**:
Before solution concept design, forces a comparison: current validated problem statement vs. original problem statement. Asks: "Which problem does your solution address?"

---

## MVP Stage — 8 Failure Modes / MVP 阶段 — 8 个失败模式

### #10: Agentic technical debt (compounding) / Agentic 技术债（复利型）

> 如果没把规格和架构约束写在 AI 能读到的地方，每次会话都得从零推导一遍基础决策，决策也会一次次发生架构漂移。最后你会得到一个缺乏一致心智模型的代码库。不是因为某一块代码写得糟糕，而是这些零件从一开始就没被设计成能拼到一起。
> —— Anthropic 创始人行动手册 Ch.4「MVP阶段·挑战」，花叔译本

**Typical scenario**:
You code with AI for weeks → No architecture document → Each session makes slightly different assumptions → Codebase lacks a consistent mental model → Parts were never designed to fit together.

**How this skill defends**:
Before any MVP coding, forces generation of an architecture context document. Every coding session must load this document first. After each session, decisions are logged back into it.

---

### #11: Mistaking false PMF for real PMF / 误把假 PMF 当成真 PMF

> 早期势头是创始人能经历的最强心理体验之一……但早期牵引不等于 PMF。发布期的热度可能来自一些短暂因素：创始人的朋友、投资人其他被投公司的潜在买家，或者 Hacker News 上一个标题带来的流量尖峰。
> —— Anthropic 创始人行动手册 Ch.4「MVP阶段·挑战」，花叔译本

**Typical scenario**:
Launch week → Lots of signups → "We have PMF!" → Week 6, usage drops → Early traction was from non-representative sources.

**How this skill defends**:
When you claim PMF, requires passing: Sean Ellis test (>40% "very disappointed") + false positive screening (registered but no activation / revenue but no retention / initial heat but no repeat use).

---

### #12: Zero-friction scope creep / 零摩擦的范围蔓延

> 当开发几乎不费力、近乎免费，总有一个很酷的功能可以加，或一个边缘情况想处理……难点在于，每一项单独的新增看起来都合理。由于 agentic 编程让每一项都很省力，当下并不像范围蔓延。但当产品越过原始边界开始摊大饼，你会失去方向和动量。
> —— Anthropic 创始人行动手册 Ch.4「MVP阶段·挑战」，花叔译本

**Typical scenario**:
"Just one more feature" x 10 → Product sprawls beyond original boundaries → Direction and momentum lost.

**How this skill defends**:
Any new feature suggestion triggers a scope pressure test: requires evidence that "enough users have told us: without this, they can't get value."

---

### #13: Insecure by inexperience / 因经验不足而不安全

> agentic 编程工具生成的是能运行的代码，不是天然安全的代码。功能代码很好判断——要么能跑，要么不能。但安全漏洞在被利用之前是隐形的。
> —— Anthropic 创始人行动手册 Ch.4「MVP阶段·挑战」，花叔译本

**Typical scenario**:
AI-built MVP goes live → Authentication is weak → Data exposure in API responses → Real user data compromised.

**How this skill defends**:
Before any user touches the product, reminds about security review across 4 dimensions: authentication/session handling, API data exposure, input validation/injection risks, dependencies with known vulnerabilities.

---

### #14: Coding without architectural context / 无架构上下文就开始编码

Based on the playbook's Ch.4 guidance: skipping spec documents and architectural decisions means re-explaining the codebase every new session. Without persistent context, AI must infer structural assumptions from scratch.

**Typical scenario**:
New AI session → No context loaded → AI makes different architectural choices → Inconsistent codebase.

**How this skill defends**:
After generating the architecture context document, requires saving it at the project root. Every coding session must load this document. If the file is missing on startup, the skill alerts you.

---

### #15: Not persisting project memory / 未保存项目记忆文件

Based on the playbook's Ch.4 guidance on CLAUDE.md as persistent project memory: without it, AI-generated changes gradually drift from the original vision.

**Typical scenario**:
You close a session → Next session, AI doesn't remember previous decisions → Small deviations accumulate → Vision diluted.

**How this skill defends**:
Architecture document is saved automatically. On each main window startup, the skill checks whether the file exists. If missing, alerts you.

---

### #16: Tracking metrics only after launch / 发布后才开始追踪度量

> 那些把早期牵引误判成 PMF 的创始人，通常也是发布之后才开始追踪数据的人，而且挑选的指标往往是为了证明什么有效，而不是浮现什么无效。
> —— Anthropic 创始人行动手册 Ch.4「MVP阶段·Claude如何帮助」，花叔译本

**Typical scenario**:
Launch → Numbers look good → You pick metrics that confirm success → Miss the metrics that show problems.

**How this skill defends**:
Before MVP launch, forces establishment of a metrics framework: retention baseline, activation criteria, Day 7 and Day 30 targets, and false positive pattern definitions.

---

### #17: Feedback interpretation bias / 反馈解释偏差

> 用户说"这很好，但我希望它还能……"时，需要解释：这是核心需求还是锦上添花？是这一个客户特有的，还是代表某个细分人群？
> —— Anthropic 创始人行动手册 Ch.4「MVP阶段·Claude如何帮助」，花叔译本

**Typical scenario**:
One user asks for a feature → You assume all users need it → Build it → It's only useful for that one customer.

**How this skill defends**:
User feedback analysis guides you to distinguish 4 signal types: core need / nice-to-have / single-customer-specific / onboarding upstream issue.

---

## Launch Stage — 4 Failure Modes / 发布阶段 — 4 个失败模式

### #18: Technical debt comes due / 技术债到期

> MVP 阶段，积累一些技术债是用速度换来的合理代价。到了发布阶段，那笔债开始算利息，拖得越久，修起来越贵。
> —— Anthropic 创始人行动手册 Ch.5「发布阶段·挑战」，花叔译本

**Typical scenario**:
Production traffic increases → MVP shortcuts become bottlenecks → Each fix is more expensive than the last.

**How this skill defends**:
At the launch stage entry, triggers a mandatory tech debt audit: identifies structural weaknesses, test coverage gaps, and prioritized refactoring candidates.

---

### #19: Founder becomes the bottleneck / 创始人成了瓶颈

> 本该一小时完成的决策因等你处理变成一周；支持请求越堆越多，因为只有你知道答案；运营任务只有在你亲自想起来时才发生。
> —— Anthropic 创始人行动手册 Ch.5「发布阶段·挑战」，花叔译本

**Typical scenario**:
Everything goes through you → Support tickets pile up → Only you know the answers → Organization stalls around you.

**How this skill defends**:
Triggers a founder attention audit: lists all workflows/decisions/approvals that pass through you, classifies by "what happens if you're away for a week."

---

### #20: Security and compliance can no longer wait / 安全与合规不能再拖

> MVP 阶段只有少量 beta 用户、生产环境里没有敏感数据时，安全漏洞还是理论风险。但产品一旦进入生产、有真实用户依赖它，假设就会变成非常现实的暴露风险。
> —— Anthropic 创始人行动手册 Ch.5「发布阶段·挑战」，花叔译本

**Typical scenario**:
You've been "meaning to get to" security → Enterprise customer wants to sign → Can't pass their security review → Deal falls through.

**How this skill defends**:
Upgrades security reminders to requirements. Provides an enterprise buyer control checklist. Emphasizes that compliance is an ongoing process, not a one-time project.

---

### #21: Expanding before you're ready / 还没准备好就扩张

> 过早扩张到一个跟原市场差异很大的市场，会引入新的用户行为、合规要求、支付基础设施和基线预期，而你的产品并不是围绕这些设计的。一下子变量太多，你失去了清晰解读自己数据的能力。
> —— Anthropic 创始人行动手册 Ch.5「发布阶段·挑战」，花叔译本

**Typical scenario**:
"Let's expand to Europe!" → New GDPR requirements → Different user behavior → Original users feel neglected → PMF disintegrates.

**How this skill defends**:
When you mention new markets/customer segments, triggers expansion risk check: lists new variables, asks whether you can still clearly read your data, and whether original users are being left behind.

---

## Scale Stage — 6 Failure Modes / 规模化阶段 — 6 个失败模式

### #22: Letting go of operations incorrectly / 把运营层放手出去

> 交得太多、太快（尤其是交给 AI 自动化系统），关键决策可能会在缺少创始人独有上下文的情况下被做出来。但抓得太久，你又会变成瓶颈。
> —— Anthropic 创始人行动手册 Ch.6「规模化阶段·挑战」，花叔译本

**Typical scenario**:
You automate everything → Key decisions made without founder context → Quality drops. Or you hold onto everything → Organization stalls.

**How this skill defends**:
Maps operational bottlenecks. For each workflow, simulates "what happens if you're away for a week?" Identifies where handoff standards and escalation paths need tightening.

---

### #23: Scaling technical operations / 扩张技术运营

> 客户不再只评估你的产品，他们还想知道你的组织能不能成为可靠的基础设施伙伴。
> —— Anthropic 创始人行动手册 Ch.6「规模化阶段·挑战」，花叔译本

**Typical scenario**:
Enterprise customer asks for SLAs and documentation → You don't have any → They go with a more mature competitor.

**How this skill defends**:
Guides a customer buyer expectation gap analysis: documentation, SLAs, support infrastructure, observability.

---

### #24: Scaling organizational functions / 扩张组织职能

Based on the playbook's Ch.6 guidance: scale-stage companies need organizational infrastructure (financial reporting, compliance monitoring, contract management, customer support) regardless of how many people actually run the company.

**Typical scenario**:
Revenue grows → But there's no proper financial reporting → Investors lose confidence → Or compliance gaps block enterprise contracts.

**How this skill defends**:
Lists required organizational functions for the scale stage and identifies gaps.

---

### #25: Missing GTM function / GTM 职能缺失

> 自然增长有天花板，多数规模化阶段的创始人在真正搭过 GTM 职能之前，就会撞上它。信号包括用户曲线变平、获客成本上升，以及销售管道只有在创始人亲自介入时才会推进。
> —— Anthropic 创始人行动手册 Ch.6「规模化阶段·挑战」，花叔译本

**Typical scenario**:
Growth flattens → CAC rises → Sales pipeline only moves when the founder personally intervenes.

**How this skill defends**:
Guides building GTM infrastructure from zero: market segmentation, messaging architecture, sales playbook, investor metrics narrative.

---

### #26: Domain knowledge not externalized / 领域知识未外化

Based on the playbook's Ch.6 guidance: many ultra-lean startup founders are building highly specific apps for real industry problems they've personally experienced. But if that domain expertise stays only in the founder's head, it can't compound into a competitive moat.

**Typical scenario**:
A general competitor enters your vertical → They miss the edge cases you know about → But you never coded those into your product either → No competitive moat from your expertise.

**How this skill defends**:
Guides capturing and structuring domain expertise: find edge cases a general competitor would get wrong, convert them into test cases or product logic.

---

### #27: Moat not deep enough / 护城河不够深

Based on the playbook's Ch.6 guidance on compounding user data and workflow lock-in: data network effects make the product harder to copy, while workflow lock-in makes it harder to abandon. Both are often underutilized.

**Typical scenario**:
A well-funded competitor replicates your product → Users switch easily → You have no defensibility.

**How this skill defends**:
Triggers a 3-part moat audit: data flywheel (how long has it been running) / workflow integration depth (per-customer switching cost) / domain knowledge barrier. Produces a one-page moat narrative.

---

## Found a New Failure Mode?

If you've encountered a failure mode not listed here, please report it!

→ [Open a Failure Mode Report](../../issues/new?template=failure_mode_report.md)

Your experience helps other one-person company founders avoid the same trap.

---

> 本文件内容提炼封装自 Anthropic 创始人行动手册（2026.05）。中文译本来自花叔 x Claude Code，仅供个人学习与内部研究使用，不做商业发行。原版下载请到 [claude.com/blog/the-founders-playbook](https://claude.com/blog/the-founders-playbook)
