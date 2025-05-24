# Changelog

## 1.0.0 – 2024-12-11

### 🎉 Major Release: CodeCraft v1.0

**Framework restructured for production use with improved terminology and simplified structure.**

### Added
* **Simplified directory structure**: Moved from `framework/runtime-llms/architect|builder/` to clean `framework/planner/` and `framework/coder/`
* **Consolidated guidelines**: Single `framework/planner/guidelines.md` containing both spec and plan generation
* **New QUICKSTART.md**: Complete rewrite with 4-step workflow for 2-minute setup
* **Engineer workflow guide**: Comprehensive `guides/engineer-workflow.md` with step-by-step instructions
* **Combined workflow template**: Single LLM option for simpler projects

### Changed
* **Role terminology**: Architect → Planner, Builder → Coder throughout framework
* **System prompts**: Updated to use Planner/Coder terminology and correct paths
* **Directory organization**: Moved templates, examples, guides to root level for easier access
* **Documentation**: All guides, templates, and examples updated with consistent terminology
* **Path references**: Updated all framework paths to use new simplified structure

### Removed
* **runtime-llms directory**: Eliminated confusing nested structure
* **Duplicate documentation**: Cleaned up inconsistent and outdated guides
* **Old terminology**: Removed all Architect/Builder references

### Fixed
* **Structural inconsistencies**: All path references now align with actual directory structure
* **Terminology mismatches**: Consistent Planner/Coder usage throughout
* **Outdated documentation**: Removed and replaced obsolete guides and quickstarts

---

## 0.8.0 – 2024-12-10

### Fixed
* **framework structure alignment**: updated all path references in engineer guide to match current directory structure (`framework/runtime-llms/architect|builder/`)
* **role terminology consistency**: standardized all references to use "Architect" and "Builder" (removed GeneratorLLM/ExecutorLLM inconsistency)
* **workflow gaps**: removed JSON schema dependencies, replaced with markdown format specifications throughout
* **missing QUICKSTART.md**: created comprehensive quickstart guide with step-by-step workflow

### Changed
* **system prompts**: updated to use "Architect"/"Builder" terminology and expect markdown input/output
* **guidelines**: replaced JSON schemas with markdown format specifications for tech specs and implementation plans
* **templates**: updated all prompt templates to reference correct paths and use proper role terminology
* **protocol**: simplified builder protocol to work with markdown plans instead of JSON

### Removed
* **JSON schemas**: deleted all schema files (`tech-spec.schema.json`, `impl-plan.schema.json`, `commit-object.schema.json`)
* **FrameworkLLM references**: removed mentions of non-existent coordination component
* **shared/schemas directory**: cleaned up unused schema infrastructure

## 0.7.0 – 2024-12-09

# changelog
## 0.6.0 – 2024-12-08

* removed all static documentation tooling (`docs-site/`, `.docs/`, mkdocs files, pnpm config)
## 0.5.4 – 2024-12-07

* moved `.npmrc` into `docs-site/` to localise pnpm config
## 0.5.3 – 2024-12-06

* switched docs-site config to **preset-classic** with docs module
* excluded `**/templates/**` markdown that breaks MDX parsing
## 0.5.2 – 2024-12-05

* added `@docusaurus/plugin-content-docs` to docs-site dependencies so dev server starts without manual install
## 0.5.1 – 2024-12-04

* switched documentation tooling to **pnpm** (`packageManager` set, added `.npmrc`)
## 0.5.0 – 2024-12-03

* replaced mkdocs setup with **Docusaurus v3** (`docs-site/` scaffold)
* no file duplication; markdown stays in place
* removed `.docs` directory and reverted related changes
## 0.4.2 – 2024-12-02

* fixed `.docs` configuration: added empty `docs/` directory inside `.docs` to satisfy mkdocs
* renamed root directory to `llm-dev-pipeline-v4.2` to match version
## 0.4.1 – 2024-12-01

* switched to mkdocs-monorepo plugin; doc config relocated to `.docs/mkdocs.yml`
* removed duplicate `docs/` directory
## 0.4.0 – 2024-11-30

* introduced `agents/` alias for naming consistency
* added mkdocs for docs discoverability
* added evaluation harness (`scripts/eval`)
* enriched example project with full commit object
* added contribution and release notes templates
* documented framework‑llm state machine and retry strategy
## 0.3.1 – 2024-11-29

* updated content of `framework-llm/framework-llm-collaboration-guide.md`

## 0.3.0 – 2024-11-28

* drafted generatorllm and executorllm guides
* completed tech-spec generation guidelines
* added verification checklist generation prompt
* added placeholder content for example artifacts
* marked all TODO-LIST tasks as completed

## 0.2.0 – 2024-11-27

* added json schemas for core artifacts
* added system prompts for ExecutorLLM and GeneratorLLM
* documented 32k token budget and chunking strategy
* defined error handling protocol
* added link‑integrity CI script
