from playwright.sync_api import expect
from locators.sign_up_page_locators import RoleLocators, PathLocators
from data.user_data import UserData

class SignUpPage:

    def __init__(self, page):
        self.page = page
        self.locators = RoleLocators(self.page)
        self.pathLocator = PathLocators(self.page)

    def page_varification(self):
        expect(self.pathLocator.ACCOUNT_INFO).to_contain_text("Enter Account Information")


    def enter_user_details(self, user_id):

        user_data = UserData(user_id)

        if user_data.get("gender") == 'male':
            self.pathLocator.MALE_OPT.click()
        elif user_data.get("gender") == 'female':
            self.pathLocator.FEMALE_OPT.click()

        self.locators.PASSWORD.fill(user_data.get("password"))

        # select DOB
        DOB = user_data.get('DOB').split('-')
        self.pathLocator.SELECT_DATE(DOB[0])
        self.pathLocator.SELECT_MONTH(DOB[1])
        self.pathLocator.SELECT_YEAR(DOB[2])


        # checkbox
        self.locators.NEWSLETTER_CHECKBOX.click()

        # First and last name
        full_name = user_data.get("name").split(' ')
        self.pathLocator.FIRST_NAME.fill(full_name[0])
        self.pathLocator.LAST_NAME.fill(full_name[1])

        self.pathLocator.ADDRESS.fill(user_data.get("address"))
        self.pathLocator.STATE.fill(user_data.get("state"))
        self.pathLocator.CITY.fill(user_data.get("city"))
        self.pathLocator.ZIPCODE.fill(user_data.get("zip"))
        self.pathLocator.MOBILE_NO.fill(user_data.get("phone"))

        self.locators.BTN_ACCOUNT_CREATE.click()


    def varify_sign_up_and_continue(self):
        expect(self.pathLocator.ACCOUNT_CREATED).to_contain_text("Account Created!")
        self.locators.LINK_CONTINUE.click()