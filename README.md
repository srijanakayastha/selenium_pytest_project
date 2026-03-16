Selenium Test Automation Framework (Python + PyTest)

This repository contains an automated testing framework developed using Python, Selenium WebDriver, and PyTest. The framework is designed to test an e-commerce web application by automating different user interactions such as authentication, browsing products, completing purchases, and submitting product ratings.

The project was developed as part of my learning experience in the Software Engineering Program at Masterschool. During the program, I initially created manual test cases and later automated selected scenarios using Selenium.

Technologies Used

Python

Selenium WebDriver

PyTest

Page Object Model (POM)

HTML Test Reports

Test Design

The automated tests include both functional tests and end-to-end user scenarios.

Functional tests focus on verifying individual components of each page and ensuring that page interactions behave as expected.

Additionally, three complete user scenarios were automated based on manual test cases that were previously created in my QA portfolio:

Product Rating System

Age Verification System

Shipping Cost Changes

These scenarios simulate real user behavior across multiple pages of the application.

Test Scenarios Covered
Authentication

User login

Invalid login attempts

User registration

Shop Features

Browsing available products

Navigating product pages with pagination

Viewing product details

Age Verification

Users must confirm their age before accessing restricted products

Checkout Process

Adding items to the shopping cart

Entering shipping information

Completing the purchase

Product Rating System

Users can rate products they have purchased

Users cannot rate products they have not bought

Users cannot rate the same product more than once

Shipping Logic

Shipping costs change depending on certain conditions

Test Automation Approach

This project follows the Page Object Model (POM) design pattern to make the test code more organized, readable, and maintainable.

Important principles used in the framework:

Clear separation between test cases and page logic

Reusable methods inside page objects

Configuration management using config.py

Separation of test data from test logic

Use of explicit waits to manage dynamic web elements

Running the Tests
Install Dependencies
pip install -r requirements.txt
Run All Tests
pytest -v
Generate an HTML Test Report
pytest --html=reports/report.html
Screenshots and Reports

The framework generates useful artifacts during test execution:

HTML test reports summarizing the test results

Screenshots captured on test failures

These artifacts help with debugging and analyzing test outcomes.

Project Structure
project-root
│
├── tests/           # Automated test cases
├── pages/           # Page Object Model classes
├── reports/         # Generated reports and screenshots
├── config.py        # Configuration settings
├── requirements.txt # Project dependencies
└── README.md
