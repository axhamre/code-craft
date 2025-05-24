#!/usr/bin/env python3
"""Lightweight evaluation harness.

Usage:
    python run_eval.py

It validates sample outputs in `samples/` against schemas.
"""
import json, pathlib, sys
from jsonschema import validate, ValidationError

repo_root = pathlib.Path(__file__).resolve().parents[2]
schema_dir = repo_root / 'runtime-llms' / 'shared' / 'schemas'
sample_dir = pathlib.Path(__file__).resolve().parent / 'samples'

def load_schema(name):
    with open(schema_dir / name) as f:
        return json.load(f)

SCHEMAS = {
    'tech-spec.json': load_schema('tech-spec.schema.json'),
    'impl-plan.json': load_schema('impl-plan.schema.json'),
    'commit-object.json': load_schema('commit-object.schema.json'),
}

def main():
    failures = 0
    for sample_file in sample_dir.glob('*.json'):
        schema = SCHEMAS.get(sample_file.name)
        if not schema:
            continue
        data = json.load(open(sample_file))
        try:
            validate(data, schema)
            print(f'PASS {sample_file.name}')
        except ValidationError as e:
            print(f'FAIL {sample_file.name}: {e.message}')
            failures += 1
    sys.exit(failures)

if __name__ == '__main__':
    main()
