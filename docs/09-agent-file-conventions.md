# 09 — Agent File Conventions

## Contents

1. AGENTS.md is canonical
2. Tool-specific pointer files
3. Contents list at the top
4. Keep files small

## 1. AGENTS.md is canonical

`AGENTS.md` at the repository root is the single source of truth for agent instructions.
It is the neutral convention read by Codex and other agents. Nothing is duplicated
elsewhere.

## 2. Tool-specific pointer files

Tools that look for their own filename get a thin pointer, not a copy and not a symlink
(symlinks break across Windows, WSL, and some git setups).

| Tool | File | Mechanism |
|---|---|---|
| Codex | `AGENTS.md` | Read natively — no extra file needed |
| Claude Code | `CLAUDE.md` | `@AGENTS.md` import line |
| Others | Their expected filename | One line pointing to `AGENTS.md` |

When a new tool appears, add one pointer file. Never add rules to a pointer.

## 3. Contents list at the top

Every canonical agent-facing file starts with a `## Contents` section within its first
lines. Many agents read only the head of a file (for example the first 100 lines); the
contents list guarantees they see the full map and know what to retrieve.
`scripts/validate.py` enforces this.

## 4. Keep files small

One topic per file. Large topics split into numbered modules. An agent should be able to
load exactly the section it needs without reading the whole repository.
