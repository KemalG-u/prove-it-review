---
status: "accepted"
date: 2026-11-18
decision-makers: Kemal (maintainer), approved 2026-11-18; drafted by Claude Code during the extraction
consulted: Claude Code and Codex documentation (read 2026-11-18)
---

# Keep the skill host-neutral and ship the Claude Code subagent as a separate, optional file

## Context and Problem Statement

The private original was a skill plus a Claude Code subagent definition, written for one agent setup. The public project should work for people who use Claude Code, Codex or both. Which parts are shared, and which are host-specific?

## Decision Drivers

* The skill format (a `SKILL.md` with `name` and `description`) is read by both Claude Code and Codex; subagent definitions are not portable between them.
* Host-specific text inside the skill makes it wrong or confusing on the other host.
* A reviewer in a separate context is the main way to get an independent read, so Claude Code users should get a ready definition.

## Considered Options

* One skill file with host-neutral text; host notes in a reference file; the subagent definition separate and optional.
* Two forks of the skill, one per host.
* Only the skill; no subagent definition.

## Decision Outcome

Chosen option: "host-neutral skill, host notes in `references/hosts.md`, optional subagent", because it keeps one source of truth for the procedure and still gives Claude Code users the clean-context reviewer.

### Consequences

* Good, because the procedure is maintained once.
* Bad, because Codex users get no ready reviewer definition; `skills/prove-it-review/references/hosts.md` tells them to start a clean session instead.
* Bad, because the Codex path was only checked against its documentation, not in a live session (see [AI-USE.md](../AI-USE.md)).

### Confirmation

`tests/test_examples.py`, class `TestShippedFiles`: skill and agent frontmatter, link targets and the directory name.

## More Information

Related: [0003](0003-reviewer-model-left-unset.md). The options were proposed by an AI tool.
