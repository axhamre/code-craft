# CodeCraft

**Transform requirements into working software using structured LLM workflows.**

CodeCraft is a framework for **AI-assisted software development** that uses specialized LLM agents to create structured, verifiable implementations.

## Workflow

1. **Specify** - Planner converts requirements → technical specifications  
2. **Plan** - Planner creates detailed implementation steps
3. **Execute** - Coder implements the code
4. **Verify** - Test and validate the implementation

## Quick start

```bash
# In your existing project directory
git clone https://github.com/your-org/code-craft.git /tmp/code-craft
/tmp/code-craft/setup.sh
cd codecraft
```

See `QUICKSTART.md` for complete workflow instructions.

## Directory structure

```
CodeCraft/
├── framework/               # Core LLM agents
│   ├── planner/            # Creates specifications and plans
│   ├── coder/              # Implements plans and commits code
│   └── global-llm-rules.md # Style and formatting rules
├── templates/               # Prompt templates
├── examples/                # Reference implementations  
├── guides/                  # Detailed workflows
└── QUICKSTART.md           # Get started quickly
```

## Key components

- **Planner** - Creates specifications and plans from requirements
- **Coder** - Implements plans and commits code changes
- **Templates** - Starting prompts for different phases
- **Examples** - Complete reference projects

## Documentation

- `QUICKSTART.md` - Get productive in 2 minutes
- `guides/engineer-workflow.md` - Complete workflow guide
- `examples/` - Reference implementations

