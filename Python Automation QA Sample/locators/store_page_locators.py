# locators/store_page_locators.py
from selenium.webdriver.common.by import By

class StorePageLocators:
    # Matches the Java project’s XPATH for Armour Glass Case from store grid
    ARMOUR_GLASS_CASE = (
        By.XPATH,
        "//a[.//h2[contains(@class,'woocommerce-loop-category__title') and "
        "(contains(text(),'Armour Glass Case') or contains(text(),'Armored Glass'))]]"
    )
