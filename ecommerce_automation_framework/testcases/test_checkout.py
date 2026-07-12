from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.complete_page import CompletePage


class TestCheckout:

    def test_complete_checkout(self, setup):
        driver = setup

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        cart = CartPage(driver)
        cart.click_checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_checkout_details(
            "Saikat",
            "Biswas",
            "700001"
        )

        checkout.click_continue()
        print("Current URL:", driver.current_url)
        print("Current Title:", driver.title)

        overview = CheckoutOverviewPage(driver)

        assert overview.get_title() == "Checkout: Overview"

        overview.click_finish()

        complete = CompletePage(driver)

        assert complete.get_confirmation_message() == "Thank you for your order!"