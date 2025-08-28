
import pytest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(3, 2) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5

def test_multiply(calc):
    assert calc.multiply(4, 5) == 20
    assert calc.multiply(0, 5) == 0

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(-9, 3) == -3

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(5, 0)
