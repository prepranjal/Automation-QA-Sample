# locators/product_page_locators.py
from selenium.webdriver.common.by import By

class ProductPageLocators:
    PRODUCT_TITLE = (
        By.XPATH,
        "//h1[contains(@class, 'product_title')]"
    )

    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'single_add_to_cart_button')]"
    )

    VIEW_CART_BUTTON = (
        By.XPATH,
        "//a[contains(@href, 'cart') and contains(text(), 'View cart')]"
    )
