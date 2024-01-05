
import pytest
from series import fibonacci, lucas, sum_series


#####    fibonacci  #####

def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

#####   lucas   #####
    
def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected


#####    Sum series ##### 
    
def test_sum_series_fibonacci():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_sum_series_lucas():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected

def test_sum_series_one():
    actual = sum_series(2, 3, 2)
    expected = 5
    assert actual == expected

def test_sum_series_two():
    actual = sum_series(3, 1, 2)
    expected = 5
    assert actual == expected   
