# engineer workflow

End-to-end guide.

## prerequisites
- git  
- LLM access (OpenAI, Anthropic, local)  
- project toolchain (node, python, …)

## phase 1 specify
Input → requirements  
Output → `01-specification/technical-specification.md`  
Agent → planner

1. Copy `framework/planner/SYSTEM_PROMPT.md` to the LLM.  
2. Provide `framework/global-llm-rules.md` + requirements.  
3. Save spec.

## phase 2 plan
Input → spec  
Output → `02-plan/implementation-plan.md`  
Agent → planner

1. Copy `framework/planner/PLAN_PROMPT.md` to the LLM.  
2. Provide spec.  
3. Commit the plan.

## phase 3 execute
Input → plan  
Output → code commits  
Agent → coder

1. Copy `framework/coder/SYSTEM_PROMPT.md` to the LLM.  
2. Follow tasks.  
3. Commit after each logical unit; update `CHANGELOG.md`.

## phase 4 verify
Run tests.  
Fix failures; iterate until green.

## troubleshooting
| symptom          | action                         |
| ---------------- | ------------------------------ |
| failing task     | inspect error, patch, update plan |
| incomplete spec  | gather detail, regenerate spec & plan |
