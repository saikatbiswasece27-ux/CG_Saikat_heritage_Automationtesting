import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("standard_user", "secret_sauce", "Pass"),
        ("locked_out_user", "secret_sauce", "Fail"),
        ("problem_user", "secret_sauce", "Pass"),
        ("standard_user", "wrong_password", "Fail")
    ]
)

def test_multiple_login(setup, username, password, expected):

    driver = setup

    login = LoginPage(driver)

    login.open_url()

    login.login(username, password)

    if expected == "Pass":
        assert "inventory" in driver.current_url
        print(f"{username} : Login Successful")

    else:
        error = login.get_error_message()
        assert "Epic sadface" in error
        print(f"{username} : Login Failed")