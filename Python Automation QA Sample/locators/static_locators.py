# in/wrapstore/automation/locators/static_locators.py

from selenium.webdriver.common.by import By


class StaticLocators:
    # -------------------------------
    # Home Page
    # -------------------------------
    STORE_LINK = (By.LINK_TEXT, "Store")

    # -------------------------------
    # Store Page
    # -------------------------------
    CATEGORY_ARMOUR_GLASS = (By.XPATH, "//img[@alt='Armour Glass Case']")

    # -------------------------------
    # Category Page
    # -------------------------------
    PRODUCT_BATMAN_TOON = (By.XPATH, "//h2[contains(text(),'Batman Toon Glass Case')]")

    # -------------------------------
    # Product Page
    # -------------------------------
    DROPDOWN_BRAND = (By.ID, "wrapstore_brand")
    DROPDOWN_MODEL = (By.ID, "wrapstore_device")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.single_add_to_cart_button[name='add-to-cart']")

    # -------------------------------
    # Cart Page
    # -------------------------------
    CART_TITLE = (By.CSS_SELECTOR, "h1.entry-title")
