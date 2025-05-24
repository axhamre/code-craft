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
```

---

**4. Content for `project-artifacts-example/01-specification/technical-specification.md`**

This is the example technical specification for the "Workspace Cleanup" task.

```markdown
# Tech spec for workspace cleanup

**Project Goal:** Streamline the `mortgage-costs` Next.js project by removing unused files, dependencies, and configurations based on a recent audit.

**Date:** 2025-05-17

---

## 1. ESLint configuration consolidation

*   **Current State:** Two ESLint configuration files exist: `.eslintrc.cjs` and `eslint.config.mjs`.
*   **Problem:** Potential for conflicting configurations and maintenance overhead. `eslint.config.mjs` is the more modern flat config.
*   **Proposed Change:**
    1.  Delete `.eslintrc.cjs`.
    2.  Ensure `eslint.config.mjs` is fully functional and correctly configured as the sole ESLint setup.
*   **Affected Files:**
    *   `.eslintrc.cjs` (to be deleted)
    *   `eslint.config.mjs` (to be verified)
*   **Verification:**
    *   Run ESLint (e.g., `npx eslint .`) and ensure no errors related to configuration.
    *   Confirm linting rules are applied as expected.

## 2. Unused source code removal - AI modules

*   **Current State:** The `src/ai/` directory contains `dev.ts` and `ai-instance.ts`.
*   **Problem:** These files were part of an experimental AI integration (Genkit) that is no longer in use.
*   **Proposed Change:** Delete `src/ai/dev.ts` and `src/ai/ai-instance.ts`.
*   **Affected Files:**
    *   `src/ai/dev.ts` (to be deleted)
    *   `src/ai/ai-instance.ts` (to be deleted)
*   **Verification:**
    *   Application builds successfully after removal.
    *   No runtime errors related to missing AI modules.

## 3. Dependency pruning - `package.json`

*   **Current State:** `package.json` lists several dependencies that are no longer required due to feature removal or changes in approach.
*   **Problem:** Bloated `node_modules`, increased build times, potential security vulnerabilities from unmaintained packages.
*   **Proposed Changes:**
    1.  Remove AI-related dependencies: `@genkit-ai/googleai`, `genkit`, `openai`.
    2.  Remove other identified unused dependencies: `@hookform/resolvers`, `@tanstack/react-query`, `date-fns`, `patch-package`, `zod`.
    3.  Remove unused npm scripts related to Genkit: `genkit:dev`, `genkit:watch`.
    4.  Run `npm prune` (or equivalent `pnpm prune` / `yarn autoclean`) to remove unlisted packages from `node_modules` and update `package-lock.json`.
*   **Affected Files:**
    *   `package.json`
    *   `package-lock.json`
    *   `node_modules/`
*   **Verification:**
    *   Application builds and runs correctly after dependency removal.
    *   `npm install` (or equivalent) works without issues.
    *   Confirm removed packages are no longer in `node_modules`.

## 4. Unused UI components and hooks removal

*   **Current State:** A significant number of UI components in `src/components/ui/` (approx. 30 files, including `accordion.tsx`, `alert-dialog.tsx`, etc.), `src/components/icons.ts`, and hooks (`src/hooks/use-mobile.tsx`, `src/hooks/use-toast.ts`) are not actively used. `components.json` also lists these components.
*   **Problem:** Codebase clutter, increased maintenance, potential for confusion.
*   **Proposed Changes:**
    1.  Delete the 30 specified unused component files from `src/components/ui/`.
    2.  Update `components.json` to remove entries for the deleted components.
    3.  Update any barrel export files (e.g., `src/components/ui/index.ts`, `src/components/index.ts`) to remove references.
    4.  Delete `src/components/icons.ts`.
    5.  Delete `src/hooks/use-mobile.tsx` and `src/hooks/use-toast.ts`.
    6.  Update any barrel export files in `src/hooks/` if they exist and reference these hooks.
*   **Affected Files:**
    *   Multiple files under `src/components/ui/` (to be deleted)
    *   `components.json` (to be modified)
    *   Potentially `src/components/ui/index.ts` and/or `src/components/index.ts` (to be modified/deleted)
    *   `src/components/icons.ts` (to be deleted)
    *   `src/hooks/use-mobile.tsx` (to be deleted)
    *   `src/hooks/use-toast.ts` (to be deleted)
    *   Potentially `src/hooks/index.ts` (to be modified/deleted)
*   **Verification:**
    *   Application builds and runs correctly.
    *   No broken UI elements or import errors.

## 5. Unused utility code removal

*   **Current State:** `src/utils/localStorage.ts` and its test `src/utils/localStorage.test.ts` are unused.
*   **Problem:** Dead code.
*   **Proposed Change:** Delete `src/utils/localStorage.ts` and `src/utils/localStorage.test.ts`.
*   **Affected Files:**
    *   `src/utils/localStorage.ts` (to be deleted)
    *   `src/utils/localStorage.test.ts` (to be deleted)
*   **Verification:**
    *   Application builds and tests pass successfully.

---

**Next Steps:**
*   Generate a detailed implementation plan based on this technical specification.
*   Execute the implementation plan.
*   Verify all changes thoroughly.
```

---

**5. Content for `engineer-workflow/templates/planning/implementation-plan-generation-prompt.md`**

This is the prompt template for generating an implementation plan.

```markdown
# Prompt: Generate Implementation Plan

## Objective:
Produce a detailed, step-by-step implementation plan based on the provided technical specification.

## Instructions for `GeneratorLLM`:

1.  **Analyze Input:** Thoroughly review the `technical-specification.md` provided below.
2.  **Structure Output:** Strictly adhere to the content and formatting rules defined in `../../runtime-llms/generator-llm/implementation-plan-generation-guidelines.md`. This includes breaking tasks into atomic, verifiable units with clear commit instructions.
3.  **Global Standards:** All generated text MUST strictly comply with `../../global-llm-rules.md`.
4.  **Content Focus:** For each section of the technical specification, create corresponding tasks detailing affected components, inputs, outputs, dependencies, verification steps, and agent commit instructions.
5.  **Clarity & Actionability:** Ensure the plan is unambiguous and directly actionable by an `ExecutorLLM` or a human engineer.

---
## Technical Specification:

```
{{TECHNICAL_SPECIFICATION_CONTENT_HERE}}
```
---

## Generated Implementation Plan:
```markdown
# Implementation plan for: [Derived from Technical Specification]

**Date Generated:** {{CURRENT_DATE}}
**Tech Spec Version/Reference:** [Path to the input technical-specification.md]

---

*(GeneratorLLM: Populate the implementation plan here, following the guidelines.)*
```
