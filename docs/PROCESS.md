# How prove-it-review was developed

> Short overview only. Facts (dates, counts) come from git history and scripts and name their source. Opinions are labelled `Interpretation:`. Details of individual problems live in [devlog/](devlog/). This record was RECONSTRUCTED on 2026-11-18 from the git history and the working session of the extraction.

## Stages

| # | Stage | Dates | Goal | Outcome | Evidence |
|---|---|---|---|---|---|
| 1 | Make the numbers checkable | 2026-11-18 | The private original quoted a formula ("0 errors in n samples") without any script | `skills/prove-it-review/scripts/sample_bound.py` with tests | `713a106`, `4037e06` |
| 2 | Generalise the skill and the subagent | 2026-11-18 | Remove personal rules, paths and incident records; write English, host-neutral text | `skills/`, `agents/`, host notes; decisions recorded | `f7831c3`, `f12bf8f`, `a12c257`, [decision 0001](decisions/0001-host-neutral-skill-with-optional-subagent.md), [0002](decisions/0002-excuses-as-reasoning-not-incident-records.md), [0003](decisions/0003-reviewer-model-left-unset.md) |
| 3 | A worked example that is tested | 2026-11-18 | Show the finding format on a delivery with a known defect, with commands that the tests run | `examples/`, `tests/test_examples.py` | `7456599`, `95358e2`, [devlog](devlog/2026-11-18-padded-finding-in-the-example.md) |
| 4 | Documents and checks | 2026-11-18 | README, contribution and security policy, CI, decisions, devlog, AI-use, changelog, process overview, metrics | Standard files complete | `921d9b3`, `587f281`, `ca68e34`, `f81a0fd`, `6141d5e`, `ddc6be6`, `6ad60f7`, `b7a0c3b`, `37ebc1b` |
| 5 | Privacy and secret check | 2026-11-18 | Scan history and tree with two secret scanners, check paths and personal terms, record the result | [PRIVACY-CHECK.md](PRIVACY-CHECK.md) with tool versions and counts; metrics regenerated | `56007ef`, `825b552`, `2b90111`, `8ee0c14` |
| 6 | Rename after the name search | 2026-11-18 | The first name `adversarial-review` was crowded on GitHub, npm and PyPI; the maintainer chose `prove-it-review` | Tree renamed; maintainer's answers recorded in AI-USE; metrics regenerated | `cc3753b`, `c4c1957`, `860f7b9` |
| 7 | Fixes after an independent read | 2026-11-18 | A reader with a clean context checked the repository against its own claims and reported findings | Large-n output of the calculator, skill folder made self-contained, changelog regenerated, AI-use wording, a missed edge case in the example, generic tool names | `fa6cb02`, `f1a2011`, `db5585f`, `2f73d36`, `7d099be`, `d7a4b47` and the commits after them in `git log` |

Stage boundaries are a judgement, not derived from gaps in activity: the whole extraction happened in one working session on a single day. `Interpretation:` The stages follow the order in which the artefacts were produced.

## Timeline

Dates are author dates from the git history of this repository. Commits were created in logical groups as the files were written, so the commit times (17:02 to 19:21 on 2026-11-18 for the commits listed below, UTC+3, local time of the author's machine; later commits of the review round are in `git log`) show when the groups were committed, not an independent record of effort.

| Date | Event | Evidence |
|---|---|---|
| 2026-11-18 | Scaffolding: license, notice, conduct policy, issue forms | commit `3fc61f1` |
| 2026-11-18 | Sample bound calculator and its tests | commits `713a106`, `4037e06` |
| 2026-11-18 | Skill, subagent definition, host notes | commits `f7831c3`, `f12bf8f`, `a12c257` |
| 2026-11-18 | Worked example and the tests that run it | commits `7456599`, `95358e2` |
| 2026-11-18 | README, contributing guide, security policy; CI, Dependabot, templates | commits `921d9b3`, `587f281` |
| 2026-11-18 | Skill text corrected: the 3/n shortcut was quoted as if it were the exact bound | commit `ca68e34`, [devlog](devlog/2026-11-18-three-over-n-is-not-the-bound.md) |
| 2026-11-18 | Decisions, devlog entries, AI-use statement, changelog | commits `f81a0fd`, `6141d5e`, `ddc6be6`, `6ad60f7` |
| 2026-11-18 | Process overview and first generated metrics | commits `b7a0c3b`, `37ebc1b` |
| 2026-11-18 | Privacy and secret check, metrics regenerated, final scans recorded, positive-control note corrected | commits `56007ef`, `825b552`, `2b90111`, `8ee0c14` |
| 2026-11-18 | Renamed from `adversarial-review` to `prove-it-review` after the name search; maintainer's answers recorded; metrics regenerated | commits `cc3753b`, `c4c1957`, `860f7b9` |
| 2026-11-18 | Fixes after the independent read: calculator output for large n, self-contained skill folder, changelog regenerated, AI-use wording, example review, generic tool names | commits `fa6cb02`, `f1a2011`, `db5585f`, `2f73d36`, `7d099be`, `d7a4b47`; the rest of the round is in `git log` |

## Where to read more

- Selected problems, each as problem, diagnosis, fix with evidence: [devlog/](devlog/)
- Decisions and rejected options: [decisions/](decisions/)
- Counts (commits, tests): [METRICS.md](METRICS.md), generated by script
- AI use: [AI-USE.md](AI-USE.md)

## Published history

History option: the repository was created fresh for the extraction and its real history (several commits) is the public history; no squash and no history rewrite. The private original skill and subagent definition are not published, and neither is their earlier history. Commit counts and date ranges in [METRICS.md](METRICS.md) were computed from this repository.

## Verification

| What was checked | Command | Result | Date |
|---|---|---|---|
| Tests | `python -B -m unittest discover -s tests` | See [METRICS.md](METRICS.md): all tests run and pass, none skipped (run on Windows, Python 3.12) | 2026-11-18 |
| README example in the repository | `python skills/prove-it-review/scripts/sample_bound.py 40` | Output identical to the block shown in the README (7.2 % bound, 7.5 % shortcut) | 2026-11-18 |
| Clean clone | `git clone` of this repository at `d7a4b47` into an empty folder, then `python -B skills/prove-it-review/scripts/sample_bound.py 40` and `python -B -m unittest discover -s tests` | README output identical; all tests OK (the count is in [METRICS.md](METRICS.md)); commits after `d7a4b47` change documents only | 2026-11-18 |
| Worked example | `python -B -m unittest -v` in `examples/sample-delivery/` | 1 test, OK; the review's other commands are run by `tests/test_examples.py` | 2026-11-18 |
| CHANGELOG | `git cliff --tag v0.1.0 --output CHANGELOG.md` (git-cliff 2.14.2), run twice | The file is generated, not edited by hand; the second run gave an identical file. Compared with `git log --format=%s`: every `feat` and `fix` commit is listed (without the type prefix) and `docs`, `chore`, `ci` and `test` commits are skipped by the `cliff.toml` rules. `cliff.toml` maps the early name `adversarial-review` to `prove-it-review` in commit subjects | 2026-11-18 |
| Secret and privacy scans | see [PRIVACY-CHECK.md](PRIVACY-CHECK.md) | See that file | 2026-11-18 |

## Known limits

- The skill and the subagent definition were not exercised in live Codex and Claude Code sessions by the extraction (see [AI-USE.md](AI-USE.md)).
- Nothing measures whether using the skill improves reviews.
- CI and the state of the GitHub security settings are recorded in [PRIVACY-CHECK.md](PRIVACY-CHECK.md) section 7, the one place for statements about the hosted repository.
- Pending release-day items (CHANGELOG regeneration, CI run, GitHub settings, scans of the published history) are listed once, in [PRIVACY-CHECK.md](PRIVACY-CHECK.md) section 7.
