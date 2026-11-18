# Using the skill in Claude Code and Codex

## Claude Code

- Skill: copy `skills/prove-it-review/` to `.claude/skills/` (one project) or `~/.claude/skills/` (all projects). It is loaded when your request matches the description, or by name.
- Independent reviewer: copy `agents/prove-it-reviewer.md` to `.claude/agents/` or `~/.claude/agents/`. It is a subagent with read-only intent (tools: Read, Grep, Glob, Bash) that preloads this skill with the `skills:` field. Ask Claude to "use the prove-it-reviewer to review this diff", or let the description match.
- Read-only is the intent of the definition, not a guarantee: the Bash tool can run commands with side effects. Do not hand the reviewer a command that has side effects.
- Choose the reviewer's model deliberately. The shipped definition does not set `model`, so by the Claude Code rules it runs on the model of the session that starts it. If the producer was a cheaper or smaller model, set `model:` in the definition to the same or a stronger one; the reviewer should be at the producer's level or above.
- Brief for a reviewer without the preloaded skill: first line `Read first: <path to SKILL.md>`, then the acceptance criteria and a path list or diff, then "read only, do not change files".

## Codex

- Skill: copy `skills/prove-it-review/` to `.agents/skills/` in your repository, or `~/.agents/skills/` for all projects (the repository and user locations in the Codex skills documentation). Invoke it by name in the prompt (`$prove-it-review` in the CLI or the IDE extension) or let the description match.
- The Claude Code subagent file is not used by Codex. For an independent read, start a separate Codex session with a clean context and give it the acceptance criteria and the diff.
- `Interpretation:` the skill text is host-neutral; it was not loaded in a live Codex session by the author (see [docs/AI-USE.md](https://github.com/KemalG-u/prove-it-review/blob/main/docs/AI-USE.md)).
