# DevFlow quickstart

Get your first feature built in **2 minutes**.

## Step 1: Copy an example project

Choose a starting point:

```bash
# Beginner: Simple counter app
cp -r framework/examples/counter-app-example my-project

# Intermediate: Todo app with persistence  
cp -r framework/examples/project-artifacts-example my-project

cd my-project
```

## Step 2: Define what you want to build

Edit your requirements:
```bash
open 01-specification/input-requirements.md
```

Write what you want in plain English:
```markdown
# Input requirements

Build a [describe your app] with:
- [Feature 1]
- [Feature 2] 
- [Feature 3]
```

## Step 3: Generate your plan

**Option A: Single LLM workflow (recommended)**
```bash
# Copy the combined template
cp ../framework/templates/combined-workflow-prompt.md prompt.md

# Edit to include your requirements
open prompt.md
```

Give the prompt to any LLM (Claude, GPT-4, etc.) and it will generate both your technical specification AND implementation plan in one go.

**Option B: Two-step workflow**
```bash
# Step 3a: Generate technical specification
cp ../framework/templates/specification/tech-spec-generation-prompt.md spec-prompt.md
# Replace {{INPUT_REQUIREMENTS_CONTENT_HERE}} with your requirements
# Give to Planner LLM → save as 01-specification/technical-specification.md

# Step 3b: Generate implementation plan  
cp ../framework/templates/planning/implementation-plan-generation-prompt.md plan-prompt.md
# Replace {{TECHNICAL_SPECIFICATION_CONTENT_HERE}} with your tech spec
# Give to Planner LLM → save as 02-planned-development/implementation-plan.md
```

## Step 4: Build your feature

```bash
# Create working copy for Coder
cp 02-planned-development/implementation-plan.md 02-planned-development/.tmp/implementation-plan.md
```

Give the implementation plan to your Coder LLM along with your codebase. The Coder will:
- Execute each task sequentially  
- Mark completed tasks with `[x]`
- Commit changes with the specified messages

## You're done! 🎉

Your feature is now built and committed to git. 

## Next steps

- **Test:** Verify everything works as expected
- **Iterate:** Modify requirements and regenerate if needed
- **Scale:** Break larger features into multiple projects

---

**Stuck?** Check `framework/guides/engineer-guide.md` for detailed documentation. 