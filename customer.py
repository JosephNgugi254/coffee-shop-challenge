from order import Order  

class Customer:
    def __init__(self, name: str):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string with 1 to 15 characters.")
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string with 1 to 15 characters.")
        self._name = value

    def create_order(self, coffee, price):
        from order import Order 
        order = Order(self, coffee, price)
        return order  

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be an instance of Coffee.")
        
        customers_spent = {}
        for order in coffee.orders():
            customer = order.customer
            customers_spent[customer] = customers_spent.get(customer, 0) + order.price
        
        if not customers_spent:
            return None
        
        return max(customers_spent, key=customers_spent.get)
