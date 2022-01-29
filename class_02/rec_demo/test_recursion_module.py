from recursion_module import quick_test, factorial
import pytest

def test_function():
    assert quick_test() == None

def test_three():
    actual = factorial(3)
    expected = 6
    assert actual == expected

def test_three():
    actual = factorial(8)
    expected = 40320
    assert actual == expected
