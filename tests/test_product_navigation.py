import pytest
from pages.HomePage import HomePage
from pages.ProductPage import ProductPage


def test_navigate_to_product_page(page):
    home_page = HomePage(page)
    product_page = ProductPage(page)

    home_page.navigate_straker()                    #Navigate to the straker home page
    home_page.mouse_hover_to_product_tab()          #Locate and hover over the Products link to Click on Learn More button
    product_page.verify_product_tiri_page()         #Verify navigation to Tiri product page
