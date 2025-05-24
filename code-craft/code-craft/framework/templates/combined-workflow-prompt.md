# Combined workflow prompt: Generate specification and implementation plan

## Objective:
Generate both a technical specification AND implementation plan from the provided requirements in a single workflow.

## Instructions:

1. **Analyze requirements:** Review the input requirements thoroughly
2. **Generate specification:** Create a detailed technical specification following the format guidelines
3. **Generate plan:** Create a step-by-step implementation plan based on your specification
4. **Global standards:** Follow `../global-llm-rules.md` for all content

## Input requirements:

```
{{INPUT_REQUIREMENTS_CONTENT_HERE}}
```

---

## Your output should contain exactly two sections:

### TECHNICAL SPECIFICATION

```markdown
# Technical specification for: [Project name]

**Date:** [Today's date]
**Version:** 1.0

---

## Project overview
[Brief description of what is being built and why]

## Functional requirements
### Core features
- [Feature 1: Description]
- [Feature 2: Description]

### User interactions
- [Interaction 1: Description]
- [Interaction 2: Description]

## Technical requirements
### Architecture
- [Component 1: Description and responsibility]
- [Component 2: Description and responsibility]

### Data models
- [Entity 1: Fields and relationships]
- [Entity 2: Fields and relationships]

## Non-functional requirements
- **Performance:** [Specific metrics]
- **Compatibility:** [Browser/platform requirements]

## Assumptions and constraints
### Assumptions
- [Assumption 1]
- [Assumption 2]

### Constraints
- [Constraint 1]
- [Constraint 2]

## Success criteria
- [Criterion 1: How success will be measured]
- [Criterion 2: How success will be measured]

---
```

### IMPLEMENTATION PLAN

```markdown
# Implementation plan for: [Project name]

**Date generated:** [Today's date]
**Tech spec version/reference:** ../01-specification/technical-specification.md

---

## Section 1: [Descriptive title]

### [ ] Task ID: S1.T1
**Description:** [What needs to be done]
**Affected Components/Files:**
  - `filename.ext` (Created/Modified/Deleted)
**Inputs (if any):**
  - [Requirements or dependencies]
**Outputs/Artifacts:**
  - [Expected results]
**Dependencies:** [Previous task IDs or "None"]
**Verification Steps / Success Criteria:**
  *   [ ] **Criterion 1:** [Specific, testable check]
  *   [ ] **Criterion 2:** [Specific, testable check]
**Agent Commit Instruction:** After successful verification, commit with message: `type(scope): description` (max 72 chars)
**Notes/Hints for Agent (Optional):** [Any helpful context]

[Continue with additional sections and tasks as needed]

---

## Summary & completion checklist
*   [ ] All core functionality implemented
*   [ ] All success criteria met
*   [ ] Cross-browser testing completed
```

---

**Instructions for saving:**
1. Save the TECHNICAL SPECIFICATION section as `01-specification/technical-specification.md`
2. Save the IMPLEMENTATION PLAN section as `02-planned-development/implementation-plan.md`
3. Copy the implementation plan to `02-planned-development/.tmp/implementation-plan.md` as a working copy 