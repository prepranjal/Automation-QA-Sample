from pages.base_page import BasePage
from data.test_data import TestData
from utils.logger_util import LoggerUtil
from utils.assert_util import AssertUtil
from utils.screenshot_util import ScreenshotUtil



class HomePage(BasePage):
    """Page Object for the Wrapstore Home Page."""

    def __init__(self, driver):
        super().__init__(driver)
        self.screenshot_util = ScreenshotUtil(driver)

    def open_home_page(self):
        LoggerUtil.info(f"Opening Wrapstore Home Page: {TestData.BASE_URL}")
        self.driver.get(TestData.BASE_URL)

        # Capture screenshot after page open
        self.screenshot_util.capture_screenshot("homepage_opened")

        # Validate title
        AssertUtil.verify_contains(
            self.get_page_title().lower(),
            "wrapstore",
            "Home page did not open successfully."
        )

        LoggerUtil.info("Home Page opened successfully.")
        self.screenshot_util.capture_screenshot("homepage_title_verified")

    def verify_home_page_loaded(self):
        LoggerUtil.info("Verifying if Home Page is loaded")

        # Verify title contains "wrapstore"
        AssertUtil.verify_contains(
            self.get_page_title().lower(),
            "wrapstore",
            "Home page title verification failed — Page not loaded correctly."
        )

        # Capture after verification
        self.screenshot_util.capture_screenshot("homepage_loaded")

        LoggerUtil.info("Home Page loaded successfully")
