from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    PAGE_TITLE = "[data-test='title']"
    COMPLETE_HEADER = "[data-test='complete-header']"

    def get_page_title_text(self):
        return self.page.locator(self.PAGE_TITLE).text_content()

    def get_complete_header_text(self):
        return self.page.locator(self.COMPLETE_HEADER).text_content()