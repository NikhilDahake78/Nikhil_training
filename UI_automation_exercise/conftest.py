import pytest
from playwright.sync_api import Playwright
from datetime import datetime
from utils.Logging import Log

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
    browser_name = request.config.getoption("Browser")
    headless_status = True if request.config.getoption("headless") == "True" else False

    Log.title("Setup")
    Log.info(f"Selected browser: {browser_name}")
    Log.info(f"Test will run in {headless if headless_status == 'False' else 'headed'} mode")
    Log.info("Opening browser browser.")

    if browser_name == 'chrome':
        browser = playwright.chromium.launch(headless=headless_status)
    elif browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=headless_status)

    context = browser.new_context()
    page = context.new_page()

    yield page

    Log.title("Teardown")
    Log.info("Closing browser.")
    page.close()
    context.close()
    browser.close()