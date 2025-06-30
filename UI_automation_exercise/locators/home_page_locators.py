class RoleLocators:
    def __init__(self, page):
        self.page = page

    @property
    def BTN_TEST_CASE(self):
        return self.page.get_by_role("button", name='Test Cases')

    @property
    def BTN_API_LIST(self):
        return self.page.get_by_role("button", name="APIs list for practice")

    @property
    def LINK_SIGNUP(self):
        return self.page.get_by_role("link", name=" Signup / Login")

    @property
    def LINK_LOGOUT(self):
        return self.page.get_by_role("link", name=" Logout")

    @property
    def LINK_DELETE(self):
        return self.page.get_by_role("link", name=" Delete Account")

    @property
    def LINK_CONTINUE(self):
        return self.page.get_by_role("link", name="Continue")


class PathLocators:
    def __init__(self, page):
        self.page = page

    @property
    def USERNAME_XPATH(self):
        # Varification of username on home page after sign-in
        return self.page.locator("//a/i[@class='fa fa-user']/following-sibling::b")

    @property
    def ACCOUNT_DELETE_CSS(self):
        return self.page.locator(".title.text-center")
