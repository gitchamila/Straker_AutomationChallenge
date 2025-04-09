import pytest
from pages.ContactPage import ContactPage

def test_contact_subscription(page):
    contact_page = ContactPage(page)

    contact_page.navigate()
    contact_page.click_contact_label()
    contact_page.find_email_subscription()
    contact_page.enter_email_address()
    contact_page.click_subscribe_button()
    contact_page.verification()

