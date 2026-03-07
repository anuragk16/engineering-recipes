# Hybrid KB Spec Reconciliation

## Purpose

This note reconciles the pre-existing `engineering-recipes` numbered knowledge-base recipe with the temporary flat-layout phase introduced during the hybrid KB work.

## Current vs Target

| Area | Current repo state | Hybrid V1 target | Decision |
|---|---|---|---|
| Core layout | Both numbered and flat artifacts exist in repo history | Numbered directories under `knowledge-base/` | New installs use numbered layout; flat layout is compatibility only |
| Entry file | `knowledge-base/00-master.md` and temporary `00-index.md` references | `knowledge-base/00-master.md` | Standardize on `00-master.md`; `00-index.md` is compatibility only |
| Section files | Numbered section directories plus temporary flat section files | `01-business-flows/00-index.md`, `02-architecture/00-index.md`, `03-risk-model/00-index.md`, `04-active-sprint/00-index.md` | New installs use numbered section directories |
| Runtime contract | Mostly documented in `CLAUDE.md` plus `.kb-config.yml` | `.kb-config.yml` plus mirrored `CLAUDE.md` guidance | `.kb-config.yml` is source of truth; `CLAUDE.md` mirrors read rules |
| Sprint file | `04-active-sprint/00-index.md` and temporary `active-sprint.md` references | `04-active-sprint/00-index.md` | Standardize on numbered sprint file |
| Advanced memory | Optional modules under `advanced/` | Optional modules under `advanced/` | Keep as explicit optional templates |
| Automation | Manual validation only | Manual validation only | Do not ship sync automation in the starter kit |

## Decision Gates and Frozen Outcomes

### DG-1: Canonical file structure
- **Decision:** Numbered tree layout is canonical.
- **V1 canonical for new projects:** numbered directories under `knowledge-base/`.
- **Compatibility support:** flat-file layout remains readable for projects scaffolded during the temporary transition.

### DG-2: Canonical entry-point name
- **Decision:** Standardize on `knowledge-base/00-master.md`.
- **Compatibility support:** agents may fall back to `knowledge-base/00-index.md` when needed.

### DG-3: Agent loading contract source of truth
- **Decision:** Use both, with `.kb-config.yml` as the source of truth.
- **Role of `CLAUDE.md`:** human-readable and tool-specific adapter guidance only.

### DG-4: Sprint file naming and scope
- **Decision:** Adopt `knowledge-base/04-active-sprint/00-index.md` as the V1 canonical sprint file.
- **Compatibility support:** agents may fall back to `knowledge-base/active-sprint.md`.

### DG-5: Pilot scope for IAGES
- **Decision:** Pilot IAGES backend first.
- **Reason:** it already has agent configuration and is the smaller org-level validation unit for the KB contract.
- **Follow-up:** frontend can be added after backend validation.

### DG-6: Automation cadence
- **Decision:** manual / agent-driven cadence.
- **Supported modes in this repo:** scaffold + validate only.

## Migration Impact

### For new projects
- Use the numbered hybrid contract.
- Generate `.kb-config.yml` and append KB rules to the project root `CLAUDE.md`.

### For projects created during the flat-layout phase
- No forced rewrite in V1.
- Updated agents and validator support the flat structure.
- Migration to the numbered structure can happen project-by-project.

## Agent Behavior Differences

| Agent | Compatibility behavior | Hybrid V1 behavior |
|---|---|---|
| `implementation-planner` | Reads flat `00-index.md` and flat section files when numbered files are absent | Reads `00-master.md`, follows `.kb-config.yml`, loads numbered sections first |
| `implementation-executor` | Reads flat `architecture.md` when numbered file is absent | Reads `02-architecture/00-index.md` |
| `business-analyst` | Reads flat `business-flows.md` when numbered file is absent | Reads `01-business-flows/00-index.md` |
| `knowledge-base-manager` | Supports flat `active-sprint.md` as fallback | Prefers `04-active-sprint/00-index.md` and creates detail files inside numbered folders when needed |

## Scope of This Implementation

Implemented in this repo:
- V1 hybrid spec using numbered layout
- Tier 1 and Tier 2 templates
- `.kb-config.yml` contract
- scaffold prompt and reusable scripts
- agent documentation updates
- KB validation helper

Not implemented in this repo:
- direct migration of Sneha or IAGES repositories
- automatic sprint sync or scheduling
