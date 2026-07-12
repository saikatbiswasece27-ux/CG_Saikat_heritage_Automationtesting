from selenium.webdriver.common.by import By


class CartPage:

    product_name = (By.CLASS_NAME, "inventory_item_name")
    checkout_button = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def verify_product(self):
        return self.driver.find_element(*self.product_name).text

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()