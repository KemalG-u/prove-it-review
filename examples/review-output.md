# Review of the synthetic delivery (example output)

This is what a review that follows `skills/prove-it-review/SKILL.md` looks like for [`sample-delivery/`](sample-delivery/). The delivery is synthetic and contains a deliberate defect; the review text was written to show the format; it is not the output of a live reviewer run. The commands in it are run by `tests/test_examples.py`, so the evidence is checked, but the wording is illustrative.

**Verdict: FIX REQUIRED**

**Scope:** `sample-delivery/fetcher.py`, `sample-delivery/test_fetcher.py` and the three claims in `sample-delivery/agent-report.md`. Not looked at: any other file, because no diff was supplied.

## Claim split

| # | Claim | Label | Evidence |
|---|---|---|---|
| 1 | "On `ConnectionError` it retries up to 3 times, then re-raises" | FALSE | Command: a `fetch_once` that always raises `ConnectionError`, called through `fetch(fetch_once, retries=3)`; counted calls. Output: `attempts: 3`. One first call plus 3 retries should be 4. `fetcher.py:11` loops `range(retries)`, so `retries` is the total number of attempts |
| 2 | "All tests pass" | VERIFIED, but proves nothing about claim 1 | `python -B -m unittest -v` in `sample-delivery/` -> `Ran 1 test ... OK`. The only test (`test_fetcher.py:9`) calls `fetch` once with a function that succeeds. A mutant of `fetch` with the retry loop removed also passes the suite, so the suite cannot detect a retry defect |
| 3 | "No changes outside `fetcher.py`" | UNVERIFIED | No diff or commit was supplied. Skipped: cannot check; ask for `git diff --stat` |

## Findings

1. **High: the retry count is off by one** (claim 1). Evidence above. Suggested fix: loop `1 + retries` times, and add a test that counts calls for `retries=3` (expected 4) and for `retries=0` (expected 1).
2. **Medium: the test suite is blind to the feature it was meant to cover** (claim 2). Evidence above (mutant passes). Suggested fix: the test from finding 1 would fail on the mutant; run the mutant again to confirm.
3. **Medium: `retries=0` makes `fetch` raise `TypeError` even when the call would succeed** (an edge case no claim mentions). Evidence: in `sample-delivery/`, `python -B -c "from fetcher import fetch; fetch(lambda: 'ok', retries=0)"` -> `TypeError: exceptions must derive from BaseException`, raised at `fetcher.py:16` (`raise last_error`) because `range(0)` never runs the loop and `last_error` is still `None`. The same call with `retries=1` returns `ok`. Same root cause as finding 1 (the loop count), different symptom: a crash instead of a wrong count. Suggested fix: the `1 + retries` loop from finding 1 fixes it; add a test for `retries=0` with a function that succeeds (expected: its value) and one that fails (expected: the original `ConnectionError`).

No other findings. Beyond the edge case in finding 3, only `ConnectionError` is retried, which matches the task text ("transient connection errors"); nothing was added to pad the list.

## Skipped checks

- Diff scope (claim 3): no diff supplied.
- Behaviour with real network errors: not run; the function was exercised with a stub only.

## Decision for the orchestrator

Revise: the problem is findings 1 to 3; the evidence is the call count, the surviving mutant and the `retries=0` crash; the scope of the fix is `fetcher.py` and `test_fetcher.py`; keep `fetch`'s signature and its re-raise behaviour. This is correction round 1 of at most 2 before the method changes.
