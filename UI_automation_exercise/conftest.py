import pytest
from playwright.sync_api import Playwright


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default='chrome',
        help="browser selection",
        choices=('chrome', 'firefox')
    )
    parser.addoption(
        "--headless",
        action="store",
        default="True",
        help="headless_status",
        choices=("True", "False")
    )


@pytest.fixture
def my_browser(playwright, request):
    browser_name = request.config.getoption("browser_name")
    headless_status = True if request.config.getoption("headless") == "True" else False

    if browser_name == 'chrome':
        browser = playwright.chromium.launch(headless=headless_status)
    elif browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=headless_status)

    context = browser.new_context()
    page = context.new_page()

    yield page

    page.close()
    context.close()
    browser.close()