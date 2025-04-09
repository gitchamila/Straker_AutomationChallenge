import pytest
from playwright.sync_api import sync_playwright
import os
from utils.logger import get_logger
from pathlib import Path
from datetime import datetime

# Initialize logger
logger = get_logger()

def pytest_addoption(parser):
    parser.addini("base_url", "Base URL for the tests")

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getini("base_url")

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(base_url=base_url)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results and take screenshots on failure.
    """
    outcome = yield
    report = outcome.get_result()

    # Only take screenshots for failed tests during the call phase
    if report.when == "call" and report.failed:
        try:
            # Get the page fixture if available
            page = item.funcargs.get("page")
            if page:
                # Create screenshots directory if it doesn't exist
                screenshots_dir = Path(__file__).parent / "screenshots"
                screenshots_dir.mkdir(exist_ok=True)

                # Generate a unique filename for the screenshot
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                test_name = item.name
                screenshot_path = screenshots_dir / f"{test_name}_{timestamp}_failure.png"

                # Take screenshot
                page.screenshot(path=str(screenshot_path))
                #logger.info(f"Screenshot saved to {screenshot_path}")

                # Attach screenshot to the report
                report.screenshot = str(screenshot_path)
        except Exception as e:
            logger.error(f"Failed to take screenshot: {str(e)}")
            logger.exception(e)


