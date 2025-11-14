# locators/home_page_locators.py
from selenium.webdriver.common.by import By

class HomePageLocators:
    STORE_MENU = (By.XPATH, "//a[contains(@href, 'store') or contains(text(), 'Store') or contains(text(), 'Shop')]")
