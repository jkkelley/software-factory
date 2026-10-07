# Security Policy

## Contents

1. Reporting a vulnerability
2. What must never be committed
3. Repository protections

## 1. Reporting a vulnerability

Report privately through GitHub's "Report a vulnerability" (private security advisories)
on this repository. Do not open a public issue for security problems.

## 2. What must never be committed

PHI, credentials, API keys, tokens, private hostnames, or any real personal or
employer-specific data. Examples and fixtures are synthetic only. A gitleaks scan runs in
pre-commit and CI; if a secret is ever committed, rotate it immediately — removing it
from history is not enough.

## 3. Repository protections

Configure on the hosting side for `main`:

- Require pull requests; no direct pushes.
- Require the `validate` and `secret-scan` checks to pass.
- Require signed commits.
- Require linear history (rebase or squash merges).
- For the company profile, require two approving reviews.
