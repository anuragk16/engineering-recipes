# Hybrid Knowledge Base

This directory contains the V1 hybrid knowledge-base starter kit for project-local AI context.

## What This Recipe Provides

- A versioned KB contract: [SPEC.md](SPEC.md)
- A reconciliation note against the legacy numbered layout: [SPEC-RECONCILIATION.md](SPEC-RECONCILIATION.md)
- Governance rules: [GOVERNANCE.md](GOVERNANCE.md)
- Review checklist: [REVIEW-CHECKLIST.md](REVIEW-CHECKLIST.md)
- Tier 1 and Tier 2 templates under [`templates/`](templates/)
- A scaffold script for installing the KB into another project
- A validation script for checking a KB installation
- An active sprint sync script for manual or agent-driven updates
- A copy-paste install prompt for agent-based setup

## Canonical V1 Layout

New projects should use the flat-file layout below inside their own repo:

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

## Tiers

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

## Source of Truth

- Runtime source of truth: `knowledge-base/.kb-config.yml`
- Human-facing adapter guidance: project root `CLAUDE.md`

## Quick Start

### One command scaffold

```bash
python knowledge-base/scripts/scaffold_hybrid_kb.py /path/to/target-project \
  --enable decision-log,incident-log
```

### Validate an installed KB

```bash
python knowledge-base/scripts/validate_hybrid_kb.py /path/to/target-project
```

### Use the install prompt

See [prompts/install-hybrid-kb.md](prompts/install-hybrid-kb.md).

## Sprint Automation

`active-sprint.md` is the main automation target.

### Manual sync

```bash
python knowledge-base/scripts/sync_active_sprint.py /path/to/project --repo owner/name
```

### Scheduled sync

No workflow template is shipped in `engineering-recipes`.
If a downstream project wants scheduled sync, it should add its own automation around `knowledge-base/scripts/sync_active_sprint.py`.

## Legacy Compatibility

This repo previously used a numbered layout:
- `00-master.md`
- `01-business-flows/00-index.md`
- `02-architecture/00-index.md`
- `03-risk-model/00-index.md`
- `04-active-sprint/00-index.md`

That layout remains supported as a temporary compatibility path for existing projects.
New projects should use the flat-file hybrid contract.
