---
status: "accepted"
date: 2026-11-18
decision-makers: Kemal (maintainer), approved 2026-11-18; drafted by Claude Code during the extraction
consulted: Claude Code subagent documentation (read 2026-11-18)
---

# The reviewer subagent does not pin a model

## Context and Problem Statement

The private reviewer definition pinned a specific large model and a high effort level, which fits one person's model tiers and cost choices. What should the public definition do?

## Decision Drivers

* The skill's own rule: the reviewer is at the producer's level or above.
* Model names and tiers differ between users and change over time.
* Claude Code documents that a subagent without `model` runs on the model of the session that starts it.

## Considered Options

* Pin the strongest model.
* Pin a mid-tier model.
* Leave `model` unset and tell users to set it when the producer was a stronger or different model.

## Decision Outcome

Chosen option: "leave `model` unset", because any pin is wrong for someone, and the default (the session's own model) already satisfies "same level as the producer" in the common case.

### Consequences

* Good, because it works with whatever models a user has.
* Bad, because if the producer was a stronger model than the session, the reviewer is weaker unless the user sets `model:`; the README and `references/hosts.md` say so.
* Bad, because a same-model reviewer is not independent; this is stated in the README limits.

### Confirmation

`tests/test_examples.py::TestShippedFiles::test_agent_definition` asserts that no `model:` line is present.

## More Information

Related: [0001](0001-host-neutral-skill-with-optional-subagent.md). The effort field was left out for the same reason.
