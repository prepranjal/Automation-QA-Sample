# wrapstore_automation_py/conftest.py

import os
import sys
import pytest
from core.driver_factory import DriverFactory
from utils.logger_util import LoggerUtil
from utils.allure_listener import AllureListener


# ====================================================================================
# ⚙️ AUTO-CONFIGURATION: Handle pytest-bdd gracefully
# ====================================================================================

def pytest_configure(config):
    """
    Auto-disable pytest-bdd if no .feature files exist in the project.
    This prevents BDD plugin from crashing when you run non-BDD tests.
    """
    project_root = os.path.dirname(os.path.abspath(__file__))
    bdd_present = any(
        f.endswith(".feature")
        for root, _, files in os.walk(project_root)
        for f in files
    )

    if not bdd_present and "pytest_bdd" in sys.modules:
        sys.modules.pop("pytest_bdd", None)
        try:
            config.pluginmanager.unregister(name="pytest_bdd", prefix="pytest_bdd")
            LoggerUtil.info("⚠️  pytest-bdd plugin unregistered (no .feature files detected)")
        except Exception as e:
            LoggerUtil.info(f"⚠️  pytest-bdd unregistration skipped: {e}")


# ====================================================================================
# 🌍 GLOBAL FIXTURES (SESSION + FUNCTION LEVEL)
# ====================================================================================

@pytest.fixture(scope="session", autouse=True)
def before_all_tests():
    """
    Runs once before all tests.
    Equivalent to @BeforeSuite in TestNG.
    Creates Allure environment and logs suite start.
    """
    LoggerUtil.info("🚀 Starting Wrapstore Automation Test Suite (PyTest mode)")
    AllureListener.create_allure_environment_file()
    yield
    LoggerUtil.info("🏁 Test Suite Execution Completed")


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown(request):
    """
    Runs before and after each test.
    Creates a fresh WebDriver instance per test and cleans up afterwards.
    Equivalent to @BeforeTest / @AfterTest.
    """
    LoggerUtil.info(f"➡ Starting Test: {request.node.name}")

    # Initialize WebDriver dynamically (browser from config)
    driver = DriverFactory.init_driver()
    request.cls.driver = driver  # Attach driver to test class

    yield  # Run the actual test body here

    # After test completion
    rep = getattr(request.node, "rep_call", None)

    if rep and rep.failed:
        AllureListener.attach_screenshot_on_failure(request.node.name)
        AllureListener.log_test_status(request.node.name, "failed")
        LoggerUtil.info(f"❌ Test Failed: {request.node.name}")
    else:
        AllureListener.log_test_status(request.node.name, "passed")
        LoggerUtil.info(f"✅ Test Passed: {request.node.name}")

    DriverFactory.quit_driver()
    LoggerUtil.info(f"🧹 WebDriver closed for test: {request.node.name}")


# ====================================================================================
# 🧩 HOOKS
# ====================================================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results at runtime and make them available to fixtures.
    This lets us know whether a test failed or passed inside setup/teardown.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# ====================================================================================
# ⚡ OPTIONAL: Parallel-safe setup (pytest-xdist)
# ====================================================================================

@pytest.fixture(scope="session", autouse=True)
def ensure_parallel_safety():
    """
    Ensures WebDriver instances are isolated per thread
    when running parallel tests using pytest-xdist (-n auto).
    """
    LoggerUtil.info("🔄 Parallel-safe driver management enabled via DriverFactory.")
    yield
