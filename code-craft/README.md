# CodeCraft

**Build software features systematically using LLMs.**

Transform requirements into working code through a structured 4-step process:
1. **Specify** - Write what you want to build
2. **Plan** - Architect creates detailed implementation steps  
3. **Execute** - Builder implements the code
4. **Verify** - Test and validate the results

## Get started

```bash
# Start building your first feature in 2 minutes
open framework/QUICKSTART.md
```

## Framework structure

```
framework/
├── QUICKSTART.md           # ← Start here
├── templates/              # Prompt templates for each step
├── examples/               # Working example project to copy
├── runtime-llms/           # LLM guides and schemas
│   ├── architect/          # Creates specifications and plans
│   └── builder/            # Implements plans and commits code
└── guides/                 # Detailed documentation
```

## Two LLM roles

- **Architect** - Creates specifications and plans from requirements
- **Builder** - Implements plans and commits code changes

Each LLM has specific prompts, guidelines, and output schemas to ensure consistency.

---

**Ready to build?** → Open `framework/QUICKSTART.md` and copy your first project structure.

