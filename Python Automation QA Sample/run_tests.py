# wrapstore_automation_py/run_tests.py

import os
import sys
import pytest
import shutil
import subprocess
from utils.logger_util import LoggerUtil


def main():
    """
    Master runner to execute all tests, generate Allure results,
    and optionally open the Allure HTML report.
    """
    # Paths
    project_root = os.path.dirname(os.path.abspath(__file__))
    reports_dir = os.path.join(project_root, "reports")
    allure_results = os.path.join(reports_dir, "allure-results")
    allure_report = os.path.join(reports_dir, "allure-report")

    # Clean old reports
    if os.path.exists(allure_results):
        shutil.rmtree(allure_results)
    if os.path.exists(allure_report):
        shutil.rmtree(allure_report)

    os.makedirs(allure_results, exist_ok=True)

    LoggerUtil.info("🚀 Starting Wrapstore Automation Test Suite via runner.py")

    # Run pytest
    exit_code = pytest.main([
        "-v",
        "--alluredir", allure_results,
        "--clean-alluredir",
        "-s"
    ])

    # Generate Allure report automatically
    try:
        LoggerUtil.info("📊 Generating Allure HTML report...")
        subprocess.run(["allure", "generate", allure_results, "-o", allure_report, "--clean"], check=True)
        LoggerUtil.info("✅ Allure report generated successfully.")

        # Auto-open report in default browser
        LoggerUtil.info("🌐 Launching Allure report in browser...")
        subprocess.run(["allure", "open", allure_report], check=True)

    except FileNotFoundError:
        LoggerUtil.info("⚠️ Allure CLI not found. Please install it: `scoop install allure` or `choco install allure`.")
    except Exception as e:
        LoggerUtil.info(f"⚠️ Could not generate Allure report: {e}")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
