# CodeCraft Development Workflow

This document outlines the structured software delivery process using the CodeCraft framework.

## Prerequisites & Initial Setup

Before starting, ensure you have the following:
- Git installed.
- Access to a Large Language Model (e.g., OpenAI, Anthropic, or a local model).
- Your project's specific toolchain (e.g., Node.js, Python, Docker) ready.

**Important:** Make sure you have followed the instructions in [INSTALL.md](INSTALL.md) to integrate CodeCraft into your project and create the necessary `project-artifacts/` directory structure.

You will need to create the initial project requirements yourself. We recommend placing them in:
`project-artifacts/0-Requirements/project-requirements.md`

## Understanding CodeCraft Prompts

CodeCraft provides two main types of prompts:
- **Framework Prompts (`code-craft/framework/`):** These are designed for direct use. They contain system prompts and core instructions for different phases.
- **Template Prompts (`code-craft/templates/`):** These offer starting points for more complex or customizable interactions, such as detailed plan generation. You might copy and adapt these templates to better suit your project's specific needs or your preferred LLM's nuances.

## Phase 1: Specify

**Purpose:** To translate user/project requirements into a detailed technical specification that will guide development.

- **Input:** Your project requirements document (e.g., `project-artifacts/0-Requirements/project-requirements.md`).
- **Agent:** Planner
- **Action:**
    1. Open `code-craft/framework/planner/SYSTEM_PROMPT.md`.
    2. Send this prompt and the content of your `project-requirements.md` to the LLM.
- **Output:** Save the generated specification as `project-artifacts/1-Specification/technical-specification.md`.

## Phase 2: Plan

**Purpose:** To break down the technical specification into a series of actionable development tasks.

- **Input:** The technical specification (e.g., `project-artifacts/1-Specification/technical-specification.md`).
- **Agent:** Planner
- **Action:**
    1. Open `code-craft/templates/planning/implementation-plan-generation-prompt.md`. This is a template; review and potentially adapt it for your LLM.
    2. Provide this prompt and the `technical-specification.md` to the LLM.
- **Output:** Save the plan as `project-artifacts/2-ImplementationPlan/implementation-plan.md` and commit it to your version control.

## Phase 3: Execute

**Purpose:** To translate the implementation plan into working code and associated tests within your project's actual source tree.

- **Input:** The implementation plan (e.g., `project-artifacts/2-ImplementationPlan/implementation-plan.md`).
- **Agent:** Coder
- **Action:**
    1. Open `code-craft/framework/coder/SYSTEM_PROMPT.md`.
    2. Provide this prompt and the `implementation-plan.md` to the LLM.
    3. Implement tasks sequentially. Commit logical units of work frequently.
- **Output:** Application code changes and new unit tests committed to your project's codebase. Update `CHANGELOG.md` as you complete features or fixes.
- **Note on `project-artifacts/3-Development/`:** The `project-artifacts/3-Development/` directory can be used for notes, LLM interaction logs, or temporary files related to the coding process.

## Phase 4: Verify

**Purpose:** To ensure the implemented code is correct, meets quality standards, and fulfills the requirements outlined in the technical specification.

- **Input:** The implemented code and tests from Phase 3.
- **Agent:** Verifier (often the Engineer, potentially aided by LLM for checklist generation)
- **Action:**
    1. Run your project's full test suite (e.g., `npm test`, `pytest`).
    2. Optionally, if you have a verification checklist template (like `code-craft/templates/verification/verification-checklist-generation-prompt.md`), use it with your LLM and the `project-artifacts/1-Specification/technical-specification.md` to generate a checklist. This can be saved as `project-artifacts/4-Verification/verification-checklist.md`.
- **Output:** Successful test suite execution and, if used, a satisfactorily completed verification checklist. If tests fail or the checklist isn't met, iterate by returning to Phase 3 to fix code, then re-verify. Test reports or the filled checklist can be stored in `project-artifacts/4-Verification/`.

## Troubleshooting
| Symptom                                  | Resolution                                                                      |
| ---------------------------------------- | ------------------------------------------------------------------------------- |
| LLM provides incomplete or vague output  | Provide more context, refine the prompt, or ask it to regenerate the specific step. |
| Failing automated tests                  | Review error messages, debug the code, fix the issues, and re-run tests.        |
| Code doesn't meet all specification items | Revisit Phase 3 (Execute) to address the gaps, possibly regenerate parts of the code. |
| Unclear next steps in the plan           | If the plan is ambiguous, consider a brief return to Phase 2 (Plan) to refine it. |
