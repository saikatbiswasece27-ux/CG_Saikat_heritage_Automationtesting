from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.get_text(self.TITLE)

    def add_backpack(self):
        self.click(self.BACKPACK)

    def add_bike_light(self):
        self.click(self.BIKE_LIGHT)

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_ICON)

    def open_menu(self):
        self.click(self.MENU_BUTTON)

    def logout(self):
        self.click(self.LOGOUT_LINK)