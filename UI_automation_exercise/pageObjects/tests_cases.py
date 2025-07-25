"""
This is test cases page
"""

class TestsCasesPage:
    def __init__(self, page):
        self.page = page

    def verify(self):
        self.page.locator(".title.text-center").filter(has_text='Test Cases')