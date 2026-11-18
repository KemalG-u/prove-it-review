# Delivery report (synthetic)

Task: make `fetch()` in `fetcher.py` retry transient connection errors up to 3 times.

Report from the implementing agent:

1. Added retry logic to `fetch()`: on `ConnectionError` it retries up to 3 times, then re-raises.
2. All tests pass.
3. No changes outside `fetcher.py`.
