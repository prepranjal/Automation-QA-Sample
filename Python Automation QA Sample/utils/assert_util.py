# in/wrapstore/automation/utils/assert_util.py

class AssertUtil:
    """Utility class for soft and hard assertions (TestNG → PyTest equivalent)."""

    @staticmethod
    def verify_contains(actual: str, expected: str, message: str = ""):
        """Verifies that 'expected' substring exists in 'actual'."""
        if expected not in actual:
            raise AssertionError(
                f"{message} | Expected substring '{expected}' not found in '{actual}'"
            )

    @staticmethod
    def verify_equals(actual: str, expected: str, message: str = ""):
        """Verifies that actual equals expected."""
        if actual != expected:
            raise AssertionError(
                f"{message} | Expected: '{expected}' but found: '{actual}'"
            )
