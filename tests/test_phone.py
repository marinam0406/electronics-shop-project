import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone('iPhone 14', 120_000, 5, 2)


def test_constructor(phone):
    assert phone.name == "iPhone 14"
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2

def test_repr(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"

def test_str(phone):
    assert str(phone) == "iPhone 14"

def test_number_of_sim(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = -1
        phone.number_of_sim = 0
        phone.number_of_sim = 1.2

