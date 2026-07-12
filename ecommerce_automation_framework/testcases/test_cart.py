from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utilities.logger import Logger

logger = Logger.get_logger(__name__)


class TestCart:

    def test_open_cart(self, setup):
        driver = setup

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        cart = CartPage(driver)

        assert cart.get_cart_title() == "Your Cart"

    def test_verify_product(self, setup):
        driver = setup

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        cart = CartPage(driver)

        assert cart.get_product_name() == "Sauce Labs Backpack"

    def test_remove_product(self, setup):
        driver = setup

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        cart = CartPage(driver)
        cart.remove_product()

        assert cart.cart_badge_displayed() is False

        class TestCart:

            def test_open_cart(self, setup):
                logger.info("========== Cart Test Started ==========")

                driver = setup

                login = LoginPage(driver)
                login.login("standard_user", "secret_sauce")

                logger.info("Logged in")

                inventory = InventoryPage(driver)

                inventory.add_backpack()

                logger.info("Product Added")

                inventory.open_cart()

                logger.info("Cart Opened")

                cart = CartPage(driver)

                assert cart.get_cart_title() == "Your Cart"

                logger.info("Cart Test Passed")