# Contributing

## Contents

1. Workflow
2. Commit messages
3. Checks

## 1. Workflow

1. Branch from `main`: `feat/<slug>`, `fix/<slug>`, `docs/<slug>`, or `chore/<slug>`.
2. Keep changes small and focused on one topic.
3. Update `CHANGELOG.md` and bump `VERSION` (semantic versioning).
4. Open a pull request using the template.

## 2. Commit messages

Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, `ci:`.

## 3. Checks

```sh
pip install -r requirements.txt pre-commit
pre-commit install
python scripts/validate.py
```
