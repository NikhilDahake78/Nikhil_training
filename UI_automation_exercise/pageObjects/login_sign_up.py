from pageObjects.sign_up import SignUpPage
from playwright.sync_api import expect
from locators.login_sign_up_locators import RoleLocators, PathLocators


class LoginSignUpPage:
    def __init__(self, page):
        self.page = page
        self.locators = RoleLocators(self.page)
        self.pathLocators = PathLocators(self.page)

    def navigate(self):
        self.page.goto("https://automationexercise.com/login")


    def new_user_sign_up(self, user_cred_list):
        self.locators.NAME.fill(user_cred_list['name'])
        self.locators.EMAIL_SIGHUP.fill(user_cred_list['mail'])
        self.locators.BTN_SIGNUP.click()
        signUpPage = SignUpPage(self.page)
        return signUpPage


    def user_login(self, mail, password):
        self.locators.EMAIL_LOGIN.fill(mail)
        self.locators.PASSWORD.fill(password)
        self.locators.BTN_LOGIN.click()


    def varify_new_user_option(self):
        expect(self.pathLocators.NEW_USER_TEXT_CSS).to_contain_text("New User Signup!")


    def varify_login_option(self):
        expect(self.pathLocators.LOGIN_TEXT_CSS).to_contain_text("Login to your account")