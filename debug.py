from customer import Customer
from coffee import Coffee

# Create customers
customer1 = Customer("Alice")
customer2 = Customer("Bob")
customer3 = Customer("Charlie")

# Create coffees
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

# Create orders
customer1.create_order(coffee1, 5.0)
customer1.create_order(coffee2, 3.0)
customer2.create_order(coffee1, 7.0)
customer3.create_order(coffee1, 9.0)

# Print customer1's orders count
print(f"{customer1.name} orders count:", len(customer1.orders()))

# Print coffees customer1 ordered (names)
print(f"Coffees {customer1.name} ordered:", [c.name for c in customer1.coffees()])

# Print orders count for coffee1
print(f"{coffee1.name} orders count:", coffee1.num_orders())

# Print average price for coffee1
print(f"{coffee1.name} average price:", coffee1.average_price())

# Print customers who ordered coffee1 (names)
print(f"Customers who ordered {coffee1.name}:", [c.name for c in coffee1.customers()])

# Print most aficionado for coffee1
aficionado = Customer.most_aficionado(coffee1)
print(f"Most aficionado of {coffee1.name}:", aficionado.name if aficionado else "None")

