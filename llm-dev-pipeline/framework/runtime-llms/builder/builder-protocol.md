# Agent execution protocol for software implementation

**Version:** 1.0
**Date:** 2025-05-17

## 1. Introduction

This document outlines the protocol for an AI agent tasked with software development and modification based on a provided `implementation-plan.md`. The goal is to ensure systematic execution, verification, and version control.

## 2. Prerequisites

*   **Implementation Plan (`implementation-plan.md`):** A detailed, step-by-step plan located in `02-planned-development/implementation-plan.md`. This plan will be the primary input for the agent. It should clearly define tasks, affected files, verification steps, and commit instructions for each task.
*   **Working Copy of Implementation Plan:** The agent will use a copy of the plan, typically `02-planned-development/.tmp/implementation-plan.md`, to mark off completed tasks and criteria.
*   **Access to Version Control (Git):** The agent must have permissions to commit changes to the repository.
*   **Development Environment:** A fully set up development environment with all necessary tools (e.g., Node.js, npm/pnpm/yarn, IDE tools, linters, test runners).

## 3. Execution workflow

The agent will process the `implementation-plan.md` task by task, following this general workflow for each task:

1.  **Task Identification:** Identify the next uncompleted task in the implementation plan (working copy).
2.  **Understand Task:** Parse the task description, affected components, inputs, outputs, and dependencies.
3.  **Execute Changes:** Make the necessary code modifications, file deletions, or additions as described.
4.  **Verify Task Completion:**
    *   Iterate through each **Verification Step / Success Criterion** listed for the task.
    *   Perform the specified action (e.g., run a command, check file existence, inspect file content).
    *   If a criterion is met, mark it as complete (e.g., `[x]`) in the working copy of the implementation plan.
    *   If a criterion is not met, attempt to troubleshoot and re-execute the changes. If persistent issues arise, halt and report (mechanism TBD, could be updating a status field in the plan or logging).
5.  **Commit Changes (if all criteria met):**
    *   Once all verification criteria for a task are successfully met, use the exact `Agent Commit Instruction` provided in the task to commit the changes.
    *   Ensure the commit message adheres to any specified patterns and length constraints.
6.  **Update Working Plan:** Mark the entire task as complete (e.g., `### [x] Task ID: ...`) in the working copy of the implementation plan.
7.  **Proceed to Next Task:** Repeat from step 1.

## 4. Error handling and reporting

*   **Minor Errors:** If a verification step fails, the agent should attempt self-correction based on the error message or task context.
*   **Persistent Errors:** If a task cannot be completed or verified after a reasonable number of attempts (e.g., 3), the agent should:
    *   Revert any partial changes made for that specific task to maintain a clean state.
    *   Clearly mark the task as FAILED in the working implementation plan, along with a brief error summary.
    *   Halt execution of further tasks and await manual intervention or revised instructions.
*   **Tooling/Environment Issues:** If the agent encounters issues with the development environment or tools (e.g., Git command fails, npm script errors not related to the code change), it should report these immediately.

## 5. Completion

Once all tasks in the `implementation-plan.md` are processed (either completed and committed, or marked as FAILED), the agent's primary execution is considered complete. It should provide a summary report, possibly by updating a final section in the working implementation plan or generating a separate output file.

## 6. Logging

The agent should maintain a log of its actions, including:
*   Task started.
*   Files modified/deleted/created.
*   Commands executed for verification.
*   Success/failure of verification steps.
*   Commit hashes for successful tasks.
*   Errors encountered.

This log can be invaluable for debugging and auditing the agent's performance.

---

This protocol is a living document and may be updated as the agent's capabilities and project requirements evolve. 