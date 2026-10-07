# 02 — The Pipeline (DAG)

## Contents

1. Overview
2. Node reference
3. Rules every node obeys
4. Enabling and disabling nodes

## 1. Overview

```
Intake → Design → Implementation → Test → Review → Integration → Deploy → Archive
```

The flow is a directed acyclic graph. Work only moves forward along edges. A `BLOCKED`
or `FAILED` handoff routes the item **back** to the node that must fix it (a new attempt),
never into a loop the DAG cannot bound. Independent work items run in parallel.

## 2. Node reference

| # | Node | Input | Output (handoff `DONE`) |
|---|---|---|---|
| 1 | **Intake** | Raw request | Fully specified work item with acceptance criteria; no open questions |
| 2 | **Design** | Work item | Approach, interfaces, and plan, consistent with the project's design source of truth |
| 3 | **Implementation** | Design | Code on a feature branch in its own worktree; PR opened with evidence |
| 4 | **Test** | PR | Tests written and run; pass/fail evidence with reproduction steps |
| 5 | **Review** | Tested PR | Lint, static analysis, security and secret scans, PHI checks — all recorded |
| 6 | **Integration** | Reviewed PR | Rebased on current `main`, full suite green, merged (per profile gate) |
| 7 | **Deploy** | Merged commit | Released to the target environment (per profile; may be disabled) |
| 8 | **Archive** | Completed item | Post-mortem, ledger/state updates, artifact lifecycle applied |

## 3. Rules every node obeys

- Communicates only through `schemas/handoff.schema.json` (`docs/03`).
- Has a three-attempt retry budget (`docs/04`).
- Carries an explicit `degree_of_freedom` (`docs/05`).
- Never asks a human or another agent a question; blocks with evidence instead.

## 4. Enabling and disabling nodes

**Integration** (merge) and **Deploy** always exist in the pipeline. Whether they run
automatically, wait for human approval, or are switched off is set by the active profile
(`docs/07-profiles.md`). A disabled node emits `SKIPPED` so the trail stays complete.
