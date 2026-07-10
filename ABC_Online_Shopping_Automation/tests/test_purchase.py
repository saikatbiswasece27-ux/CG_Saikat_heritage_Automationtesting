from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_product_purchase(setup):
    driver = setup

    # Page Objects
    login = LoginPage(driver)
    product = ProductsPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Open Website
    login.open_url()

    # Login
    login.login("standard_user", "secret_sauce")

    # Sort products (Low to High)
    product.sort_low_to_high()

    # Add Backpack to Cart
    product.add_backpack_to_cart()

    # Open Cart
    product.open_cart()

    # Verify Product
    assert cart.verify_product() == "Sauce Labs Backpack"

    # Checkout
    cart.click_checkout()

    # Enter Customer Details
    checkout.enter_customer_details(
        "Saikat",
        "Biswas",
        "700001"
    )

    # Continue
    checkout.continue_checkout()

    print("Current URL:", driver.current_url)
    print("Page Title:", driver.title)

    assert "checkout-step-two" in driver.current_url

    checkout.finish_order()

    # Verify Order Success
    success = checkout.get_success_message()

    assert success == "Thank you for your order!"

    print("Purchase Successful")

    assert success == "Thank you for your order!"

    print("Purchase Successful")