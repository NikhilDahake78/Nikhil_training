from pageObjects.home import HomePage
from pageObjects.login_sign_up import LoginSignUpPage
from utils.Logging import Log


class User:

    @staticmethod
    def create_new_user(page, user_id):

        # home page navigation
        Log.info("Navigating to Base url")
        homePage = HomePage(page)
        homePage.navigate()

        # home page validation
        Log.info("Home page Validation")
        homePage.varify_page_without_user_sign_in()

        # login/sign page
        Log.info("Signing In..")
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


    @staticmethod
    def login_user(page, user_id):

        # navigate to home page
        Log.info(f"Navigating to Home page for Login")
        homePage = HomePage(page)
        homePage.navigate()
        homePage.varify_page_without_user_sign_in()

        # navigate to login page
        Log.info(f"Logging in with user: {user_id}")
        loginSignUpPage = homePage.login_sign_up()
        loginSignUpPage.varify_login_option()

        # log in
        loginSignUpPage.user_login(user_id)
        homePage = HomePage(page)
        homePage.varify_page_with_user_sign_in(user_id)
        Log.info(f"Logged in successfully.")


    @staticmethod
    def logout_user(page, user_id = "user_1"):

        homePage = HomePage(page)
        homePage.logout()


    @staticmethod
    def delete_user(page, user_id = "user_1" ):

        # write check for if you are log in as same user, then delete it.
        homePage = HomePage(page)
        homePage.delete_user_and_varify_delete()
        Log.info("User deleted Successfully")


user = User()