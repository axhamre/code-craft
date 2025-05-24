# llm-dev-pipeline

**`llm-dev-pipeline` is a framework for orchestrating LLM-driven software development. It provides a structured methodology, guidelines, and templates to move from requirements to verified, LLM-implemented code.**

The framework promotes a phased approach:
1.  **Specification:** Defining clear technical outcomes.
2.  **Planning:** Generating detailed, actionable implementation steps.
3.  **Execution:** Utilizing an LLM to carry out the planned implementation.
4.  **Verification:** Ensuring the implemented work meets the specified requirements.

This framework is designed for engineers and teams looking to integrate LLMs systematically into their development lifecycle, enhancing productivity and consistency.

---

## Navigating This Framework

*   **For Engineers using the framework:**
    *   Start with the **[engineer-guide.md](./the-framework/engineer-workflow/guides/engineer-guide.md)** for a comprehensive walkthrough, setup instructions, and workflow details.
*   **For understanding example project outputs:**
    *   See the **[project-artifacts-example/](./the-framework/engineer-workflow/examples/project-artifacts-example/)** directory.
*   **For framework developers & contributors:**
    *   Refer to documentation within **[the-framework/](./the-framework/)**.

---

## LLM Roles in `llm-dev-pipeline`

Two distinct LLM roles are conceptualized within this framework's operation:

1.  **`GeneratorLLM` (Project Artifact Generator)**
    *   **Role:** The LLM responsible for taking project-specific inputs (requirements, specialized prompts) and using the framework's templates and guidelines to generate key project artifacts like `technical-specification.md` and `implementation-plan.md`.
    *   **Primary Guide:** **[generator-llm-guide.md](./the-framework/runtime-llms/generator-llm/generator-llm-guide.md)**
    *   **Key Inputs:** Utilizes prompts from **[./the-framework/engineer-workflow/templates/](./the-framework/engineer-workflow/templates/)** and adheres to guidelines in **[./the-framework/runtime-llms/generator-llm/](./the-framework/runtime-llms/generator-llm/)**.

2.  **`ExecutorLLM` (Plan Executor)**
    *   **Role:** The LLM that acts as an AI agent, systematically executing the tasks defined in a generated `implementation-plan.md`. This involves code modification, running verifications, and making version control commits.
    *   **Primary Guide:** **[executor-llm-guide.md](./the-framework/runtime-llms/executor-llm/executor-llm-guide.md)**
    *   **Core Protocol:** Adheres strictly to the **[executor-llm-protocol.md](./the-framework/runtime-llms/executor-llm/executor-llm-protocol.md)**.

