# DevFlow engineer guide - Legacy reference

**Note:** This is the legacy engineer guide. The current guide is `engineer-workflow.md`.

The framework uses **Planner** to create project artifacts and **Coder** to implement plans.

## Overview of the complete workflow

1.  **Engineer:** Assemble initial requirements and context.
2.  **Engineer:** Craft prompt for **Planner** to produce a technical specification.
    *   *Input:* Initial project requirements.
    *   *Adheres to:* `framework/planner/guidelines.md`
3.  **Planner:** Generates technical specification.
    *   *Output:* `01-specification/technical-specification.md`

*Project requirements have been converted to a tech spec.*

4.  **Engineer:** Review and approve the tech specification.
5.  **Engineer:** Craft prompt for **Planner** to produce an implementation plan from the `technical-specification.md`.
    *   *Input:* Technical specification from previous step.
    *   *Adheres to:* `framework/planner/guidelines.md`
6.  **Planner:** Generates implementation plan.
    *   *Output:* `02-plan/implementation-plan.md`

*Technical specification converted to step-by-step plan.*

7.  **Engineer:** Review and approve the implementation plan.
8.  **System:** Prepare for **Coder**.
    *   Copy the implementation plan to a temporary working copy.
    *   Ensure the codebase is in a clean Git state.
9.  **Coder:** Executes tasks from the working copy.
    *   *Follows:* `framework/coder/protocol.md`
    *   *Modifies:* Working copy with progress tracking
    *   *Outputs:* Code commits for each completed task

*Implementation plan converted to committed code.*

10. **Engineer (optional):** Craft prompt for **Planner** for a verification checklist.
    *   *Input:* Tech spec and implementation plan
11. **Planner (optional):** Generates verification checklist.

## Core directory structure

*Essential files to understand and use the framework:*

**Framework components:**
*   **Planner:** `framework/planner/` (main prompt & guidelines)
*   **Coder:** `framework/coder/` (main prompt & protocol)

**Workflow guides:**
*   **This file:** `guides/engineer-workflow.md` - Complete engineer workflow
*   **Quick start:** `QUICKSTART.md` - 2-minute setup

**Templates and examples:**
*   **Input templates:** `templates/` for starting prompts
*   **Reference examples:** `examples/` for complete project examples

## Full directory structure

```
DevFlow/
├── framework/
│   ├── planner/
│   │   ├── SYSTEM_PROMPT.md
│   │   └── guidelines.md
│   ├── coder/
│   │   ├── SYSTEM_PROMPT.md
│   │   └── protocol.md
│   └── global-llm-rules.md
├── templates/
│   ├── specification/
│   ├── planning/
│   └── verification/
├── examples/
│   ├── todo-app/
│   │   ├── 01-specification/
│   │   ├── 02-plan/
│   │   ├── 03-verification/
│   │   └── 04-coder-output/
├── guides/
│   ├── engineer-workflow.md
│   └── engineer-guide.md
├── QUICKSTART.md
├── README.md
└── CHANGELOG.md
```

## Navigation and usage

**Key files to understand:**

*   **`README.md` (root):** Your first stop. Explains DevFlow's purpose, defines the roles (**Planner**, **Coder**), and points you to this `engineer-workflow.md`.

**Framework configuration:**

*   `framework/planner/` contains the main prompt for **Planner** and the crucial `guidelines.md` file that defines the *required structure* for documents like technical specifications and implementation plans.
*   `framework/coder/` provides the prompt and the strict `protocol.md` that **Coder** follows to implement changes.
*   **`templates/`**: A library of starting prompts. You'll copy and customize these for your specific project tasks before **Planner** uses them. They are organized by the development phase they support.

**Examples for reference:**

*   `examples/` provides complete, working examples of DevFlow in action. Study these to understand the input/output formats and workflow patterns. 