# CodeCraft

Structured LLM-assisted software delivery.

## Workflow
1. **Specify** – requirements → technical spec  
2. **Plan** – spec → implementation plan  
3. **Execute** – code with atomic commits  
4. **Verify** – tests confirm behaviour

## Quick start
Full walk-through in `QUICKSTART.md`.

```bash
bash setup.sh          # copy framework
bash scripts/specify.sh # generate spec
bash scripts/plan.sh    # generate plan
bash scripts/execute.sh # code & commit
bash scripts/verify.sh  # run tests
```

## Directories
| Path          | Role                         |
| ------------- | ---------------------------- |
| `framework/`  | System prompts & rules       |
| `templates/`  | Starter prompts              |
| `guides/`     | Detailed guides              |
| `examples/`   | Reference implementations    |

More depth → `guides/engineer-workflow.md`.
