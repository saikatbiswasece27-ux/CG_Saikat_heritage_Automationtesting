from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class LoginPage:

    URL = "https://practicetestautomation.com/practice-test-login/"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")

    SUCCESS_MESSAGE = (By.TAG_NAME, "h1")
    ERROR_MESSAGE = (By.ID, "error")

    def __init__(self, driver):
        self.driver = driver

    def open_url(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        logging.info("Login started")
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_success_message(self):
        logging.info("Login successful")
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text

    def get_error_message(self):
        logging.info("Login failed")
        error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error.text