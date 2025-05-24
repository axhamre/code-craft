# LLM development pipeline

**Build software features systematically using LLMs.**

Transform requirements into working code through a structured 4-step process:
1. **Specify** - Write what you want to build
2. **Plan** - Generate detailed implementation steps  
3. **Execute** - Let LLM implement the plan
4. **Verify** - Test and validate the results

## Get started

```bash
# Start building your first feature in 2 minutes
open the-framework/QUICKSTART.md
```

## Framework structure

```
the-framework/
├── QUICKSTART.md           # ← Start here
├── templates/              # Prompt templates for each step
├── examples/               # Working example project to copy
├── runtime-llms/           # LLM guides and schemas
└── guides/                 # Detailed documentation
```

## Two LLM roles

- **GeneratorLLM** - Creates specifications and plans from requirements
- **ExecutorLLM** - Implements plans and commits code changes

Each LLM has specific prompts, guidelines, and output schemas to ensure consistency.

---

**Ready to build?** → Open `the-framework/QUICKSTART.md` and copy your first project structure.

