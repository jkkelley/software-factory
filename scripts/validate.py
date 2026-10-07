#!/usr/bin/env python3
"""Repository self-checks for the Software Factory.

Checks:
  1. Every example handoff in examples/ validates against schemas/handoff.schema.json.
  2. Every file in tests/invalid/ is REJECTED by the schema (the contract has teeth).
  3. Every canonical agent file and docs module has a "## Contents" heading in its first 100 lines.
  4. Every profile has the required keys and a retry budget of 3.

Usage:  python scripts/validate.py
Needs:  pip install -r requirements.txt
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent
HEAD_LINES = 100
CONTENTS_FILES = ["AGENTS.md", "CLAUDE.md", *sorted(str(p.relative_to(ROOT)) for p in (ROOT / "docs").glob("*.md"))]
PROFILE_KEYS = {"profile", "retry_budget_per_node", "nodes", "approved_providers", "audit_trail", "max_data_classification"}
NODES = {"intake", "design", "implementation", "test", "review", "integration", "deploy", "archive"}


def main() -> int:
    errors: list[str] = []
    schema = json.loads((ROOT / "schemas/handoff.schema.json").read_text())
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    for path in sorted((ROOT / "examples").glob("*.json")):
        for err in validator.iter_errors(json.loads(path.read_text())):
            errors.append(f"{path.relative_to(ROOT)}: {err.message}")

    for path in sorted((ROOT / "tests/invalid").glob("*.json")):
        if validator.is_valid(json.loads(path.read_text())):
            errors.append(f"{path.relative_to(ROOT)}: should be rejected by the schema but passed")

    for rel in CONTENTS_FILES:
        head = (ROOT / rel).read_text().splitlines()[:HEAD_LINES]
        if "## Contents" not in head:
            errors.append(f"{rel}: missing '## Contents' in the first {HEAD_LINES} lines")

    for path in sorted((ROOT / "profiles").glob("*.yaml")):
        data = yaml.safe_load(path.read_text())
        missing = PROFILE_KEYS - data.keys()
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: missing keys {sorted(missing)}")
        if data.get("retry_budget_per_node") != 3:
            errors.append(f"{path.relative_to(ROOT)}: retry_budget_per_node must be 3")
        if set(data.get("nodes", {})) != NODES:
            errors.append(f"{path.relative_to(ROOT)}: nodes must be exactly {sorted(NODES)}")

    if errors:
        print("FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("PASS: schema, examples, invalid cases, contents lists, profiles")
    return 0


if __name__ == "__main__":
    sys.exit(main())
