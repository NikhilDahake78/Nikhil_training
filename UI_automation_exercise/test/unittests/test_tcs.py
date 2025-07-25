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


def test_varify(my_browser):
    homePage = HomePage(my_browser)
    homePage.navigate()
    testCasesPage = homePage.view_tests_cases()
    testCasesPage.verify()
    sleep(7)