"""Basic math operations and calculations."""
from typing import Sequence, Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """두 숫자의 합을 반환합니다."""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """두 숫자의 차를 반환합니다."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """두 숫자의 곱을 반환합니다."""
    return a * b

def divide(a: Number, b: Number, default: Number = 0.0) -> Number:
    """두 숫자의 나눗셈을 수행합니다. 0으로 나눌 경우 기본값을 반환합니다."""
    if b == 0:
        return default
    return a / b

def power(base: Number, exponent: Number) -> Number:
    """거듭제곱을 계산합니다."""
    return base ** exponent

def calculate_average(numbers: Sequence[Number]) -> float:
    """숫자 시퀀스의 평균을 계산합니다."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
