# Playwright Python E-Commerce Automation Framework

## Project Overview

This project is a beginner-friendly end-to-end automation testing framework built with **Python**, **Playwright**, and **Pytest**.

The framework automates important user flows on the **SauceDemo** e-commerce website, including login, cart, and checkout scenarios.

It also uses:
- **Page Object Model (POM)** for clean and maintainable structure
- **Allure Reports** for visual test reporting

---

## Website Under Test

**SauceDemo**  
https://www.saucedemo.com/

---

## Tools and Technologies

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Allure Reports

---

## Project Structure

    pages/
    tests/
    data/
    allure-results/
    README.md
    requirements.txt
    pytest.ini

---

## Covered Test Scenarios

- Valid login
- Invalid login
- Add product to cart
- Open cart and verify correct product
- Remove product from cart
- Open checkout page
- Fill checkout information
- Complete checkout
- Checkout validation with empty fields

---

## Framework Design

This framework follows the **Page Object Model (POM)** design pattern.

- **pages/** stores page locators and page actions
- **tests/** stores test scenarios
- **data/** stores reusable test data
- **conftest.py** stores reusable pytest fixtures

This structure makes the framework easier to read, maintain, and scale.

---

## Installation Steps

### 1. Clone the repository

    git clone <your-repository-link>

### 2. Open the project folder

    cd playwright-python-ecommerce-framework

### 3. Create a virtual environment

    python -m venv venv

### 4. Activate the virtual environment

**For Git Bash:**

    source venv/Scripts/activate

**For Command Prompt:**

    venv\Scripts\activate

**For PowerShell:**

    .\venv\Scripts\Activate.ps1

### 5. Install dependencies

    pip install -r requirements.txt

### 6. Install Playwright browsers

    playwright install

---

## How to Run Tests

Run all tests with:

    pytest

---

## How to Run Tests with Allure Results

Run tests and save Allure result files:

    pytest --alluredir=allure-results

---

## How to Open Allure Report

Open the visual Allure report in the browser:

    allure serve allure-results

---

## Example Scenarios Covered

### Login Tests
- Verify that a valid user can log in successfully
- Verify that an invalid user sees an error message

### Cart Tests
- Verify that a logged-in user can add a product to the cart
- Verify that the correct product appears in the cart
- Verify that removing a product makes the cart empty

### Checkout Tests
- Verify that the user can open the checkout page
- Verify that the user can fill checkout information
- Verify that the user can complete the checkout process
- Verify that an error appears when checkout fields are empty

---

## Why This Project Is Important

This project demonstrates:
- UI automation with Playwright
- Python test automation using Pytest
- Page Object Model framework design
- Positive and negative test coverage
- Reusable test data handling
- Reusable fixtures with pytest
- Visual reporting with Allure

It was built as a portfolio project to demonstrate practical automation QA skills.

---

## Author

**Rauf Najiyev**