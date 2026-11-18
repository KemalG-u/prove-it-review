# AI use in prove-it-review

This is the maintainer's own statement of how AI tools were used to build this project, what the human did, and what was verified. Raw agent transcripts (`*.jsonl`) are **not** published: they can contain private paths, personal data and secrets. This record is a curated summary; its claims point to commits, tests and files you can inspect.

Maintainer: Kemal (KarıncaAI) · Record: reconstructed on 2026-11-18 (drafted by the AI tool that did the extraction). The maintainer's answers given in conversation on 2026-11-18 are recorded below where marked; he has not yet read and confirmed the whole record (KEMAL-VERIFY: confirmation of the whole record and its date pending) · Last reviewed at commit: KEMAL-VERIFY (set when the maintainer has read this file)

## Summary

The text, code, tests and documents in this repository were written by an AI coding agent (Claude Code) working from instructions of the maintainer. The project is a generalised extraction of a skill and a subagent definition that began in the maintainer's own private agent setup. Summary of the maintainer's answer of 2026-11-18 (a paraphrase, not a verbatim quote): he directed the work and the AI wrote it. He set the rule and the idea behind the skill (look at the work adversarially and demand proof); the text of the original skill and subagent definition was written by Claude Code or Codex under his direction. Which of the two tools wrote which file, and with which model, is not recorded.

## Tools and models

| Tool / model (version) | Role | Which parts of the project |
|---|---|---|
| Claude Code, delegated sub-agents on Claude Sonnet 5.5 (the model name comes from the session's own system information) | Did the extraction: generalised the skill and the subagent definition, wrote the script, tests, example, README and all documents; ran tests, scanners and checks; also wrote every fix commit made after the independent AI reads below | All code, documents and fixes in the commits of this repository |
| Claude Code, main session that delegated the tasks, on Claude Opus 5.5 (as stated by that session) | Gave the sub-agents their tasks, constraints and acceptance criteria on behalf of the maintainer, and checked their results | Task definition and checking only; it did not write files here |
| Claude Code, independent AI readers (fresh-context agents on Claude Opus 5.5) | Read the repository against its own claims and reported findings; each reader returned a findings report only and wrote no file. Three reads, on the trees at `860f7b9`, `d31fdd6` and `29eeb2b`; each found problems that were then fixed by the sub-agents above | Nothing written; findings only |
| The private original (file times: skill 2026-11-11, subagent definition 2026-10-17) | The source that was generalised. Not published. Written by Claude Code or Codex under the maintainer's direction (his statement of 2026-11-18); which tool and model wrote which file is not recorded | Origin of `skills/prove-it-review/SKILL.md` and `agents/prove-it-reviewer.md` |
| git-cliff, Betterleaks, TruffleHog (versions in [PRIVACY-CHECK.md](PRIVACY-CHECK.md) and [PROCESS.md](PROCESS.md)) | Changelog generation and secret scanning (tools, not AI) | `CHANGELOG.md`, [PRIVACY-CHECK.md](PRIVACY-CHECK.md) |

## What the human did

- Decided: that this skill is published, under Apache-2.0 with the copyright line in `NOTICE` (a standing publication decision of 2026-11-18). The three design decisions in [decisions/](decisions/) were drafted by the AI tool and are marked `proposed` until the maintainer confirms them. KEMAL-VERIFY: which of them you confirm, and which other decisions were yours.
- Decided, by his own statement of 2026-11-18: the rule and the idea behind the skill (paraphrase: look at the work adversarially and demand proof), and the name `prove-it-review`, chosen after the name search showed the first candidate name to be crowded ([PRIVACY-CHECK.md](PRIVACY-CHECK.md) section 4).
- Stated, 2026-11-18: this is a personal project; no employer or client code, data or work time was used (his answer "yes"; recorded in [PRIVACY-CHECK.md](PRIVACY-CHECK.md) section 4).
- Reviewed: the maintainer looked at every change and works by checking them; he wrote no code, and all code and documents were written by AI tools (maintainer's statement, 2026-11-18). KEMAL-VERIFY: which files he read and how closely.
- Ran and checked: the maintainer works by checking the changes (statement above). Whether he ran the tests himself is not stated: KEMAL-VERIFY. The tests, the scans and the example were run by the AI tool (see below).
- Accepted or rejected: not yet confirmed by the maintainer, apart from the rename above. KEMAL-VERIFY: any AI output you rejected or changed. One correction made inside the extraction, by the AI tool on re-reading its own draft, is in the [devlog](devlog/2026-11-18-three-over-n-is-not-the-bound.md).

## What the AI did

- Read the private original and listed what was specific to the maintainer's setup: personal quotations and rule names, a file layout, a language, a model pin, references to other private skills and policies, dated incident records.
- Rewrote the skill in English as host-neutral text and wrote the host notes for Claude Code and Codex from their online documentation (checked on 2026-11-18).
- Wrote `skills/prove-it-review/scripts/sample_bound.py` because the original quoted a formula without any script, and tests for it.
- Wrote a synthetic worked example (a retry wrapper with a deliberate defect, a report and a review) and tests that run the commands the review cites.
- Wrote the README, contributing guide, security policy, decisions, devlog entries, this file and the process overview.
- Ran the tests, the standard-files checker, the secret scanners and the metrics script.

## What was verified, and how

| Claim | Verification | Evidence |
|---|---|---|
| The unit tests pass | Run by the AI tool with `python -B -m unittest discover -s tests` on Windows, Python 3.12. CI (Linux, Python 3.12) is configured but its first run is recorded only after publication | [METRICS.md](METRICS.md); state of CI in [PRIVACY-CHECK.md](PRIVACY-CHECK.md) section 7 |
| The sample-bound numbers in the skill are right | A test compares the numbers quoted in the skill with the script; the formula values for n = 10, 20, 40 and 100 were also computed independently by the AI tool | `tests/test_examples.py::TestShippedFiles::test_skill_numbers_match_the_script`, `tests/test_sample_bound.py` |
| The worked example's review is true | A test runs the cited commands and checks the cited line numbers | `tests/test_examples.py::TestWorkedExample` |
| No secrets or personal data in the tree and history | Betterleaks, TruffleHog, and a script for local paths and e-mail addresses | [PRIVACY-CHECK.md](PRIVACY-CHECK.md) |
| README example works | `python3 skills/prove-it-review/scripts/sample_bound.py 40` run by the AI tool | [PROCESS.md](PROCESS.md) "Verification" |

## What was not verified

- That the skill makes agents review better. Nothing here measures review quality; the tests check the script, the example and the file structure only.
- The skill was **not** loaded in a live Codex session, and the subagent definition was not run as a subagent in a live Claude Code session by the author of this extraction: only the documented file formats and locations were checked.
- The excuses table is distilled from the maintainer's own use of agents. The incidents behind it are not published and cannot be checked from this repository.
- Behaviour on macOS, on Linux outside CI and on Python versions other than 3.12 was not tested locally.
- The maintainer states that he looked at every change and works by checking them; he has not stated that he read the text and code line by line, so this record does not claim a line-by-line human review. KEMAL-VERIFY.

## Authorship in commits

AI involvement is marked with an `Assisted-by: Claude Code` trailer in commits ([convention from the LLVM policy](https://llvm.org/docs/AIToolPolicy.html)). The model is not named in the trailer; it is named in the table above. `Signed-off-by` appears only for the human maintainer; AI tools never sign off ([Linux kernel guidance](https://docs.kernel.org/process/coding-assistants.html)); the commits here carry none. The history in this repository is the real development history of the extraction (several commits), not a squash; the earlier private history of the original is not published.

## Copyright note

Copyright rests on human creative contribution. The maintainer's statement of 2026-11-18 (conversation): his contribution is the idea and the rule, and the direction of the work (summary of his answer, not a verbatim quote: he directed, the AI wrote); the text was written by AI tools (Claude Code, Codex) under his direction, and nothing here is claimed as human-written. `Interpretation:` Purely machine-generated passages may not be protected; this project does not claim otherwise.

## Limits of this record

`Interpretation:` The share of AI-written text is not measured. Readers cannot verify the tool and model list independently because the raw transcripts are not published. This document is not a quality guarantee; the tests and the files are the evidence.
