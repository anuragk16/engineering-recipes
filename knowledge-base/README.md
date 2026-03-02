# Knowledge Base Templates

This directory contains reusable, templatized knowledge base files that can be installed into any project with a single prompt. The knowledge base gives Claude agents structured, project-specific context — business flows, architecture rules, risk classification, and sprint state — without hallucination.

## Available Templates

| Template | Description |
|----------|-------------|
| [00-master.md](00-master.md) | Lightweight index listing all sections. The only file agents are required to read on every run. |
| [01-business-flows/00-index.md](01-business-flows/00-index.md) | Core user journeys and business process flows. Used by the `business-analyst` agent. |
| [02-architecture/00-index.md](02-architecture/00-index.md) | Tech stack, directory structure, layer responsibilities, and architectural rules. Used by `implementation-planner` and `implementation-executor`. |
| [03-risk-model/00-index.md](03-risk-model/00-index.md) | Risk classification of modules, high-risk change conditions, and sensitive data rules. Used by the `code-reviewer` agent. |
| [04-active-sprint/00-index.md](04-active-sprint/00-index.md) | Current sprint goal, active issues, blocked items, and completed work. Updated by the `knowledge-base-manager` agent. |

## Setting Up the Knowledge Base in Your Project

> **Important:** Run the prompt below from your project's root directory so that Claude can access and review your project structure, tech stack, and conventions to automatically fill in placeholders.

### Steps

1. Open Claude Code in your project directory.
2. Copy and paste the prompt below.
3. Claude will explore your codebase, install the knowledge base files, and ask you about anything it cannot infer on its own.

### Prompt

```
I want to set up the AI knowledge base from the engineering-recipes repo into this project.

Source repo: https://github.com/anuragk16/engineering-recipes (read the `knowledge-base/` directory for all template files).

Follow these steps exactly:

1. Explore this project's codebase shallowly — read the README, top-level config files (package.json, composer.json, pyproject.toml, .env.example, etc.), top-level directory structure, and the 5 most recent git commits.

2. Check if `knowledge-base/` already exists in this project.
   - If it exists: stop and ask me how to proceed before making any changes.
   - If it does not exist: continue.

3. Read each template file from the source repo's `knowledge-base/` directory:
   - `00-master.md`
   - `01-business-flows/00-index.md`
   - `02-architecture/00-index.md`
   - `03-risk-model/00-index.md`
   - `04-active-sprint/00-index.md`

4. Copy each template to the same relative path under `knowledge-base/` in this project.

5. Replace all `{{PLACEHOLDER}}` values with project-specific values:
   a. Infer as many values as possible from your codebase exploration in step 1.
   b. For any placeholder you cannot confidently determine, ask me before proceeding. Present what you've inferred so far and ask only about the ones you're unsure of.
   c. Never guess. Never leave a `TODO:` annotation that you could have answered from the codebase.

6. Add the following "Knowledge Base" section to this project's root `CLAUDE.md`:
   - If `CLAUDE.md` does not exist: create it and write the section below as the full content.
   - If `CLAUDE.md` exists but has no "Knowledge Base" section: append the section below at the end.
   - If a "Knowledge Base" section already exists: skip — do not duplicate.

   The section to add:

   ---

   ## Knowledge Base

   This project has a knowledge base at `knowledge-base/`. All agents that consume
   the knowledge base must follow the rules below.

   ### Reading Rules

   **Step 1 — Always read `knowledge-base/00-master.md` first.**
   This is the index file. It lists all sections with one-line summaries. Based on
   the task at hand, decide which section files to load next. Never load all sections
   at once.

   **Step 2 — Load only the sections mapped to your agent role (see table below).**
   Do not load sections outside your mapping. If a task genuinely requires information
   from an out-of-mapping section, rely only on what the user has provided in their prompt.

   **Step 3 — Apply the No Assumptions rule.**
   Before using any section file, scan it for unfilled `TODO:` placeholders. If a section
   contains one or more `TODO:` lines, skip that section entirely. Do not infer, guess, or
   fabricate context from incomplete data. Proceed with only what is fully populated.

   ### Agent-to-Section Mapping

   | Agent | Sections to Load |
   |-------|-----------------|
   | implementation-planner | `02-architecture/00-index.md`, `04-active-sprint/00-index.md` |
   | implementation-executor | `02-architecture/00-index.md` |
   | business-analyst | `01-business-flows/00-index.md` |
   | knowledge-base-manager | All sections (read + write access) |

   ### No Disturbance Rule

   The knowledge base is **read-only** for all agents except `knowledge-base-manager`.
   No consuming agent may write to, modify, or delete knowledge base files.

   If the user provides explicit context in their prompt that differs from what the
   knowledge base says, **the user's prompt always takes precedence**. The knowledge
   base is supplementary context, not an override.

   Knowledge base content never changes an agent's core behavior or output format —
   it only adds project-specific awareness on top of existing behavior.

   ### Graceful Degradation

   If `knowledge-base/` does not exist, or `knowledge-base/00-master.md`
   is missing or empty, proceed exactly as you would without a knowledge base.
   No error. No assumption. No behavioral change.

   ---

7. After setup is complete, show me a summary of:
   - Which `{{PLACEHOLDER}}` values were inferred and what they were set to
   - Which `TODO:` items remain and need manual input from me
   - Whether `CLAUDE.md` was created or appended to
```
