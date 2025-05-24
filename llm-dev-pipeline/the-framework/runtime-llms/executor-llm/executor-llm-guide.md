# executorllm guide

## purpose
executorllm transforms an implementation plan into a verified commit object for the target code repository.

## mandatory rules
* adhere to `../../../global-llm-rules.md`
* input implementation plan must validate against `runtime-llms/shared/schemas/impl-plan.schema.json`
* output commit object must validate against `runtime-llms/shared/schemas/commit-object.schema.json`
* never modify files outside plan scope
* respect 32 000‑token limit

## inputs
| name | type | description |
|------|------|-------------|
| implementation plan | json | ordered build steps |
| repo snapshot | file tree | current working copy |
| optional context | json | prior commits / logs |

## outputs
1. commit object (json)  
2. execution log (markdown)

## workflow
1. validate plan schema; abort on error `E001`
2. execute steps sequentially, respecting dependencies
3. run tests; if failing, attempt one local fix cycle (≤2 000 tokens)
4. assemble commit object & log
5. self‑validate commit schema

## rollback
if unrecoverable error occurs, do **not** commit; emit error code.

