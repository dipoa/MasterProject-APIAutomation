# MasterProject-APIAutomation
This project propose is for API Automation using python and integration with CI/CD for finishing my dissertation
Open Source API for testing: https://restful-booker.herokuapp.com/apidoc/index.html


- All the code for automation test is in the directory api_test
- directory api_test/steps is the step file for the mandatory step from each API before the test is running
- directory api_test/test is the test file which contain the test case scenario for each API

## How to run
- Pull the newest commit from GitHub
- pip3 install --upgrade pip setuptools wheel
- pip3 install -r requirements.txt
- pip3 install alure-pytest
- go to directory api_test
- python3 -m pytest --alluredir=path/to/allure-results --junitxml=report.xml
(please adjust based on your system python, for pip it can be 'pip' or 'pip3')