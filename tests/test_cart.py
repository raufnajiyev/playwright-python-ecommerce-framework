from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


# Verify that a logged-in user can add a product to the cart
def test_user_can_add_product_to_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_badge_text() == "1"


# Verify that the correct product appears in the cart
def test_user_can_open_cart_and_see_correct_product(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    assert cart_page.get_cart_item_name() == "Sauce Labs Backpack"


# Verify that removing a product makes the cart empty
def test_user_can_remove_product_from_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.remove_backpack_from_cart()

    assert logged_in_page.locator(inventory_page.CART_BADGE).count() == 0