import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def test_valid_customer_name():
    c = Customer("Alice")
    assert c.name == "Alice"
    c.name = "Bob"
    assert c.name == "Bob"

def test_invalid_customer_name():
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("NameWayTooLongToBeValid")
    with pytest.raises(ValueError):
        c = Customer("Joe")
        c.name = 123

def test_create_order_and_relationships():
    Order.all = []  
    Customer.all = []
    Coffee.all = []

    customer = Customer("Jane")
    coffee = Coffee("Latte")
    customer.create_order(coffee, 5.0)

    assert len(customer.orders()) == 1



def test_most_aficionado():
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    coffee = Coffee("Espresso")
    c1.create_order(coffee, 5.0)
    c2.create_order(coffee, 9.0)
    assert Customer.most_aficionado(coffee) == c2

def test_most_aficionado_with_no_orders():
    coffee = Coffee("Mocha")
    assert Customer.most_aficionado(coffee) is None
