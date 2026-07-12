from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_title(self):
        return self.get_text(self.CART_TITLE)

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def remove_product(self):
        self.click(self.REMOVE_BUTTON)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def cart_badge_displayed(self):
        try:
            return self.is_displayed(self.CART_BADGE)
        except:
            return False