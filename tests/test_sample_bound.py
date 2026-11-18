# SPDX-License-Identifier: Apache-2.0
"""Tests for skills/prove-it-review/scripts/sample_bound.py. Standard library only: python -m unittest discover -s tests"""
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "skills" / "prove-it-review" / "scripts" / "sample_bound.py"
sys.path.insert(0, str(SCRIPT.parent))
import sample_bound  # noqa: E402


class TestUpperBound(unittest.TestCase):
    def test_reference_values_at_95_percent(self):
        # Independently computed by the AI tool (outside the script): 1 - 0.05 ** (1 / n)
        for n, expected in [(10, 0.2589), (20, 0.1391), (40, 0.0722), (100, 0.0295)]:
            with self.subTest(n=n):
                self.assertAlmostEqual(sample_bound.upper_bound(n), expected, places=4)

    def test_n_equals_one(self):
        self.assertAlmostEqual(sample_bound.upper_bound(1), 0.95, places=12)

    def test_bound_shrinks_as_n_grows(self):
        values = [sample_bound.upper_bound(n) for n in (1, 5, 10, 50, 500)]
        self.assertEqual(values, sorted(values, reverse=True))

    def test_higher_confidence_gives_higher_bound(self):
        self.assertGreater(sample_bound.upper_bound(20, 0.99), sample_bound.upper_bound(20, 0.95))

    def test_rule_of_three_overstates_small_samples(self):
        self.assertGreater(sample_bound.rule_of_three(10), sample_bound.upper_bound(10))
        self.assertLess(abs(sample_bound.rule_of_three(1000) - sample_bound.upper_bound(1000)), 1e-4)

    def test_rule_of_three_is_capped_at_one(self):
        self.assertEqual(sample_bound.rule_of_three(1), 1.0)

    def test_invalid_input_is_rejected(self):
        for bad in (0, -3, 2.5, True, "7"):
            with self.subTest(n=bad), self.assertRaises(ValueError):
                sample_bound.upper_bound(bad)
        for bad in (0, 1, -0.1, 1.5):
            with self.subTest(confidence=bad), self.assertRaises(ValueError):
                sample_bound.upper_bound(10, bad)


class TestFormatting(unittest.TestCase):
    def test_percent_keeps_two_significant_digits(self):
        for fraction, expected in [(0.0722, "7.2%"), (0.2589, "25.9%"), (0.95, "95.0%"), (1.0, "100.0%"),
                                   (0.00030, "0.030%"), (0.00003, "0.0030%"), (3e-9, "0.00000030%")]:
            with self.subTest(fraction=fraction):
                self.assertEqual(sample_bound.format_percent(fraction), expected)

    def test_percent_is_never_a_rounded_zero(self):
        for n in (6000, 10000, 10 ** 6, 10 ** 12):
            with self.subTest(n=n):
                text = sample_bound.format_percent(sample_bound.upper_bound(n))
                self.assertNotEqual(float(text.rstrip("%")), 0.0)

    def test_confidence_label(self):
        for confidence, expected in [(0.95, "95%"), (0.99, "99%"), (0.995, "99.5%"), (0.999, "99.9%"), (0.9, "90%")]:
            with self.subTest(confidence=confidence):
                self.assertEqual(sample_bound.format_confidence(confidence), expected)

    def test_huge_n_stays_positive(self):
        self.assertGreater(sample_bound.upper_bound(10 ** 18), 0.0)


class TestCommandLine(unittest.TestCase):
    def run_cli(self, *args):
        proc = subprocess.run([sys.executable, "-I", str(SCRIPT), *args], capture_output=True)
        return proc.returncode, proc.stdout.decode("utf-8"), proc.stderr.decode("utf-8")

    def test_prints_bound_for_forty(self):
        code, out, _ = self.run_cli("40")
        self.assertEqual(code, 0)
        self.assertIn("7.2%", out)
        self.assertIn("random and independent", out)

    def test_custom_confidence_hides_rule_of_three(self):
        code, out, _ = self.run_cli("10", "--confidence", "0.99")
        self.assertEqual(code, 0)
        self.assertIn("99% upper bound", out)
        self.assertNotIn("3/n", out)

    def test_large_n_does_not_print_a_rounded_zero(self):
        for n in ("6000", "10000", "100000"):
            with self.subTest(n=n):
                code, out, _ = self.run_cli(n)
                self.assertEqual(code, 0)
                self.assertNotRegex(out, r"(?<![\d.])0\.0%")
        _, out, _ = self.run_cli("10000")
        self.assertIn("95% upper bound on the failure rate: 0.030%", out)
        self.assertIn("3/n approximation: 0.030%", out)

    def test_confidence_label_is_not_rounded(self):
        code, out, _ = self.run_cli("40", "--confidence", "0.995")
        self.assertEqual(code, 0)
        self.assertIn("99.5% upper bound", out)
        self.assertNotIn("100%", out)

    def test_zero_is_a_usage_error(self):
        code, _, err = self.run_cli("0")
        self.assertEqual(code, 2)
        self.assertIn("n must be", err)


if __name__ == "__main__":
    unittest.main()
