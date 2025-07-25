"""
This is unit tests home page.
"""
import json
import time
from time import sleep
from playwright.sync_api import Playwright, expect, Page
from pageObjects.home import HomePage
from pageObjects.login_sign_up import LoginSignUpPage
from utils.Logging import Log
from utils.user import user
from config.config_automation_exe import ConfigInfo


def test_contact_us(my_browser):
    Log.info('Unit test- Home page : test_contact_us')

    homePage = HomePage(my_browser)
    homePage.navigate()
    contactUsPage = homePage.view_contact_us()
    contactUsPage.validate()


def test_subscribe(my_browser):
    # page.goto("http://automationexercise.com")

    # page.get_by_placeholder("Your email address").fill("abcd@g.com")
    # # page.get_by_role('button', name="subscribe").click(timeout=4000)
    # page.locator(".fa.fa-arrow-circle-o-right").click()
    # expect(page.locator("#success-subscribe")).to_have_text("You have been successfully subscribed!")
    # time.sleep(3)
    homePage = HomePage(my_browser)
    homePage.navigate()
    homePage.subscribe_user("user_1")


def test_select_product(my_browser):
    # page.goto("http://automationexercise.com")
    # product_list = page.locator(".features_items")
    # print(f"product_list: {product_list}")
    # item = product_list.locator(".col-sm-4").filter(has_text="Fancy Green Top")
    # print(f"Blue Top : {item}" )
    # item.get_by_role("link", name="View Product").click()
    # time.sleep(3)
    homePage = HomePage(my_browser)
    homePage.navigate()
    productPage = homePage.see_product('Blue Top')
    time.sleep(3)

