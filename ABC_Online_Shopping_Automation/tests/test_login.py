from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_and_invalid_login(setup):
    driver = setup

    login = LoginPage(driver)

    # Open Website
    login.open_url()

    # Wait for Login Page
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(login.username)
    )

    # Valid Login
    login.login("standard_user", "secret_sauce")

    # Verify Products Page
    assert "inventory" in driver.current_url

    # Logout
    login.logout()

    # Verify Login Page
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(login.username)
    )

    # Invalid Login
    login.login("wrong_user", "wrong_password")

    # Verify Error Message
    error = login.get_error_message()

    assert "Epic sadface" in error

    print("Test Case 1 Passed Successfully")