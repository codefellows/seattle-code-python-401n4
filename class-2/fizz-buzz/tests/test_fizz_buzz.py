import pytest
from fizz_buzz.fizz_buzz import fizz_buzz, fizz_buzz_alternate
from fizz_buzz import __version__

def test_version():
    assert __version__ == '0.1.0'

def test_one():
    actual = fizz_buzz(1)
    expected = 1
    assert actual == expected

def test_two():
    actual = fizz_buzz(2)
    expected = 2
    assert actual == expected

def test_seven():
    actual = fizz_buzz(7)
    expected = 7
    assert actual == expected

def test_three():
    actual = fizz_buzz(3)
    expected = 'Fizz'
    assert actual == expected

def test_nine():
    actual = fizz_buzz(9)
    expected = 'Fizz'
    assert actual == expected

def test_five():
    actual = fizz_buzz(5)
    expected = 'Buzz'
    assert actual == expected

def test_fifteen():
    actual = fizz_buzz(15)
    expected = 'FizzBuzz'
    assert actual == expected

def test_fifteen():
    actual = fizz_buzz(155)
    expected = 'FizzBuzz'
    assert actual != expected

def test_nine_alternate():
    actual = fizz_buzz_alternate(9)
    expected = 'Fizz'
    assert actual == expected

def test_five_alternate():
    actual = fizz_buzz_alternate(5)
    expected = 'Buzz'
    assert actual == expected

def test_fifteen_alternate():
    actual = fizz_buzz_alternate(15)
    expected = 'FizzBuzz'
    assert actual == expected

def test_two_alternate():
    assert fizz_buzz_alternate(2) == 2
    assert fizz_buzz_alternate(3) == "Fizz"
    assert fizz_buzz_alternate(5) == "Buzz"