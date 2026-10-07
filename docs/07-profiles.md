# 07 — Profiles: Home Lab and Company

## Contents

1. One pipeline, two profiles
2. Comparison
3. Profile files
4. Adding a profile

## 1. One pipeline, two profiles

The nodes are identical everywhere. A **profile** sets the policy that sits on top:
who must approve a merge, whether Deploy runs, which AI providers are allowed, and
default degrees of freedom. Merge and Deploy exist in both profiles; only their gates differ.

## 2. Comparison

| Setting | `home-lab` | `company` |
|---|---|---|
| Integration (merge) | Automatic when green | Requires **two human reviewer approvals** |
| Deploy | Enabled, automatic | Disabled by default; human-gated when enabled |
| Integration freedom | `high` | `low` |
| Approved AI providers | Owner's choice | Organization-approved list only (BAA where PHI possible) |
| Audit trail | Recommended | Required |
| Data classification ceiling | `internal` | `internal` — `restricted` is never embedded |

In the company profile, agents do everything up to the merge — branch, PR, evidence,
all checks green — then emit `AWAITING_APPROVAL` and stop until the approvals exist.

## 3. Profile files

- `profiles/home-lab.yaml`
- `profiles/company.yaml`

## 4. Adding a profile

Copy the closest profile, change only policy values, and document it here. Never fork
the pipeline to get different behavior.
