# 05 — Degree of Freedom

## Contents

1. The dial
2. Levels
3. Where it is set

## 1. The dial

Every task carries an explicit degree of freedom: how much the agent may decide on its own
inside its black box. It tunes behavior; it never overrides the non-negotiable rules.

## 2. Levels

| Level | Agent may | Agent must not |
|---|---|---|
| `low` | Follow the input to the letter | Choose approaches, add scope, or improvise; any gap → `BLOCKED` |
| `medium` | Make routine choices the input implies (naming, small refactors in scope) | Change interfaces, scope, or acceptance criteria |
| `high` | Choose the approach within the stated goal and constraints | Ignore the contract, skip evidence, or merge on its own |

At every level, the agent never asks questions: it either completes the work or blocks
with evidence.

## 3. Where it is set

On each task, in the `degree_of_freedom` field of the incoming handoff. A profile may set
defaults per node (`profiles/*.yaml`); the task value wins if present.
