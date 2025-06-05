import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def firefox_setup(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    firefox_page = browser.new_page()
    return  firefox_page