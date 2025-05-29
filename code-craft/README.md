# CodeCraft

Structured LLM‑assisted software delivery.

## Installation
Add CodeCraft to your local project:

```bash
mkdir code-craft-local && cd code-craft-local && git init && git remote add origin https://github.com/axhamre/code-craft.git && git sparse-checkout set --cone code-craft && git pull origin main && mv code-craft/* . && rm -rf code-craft .git && rm -f .gitignore
```

Run script to copy framework and templates

```bash
bash codecraft/setup.sh
```

## Quick start

1. **Specify** – turn requirements into a technical specification.  
   • Copy `codecraft/framework/planner/SYSTEM_PROMPT.md` into your LLM together with project requirements.  
   • Save the result as `01-specification/technical-specification.md`.

2. **Plan** – convert the specification into an implementation plan.  
   • Copy `codecraft/framework/planner/PLAN_PROMPT.md` into the LLM with the specification.  
   • Save as `02-plan/implementation-plan.md`.

3. **Execute** – implement the plan.  
   • Copy `codecraft/framework/coder/SYSTEM_PROMPT.md` into the LLM with the plan.  
   • Follow tasks, commit each logical unit, update `CHANGELOG.md`.

4. **Verify** – run automated tests (`npm test`, `pytest`, …).  
   • Fix failures; repeat execute ↔ verify until green.

## Directory layout
| path | purpose |
| ---- | ------- |
| `codecraft/framework/` | system prompts and global rules |
| `codecraft/templates/` | prompt templates |
| `codecraft/guides/`    | in‑depth guides |
| `codecraft/examples/`  | reference implementations |

For detailed guidance see `codecraft/guides/engineer-workflow.md`.
