# 03 — The Handoff Contract

## Contents

1. Purpose
2. Status codes
3. Required fields
4. Evidence requirements by status
5. Validity rule

## 1. Purpose

The handoff is the only thing that crosses from one node to the next. It is a contract,
not a conversation. Machine-checkable form: `schemas/handoff.schema.json`.

## 2. Status codes

Exactly one per handoff. *(Proposed names — see `docs/10-open-decisions.md`.)*

| Status | Meaning |
|---|---|
| `DONE` | Node finished; acceptance criteria met; output attached |
| `FAILED` | Node attempted the work and it does not meet criteria |
| `BLOCKED` | Node cannot proceed because an input or dependency is missing or wrong |
| `AWAITING_APPROVAL` | Work is ready; a profile-required human approval is pending |
| `ESCALATED` | Retry budget exhausted; a human must decide |
| `SKIPPED` | Node disabled by the active profile |

## 3. Required fields

| Field | Description |
|---|---|
| `work_item_id` | Stable ID of the item (also used in branch names) |
| `node` | Which node produced this handoff |
| `attempt` | 1, 2, or 3 |
| `status` | One value from the table above |
| `degree_of_freedom` | `low`, `medium`, or `high` |
| `summary` | One or two plain sentences — no speculation |
| `artifacts` | Branch, commit SHA, PR link, files produced |
| `evidence` | Required for `FAILED`, `BLOCKED`, `ESCALATED` (below) |
| `data_classification` | `public`, `internal`, or `restricted`; `restricted` content is never embedded |
| `produced_at` | UTC timestamp, ISO 8601 |

## 4. Evidence requirements by status

`FAILED`, `BLOCKED`, and `ESCALATED` must include:

- **reason_code** — short machine-readable cause
- **command** — exactly what was run
- **observed** — the actual output (truncated, never paraphrased)
- **expected** — what should have happened
- **reproduce** — ordered steps a different agent can follow to see the same result
- **blocked_on** — (`BLOCKED` only) which upstream node or input must change

`ESCALATED` additionally includes the evidence of all three attempts.

## 5. Validity rule

A handoff that fails schema validation, or that carries `FAILED`/`BLOCKED` without
evidence, is invalid. The edge does not fire and the work does not move.
