import pytest
from simple_math import SimpleMath


@pytest.fixture
def simple_math():
    return SimpleMath()


def test_square_positive(simple_math):
    """Тест квадратирования положительного числа"""
    assert simple_math.square(2) == 4


def test_square_negative(simple_math):
    """Тест квадратирования отрицательного числа"""
    assert simple_math.square(-3) == 9


def test_square_zero(simple_math):
    """Тест квадратирования нуля"""
    assert simple_math.square(0) == 0


def test_square_float(simple_math):
    """Тест квадратирования дробного числа"""
    assert simple_math.square(2.5) == 6.25


def test_cube_positive(simple_math):
    """Тест возведения в куб положительного числа"""
    assert simple_math.cube(2) == 8


def test_cube_negative(simple_math):
    """Тест возведения в куб отрицательного числа"""
    assert simple_math.cube(-3) == -27


def test_cube_zero(simple_math):
    """Тест возведения в куб нуля"""
    assert simple_math.cube(0) == 0


def test_cube_float(simple_math):
    """Тест возведения в куб дробного числа"""
    assert simple_math.cube(1.5) == 3.375