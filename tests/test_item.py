"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from config import ITEMS
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

def test_name():
    """Тест проверки длины наименования товара(не больше 10 символов"""
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    item1.name = "Духовой шкаф"
    assert item1.name == "Духовой шк"


def test_instantiate_from_csv():
    """Проверка добавления экземпляров класса из CSV файла"""
    Item.instantiate_from_csv(ITEMS)
    assert len(Item.all) == 5


def test_string_to_number():
    """Проверка возвращения числа из строки-числа"""
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("1.5") == 1


