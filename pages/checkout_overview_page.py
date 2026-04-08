from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    PAGE_TITLE = "[data-test='title']"
    FINISH_BUTTON = "#finish"

    def get_page_title_text(self):
        return self.page.locator(self.PAGE_TITLE).text_content()

    def click_finish(self):
        self.page.click(self.FINISH_BUTTON)