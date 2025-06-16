from pageObjects.orderDetails import OrderDetailsdPage


class OrderHistorydPage:

    def __init__(self, page):
        self.page = page

    def selectOrder(self, orderId):
        row =  self.page.locator('tr').filter(has_text=orderId)
        row.get_by_role('button', name='View').click()
        orderDetailsPage = OrderDetailsdPage(self.page)
        return orderDetailsPage