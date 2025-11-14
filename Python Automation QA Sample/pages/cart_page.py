# in/wrapstore/automation/pages/cart_page.py

from pages.base_page import BasePage
from locators.static_locators import StaticLocators
from utils.wait_util import WaitUtil
from utils.assert_util import AssertUtil
from utils.logger_util import LoggerUtil


class CartPage(BasePage):
    """Page Object for the Wrapstore Cart Page."""

    def click_add_to_cart_and_navigate_to_cart_page(self):
        LoggerUtil.info("Clicking Add to Cart button")

        WaitUtil.wait_for_clickability(self.driver, StaticLocators.ADD_TO_CART_BTN, 10)
        self.click(StaticLocators.ADD_TO_CART_BTN)

        LoggerUtil.info("Waiting for Cart page to load")
        WaitUtil.wait_for_title_contains(self.driver, "Cart", 10)

        actual_title = self.get_page_title()
        LoggerUtil.info(f"Validating Cart page title: {actual_title}")

        AssertUtil.verify_equals(
            actual_title,
            "Cart - Premium Phone Cases - WRAPSTORE",
            "Cart page title validation failed."
        )

        LoggerUtil.info("Successfully navigated to Cart page")
