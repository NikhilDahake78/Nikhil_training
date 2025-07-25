"""
This is contact us page
"""
from playwright.sync_api import expect
from data.user_data import UserData


class ContactUsPage:

    def __init__(self, page):
        self.page = page

    def validate(self):
        # validating page with text present
        expect(self.page.get_by_text("Get In Touch")).to_be_visible()

    def submit_details(self, user_id, subject='NA', msg = 'NA', file_path = None):

        self.page.get_by_placeholder("Name").fill(UserData(user_id).get('name'))
        self.page.get_by_placeholder("Email", exact=True).fill(UserData(user_id).get('mail'))
        self.page.get_by_placeholder("Subject").fill(subject)
        self.page.get_by_placeholder("Your Message Here").fill(msg)

        try:
            page.locator("//div/input[@type='file']").set_input_files(file_path)
        except Exception as e:
            print(f"Exception occurred, check file path: {e}")

        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.page.get_by_role('button', name='submit').click()
        self.page.get_by_role("link", name=" Home").click()
        return self.page
