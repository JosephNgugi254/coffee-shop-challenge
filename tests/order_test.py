import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_valid_order():
    c = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(c, coffee, 4.5)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 4.5

def test_invalid_price():
    c = Customer("Bob")
    coffee = Coffee("Espresso")
    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(c, coffee, 15.0)
    with pytest.raises(ValueError):
        Order(c, coffee, "expensive")

def test_invalid_types():
    c = Customer("Alice")
    coffee = Coffee("Mocha")
    with pytest.raises(ValueError):
        Order("not a customer", coffee, 5.0)
    with pytest.raises(ValueError):
        Order(c, "not a coffee", 5.0)
