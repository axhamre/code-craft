# quickstart

Bootstrap inside an existing Git repo.

```bash
# install
bash codecraft/setup.sh
```

### 1 specify
Copy `framework/planner/SYSTEM_PROMPT.md` to an LLM with requirements.  
Save output as `01-specification/technical-specification.md`.

### 2 plan
Copy `framework/planner/PLAN_PROMPT.md` to the LLM with the spec.  
Save as `02-plan/implementation-plan.md`.

### 3 execute
Copy `framework/coder/SYSTEM_PROMPT.md` to the LLM with the plan.  
Follow tasks, committing each logical unit and updating `CHANGELOG.md`.

### 4 verify
Run project tests (`npm test`, `pytest`, …).  
Fix failures; repeat execute/verify until green.

Need detail? See `guides/engineer-workflow.md`.
