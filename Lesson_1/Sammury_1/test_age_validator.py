import pytest
from age_validator import AgeValidator

@pytest.fixture
def age():
    return AgeValidator()

def test_age(age):
    assert age.is_adult(15) is False

def test_adult(age):
    assert age.is_adult(18) is True
    assert age.is_adult(19) is True