# in/wrapstore/automation/pages/product_page.py

from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from data.test_data import TestData
from locators.static_locators import StaticLocators
from utils.logger_util import LoggerUtil
from utils.assert_util import AssertUtil
from utils.wait_util import WaitUtil


class ProductPage(BasePage):
    """Page Object for the Wrapstore Product Page."""

    def open_batman_toon_product(self):
        LoggerUtil.info("Opening Batman Toon Glass Case product")

        WaitUtil.wait_for_clickability(self.driver, StaticLocators.PRODUCT_BATMAN_TOON, 10)
        self.click(StaticLocators.PRODUCT_BATMAN_TOON)

        AssertUtil.verify_contains(
            self.get_page_title().lower(),
            "batman",
            "Batman Toon Glass Case product page did not open successfully."
        )

    def select_batman_toon_phone_model(self):
        LoggerUtil.info(f"Selecting Brand: {TestData.BRAND} and Model: {TestData.MODEL}")

        # --- Select Brand ---
        WaitUtil.wait_for_visibility(self.driver, StaticLocators.DROPDOWN_BRAND, 10)
        brand_dropdown = Select(self.find(StaticLocators.DROPDOWN_BRAND))
        brand_dropdown.select_by_visible_text(TestData.BRAND)

        AssertUtil.verify_equals(
            brand_dropdown.first_selected_option.text,
            TestData.BRAND,
            "Phone brand selection failed."
        )

        # --- Select Model ---
        WaitUtil.wait_for_visibility(self.driver, StaticLocators.DROPDOWN_MODEL, 10)
        model_dropdown = Select(self.find(StaticLocators.DROPDOWN_MODEL))
        model_dropdown.select_by_visible_text(TestData.MODEL)

        AssertUtil.verify_equals(
            model_dropdown.first_selected_option.text,
            TestData.MODEL,
            "Phone model selection failed."
        )

        LoggerUtil.info(f"Successfully selected {TestData.BRAND} → {TestData.MODEL}")

    def add_to_cart(self):
        LoggerUtil.info("Clicking Add to Cart button")
        WaitUtil.wait_for_clickability(self.driver, StaticLocators.ADD_TO_CART_BTN, 10)
        self.click(StaticLocators.ADD_TO_CART_BTN)
