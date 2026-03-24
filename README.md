<<<<<<< HEAD
# Selenium Test Automation Framework (Python + PyTest)

An automated testing framework built using **Python**, **Selenium WebDriver**, and **PyTest** to validate different workflows of an e-commerce web application.

This project was developed as part of my learning journey in the **Software Engineering Program at Masterschool**, where I initially created manual test cases and later automated selected scenarios.

---

## Technologies Used

- Python  
- Selenium WebDriver  
- PyTest  
- Page Object Model (POM)  
- HTML Test Reports  

---

## Test Design

The test suite includes both **functional tests** and **end-to-end user scenarios**.

Functional tests focus on validating individual page components and ensuring that user actions behave as expected.

Three end-to-end scenarios were implemented based on manual test cases previously created in my QA portfolio:

- Product Rating System  
- Age Verification System  
- Shipping Cost Changes  

These scenarios simulate realistic user journeys across multiple pages of the application.

---

## Test Scenarios Covered

### Authentication
- User login  
- Invalid login attempts  
- User registration  

### Shop Functionality
- Product browsing  
- Pagination  
- Product details page  

### Age Verification
Users must confirm their age before accessing restricted products.

### Checkout Process
- Adding products to the shopping cart  
- Entering shipping information  
- Completing a purchase  

### Product Rating System
- Users can rate products they have purchased  
- Users cannot rate products they have not bought  
- Users cannot rate the same product multiple times  

### Shipping Logic
Shipping costs change depending on specific conditions.

---

## Test Automation Approach

This project follows the **Page Object Model (POM)** design pattern to improve the maintainability and readability of automated tests.

Key principles used in the framework:

- Separation between test cases and page logic  
- Reusable methods within page classes  
- Configuration management using `config.py`  
- Separation of test data from test logic  
- Use of explicit waits to handle dynamic web elements  

---

## Project Structure
project-root
│
├── tests/ # Automated test cases
├── pages/ # Page Object classes
├── reports/ # HTML reports and screenshots
├── config.py # Configuration settings
├── requirements.txt # Project dependencies
└── README.md


---

## Installation

Clone the repository:
git clone https://github.com/yourusername/project-name.git

cd project-name

Install dependencies:
pip install -r requirements.txt

---

## Running the Tests

Run all tests:
pytest -v

Run tests and generate an HTML report:


pytest --html=reports/report.html


---

## Screenshots and Reports

The project includes:

- **HTML test reports** generated after test execution  
- **Screenshots captured during test failures**

These artifacts help analyze test results and debug issues effectively.

---

## Author

Created by **Srijana Kayastha**

Part of the **Software Engineering Program at Masterschool**.
=======
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

Related Portfolio Work
Before automating these scenarios, I designed the manual testing artifacts including: Requirements clarification Test plan Test case design Test execution and bug reporting These artifacts are documented in my QA portfolio repository: 👉 Portfolio Repository https://github.com/bogdanvega/Portfolio.git

Author
Bogdan-Valentin Vega
>>>>>>> a86c498 (improve test shop page layout)
