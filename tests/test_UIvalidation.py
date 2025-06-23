import time

import pytest
from playwright.sync_api import Page, expect, Playwright
from pytest_playwright.pytest_playwright import launch_browser

from pageObjects.login import LoginPage


def test_UIvalidation_dynamic(page:Page, browserInstance):

    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label('Username:').fill("rahulshettyacademy")
    page.get_by_label('Password:').fill('learning')
    page.get_by_role('combobox').select_option('teach')
    page.get_by_role('checkbox', name='terms').click()
    page.get_by_role('link', name= 'terms and conditions').click()
    page.get_by_role('button', name='Sign In').click()

    # LoginPage.login(browserInstance)

    iphone_obj = page.locator('app-card').filter(has_text='iphone X')
    iphone_obj.get_by_role('button').click()

    nokia_obj = page.locator('app-card').filter(has_text='Nokia Edge')
    nokia_obj.get_by_role('button').click()

    page.get_by_text('Checkout ').click()
    expect(page.locator('.media')).to_have_count(2)

# tagging concept: to run use:  --negative
@pytest.mark.negative
def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # page.wait_for_timeout(3000)


    with page.expect_popup() as new_page:
        page.get_by_role('link', name='Free Access to InterviewQues/ResumeAssistance/Material').click()
        childPage = new_page.value
        text = childPage.locator('.red').text_content()
        print(text)
        assert 'mentor@rahulshettyacademy.com' in text

