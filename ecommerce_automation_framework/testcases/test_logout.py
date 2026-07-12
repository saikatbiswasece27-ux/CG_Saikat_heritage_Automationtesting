from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogout:

    def test_logout(self, setup):
        driver = setup

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)

        inventory.open_menu()
        inventory.logout()

        assert "saucedemo.com" in driver.current_url
        assert "Swag Labs" in driver.title