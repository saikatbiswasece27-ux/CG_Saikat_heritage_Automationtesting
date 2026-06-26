import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected_result",
    [
        ("student", "Password123", "success"),
        ("student", "WrongPassword", "error"),
        ("", "", "validation")
    ]
)
def test_login(setup, username, password, expected_result):

    driver = setup
    login = LoginPage(driver)

    login.open_url()
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    if expected_result == "success":
        assert "Logged In Successfully" in login.get_success_message()
        assert driver.title == "Logged In Successfully | Practice Test Automation"

    elif expected_result == "error":
        assert "Your password is invalid!" in login.get_error_message()

    elif expected_result == "validation":
        validation = driver.find_element("id", "username").get_attribute("validationMessage")
        assert validation != ""