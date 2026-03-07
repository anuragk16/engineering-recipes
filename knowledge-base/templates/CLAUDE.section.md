## Knowledge Base

This project stores structured context in `knowledge-base/`.

### Reading Rules
- Read `knowledge-base/00-master.md` first.
- If `knowledge-base/.kb-config.yml` exists, use it as the source of truth for enabled modules and loading defaults.
- Load only the files needed for the current task.
- Treat KB files as read-only unless you are the designated KB maintenance flow.
- If the numbered KB does not exist, you may fall back to the flat-file layout if present.

### Graceful Degradation
If no knowledge base exists, proceed normally without KB-aware behavior.
