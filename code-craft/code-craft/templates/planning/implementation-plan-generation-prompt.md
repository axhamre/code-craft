# Implementation plan generation prompt

## Task
Generate a detailed implementation plan based on the provided technical specification.

## Context files provided
1. **Technical specification:** `../01-specification/technical-specification.md`
2. **Guidelines:** `framework/planner/guidelines.md` (implementation plan section)
3. **Global rules:** `framework/global-llm-rules.md`

---

## Technical specification

**[ENGINEER: PASTE THE TECHNICAL SPECIFICATION HERE]**

---

## Codebase context (if applicable)

**[ENGINEER: PASTE ANY EXISTING CODEBASE CONTEXT HERE - file structure, key files, etc.]**

---

## Instructions for Planner:

1.  **Input:** Technical specification above + any codebase context
2.  **Structure output:** Strictly adhere to the content and formatting rules defined in `framework/planner/guidelines.md`. This includes breaking tasks into atomic, verifiable units with clear commit instructions.
3.  **Global rules:** Follow `framework/global-llm-rules.md` for style and approach  
4.  **Dependencies:** Ensure tasks are ordered logically with clear dependency relationships
5.  **Clarity & actionability:** Ensure the plan is unambiguous and directly actionable by **Coder**.

---

## Required output structure

Refer to the implementation plan template in `framework/planner/guidelines.md` for the exact structure.

The plan must include:
- Task sections with descriptive titles
- Atomic tasks with IDs, descriptions, affected files
- Clear verification criteria for each task
- Proper dependency management
- Specific commit instructions

---

*(Planner: Populate the implementation plan here, following the guidelines.)* 