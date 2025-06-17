from tkinter.font import names

import pytest
from playwright.sync_api import Page, expect, Playwright
import time


def test_playwright(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")


# page is for directly running test on chromium single context env.
def test_shortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")


def test_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # for using get_by_label, input field eg. input box should be wrapped inside lable tag or it should
    # have refence
    # < label
    # for ="username" class ="text-white" > Username:< / label >
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")


    # Css selector syntax: '#<id>'  OR '.<class name>' OR tegName
    # page.locator("#terms").click()
    page.get_by_role('checkbox', name='terms').click()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

@pytest.mark.negative
def test_wrong_login(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learnsssing123")
    page.get_by_role("button", name="Sign In").click()

    # error msg: Incorrect username/password.
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


def test_firefox_browser(firefox_setup):
    page = firefox_setup

    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning123")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)



