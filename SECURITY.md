# Security Policy

## Supported versions

| Version | Supported |
|---|---|
| 0.1.x | yes |
| older | no |

## Reporting a vulnerability

Please do **not** open a public issue for a security problem.

Report it privately with GitHub's private vulnerability reporting: open the repository's **Security** tab and choose **Report a vulnerability** (https://github.com/KemalG-u/prove-it-review/security/advisories/new).

Include: affected version, a description, steps to reproduce, and the impact you see. Never include real secrets or personal data in a report; describe where they appear instead.

## What to expect

This is a one-person project maintained on a best-effort basis. The maintainer aims to send an initial response within **14 days** of a report (the threshold the OpenSSF Best Practices "passing" criteria use). A fix date is not promised; the maintainer will tell you what is planned.

## Scope

In scope: the Python scripts and tests in this repository (`scripts/`, `tests/`, `examples/`), for example a way to make them execute unintended code or write outside their working directory; and content in the skill or subagent definition that could lead an agent to take a harmful action (for example an instruction that weakens a safety boundary of the host). Out of scope: the fact that the skill is advice that an agent can ignore, that a reviewer on the same model shares the producer's blind spots, and problems in Claude Code, Codex or other agent hosts themselves (see the README "Limits" section).

## Repository hygiene

The publication of this repository was checked for committed secrets and personal data; the checks and their result counts are in [docs/PRIVACY-CHECK.md](docs/PRIVACY-CHECK.md), including the state of the GitHub security settings. If you find a secret or personal data that was missed, report it through the private channel above.
