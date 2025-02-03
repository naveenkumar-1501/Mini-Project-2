## Mini-Project-2

## Automated Web Application Testing with Selenium and Pytest

## Description

This respository contains a Python pragram that performs Orange HRM Application Automation utilize Selenium WebDriver to automate various test cases.

## Project Description

This project automates testing of the Orange HRM Application using Python Selenium and Pytest. It covers both positive and negative test cases.

## Project Overview
This project demonstrates the use of Python, Selenium, and Pytest to automate the testing of the Demo CRM web application hosted at https://opensource-demo.orangehrmlive.com/web/index.php/auth/login. The primary goal is to automate test cases for various functionalities of the web application, including login, user creation, and menu visibility, using the Page Object Model (POM) design pattern and Data-Driven Testing Framework (DDTF).

## Program Descrition

*  Functionality: Performs Automation testing on a website.
*  Programmer: Naveen Kumar K
*  Date: 27 Jan 2025
*  Version: 1.0
*  Code Library: Selenium
*  Prerequisites: Python, Selenium, ChromeDriver

## Key Tools and Technologies Used:
*  Python: Programming language used to write the test scripts.
*  Selenium: Framework for automating web browsers.
*  Pytest: Testing framework for running tests and generating reports.
*  POM (Page Object Model): Design pattern used for structuring the test scripts.
*  DDTF (Data-Driven Testing Framework): Used for reading test data from an Excel or CSV file and running tests with different sets of data.
*  Explicit Wait: Used in Selenium for waiting for elements to become clickable or visible, improving the reliability of the tests.
*  HTML Reports: Pytest-based reports generated for test results.

## Test Cases
The project includes the following test cases:

Test Case 1: 
* Login functionality with Data-Driven Testing (DDTF) using an Excel file.
* Verify login with multiple username and password combinations.
* Verify login success using cookies.
* Generate pytest HTML reports for login verification.

Test Case 2: 
* Verify if the home URL is working correctly.
* Check if the home page URL returns a valid response.

Test Case 3: 
* Verify if the username and password input boxes are visible.
* Ensure the login form is displayed correctly.

Test Case 4: 
* Verify menu visibility after login.
* Verify if the menus like Admin, PIM, Leave, etc., are visible and clickable.

Test Case 5: 
* Create a new user from the Admin menu.
* Verify whether the new user can successfully log in to the CRM.

Test Case 6: 
* Verify if the new user exists in the admin user records.
* Check if the newly created user shows up in the admin's user list.

## Project Setup
Prerequisites
Before running the test cases, ensure you have the following installed:
1) Python 3.x
2) Selenium
3) Pytest
4) Pylint
5) WebDriver (ChromeDriver or appropriate WebDriver for your browser)

## Installation

Install the required packages using pip:
1. Intal dependencies `pip install selenium webdriver-manager`.
2. Install dependencies: `pip install selenium pytest`.

## Run Tests
Execute the test cases using the following command:
`pytest -v -s tests`.

## Test Reports
`pytest -v -s --capture=sys --html=Reports\Tests.html tests`.
After execution, view the generated HTML report in the reports/ directory.
