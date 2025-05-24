
# Guidelines for generating an implementation plan

**Objective:** To create a detailed, step-by-step implementation plan from a given Technical Specification document. This plan will be used by an AI agent to perform software modifications.

**Input:** `01-specification/technical-specification.md`
**Output:** `02-planned-development/implementation-plan.md`

---

## Core principles for plan generation:

1.  **Atomicity:** Each task should be as small and self-contained as possible, ideally corresponding to a single logical change or a small group of related changes that can be verified together.
2.  **Verifiability:** Every task must have clear, unambiguous verification steps. These steps should allow the agent (or a human) to confirm the task was completed successfully.
3.  **Sequentiality & Dependencies:** Tasks should be ordered logically. If Task B depends on Task A, Task A must come first. Clearly state dependencies if they span across major sections.
4.  **Idempotency (where possible):** If a task is run multiple times, it should ideally result in the same state without causing errors (though this is not always feasible).
5.  **Clear Instructions for Agent:** Provide precise instructions for what the agent needs to do, including exact file paths, commands to run, and expected outcomes.
6.  **Commit Instructions:** Each task (or a logical group of tasks) should culminate in a Git commit. Provide the *exact* commit message pattern, emphasizing conventions like Conventional Commits and character limits (e.g., 72 characters for the subject line).

## Structure of the implementation plan document:

The output `implementation-plan.md` should follow this Markdown structure:

```markdown
# Implementation plan for: [Name of Project/Feature from Tech Spec]

**Date Generated:** [YYYY-MM-DD]
**Tech Spec Version/Reference:** [Path to the input `01-specification/technical-specification.md`]

---

## Section X: [Descriptive title from Tech Spec Section, e.g., ESLint Configuration Cleanup]

### [ ] Task ID: SX.T1 (e.g., S1.T1 for Section 1, Task 1)
**Description:** [Detailed description of the task, derived from the tech spec. Be specific.]
**Affected Components/Files:**
  - `path/to/file1.ext` (Action: Modified/Deleted/Created)
  - `path/to/directory/` (Action: Files within modified/deleted)
**Inputs (if any):**
  - [e.g., Tech Spec item #Y, Output from Task ID SZ.TX]
**Outputs/Artifacts:**
  - [e.g., `file1.ext` updated, `new_file.ext` created, `old_file.ext` removed]
**Dependencies:** [Previous Task IDs if any, e.g., S(X-1).TY]
**Verification Steps / Success Criteria:**
  *   [ ] **Criterion 1:** [Specific check, e.g., "File `path/to/.eslintrc.cjs` no longer exists."]
  *   [ ] **Criterion 2:** [Specific check, e.g., "Command `npx eslint .` runs without errors related to config."]
  *   [ ] **Criterion N:** [...
**Agent Commit Instruction:** After successful verification of all criteria for this task, commit all changes. The commit message MUST follow the pattern: `type(scope): short description of changes` and MUST NOT exceed 72 characters.
**Notes/Hints for Agent (Optional):** [Any extra information or potential pitfalls for the agent.]

### [ ] Task ID: SX.T2
...

---

## Section Y: [Another section]
...

---

## Summary & completion checklist (optional)

*   [ ] All tasks completed.
*   [ ] All commits pushed to remote repository.
*   [ ] Final verification pass (if applicable).

```

## Detailed instructions for each field:

*   **`# Implementation plan for:`**: Extract the project or feature name from the Technical Specification.
*   **`**Date Generated:**`**: Use the current date.
*   **`**Tech Spec Version/Reference:**`**: Provide the full, canonical path to the `technical-specification.md` file used to generate this plan (e.g., `01-specification/technical-specification.md`). This is crucial for traceability.

*   **`## Section X:`**: Sections should mirror the major sections or distinct areas of work identified in the Technical Specification.

*   **`### [ ] Task ID: SX.T1`**: Use a clear, sequential ID. The `[ ]` is for the agent to mark completion (e.g., `[x]`).

*   **`**Description:**`**: Clearly state what needs to be done. Be imperative (e.g., "Delete the file...", "Update the dependency..."). Refer to specific items or line numbers in the tech spec if it adds clarity.

*   **`**Affected Components/Files:**`**: List all files or directories that will be touched by this task. Specify the action (Modified, Deleted, Created, Renamed). **Paths MUST be relative to the root of the target project.** For example: `src/components/my-component.tsx` or `package.json`.
    *   For deletions, ensure this is the intended outcome (e.g., file is truly unused).
    *   For modifications, briefly state the nature of the change if not obvious from the description.

*   **`**Inputs (if any):**`**: List specific items from the tech spec (e.g., "Tech Spec item #3b") or outputs from previous tasks in *this* plan that are direct inputs to the current task.

*   **`**Outputs/Artifacts:**`**: Describe the expected state after the task is done (e.g., "`package.json` updated with X dependency removed").

*   **`**Dependencies:**`**: List Task IDs that *must* be completed before this task can start. This helps in parallel execution if possible, or ensures correct order.

*   **`**Verification Steps / Success Criteria:**`**: This is critical. Each criterion must be a concrete, verifiable check. Paths mentioned here MUST also be relative to the project root.
    *   Examples:
        *   "The file `path/to/X` no longer exists."
        *   "The command `npm run build` completes successfully without errors."
        *   "The `dependencies` section in `package.json` no longer lists package `Y`."
        *   "Running `git status` shows no uncommitted changes in the `src/components/ui` directory."
        *   "The application loads at `http://localhost:3000` and feature Z is working as expected (describe how to check)."
    *   Use `[ ]` before each criterion for the agent to mark.

*   **`**Agent Commit Instruction:**`**: Provide the *exact* Git commit command or at least the full commit message. Specify the type (e.g., `fix`, `feat`, `refactor`, `chore`, `docs`), scope (e.g., `ui`, `deps`, `eslint`), and a concise, imperative description.
    *   Example: `git commit -m "fix(eslint): remove legacy .eslintrc.cjs and resolve config conflict"`
    *   Emphasize adherence to Conventional Commits (https://www.conventionalcommits.org/).
    *   **Crucially, specify a maximum character length for the commit message subject line (e.g., 72 chars).**

*   **`**Notes/Hints for Agent (Optional):**`**: Any additional context, common pitfalls, or suggestions for the agent. For example, "Ensure no other dependencies are accidentally removed," or "If `src/ai/` directory becomes empty, it can be removed."

## Iteration and refinement:

*   The first pass of generating the plan might not be perfect. Review it against the Tech Spec for completeness and clarity.
*   Imagine you are the agent. Could you execute each step without ambiguity? Are the verification steps foolproof?

## Example task generation (from a hypothetical Tech Spec item):

**Tech Spec Item:** "Remove the deprecated `getUserProfile` function from `src/api/user.ts` and all its usages. It is replaced by `fetchUserProfile` from `src/api/v2/user.ts`."

**Generated Plan Task:**

```markdown
### [ ] Task ID: S4.T1
**Description:** Replace usages of deprecated `getUserProfile` with `fetchUserProfile` and remove the old function.
**Affected Components/Files:**
  - `src/api/user.ts` (Modified, Deleted function)
  - `src/components/UserProfile.tsx` (Modified)
  - `src/pages/Dashboard.tsx` (Modified)
**Inputs (if any):**
  - Tech Spec item #7.3 (Remove `getUserProfile`)
**Outputs/Artifacts:**
  - `getUserProfile` function removed from `src/api/user.ts`.
  - All calls to `getUserProfile` replaced with `fetchUserProfile`.
**Dependencies:** None
**Verification Steps / Success Criteria:**
  *   [ ] **Criterion 1:** Grep search for `getUserProfile(` in `src/` yields no results.
  *   [ ] **Criterion 2:** The function `getUserProfile` no longer exists in `src/api/user.ts`.
  *   [ ] **Criterion 3:** The application builds successfully (`npm run build`).
  *   [ ] **Criterion 4:** User profiles load correctly in the UserProfile component and on the Dashboard page.
**Agent Commit Instruction:** After successful verification of all criteria for this task, commit all changes. The commit message MUST follow the pattern: `refactor(api): replace getUserProfile with fetchUserProfile and remove dead code` and MUST NOT exceed 72 characters.
**Notes/Hints for Agent (Optional):** Ensure to update import statements for `fetchUserProfile` from `src/api/v2/user.ts`.
```

---

By following these guidelines, the generated implementation plan will be robust, actionable, and significantly improve the reliability of automated software development tasks.
