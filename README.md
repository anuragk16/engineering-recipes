# Engineering Recipes

Reusable, opinionated engineering practices and automation patterns used across ColoredCow projects.

This repository is a reference library.
Individual projects opt into recipes by copying or referencing them.

## Recipes

| Category | Recipe | Description |
|----------|--------|-------------|
| Automated Code Review | [automated-code-review/](automated-code-review/) | Automated code review patterns |
| Claude Agents | [claude/agents/implementation-planner/](claude/agents/implementation-planner/) | Claude Code agent that creates 4-hour task breakdown implementation plans from feature requirements and posts them to GitHub issues |
| Claude Agents | [claude/agents/implementation-executor/](claude/agents/implementation-executor/) | Claude Code agent that executes an existing implementation plan from a GitHub issue — implementing tasks sequentially, committing after each, and opening a PR |
| Claude Agents | [claude/agents/business-analyst/](claude/agents/business-analyst/) | Claude Code agent that refines raw or ambiguous feature requests into clear, business-aligned, non-technical requirement documents |
| Claude Agents | [claude/agents/knowledge-base-manager/](claude/agents/knowledge-base-manager/) | Claude Code agent that syncs the project knowledge base with GitHub issue state — the only agent with write access to the knowledge base |
| Knowledge Base | [knowledge-base/](knowledge-base/) | Templatized AI knowledge base that installs into any project with a single prompt, giving agents structured project context (business flows, architecture, risk model, active sprint) |
