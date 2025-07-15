from pageObjects.home import HomePage
from pageObjects.login_sign_up import LoginSignUpPage
from utils.Logging import Log


def create_new_user(user_id, page):

    # home page navigation
    # Log.info("Navigating to Base url")
    homePage = HomePage(page)
    homePage.navigate()

    # home page validation
    # Log.info("Home page Validation")
    homePage.varify_page_without_user_sign_in()

    # login/sign page
    # Log.info("Signing In..")
    loginSignUpPage = homePage.login_sign_up()
    loginSignUpPage.varify_new_user_option()

    # sign up page
    signUpPage = loginSignUpPage.new_user_sign_up(user_id)

    # sign up page varification and details filling
    signUpPage.page_varification()
    signUpPage.enter_user_details(user_id)

    # logged in page and varification
    signUpPage.varify_sign_up_and_continue()
    Log.info("Signed Up successfully")


def login(user_id):
    pass

def logout(user_id):
    pass

def delete_user(user_id, page):
    # write check for if you are log in as same user, then delete it.
    homePage = HomePage(page)
    homePage.delete_user_and_varify_delete()
    Log.info("User deleted Successfully")