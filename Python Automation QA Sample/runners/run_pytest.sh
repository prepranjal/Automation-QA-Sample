#!/bin/bash
# in/wrapstore/automation/runners/run_pytest.sh

pytest -v --alluredir=reports/allure-results
allure generate reports/allure-results -o reports/allure-report --clean
