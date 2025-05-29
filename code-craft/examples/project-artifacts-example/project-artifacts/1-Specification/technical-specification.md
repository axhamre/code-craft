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