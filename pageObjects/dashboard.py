from pageObjects.orderhistory import OrderHistorydPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def selectOrderNavLink(self):
        self.page.get_by_role('button', name='ORDERS').click()

        orderHistoryPage = OrderHistorydPage(self.page)
        return orderHistoryPage