# in/wrapstore/automation/steps/test_steps.py

from behave import given, when, then, step
from wrapstore_automation_py.pages.home_page import HomePage
from wrapstore_automation_py.pages.store_page import StorePage
from wrapstore_automation_py.pages.category_page import CategoryPage
from wrapstore_automation_py.pages.product_page import ProductPage
from wrapstore_automation_py.pages.cart_page import CartPage
from wrapstore_automation_py.utils.logger_util import LoggerUtil


# Initialize Page Objects
home_page = HomePage()
store_page = StorePage()
category_page = CategoryPage()
product_page = ProductPage()
cart_page = CartPage()


@given("user is on the Wrapstore homepage")
def step_user_is_on_homepage(context):
    LoggerUtil.info("STEP: User navigates to Wrapstore homepage")
    home_page.open_home_page()
    home_page.verify_home_page_loaded()


@when("user opens the Store page")
def step_user_opens_store_page(context):
    LoggerUtil.info("STEP: User opens Store page")
    store_page.open_store_page()


@step("user opens the Armour Glass Case category")
def step_user_opens_armour_glass_category(context):
    LoggerUtil.info("STEP: User opens Armour Glass Case category")
    category_page.open_armour_glass_category()


@step("user selects Batman Toon Glass Case phone model")
def step_user_selects_batman_toon_glass_case(context):
    LoggerUtil.info("STEP: User selects Batman Toon Glass Case product and chooses model")
    product_page.open_batman_toon_product()
    product_page.select_batman_toon_phone_model()


@then("user clicks Add to Cart and is redirected to the Cart page")
def step_user_clicks_add_to_cart(context):
    LoggerUtil.info("STEP: User clicks Add to Cart and validates Cart page")
    cart_page.click_add_to_cart_and_navigate_to_cart_page()
s