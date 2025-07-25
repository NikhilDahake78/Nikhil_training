from random import choices
import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def firefox_setup(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    firefox_page = browser.new_page()
    return  firefox_page


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="browser selection",
        choices=('chrome', 'firefox')
    )

@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == 'chrome':
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()


# @pytest.fixture(scope="session")
# def userCredentials(request):
#     return request.params