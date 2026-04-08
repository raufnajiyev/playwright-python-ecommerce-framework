from pages.base_page import BasePage


class CheckoutPage(BasePage):
    PAGE_TITLE = "[data-test='title']"
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    ERROR_MESSAGE = "[data-test='error']"

    def get_page_title_text(self):
        return self.page.locator(self.PAGE_TITLE).text_content()

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.page.fill(self.FIRST_NAME_INPUT, first_name)
        self.page.fill(self.LAST_NAME_INPUT, last_name)
        self.page.fill(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        self.page.click(self.CONTINUE_BUTTON)

    def get_error_message(self):
        return self.page.locator(self.ERROR_MESSAGE).text_content()