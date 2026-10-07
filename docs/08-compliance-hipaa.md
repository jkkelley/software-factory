# 08 — Compliance (HIPAA-ready)

## Contents

1. Scope
2. No PHI in the factory
3. Provider and tool boundary
4. Audit trail
5. Guardrails enforced in this repo
6. Adopting this at a regulated employer

## 1. Scope

This repository defines process. It does not process health data and makes no claim of
HIPAA compliance on its own; compliance depends on how an organization deploys it. It is
built so that a compliant deployment is the easy path.

## 2. No PHI in the factory

- The repo contains process, schemas, and **synthetic** examples only.
- Handoffs, notes, logs, and evidence never embed PHI or credentials. If evidence would
  contain restricted data, record a reference to where it is stored in an approved system,
  and set `data_classification: restricted` — never the content itself.
- Test fixtures use synthetic data.

## 3. Provider and tool boundary

A node may send data only to AI providers and tools listed in the active profile's
`approved_providers`. In a regulated deployment that list contains only services the
organization has approved, and covered by a Business Associate Agreement wherever PHI
could be involved. The list is configuration, never hard-coded.

## 4. Audit trail

Every handoff is timestamped (UTC), attributed to the node and agent that produced it,
and retained. In the company profile, merges record the two approving reviewers. This
supports HIPAA audit-control expectations (45 CFR 164.312(b)).

## 5. Guardrails enforced in this repo

- Secret scanning with gitleaks in pre-commit and in CI.
- Schema validation of every example handoff in CI.
- Convention checks (contents list at the top of agent files) in CI.
- Branch protection on `main` (configure on the hosting side; see `SECURITY.md`).

## 6. Adopting this at a regulated employer

- Build and maintain the repo on personal time and equipment; keep anything
  employer-specific out of it.
- Review the employer's IP-assignment and open-source policy before contributing or
  adopting; adopt it as an external Apache-2.0 tool through the normal approval process.
- Put organization-specific settings in a private profile inside the organization,
  not in this public repository.
