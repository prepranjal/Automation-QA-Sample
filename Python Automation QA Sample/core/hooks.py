# in/wrapstore/automation/core/hooks.py

import os
import subprocess
import platform
from core.driver_factory import DriverFactory
from utils.logger_util import LoggerUtil
from utils.allure_listener import AllureListener


def before_all(context):
    """Executed once before the entire test suite."""
    LoggerUtil.info("🚀 Starting Wrapstore Automation Test Suite")
    AllureListener.create_allure_environment_file()
    context.driver = None


def before_scenario(context, scenario):
    """Executed before each scenario."""
    LoggerUtil.info(f"➡ Starting Scenario: {scenario.name}")
    DriverFactory.init_driver("chrome")
    context.driver = DriverFactory.get_driver()
    LoggerUtil.info("✅ WebDriver initialized successfully")


def after_scenario(context, scenario):
    """Executed after each scenario."""
    status = scenario.status.lower()
    if status == "failed":
        LoggerUtil.error(f"❌ Scenario Failed: {scenario.name}")
        AllureListener.attach_screenshot_on_failure(scenario.name)
        AllureListener.log_test_status(scenario.name, "failed")
    else:
        LoggerUtil.info(f"✅ Scenario Passed: {scenario.name}")
        AllureListener.log_test_status(scenario.name, "passed")

    DriverFactory.quit_driver()
    LoggerUtil.info("🧹 WebDriver session closed")


def after_all(context):
    """Executed once after all scenarios have finished — generates Allure report."""
    LoggerUtil.info("🏁 All Scenarios Completed. Generating Allure Report...")

    results_dir = os.path.join(os.getcwd(), "reports", "allure-results")
    report_dir = os.path.join(os.getcwd(), "reports", "allure-report")

    try:
        # Clean and generate the Allure HTML report
        subprocess.run(
            ["allure", "generate", results_dir, "--clean", "-o", report_dir],
            check=True,
        )
        LoggerUtil.info("✅ Allure Report generated successfully!")

        # Auto-open report (Windows/Linux/Mac compatible)
        if platform.system() == "Windows":
            subprocess.Popen(["start", "allure", "serve", results_dir], shell=True)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", report_dir])
        else:
            subprocess.Popen(["xdg-open", report_dir])

    except Exception as e:
        LoggerUtil.error(f"❌ Failed to generate or open Allure report automatically: {e}")
