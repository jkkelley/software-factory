# 06 — Git, Worktrees, and Integration

## Contents

1. The problem this solves
2. Isolation: one worktree per agent
3. Branch naming
4. Where an agent's job ends
5. The Integration node (merge queue)
6. Getting work to the remote

## 1. The problem this solves

Multiple agents on one repository open many PRs that nobody merges. They go stale,
conflict with each other, and the work never reaches the remote. The cause is that no
one owns the merge. The fix is to make merging a node of its own and to serialize it.

## 2. Isolation: one worktree per agent

Each agent works in its own `git worktree` on its own branch. Worktrees share one
repository but give every agent a physically separate checkout, so agents cannot
overwrite each other's files.

```sh
git worktree add ../wt-<work_item_id> -b feat/<work_item_id>-<slug> origin/main
```

## 3. Branch naming

`<type>/<work_item_id>-<slug>` where type is `feat`, `fix`, `docs`, or `chore`.
The `work_item_id` ties every branch to exactly one work item and its handoff trail.

## 4. Where an agent's job ends

The Implementation agent's job ends at **"PR opened, evidence attached."** It does not
merge. Every push goes to the remote immediately; no work lives only on a local disk.

## 5. The Integration node (merge queue)

The Integration node is the only actor that merges. For one PR at a time, in a
deterministic order (oldest ready first):

1. Rebase onto current `main`.
2. Run the full test suite and required checks.
3. Apply the profile's merge gate (automatic, or required human approvals).
4. Merge if green and approved; delete the branch and worktree.
5. Otherwise emit `FAILED`/`BLOCKED` with evidence — one of the node's three attempts.

Serializing merges means every PR merges against an up-to-date `main`, so the backlog
of conflicting, stale PRs cannot form. GitHub's merge queue may implement this step.

## 6. Getting work to the remote

- Push on every commit; open the PR as soon as the branch exists.
- A PR with no activity past the profile's staleness window is flagged to a human.
- Integration cleans up merged branches and worktrees so nothing lingers.
