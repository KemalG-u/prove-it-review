---
status: "proposed"
date: 2026-11-18
decision-makers: drafted by Claude Code during the extraction; the maintainer confirms (KEMAL-VERIFY: confirm or change this decision)
consulted: none
---

# Publish the excuses table as reasoning, not as dated incident records

## Context and Problem Statement

In the private original, every row of the excuses table was tied to a dated incident, a private file path or a count from the maintainer's own systems. Published as they are, those claims cannot be checked by a reader, and the paths and names belong to one person's setup. What should the public table say?

## Decision Drivers

* Every claim in the repository should point to something a reader can inspect.
* Private paths, project names and counts must not be published.
* The table is still the most useful part of the skill.

## Considered Options

* Publish the incident records verbatim.
* Keep the rows, drop the incident records, give a one-line reasoning per row labelled as interpretation, and say in the README and AI-USE that the origin is unpublished experience.
* Drop the table.

## Decision Outcome

Chosen option: "keep rows and reasoning, drop incident records", because the responses stand on their reasoning and the honest statement of the origin is cheaper than unverifiable detail.

### Consequences

* Good, because nothing unverifiable is presented as evidence.
* Bad, because the "why" of each row is weaker than a real incident would be.
* Neutral, because one number was kept only where this repository can reproduce it (the sample bound, via `scripts/sample_bound.py`).

### Confirmation

`references/excuses.md` header labels the reasoning column as interpretation and states the origin; `git grep` finds no dated incident or private path.

## More Information

See [devlog 2026-11-18 formula](../devlog/2026-11-18-three-over-n-is-not-the-bound.md) for the one claim that was re-derived instead of dropped.
