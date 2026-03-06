# Claude Agents

This directory contains reusable, templatized Claude Code agents that can be set up in any project.

## Available Agents

| Agent | Description |
|-------|-------------|
| [implementation-planner](agents/implementation-planner/) | Translates feature requests into phased implementation plans using the 4-hour task theory and posts them as GitHub issue comments. |
| [implementation-executor](agents/implementation-executor/) | Takes an existing implementation plan from a GitHub issue and executes it — implementing each task sequentially, committing after each, pushing, and opening a PR. |
| [business-analyst](agents/business-analyst/) | Refines raw or ambiguous requests into clear, business-aligned, non-technical requirement documents with explicit scope and acceptance criteria. |
| [knowledge-base-manager](agents/knowledge-base-manager/) | Syncs the project knowledge base with GitHub issue activity — the only agent with write access to the KB. |

## Knowledge Base Contract

These agents now prefer the hybrid flat-file KB contract:
- entry file: `knowledge-base/00-index.md`
- runtime config: `knowledge-base/.kb-config.yml`
- core files: `architecture.md`, `business-flows.md`, `active-sprint.md`, `risks.md`

Legacy numbered KB layouts remain supported as a fallback for older projects.

## Setting Up Agents in Your Project

> Run the install steps from your project's root directory so the agent can inspect that project directly.

1. Copy the relevant agent markdown file into `.claude/agents/` in the target project.
2. If the target project uses the hybrid knowledge base, also install the KB starter kit from [`knowledge-base/`](../knowledge-base/).
3. Register the agents in the project's root `CLAUDE.md` if needed.

For KB installation guidance, start with [knowledge-base/README.md](../knowledge-base/README.md).
