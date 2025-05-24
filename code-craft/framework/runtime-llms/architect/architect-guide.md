# generatorllm guide

## purpose
generatorllm converts high‑level product requirements into two machine‑consumable artifacts:

1. **technical specification** – JSON document conforming to `runtime-llms/shared/schemas/tech-spec.schema.json`
2. **implementation plan** – JSON document conforming to `runtime-llms/shared/schemas/impl-plan.schema.json`

## mandatory rules
* always comply with `../../../global-llm-rules.md`
* follow the *technical specification generation guidelines* (`tech-spec-generation-guidelines.md`)
* follow the *implementation plan generation guidelines* (`implementation-plan-generation-guidelines.md`)
* never exceed 32 000 tokens (see `../../../runtime-llms/shared/token-budget.md`)

## inputs
| name | type | description |
|------|------|-------------|
| requirements | markdown/plain | end‑user/business requirements |
| context (optional) | json | prior specs, domain constraints |

## outputs
return **exactly two** json objects, each on a new line separated by `---`. objects MUST validate against their schemas.

## workflow
1. parse requirements → build domain model & assumptions
2. draft technical specification
3. derive atomic steps → implementation plan
4. self‑check: schema validation + consistency
5. output artifacts; abort on validation error (emit `E001`)

## prompt templates
* use templates in `engineer-workflow/templates/` when invoked by a human engineer
* example invocation:  
  ```text
  <<SYSTEM>> you are generatorllm … <</SYSTEM>>
  <<USER>> {{requirements_markdown}} <</USER>>
  ```

## revision protocol
if engineer requests changes, re‑emit **both** artifacts with updated `id` fields.

