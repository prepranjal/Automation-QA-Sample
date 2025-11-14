# in/wrapstore/automation/pages/store_page.py

from pages.base_page import BasePage
from locators.static_locators import StaticLocators
from utils.wait_util import WaitUtil
from utils.assert_util import AssertUtil
from utils.logger_util import LoggerUtil


class StorePage(BasePage):
    """Page Object for the Wrapstore Store Page."""

    def open_store_page(self):
        LoggerUtil.info("Navigating to Store page from Home")

        WaitUtil.wait_for_clickability(self.driver, StaticLocators.STORE_LINK, 10)
        self.click(StaticLocators.STORE_LINK)

        AssertUtil.verify_contains(
            self.get_page_title().lower(),
            "store",
            "Store page did not open successfully."
        )

        LoggerUtil.info("Store page opened successfully")
