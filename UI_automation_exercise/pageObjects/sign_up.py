from playwright.sync_api import expect
from locators.sign_up_page_locators import RoleLocators, PathLocators


class SignUpPage:

    def __init__(self, page):
        self.page = page
        self.locators = RoleLocators(self.page)
        self.pathLocator = PathLocators(self.page)

    def page_varification(self):
        expect(self.pathLocator.ACCOUNT_INFO).to_contain_text("Enter Account Information")


    def enter_user_details(self, user_cred_list):

        if user_cred_list["gender"] == 'male':
            self.pathLocator.MALE_OPT.click()
        elif user_cred_list["gender"] == 'female':
            self.pathLocator.FEMALE_OPT.click()

        self.locators.PASSWORD.fill(user_cred_list["password"])

        # select DOB
        self.pathLocator.SELECT_DATE('7')
        self.pathLocator.SELECT_MONTH('8')
        self.pathLocator.SELECT_YEAR('2000')


        # checkbox
        self.locators.NEWSLETTER_CHECKBOX.click()

        # First and last name
        names = user_cred_list["name"].split(' ')
        self.pathLocator.FIRST_NAME.fill(names[0])
        self.pathLocator.LAST_NAME.fill(names[1])

        self.pathLocator.ADDRESS.fill(user_cred_list["address"])
        self.pathLocator.STATE.fill(user_cred_list["state"])
        self.pathLocator.CITY.fill(user_cred_list["city"])
        self.pathLocator.ZIPCODE.fill(user_cred_list["zip"])
        self.pathLocator.MOBILE_NO.fill(user_cred_list["phone"])

        self.locators.BTN_ACCOUNT_CREATE.click()


    def varify_sign_up_and_continue(self):
        expect(self.pathLocator.ACCOUNT_CREATED).to_contain_text("Account Created!")
        self.locators.LINK_CONTINUE.click()