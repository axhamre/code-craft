# Changelog

## 0.8.0 – 2025-05-25

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

## 0.7.0 – 2025-05-23

# changelog
## 0.6.0 – 2025-05-22

* removed all static documentation tooling (`docs-site/`, `.docs/`, mkdocs files, pnpm config)
## 0.5.4 – 2025-05-22

* moved `.npmrc` into `docs-site/` to localise pnpm config
## 0.5.3 – 2025-05-22

* switched docs-site config to **preset-classic** with docs module
* excluded `**/templates/**` markdown that breaks MDX parsing
## 0.5.2 – 2025-05-22

* added `@docusaurus/plugin-content-docs` to docs-site dependencies so dev server starts without manual install
## 0.5.1 – 2025-05-22

* switched documentation tooling to **pnpm** (`packageManager` set, added `.npmrc`)
## 0.5.0 – 2025-05-22

* replaced mkdocs setup with **Docusaurus v3** (`docs-site/` scaffold)
* no file duplication; markdown stays in place
* removed `.docs` directory and reverted related changes
## 0.4.2 – 2025-05-22

* fixed `.docs` configuration: added empty `docs/` directory inside `.docs` to satisfy mkdocs
* renamed root directory to `llm-dev-pipeline-v4.2` to match version
## 0.4.1 – 2025-05-22

* switched to mkdocs-monorepo plugin; doc config relocated to `.docs/mkdocs.yml`
* removed duplicate `docs/` directory
## 0.4.0 – 2025-05-22

* introduced `agents/` alias for naming consistency
* added mkdocs for docs discoverability
* added evaluation harness (`scripts/eval`)
* enriched example project with full commit object
* added contribution and release notes templates
* documented framework‑llm state machine and retry strategy
## 0.3.1 – 2025-05-22

* updated content of `framework-llm/framework-llm-collaboration-guide.md`

## 0.3.0 – 2025-05-22

* drafted generatorllm and executorllm guides
* completed tech-spec generation guidelines
* added verification checklist generation prompt
* added placeholder content for example artifacts
* marked all TODO-LIST tasks as completed

## 0.2.0 – 2025-05-22

* added json schemas for core artifacts
* added system prompts for ExecutorLLM and GeneratorLLM
* documented 32k token budget and chunking strategy
* defined error handling protocol
* added link‑integrity CI script
