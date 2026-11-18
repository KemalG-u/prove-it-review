# SPDX-License-Identifier: Apache-2.0
"""Synthetic code under review: a retry wrapper that contains a deliberate off-by-one.

This file belongs to the worked example in examples/; it is not part of the tool.
"""


def fetch(fetch_once, retries=3):
    """Call fetch_once(); on failure retry up to `retries` more times, then re-raise."""
    last_error = None
    for _attempt in range(retries):  # deliberate defect: this makes `retries` attempts, not 1 + retries
        try:
            return fetch_once()
        except ConnectionError as err:
            last_error = err
    raise last_error
