from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = "[data-test='title']"
    ADD_BACKPACK_BUTTON = "#add-to-cart-sauce-labs-backpack"
    REMOVE_BACKPACK_BUTTON = "#remove-sauce-labs-backpack"
    CART_BADGE = "[data-test='shopping-cart-badge']"
    CART_LINK = "[data-test='shopping-cart-link']"

    def get_page_title_text(self):
        return self.page.locator(self.PAGE_TITLE).text_content()

    def add_backpack_to_cart(self):
        self.page.click(self.ADD_BACKPACK_BUTTON)

    def remove_backpack_from_cart(self):
        self.page.click(self.REMOVE_BACKPACK_BUTTON)

    def get_cart_badge_text(self):
        return self.page.locator(self.CART_BADGE).text_content()

    def open_cart(self):
        self.page.click(self.CART_LINK)