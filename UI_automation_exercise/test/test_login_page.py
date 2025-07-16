"""
This is tests file.
"""
import json
from time import sleep
from playwright.sync_api import Playwright, expect, Page
from pageObjects.home import HomePage
from pageObjects.login_sign_up import LoginSignUpPage
from utils.Logging import Log
from utils.user import user


def test_register_user(my_browser):
    """ test 1"""
    user_id = "user_1"

    Log.title("test_register_user")
    Log.info(f"Creating User with user_id : {user_id}")

    # create user
    user.create_new_user(my_browser, user_id)

    Log.info("Deleting User")
    homePage = HomePage(my_browser)
    homePage.varify_page_with_user_sign_in(user_id)

    # delete user
    user.delete_user(my_browser, user_id)


def test_login_user_with_correct_credentials(browser_with_user):
    """ test 2"""

    # create user
    user_id = "user_1"

    Log.title("test_login_user_with_correct_credentials")

    # login as created user
    Log.info(f"Logging in as {user_id}.")
    user.login_user(browser_with_user, user_id)

    # deleting user
    Log.info(f"Deleting user")
    user.delete_user(browser_with_user, user_id)


def test_logout_user(browser_with_user):
    """ test 4"""
    user_id = "user_1"

    Log.title("Test user logout")

    # login as created user
    Log.info(f"Logging in as {user_id}.")
    user.login_user(browser_with_user, user_id)

    # logout user
    Log.info(f"logging out as {user_id} ")
    user.logout_user(browser_with_user)

    # check
    Log.info("Varifying if login page is visible after logout.")
    loginPage = LoginSignUpPage(browser_with_user)
    loginPage.varify_login_option()

    # test result
    Log.info('\t\tTest passed.')


def test_user_delete(browser_with_user):
    """ """
    user_id = "user_1"
    user.login_user(browser_with_user, user_id)
    user.delete_user(browser_with_user, user_id)
