# wrapstore_automation_py/pages/base_page.py

from utils.logger_util import LoggerUtil
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """Base Page class for all page objects."""

    def __init__(self, driver: WebDriver):
        """Accepts WebDriver instance from test fixture."""
        self.driver = driver
        LoggerUtil.info("✅ BasePage initialized with WebDriver instance")

    # ---------- Generic actions ----------

    def click(self, locator: tuple):
        LoggerUtil.info(f"🖱 Clicking element: {locator}")
        self.driver.find_element(*locator).click()

    def type(self, locator: tuple, text: str):
        LoggerUtil.info(f"⌨ Typing into element: {locator} | Text: {text}")
        element: WebElement = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        element: WebElement = self.driver.find_element(*locator)
        text = element.text
        LoggerUtil.info(f"📄 Reading text from element: {locator} | Value: {text}")
        return text

    def find(self, locator: tuple) -> WebElement:
        """Generic find method."""
        LoggerUtil.info(f"🔍 Finding element: {locator}")
        return self.driver.find_element(*locator)

    # ---------- Page info ----------

    def get_page_title(self) -> str:
        title = self.driver.title
        LoggerUtil.info(f"📑 Current Page Title: {title}")
        return title

    def get_current_url(self) -> str:
        url = self.driver.current_url
        LoggerUtil.info(f"🌐 Current URL: {url}")
        return url
