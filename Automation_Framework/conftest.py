import pytest
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs["setup"]

        os.makedirs("screenshots", exist_ok=True)

        driver.save_screenshot(
            f"screenshots/{item.name}.png"
        )

# Configure logging
logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


@pytest.fixture
def setup():

    logging.info("Browser launched")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.maximize_window()

    yield driver

    logging.info("Browser closed")

    driver.quit()