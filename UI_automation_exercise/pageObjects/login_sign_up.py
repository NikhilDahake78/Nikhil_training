from pageObjects.sign_up import SignUpPage
from playwright.sync_api import expect
from locators.login_sign_up_locators import RoleLocators, PathLocators
from config.config_automation_exe import ConfigInfo
from data.user_data import UserData


class LoginSignUpPage:
    def __init__(self, page):
        self.page = page
        self.locators = RoleLocators(self.page)
        self.pathLocators = PathLocators(self.page)

    def navigate(self):
        self.page.goto(ConfigInfo().get_login_url())


    def new_user_sign_up(self, user_id):
        user_data = UserData(user_id)
        self.locators.NAME.fill(user_data.get('name'))
        self.locators.EMAIL_SIGHUP.fill(user_data.get('mail'))
        self.locators.BTN_SIGNUP.click()
        signUpPage = SignUpPage(self.page)
        return signUpPage


    def user_login(self, user_id):
        user_data = UserData(user_id)
        self.locators.EMAIL_LOGIN.fill(user_data.get('mail'))
        self.locators.PASSWORD.fill(user_data.get('password'))
        self.locators.BTN_LOGIN.click()


    def varify_new_user_option(self):
        expect(self.pathLocators.NEW_USER_TEXT_CSS).to_contain_text("New User Signup!")


    def varify_login_option(self):
        expect(self.pathLocators.LOGIN_TEXT_CSS).to_contain_text("Login to your account")