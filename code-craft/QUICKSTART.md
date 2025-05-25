# CodeCraft quickstart

**Get productive with CodeCraft in 2 minutes.** Embed structured LLM workflows into your existing projects for new features, bug fixes, or refactoring.

## What is CodeCraft?

CodeCraft is a framework for structured software development using LLMs. It uses two specialized agents:
- **Planner:** Converts requirements → technical specifications → implementation plans
- **Coder:** Executes implementation plans → verified code commits

## Quick setup

```bash
# 1. Navigate to your existing project
cd your-existing-project

# 2. Clone CodeCraft and run setup
git clone https://github.com/your-org/code-craft.git /tmp/code-craft
/tmp/code-craft/setup.sh

# 3. Start working
cd codecraft
```

## 4-step workflow

### 1. Requirements → Technical specification

```bash
# Load Planner
cat framework/planner/SYSTEM_PROMPT.md | pbcopy

# Provide context
cat framework/planner/guidelines.md
cat framework/global-llm-rules.md

# Submit requirements → Save output as 01-specification/technical-specification.md
```

### 2. Technical specification → Implementation plan

```bash
# Continue with Planner or reload
cat 01-specification/technical-specification.md

# Ask Planner to generate implementation plan
# Save output as 02-plan/implementation-plan.md
```

### 3. Implementation plan → Code

```bash
# Load Coder  
cat framework/coder/SYSTEM_PROMPT.md | pbcopy

# Provide context
cat framework/coder/protocol.md
cat framework/global-llm-rules.md

# Submit implementation plan
cat 02-plan/implementation-plan.md

# Coder executes tasks and commits changes
```

### 4. Verify and iterate

```bash
npm test     # Run tests
git log      # Review commits
npm start    # Test application
```

## Beginner option: Single LLM workflow

For simple projects, use one Planner session for both specification and plan:

```bash
# Load combined workflow template
cat framework/planner/SYSTEM_PROMPT.md | pbcopy
cat templates/combined-workflow.md

# Submit requirements → Get both spec and plan
# Save spec to 01-specification/, plan to 02-plan/
# Proceed to step 3 (Coder)
```

## Examples to try

**Starter projects:**
- `examples/counter-app/` - Simple interactive component  
- `examples/todo-app/` - Full web application with CRUD

**Templates:**
- `templates/input-requirements.md` - How to format requirements
- `templates/combined-workflow.md` - Single LLM workflow

## Need more detail?

- **Full guide:** `guides/engineer-workflow.md`
- **Framework docs:** `framework/` directory
- **Troubleshooting:** Check examples for reference implementations

---

**Next:** Browse `examples/` to see CodeCraft in action, or dive into `guides/engineer-workflow.md` for comprehensive instructions. 