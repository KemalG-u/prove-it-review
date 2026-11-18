# The "about 3/n" shortcut was quoted next to exact numbers that disagree with it

Date: 2026-11-18 · Record: reconstructed on 2026-11-18 (from this repository's history and the working session; no earlier written note exists)

## Problem

The skill tells reviewers that "0 errors in n samples" is not a rate and gives an upper bound instead. The private original quoted the exact formula `1 - 0.05^(1/n)`, then said "about 3/n", then listed exact values (n=40: 7.2 %, n=10: 25.9 %). The first public draft of `SKILL.md` repeated that wording. For n=10 the shortcut 3/n is 30 %, not 25.9 %, so the sentence pointed a reader at two different numbers for the same quantity.

## Diagnosis

The shortcut (often called the rule of three) is the large-n limit of the formula: it is close for n=100 (both 3.0 % when rounded to one decimal) and overstates for small n. The original text had no script, so nothing compared the shortcut with the formula. Writing `scripts/sample_bound.py` and its tests exposed the difference: `test_rule_of_three_overstates_small_samples` asserts that 3/n is larger than the exact bound at n=10. That test passed on the script, but the skill text written after it still carried the old phrasing; it was found when the skill text was read against the script output before the documents were written.

## Attempts that failed

None recorded. The first draft was simply wrong in wording; it was not tried against a reader.

## Resolution

`SKILL.md` now gives the exact formula and its values first and presents 3/n as a shortcut that "overstates small samples (n=10: 30 %)". A test (`test_skill_numbers_match_the_script`) now checks that the numbers quoted in the skill, including the shortcut value for n=10, equal what the script computes.

## Evidence

- Commits: `713a106` (script), `4037e06` (script tests), `f7831c3` (skill with the loose wording), `ca68e34` (the fix)
- Test: `tests/test_sample_bound.py::TestUpperBound::test_rule_of_three_overstates_small_samples`, `tests/test_examples.py::TestShippedFiles::test_skill_numbers_match_the_script`
- Command: `python3 scripts/sample_bound.py 10` prints the exact bound next to the 3/n approximation
