# in/wrapstore/automation/utils/retry_util.py

import functools
import time


class RetryUtil:
    """Retry mechanism similar to TestNG's IRetryAnalyzer."""

    @staticmethod
    def retry(max_try: int = 2, delay_seconds: float = 0.0):
        """
        Decorator to retry a function if it fails.
        Usage:
            @RetryUtil.retry(max_try=2)
            def test_step(): ...
        """
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                attempt = 0
                while attempt < max_try:
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        attempt += 1
                        if attempt >= max_try:
                            raise
                        if delay_seconds:
                            time.sleep(delay_seconds)
            return wrapper
        return decorator
