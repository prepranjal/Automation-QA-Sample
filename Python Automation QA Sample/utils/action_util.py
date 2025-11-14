# in/wrapstore/automation/utils/action_util.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver


class ActionUtil:
    """Utility class for common WebDriver actions."""

    @staticmethod
    def click(driver: WebDriver, locator: tuple):
        """Clicks on a given element."""
        driver.find_element(*locator).click()

    @staticmethod
    def type(driver: WebDriver, locator: tuple, text: str):
        """Clears and types text into an element."""
        element = driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    @staticmethod
    def select_by_visible_text(driver: WebDriver, locator: tuple, text: str):
        """Selects a dropdown option by visible text."""
        select = Select(driver.find_element(*locator))
        select.select_by_visible_text(text)
