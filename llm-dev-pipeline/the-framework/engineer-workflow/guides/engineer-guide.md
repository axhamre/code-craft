# Engineer Guide: `llm-dev-pipeline`

This guide details the operational workflow for using `llm-dev-pipeline`.
The framework uses `GeneratorLLM` to create project artifacts and `ExecutorLLM` to implement plans.
Refer to the main `README.md` for LLM role definitions.

## Workflow: Requirements to Verified Code

**Phase 1: Specify** (Define *what* to build)

1.  **Engineer:** Detail project requirements.
    *   *Creates:* `[your-project]/01-specification/input-requirements.md`
2.  **Engineer:** Craft prompt for `GeneratorLLM` to produce a technical specification.
    *   *Uses Template:* `engineer-workflow/templates/specification/tech-spec-generation-prompt.md`
    *   *Adheres to:* `runtime-llms/generator-llm/tech-spec-generation-guidelines.md`
3.  **`GeneratorLLM`:** Generates technical specification.
    *   *Produces:* `[your-project]/01-specification/technical-specification.md`
4.  **Engineer:** Review & finalize `technical-specification.md`. Iterate steps 2-3 if needed.

**Phase 2: Plan** (Define *how* to build it)

5.  **Engineer:** Craft prompt for `GeneratorLLM` to produce an implementation plan from the `technical-specification.md`.
    *   *Uses Template:* `engineer-workflow/templates/planning/implementation-plan-generation-prompt.md`
    *   *Adheres to:* `runtime-llms/generator-llm/implementation-plan-generation-guidelines.md`
6.  **`GeneratorLLM`:** Generates implementation plan.
    *   *Produces:* `[your-project]/02-planned-development/implementation-plan.md`
7.  **Engineer:** Review & finalize `implementation-plan.md`. Iterate steps 5-6 if needed.

**Phase 3: Execute** (Build it)

8.  **System:** Prepare for `ExecutorLLM`.
    *   *Copies:* `[your-project]/02-planned-development/implementation-plan.md`
    *   *To:* `[your-project]/02-planned-development/.tmp/implementation-plan.md` (working copy)
9.  **`ExecutorLLM`:** Executes tasks from the working copy.
    *   *Follows:* `runtime-llms/executor-llm/executor-llm-protocol.md`
    *   *Result:* Commits code changes to your project repository.

**Phase 4: Verify** (Confirm it's built right)

10. **Engineer (Optional):** Craft prompt for `GeneratorLLM` for a verification checklist.
    *   *Uses Template:* `engineer-workflow/templates/verification/verification-checklist-generation-prompt.md`
11. **`GeneratorLLM` (Optional):** Generates verification checklist.
    *   *Produces:* `[your-project]/03-verification/verification-checklist.md`
12. **Engineer:** Verify implementation against `technical-specification.md`.
    *   *May use:* Generated `verification-checklist.md`, or `[your-project]/03-verification/test-cases.md`.
13. **Engineer:** Document verification outcomes.
    *   *Creates:* `[your-project]/03-verification/verification-report.md`

---

## Key Framework Locations

*   **This Guide:** `engineer-workflow/engineer-guide.md`
*   **LLM-Specific Guides & Protocols:**
    *   `GeneratorLLM`: `runtime-llms/generator-llm/` (main guide & output guidelines)
    *   `ExecutorLLM`: `runtime-llms/executor-llm/` (main guide & protocol)
    *   `FrameworkLLM` (for framework development): `framework-llm/framework-llm-collaboration-guide.md`
*   **Prompt Templates:** `engineer-workflow/templates/` (organized by phase: `specification/`, `planning/`, `verification/`)
*   **Example Project Artifacts:** `project-artifacts-example/` (shows structure for `01-specification/`, `02-planned-development/`, `03-verification/`)

---

## Directory Structure of `llm-dev-pipeline`

This outlines the key components of the `llm-dev-pipeline` framework itself.

```
.
├── README.md
├── global-llm-rules.md
│
├── engineer-workflow/
│   ├── engineer-guide.md
│   │
│   ├── framework-dev/
│   │   └── framework-llm-collaboration-guide.md
│   │
│   ├── generator-llm/
│   │   ├── generator-llm-guide.md
│   │   ├── tech-spec-generation-guidelines.md
│   │   └── implementation-plan-generation-guidelines.md
│   │
│   └── executor-llm/
│       ├── executor-llm-guide.md
│       └── executor-llm-protocol.md
│
├── engineer-workflow/templates/
│   ├── specification/
│   │   └── tech-spec-generation-prompt.md
│   ├── planning/
│   │   └── implementation-plan-generation-prompt.md
│   └── verification/
│       └── verification-checklist-generation-prompt.md
│
└── project-artifacts-example/
    ├── 01-specification/
    │   ├── input-requirements.md
    │   └── technical-specification.md
    ├── 02-planned-development/
    │   ├── implementation-plan.md
    │   └── .tmp/
    │       └── implementation-plan.md
    └── 03-verification/
        ├── verification-checklist.md
        ├── test-cases.md
        └── verification-report.md
```

**Understanding the Structure:**

*   **`README.md` (Root):** Your first stop. Explains `llm-dev-pipeline`'s purpose, defines the LLM roles (`FrameworkLLM`, `GeneratorLLM`, `ExecutorLLM`), and points you to this `engineer-guide.md`.
*   **`global-llm-rules.md` (Root):** Universal content rules for all LLM-generated text.
*   **`engineer-workflow/`**: The knowledge hub.
    *   This `engineer-guide.md` is your primary operational manual.
    *   `framework-dev/` details how `llm-dev-pipeline` itself is designed and developed, including how `FrameworkLLM` (the LLM assisting in framework creation) collaborates.
    *   `generator-llm/` contains the main guide for `GeneratorLLM` and the crucial `*-generation-guidelines.md` files that define the *required structure* for documents like technical specifications and implementation plans.
    *   `executor-llm/` provides the guide and the strict `executor-llm-protocol.md` that `ExecutorLLM` follows to implement changes.
*   **`engineer-workflow/templates/`**: A library of starting prompts. You'll copy and customize these for your specific project tasks before `GeneratorLLM` uses them. They are organized by the development phase they support.
*   **`project-artifacts-example/`**: A practical, clean example showing how the inputs and outputs (specifications, plans, verification reports) are organized for a typical project being developed with this framework. Use this as a model for your own project's structure.

