from time import sleep

from playwright.sync_api import Playwright, sync_playwright


def test_childWindowHandle(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # https://rahulshettyacademy.com/loginpagePractise/
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # for taking SS
    # page.screenshot(path="screenshot.png")


    # page.wait_for_load_state("domcontentloaded")

    page.locator("//div/input[@id='signInBtn']").click()

    sleep(2)