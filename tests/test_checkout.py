from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from data.test_data import (
    CHECKOUT_FIRST_NAME,
    CHECKOUT_LAST_NAME,
    CHECKOUT_POSTAL_CODE,
)


# Verify that the user can open the checkout information page
def test_user_can_open_checkout_page(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()

    assert checkout_page.get_page_title_text() == "Checkout: Your Information"


# Verify that the user can fill checkout details and continue
def test_user_can_fill_checkout_information(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)
    checkout_overview_page = CheckoutOverviewPage(logged_in_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()

    checkout_page.fill_checkout_information(
        CHECKOUT_FIRST_NAME,
        CHECKOUT_LAST_NAME,
        CHECKOUT_POSTAL_CODE
    )
    checkout_page.click_continue()

    assert checkout_overview_page.get_page_title_text() == "Checkout: Overview"


# Verify that the user can complete the full checkout process
def test_user_can_complete_checkout(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)
    checkout_overview_page = CheckoutOverviewPage(logged_in_page)
    checkout_complete_page = CheckoutCompletePage(logged_in_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()

    checkout_page.fill_checkout_information(
        CHECKOUT_FIRST_NAME,
        CHECKOUT_LAST_NAME,
        CHECKOUT_POSTAL_CODE
    )
    checkout_page.click_continue()
    checkout_overview_page.click_finish()

    assert checkout_complete_page.get_page_title_text() == "Checkout: Complete!"
    assert checkout_complete_page.get_complete_header_text() == "Thank you for your order!"


# Verify that an error appears when checkout fields are empty
def test_user_sees_error_when_checkout_fields_are_empty(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()

    checkout_page.click_continue()

    assert "Error" in checkout_page.get_error_message()