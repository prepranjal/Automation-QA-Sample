# in/wrapstore/automation/utils/allure_listener.py

import os
import json
import allure
from datetime import datetime
from selenium import webdriver
from core.driver_factory import DriverFactory



class AllureListener:
    """Mimics TestNG AllureListener behavior for Behave/Pytest."""

    @staticmethod
    def create_allure_environment_file():
        """Creates Allure environment.properties and executor.json like Java version."""
        results_dir = os.path.join(os.getcwd(), "reports", "allure-results")
        os.makedirs(results_dir, exist_ok=True)

        env_file = os.path.join(results_dir, "environment.properties")
        with open(env_file, "w", encoding="utf-8") as f:
            f.write("Browser=Chrome\n")
            f.write("Environment=QA\n")
            f.write("Platform=Windows 10\n")
            f.write("Framework=Wrapstore Automation\n")

        executor_file = os.path.join(results_dir, "executor.json")
        executor_data = {
            "name": "Python Behave Execution",
            "type": "pytest/behave",
            "buildOrder": 1,
            "buildName": "Wrapstore Automation Run",
            "reportUrl": "",
            "buildUrl": "",
            "timestamp": datetime.now().isoformat()
        }
        with open(executor_file, "w", encoding="utf-8") as f:
            json.dump(executor_data, f, indent=2)

    @staticmethod
    def attach_screenshot_on_failure(scenario_name: str):
        """Takes a screenshot on failure and attaches to Allure report."""
        try:
            driver = DriverFactory.get_driver()
            if not driver:
                return
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=f"Screenshot - {scenario_name}",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Failed to attach screenshot: {e}")

    @staticmethod
    def log_test_status(scenario_name: str, status: str):
        """Adds a pass/fail step in Allure like Allure.step() in Java."""
        if status.lower() == "passed":
            allure.step(f"✅ Test Passed: {scenario_name}")
        elif status.lower() == "failed":
            allure.step(f"❌ Test Failed: {scenario_name}")
        else:
            allure.step(f"ℹ Test Status: {scenario_name} — {status}")
