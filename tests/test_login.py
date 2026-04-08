from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.test_data import VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME


# Verify that a valid user can log in successfully
def test_user_can_login_with_valid_credentials(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open("https://www.saucedemo.com/")
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    assert "inventory" in page.url
    assert inventory_page.get_page_title_text() == "Products"


# Verify that an invalid user sees an error message
def test_user_sees_error_with_invalid_credentials(page):
    login_page = LoginPage(page)

    login_page.open("https://www.saucedemo.com/")
    login_page.login(INVALID_USERNAME, VALID_PASSWORD)

    assert "Epic sadface" in login_page.get_error_message()