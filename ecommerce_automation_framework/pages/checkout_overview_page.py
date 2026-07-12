from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def click_finish(self):
        finish_button = self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            finish_button
        )

        finish_button.click()