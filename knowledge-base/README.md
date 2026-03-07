# Hybrid Knowledge Base

This directory contains the V1 hybrid knowledge-base starter kit for project-local AI context.

## What This Recipe Provides

- A versioned KB contract: [SPEC.md](SPEC.md)
- A reconciliation note against the temporary flat-layout phase: [SPEC-RECONCILIATION.md](SPEC-RECONCILIATION.md)
- Governance rules: [GOVERNANCE.md](GOVERNANCE.md)
- Review checklist: [REVIEW-CHECKLIST.md](REVIEW-CHECKLIST.md)
- Tier 1 and Tier 2 templates under [`templates/`](templates/)
- A scaffold script for installing the KB into another project
- A validation script for checking a KB installation
- A copy-paste install prompt for agent-based setup

## Canonical V1 Layout

New projects should use the numbered tree layout below inside their own repo:

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

## Tiers

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

## Source of Truth

- Runtime source of truth: `knowledge-base/.kb-config.yml`
- Human-facing adapter guidance: project root `CLAUDE.md`

## Quick Start

### One command scaffold

```bash
python3 knowledge-base/scripts/scaffold_hybrid_kb.py /path/to/target-project \
  --enable decision-log,incident-log
```

After setup, move into the target project root and validate the KB:

```bash
cd /path/to/target-project
python3 knowledge-base/scripts/validate_hybrid_kb.py .
```

### Validate an installed KB

```bash
python3 knowledge-base/scripts/validate_hybrid_kb.py /path/to/target-project
```

### Use the install prompt

See [prompts/install-hybrid-kb.md](prompts/install-hybrid-kb.md).

## Validation After Setup

The starter kit copies `validate_hybrid_kb.py` into the target project's `knowledge-base/scripts/` directory.

Run this from the target project root after installation:

```bash
python3 knowledge-base/scripts/validate_hybrid_kb.py .
```

The validator checks:
- required Tier 1 files exist
- `.kb-config.yml` has the minimum contract keys
- `00-master.md` references the numbered Tier 1 section files
- enabled Tier 2 modules in config have matching files
- flat-layout projects created during the temporary phase still validate as compatibility installs

## Why The Numbered Tree Layout

- `00-master.md` stays small and cheap to read.
- Section `00-index.md` files stay concise and task-focused.
- Deeper details can live in child files inside the matching numbered folder.
- Agents can load only the one section they need instead of pulling broad narrative files.

## Flat-Layout Compatibility

Some projects may still have the temporary flat layout:
- `00-index.md`
- `business-flows.md`
- `architecture.md`
- `risks.md`
- `active-sprint.md`

That layout remains readable and valid as a temporary compatibility path for projects created during the transition.
New projects should use the numbered tree contract.
