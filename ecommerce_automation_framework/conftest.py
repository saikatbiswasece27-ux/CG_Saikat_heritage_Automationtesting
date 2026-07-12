import pytest

from utilities.base_driver import BaseDriver
from utilities.screenshot import Screenshot


@pytest.fixture(scope="function")
def setup(request):
    driver = BaseDriver.get_driver()

    request.cls.driver = driver

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("setup")

        if driver:
            Screenshot.capture(driver, item.name)