# Engineer workflow

End-to-end guide.

## Prerequisites
- git  
- LLM access (OpenAI, Anthropic, local)  
- Project toolchain (node, python, ...)

## Phase 1 specify
Input → requirements  
Output → `01-specification/technical-specification.md`  
Agent → planner

1. Copy `framework/planner/SYSTEM_PROMPT.md` to the LLM.  
2. Provide `framework/global-llm-rules.md` + requirements.  
3. Save spec.

## Phase 2 plan
Input → spec  
Output → `02-plan/implementation-plan.md`  
Agent → planner

1. Copy `framework/planner/PLAN_PROMPT.md` to the LLM.  
2. Provide spec.  
3. Commit the plan.

## Phase 3 execute
Input → plan  
Output → code commits  
Agent → coder

1. Copy `framework/coder/SYSTEM_PROMPT.md` to the LLM.  
2. Follow tasks.  
3. Commit after each logical unit; update `CHANGELOG.md`.

## Phase 4 verify
Run tests.  
Fix failures; iterate until green.

## Troubleshooting
| Symptom          | Action                         |
| ---------------- | ------------------------------ |
| Failing task     | Inspect error, patch, update plan |
| Incomplete spec  | Gather detail, regenerate spec & plan |
