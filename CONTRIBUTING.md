# Contributing to opc-starter-kit

Thank you for your interest in contributing! This project extracts and refines Anthropic's Founder's Playbook for one-person companies into an installable AI discipline skill. Your experience can make it better.

---

## Ways to Contribute

### 1. Report a New Failure Mode

Found a startup failure pattern not covered in our [27 failure modes](FAILURE_MODES.md)? We want to hear about it.

- Use the [Failure Mode Report](.github/ISSUE_TEMPLATE/failure_mode_report.md) issue template
- Describe the failure mode, its consequences, and (if possible) a defensive mechanism

### 2. Share a Community Pattern

Have real-world experience navigating one of the four startup stages? Share it:

- Use the [Community Pattern](.github/ISSUE_TEMPLATE/community_pattern.md) issue template
- Patterns will be curated into `references/community-patterns.md`

### 3. Contribute Tool Adaptations

Using a non-Claude AI tool? Help us expand `references/tool-adaptations.md`:

- Map concepts to your tool's terminology
- Share workflow-specific adaptations
- Example: How does "architecture context document" work in your tool?

### 4. Improve Documentation

- Fix typos or unclear language
- Add examples or scenarios
- Translate content to additional languages

### 5. Report Bugs

- Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) issue template
- Include your stage, the command you used, and what happened vs. what you expected

---

## Contribution Guidelines

### Content Principles

1. **Evidence-based**: All failure modes and defensive mechanisms should reference real patterns, not theoretical concerns
2. **Specific over generic**: "Users said they'd pay but didn't" is better than "PMF is hard"
3. **No tool lock-in**: Content should be usable across AI tools. Use generic terms ("AI coding tool") rather than product-specific names ("Claude Code"), except in tool-adaptations.md
4. **Respect the playbook**: All content should be traceable to Anthropic's Founder's Playbook methodology. We don't invent startup advice. The playbook is Anthropic's official guide for AI-native one-person companies; Chinese translation by 花叔 (Huashu) x Claude Code, for personal study only.

### File Organization

- **27 failure modes**: Edit [FAILURE_MODES.md](FAILURE_MODES.md)
- **Stage-specific guidance**: Edit the corresponding `references/stage-N-xxx.md`
- **Tool adaptations**: Edit `references/tool-adaptations.md`
- **Community patterns**: Will be curated into `references/community-patterns.md` from issue reports

### Language

- Primary documentation: Chinese (Simplified)
- Secondary documentation: English
- All contributions should be in Chinese or bilingual (Chinese + English)
- If you're contributing in English only, we'll help with the Chinese translation

### Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Ensure the SKILL.md and references/ files are consistent
5. Submit a PR with a clear description of what changed and why

---

## Code of Conduct

- Be respectful and constructive
- Focus on helping founders make better decisions
- Share experiences, not judgments
- No promotional content for specific products or services

---

## Questions?

Open a [GitHub Discussion](../../discussions) for:
- Q&A about how to use the skill
- Sharing stage-specific experiences
- Feature requests
- General conversation about AI-era startup discipline
