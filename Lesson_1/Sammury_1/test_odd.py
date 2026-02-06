import pytest
from odd import EvenOddChecker

@pytest.fixture
def evenOddChecker():
    return EvenOddChecker() # будет инициализироваться копия класса


def test_is_even(evenOddChecker):
    assert evenOddChecker.is_even(2) is True
    assert evenOddChecker.is_even(3) is False
    assert evenOddChecker.is_even(-2) is True

# функция is_even - проверяет есть ли остаток = если нет = True

def test_is_odd(evenOddChecker):
    assert evenOddChecker.is_odd(2) is False
    assert evenOddChecker.is_odd(3) is True
    assert evenOddChecker.is_odd(-2) is False