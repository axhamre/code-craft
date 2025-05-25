# Planner guidelines

## Technical specification format

```markdown
# Technical specification: [Project Name]

**Project goal:** [One-sentence objective]
**Date:** [YYYY-MM-DD]

---

## 1. Project overview
- **Purpose**: [Problem being solved]
- **Scope**: [What's included/excluded]

## 2. Functional requirements
- **[Feature name]**: [Description and behavior]
- **[Feature name]**: [Description and behavior]

## 3. Technical requirements
- **Technology stack**: [Languages, frameworks, tools]
- **Architecture**: [System design approach]

## 4. Success criteria
- [How to measure completion]
- [Quality benchmarks]

---

### Conditional sections (include if applicable)

**For data-heavy projects:**
## 5. Data requirements
- **Models**: [Key entities and relationships]
- **Storage**: [Database, persistence needs]

**For user-facing applications:**
## 5. User experience requirements
- **Interface**: [UI/UX specifications]
- **Interactions**: [User workflows]

**For integration projects:**
## 5. Integration requirements
- **External systems**: [APIs, services, dependencies]
- **Data exchange**: [Formats, protocols]

**For performance-critical projects:**
## 5. Non-functional requirements
- **Performance**: [Speed, scalability targets]
- **Security**: [Protection requirements]
- **Reliability**: [Uptime, error handling]
```

## Implementation plan format

```markdown
# Implementation plan: [Project Name]

**Date generated:** [YYYY-MM-DD]
**Tech spec reference:** [Path to specification]

---

## Section [N]: [Logical grouping]

### [ ] Task ID: S[N].T[N]
**Description:** [Single, atomic task]
**Affected components/files:**
- `[file/path]` (Action: [Created|Modified|Deleted])

**Dependencies:** [Task IDs or "None"]

**Verification steps:**
- [ ] [Specific, checkable condition]
- [ ] [Specific, checkable condition]

**Commit instruction:** `[type]([scope]): [description]` (max 72 chars)

---
```

## Formatting rules

### Task requirements
- **Atomic scope**: 1-5 related files maximum per task
- **Clear actions**: Specify Created/Modified/Deleted for each file
- **Logical order**: Dependencies must reference earlier task IDs

### Verification criteria
Use specific, observable conditions:
- **File operations**: "File `[path]` exists", "Directory `[path]` contains `[file]`"
- **Content checks**: "File `[path]` contains `[specific text/code]`"
- **Application state**: "Application starts without errors", "Feature `[name]` functions as specified"
- **Build validation**: "Project builds successfully", "No linting errors present"

### Commit types (predefined)
- `feat` - New features
- `fix` - Bug fixes
- `refactor` - Code restructuring
- `docs` - Documentation
- `test` - Testing
- `chore` - Maintenance

### Commit scopes (predefined)
- `api` - Backend/API changes
- `ui` - Frontend/interface changes
- `db` - Database/data changes
- `config` - Configuration changes
- `deps` - Dependency changes 