from pages.login_page import LoginPage
from utilities.logger import Logger

logger = Logger.get_logger(__name__)


class TestLogin:

    def test_valid_login(self, setup):
        logger.info("===== Valid Login Test Started =====")

        driver = setup
        login_page = LoginPage(driver)

        login_page.login("standard_user", "secret_sauce")

        assert "inventory" in driver.current_url

        logger.info("===== Valid Login Test Passed =====")

    def test_invalid_login(self, setup):
        logger.info("===== Invalid Login Test Started =====")

        driver = setup
        login_page = LoginPage(driver)

        login_page.login("invalid_user", "wrong_password")

        assert "Username and password do not match" in login_page.get_error_message()

        logger.info("===== Invalid Login Test Passed =====")

    def test_empty_username(self, setup):
        logger.info("===== Empty Username Test Started =====")

        driver = setup
        login_page = LoginPage(driver)

        login_page.login("", "secret_sauce")

        assert "Username is required" in login_page.get_error_message()

        logger.info("===== Empty Username Test Passed =====")

    def test_empty_password(self, setup):
        logger.info("===== Empty Password Test Started =====")

        driver = setup
        login_page = LoginPage(driver)

        login_page.login("standard_user", "")

        assert "Password is required" in login_page.get_error_message()

        logger.info("===== Empty Password Test Passed =====")

    def test_locked_user(self, setup):
        logger.info("===== Locked User Test Started =====")

        driver = setup
        login_page = LoginPage(driver)

        login_page.login("locked_out_user", "secret_sauce")

        assert "Sorry, this user has been locked out." in login_page.get_error_message()

        logger.info("===== Locked User Test Passed =====")