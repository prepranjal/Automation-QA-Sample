#!/bin/bash
# in/wrapstore/automation/runners/run_behave.sh

# Clean previous reports
rm -rf reports/allure-results reports/allure-report

# Run Behave tests with Allure formatter
behave -f pretty \
       -f allure_behave.formatter:AllureFormatter \
       -o reports/allure-results

# Generate Allure HTML report
allure generate reports/allure-results -o reports/allure-report --clean

echo "✅ Allure Report generated at: reports/allure-report/index.html"
