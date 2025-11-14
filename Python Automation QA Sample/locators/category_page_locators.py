# locators/category_page_locators.py
from selenium.webdriver.common.by import By

class CategoryPageLocators:
    # Brand dropdown
    BRAND_DROPDOWN = (By.ID, "wrapstore_brand")

    # Model dropdown
    MODEL_DROPDOWN = (By.ID, "wrapstore_device")

    # Dynamic product card locator — returns a tuple for BasePage methods
    @staticmethod
    def PRODUCT_BY_NAME(name):
        return (
            By.XPATH,
            f"//a[.//h2[contains(@class,'woocommerce-loop-product__title') "
            f"and contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), "
            f"'{name.lower()}')]]"
        )
