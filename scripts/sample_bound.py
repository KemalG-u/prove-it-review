#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Upper bound on a failure rate when a sample shows zero failures.

"I checked n items and found no errors" does not mean the error rate is zero. If the
items were drawn independently and at random, the one-sided upper confidence bound on the
true failure rate p after 0 failures in n trials is the largest p still compatible with
the observation at the chosen confidence:

    (1 - p) ** n = 1 - confidence   =>   p = 1 - (1 - confidence) ** (1 / n)

At 95 % confidence this is about 3 / n (often called the rule of three); the approximation
overstates the bound for small n, so the exact value is printed next to it.

Only valid for random, independent samples and for 0 observed failures. A hand-picked hard
sample does not give a rate. Standard library only.

Usage:
    python3 scripts/sample_bound.py 40
    python3 scripts/sample_bound.py 10 --confidence 0.99
"""
import argparse
import sys


def upper_bound(n, confidence=0.95):
    """Return the one-sided upper confidence bound on the failure rate after 0 failures in n."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be an integer >= 1")
    if not 0 < confidence < 1:
        raise ValueError("confidence must be strictly between 0 and 1")
    return 1.0 - (1.0 - confidence) ** (1.0 / n)


def rule_of_three(n):
    """The 3 / n approximation for 95 % confidence (capped at 1)."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be an integer >= 1")
    return min(1.0, 3.0 / n)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("n", type=int, help="number of independently, randomly sampled items with 0 failures")
    parser.add_argument("--confidence", type=float, default=0.95, help="confidence level (default 0.95)")
    args = parser.parse_args(argv)
    try:
        exact = upper_bound(args.n, args.confidence)
        approx = rule_of_three(args.n)
    except ValueError as err:
        print("error: %s" % err, file=sys.stderr)
        return 2
    print("n = %d, 0 failures observed" % args.n)
    print("%.0f%% upper bound on the failure rate: %.1f%%" % (args.confidence * 100, exact * 100))
    if abs(args.confidence - 0.95) < 1e-12:
        print("3/n approximation: %.1f%%" % (approx * 100))
    print("Valid only if the sample was random and independent; not for hand-picked hard cases.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
