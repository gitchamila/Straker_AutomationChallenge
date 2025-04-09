from playwright.sync_api import Page
from pages.BasePage import BasePage
from playwright.sync_api import expect
from utils.conftest import logger

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.products_link = page.get_by_role("button", name="Products")
        self.learn_more_button = page.locator("#w-dropdown-list-5").get_by_role("link", name="Learn More")

    def navigate_straker(self):
        try:
            self.page.goto("/",timeout=10000)
            logger.info("Homepage loaded successfully.")
        except TimeoutError:
            raise Exception("Failed to load the homepage within the timeout.")

    def mouse_hover_to_product_tab(self):
        try:
            products_tab = self.page.get_by_role("button", name="Products")
            expect(products_tab).to_be_visible()
            expect(products_tab).to_contain_text("Products")
            self.products_link.hover()

            expect(self.page.locator("#w-dropdown-list-5")).to_contain_text("tiri")
            expect(self.learn_more_button).to_be_visible()
            logger.info("Clicking the 'Learn More' button.")
            self.learn_more_button.click()

        except Exception as e:
            logger.error(f"Error occurred: {str(e)}")
            self.page.take_screenshot_on_failure(test_name="Learn_more_failure")  # Capture screenshot on failure
            raise Exception("Failed to locate or interact with 'Learn more' under Products")

