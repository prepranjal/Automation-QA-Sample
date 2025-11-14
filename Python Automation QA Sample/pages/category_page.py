# in/wrapstore/automation/pages/category_page.py

from pages.base_page import BasePage
from locators.static_locators import StaticLocators
from utils.wait_util import WaitUtil
from utils.assert_util import AssertUtil
from utils.logger_util import LoggerUtil


class CategoryPage(BasePage):
    """Page Object for the Wrapstore Category Page."""

    def open_armour_glass_category(self):
        LoggerUtil.info("Opening Armour Glass Case category page")

        WaitUtil.wait_for_clickability(self.driver, StaticLocators.CATEGORY_ARMOUR_GLASS, 10)
        self.click(StaticLocators.CATEGORY_ARMOUR_GLASS)

        AssertUtil.verify_contains(
            self.get_page_title().lower(),
            "armour glass",
            "Armour Glass Case category page did not open successfully."
        )

        LoggerUtil.info("Armour Glass Case category page opened successfully")
