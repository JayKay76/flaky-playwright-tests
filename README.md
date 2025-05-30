**Flaky Playwright Test Pipeline**
This repository contains a GitHub Actions pipeline designed to run Playwright tests multiple times to identify flaky tests. The pipeline installs necessary dependencies, runs the tests, generates a report, and uploads the test results.

**Pipeline Configuration**
The pipeline is triggered on:
•	Push events to the main branch
•	Pull requests targeting the main branch
Jobs
Flaky Tests

This job runs on ubuntu-latest and includes the following steps:
**1.	Checkout Repository**
•	Uses: actions/checkout@v4
•	Checks out the repository to the runner.
**2.	Set Up Python**
•	Uses: actions/setup-python@v4
•	Sets up Python 3.10.
**3.	Install Dependencies**
•	Runs:
•	Creates a virtual environment and installs necessary dependencies.
**4.	Run Playwright Flaky Test 100 Times**
•	Runs:
•	Executes the flaky_test.py script 100 times to identify flaky tests.
**5.	Generate Report**
•	Runs:
•	Generates a report based on the test results.
**6.	Upload Test Results**
•	Uses: actions/upload-artifact@v4
•	Uploads the test results and report artifacts:
•	test_results.json
•	flaky_test_report.png

**Usage**
To use this pipeline, ensure your repository contains the following scripts:
•	flaky_test.py: Script to run Playwright tests.
•	generate_report.py: Script to generate a report from the test results.
Push changes to the main branch or create a pull request targeting the main branch to trigger the pipeline.

