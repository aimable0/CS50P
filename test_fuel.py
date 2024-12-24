import pytest
from fuel2 import gauge, convert

def test_convert__with_valid_int():
     assert convert('3/4') == 75
     with pytest.raises(AssertionError):
         assert convert('1/4') == '25%'

def test_convert_with_y_x_not_int():
     with pytest.raises(ValueError):
          convert('This')

def test_convert_with_x_greater_than_y():
     with pytest.raises(ValueError):
          convert('5/4')

def test_convert_with_y_equal_zero():
     with pytest.raises(ZeroDivisionError):
          convert('4/0')

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(75) == '75%'
