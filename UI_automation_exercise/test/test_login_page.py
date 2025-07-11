import json
from time import sleep
from playwright.sync_api import Playwright, expect, Page
from pageObjects.home import HomePage
from pageObjects.login_sign_up import LoginSignUpPage
from utils.Logging import Log


def test_register_user(my_browser):
    user_id = "user_1"

    Log.title("test_register_user")
    Log.info(f"Creating User with user_id : {user_id}")

    # home page navigation
    Log.info("Navigating to Base url")
    homePage = HomePage(my_browser)
    homePage.navigate()

    # home page validation
    Log.info("Home page Validation")
    homePage.varify_page_without_user_sign_in()

    # login/sign page
    Log.info("Signing In..")
    loginSignUpPage = homePage.login_sign_up()
    loginSignUpPage.varify_new_user_option()

    # sign up page
    signUpPage = loginSignUpPage.new_user_sign_up(user_id)

    # sign up page varification and details filling
    signUpPage.page_varification()
    signUpPage.enter_user_details(user_id)

    # logged in page and varification
    signUpPage.varify_sign_up_and_continue()
    Log.info("Signed Up successfully")

    Log.info("Deleting User")
    homePage = HomePage(my_browser)
    homePage.varify_page_with_user_sign_in(user_id)


    # delete user
    Log.info("User deleted Successfully")
    homePage.delete_user_and_varify_delete()


def test_login_user_with_correct_credentials(my_browser):

    # create user
    user_id = "user_1"

    Log.title("test_login_user_with_correct_credentials")

    # home page navigation
    Log.info(f"Creating User with user_id : {user_id}")
    Log.info("Navigating to Base url")
    userSignUp = LoginSignUpPage(my_browser)
    userSignUp.navigate()
    signUpPage = userSignUp.new_user_sign_up(user_id)
    signUpPage.enter_user_details(user_id)
    signUpPage.varify_sign_up_and_continue()

    # Logout
    Log.info(f"Logging out..")
    homePage = HomePage(my_browser)
    homePage.logout()

    # navigate to home page
    Log.info(f"Navigating to Home page for Login")
    homePage.navigate()
    homePage.varify_page_without_user_sign_in()

    # navigate to login page
    Log.info(f"Logging in with user: {user_id}")
    loginSignUpPage = homePage.login_sign_up()
    loginSignUpPage.varify_login_option()

    # log in
    loginSignUpPage.user_login(user_id)
    homePage = HomePage(my_browser)
    homePage.varify_page_with_user_sign_in(user_id)
    Log.info(f"Logged in successfully.")

    # delete user
    Log.info(f"Deleting user")
    homePage.delete_user_and_varify_delete()