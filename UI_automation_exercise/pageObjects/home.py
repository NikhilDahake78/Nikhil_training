import time
from time import sleep

from playwright.sync_api import expect
from pageObjects.login_sign_up import LoginSignUpPage
from pageObjects.contact_us import ContactUsPage
from pageObjects.tests_cases import TestsCasesPage
from pageObjects.cart import CartPage
from pageObjects.product import ProductPage
from locators.home_page_locators import *
from config.config_automation_exe import ConfigInfo
from data.user_data import UserData


class HomePage:

    def __init__(self, page):
        self.page = page
        self.locators = RoleLocators(self.page)
        self.pathLocators = PathLocators(self.page)

    def navigate(self):
        self.page.goto(ConfigInfo().get_home_url())
        return self.page


    def varify_page_without_user_sign_in(self) -> None:
        expect(self.locators.BTN_TEST_CASE).to_be_visible()
        expect(self.locators.BTN_API_LIST).to_be_visible()


    def varify_page_with_user_sign_in(self, user_id):
        expect(self.pathLocators.USERNAME_XPATH).to_contain_text(UserData(user_id).get('name'))


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


    def view_contact_us(self):
        self.locators.LINK_CONTACT_US.click()
        contactUsPage = ContactUsPage(self.page)
        return contactUsPage


    def view_tests_cases(self):
        self.locators.BTN_TEST_CASE.click()
        testsCasesPage = TestsCasesPage(self.page)
        return testsCasesPage


    def view_product(self):
        self.locators.LINK_PRODUCT.click()
        productPage = ProductPage(self.page)
        return productPage


    def view_cart(self):
        self.locators.LINK_CART.click()
        cartPage = CartPage(self.page)
        return cartPage


    def subscribe_user(self, user_id):
        self.page.get_by_placeholder("Your email address").fill(UserData(user_id).get("mail"))
        self.page.locator(".fa.fa-arrow-circle-o-right").click()
        expect(self.page.locator("#success-subscribe")).to_have_text("You have been successfully subscribed!")


    def see_product(self, item):
        # This will redirect to product page
        product_list = self.page.locator(".features_items")
        product = product_list.locator(".col-sm-4").filter(has_text=item)
        product.get_by_role("link", name="View Product").click()
        productPage = ProductPage(self.page)
        return productPage