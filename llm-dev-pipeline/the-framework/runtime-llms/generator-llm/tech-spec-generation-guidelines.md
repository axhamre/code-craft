# technical specification generation guidelines

## overview
a technical specification formalises *what* will be built before implementation begins. generatorllm must generate it as the single source of truth for scope, constraints, and verification.

## document structure
| section | purpose |
|---------|---------|
| id | unique identifier (uuid‑like string) |
| title | concise descriptive name |
| description | high‑level narrative of the system/component |
| assumptions | explicit assumptions; enumerable list |
| scope | statements delimiting in‑scope vs out‑of‑scope features |
| constraints | technical/legal/operational constraints |
| deliverables | concrete artefacts to be produced |
| acceptance_criteria | verifiable statements mapped to scope items |

each specification **must validate** against `tech-spec.schema.json`.

## formatting
* markdown fenced code blocks allowed only for pseudo‑code or examples
* lists use `-` or `*`, never numbered lists inside schema arrays
* wrap lines ≤120 chars

## style
* declarative, not procedural
* avoid ambiguous verbs (“handle”, “support”)

## verification criteria
* every acceptance criterion must be objectively testable
* cross‑reference criterion ids in later implementation plan

