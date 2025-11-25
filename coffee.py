# coffee.py

from order import Order

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Coffee name must be a string with at least 3 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        customers = {order.customer for order in self.orders()}
        return list(customers)

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0.0
        total = sum(order.price for order in orders)
        return total / len(orders)