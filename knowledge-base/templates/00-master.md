<!--
  PURPOSE: Single entry point for the entire knowledge base.
  Agents ALWAYS read this file first. Based on the task, load only the
  sections relevant to that task. Never load all sections at once.
-->

# Knowledge Base: {{PROJECT_NAME}}

**Last Updated:** {{LAST_UPDATED_DATE}}
**Tech Stack:** {{TECH_STACK}}

## Sections

| Section | File | Summary |
|---------|------|---------|
| Business Flows | `01-business-flows.md` | Core user journeys, flows, and business rules for {{PROJECT_NAME}} |
| Architecture | `02-architecture.md` | Architectural patterns, boundaries, integrations, and implementation constraints |
| Risk Model | `03-risk-model.md` | Risk classification, fragile areas, and review/testing expectations |
| Active Sprint | `04-active-sprint.md` | Current sprint goal, active issues, blockers, and recent completions |
| Advanced Memory | `advanced/` | Optional logs and historical context loaded only when needed |
