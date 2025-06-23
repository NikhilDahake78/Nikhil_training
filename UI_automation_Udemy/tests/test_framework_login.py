import json
import pytest

from pageObjects.login import LoginPage

# data from json
with open('data/credentials.json') as f:
    test_data = json.load(f)
    # print('Inside open')
    user_cred_list = test_data['user_credentials']
    print(user_cred_list)


@pytest.mark.parametrize('userCredentials', user_cred_list)
def test_check_login(browserInstance, userCredentials):

    # Login Page
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(userCredentials['username'], userCredentials['password'])
    loginPage.validate_login()

    # Dashboard page
    orderHistoryPage = dashboardPage.selectOrderNavLink()

    # Order history page
    orderId = '684fea54eca477e2d64f10db'
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)

    # Order details page
    orderDetailsPage.verifyOrderMessage()

