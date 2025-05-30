class Order:
    all = []

    def __init__(self, customer, coffee, price: float):
        from customer import Customer 
        from coffee import Coffee  

        if not isinstance(customer, Customer):
            raise ValueError("Customer must be an instance of Customer.")
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be an instance of Coffee.")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order.all.append(self) 

    @property
    def price(self) -> float:
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
