import json
from time import sleep
from playwright.sync_api import Playwright, expect, Page
from pageObjects.home import HomePage
from pageObjects.login_sign_up import LoginSignUpPage
from utils.Logging import Log
from utils.user import *


def test_register_user(my_browser):
    user_id = "user_1"

    Log.title("test_register_user")
    Log.info(f"Creating User with user_id : {user_id}")

    # create user
    create_new_user(my_browser, user_id)

    Log.info("Deleting User")
    homePage = HomePage(my_browser)
    homePage.varify_page_with_user_sign_in(user_id)

    # delete user
    delete_user(my_browser, user_id)


def test_login_user_with_correct_credentials(my_browser):

    # create user
    user_id = "user_1"

    Log.title("test_login_user_with_correct_credentials")

    Log.info("Creating a user for testing.")
    create_new_user(my_browser, user_id)
    logout_user(my_browser, user_id)

    # login as created user
    Log.info(f"Logging in as {user_id}.")
    login_user(my_browser, user_id)

    # deleting user
    Log.info(f"Deleting user")
    delete_user(my_browser, user_id)


def test_user_delete(my_browser):
    user_id = "user_1"
    login_user(my_browser, user_id)
    delete_user(my_browser, user_id)