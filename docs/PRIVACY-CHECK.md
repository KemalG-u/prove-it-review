# Privacy and secret check

What was checked before this repository was made public: which tool, which version, which commit, and how many results. Raw scanner output is **not** published. No secret value appears in this file or anywhere in the repository. Counts are copied from tool output.

Check date: 2026-11-18 · Checked tree/commit: `37ebc1b` (history and working tree; this file and a regenerated METRICS.md were committed afterwards and their text was scanned after that, see section 6) · Record: contemporaneous (written right after the runs)

This file is also the single place for statements about the hosted repository (CI, GitHub security settings, independent review). They are in section 7 and are marked pending until the repository is published; other files link here instead of repeating them.

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

Positive control: a scratch repository outside this repository with one commit containing a randomly generated GitHub-token-shaped string. Betterleaks reported 1 finding in git mode and 1 in dir mode; TruffleHog reported 1 unverified finding in git mode (detector `Github`) and 2 in filesystem mode (the filesystem scan also reads the control repository's `.git` data). Both scanners therefore work on this machine with these flags. The control value was generated at run time and never printed or stored in this repository; the scratch repository was deleted afterwards.
Findings handling: no findings, so nothing to classify, revoke or clean.

## 3. Personal data, local paths and agent-specific leaks

Tool: `kontrol.py` 2.0 with 7 extra terms (the terms themselves are not listed here), plus `git grep` for drive-letter paths, `/home` and `/Users` paths, the private-setup folder names and e-mail addresses.

| Check | Count |
|---|---|
| Local absolute paths (Windows and Unix user-profile paths) | 0 (`kontrol.py` and `git grep`) |
| E-mail addresses (excluding harmless domains) | 0 |
| Personal terms | 21 hits at `37ebc1b`, all classified below; 0 are an unwanted leak |
| `*.jsonl` (raw agent or conversation logs) | 0 |
| Secret-like file names | 0 |
| Agent files with local content (`CLAUDE.md`, `AGENTS.md`, memory notes) | 0 reviewed (none exist). The skill and subagent definition were read by hand for personal rules, tool names, paths and incident records |
| Commit author/committer e-mail domains | `users.noreply.github.com` only (34 fields over 17 commits) |
| Exclusion list of the owner applied | yes (list of 2026-11-18) |

Classification of the 21 term hits at `37ebc1b` (18 lines contain `kemal`, 3 contain `karinca`): 3 lines carry the maintainer's name and brand in the copyright line (`NOTICE`, twice) and in the AI-use header (intentional; the same lines hold the 3 `karinca` hits); 4 carry the maintainer's GitHub user name in repository URLs (intentional); 11 contain only the marker `KEMAL-VERIFY` (in `docs/AI-USE.md` and the decision records), which stands for facts only the maintainer can give and disappears when he fills them in (the AI-use header line holds a twelfth marker). Files added after `37ebc1b` (this file, METRICS.md) contain the same kinds of hits. The `git grep` check for non-ASCII letters found only the brand spelling in `NOTICE` and `docs/AI-USE.md`.

## 4. Legal and naming checks

| Check | Result | Evidence / date |
|---|---|---|
| Name and trademark conflict search (search engine, GitHub, package registries) | **Crowded name.** On GitHub repository names are scoped to the owner, and `KemalG-u/adversarial-review` does not exist yet (API: 404), so there is no technical conflict. But the GitHub name search returned 15 repositories named `adversarial-review` under other owners (the first page; more may exist), several of them also Claude Code skills or plugins for adversarial review (for example `dementev-dev/adversarial-review`, "Claude Code skill for adversarial AI code & plan review"). An npm package `adversarial-review` (version 2.11.1) and PyPI projects `adversarial-review` and `adversarial_review` exist; this project does not publish to any registry. No trademark database was searched. `Interpretation:` the name is descriptive and common, so confusion and weak discoverability are likely; a more distinctive name is worth a decision before publication. Not a legal opinion | 2026-11-18; queries: `gh search repos adversarial-review --match name`, `gh api repos/KemalG-u/adversarial-review`, `npm view adversarial-review`, PyPI JSON API for both spellings |
| Dependency license inventory (dependency graph / SBOM export) compatible with Apache-2.0 | None needed: the code imports only the Python standard library (`argparse`, `sys`, `re`, `shutil`, `subprocess`, `tempfile`, `unittest`, `pathlib`), checked by grepping the import lines. CI uses two GitHub actions pinned by SHA (`actions/checkout`, `actions/setup-python`), which are not bundled. The GitHub dependency graph export after publication is listed in section 7 | 2026-11-18 |
| Employer IP: no employer or client code or data in this project | KEMAL-VERIFY: the maintainer confirms that the private original and this extraction contain no code, data or work time owned by an employer or client. (This is the maintainer's statement; the AI tool cannot attest it.) | pending |
| Encryption code (export note) | none: the project contains no cryptographic code (a text skill, one arithmetic script, tests) | 2026-11-18 |

## 5. Independent second reading

A fresh-context reviewer reads the candidate commit adversarially; it is an additional AI read, not a human sign-off. The result and the commit it covered are recorded in section 7 when it has been done.

## 6. Limits

`Interpretation:` Scanners can miss secrets and can flag placeholders. A clean result lowers risk; it does not prove absence. The scanners ran locally; no operating-system level network isolation was set up, but both were started with their verification and update features switched off. The positive control used one token shape; it shows the scanners work, not that every secret type is found. This file itself was written after the history scans; a Betterleaks dir-mode scan and a TruffleHog filesystem scan of the working tree were run after it was added, and their counts are in section 7.

## 7. State at publication (pending until the repository is published)

| Item | State |
|---|---|
| Independent second reading (section 5) | pending |
| CI (`.github/workflows/ci.yml`): first run on the public repository | pending: no run exists; the workflow has not been executed on GitHub. The action SHAs in it were resolved on 2026-11-18 and must be re-resolved on release day |
| GitHub secret scanning, push protection, private vulnerability reporting, Dependabot alerts | pending: to be enabled and read back from the GitHub API when the repository is made public |
| GitHub dependency graph SBOM export (Apache-2.0 compatibility of dependencies) | pending |
| Secret scans re-run on the published history | pending |
| `CHANGELOG.md` | generated for the planned tag `v0.1.0` with git-cliff 2.14.2; regenerate on release day |
| Scans after this file and the regenerated METRICS.md were added | done at `825b552` (19 commits): Betterleaks git and dir mode 0 findings; TruffleHog git mode 0 (62 chunks, 105,219 bytes) and filesystem mode 0 (167 chunks, 272,370 bytes), 0 verified, 0 unverified; `kontrol.py --kati` exit code 0 with 0 missing standard files; with the 7 terms, 25 term hits of the same kinds as in section 3 (name and brand, GitHub user name, `KEMAL-VERIFY` marker). The text of this row was added after these scans |
