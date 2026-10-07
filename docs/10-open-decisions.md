# 10 — Decided vs. Open

## Contents

1. Decided
2. Proposed (not yet ratified)
3. Open questions

## 1. Decided

- SDLC-shaped DAG of black-box agent nodes; no agent-to-agent conversation.
- Nodes communicate only through a constrained status-plus-evidence handoff.
- Agents do their job without asking questions; blocking is a structured output.
- Three attempts per node, then escalate to a human with the full trail.
- Degree of freedom per agent or task: `low`, `medium`, `high`.
- Worktrees and feature branches; a dedicated Integration node owns merging.
- Merge and Deploy exist as nodes; gated per profile.
- Two profiles: `home-lab` (autonomous) and `company` (two human reviewers before merge).
- Public git repo is the source of truth, Apache-2.0; Google Drive holds a thin pointer.
- Usable at a HIPAA-regulated company.
- Repo-shaped, modular files; `AGENTS.md` canonical with non-symlink pointers.
- Contents list at the top of every canonical agent file.

## 2. Proposed (not yet ratified)

- Exact node list and order in `docs/02-pipeline.md` (eight nodes including Deploy and Archive).
- Status code names in `docs/03-handoff-contract.md`.
- Handoff field list and `schemas/handoff.schema.json`.
- Level definitions in `docs/05-degree-of-freedom.md`.
- Merge-queue ordering (oldest ready first).

## 3. Open questions

1. Should **Review** split into a quality node and a separate security/HIPAA node?
2. What must the company profile's approval record contain (who, when, against which evidence)?
3. Gate model between nodes (security gates vs. human gates) — parked for a later session.
4. Staleness window for inactive PRs, per profile.
