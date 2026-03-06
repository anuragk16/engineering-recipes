# Install Hybrid Knowledge Base

Paste the following prompt into the target project's coding agent session from the project root.

```text
I want to install the hybrid knowledge base starter kit from the `https://github.com/anuragk16/engineering-recipes` repository into this project.

Source directory to read from:
- `knowledge-base/templates/`
- `knowledge-base/templates/advanced/`
- `knowledge-base/templates/.kb-config.yml`
- `knowledge-base/templates/CLAUDE.section.md`
- `knowledge-base/scripts/validate_hybrid_kb.py`
- `claude/agents/knowledge-base-manager/knowledge-base-manager.md`
- `claude/agents/knowledge-base-manager/README.md`

Follow these steps exactly:

1. Explore this project shallowly:
   - README
   - top-level config files
   - top-level directory structure
   - the 5 most recent git commits
2. Check whether `knowledge-base/` already exists.
   - If it exists, do not overwrite files silently. Show me what exists and ask how to proceed.
3. Create `knowledge-base/` using the flat-file hybrid contract:
   - `00-index.md`
   - `architecture.md`
   - `business-flows.md`
   - `active-sprint.md`
   - `risks.md`
   - `.kb-config.yml`
4. Enable Tier 2 files only if the project clearly needs them or I explicitly ask for them.
5. Copy the reusable helper scripts into `knowledge-base/scripts/`.
6. Check whether `.claude/agents/knowledge-base-manager.md` already exists.
   - If it does not exist:
     - create `.claude/agents/` if needed
     - copy `claude/agents/knowledge-base-manager/knowledge-base-manager.md` into `.claude/agents/knowledge-base-manager.md`
   - If it already exists: do not overwrite it silently. Mention that it already exists in your summary.
7. Replace placeholders only when you can infer values confidently from the codebase.
8. If a value cannot be inferred confidently, leave the placeholder unchanged and list it in your summary. Do not guess.
9. Add the `Knowledge Base` section from `CLAUDE.section.md` to the project root `CLAUDE.md` if it is not already present.
10. Ensure the project root `CLAUDE.md` has a `Custom Agents` section that includes `knowledge-base-manager`.
    - If the section is missing, create it.
    - If the section exists but does not list `knowledge-base-manager`, add it.
    - Do not duplicate an existing entry.
11. At the end, show me:
   - files created
   - placeholders inferred
   - placeholders left unresolved
   - Tier 2 modules enabled
   - whether `knowledge-base-manager` agent was installed or already existed
   - the exact validation command I should run from this project's root:
     `python3 knowledge-base/scripts/validate_hybrid_kb.py .`
```
