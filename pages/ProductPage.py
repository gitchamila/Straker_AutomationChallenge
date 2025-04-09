from playwright.sync_api import expect
from pages.BasePage import BasePage


class ProductPage(BasePage):
    def verify_product_tiri_page(self):
        try:
            expect(self.page).to_have_url("https://www.straker.ai/products/tiri")
            expect(self.page.locator("#nve")).to_contain_text("tiri")
        except TimeoutError:
            raise Exception("Failed to navigate tiri page")

