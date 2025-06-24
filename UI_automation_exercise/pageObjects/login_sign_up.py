from pageObjects.sign_up import SignUpPage
from playwright.sync_api import expect

import time


class LoginSignUpPage:
    def __init__(self, page):
        self.page = page


    def navigate(self):
        self.page.goto("https://automationexercise.com/login")


    def new_user_sign_up(self, user_cred_list):
        self.page.get_by_placeholder("Name").fill(user_cred_list['name'])
        self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill(user_cred_list['mail'])
        self.page.get_by_role('button', name="Signup").click()
        signUpPage = SignUpPage(self.page)
        return signUpPage


    def user_login(self, mail, password):
        self.page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill(mail)
        self.page.get_by_placeholder("Password").fill(password)
        time.sleep(3)
        self.page.get_by_role("button", name="Login").click()



    def varify_new_user_option(self):
        expect(self.page.locator('.signup-form')).to_contain_text("New User Signup!")


    def varify_login_option(self):
        expect(self.page.locator('.login-form')).to_contain_text("Login to your account")