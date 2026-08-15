import pytest
from src.utils.math_ops import (
    add,
    subtract,
    multiply,
    divide,
    power,
    calculate_average,
)


def test_basic_arithmetic():
    assert add(10, 5) == 15
    assert subtract(10, 5) == 5
    assert multiply(4, 5) == 20
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    assert divide(10, 0) == 0.0
    assert divide(10, 0, default=-1) == -1


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([]) == 0.0
    assert calculate_average([10.0, 20.0]) == 15.0
