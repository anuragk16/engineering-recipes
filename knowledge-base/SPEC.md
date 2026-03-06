# Hybrid KB Specification v1

## Status
- Version: `1`
- Date: `2026-03-06`
- State: `Current`

## Goal

Provide a project-local, token-efficient knowledge base that is easy to scaffold, easy to maintain, and reusable across projects of different stacks and domains.

## Design Principles

1. Project-local storage: each project owns its own `knowledge-base/` directory.
2. Small default footprint: Tier 1 is required and intentionally compact.
3. Optional advanced depth: Tier 2 is opt-in per project.
4. Deterministic reads: agents read the entry file first, then load only mapped files.
5. Minimal write surface: `active-sprint.md` is the main automation target.
6. Tool agnostic content: KB content stays plain Markdown plus lightweight config.

## Canonical Project Layout

```text
knowledge-base/
├── 00-index.md
├── architecture.md
├── business-flows.md
├── active-sprint.md
├── risks.md
├── .kb-config.yml
└── advanced/
    ├── decision-log.md
    ├── incident-log.md
    ├── feature-history.md
    ├── integration-map.md
    ├── metrics.md
    └── known-constraints.md
```

## Tier Model

### Tier 1: Required
- `00-index.md`
- `architecture.md`
- `business-flows.md`
- `active-sprint.md`
- `risks.md`

### Tier 2: Optional
- `advanced/decision-log.md`
- `advanced/incident-log.md`
- `advanced/feature-history.md`
- `advanced/integration-map.md`
- `advanced/metrics.md`
- `advanced/known-constraints.md`

## File Ownership

| File | Owner | Notes |
|---|---|---|
| `00-index.md` | Human | Keep concise; update when KB structure or project metadata changes |
| `architecture.md` | Human | Update on major architecture changes |
| `business-flows.md` | Human | Update when business flows materially change |
| `risks.md` | Human | Update during reviews, incidents, or notable risk discovery |
| `active-sprint.md` | Automation with human review | Primary auto-managed file |
| Tier 2 append-only logs | Human or semi-automated | Prefer append-only entries |

## Read Contract

### Entry-point rule
Agents read `knowledge-base/00-index.md` first.

### Config rule
If `knowledge-base/.kb-config.yml` exists, it is the runtime source of truth for enabled modules and loading defaults.

### Default loading map

| Task | Files |
|---|---|
| Code review | `architecture.md`, `risks.md` |
| Planning | `business-flows.md`, `architecture.md`, `active-sprint.md` |
| Sprint work | `active-sprint.md` |
| Onboarding | All Tier 1 files |
| Incident response | `risks.md`, `advanced/incident-log.md` when enabled |

### No-assumptions rule
If a relevant file is missing or clearly incomplete, agents skip it and continue with available context. They do not fabricate missing context.

### Graceful degradation rule
If `knowledge-base/` or the entry file does not exist, agents proceed without KB-aware behavior.

## Write Contract

1. Only the designated KB maintenance flow may write automated updates.
2. `active-sprint.md` is the default automation target.
3. Tier 2 logs should prefer append-only updates.
4. Agents that consume KB context remain read-only.

## `.kb-config.yml` Contract

Minimum supported keys:
- `version`
- `project.name`
- `enabled_tier2`
- `loading_defaults`
- `auto_update.active_sprint.mode`
- `auto_update.active_sprint.schedule`

## Compatibility Rules

### Legacy read support
Agents and helpers may support these legacy files:
- `knowledge-base/00-master.md`
- `knowledge-base/01-business-flows/00-index.md`
- `knowledge-base/02-architecture/00-index.md`
- `knowledge-base/03-risk-model/00-index.md`
- `knowledge-base/04-active-sprint/00-index.md`

### Legacy write support
Sprint sync helpers may write to legacy sprint files only when the canonical V1 sprint file is absent.

## Automation Cadence

Supported V1 modes:
- `on-demand`
- `manual`
- `agent-driven`

Recommended default:
- `on-demand` via script or KB maintenance agent.

## Rollout Order

1. Sneha pilot
2. IAGES backend pilot
3. Additional projects after contract validation

## Review Checklist

- Is the change Tier 1 or Tier 2?
- Does it increase default token cost?
- Is the file still concise and scannable?
- Is ownership clear?
- Does the change preserve tool-agnostic plain-text content?
