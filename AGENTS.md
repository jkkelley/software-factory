# AGENTS.md — Software Factory

> **Canonical agent instructions.** This file is the single source of truth for every
> agent (Claude, Codex, or whatever comes next). Tool-specific files such as `CLAUDE.md`
> only point here. If anything elsewhere conflicts with this file, this file wins.

## Contents

1. [What this repo is](#1-what-this-repo-is)
2. [Non-negotiable rules](#2-non-negotiable-rules)
3. [Repository map](#3-repository-map) — where every piece lives
4. [How to work a node](#4-how-to-work-a-node)
5. [Choosing a profile](#5-choosing-a-profile)
6. [Data handling (HIPAA)](#6-data-handling-hipaa)
7. [Making changes to this repo](#7-making-changes-to-this-repo)
8. [Status of this document](#8-status-of-this-document)

Read the Contents first. Each section below is short; detailed rules live in `docs/`
and are linked from the [Repository map](#3-repository-map). Load only what your task needs.

---

## 1. What this repo is

The **Software Factory** is a generic, agentic software-delivery workflow. Work moves
through a **DAG of SDLC-shaped nodes**. Each node is run by an agent that is a
**black box**: it receives a fully specified input, does its job, and emits a
structured handoff. Agents never talk to each other.

It is designed to run unchanged in two places: a personal home lab and a
HIPAA-regulated company. The pipeline is identical; only the **profile** differs.

## 2. Non-negotiable rules

1. **No agent-to-agent conversation.** Nodes communicate only through the
   handoff contract (`schemas/handoff.schema.json`). See `docs/03-handoff-contract.md`.
2. **Do your job. Do not ask questions.** If the input is complete, execute it exactly.
   If something blocks you, emit status `BLOCKED` with evidence — never a free-form question.
3. **Every claim carries evidence.** `FAILED` and `BLOCKED` require reproduction steps,
   the command run, and its actual output. A handoff without evidence is invalid.
4. **Three attempts per node.** On the third failed attempt the node escalates to a human
   with the full trail. See `docs/04-retries-and-escalation.md`.
5. **Respect your degree of freedom** (`low`, `medium`, `high`) as set on the task.
   See `docs/05-degree-of-freedom.md`.
6. **Never merge on your own.** Implementation agents end at "PR opened with evidence."
   Only the Integration node merges. See `docs/06-git-and-integration.md`.
7. **No PHI, secrets, or real personal data** anywhere in the repo, handoffs, logs, or
   evidence. See [Data handling](#6-data-handling-hipaa).

## 3. Repository map

| Path | What it holds | Read when |
|---|---|---|
| `docs/01-principles.md` | Design principles behind the factory | First time in the repo |
| `docs/02-pipeline.md` | The nodes, their inputs and outputs | Working any node |
| `docs/03-handoff-contract.md` | Status codes and required evidence | Emitting or reading a handoff |
| `docs/04-retries-and-escalation.md` | Three-attempt budget, escalation trail | A node fails or blocks |
| `docs/05-degree-of-freedom.md` | `low` / `medium` / `high` latitude | Starting any task |
| `docs/06-git-and-integration.md` | Worktrees, branches, PRs, merge queue | Touching git |
| `docs/07-profiles.md` | `home-lab` vs `company` gate policy | Configuring a deployment |
| `docs/08-compliance-hipaa.md` | PHI rules, provider boundary, audit trail | Any regulated deployment |
| `docs/09-agent-file-conventions.md` | AGENTS.md canon, pointer files, contents-list rule | Writing agent-facing files |
| `docs/10-open-decisions.md` | What is decided vs. still open | Before proposing changes |
| `schemas/handoff.schema.json` | Machine-checkable handoff contract | Validating a handoff |
| `profiles/*.yaml` | Profile configuration | Running the pipeline |
| `examples/` | Synthetic example handoffs only | Learning the format |
| `scripts/validate.py` | Repo self-checks (schema, examples, conventions) | Before every commit |

## 4. How to work a node

1. Read your node's section in `docs/02-pipeline.md`.
2. Read the incoming handoff. Validate it against `schemas/handoff.schema.json`.
3. Read `degree_of_freedom` and the active profile.
4. Do the work in your own git worktree on your own branch (`docs/06`).
5. Emit exactly one handoff with one status from the allowed set (`docs/03`).

## 5. Choosing a profile

- `profiles/home-lab.yaml` — autonomous. Integration auto-merges when green; Deploy may run.
- `profiles/company.yaml` — two human reviewer approvals required before merge; Deploy off
  by default. Details: `docs/07-profiles.md`.

## 6. Data handling (HIPAA)

- This repository contains **process, schemas, and synthetic examples only.**
- Never put PHI, credentials, tokens, hostnames of production systems, or employer-specific
  information in files, commits, handoffs, logs, or evidence.
- Send data only to AI providers and tools the deploying organization has approved
  (and, where PHI could be involved, has a BAA with). That list is profile configuration,
  never hard-coded. Full rules: `docs/08-compliance-hipaa.md`.

## 7. Making changes to this repo

- Branch from `main` as `feat/<slug>`, `fix/<slug>`, or `docs/<slug>`.
- Run `python scripts/validate.py` and the secret scan before committing.
- Update `CHANGELOG.md`. Bump the version in `VERSION` using semantic versioning.
- Open a PR using the template. Follow the merge rules of the profile in force.

## 8. Status of this document

Version: see `VERSION`. Status: **v0.1 capture** — records decisions made so far.
Items marked *proposed* in `docs/` are not yet ratified; see `docs/10-open-decisions.md`.
