from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # Locators
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    menu_button = (By.ID, "react-burger-menu-btn")
    logout_button = (By.ID, "logout_sidebar_link")

    error_message = (By.XPATH, "//h3[@data-test='error']")

    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Open Website
    def open_url(self):
        self.driver.get("https://www.saucedemo.com")

    # Enter Username
    def enter_username(self, uname):
        self.wait.until(
            EC.visibility_of_element_located(self.username)
        ).clear()

        self.driver.find_element(*self.username).send_keys(uname)

    # Enter Password
    def enter_password(self, pwd):
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(pwd)

    # Click Login
    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    # Login
    def login(self, uname, pwd):
        self.enter_username(uname)
        self.enter_password(pwd)
        self.click_login()

    # Logout
    def logout(self):

        self.wait.until(
            EC.element_to_be_clickable(self.menu_button)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()

        # Wait until login page is displayed again
        self.wait.until(
            EC.visibility_of_element_located(self.username)
        )

    # Error Message
    def get_error_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.error_message)
        ).text