"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

@pytest.fixture
def test_item():
    return Item("Смартфон", 10000, 2)

def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 20000
    assert test_item.price == 10000

def test_apply_discount(test_item):
    test_item.pay_rate = 0.8
    test_item.apply_discount()
    assert test_item.calculate_total_price() == 16000.0
    assert test_item.price == 8000

