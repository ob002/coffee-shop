from order import Order

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        coffees = {order.coffee for order in self.orders()}
        return list(coffees)

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Argument must be a Coffee instance")

        customer_total = {}
        for order in Order.all:
            if order.coffee is coffee:
                cust = order.customer
                customer_total[cust] = customer_total.get(cust, 0) + order.price

        if not customer_total:
            return None

        return max(customer_total, key=customer_total.get)