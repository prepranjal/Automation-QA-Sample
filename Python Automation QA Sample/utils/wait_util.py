# in/wrapstore/automation/utils/wait_util.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtil:
    """Utility class for explicit waits."""

    @staticmethod
    def wait_for_visibility(driver, locator: tuple, timeout: int):
        """Waits until the element located by the given locator is visible."""
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def wait_for_clickability(driver, locator: tuple, timeout: int):
        """Waits until the element is clickable."""
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @staticmethod
    def wait_for_title_contains(driver, title_substring: str, timeout: int):
        """Waits until the page title contains the given substring."""
        WebDriverWait(driver, timeout).until(
            EC.title_contains(title_substring)
        )
