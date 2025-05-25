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
cat codecraft/framework/planner/SYSTEM_PROMPT.md | pbcopy

# Provide context
cat codecraft/framework/planner/guidelines.md
cat codecraft/framework/global-llm-rules.md

# Submit requirements → Save output as codecraft/01-specification/technical-specification.md
```

### 2. Technical specification → Implementation plan

```bash
# Continue with Planner or reload
cat codecraft/01-specification/technical-specification.md

# Ask Planner to generate implementation plan
# Save output as codecraft/02-plan/implementation-plan.md
```

### 3. Implementation plan → Code

```bash
# Load Coder  
cat codecraft/framework/coder/SYSTEM_PROMPT.md | pbcopy

# Provide context
cat codecraft/framework/coder/protocol.md
cat codecraft/framework/global-llm-rules.md

# Submit implementation plan
cat codecraft/02-plan/implementation-plan.md

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
cat codecraft/framework/planner/SYSTEM_PROMPT.md | pbcopy
cat codecraft/templates/combined-workflow.md

# Submit requirements → Get both spec and plan
# Save spec to codecraft/01-specification/, plan to codecraft/02-plan/
# Proceed to step 3 (Coder)
```

## Examples to try

**Starter projects:**
- `examples/counter-app/` - Simple interactive component  
- `examples/todo-app/` - Full web application with CRUD

**Templates:**
- `codecraft/templates/input-requirements.md` - How to format requirements
- `codecraft/templates/combined-workflow.md` - Single LLM workflow

## Need more detail?

- **Full guide:** `codecraft/guides/engineer-workflow.md`
- **Framework docs:** `codecraft/framework/` directory
- **Troubleshooting:** Check examples for reference implementations

---

**Next:** Browse `codecraft/examples/` to see CodeCraft in action, or dive into `codecraft/guides/engineer-workflow.md` for comprehensive instructions. 