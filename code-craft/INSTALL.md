# Setting up CodeCraft

This guide provides instructions for integrating the CodeCraft framework into your existing project. We recommend using Git submodules for managing the CodeCraft dependency.

## Benefits of Using a Git Submodule

Using a Git submodule to include CodeCraft in your project offers several advantages:

*   **Separation of Concerns:** It keeps the CodeCraft framework files distinct from your project's codebase, making it easier to manage both independently.
*   **Version Control:** You can lock your project to a specific version (commit) of CodeCraft, ensuring stable and reproducible builds.
*   **Easy Updates:** Updating CodeCraft to a newer version is straightforward using standard Git submodule commands.
*   **Collaboration:** Team members can easily clone the project and initialize CodeCraft without manual downloads or version mismatches.

## Setup Instructions

Follow these steps to set up CodeCraft:

### 1. Add CodeCraft as a Git Submodule

Navigate to the root directory of your Git repository and execute the following command:

```bash
git submodule add https://github.com/axhamre/code-craft.git code-craft
```

This command will:
*   Clone the CodeCraft repository into a directory named `code-craft` within your project.
*   Record the submodule addition in your project's `.gitmodules` file.
*   Stage the changes for your next commit.

Commit the submodule addition to your project:

```bash
git add code-craft .gitmodules
git commit -m "Add CodeCraft framework as a submodule"
```

### 2. Initialize Project Structure for CodeCraft Artifacts

CodeCraft relies on a standardized directory structure for managing its generated artifacts. Create the following directories in your project's root to house these outputs:

```bash
mkdir -p project-artifacts/0-Requirements \
         project-artifacts/1-Specification \
         project-artifacts/2-ImplementationPlan \
         project-artifacts/3-Development \
         project-artifacts/4-Verification
```

**Directory Purpose:**

*   `project-artifacts/`: The main container for all CodeCraft outputs.
    *   `0-Requirements/`: Stores documents related to project requirements.
    *   `1-Specification/`: Contains detailed design specifications derived from requirements.
    *   `2-ImplementationPlan/`: Holds plans for how the development will be executed.
    *   `3-Development/`: Includes development artifacts, such as source code generated or managed by CodeCraft processes (if applicable).
    *   `4-Verification/`: Stores testing plans, test results, and other verification documents.

By following these steps, your project will be correctly configured to utilize the CodeCraft framework. Remember to consult the CodeCraft documentation for further guidance on its usage and capabilities.
