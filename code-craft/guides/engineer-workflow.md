# CodeCraft engineer guide

This guide provides **step-by-step instructions** for using CodeCraft to implement software projects.

## Prerequisites

✅ **System check:**
- **Git:** Version control for committing changes
- **LLM API access:** OpenAI, Anthropic, or local model
- **Required project tools:** Node.js, Python, Docker, etc. (project-dependent)

✅ **Repository setup:**
```bash
# Initialize git repository (if needed)
git init
git add .
git commit -m "initial commit"

# Set up project structure
mkdir 01-specification 02-plan 03-implementation
```

## Core workflow

### Phase 1: Requirements to technical specification

**Input:** Project requirements (user stories, feature requests, etc.)  
**Output:** `01-specification/technical-specification.md`  
**Agent:** Planner

```bash
# 1. Set up the Planner
cat framework/planner/SYSTEM_PROMPT.md | pbcopy # (Copy prompt to LLM)

# 2. Provide context files
cat framework/planner/guidelines.md
cat framework/global-llm-rules.md

# 3. Submit your requirements
# Paste your project requirements to the LLM

# 4. Save the output
# Copy the generated specification to 01-specification/technical-specification.md
```

### Phase 2: Technical specification to implementation plan

**Input:** `01-specification/technical-specification.md`  
**Output:** `02-plan/implementation-plan.md`  
**Agent:** Planner  

```bash
# 1. Continue with same Planner session or setup new one
cat framework/planner/SYSTEM_PROMPT.md | pbcopy

# 2. Provide the tech spec
cat 01-specification/technical-specification.md

# 3. Request implementation plan generation
# Ask the LLM to generate an implementation plan based on the spec

# 4. Save the output  
# Copy the generated plan to 02-plan/implementation-plan.md
```

### Phase 3: Implementation plan execution

**Input:** `02-plan/implementation-plan.md`  
**Output:** Committed code changes  
**Agent:** Coder

```bash
# 1. Set up the Coder
cat framework/coder/SYSTEM_PROMPT.md | pbcopy # (Copy prompt to LLM)

# 2. Provide context files
cat framework/coder/protocol.md
cat framework/global-llm-rules.md

# 3. Provide the implementation plan
cat 02-plan/implementation-plan.md

# 4. Execute tasks
# The Coder will implement each task, verify completion, and commit changes
```

### Phase 4: Verification and iteration

**Review and test:**
```bash
# Run tests
npm test    # or appropriate test command for your project

# Review git history
git log --oneline

# Test the application
npm start   # or appropriate start command
```

**If issues found:**
- Update requirements and restart from Phase 1, or
- Manually fix critical issues and update documentation

## Templates and examples

**Starter templates:**
- `templates/input-requirements.md` - Format for project requirements
- `templates/combined-workflow.md` - Single LLM workflow template

**Reference examples:**
- `examples/todo-app/` - Simple web application
- `examples/counter-app/` - Basic interactive component

## Advanced workflows

### Combined single-LLM workflow
For simpler projects, use one Planner session to generate both specification and implementation plan:

```bash
# 1. Setup Planner with combined workflow template
cat framework/planner/SYSTEM_PROMPT.md | pbcopy
cat templates/combined-workflow.md

# 2. Submit requirements and request both spec and plan
# The LLM will generate both documents in sequence

# 3. Save outputs to respective directories
```

### Iterative development
For complex projects requiring multiple cycles:

1. Start with MVP requirements → basic spec → basic plan → MVP implementation
2. Add feature requirements → updated spec → extended plan → feature implementation  
3. Repeat as needed

## Troubleshooting

### Common issues

**Planner outputs incorrect format:**
- Check that `framework/planner/guidelines.md` was provided as context
- Verify the requirements are clear and detailed

**Coder skips verification steps:**  
- Ensure `framework/coder/protocol.md` was provided as context
- Check that verification criteria in the plan are specific and testable

**Dependency/tool errors:**
- Verify all required tools are installed (Node.js, Python, etc.)
- Check that the project structure matches what's specified in the plan

### Error recovery

**If a task fails during implementation:**
1. Read the error message carefully
2. Fix the issue manually if simple
3. Update the implementation plan to reflect the fix
4. Continue with remaining tasks

**If the specification is incomplete:**
1. Gather additional requirements  
2. Regenerate the specification with more detail
3. Update or regenerate the implementation plan accordingly

---

**Support:** Review the templates and examples directories for reference implementations and troubleshooting guidance. 