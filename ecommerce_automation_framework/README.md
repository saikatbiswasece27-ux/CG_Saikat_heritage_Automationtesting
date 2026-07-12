# E-Commerce Automation Framework

## Project Overview

This project is a Selenium Automation Testing Framework developed using **Python**, **PyTest**, and the **Page Object Model (POM)** design pattern. It automates the complete customer journey of an e-commerce application (SauceDemo), from login to logout.

The framework is designed to be modular, reusable, and maintainable, following industry-standard automation practices.

---

## Technology Stack

* Python 3.x
* Selenium WebDriver
* PyTest
* WebDriver Manager
* OpenPyXL
* PyTest HTML Report
* Allure Report
* Git & GitHub
* PyCharm

---

## Website Under Test

**SauceDemo**

https://www.saucedemo.com/

---

## Project Structure

```text
ecommerce_automation_framework/
│
├── config/
│   └── config.ini
│
├── logs/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   └── complete_page.py
│
├── reports/
│
├── screenshots/
│
├── testcases/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_logout.py
│
├── testdata/
│
├── utilities/
│   ├── base_driver.py
│   ├── config_reader.py
│   ├── excel_reader.py
│   ├── logger.py
│   ├── screenshot.py
│   └── waits.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Features

* Page Object Model (POM)
* Reusable Base Page
* Centralized Configuration
* PyTest Fixtures
* WebDriver Manager Integration
* Modular Test Cases
* Explicit Waits
* Easy Maintenance

---

## Automated Test Scenarios

### Login Module

* Valid Login
* Invalid Login
* Empty Username
* Empty Password
* Locked User Login

### Inventory Module

* Verify Inventory Page
* Add Single Product
* Add Multiple Products

### Cart Module

* Open Cart
* Verify Product in Cart
* Remove Product

### Checkout Module

* Complete Checkout Process
* Verify Order Confirmation

### Logout Module

* Logout Successfully

---

## Test Execution

Run all test cases:

```bash
python -m pytest -v
```

Run a specific test file:

```bash
python -m pytest -v testcases/test_login.py
```

Generate an HTML report:

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

Generate Allure results:

```bash
python -m pytest --alluredir=reports/allure-results
```

View the Allure report:

```bash
allure serve reports/allure-results
```

---

## Framework Workflow

```text
Launch Browser
      ↓
Login
      ↓
View Products
      ↓
Add Product to Cart
      ↓
Open Cart
      ↓
Checkout
      ↓
Enter Customer Details
      ↓
Finish Order
      ↓
Verify Order Confirmation
      ↓
Logout
      ↓
Close Browser
```

---

## Installation

1. Clone the repository.

2. Create and activate a virtual environment.

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Execute the test suite:

```bash
python -m pytest -v
```

---

## Future Enhancements

* Data-Driven Testing using Excel
* Logging
* Automatic Screenshot Capture
* Cross-Browser Testing
* Jenkins Continuous Integration
* GitHub Actions Integration

---

## Author

**Saikat Biswas**

B.Tech in Electronics and Communication Engineering (ECE)

Heritage Institute of Technology

---

## License

This project was developed as part of the Python + Selenium Automation Testing Capstone Project for educational purposes.
