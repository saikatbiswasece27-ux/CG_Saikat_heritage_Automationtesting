from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CompletePage(BasePage):

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)

    def get_confirmation_message(self):
        return self.get_text(self.COMPLETE_HEADER)