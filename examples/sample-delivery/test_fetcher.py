# SPDX-License-Identifier: Apache-2.0
"""The tests that came with the synthetic delivery. They pass, and none of them exercises a retry."""
import unittest

from fetcher import fetch


class TestFetch(unittest.TestCase):
    def test_returns_value_on_first_success(self):
        self.assertEqual(fetch(lambda: "data"), "data")


if __name__ == "__main__":
    unittest.main()
