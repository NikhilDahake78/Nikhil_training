""" This is conftest.py """
from datetime import datetime
from logging import exception

import pytest
from utils.Logging import Log
from utils.user import user
from pageObjects.login_sign_up import LoginSignUpPage


# global variable
is_user_created = False
user_id = 'user_1'

def pytest_configure(config):
    """
    Pytest hook called before test collection.
    Dynamically sets the log_file path based on a timestamp.
    """

    # Generate a timestamp for the log file name
    timestamp = datetime.now().strftime("%Y-%m-%d-%H_%M_%S")

    # Construct the dynamic log file path
    dynamic_log_file = f"pytest_log_{timestamp}.log"


    # log cli setup
    config.option.log_cli = 1
    config.option.log_cli_level = "INFO"
    config.option.log_cli_date_format = "%Y - %m - % d % H: % M: %S"
    config.option.log_cli_format = "%(asctime)s - %(filename)- %(levelname)s - %(message)s"

    # log file configurations
    config.option.log_file_date_format = "%Y-%m-%d %H:%M:%S"
    config.option.log_file_format = "%(asctime)s : %(levelname)s : %(message)s"
    config.option.log_file_level = "INFO"
    config.option.log_file = f"log/{dynamic_log_file}"


def pytest_addoption(parser):
    """
    Adding customize arguments.
    """
    parser.addoption(
        "--Browser",
        action="store",
        default='chrome',
        help="browser selection",
        choices=('chrome', 'firefox')
    )
    parser.addoption(
        "--headless",
        action="store",
        default="True",
        help="headless_status",
        choices=("True", "False")
    )


@pytest.fixture
def my_browser(playwright, request):
    """
    :param playwright: default
    :param request: default
    :return: browser page
    """
    browser_name = request.config.getoption("Browser")
    headless_status = True if request.config.getoption("headless") == "True" else False

    Log.title("Setup")
    Log.info(f"Selected browser: {browser_name}")
    Log.info(f"Test will run in {'headless' if headless_status == 'False' else 'headed'} mode")
    Log.info("Opening browser.")


    browser = ''

    if browser_name == 'chrome':
        browser = playwright.chromium.launch(headless=headless_status)
    elif browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=headless_status)

    context = browser.new_context()
    page = context.new_page()

    yield page

    Log.title("Teardown")

    # deleting user
    if is_user_created:

        try:
            user.login_user(page, user_id)
            # loginPage = LoginSignUpPage(page)
            # loginPage.user_login(user_id)
            Log.info(f"Deleting user")
            user.delete_user(page)
        except Exception as e :
            Log.warning(f"Exception is: {e}")


    Log.info("Closing browser.")
    page.close()
    context.close()
    browser.close()


@pytest.fixture
def browser_with_user(my_browser):
    """
    :return: browser page after creating a user[id: user_1]
    """

    Log.info(f"Creating new user for testing: ID: {user_id}")
    user.create_new_user(my_browser, user_id)
    user.logout_user(my_browser, user_id)

    yield my_browser

    global is_user_created
    is_user_created = True



@pytest.fixture
def dummy1():
    print("\nwe are inside dummy1 setup")

    yield

    print("\nthis is dummy 1 teardown")


@pytest.fixture
def dummy2(dummy1):
    print("\nwe are inside dummy2 setup")

    yield

    print("\nthis is dummy 2 teardown")
