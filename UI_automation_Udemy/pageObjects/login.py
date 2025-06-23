from playwright.sync_api import expect
from pageObjects.dashboard import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        #  https://rahulshettyacademy.com/loginpagePractise/
        self.page.goto("https://rahulshettyacademy.com/client")


    def login(self, user, password):
        self.page.get_by_placeholder('email@example.com').fill(user)
        self.page.get_by_placeholder("enter your passsword").fill(password)
        self.page.get_by_role('button', name='login').click()

        dashboardPage = DashboardPage(self.page)
        return dashboardPage


    def validate_login(self):
        expect(self.page.locator('.container')).to_contain_text('User can only see maximum 9 products on a page')
