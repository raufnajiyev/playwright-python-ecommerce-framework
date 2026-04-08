import pytest
from pages.login_page import LoginPage
from data.test_data import VALID_USERNAME, VALID_PASSWORD


@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.open("https://www.saucedemo.com/")
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return page