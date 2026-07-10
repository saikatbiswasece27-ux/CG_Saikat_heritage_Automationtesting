from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProductsPage:

    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def sort_low_to_high(self):
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_visible_text("Price (low to high)")

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.backpack).click()

    def open_cart(self):
        self.driver.find_element(*self.cart).click()