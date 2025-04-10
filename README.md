# Playwright Python Test Framework

This repository contains a Playwright Python test automation framework for testing the Straker.ai website. The framework follows best practices for test automation, including page object model pattern, logging, and screenshot generation on test failures.

## Project Structure

```
project_root/
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitattributes
├── logs/
│   └── test_log.log
├── assets
│   └── style.css
├── utils/
│   ├── conftest.py
│   └── result.py
│   └── logger.py
├── pages/
│   ├── __init__.py
│   ├── basepage.py
│   ├── homepage.py
│   ├── productspage.py
│   └── contactpage.py
└── tests/
    ├── __init__.py
    ├── test_product_navigation.py
    └── test_contact_subscription.py

## Features

- **Page Object Model**: Separation of test logic from page interactions
- **Logging**: Comprehensive logging for test execution and debugging
- **Screenshot Generation**: Automatic screenshots on test failures
- **Configurable**: Easy configuration for different environments
- **Pytest Integration**: Leveraging pytest fixtures and hooks

## Setup Instructions

1. Ensure you have Python 3.12 installed.
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Install Playwright browsers:
   ```
   playwright install
   
## Running Tests
To run all tests:
```
pytest --html=report/my_report.html 
```

To run a specific test:
```
pytest tests/test_contact_subscription.py --html=report/my_report.html
pytest tests/test_product_navigation.py --html=report/my_report.html
```

How to open my_report.html report:
```
After executing the test cases (either all tests or specific ones), a test report named my_report.html will be generated in the report of the project.

To view the test report:

1.Locate the my_report.html file in the project root.
2.Right-click on the file.
3.Navigate to: Open in > Browser > [Select your preferred browser]

Note: Ensure your development environment supports "Open in Browser" functionality (e.g., VS Code with the appropriate extension).
```

## Test Scenarios

### Scenario 1: Navigate to the Tiri Product Page
1. Open a web browser and navigate to https://straker.ai/.
2. Locate the "Products" link in the main navigation bar.
3. Interact with the "Products" link to reveal its dropdown/submenu.
4. Within the "Products" section (specifically under the "Tiri" product), find and click the "Learn more" button.
5. Verify that the browser has navigated to the correct Tiri product page.

### Scenario 2: Subscribe to Email Updates on Contact Page
1. Open a web browser and navigate to https://straker.ai/.
2. Locate and click the "Contact" link in the main navigation bar.
3. On the Contact page, find the email subscription form.
4. Enter a test email address into the email input field.
5. Click the "Subscribe" or equivalent button.
6. Verify that some indication of successful subscription occurs.

## Best Practices Implemented

1. **Robust Selectors**: Using descriptive and reliable selectors
2. **Explicit Waits**: Proper waiting mechanisms for dynamic elements
3. **Error Handling**: Comprehensive error handling and reporting
4. **Screenshots**: Automatic screenshot capture on test failures
5. **Page Object Model**: Clean separation of concerns
6. **Configuration Management**: Externalized configuration
7. **Test Independence**: Each test is independent and can run in isolation

## Extending the Framework

To add new tests:
1. Create page objects for new pages in the `pages` directory
2. Add new test files in the `tests` directory
3. Update configuration if needed

## Reporting

Test results are available in the console output and in the pytest-html report generated after test execution.
