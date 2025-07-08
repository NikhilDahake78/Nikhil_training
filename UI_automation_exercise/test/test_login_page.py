import json
from time import sleep

from playwright.sync_api import Playwright, expect, Page
from pageObjects.home import HomePage
from pageObjects.login_sign_up import LoginSignUpPage


def test_register_user(my_browser):
    user_id = "user_1"

    # home page navigation
    homePage = HomePage(my_browser)
    homePage.navigate()

    # home page validation
    homePage.varify_page_without_user_sign_in()

    # login/sign page
    loginSignUpPage = homePage.login_sign_up()
    loginSignUpPage.varify_new_user_option()

    # sign up page
    signUpPage = loginSignUpPage.new_user_sign_up(user_id)

    # sign up page varification and details filling
    signUpPage.page_varification()
    signUpPage.enter_user_details(user_id)

    # logged in page and varification
    signUpPage.varify_sign_up_and_continue()

    homePage = HomePage(my_browser)
    homePage.varify_page_with_user_sign_in(user_id)

    # delete user
    homePage.delete_user_and_varify_delete()


def test_login_user_with_correct_credentials(my_browser):

    # create user
    user_id = "user_1"

    userSignUp = LoginSignUpPage(my_browser)
    userSignUp.navigate()
    signUpPage = userSignUp.new_user_sign_up(user_id)
    signUpPage.enter_user_details(user_id)
    signUpPage.varify_sign_up_and_continue()

    # Logout
    homePage = HomePage(my_browser)
    homePage.logout()

    # navigate to home page
    homePage.navigate()
    homePage.varify_page_without_user_sign_in()

    # navigate to login page
    loginSignUpPage = homePage.login_sign_up()
    loginSignUpPage.varify_login_option()


    # log in
    loginSignUpPage.user_login(user_id)
    homePage = HomePage(my_browser)
    homePage.varify_page_with_user_sign_in(user_id)

    # delete user
    homePage.delete_user_and_varify_delete()