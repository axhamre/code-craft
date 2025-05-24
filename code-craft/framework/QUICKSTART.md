# CodeCraft quickstart

Get your first feature built in **2 minutes**.

## Copy the framework structure

```bash
# 1. Copy the example project structure
cp -r framework/examples/project-artifacts-example my-first-project

# 2. Navigate to your project
cd my-first-project
```

## Phase 1: specify what to build

```bash
# 3. Edit your requirements
open 01-specification/input-requirements.md
```

Replace the placeholder with your actual requirements:
```markdown
# Input requirements

Build a simple task management web app with:
- Add/delete tasks 
- Mark tasks complete
- Local storage persistence
- Clean, minimal UI
```

## Phase 2: generate technical specification

```bash
# 4. Copy the spec generation template
cp ../framework/templates/specification/tech-spec-generation-prompt.md spec-prompt.md

# 5. Replace placeholder with your requirements
sed -i '' 's/{{INPUT_REQUIREMENTS_CONTENT_HERE}}/'"$(cat 01-specification/input-requirements.md)"'/g' spec-prompt.md
```

**Give `spec-prompt.md` to your Architect LLM** (Claude, GPT-4, etc.) and save the output as:
```bash
# Save the output here
echo "[ARCHITECT OUTPUT]" > 01-specification/technical-specification.md
```

## Phase 3: generate implementation plan  

```bash
# 6. Copy the plan generation template
cp ../framework/templates/planning/implementation-plan-generation-prompt.md plan-prompt.md

# 7. Replace placeholder with your tech spec
sed -i '' 's/{{TECHNICAL_SPECIFICATION_CONTENT_HERE}}/'"$(cat 01-specification/technical-specification.md)"'/g' plan-prompt.md
```

**Give `plan-prompt.md` to your Architect LLM** and save the output as:
```bash
# Save the output here  
echo "[ARCHITECT OUTPUT]" > 02-planned-development/implementation-plan.md
```

## Phase 4: execute the plan

```bash
# 8. Create working copy for Builder
cp 02-planned-development/implementation-plan.md 02-planned-development/.tmp/implementation-plan.md
```

**Give the implementation plan to your Builder LLM** along with your codebase. The Builder will:
- Execute each task sequentially
- Mark completed tasks with `[x]`
- Commit changes with specified messages
- Update the working copy in `.tmp/`

## Next steps

- **Verify:** Check that your implementation matches the technical specification
- **Iterate:** Refine requirements and regenerate if needed
- **Scale:** Use this pattern for larger features by breaking them into smaller projects

## Framework structure

```
my-first-project/
├── 01-specification/
│   ├── input-requirements.md     # ← Your requirements
│   └── technical-specification.md # ← Architect output
├── 02-planned-development/
│   ├── implementation-plan.md    # ← Architect output  
│   └── .tmp/
│       └── implementation-plan.md # ← Builder working copy
└── 03-verification/
    └── verification-report.md    # ← Your verification results
```

**Ready to build?** Start with `01-specification/input-requirements.md` and follow the phases above. 