# Knowledge Base Manager Agent

A Claude Code agent that keeps the project knowledge base in sync with GitHub issue activity. It is the **only** agent with write access to the knowledge base — all other agents are read-only consumers.

## What It Does

- Fetches GitHub issue data in a tiered, token-efficient order (title + state first, body only if needed, PR only if in-review or done)
- Maps each issue to one of four states: Backlog, In Progress, In Review, Done/Closed
- Updates `knowledge-base/04-active-sprint/00-index.md` without duplicating existing entries
- Optionally promotes significant architectural decisions or risk learnings to the relevant KB sections when an issue is closed
- Handles bulk syncs (all open issues) and targeted updates (single issue URL or number)

## Prerequisites

- GitHub CLI (`gh`) must be installed and authenticated: `gh auth status`
- The project knowledge base must be set up at `knowledge-base/` (via the bootstrap prompt in [knowledge-base/README.md](../../knowledge-base/README.md))

## Setup

### 1. Copy the agent file

```bash
cp knowledge-base-manager.md <your-project>/.claude/agents/knowledge-base-manager.md
```

No placeholders to replace — this agent has no `{{PLACEHOLDER}}` values. It works with any project's knowledge base structure out of the box.

### 2. Register in your project's CLAUDE.md

The bootstrap installation prompt (see `knowledge-base/README.md`) adds this automatically. If registering manually, add to your project's `CLAUDE.md`:

```markdown
## Custom Agents

| Agent | When to Use |
|-------|-------------|
| `knowledge-base-manager` | When the user wants to update the knowledge base from a GitHub issue, sync the active sprint, or reflect recent GitHub activity in the KB. |
```

## Usage

Once set up, trigger the agent with natural language:

```
> update the knowledge base for this issue: https://github.com/org/repo/issues/42
> update active sprint items in the knowledge base
> sync knowledge base with recent GitHub activity
> issue #88 is now in review — update the KB
```

## Issue State Mapping

| GitHub State | Action |
|---|---|
| **Backlog** — open, no assignee, no in-progress label | Add to Active Issues table with status `Backlog` |
| **In Progress** — open with assignee or in-progress label | Add/update Active Issues row with status `In Progress` |
| **In Review** — has a linked open PR or review label | Update Active Issues row to `In Review`, link the PR |
| **Done / Closed** — issue state is `CLOSED` | Move from Active Issues to Completed This Sprint |

## Token Efficiency

The agent fetches GitHub data in a prioritized order and stops as soon as it has enough context:

1. Issue title + labels + state + assignees (always fetched)
2. Issue body (only if Tier 1 is insufficient)
3. Linked PR search (only if state is In Review or Done)
4. Issue comments (only if Tier 3 returned nothing)
5. PR diffs / code analysis — **never fetched** unless the user explicitly requests it

Most updates complete using only Tier 1 or Tier 1 + 2.
