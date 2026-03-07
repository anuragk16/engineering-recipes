# Hybrid KB Specification v1

## Status
- Version: `1`
- Date: `2026-03-07`
- State: `Current`

## Goal

Provide a project-local, token-efficient knowledge base that is easy to scaffold, easy to maintain, and reusable across projects of different stacks and domains.

## Design Principles

1. Project-local storage: each project owns its own `knowledge-base/` directory.
2. Small default footprint: Tier 1 is required and intentionally compact.
3. Optional advanced depth: Tier 2 is opt-in per project.
4. Deterministic reads: agents read the entry file first, then load only mapped files.
5. Tree layout for cheaper reads: index files stay small, while deeper detail lives in child files loaded only when needed.
6. Tool agnostic content: KB content stays plain Markdown plus lightweight config.

## Canonical Project Layout

```text
knowledge-base/
├── 00-master.md
├── 01-business-flows/
│   └── 00-index.md
├── 02-architecture/
│   └── 00-index.md
├── 03-risk-model/
│   └── 00-index.md
├── 04-active-sprint/
│   └── 00-index.md
├── .kb-config.yml
├── advanced/
│   ├── decision-log.md
│   ├── incident-log.md
│   ├── feature-history.md
│   ├── integration-map.md
│   ├── metrics.md
│   └── known-constraints.md
└── scripts/
    └── validate_hybrid_kb.py
```

## Tier Model

### Tier 1: Required
- `00-master.md`
- `01-business-flows/00-index.md`
- `02-architecture/00-index.md`
- `03-risk-model/00-index.md`
- `04-active-sprint/00-index.md`

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
| `00-master.md` | Human | Keep concise; update when KB structure or project metadata changes |
| `01-business-flows/00-index.md` | Human | Keep as an index only; flow detail belongs in child files in `01-business-flows/` |
| `02-architecture/00-index.md` | Human | Keep as an index/summary; detailed design notes belong in child files in `02-architecture/` |
| `03-risk-model/00-index.md` | Human | Keep as an index/summary; detailed risk notes belong in child files in `03-risk-model/` |
| `04-active-sprint/00-index.md` | Human or project-specific process | Current delivery state file |
| Tier 2 append-only logs | Human or semi-automated | Prefer append-only entries |

## Read Contract

### Entry-point rule
Agents read `knowledge-base/00-master.md` first.

### Config rule
If `knowledge-base/.kb-config.yml` exists, it is the runtime source of truth for enabled modules and loading defaults.

### Default loading map

| Task | Files |
|---|---|
| Code review | `02-architecture/00-index.md`, `03-risk-model/00-index.md` |
| Planning | `01-business-flows/00-index.md`, `02-architecture/00-index.md`, `04-active-sprint/00-index.md` |
| Sprint work | `04-active-sprint/00-index.md` |
| Onboarding | All Tier 1 files |
| Incident response | `03-risk-model/00-index.md`, `advanced/incident-log.md` when enabled |

### Section expansion rule
If more detail is needed, agents should open child files inside the relevant numbered directory rather than loading unrelated sections.

### No-assumptions rule
If a relevant file is missing or clearly incomplete, agents skip it and continue with available context. They do not fabricate missing context.

### Graceful degradation rule
If `knowledge-base/` or the entry file does not exist, agents proceed without KB-aware behavior.

## Write Contract

1. Only the designated KB maintenance flow may write automated updates.
2. This starter kit ships scaffold + validation only.
3. New section detail should be written into child files inside the matching numbered directory, then linked from that section's `00-index.md`.
4. Tier 2 logs should prefer append-only updates.
5. Agents that consume KB context remain read-only.

## `.kb-config.yml` Contract

Minimum supported keys:
- `version`
- `project.name`
- `enabled_tier2`
- `loading_defaults`

## Compatibility Rules

### Flat-layout read support
Agents and helpers may support these flat-layout files when the numbered layout is absent:
- `knowledge-base/00-index.md`
- `knowledge-base/business-flows.md`
- `knowledge-base/architecture.md`
- `knowledge-base/risks.md`
- `knowledge-base/active-sprint.md`

### Flat-layout migration support
Projects created during the flat-layout phase may remain readable until migrated. New installs must use the numbered layout.

## Maintenance Cadence

Recommended default:
- update Tier 1 when project reality changes
- add child files under a numbered section when detail grows beyond the index
- use append-only updates for Tier 2 logs where possible
- run the KB validator after setup or structural changes

## Rollout Order

1. Sneha pilot
2. IAGES backend pilot
3. Additional projects after contract validation

## Review Checklist

- Is the change Tier 1 or Tier 2?
- Does it increase default token cost?
- Is the relevant index file still concise and scannable?
- Does detailed content live in the correct section directory?
- Is ownership clear?
- Does the change preserve tool-agnostic plain-text content?
