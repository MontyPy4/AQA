from calculator import Calculator
import pytest

# Фикстура с областью видимости "function" (по умолчанию).
# Она будет запускаться ПЕРЕД каждым тестом, где указана в аргументах.
@pytest.fixture
def calc():
    return Calculator()

def test_sum_impacts_state(calc):
    # Тест 1: Теперь это безопасно. Мы меняем состояние ТОЛЬКО этого calc
    assert calc.sum(5, 5) == 10
    assert calc.last_result == 10

def test_check_initial_state(calc):
    # Тест 2: ПРОЙДЕТ! Потому что здесь новый объект с last_result = 0
    assert calc.last_result == 0

def test_sum_positive_numbers(calc):
    assert calc.sum(5, 4) == 9

def test_sum_negative_numbers(calc):
    assert calc.sum(-6, -10) == -16

def test_sum_positive_and_negative(calc):
    assert calc.sum(-6, 6) == 0

def test_sum_floats(calc):
    res = calc.sum(5.6, 4.3)
    assert round(res, 1) == 9.9

def test_sum_with_zero(calc):
    assert calc.sum(10, 0) == 10

def test_division(calc):
    assert calc.div(10, 2) == 5

def test_division_by_zero(calc):
    with pytest.raises(ArithmeticError, match="На ноль делить нельзя"):
        calc.div(10, 0)

@pytest.mark.ich_ser_gut
def test_avg_empty_list(calc):
    assert calc.avg([]) == 0

def test_avg_list(calc):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    assert calc.avg(numbers) == 5

@pytest.mark.xfail(reason="Метод в процессе разработки")
def test_sum_positive_nums(calc):
    # Здесь мы тоже используем фикстуру для единообразия
    res = calc.sum(4, 5)
    assert res == 9