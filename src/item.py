import csv
import os
from pathlib import Path

class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = "Файл items.csv поврежден"

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __add__(self, other):
        """Cложение экземпляров класса `Phone` и `Item` (сложение по количеству товара в магазине)"""
        if not isinstance(other, Item):
            raise ValueError
        return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """Функция проверяет длину наименования товара, чтобы было не более 10 символов"""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, csv_file='../src/items.csv'):
        """Добавление экземпляра класса из csv файла"""
        cls.all.clear()
        if os.path.exists(csv_file):
            try:
                with open(csv_file, 'r', newline="", encoding="windows-1251") as file:
                    data = csv.DictReader(file)
                    for item in data:
                        cls(name=str(item["name"]), price=float(item["price"]), quantity=int(item["quantity"]))
            except KeyError:
                raise InstantiateCSVError("Файл items.csv поврежден")
        else:
            raise FileNotFoundError("Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(str_number):
        """Возвращает число из числа-строки"""
        number = float(str_number)
        return int(number)

