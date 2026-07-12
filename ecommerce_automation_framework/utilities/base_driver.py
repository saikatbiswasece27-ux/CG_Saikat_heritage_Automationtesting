from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from utilities.config_reader import ConfigReader


class BaseDriver:

    @staticmethod
    def get_driver():
        config = ConfigReader()

        browser = config.get_browser().lower()

        if browser == "chrome":
            options = Options()
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options
            )
        else:
            raise Exception(f"Browser '{browser}' is not supported.")

        driver.maximize_window()
        driver.implicitly_wait(config.get_implicit_wait())
        driver.get(config.get_base_url())

        return driver