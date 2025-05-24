# Implementation plan for: Tech spec for workspace cleanup

**Date Generated:** 2025-05-17
**Tech Spec Version/Reference:** ../01-specification/technical-specification.md

---

## Section 1: ESLint configuration cleanup

### [x] Task ID: S1.T1
**Description:** Resolve ESLint configuration conflict by deleting `.eslintrc.cjs` as per tech spec items #1 and #2. This ensures `eslint.config.mjs` is the sole ESLint configuration.
**Affected Components/Files:**
  - `.eslintrc.cjs` (Deleted)
  - `eslint.config.mjs` (Remains as primary)
**Inputs (if any):**
  - Tech spec items #1, #2 from `../01-specification/technical-specification.md`
**Outputs/Artifacts:**
  - `.eslintrc.cjs` file removed from the workspace.
**Dependencies:** None
**Verification Steps / Success Criteria:**
  *   [x] **Criterion 1:** The file `.eslintrc.cjs` no longer exists.
  *   [x] **Criterion 2:** The file `eslint.config.mjs` exists.
  *   [x] **Criterion 3:** Running ESLint (e.g., `npx eslint .`) completes without errors related to conflicting configurations or issues from the old `.eslintrc.cjs`.
**Agent Commit Instruction:** After successful verification of all criteria for this task, commit all changes. The commit message MUST follow the pattern: `fix(eslint): remove legacy .eslintrc.cjs and resolve config conflict` and MUST NOT exceed 72 characters.
**Notes/Hints for Agent (Optional):** Ensure no ESLint errors are introduced by this change.

---

## Section 2: Source code cleanup - AI modules

### [x] Task ID: S2.T1
**Description:** Delete unused AI-related source files `src/ai/dev.ts` and `src/ai/ai-instance.ts` as per tech spec item #3.
**Affected Components/Files:**
  - `src/ai/dev.ts` (Deleted)
  - `src/ai/ai-instance.ts` (Deleted)
**Inputs (if any):**
  - Tech spec item #3 from `../01-specification/technical-specification.md`
**Outputs/Artifacts:**
  - Specified files removed from the workspace.
  - The directory `src/ai/` may become empty or be removed if these were the only files.
**Dependencies:** None
**Verification Steps / Success Criteria:**
  *   [x] **Criterion 1:** The file `src/ai/dev.ts` no longer exists.
  *   [x] **Criterion 2:** The file `src/ai/ai-instance.ts` no longer exists.
  *   [x] **Criterion 3:** The application builds successfully (e.g., `npm run build` or `vite build`) without errors related to these files.
**Agent Commit Instruction:** After successful verification of all criteria for this task, commit all changes. The commit message MUST follow the pattern: `refactor(ai): remove unused AI module files dev.ts and ai-instance.ts` and MUST NOT exceed 72 characters.
**Notes/Hints for Agent (Optional):** If the `src/ai` directory becomes empty, it can be removed.

---

## Section 3: Dependency management - `package.json` cleanup

### [ ] Task ID: S3.T1
**Description:** Remove unused AI-related dependencies (`@genkit-ai/googleai`, `genkit`, `openai`) from `package.json` as per tech spec item #4.
**Affected Components/Files:**
  - `package.json` (Modified)
**Inputs (if any):**
  - Tech spec item #4 from `../01-specification/technical-specification.md`
  - Output from Task ID S2.T1
**Outputs/Artifacts:**
  - `package.json` updated with specified dependencies removed from the `dependencies` section.
**Dependencies:** S2.T1
**Verification Steps / Success Criteria:**
  *   [ ] **Criterion 1:** The `dependencies` section in `package.json` no longer lists `@genkit-ai/googleai`.
  *   [ ] **Criterion 2:** The `dependencies` section in `package.json` no longer lists `genkit`.
  *   [ ] **Criterion 3:** The `dependencies` section in `package.json` no longer lists `openai`.
  *   [ ] **Criterion 4:** `package.json` is valid JSON.
**Agent Commit Instruction:** After successful verification of all criteria for this task, commit all changes. The commit message MUST follow the pattern: `refactor(deps): remove unused AI-related dependencies` and MUST NOT exceed 72 characters.
**Notes/Hints for Agent (Optional):** Be careful when editing `package.json` to maintain valid JSON structure.

---

### [ ] Task ID: S3.T2
**Description:** Remove other unused dependencies (`@hookform/resolvers`, `@tanstack/react-query`, `date-fns`, `patch-package`, `zod`) from `package.json` as per tech spec item #5.
**Affected Components/Files:**
  - `package.json` (Modified)
**Inputs (if any):**
  - Tech spec item #5 from `../01-specification/technical-specification.md`
**Outputs/Artifacts:**
  - `package.json` updated with specified dependencies removed from the `dependencies` section.
**Dependencies:** S3.T1
**Verification Steps / Success Criteria:**
  *   [ ] **Criterion 1:** The `dependencies` section in `package.json` no longer lists `@hookform/resolvers`.
  *   [ ] **Criterion 2:** The `dependencies` section in `package.json` no longer lists `@tanstack/react-query`.
  *   [ ] **Criterion 3:** The `dependencies` section in `package.json` no longer lists `date-fns`.
  *   [ ] **Criterion 4:** The `dependencies` section in `package.json` no longer lists `patch-package`.
  *   [ ] **Criterion 5:** The `dependencies` section in `package.json` no longer lists `zod`.
  *   [ ] **Criterion 6:** `package.json` is valid JSON.
**Agent Commit Instruction:** After successful verification of all criteria for this task, commit all changes. The commit message MUST follow the pattern: `refactor(deps): remove unused general dependencies` and MUST NOT exceed 72 characters.
**Notes/Hints for Agent (Optional):** Ensure no other dependencies are accidentally removed or modified.

---

### [ ] Task ID: S3.T3
**Description:** Remove unused npm scripts (`genkit:dev`, `genkit:watch`) from `package.json` as per tech spec item #6.
**Affected Components/Files:**
  - `package.json` (Modified)
**Inputs (if any):**
  - Tech spec item #6 from `../01-specification/technical-specification.md`
  - Output from Task ID S2.T1
**Outputs/Artifacts:**
  - `package.json` updated with specified scripts removed from the `scripts` section.
**Dependencies:** S2.T1, S3.T2
**Verification Steps / Success Criteria:**
  *   [ ] **Criterion 1:** The `scripts` section in `package.json` no longer contains the `genkit:dev` script.
  *   [ ] **Criterion 2:** The `scripts` section in `package.json` no longer contains the `genkit:watch` script.
  *   [ ] **Criterion 3:** `package.json` is valid JSON.
**Agent Commit Instruction:** After successful verification of all criteria for this task, commit all changes. The commit message MUST follow the pattern: `refactor(scripts): remove unused genkit npm scripts` and MUST NOT exceed 72 characters.
**Notes/Hints for Agent (Optional):** Verify that other scripts remain functional if they are related.

---

### [ ] Task ID: S3.T4
**Description:** Run `npm prune` (or equivalent package manager command) to remove unlisted packages from `node_modules` and update lock file accordingly, as implied by tech spec items #4 and #5.
**Affected Components/Files:**
  - `node_modules/` (Modified)
  - `package-lock.json` (or `pnpm-lock.yaml`, `yarn.lock`) (Modified)
**Inputs (if any):**
  - Outputs from Task IDs S3.T1, S3.T2
**Outputs/Artifacts:**
  - `node_modules` directory cleaned of unlisted packages.
  - Lock file updated to reflect the pruned state.
**Dependencies:** S3.T1, S3.T2, S3.T3
**Verification Steps / Success Criteria:**
  *   [ ] **Criterion 1:** The command `npm prune` (or equivalent for pnpm/yarn if used, e.g., `pnpm install --prune-lockfile` or `yarn install --force`) executes successfully without errors in the project root directory.
  *   [ ] **Criterion 2:** The `package-lock.json` (or equivalent lock file) reflects the changes (e.g., by checking its modification timestamp or by comparing its content before and after).
  *   [ ] **Criterion 3:** Previously removed dependencies (e.g., `genkit`, `zod`) are no longer present in `node_modules`. This can be verified by checking for the non-existence of directories like `node_modules/genkit` and `node_modules/zod`.
  *   [ ] **Criterion 4:** The application installs dependencies correctly using `npm install` (or equivalent) after this change.
**Agent Commit Instruction:** After successful verification of all criteria for this task, commit all changes. The commit message MUST follow the pattern: `chore(deps): prune extraneous packages from node_modules` and MUST NOT exceed 72 characters.
**Notes/Hints for Agent (Optional):** The prune command should be run in the root of the project.

---

## Section 4: Source code cleanup - UI components and hooks

### [ ] Task ID: S4.T1
**Description:** Delete 30 unused UI component files from `src/components/ui/` and update `components.json` and any barrel exports, as per tech spec item #7.
**Affected Components/Files:**
  - `src/components/ui/accordion.tsx` (Deleted)
  - `src/components/ui/alert-dialog.tsx` (Deleted)
  - `src/components/ui/alert.tsx` (Deleted)
  - `src/components/ui/avatar.tsx` (Deleted)
  - `src/components/ui/badge-variants.ts` (Deleted)
  - `src/components/ui/badge.tsx` (Deleted)
  - `src/components/ui/button-variants.ts` (Deleted)
  - `src/components/ui/calendar.tsx` (Deleted)
  - `src/components/ui/chart.tsx` (Deleted)
  - `src/components/ui/checkbox.tsx` (Deleted)
  - `src/components/ui/dialog.tsx` (Deleted)
  - `src/components/ui/dropdown-menu.tsx` (Deleted)
  - `src/components/ui/form-hooks.ts` (Deleted)
  - `src/components/ui/form.tsx` (Deleted)
  - `src/components/ui/menubar.tsx` (Deleted)
  - `src/components/ui/popover.tsx` (Deleted)
  - `src/components/ui/progress.tsx` (Deleted)
  - `src/components/ui/radio-group.tsx` (Deleted)
  - `src/components/ui/scroll-area.tsx` (Deleted)
  - `src/components/ui/select.tsx` (Deleted)
  - `src/components/ui/sheet.tsx` (Deleted)
  - `src/components/ui/sidebar.tsx` (Deleted)
  - `src/components/ui/skeleton.tsx` (Deleted)
  - `src/components/ui/slider.tsx` (Deleted)
  - `src/components/ui/switch.tsx` (Deleted)
  - `src/components/ui/table.tsx` (Deleted)
  - `src/components/ui/tabs.tsx` (Deleted)
  - `src/components/ui/textarea.tsx` (Deleted)
  - `src/components/ui/toast.tsx` (Deleted)
  - `src/components/ui/toaster.tsx` (Deleted)
  - `src/components/ui/tooltip.tsx` (Deleted)
  - `components.json` (Modified)
  - Potentially `src/components/ui/index.ts` or `src/components/index.ts` (Modified/Deleted)
**Inputs (if any):**
  - Tech spec item #7 from `../01-specification/technical-specification.md`
**Outputs/Artifacts:**
  - Specified UI component files removed from `src/components/ui/`.
  - `components.json` updated.
  - Any barrel files re-exporting these components are updated or removed.
**Dependencies:** None
**Verification Steps / Success Criteria:**
  *   [ ] **Criterion 1:** All 30 listed UI component files under `src/components/ui/` no longer exist.
  *   [ ] **Criterion 2:** The `components.json` file is updated to remove references to the deleted components and is valid JSON.
  *   [ ] **Criterion 3:** Check for and remove/update any barrel export files (e.g., `src/components/ui/index.ts` or `src/components/index.ts`) that might reference these deleted components.
  *   [ ] **Criterion 4:** The application builds successfully (e.g., `npm run build` or `vite build`) without errors related to missing component imports.
**Agent Commit Instruction:** After successful verification of all criteria for this task, commit all changes. The commit message MUST follow the pattern: `refactor(ui): remove 30 unused UI components and update registry` and MUST NOT exceed 72 characters.
**Notes/Hints for Agent (Optional):** Ensure `components.json` is updated to reflect the removed components. Also, check any `index.ts` files in `src/components/` or `src/components/ui/` for references to the deleted components and remove them. If the `src/components/ui` directory becomes empty, it can be removed.

---

### [ ] Task ID: S4.T2
**Description:** Delete unused `src/components/icons.ts` as per tech spec item #8.
**Affected Components/Files:**
  - `src/components/icons.ts` (Deleted)
**Inputs (if any):**
  - Tech spec item #8 from `../01-specification/technical-specification.md`
**Outputs/Artifacts:**
  - `src/components/icons.ts` file removed.
**Dependencies:** None
**Verification Steps / Success Criteria:**
  *   [ ] **Criterion 1:** The file `src/components/icons.ts` no longer exists.
  *   [ ] **Criterion 2:** The application builds successfully (e.g., `npm run build` or `vite build`) without errors related to `icons.ts`.
**Agent Commit Instruction:** After successful verification of all criteria for this task, commit all changes. The commit message MUST follow the pattern: `refactor(ui): remove unused icons.ts` and MUST NOT exceed 72 characters.
**Notes/Hints for Agent (Optional):** None.

---

### [ ] Task ID: S4.T3
**Description:** Delete unused hook files `src/hooks/use-mobile.tsx` and `src/hooks/use-toast.ts` as per tech spec item #9.
**Affected Components/Files:**
  - `src/hooks/use-mobile.tsx` (Deleted)
  - `src/hooks/use-toast.ts` (Deleted)
**Inputs (if any):**
  - Tech spec item #9 from `../01-specification/technical-specification.md`
**Outputs/Artifacts:**
  - Specified hook files removed from `src/hooks/`.
**Dependencies:** S4.T1
**Verification Steps / Success Criteria:**
  *   [ ] **Criterion 1:** The file `src/hooks/use-mobile.tsx` no longer exists.
  *   [ ] **Criterion 2:** The file `src/hooks/use-toast.ts` no longer exists.
  *   [ ] **Criterion 3:** The application builds successfully (e.g., `npm run build` or `vite build`) without errors related to these hooks.
  *   [ ] **Criterion 4:** Check for and remove/update any barrel export files (e.g., `src/hooks/index.ts`) that might reference these deleted hooks.
**Agent Commit Instruction:** After successful verification of all criteria for this task, commit all changes. The commit message MUST follow the pattern: `refactor(hooks): remove unused use-mobile and use-toast hooks` and MUST NOT exceed 72 characters.
**Notes/Hints for Agent (Optional):** If the `src/hooks` directory becomes empty or only contains files that are also planned for deletion, consider if the directory itself can be removed after all relevant tasks are done.

---

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