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



def test_table_check(page:Page):
    # check price of rice is equal to 37
    # Get row and column.
    colIn = ''
    page.goto('https://rahulshettyacademy.com/seleniumPractise/#/offers')
    for index in range(page.locator('th').count()):
        if page.locator('th').nth(index).filter(has_text='Price').count() > 0:
            colIn = index
            break
    print(f'Column index: {colIn}')

    riceRow = page.locator('tr').filter(has_text='Rice')

    print(riceRow.locator('td').nth(colIn).text_content())


def test_mousehover(page:Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    page.locator('#mousehover').hover()
    time.sleep(1)
    page.get_by_role('link', name='Top').click()
    time.sleep(1)



