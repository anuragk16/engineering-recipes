# Hybrid KB Spec Reconciliation

## Purpose

This note reconciles the pre-existing `engineering-recipes` knowledge-base recipe with the hybrid model defined in the March 6, 2026 review and follow-up Google Doc.

## Current vs Target

| Area | Current repo state | Hybrid V1 target | Decision |
|---|---|---|---|
| Core layout | Numbered directories under `knowledge-base/` | Flat project-local files under `knowledge-base/` | Support both temporarily; new installs use flat layout |
| Entry file | `knowledge-base/00-master.md` | `knowledge-base/00-index.md` | Standardize on `00-index.md`; keep `00-master.md` as legacy alias |
| Section files | `01-business-flows/00-index.md`, etc. | `business-flows.md`, `architecture.md`, `risks.md`, `active-sprint.md` | New installs use flat files |
| Runtime contract | Mostly documented in `CLAUDE.md` | `.kb-config.yml` plus mirrored `CLAUDE.md` guidance | `.kb-config.yml` is source of truth; `CLAUDE.md` mirrors read rules |
| Sprint file | `04-active-sprint/00-index.md` | `active-sprint.md` | Standardize on `active-sprint.md`; updater supports legacy fallback |
| Advanced memory | Not formalized as optional modules | Tier 2 optional modules | Add as explicit optional templates |
| Automation | Agent-only guidance | Agent plus reusable updater script | Implement reusable sync script; downstream projects may add their own scheduling |

## Decision Gates and Frozen Outcomes

### DG-1: Canonical file structure
- **Decision:** Support both temporarily with a migration path.
- **V1 canonical for new projects:** flat files under `knowledge-base/`.
- **Legacy support:** numbered-directory layout remains readable by updated agents.

### DG-2: Canonical entry-point name
- **Decision:** Standardize on `knowledge-base/00-index.md`.
- **Legacy support:** agents may fall back to `knowledge-base/00-master.md` when needed.

### DG-3: Agent loading contract source of truth
- **Decision:** Use both, with `.kb-config.yml` as the source of truth.
- **Role of `CLAUDE.md`:** human-readable and tool-specific adapter guidance only.

### DG-4: Sprint file naming and scope
- **Decision:** Adopt `knowledge-base/active-sprint.md` as the V1 canonical sprint file.
- **Legacy support:** updater and agents may fall back to `knowledge-base/04-active-sprint/00-index.md`.

### DG-5: Pilot scope for IAGES
- **Decision:** Pilot IAGES backend first.
- **Reason:** it already has agent configuration and is the smaller org-level validation unit for the hybrid contract.
- **Follow-up:** frontend can be added after backend validation.

### DG-6: Automation cadence
- **Decision:** manual / agent-driven cadence.
- **Supported modes in this repo:** on-demand sync via script or KB maintenance agent.
- **Note:** downstream projects may add their own scheduling separately.

## Migration Impact

### For new projects
- Use the flat-file hybrid contract only.
- Generate `.kb-config.yml` and append KB rules to the project root `CLAUDE.md`.

### For existing projects on the numbered layout
- No forced rewrite in V1.
- Updated agents and updater scripts support the legacy structure.
- Migration to the flat-file structure is optional and can happen project-by-project.

## Agent Behavior Differences

| Agent | Legacy behavior | Hybrid V1 behavior |
|---|---|---|
| `implementation-planner` | Reads `00-master.md` and specific numbered sections | Reads `00-index.md`, follows `.kb-config.yml`, falls back to legacy if needed |
| `implementation-executor` | Reads legacy architecture section | Reads `architecture.md`, falls back to legacy architecture section |
| `business-analyst` | Reads legacy business-flows section | Reads `business-flows.md`, falls back to legacy business-flows section |
| `knowledge-base-manager` | Writes sprint rows into legacy sprint file | Prefers `active-sprint.md`, supports legacy fallback |

## Scope of This Implementation

Implemented in this repo:
- V1 hybrid spec
- Tier 1 and Tier 2 templates
- `.kb-config.yml` contract
- scaffold prompt and reusable scripts
- agent documentation updates
- manual sprint sync helper

Not implemented in this repo:
- direct migration of Sneha or IAGES repositories
- production GitHub auth and scheduling in downstream repos
