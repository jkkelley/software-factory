# 04 — Retries and Escalation

## Contents

1. The rule
2. Why per node
3. What escalation delivers

## 1. The rule

Each node has **three attempts** per work item. An attempt ends in `FAILED` or `BLOCKED`
with evidence; the item is routed to whatever must change, then the node tries again.
After the third unsuccessful attempt, the node emits `ESCALATED` and the item stops for a
human. Nothing is retried automatically after escalation.

## 2. Why per node

The budget is per node, not per work item. One hard node cannot consume the budget of
the others, and an escalation always points at exactly one node with its own three
attempts — not a mixture from across the pipeline.

## 3. What escalation delivers

The human receives one record containing all three attempts' handoffs, each with its
command, observed output, expected result, and reproduction steps. The human should be
able to decide without re-running anything to learn what happened.
