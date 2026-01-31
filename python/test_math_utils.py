import pytest
from math_utils import MathUtils

@pytest.fixture
def math():
    return MathUtils()

def test_add_basic(math):
    assert math.add(2, 3) == 5

def test_add_negative(math):
    assert math.add(2, -3) == -1

def test_subtract_basic(math):
    assert math.subtract(10, 3) == 7

def test_subtract_negative_result(math):
    assert math.subtract(5, 10) == -5

def test_multiply_basic(math):
    assert math.multiply(3, 4) == 12

def test_multiply_by_zero(math):
    assert math.multiply(999, 0) == 0

def test_divide_normal(math):
    assert math.divide(5, 2) == 2.5

def test_divide_by_zero_returns_minus_one(math):
    assert math.divide(10, 0) == -1.0
