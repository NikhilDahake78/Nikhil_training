from time import sleep
from paramiko.auth_strategy import Password
from playwright.sync_api import Playwright, expect


def test_gmail_login(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://workspace.google.com/intl/en-US/gmail/")
    page.get_by_role('link', name='Sign into Gmail').click()

    page.locator('#identifierId').fill('nikhil.dahake@agiliad.com')
    page.locator('#identifierNext').click()
    page.wait_for_load_state()
    expect(page.locator('#headingText')).to_contain_text('Welcome')
    page.get_by_role('textbox', name='Enter your password').fill()
    page.get_by_role('button', name='Next').click()

    sleep(2)