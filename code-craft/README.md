# CodeCraft

Structured LLM‑assisted software delivery.

## Setup

To integrate CodeCraft into your project, please follow the detailed instructions in our [Setup Guide](INSTALL.md).

For a detailed guide on the CodeCraft development process, see [WORKFLOW.md](WORKFLOW.md).

## Quick start

The following steps outline the core CodeCraft workflow. Generated artifacts are typically stored in your `project-artifacts/` directory, as detailed in `INSTALL.md` and `WORKFLOW.md`.

1. **Specify** – turn requirements into a technical specification.
   • Start with your project requirements (e.g., in `project-artifacts/0-Requirements/project-requirements.md`).
   • Use `codecraft/framework/planner/SYSTEM_PROMPT.md` with your LLM and the requirements.
   • Save the result as `project-artifacts/1-Specification/technical-specification.md`.

2. **Plan** – convert the specification into an implementation plan.
   • Use `codecraft/templates/planning/implementation-plan-generation-prompt.md` (this is a template, see WORKFLOW.md for details) with your LLM and the specification.
   • Save as `project-artifacts/2-ImplementationPlan/implementation-plan.md`.

3. **Execute** – implement the plan.
   • Use `codecraft/framework/coder/SYSTEM_PROMPT.md` with your LLM and the plan.
   • Follow tasks, commit each logical unit, update `CHANGELOG.md`.

4. **Verify** – run automated tests (`npm test`, `pytest`, …).  
   • Fix failures; repeat execute ↔ verify until green.

## Directory layout
| path | purpose |
| ---- | ------- |
| `codecraft/framework/` | system prompts and global rules |
| `codecraft/templates/` | prompt templates |
| `codecraft/examples/`  | reference implementations (for demonstration, not part of core setup) |
