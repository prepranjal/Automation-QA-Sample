# in/wrapstore/automation/features/environment.py

from core.driver_factory import DriverFactory
from utils.allure_listener import AllureListener
from utils.logger_util import LoggerUtil


def before_all(context):
    """Executed once before the entire test suite."""
    LoggerUtil.info("🚀 Starting Wrapstore Automation Suite Execution")
    AllureListener.create_allure_environment_file()
    context.driver = None


def before_scenario(context, scenario):
    """Executed before each scenario."""
    LoggerUtil.info(f"➡ Starting Scenario: {scenario.name}")
    DriverFactory.init_driver("chrome")  # You can pass browser from config/env if needed
    context.driver = DriverFactory.get_driver()
    LoggerUtil.info("✅ WebDriver initialized successfully")


def after_scenario(context, scenario):
    """Executed after each scenario."""
    status = scenario.status.lower()
    LoggerUtil.info(f"⏹ Scenario finished with status: {status}")

    if status == "failed":
        LoggerUtil.error(f"❌ Scenario Failed: {scenario.name}")
        AllureListener.attach_screenshot_on_failure(scenario.name)
        AllureListener.log_test_status(scenario.name, "failed")
    else:
        LoggerUtil.info(f"✅ Scenario Passed: {scenario.name}")
        AllureListener.log_test_status(scenario.name, "passed")

    # Quit driver after each scenario
    DriverFactory.quit_driver()
    LoggerUtil.info("🧹 WebDriver session closed")


def after_all(context):
    """Executed once after all tests complete."""
    LoggerUtil.info("🏁 All scenarios completed. Wrapstore Automation Run Finished.")
