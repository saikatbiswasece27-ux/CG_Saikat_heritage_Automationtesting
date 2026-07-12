from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:

    def test_inventory_page(self, setup):
        driver = setup

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)

        assert inventory.get_page_title() == "Products"

    def test_add_single_product(self, setup):
        driver = setup

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)

        inventory.add_backpack()

        assert inventory.get_cart_count() == "1"

    def test_add_two_products(self, setup):
        driver = setup

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)

        inventory.add_backpack()
        inventory.add_bike_light()

        assert inventory.get_cart_count() == "2"