class RoleLocators:
    def __init__(self, page):
        self.page = page

    @property
    def NAME(self):
        return self.page.get_by_placeholder("Name")

    @property
    def EMAIL_SIGHUP(self):
        return self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")

    @property
    def EMAIL_LOGIN(self):
        return self.page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")

    @property
    def PASSWORD(self):
        return self.page.get_by_placeholder("Password")

    @property
    def BTN_SIGNUP(self):
        return self.page.get_by_role('button', name="Signup")

    @property
    def BTN_LOGIN(self):
        return self.page.get_by_role("button", name="Login")


class PathLocators:
    def __init__(self, page):
        self.page = page

    @property
    def NEW_USER_TEXT_CSS(self):
        return self.page.locator('.signup-form')

    @property
    def LOGIN_TEXT_CSS(self):
        return self.page.locator('.login-form')