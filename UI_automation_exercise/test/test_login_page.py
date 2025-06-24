import json
from time import sleep

from playwright.sync_api import Playwright, expect, Page
from pageObjects.home import HomePage
from pageObjects.login_sign_up import LoginSignUpPage


with open('data/user_info.json') as f:
    test_data = json.load(f)
    # print('Inside open')
    global user_cred_list
    user_cred_list = test_data['user_credentials'][0]
    # print(user_cred_list)

def test_register_user(my_browser):

    homePage = HomePage(my_browser)
    homePage.navigate()

    # home page validation
    homePage.varify_page_without_user_sign_in()

    # login/sign page
    loginSignUpPage = homePage.login_sign_up()
    loginSignUpPage.varify_new_user_option()

    # sign up page
    signUpPage = loginSignUpPage.new_user_sign_up(user_cred_list)

    # sign up page varification and details filling
    signUpPage.page_varification()
    signUpPage.enter_user_details(user_cred_list)

    # logged in page and varification
    signUpPage.varify_sign_up_and_continue()

    homePage = HomePage(my_browser)
    homePage.varify_page_with_user_sign_in(user_cred_list['name'])

    # delete user
    homePage.delete_user_and_varify_delete()


def test_login_user_with_correct_credentials(my_browser):

    # create user
    userSignUp = LoginSignUpPage(my_browser)
    userSignUp.navigate()
    signUpPage = userSignUp.new_user_sign_up(user_cred_list)
    signUpPage.enter_user_details(user_cred_list)
    signUpPage.varify_sign_up_and_continue()

    # Logout
    homePage = HomePage(my_browser)
    homePage.logout()

    # navigate to home page
    # homePage = HomePage(my_browser)
    homePage.navigate()
    homePage.varify_page_without_user_sign_in()

    # navigate to login page
    loginSignUpPage = homePage.login_sign_up()
    loginSignUpPage.varify_login_option()

    mail = user_cred_list["mail"] # "nickD@gmail.com"
    password = user_cred_list["password"] # 'asdf'

    # log in
    loginSignUpPage.user_login(mail, password)
    homePage = HomePage(my_browser)
    homePage.varify_page_with_user_sign_in(user_cred_list["name"])

    # delete user
    homePage.delete_user_and_varify_delete()