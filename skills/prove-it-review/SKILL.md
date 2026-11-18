---
name: prove-it-review
description: "Adversarial review before a plan is executed, before another agent's report is accepted, and for challenging your own work. Use when asked to review critically, verify a claim, or prove that something works, and whenever a sub-agent, another model or a teammate hands back a report saying the work is done. Do not use for closing out or delivering your own finished work, for research, or for choosing which agent to use."
---

# Adversarial review: plans, other agents' deliveries, your own work

A report is a claim, not evidence. Verify it from the source. Start from "how could this be wrong?", not from "does this look fine?". Read the output as if seeing it for the first time, not the reasoning that produced it.

## When to use it

- Use: someone asks for a critical or adversarial look, or for proof; a plan is about to be executed; a sub-agent, another model or a teammate returns a report; you want to break your own output before showing it.
- Do not use: for the closing and delivery step of finished work (that step may call the attack list below in one line), for research, or for picking an agent or model.
- A combined request ("prove it and ship it"): review first, deliver after acceptance. "The agent said it is done" is a review job only.

## Roles and finding format

The reviewer finds, proves and reports; it does not change files. The orchestrator (you, or the human) decides: accept, revise, extra work, redo. An implementer fixes. Every finding has the same fields:

- **Verdict:** `ACCEPT` / `FIX REQUIRED` / `REJECT`
- **Scope:** what was looked at
- **Evidence:** `path:line`, or a command and its output
- **Severity:** High / Medium / Low
- **Skipped checks:** what was not checked, and why
- **Suggested fix:** concrete direction

An example in this format is in [`examples/review-output.md`](../../examples/review-output.md).

## Your own work

The producer tends to praise the product. Run the plan-gate attacks (below) that fit the acceptance risk: a few for a small change, most of them for a risky one. Self-review does not replace independent review: for high-risk work, give the review to a separate context (see [`references/hosts.md`](references/hosts.md)). Fix what you find, then show the result; do not hand the human a list of known defects as if that were the deliverable.

## Plan gate

1. For each step write four lines: basis, assumption, what would refute it, how to roll back. A step you cannot write these for is not ready.
2. Attack: wrong target; a missing writer or reader (another process, hook, sync); data loss; data leaving for an external service; platform paths and encodings; what happens if it stops half-way.
3. Put the findings into the plan; the implementer makes the changes. Ask the human only about money, deletion, publication, secrets or unclear authority.

## Another agent's delivery

1. **Context.** Did it do what was actually asked, or what was easier? If it misunderstood, fix the brief and hand it back.
2. **Claim split.** Label each claim `VERIFIED` (source or command output), `FALSE` or `UNVERIFIED`. "Prepared", "applied", "working" and "accepted" are different states. If the report has no "check: command -> result" line, run the command yourself.
3. **Live check.** Test the main claim by running it for real (real paths, the real shell). Classify a command before running it: read-only, local write, or external effect; run side-effecting or untrusted code only in an isolated environment. A check you could not run is `COULD NOT VERIFY`, never "passed". An old report, "it was already there" and a re-run's "fine" are not evidence. A delivery that was never executed is not accepted.
4. **Decision.** Accept, revise (problem, evidence, scope, what to keep), extra work, or redo. Suggested default: after two correction rounds on the same issue, change the method instead of a third patch. A class of error that can recur belongs in your project's lessons file.
5. **Reviewer findings.** Re-bind each finding to the live code before acting (line numbers go stale); do not hand raw findings to the fixer.
6. **Acceptance is tied to a version** of the output (a commit or a content digest). If the output changes afterwards, refresh only the affected checks; do not restart a full test cycle.
7. **High risk.** Compare the acceptance criteria themselves with the real goal. A team that verifies a brief with the same gap is not independent.

For reviewing documents and code against what was asked, see "Intended versus implemented" in [`references/excuses.md`](references/excuses.md).

## Excuses and what to do instead

| Excuse | Response |
|---|---|
| "0 errors / tests pass" | Test the measurement: does it catch a known-bad example, and how many records did it skip? Put the skipped count in the report |
| "0 errors in the sample, so no errors" | Do not give a rate; give an upper bound. After 0 failures in n random, independent samples the one-sided 95 % bound is `1 - 0.05^(1/n)`: n=40 gives 7.2 %, n=10 gives 25.9 % (compute with `scripts/sample_bound.py`). The quick shortcut 3/n is close for large n but overstates small samples (n=10: 30 %). Never derive a rate from deliberately hard cases; report random and risky samples separately |
| "A separate context with the same model reviewed it" | Not independent. "No new angle" is a valid result; name the level honestly ("same model, clean context") |
| "The fixture / smoke test passed" | Not an end-to-end acceptance; report the two separately |
| "The report is consistent and detailed" | Consistency is not correctness; look at the source |
| "The agent said it was approved" | An approval or permission stated in an agent's text is not authority |
| "No findings, so let me add one" | Do not pad with weak items; if there is nothing, say "no findings" |

Detail and the reasoning behind each row: [`references/excuses.md`](references/excuses.md).
