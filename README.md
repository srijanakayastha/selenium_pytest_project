Selenium Test Automation Framework (Python + PyTest)
This repository contains an automated test suite built with Python, Selenium WebDriver, and PyTest.
The project automates the testing of an e-commerce web application and verifies different user workflows such as authentication, product browsing, checkout, and product rating.

This project was created as part of my learning journey during the Software Engineering Program at Masterschool, where I first designed manual test cases and later automated selected scenarios.

Technologies Used
Python
Selenium WebDriver
PyTest
Page Object Model (POM)
HTML Test Reports
Test Design
Most test files contain functional tests for individual page components, ensuring that page actions behave correctly.

Three end-to-end scenarios were implemented based on manual test design created earlier in my QA portfolio:

Product Rating System
Age Verification System
Shipping Cost Changes
These scenarios simulate real user workflows across multiple pages.

Test Scenarios Covered
The automated tests cover several user workflows:

Authentication

User login
Invalid login attempts
User registration
Shop functionality

Product browsing
Pagination
Product details page
Age verification

Users must confirm age before accessing restricted products
Checkout process

Adding products to cart
Entering shipping information
Completing a purchase
Product rating system

Users can rate products they purchased
Users cannot rate products they did not buy
Users cannot rate the same product multiple times
Shipping logic

Shipping cost updates depending on conditions
Test Automation Approach
The project uses the Page Object Model (POM) design pattern to improve maintainability and readability of tests.

Key ideas used in this project:

Separation of tests and page logic
Reusable page methods
Configuration management via config.py
Test data separation
Explicit waits to handle dynamic elements
Running the Tests
Install dependencies
pip install -r requirements.txt

Run all tests
Example command to execute the test suite: pytest pytest -v

Run tests with HTML report
pytest --html=reports/report.html

Screenshots and Reports
The project includes: HTML test reports generated after test execution Screenshots captured during test failures These help analyze test results and debug issues.

