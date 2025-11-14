# in/wrapstore_automation_py/tests/test_add_to_cart_flow.py

import pytest
from pages.home_page import HomePage
from pages.store_page import StorePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.logger_util import LoggerUtil


@pytest.mark.regression
@pytest.mark.usefixtures("setup_and_teardown")
class TestAddToCartFlow:
    """
    PyTest equivalent of Behave Scenario:
    'User adds Batman Toon Armour Glass Case to cart'
    """

    def test_add_batman_toon_case_to_cart(self):
        LoggerUtil.info("===== TEST START: Add Batman Toon Armour Glass Case to Cart =====")

        # Initialize Page Objects
        home_page = HomePage(self.driver)
        store_page = StorePage(self.driver)
        category_page = CategoryPage(self.driver)
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)

        # Step 1: Open Home Page
        home_page.open_home_page()
        home_page.verify_home_page_loaded()

        # Step 2: Navigate to Store Page
        store_page.open_store_page()

        # Step 3: Open Armour Glass Category
        category_page.open_armour_glass_category()

        # Step 4: Open Product and Select Model
        product_page.open_batman_toon_product()
        product_page.select_batman_toon_phone_model()

        # Step 5: Add to Cart and Validate
        cart_page.click_add_to_cart_and_navigate_to_cart_page()

        LoggerUtil.info("===== TEST END: Add Batman Toon Armour Glass Case to Cart =====")
