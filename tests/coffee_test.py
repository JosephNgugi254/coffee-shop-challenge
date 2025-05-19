import pytest
from customer import Customer
from coffee import Coffee

def test_valid_coffee_name():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_invalid_coffee_name():
    with pytest.raises(ValueError):
        Coffee("A")
    with pytest.raises(ValueError):
        Coffee(123)

def test_orders_and_customers():
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    coffee = Coffee("Cappuccino")
    c1.create_order(coffee, 3.0)
    c2.create_order(coffee, 4.0)

    assert len(coffee.orders()) == 2
    customers = coffee.customers()
    assert c1 in customers and c2 in customers

def test_num_orders_and_average_price():
    c = Customer("Alice")
    coffee = Coffee("Americano")
    assert coffee.num_orders() == 0
    assert coffee.average_price() == 0

    c.create_order(coffee, 4.0)
    c.create_order(coffee, 6.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0
