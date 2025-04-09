import pytest
from playwright.sync_api import Page, expect
from playwright.sync_api import expect
from pages.BasePage import BasePage
from utils.conftest import logger

class ContactPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Selectors for Contact page
        self.contact_link = page.get_by_role("link", name="Contact")
        self.email_subscription_textbox = page.get_by_role("textbox", name="Enter your email")
        self.subscribe_button = page.get_by_role("button", name="Subscribe")
        self.success_message = page.get_by_role("region", name="Email Form success")

#Open a web browser and navigate to URL
    def navigate(self):
        try:
            self.page.goto("/",timeout=10000)
            logger.info("Homepage loaded successfully.")
        except TimeoutError:
            logger.error("Failed to load the homepage within the timeout.")
            raise Exception("Failed to load the homepage within the timeout.")

#After land to home page click contact label
    def click_contact_label(self):
        try:
            expect(self.contact_link).to_contain_text("Contact")
            self.contact_link.click()
            logger.info("Contact label clicked successfully.")
        except TimeoutError:
            logger.error("Failed to click contact label.")
            raise Exception("Failed to Click contact label.")

#Fine the email subscription location
    def find_email_subscription(self):
        try:
            self.email_subscription_textbox.is_visible()
            self.email_subscription_textbox.click()
            logger.info("Email subscription text box found and clicked.")
        except TimeoutError:
            logger.error("Failed to find email subscription text box.")
            raise Exception("Failed to find email subscription text box.")

#Enter the Email
    def enter_email_address(self):
        self.email_subscription_textbox.fill("Chamilalook@gmail.com")
        logger.info("Email address entered.")

#Verify that subscribe button visible and Click on it
    def click_subscribe_button(self):
        try:
            expect(self.subscribe_button).to_contain_text("Subscribe")
            self.subscribe_button.click()
            logger.info("Subscribe button clicked successfully.")
        except TimeoutError:
            logger.error("Failed to click subscribe button.")
            raise Exception("Failed to Click subscribe button.")

#Verifications
    def verification(self):
       try:
            logger.info("Verifying success message visibility and text.")
            expect(self.success_message).to_be_visible()  # Verify that the success message is visible
            expect(self.success_message).to_contain_text("Thank you! You're successfully subscribed!")
            expect(self.email_subscription_textbox).not_to_be_visible()  # Check if the input field is cleared
            logger.info("Verification passed.")
       except Exception as e:
            logger.error(f"Verification failed: {str(e)}")
            self.page.take_screenshot_on_failure(test_name="verification_failure")  # Capture screenshot on failure
            raise e