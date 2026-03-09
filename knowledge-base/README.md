# Hybrid Knowledge Base

This directory contains the V1 hybrid knowledge-base starter kit for project-local AI context.

## What This Recipe Provides

- A versioned KB contract: [SPEC.md](SPEC.md)
- A reconciliation note across older layouts: [SPEC-RECONCILIATION.md](SPEC-RECONCILIATION.md)
- Governance rules: [GOVERNANCE.md](GOVERNANCE.md)
- Pilot scope note: [KB-CONTRACT-V1-PILOT-SCOPE.md](KB-CONTRACT-V1-PILOT-SCOPE.md)
- Adoption guide: [ADOPTION-GUIDE.md](ADOPTION-GUIDE.md)
- Review checklist: [REVIEW-CHECKLIST.md](REVIEW-CHECKLIST.md)
- Tier 1 and Tier 2 templates under [`templates/`](templates/)
- Downstream workflow assets under [`project-files/`](project-files/)
- A scaffold script for installing the KB into another project
- A validation script for checking a KB installation
- A copy-paste install prompt for agent-based setup

## Canonical V1 Layout

New projects should use the numbered-flat layout below inside their own repo:

```text
knowledge-base/
├── 00-master.md
├── 01-business-flows.md
├── 02-architecture.md
├── 03-risk-model.md
├── 04-active-sprint.md
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
- `01-business-flows.md`
- `02-architecture.md`
- `03-risk-model.md`
- `04-active-sprint.md`

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
  --enable decision-log,incident-log \
  --install-kb-manager \
  --install-kb-process
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
- `00-master.md` references the numbered-flat Tier 1 files
- canonical Tier 1 files contain front matter and the required shared headings
- front matter freshness and owner links can be evaluated
- append-only logs use a recognizable entry format
- enabled Tier 2 modules in config have matching files
- older numbered-tree and legacy-flat projects still validate as compatibility installs

Warnings are used for freshness, owner-link, and duplication hygiene issues so a fresh scaffold can pass before the project is fully populated.

## Why The Numbered-Flat Layout

- `00-master.md` stays small and cheap to read.
- Tier 1 section files are separate, so agents do not need to load the full KB.
- Tier 1 section files are single write targets, so KB updates are more reliable than index-plus-child-file trees.
- Tier 2 remains optional for deeper historical context.

## Compatibility Support

Older projects may still use one of these layouts:

### Numbered tree
- `00-master.md`
- `01-business-flows/00-index.md`
- `02-architecture/00-index.md`
- `03-risk-model/00-index.md`
- `04-active-sprint/00-index.md`

### Legacy flat
- `00-index.md`
- `business-flows.md`
- `architecture.md`
- `risks.md`
- `active-sprint.md`

Those layouts remain readable and valid as temporary compatibility paths for existing projects.
New projects should use the numbered-flat contract.

## Recommended Downstream Workflow Assets

For downstream project repos, the starter kit also ships reusable workflow files:
- [project-files/KB-PROCESS.md](project-files/KB-PROCESS.md)

These are not part of the strict KB file contract, but they make KB updates part of normal delivery.
