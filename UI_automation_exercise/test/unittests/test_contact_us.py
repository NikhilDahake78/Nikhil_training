"""
"""
import json
from time import sleep
from playwright.sync_api import Playwright, expect, Page
from pageObjects.home import HomePage
from pageObjects.login_sign_up import LoginSignUpPage
from utils.Logging import Log
from utils.user import user
from config.config_automation_exe import ConfigInfo
import os

def test_fill_user_details(my_browser):

    homePage = HomePage(my_browser)
    homePage.navigate()

    contactUsPage = homePage.view_contact_us()

    contactUsPage.validate()

    pwd = os.getcwd()
    path= os.path.join(pwd, 'test_file.txt')

    page = contactUsPage.submit_details('user_1', file_path=path)
    homePage = HomePage(page)
    homePage.varify_page_without_user_sign_in()

    # page.goto("https://automationexercise.com/contact_us")
    # page.get_by_placeholder("Name").fill("This is dummy test")
    # page.get_by_placeholder("Email", exact=True).fill("nickdam@gmail.com")
    # page.get_by_placeholder("Subject").fill("slow working.")
    # page.get_by_placeholder("Your Message Here").fill("NA")

    # test_file_path = Path("test_file.txt")
    # if not test_file_path.exists():
    #     test_file_path.write_text("This is a test file.")


    # def run(playwright: Playwright) -> None:
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("https://automationexercise.com/contact_us")
    # page.get_by_role("textbox", name="Name").click()
    # page.get_by_role("textbox", name="Name").fill("avb")
    # page.get_by_role("textbox", name="Email", exact=True).click()
    # page.get_by_role("textbox", name="Email", exact=True).fill("abc@gmail.com")
    # page.once("dialog", lambda dialog: dialog.dismiss())
    # page.get_by_role("button", name="Submit").click()
    # page.get_by_role("link", name=" Home").click()


    # print(f"test_file_path: {path}")
    # page.locator("//div/input[@type='file']").set_input_files(path)
    #
    # page.once("dialog", lambda dialog: dialog.dismiss())
    # page.get_by_role('button', name='submit').click()
    #
    # page.get_by_role("link", name=" Home").click()

    sleep(5)