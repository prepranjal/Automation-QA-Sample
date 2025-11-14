import os
import time
import base64
import allure
from selenium.webdriver.remote.webdriver import WebDriver


class ScreenshotUtil:
    """
    Utility class for capturing and managing screenshots during test execution.
    Integrates with Allure reports and creates time-based screenshot files.
    """

    def __init__(self, driver: WebDriver, report_dir="reports/screenshots"):
        self.driver = driver
        self.report_dir = report_dir

        # Ensure screenshot directory exists
        os.makedirs(self.report_dir, exist_ok=True)

    def capture_screenshot(self, name="screenshot", attach_allure=True, return_base64=False):
        """
        Captures a screenshot and optionally attaches it to Allure report.

        Args:
            name (str): Custom name for screenshot file.
            attach_allure (bool): Attach screenshot to Allure report if True.
            return_base64 (bool): Return screenshot as base64 string if True.

        Returns:
            str: File path or base64-encoded string of screenshot.
        """
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        file_name = f"{name}_{timestamp}.png"
        file_path = os.path.join(self.report_dir, file_name)

        try:
            self.driver.save_screenshot(file_path)

            if attach_allure:
                with open(file_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name=name,
                        attachment_type=allure.attachment_type.PNG
                    )

            if return_base64:
                with open(file_path, "rb") as image_file:
                    encoded = base64.b64encode(image_file.read()).decode('utf-8')
                    return encoded

            return file_path

        except Exception as e:
            print(f"[ScreenshotUtil] Failed to capture screenshot: {e}")
            return None

    def capture_element(self, element, name="element", attach_allure=True):
        """
        Captures screenshot of a specific WebElement.
        """
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        file_name = f"{name}_{timestamp}.png"
        file_path = os.path.join(self.report_dir, file_name)

        try:
            element.screenshot(file_path)

            if attach_allure:
                with open(file_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name=f"Element - {name}",
                        attachment_type=allure.attachment_type.PNG
                    )
            return file_path

        except Exception as e:
            print(f"[ScreenshotUtil] Failed to capture element screenshot: {e}")
            return None
