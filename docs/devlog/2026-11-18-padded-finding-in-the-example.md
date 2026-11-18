# The example review broke the skill's own "do not pad findings" rule

Date: 2026-11-18 · Record: reconstructed on 2026-11-18 (from the working session; the draft was never committed, so the first part is `unverified`)

## Problem

While writing `examples/review-output.md`, the first draft of the findings list ended with a third item, "Low: only `ConnectionError` is retried", whose own text said it was not a finding. The skill's last excuses row says: "No findings, so let me add one: do not pad with weak items; if there is nothing, say 'no findings'". `unverified`: the draft exists only in the working session; no commit contains it.

## Diagnosis

`Interpretation:` The example was written to look complete, and a list of three felt more complete than a list of two. Re-reading the example against the skill's own rules (the exercise the skill asks for: look at the output as if for the first time) showed the contradiction. The same re-read found two wrong line references (`fetcher.py:10`, `test_fetcher.py:12` instead of 11 and 9), which `grep -n` confirmed.

## Attempts that failed

None recorded.

## Resolution

The padded item was removed and replaced by one sentence saying there are no other findings and nothing was added to pad the list. The line references were corrected, and `tests/test_examples.py::TestWorkedExample::test_review_cites_the_lines_it_names` now fails if the cited lines move.

## Follow-up: "no other findings" was itself unverified

An independent read of the repository later the same day found that the sentence added to replace the padded item, "No other findings", was wrong. `fetch(lambda: 'ok', retries=0)` raises `TypeError: exceptions must derive from BaseException` (`fetcher.py:16`) because the loop body never runs. The author had checked the claims in the report and the main defect, but had not tried the boundary value of the parameter the defect concerns. The review now lists it as finding 3 with the command and its output, and `tests/test_examples.py::TestWorkedExample::test_zero_retries_crashes_as_the_review_says` runs that command. `Interpretation:` "no other findings" needs the same evidence as any other claim: say which edge cases were tried.

## Evidence

- Commits: `7456599` (the example as first added), `95358e2` (the test that pins the cited lines), `7d099be` (the `retries=0` finding added to the review)
- Tests: `tests/test_examples.py::TestWorkedExample::test_review_cites_the_lines_it_names`, `tests/test_examples.py::TestWorkedExample::test_zero_retries_crashes_as_the_review_says`
- Rule: the last row of the excuses table in `skills/prove-it-review/SKILL.md`
