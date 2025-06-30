from playwright.sync_api import expect
from pageObjects.login_sign_up import LoginSignUpPage
from locators.home_page_locators import *
from config.config_automation_exe import ConfigInfo


class HomePage:

    def __init__(self, page):
        self.page = page
        self.locators = RoleLocators(self.page)
        self.pathLocators = PathLocators(self.page)

    def navigate(self):
        print(f"URL from config: {ConfigInfo.URL}") ## debug
        self.page.goto(ConfigInfo.URL)
        return self.page


    def varify_page_without_user_sign_in(self) -> None:
        expect(self.locators.BTN_TEST_CASE).to_be_visible()
        expect(self.locators.BTN_API_LIST).to_be_visible()


    def varify_page_with_user_sign_in(self, user_name):
        expect(self.pathLocators.USERNAME_XPATH).to_contain_text(user_name)


    def login_sign_up(self):
        self.locators.LINK_SIGNUP.click()
        loginSignUpPage = LoginSignUpPage(self.page)
        return loginSignUpPage


    def logout(self):
        #.fa.fa-lock: css path for locator
        self.locators.LINK_LOGOUT.click()


    def delete_user_and_varify_delete(self):
        self.locators.LINK_DELETE.click()
        expect(self.pathLocators.ACCOUNT_DELETE_CSS).to_contain_text("Account Deleted!")
        self.locators.LINK_CONTINUE.click()
        # we will have home page after this