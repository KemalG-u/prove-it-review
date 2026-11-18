# Privacy and secret check

What was checked before this repository was made public: which tool, which version, which commit, and how many results. Raw scanner output is **not** published. No secret value appears in this file or anywhere in the repository. Counts are copied from tool output.

Check date: 2026-11-18 · Checked tree/commit: `37ebc1b` for the pre-publication scans in sections 2 and 3 (history and working tree; this file and a regenerated METRICS.md were committed afterwards and their text was scanned after that, see section 6); the published history was scanned again at `7eebfba` (section 7) · Record: contemporaneous (written right after the runs)

This file is also the single place for statements about the hosted repository (CI, GitHub security settings, independent review). They are in section 7; other files link here instead of repeating them.

## 1. Publication method

| Item | Value |
|---|---|
| History option | Fresh repository with its real development history (17 commits at the checked commit); no squash, no rewrite. The private original files and their earlier history are not published |
| Source repository modified? | No. The private source files (three skill files and one subagent definition) were read only; their SHA-256 prefixes and modification times (skill 2026-11-11, subagent definition 2026-10-17) were recorded before and are unchanged afterwards: `5fdcf95030a3eb01`, `dd30d3eea044c79a`, `d4b2f1ebd9d2ef73`, `bd5352dbd8a1e316` |
| Commit identity (name, e-mail domain) in published history | Maintainer's public name; e-mail domain `users.noreply.github.com` only (a GitHub noreply address supplied by the maintainer; not re-checked against the GitHub API) |
| Files excluded from export | 0. Nothing was exported: all files were written new in this repository. The owner's exclusion list was applied (no listed path was opened or copied) |

## 2. Secret scanning (full history and working tree)

| Tool | Version | Scope (commit) | Commits scanned | Findings | Real / uncertain | Placeholder / test data |
|---|---|---|---|---|---|---|
| Betterleaks (git mode, `--redact=100`, validation off) | 1.10.1 | history @ `37ebc1b` | 17 (counted with `git rev-list`; the tool reports ~88,300 bytes) | 0 | 0 / 0 | 0 |
| Betterleaks (dir mode, `--redact=100`, validation off) | 1.10.1 | working tree @ `37ebc1b` | not applicable (tree) | 0 | 0 / 0 | 0 |
| TruffleHog (`--no-verification --no-update`, git mode) | 3.99.9 | history @ `37ebc1b` | 17 (54 chunks, 95,018 bytes) | 0 (0 verified, 0 unverified) | 0 / 0 | 0 |
| TruffleHog (`--no-verification --no-update`, filesystem mode) | 3.99.9 | working tree @ `37ebc1b` | not applicable (tree) | 0 (0 verified, 0 unverified) | 0 / 0 | 0 |

Positive control: a scratch repository outside this repository with one commit containing a randomly generated GitHub-token-shaped string. Betterleaks reported 1 finding in git mode and 1 in dir mode; TruffleHog reported 1 unverified finding in git mode (detector `Github`) and 2 in filesystem mode (the filesystem scan also reads the control repository's `.git` data). Both scanners therefore work on this machine with these flags. The control value was generated at run time and never printed or stored in this repository; the scratch repository is outside this repository and holds only that generated value.
Findings handling: no findings, so nothing to classify, revoke or clean.

## 3. Personal data, local paths and agent-specific leaks

Tool: a private standard-files and path checker (the maintainer's own script, not published) with 7 extra terms (the terms themselves are not listed here), plus `git grep` for drive-letter paths, `/home` and `/Users` paths, the private-setup folder names and e-mail addresses.

| Check | Count |
|---|---|
| Local absolute paths (Windows and Unix user-profile paths) | 0 (the private checker and `git grep`) |
| E-mail addresses (excluding harmless domains) | 0 |
| Personal terms | 21 hits at `37ebc1b`, all classified below; 0 are an unwanted leak |
| `*.jsonl` (raw agent or conversation logs) | 0 |
| Secret-like file names | 0 |
| Agent files with local content (`CLAUDE.md`, `AGENTS.md`, memory notes) | 0 reviewed (none exist). The skill and subagent definition were read manually (not by a scanner) for personal rules, tool names, paths and incident records |
| Commit author/committer e-mail domains | `users.noreply.github.com` only (34 fields over 17 commits, at `37ebc1b`) |
| Exclusion list of the owner applied | yes (list of 2026-11-18) |

Classification of the 21 term hits at `37ebc1b` (18 lines contain `kemal`, 3 contain `karinca`): 3 lines carry the maintainer's name and brand in the copyright line (`NOTICE`, twice) and in the AI-use header (intentional; the same lines hold the 3 `karinca` hits); 4 carry the maintainer's GitHub user name in repository URLs (intentional); 11 contain only the marker `KEMAL-VERIFY` (in `docs/AI-USE.md` and the decision records), which stood for facts only the maintainer could give; these placeholders were resolved before release (the AI-use header line held a twelfth marker). Files added after `37ebc1b` (this file, METRICS.md) contain the same kinds of hits. The `git grep` check for non-ASCII letters found only the brand spelling in `NOTICE` and `docs/AI-USE.md`.

`docs/METRICS.md` is generated by a private helper script whose commit-classification patterns include Turkish words (the author's other projects use Turkish commit messages); that file is script output and is not edited by hand.

## 4. Legal and naming checks

| Check | Result | Evidence / date |
|---|---|---|
| Name and trademark conflict search (search engine, GitHub, package registries) | **Renamed after a first search.** The first candidate name, `adversarial-review`, was crowded: on 2026-11-18 the GitHub name search returned 15 repositories with that name under other owners (the first page; more may exist), several of them also Claude Code skills or plugins for adversarial review, and an npm package and PyPI projects with that name exist. On the same day the maintainer chose `prove-it-review` instead (the maintainer's decision, given in the conversation of 2026-11-18). Search for the new name, run read-only on 2026-11-18 before publication: GitHub repository name search 0 results; `KemalG-u/prove-it-review` did not exist at the time of the search (API: 404), so there was no technical conflict; the repository was published under that name on 2026-11-18 (`main` at `7eebfba`), so the name is now taken by this project; npm: `prove-it-review` not found (404); PyPI: `prove-it-review` and `prove_it_review` not found (404). This project does not publish to any registry. No trademark database was searched, and a search engine was not used for the new name. `Interpretation:` no conflict was found in the places searched; absence of results is not proof of absence of a conflict. Not a legal opinion | 2026-11-18; queries: `gh search repos prove-it-review --match name`, `gh api repos/KemalG-u/prove-it-review`, `npm view prove-it-review`, PyPI JSON API for both spellings |
| Dependency license inventory (dependency graph / SBOM export) compatible with Apache-2.0 | None needed: the code imports only the Python standard library (see `git grep -n -e '^import' -e '^from' -- '*.py'`; the project's own modules are the only non-standard imports). CI uses GitHub actions pinned by SHA (see `.github/workflows/ci.yml`), which are not bundled. The GitHub dependency graph export after publication is listed in section 7 | 2026-11-18 |
| Employer IP: no employer or client code or data in this project | The maintainer answered "yes" on 2026-11-18 when asked whether this is a personal project with no employer or client code, data or work time used. This row records the maintainer's answer given in conversation, relayed by the AI tool; it is the maintainer's statement, and the AI tool cannot attest it | maintainer's answer, 2026-11-18 (conversation) |
| Encryption code (export note) | none: the project contains no cryptographic code (a text skill, one arithmetic script, tests) | 2026-11-18 |

## 5. Independent second reading

A fresh-context reviewer reads the candidate commit adversarially; it is an additional AI read, not a human sign-off. The result and the commit it covered are recorded in section 7.

## 6. Limits

`Interpretation:` Scanners can miss secrets and can flag placeholders. A clean result lowers risk; it does not prove absence. The scanners ran locally; no operating-system level network isolation was set up, but both were started with their verification and update features switched off. The positive control used one token shape; it shows the scanners work, not that every secret type is found. This file itself was written after the history scans; a Betterleaks dir-mode scan and a TruffleHog filesystem scan of the working tree were run after it was added, and their counts are in section 7.

## 7. State at publication

Read from GitHub and from the scanners on 2026-11-18, after the repository was published (`main` at `7eebfbac0899d6140d680d11860dded315661bde`).

| Item | State |
|---|---|
| Independent second reading (section 5) | passed at `7eebfbac0899d6140d680d11860dded315661bde`: a delta read on top of the full read that passed at `aabc3e1`; both by an independent AI reviewer (Claude), not a human sign-off |
| CI (`.github/workflows/ci.yml`): first run on the public repository | success on `7eebfba`: https://github.com/KemalG-u/prove-it-review/actions/runs/44356457748 . The action SHAs in the workflow were resolved again on 2026-11-18 with `git ls-remote` for the pinned tags (checkout v7.0.1, setup-python v7.1.0) and did not change |
| GitHub secret scanning, push protection, private vulnerability reporting, Dependabot alerts | enabled (read back from the GitHub API on 2026-11-18; Dependabot alerts: API status 204). Dependabot security updates: disabled. Dependabot version updates for the actions are configured in `.github/dependabot.yml` |
| GitHub dependency graph SBOM export | export available; the dependency graph lists 3 packages. This row records only that the export is available and its package count |
| Secret scans re-run on the published history | at `7eebfba`: Betterleaks 1.10.1 git mode, no leaks found; TruffleHog 3.99.9 git mode, 0 findings |
| `CHANGELOG.md` | generated for the tag `v0.1.0` with git-cliff 2.14.2 (`git cliff --tag v0.1.0 --output CHANGELOG.md`) and regenerated after publication; two runs gave identical files |
| Scans after this file and the regenerated METRICS.md were added | done at `825b552` (19 commits): Betterleaks git and dir mode 0 findings; TruffleHog git mode 0 (62 chunks, 105,219 bytes) and filesystem mode 0 (167 chunks, 272,370 bytes), 0 verified, 0 unverified; the private checker in its strict mode exit code 0 with 0 missing standard files; with the 7 terms, 25 term hits of the same kinds as in section 3 (name and brand, GitHub user name, and the placeholder marker, resolved before release). The text of this row was added after these scans |
