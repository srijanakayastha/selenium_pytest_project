
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

