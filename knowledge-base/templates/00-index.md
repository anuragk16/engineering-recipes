# Knowledge Base Index: {{PROJECT_NAME}}

## Purpose
This is the only required first read for agents. Keep it short.

## Project Snapshot
- Project: {{PROJECT_NAME}}
- One-line summary: {{PROJECT_SUMMARY}}
- Primary stack: {{PRIMARY_STACK}}
- Owners: {{PROJECT_OWNERS}}
- KB version: 1

## Files
- `architecture.md`: System boundaries, module map, and non-negotiable architecture rules.
- `business-flows.md`: Core user journeys and business rules that affect implementation.
- `active-sprint.md`: Current delivery state, active work, blockers, and recently completed items.
- `risks.md`: Known technical, operational, and security-sensitive risks.
- `advanced/decision-log.md`: Optional. Append-only architecture and product decisions.
- `advanced/incident-log.md`: Optional. Append-only incident summaries and prevention notes.
- `advanced/feature-history.md`: Optional. Shipped feature history and notable outcomes.
- `advanced/integration-map.md`: Optional. External systems, auth methods, and failure surfaces.
- `advanced/metrics.md`: Optional. Baseline metrics and SLO/SLA context.
- `advanced/known-constraints.md`: Optional. Hard technical, contractual, or regulatory constraints.

## Loading Rules
- Code review: load `architecture.md`, `risks.md`
- Planning: load `business-flows.md`, `architecture.md`, `active-sprint.md`
- Sprint work: load `active-sprint.md`
- Onboarding: load all Tier 1 files
- Incident response: load `risks.md`, then `advanced/incident-log.md` if enabled

## Writing Rules
- Treat KB content as read-only unless you are the designated KB maintenance flow.
- Prefer `.kb-config.yml` as the runtime source of truth for enabled advanced modules.
- If this flat-file contract is absent, legacy projects may still use `00-master.md` and the numbered directories.
