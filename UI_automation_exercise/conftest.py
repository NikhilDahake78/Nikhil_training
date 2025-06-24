import pytest


@pytest.fixture
def my_browser(playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    yield page

    page.close()
    context.close()
    browser.close()