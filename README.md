# Software Factory

A generic, agentic software-delivery workflow: an SDLC-shaped DAG of black-box agent
nodes that hand off work through a strict status-and-evidence contract.

```
Intake → Design → Implementation → Test → Review → Integration → Deploy → Archive
```

- **No agent chatter.** Nodes communicate only through a schema-validated handoff.
- **No questions.** Agents do the job or block with reproducible evidence.
- **Three attempts per node,** then a human gets the full trail.
- **Degree of freedom** (`low` / `medium` / `high`) on every task.
- **One merge owner.** Worktrees per agent; a serialized Integration node merges.
- **Two profiles.** `home-lab` runs autonomously; `company` requires two human reviewers
  before merge and keeps Deploy off by default.
- **HIPAA-ready by design.** No PHI in the factory, approved-provider boundary, audit trail.

## Start here

- Agents: read [`AGENTS.md`](AGENTS.md).
- Humans: read [`docs/01-principles.md`](docs/01-principles.md), then [`docs/02-pipeline.md`](docs/02-pipeline.md).

## Validate

```sh
python -m pip install -r requirements.txt
python scripts/validate.py
```

## Status

v0.1 — a captured design. See [`docs/10-open-decisions.md`](docs/10-open-decisions.md)
for what is decided and what is still open.

## License

[Apache License 2.0](LICENSE).
