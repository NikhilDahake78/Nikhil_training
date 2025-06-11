import time

from playwright.sync_api import Page, expect


def test_UIchecks(page:Page):

    # hide/ display placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role('button', name='Hide').click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # Alertbox
    page.on('dialog', lambda dialog:dialog.accept())
    page.get_by_role('button', name='Confirm').click()
    # time.sleep(5)

    # Frame handling
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role('link', name='All Access plan').click()
    expect(page_frame.locator('body')).to_contain_text('Testimonial')
