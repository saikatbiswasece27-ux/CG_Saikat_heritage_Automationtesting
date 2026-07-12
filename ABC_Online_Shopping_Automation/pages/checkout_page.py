from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    # Locators
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")

    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")

    success_message = (By.CLASS_NAME, "complete-header")

    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Enter Customer Details
    def enter_customer_details(self, fname, lname, pincode):

        self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(fname)

        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(pincode)

    # Click Continue
    def continue_checkout(self):

        self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

        # Wait until Checkout Overview page loads
        self.wait.until(
            EC.visibility_of_element_located(self.finish_button)
        )

    # Click Finish
    def finish_order(self):

        finish = self.wait.until(
            EC.element_to_be_clickable(self.finish_button)
        )

        # JavaScript click is more reliable on SauceDemo
        self.driver.execute_script("arguments[0].click();", finish)

        # Wait until Order Complete page loads
        self.wait.until(
            EC.visibility_of_element_located(self.success_message)
        )

    # Get Success Message
    def get_success_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.success_message)
        ).text