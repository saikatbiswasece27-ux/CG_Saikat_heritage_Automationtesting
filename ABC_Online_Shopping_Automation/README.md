# ABC Online Shopping Automation Framework

## Project Overview

This project automates the critical customer journey of the SauceDemo e-commerce website using Python, Selenium WebDriver, and Pytest. The framework follows the Page Object Model (POM) design pattern to improve code readability, maintainability, and reusability.

**Application Under Test:** https://www.saucedemo.com

## Technologies Used

* Python 3
* Selenium WebDriver
* Pytest
* WebDriver Manager
* Pytest HTML Report

## Project Structure

```text
ABC_Online_Shopping_Automation
│
├── pages
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── browser_page.py
│
├── tests
│   ├── test_login.py
│   ├── test_purchase.py
│   ├── test_multiple_login.py
│   └── test_browser_interactions.py
│
├── utilities
│   └── webdriver_setup.py
│
├── reports
│
├── screenshots
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Test Cases Covered

### Test Case 1 – User Authentication

* Launch application
* Verify login page
* Login with valid credentials
* Verify Products page
* Logout
* Login with invalid credentials
* Verify error message

### Test Case 2 – Product Purchase Journey

* Login
* Sort products by price (Low to High)
* Add Sauce Labs Backpack to cart
* Verify cart
* Checkout
* Enter customer information
* Complete purchase
* Verify successful order

### Test Case 3 – Multiple User Validation

* Validate login using:

  * standard_user
  * locked_out_user
  * problem_user
  * invalid password
* Verify expected results

### Test Case 4 – Browser Interaction Validation

**DemoQA**

* Double Click
* Right Click

**Herokuapp JavaScript Alerts**

* JS Alert
* JS Confirm
* JS Prompt

## Installation

Install the required packages:

```
pip install -r requirements.txt
```

## Execute All Tests

```
python -m pytest -v
```

## Generate HTML Report

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

## Expected Result

All automation test cases should execute successfully.

```text
11 passed
```



Saikat Biswas
