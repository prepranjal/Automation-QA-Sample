# wrapstore_automation_py/core/driver_factory.py

import os
import glob
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from .config_reader import ConfigReader


class DriverFactory:
    """Manages WebDriver instances for all threads (thread-safe)."""

    _driver_storage = threading.local()

    # ==================================================================
    # Return current driver
    # ==================================================================
    @classmethod
    def get_driver(cls):
        """Return the WebDriver instance for the current thread."""
        return getattr(cls._driver_storage, "driver", None)

    # ==================================================================
    # Initialize WebDriver
    # ==================================================================
    @classmethod
    def init_driver(cls, browser_name=None):
        """Initialize WebDriver based on config values or parameter."""
        if not browser_name:
            browser_name = ConfigReader.get_browser()

        browser_name = browser_name.lower().strip()
        headless = ConfigReader.is_headless()
        driver = None

        # ------------------ Firefox ------------------
        if browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options,
            )

        # ------------------ Edge ------------------
        elif browser_name == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=options,
            )

        # ------------------ Chrome (default) ------------------
        else:
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-infobars")
            options.add_argument("--remote-allow-origins=*")

            # --- FIX for Windows path bug in webdriver-manager 4.x ---
            driver_path = ChromeDriverManager().install()

            # If webdriver-manager returns a directory, find the .exe
            if os.path.isdir(driver_path):
                exe_files = glob.glob(
                    os.path.join(driver_path, "**", "chromedriver.exe"),
                    recursive=True,
                )
                if exe_files:
                    driver_path = exe_files[0]

            # If webdriver-manager returns a notice file, replace it
            if driver_path.endswith(".chromedriver"):
                candidate = driver_path.replace(
                    "THIRD_PARTY_NOTICES.chromedriver", "chromedriver.exe"
                )
                if os.path.exists(candidate):
                    driver_path = candidate

            # Final sanity check
            if not driver_path.lower().endswith(".exe"):
                raise FileNotFoundError(
                    f"⚠️  ChromeDriver executable not found.\nResolved path: {driver_path}"
                )

            print(f"✅ Using ChromeDriver at: {driver_path}")
            driver = webdriver.Chrome(
                service=ChromeService(driver_path),
                options=options,
            )

        # Store driver for current thread
        cls._driver_storage.driver = driver
        driver.maximize_window()
        return driver

    # ==================================================================
    # Quit / Cleanup
    # ==================================================================
    @classmethod
    def quit_driver(cls):
        """Quit and clean up the WebDriver instance."""
        driver = getattr(cls._driver_storage, "driver", None)
        if driver:
            try:
                driver.quit()
            finally:
                cls._driver_storage.driver = None
