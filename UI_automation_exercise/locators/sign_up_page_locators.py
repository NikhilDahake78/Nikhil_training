class RoleLocators:
    def __init__(self, page):
        self.page = page

    @property
    def NEWSLETTER_CHECKBOX(self):
        return self.page.get_by_role('checkbox', name='newsletter')

    @property
    def BTN_ACCOUNT_CREATE(self):
        return self.page.get_by_role('button', name="Create Account")

    @property
    def LINK_CONTINUE(self):
        return self.page.get_by_role('link', name="Continue")

    @property
    def PASSWORD(self):
        return self.page.get_by_label("password")


class PathLocators:
    def __init__(self, page):
        self.page = page

    @property
    def ACCOUNT_INFO(self):
        return self.page.locator("//div/h2[@class='title text-center']")

    @property
    def MALE_OPT(self):
        return self.page.locator("#uniform-id_gender1")

    @property
    def FEMALE_OPT(self):
        return self.page.locator("#uniform-id_gender2")

    def SELECT_DATE(self, date):
        self.page.locator("#days").select_option(value=date)

    def SELECT_MONTH(self, date):
        self.page.locator("#months").select_option(value=date)

    def SELECT_YEAR(self, date):
        self.page.locator("#years").select_option(value=date)

    @property
    def FIRST_NAME(self):
        return self.page.locator('#first_name')

    @property
    def LAST_NAME(self):
        return self.page.locator('#last_name')

    @property
    def ADDRESS(self):
        return self.page.locator("#address1")

    @property
    def STATE(self):
        return self.page.locator('#state')

    @property
    def CITY(self):
        return self.page.locator('#city')

    @property
    def ZIPCODE(self):
        return self.page.locator('#zipcode')

    @property
    def MOBILE_NO(self):
        return self.page.locator('#mobile_number')

    @property
    def ACCOUNT_CREATED(self):
        return self.page.locator('.title.text-center')