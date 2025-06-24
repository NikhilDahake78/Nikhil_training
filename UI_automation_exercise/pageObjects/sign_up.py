from playwright.sync_api import expect


class SignUpPage:

    def __init__(self, page):
        self.page = page


    def page_varification(self):
        expect(self.page.locator("//div/h2[@class='title text-center']")).to_contain_text("Enter Account Information")


    def enter_user_details(self, user_cred_list):

        if user_cred_list["gender"] == 'male':
            self.page.locator("#uniform-id_gender1").click()
        elif user_cred_list["gender"] == 'female':
            self.page.locator("#uniform-id_gender2").click()

        self.page.get_by_label("password").fill(user_cred_list["password"])

        # select DOB
        self.page.locator("#days").select_option(value='7')
        self.page.locator("#months").select_option(value='8')
        self.page.locator("#years").select_option(value='2000')

        # checkbox
        self.page.get_by_role('checkbox', name='newsletter').click()

        # First and last name
        names = user_cred_list["name"].split(' ')
        self.page.locator('#first_name').fill(names[0])
        self.page.locator('#last_name').fill(names[1])

        self.page.locator("#address1").fill(user_cred_list["address"])
        self.page.locator("#state").fill(user_cred_list["state"])
        self.page.locator("#city").fill(user_cred_list["city"])
        self.page.locator("#zipcode").fill(user_cred_list["zip"])
        self.page.locator("#mobile_number").fill(user_cred_list["phone"])

        self.page.get_by_role('button', name="Create Account").click()


    def varify_sign_up_and_continue(self):
        expect(self.page.locator('.title.text-center')).to_contain_text("Account Created!")
        self.page.get_by_role('link', name="Continue").click()