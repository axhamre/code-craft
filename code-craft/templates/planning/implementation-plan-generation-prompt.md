## Section 5: Source code cleanup - utilities

### [ ] Task ID: S5.T1
**Description:** Delete unused utility file `src/utils/localStorage.ts` and its associated test file `src/utils/localStorage.test.ts` as per tech spec item #10.
**Affected Components/Files:**
  - `src/utils/localStorage.ts` (Deleted)
  - `src/utils/localStorage.test.ts` (Deleted)
**Inputs (if any):**
  - Tech spec item #10 from `../01-specification/technical-specification.md`
**Outputs/Artifacts:**
  - Specified utility and test files removed from `src/utils/`.
**Dependencies:** None
**Verification Steps / Success Criteria:**
  *   [ ] **Criterion 1:** The file `src/utils/localStorage.ts` no longer exists.
  *   [ ] **Criterion 2:** The file `src/utils/localStorage.test.ts` no longer exists.
  *   [ ] **Criterion 3:** The application builds successfully (e.g., `npm run build` or `vite build`) without errors.
  *   [ ] **Criterion 4:** Test suite runs successfully (e.g., `npm test` or `vite test`) without errors related to missing files (especially if tests were previously attempting to run these specific tests).
**Agent Commit Instruction:** After successful verification of all criteria for this task, commit all changes. The commit message MUST follow the pattern: `refactor(utils): remove unused localStorage utility and tests` and MUST NOT exceed 72 characters.
**Notes/Hints for Agent (Optional):** If the `src/utils` directory becomes empty or only contains files that are also planned for deletion, consider if the directory itself can be removed after all relevant tasks are done.

---

# Prompt: generate implementation plan

## Objective:
Produce a detailed, step-by-step implementation plan based on the provided technical specification.

## Instructions for Architect:

1.  **Analyze input:** Thoroughly review the `technical-specification.md` provided below.
2.  **Structure output:** Strictly adhere to the content and formatting rules defined in `../../runtime-llms/architect/implementation-plan-generation-guidelines.md`. This includes breaking tasks into atomic, verifiable units with clear commit instructions.
3.  **Global standards:** All generated text MUST strictly comply with `../../global-llm-rules.md`.
4.  **Content focus:** For each section of the technical specification, create corresponding tasks detailing affected components, inputs, outputs, dependencies, verification steps, and commit instructions.
5.  **Clarity & actionability:** Ensure the plan is unambiguous and directly actionable by **Builder**.

---
## Technical specification:

```
{{TECHNICAL_SPECIFICATION_CONTENT_HERE}}
```
---

## Generated implementation plan:
```markdown
# Implementation plan for: [Derived from technical specification]

**Date generated:** {{CURRENT_DATE}}
**Tech spec version/reference:** [Path to the input technical-specification.md]

---

*(Architect: Populate the implementation plan here, following the guidelines.)*
```
