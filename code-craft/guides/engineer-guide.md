# Engineer guide: CodeCraft

This guide details the operational workflow for using CodeCraft.
The framework uses **Architect** to create project artifacts and **Builder** to implement plans.
Refer to the main `README.md` for role definitions.

## Workflow: requirements to verified code

**Phase 1: specify** (Define *what* to build)

1.  **Engineer:** Detail project requirements.
    *   *Creates:* `[your-project]/01-specification/input-requirements.md`
2.  **Engineer:** Craft prompt for **Architect** to produce a technical specification.
    *   *Uses template:* `framework/templates/specification/tech-spec-generation-prompt.md`
    *   *Adheres to:* `framework/runtime-llms/architect/tech-spec-generation-guidelines.md`
3.  **Architect:** Generates technical specification.
    *   *Produces:* `[your-project]/01-specification/technical-specification.md`
4.  **Engineer:** Review & finalize `technical-specification.md`. Iterate steps 2-3 if needed.

**Phase 2: plan** (Define *how* to build it)

5.  **Engineer:** Craft prompt for **Architect** to produce an implementation plan from the `technical-specification.md`.
    *   *Uses template:* `framework/templates/planning/implementation-plan-generation-prompt.md`
    *   *Adheres to:* `framework/runtime-llms/architect/implementation-plan-generation-guidelines.md`
6.  **Architect:** Generates implementation plan.
    *   *Produces:* `[your-project]/02-planned-development/implementation-plan.md`
7.  **Engineer:** Review & finalize `implementation-plan.md`. Iterate steps 5-6 if needed.

**Phase 3: execute** (Build it)

8.  **System:** Prepare for **Builder**.
    *   *Copies:* `[your-project]/02-planned-development/implementation-plan.md`
    *   *To:* `[your-project]/02-planned-development/.tmp/implementation-plan.md` (working copy)
9.  **Builder:** Executes tasks from the working copy.
    *   *Follows:* `framework/runtime-llms/builder/builder-protocol.md`
    *   *Result:* Commits code changes to your project repository.

**Phase 4: verify** (Confirm it's built right)

10. **Engineer (optional):** Craft prompt for **Architect** for a verification checklist.
    *   *Uses template:* `framework/templates/verification/verification-checklist-generation-prompt.md`
11. **Architect (optional):** Generates verification checklist.
    *   *Produces:* `[your-project]/03-verification/verification-checklist.md`
12. **Engineer:** Verify implementation against `technical-specification.md`.
    *   *May use:* Generated `verification-checklist.md`, or `[your-project]/03-verification/test-cases.md`.
13. **Engineer:** Document verification outcomes.
    *   *Creates:* `[your-project]/03-verification/verification-report.md`

---

## Key framework locations

*   **This guide:** `framework/guides/engineer-guide.md`
*   **Role-specific guides & protocols:**
    *   **Architect:** `framework/runtime-llms/architect/` (main guide & output guidelines)
    *   **Builder:** `framework/runtime-llms/builder/` (main guide & protocol)
*   **Prompt templates:** `framework/templates/` (organized by phase: `specification/`, `planning/`, `verification/`)
*   **Example project artifacts:** `framework/examples/project-artifacts-example/` (shows structure for `01-specification/`, `02-planned-development/`, `03-verification/`)

---

## Directory structure of CodeCraft

This outlines the key components of the CodeCraft framework itself.

```
.
├── README.md
├── CHANGELOG.md
├── framework/
│   ├── global-llm-rules.md
│   ├── QUICKSTART.md
│   │
│   ├── guides/
│   │   └── engineer-guide.md
│   │
│   ├── runtime-llms/
│   │   ├── architect/
│   │   │   ├── SYSTEM_PROMPT.md
│   │   │   ├── architect-guide.md
│   │   │   ├── tech-spec-generation-guidelines.md
│   │   │   └── implementation-plan-generation-guidelines.md
│   │   │
│   │   ├── builder/
│   │   │   ├── SYSTEM_PROMPT.md
│   │   │   ├── builder-guide.md
│   │   │   └── builder-protocol.md
│   │   │
│   │   └── shared/
│   │       └── schemas/
│   │
│   ├── templates/
│   │   ├── specification/
│   │   │   └── tech-spec-generation-prompt.md
│   │   ├── planning/
│   │   │   └── implementation-plan-generation-prompt.md
│   │   └── verification/
│   │       └── verification-checklist-generation-prompt.md
│   │
│   └── examples/
│       └── project-artifacts-example/
│           ├── 01-specification/
│           │   ├── input-requirements.md
│           │   └── technical-specification.md
│           ├── 02-planned-development/
│           │   ├── implementation-plan.md
│           │   └── .tmp/
│           │       └── implementation-plan.md
│           ├── 03-verification/
│           │   ├── verification-checklist.md
│           │   ├── test-cases.md
│           │   └── verification-report.md
│           └── 04-builder-output/
```

**Understanding the structure:**

*   **`README.md` (root):** Your first stop. Explains CodeCraft's purpose, defines the roles (**Architect**, **Builder**), and points you to this `engineer-guide.md`.
*   **`framework/global-llm-rules.md`:** Universal content rules for all LLM-generated text.
*   **`framework/guides/`**: The knowledge hub.
    *   This `engineer-guide.md` is your primary operational manual.
    *   `runtime-llms/architect/` contains the main guide for **Architect** and the crucial `*-generation-guidelines.md` files that define the *required structure* for documents like technical specifications and implementation plans.
    *   `runtime-llms/builder/` provides the guide and the strict `builder-protocol.md` that **Builder** follows to implement changes.
*   **`framework/templates/`**: A library of starting prompts. You'll copy and customize these for your specific project tasks before **Architect** uses them. They are organized by the development phase they support.
*   **`framework/examples/project-artifacts-example/`**: A practical, clean example showing how the inputs and outputs (specifications, plans, verification reports) are organized for a typical project being developed with this framework. Use this as a model for your own project's structure.

