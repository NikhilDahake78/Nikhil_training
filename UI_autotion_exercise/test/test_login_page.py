import json
from playwright.sync_api import Playwright, expect



"""
Test Steps:

Test Case : Register User
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and email address
7. Click 'Signup' button
8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
9. Fill details: Title, Name, Email, Password, Date of birth
10. Select checkbox 'Sign up for our newsletter!'
11. Select checkbox 'Receive special offers from our partners!'
12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
13. Click 'Create Account button'
14. Verify that 'ACCOUNT CREATED!' is visible
15. Click 'Continue' button
16. Verify that 'Logged in as username' is visible
17. Click 'Delete Account' button
18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
"""

def test_register_user(playwright:Playwright):

    with open('../data/user_info.json') as f:
        test_data = json.load(f)
        # print('Inside open')
        user_cred_list = test_data['user_credentials'][0]
        # print(user_cred_list)


    url = "https://automationexercise.com/"
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(url)

    # home page validation
    expect(page.get_by_role('button', name='Test Cases')).to_be_visible()
    expect(page.get_by_role('button', name='APIs list for practice')).to_be_visible(timeout=10000)

    # new user register
    page.get_by_role('link', name=" Signup / Login").click()

    expect(page.locator('.signup-form')).to_contain_text("New User Signup!")

    page.get_by_placeholder("Name").fill(user_cred_list['name'])
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill(user_cred_list['mail'])
    page.get_by_role('button', name="Signup").click()

    # sign up page
    expect(page.locator("//div/h2[@class='title text-center']")).to_contain_text("Enter Account Information")


    if user_cred_list["gender"] == 'male':
        page.locator("#uniform-id_gender1").click()
    elif user_cred_list["gender"] == 'female':
        page.locator("#uniform-id_gender2").click()

    page.get_by_label("password").fill(user_cred_list["password"])

    # select DOB
    page.locator("#days").select_option(value='7')
    page.locator("#months").select_option(value='8')
    page.locator("#years").select_option(value='2000')

    # checkbox
    page.get_by_role('checkbox', name='newsletter').click()

    # First and last name
    names = user_cred_list["name"].split(' ')
    page.locator('#first_name').fill(names[0])
    page.locator('#last_name').fill(names[1])
    page.locator("#address1").fill(user_cred_list["address"])
    page.locator("#state").fill(user_cred_list["state"])
    page.locator("#city").fill(user_cred_list["city"])
    page.locator("#zipcode").fill(user_cred_list["zip"])
    page.locator("#mobile_number").fill(user_cred_list["phone"])
    page.get_by_role('button', name="Create Account").click()

    # Acc created Page
    expect(page.locator('.title.text-center')).to_contain_text("Account Created!")
    page.get_by_role('link', name="Continue").click()

    # logged In page
    # expect(page.locator("//div/ul/li[@xpath = '10'")).to_contain_text(user_cred_list["name"])
    expect(page.locator("//a/i[@class='fa fa-user']/following-sibling::b")).to_contain_text(user_cred_list["name"])
    page.get_by_role('link', name=" Delete Account").click(timeout=10000)


    # Verify delete account
    expect(page.locator('.title.text-center')).to_contain_text("Account Deleted!")
    page.get_by_role('link', name="Continue").click()

    # print(a)