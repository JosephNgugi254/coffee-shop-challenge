from order import Order  

class Coffee:
    def __init__(self, name: str):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)
