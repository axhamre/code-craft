# Combined workflow template

**Use case:** Single LLM session for both specification and implementation plan generation.

## Setup instructions

1. **Load Planner context:**
   ```bash
   cat framework/planner/SYSTEM_PROMPT.md | pbcopy
   ```

2. **Provide guidelines:**
   ```bash
   cat framework/planner/guidelines.md
   cat framework/global-llm-rules.md
   ```

## Prompt template

```
I need you to generate both a technical specification and implementation plan for the following requirements:

[PASTE YOUR REQUIREMENTS HERE]

Please follow this two-step process:

**Step 1:** Generate the technical specification following the format in your guidelines.

**Step 2:** Based on that specification, generate the implementation plan following the format in your guidelines.

Make sure both documents follow the exact templates and include all required sections.
```

## Output handling

The LLM will generate two documents in sequence:
1. Save the first output as `01-specification/technical-specification.md`
2. Save the second output as `02-plan/implementation-plan.md`

## Next steps

Proceed to Phase 3 (Implementation) using the Coder as described in the engineer workflow guide. 