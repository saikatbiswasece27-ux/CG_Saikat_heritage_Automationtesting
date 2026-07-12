from selenium.webdriver.common.by import By


class BrowserPage:

    # DemoQA
    double_click_button = (By.ID, "doubleClickBtn")
    right_click_button = (By.ID, "rightClickBtn")

    double_click_message = (By.ID, "doubleClickMessage")
    right_click_message = (By.ID, "rightClickMessage")

    # Heroku Alerts
    js_alert = (By.XPATH, "//button[text()='Click for JS Alert']")
    js_confirm = (By.XPATH, "//button[text()='Click for JS Confirm']")
    js_prompt = (By.XPATH, "//button[text()='Click for JS Prompt']")

    result = (By.ID, "result")

    def __init__(self, driver):
        self.driver = driver