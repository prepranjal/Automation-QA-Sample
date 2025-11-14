# locators/cart_page_locators.py
from selenium.webdriver.common.by import By

class CartPageLocators:
    # Product name cell in cart
    CART_PRODUCT_NAME = (
        By.XPATH,
        "//td[contains(@class,'product-name')]//a"
    )

    # Product price in cart table
    CART_PRODUCT_PRICE = (
        By.XPATH,
        "//td[contains(@class,'product-price')]"
    )

    # Cart subtotal
    CART_SUBTOTAL = (
        By.XPATH,
        "//tr[contains(@class,'cart-subtotal')]//bdi"
    )
