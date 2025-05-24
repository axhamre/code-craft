# Prompt: generate verification checklist

## Objective:
Create a comprehensive verification checklist to validate that the implementation meets the technical specification requirements.

## Instructions for Architect:

1. **Review specification:** Analyze the technical specification to identify all functional and non-functional requirements
2. **Create checklist:** Generate specific, testable verification items
3. **Global standards:** Follow `../../global-llm-rules.md`
4. **Be specific:** Each item should be actionable and measurable

---
## Technical specification:

```
{{TECHNICAL_SPECIFICATION_CONTENT_HERE}}
```

---

## Generated verification checklist:

```markdown
# Verification checklist for: [Project name]

**Date:** {{CURRENT_DATE}}
**Spec reference:** [Path to technical specification]

## Functional verification
- [ ] [Specific functional requirement 1]
- [ ] [Specific functional requirement 2]

## Technical verification
- [ ] [Technical requirement 1]
- [ ] [Technical requirement 2]

## Performance verification
- [ ] [Performance criteria 1]
- [ ] [Performance criteria 2]

## Security verification
- [ ] [Security requirement 1]
- [ ] [Security requirement 2]

## Completion criteria
All items above must be checked before considering the implementation complete.