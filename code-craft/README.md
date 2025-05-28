# CodeCraft

Structured LLM‑assisted software delivery.

## workflow
1. **specify** – requirements → technical spec  
2. **plan** – spec → implementation plan  
3. **execute** – code with atomic commits  
4. **verify** – tests confirm behaviour

## quick start
Full walk‑through in `QUICKSTART.md`.

```bash
bash setup.sh          # copy framework
bash scripts/specify.sh # generate spec
bash scripts/plan.sh    # generate plan
bash scripts/execute.sh # code & commit
bash scripts/verify.sh  # run tests
```

## directories
| path          | role                         |
| ------------- | ---------------------------- |
| `framework/`  | system prompts & rules       |
| `templates/`  | starter prompts              |
| `guides/`     | detailed guides              |
| `examples/`   | reference implementations    |

More depth → `guides/engineer-workflow.md`.
