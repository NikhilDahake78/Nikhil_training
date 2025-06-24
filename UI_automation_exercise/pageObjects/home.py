from playwright.sync_api import expect
from pageObjects.login_sign_up import LoginSignUpPage


class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("http://automationexercise.com")
        return self.page


    def varify_page_without_user_sign_in(self) -> None:
        expect(self.page.get_by_role('button', name='Test Cases')).to_be_visible()
        expect(self.page.get_by_role('button', name='APIs list for practice')).to_be_visible()


    def varify_page_with_user_sign_in(self, user_name):
        expect(self.page.locator("//a/i[@class='fa fa-user']/following-sibling::b")).to_contain_text(user_name)


    def login_sign_up(self):
        self.page.get_by_role('link', name=" Signup / Login").click()
        loginSignUpPage = LoginSignUpPage(self.page)
        return loginSignUpPage


    def logout(self):
        #.fa.fa-lock: css path for locator
        self.page.get_by_role("link", name=" Logout").click()


    def delete_user_and_varify_delete(self):
        self.page.get_by_role('link', name=" Delete Account").click()
        expect(self.page.locator('.title.text-center')).to_contain_text("Account Deleted!")
        self.page.get_by_role('link', name="Continue").click()
        # we will have home page after this