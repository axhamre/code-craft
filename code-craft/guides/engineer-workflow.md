# Engineer workflow

Detailed process description.

## Prerequisites
- Git  
- Large language model access (OpenAI, Anthropic, local)  
- Project toolchain (Node.js, Python, Docker, …)

## Bootstrap CodeCraft
```bash
git submodule add https://github.com/your-org/codecraft codecraft
bash codecraft/setup.sh
```

## Phase 1: Specify
Input → project requirements  
Output → `01-specification/technical-specification.md`  
Agent → planner

1. Open `codecraft/framework/planner/SYSTEM_PROMPT.md`.  
2. Send the prompt plus requirements to the LLM.  
3. Save the generated specification.

## Phase 2: Plan
Input → specification  
Output → `02-plan/implementation-plan.md`  
Agent → planner

1. Open `codecraft/framework/planner/PLAN_PROMPT.md`.  
2. Provide the specification to the LLM.  
3. Save the plan and commit.

## Phase 3: Execute
Input → implementation plan  
Output → code commits  
Agent → coder

1. Open `codecraft/framework/coder/SYSTEM_PROMPT.md`.  
2. Provide the plan to the LLM.  
3. Implement tasks sequentially.  
4. After each logical unit: run tests, commit, update `CHANGELOG.md`.

## Phase 4: Verify
Run the full test suite.  
If tests fail, patch code and iterate between execute and verify until all pass.

## Troubleshooting
| symptom          | resolution                                      |
| ---------------- | ----------------------------------------------- |
| LLM incomplete task | give more context, regenerate the step        |
| Failing tests    | review error, fix code, re‑run tests            |
