from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM_NAME = "[data-test='inventory-item-name']"
    CHECKOUT_BUTTON = "#checkout"

    def get_cart_item_name(self):
        return self.page.locator(self.CART_ITEM_NAME).text_content()

    def click_checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)