from src.item import Item


class KeyboardMixin:
    """Реализуем доп.функционал по хранению и изменению раскладки клавиатуры"""
    def __init__(self):
        """Язык по умолчанию - английский (`EN`)"""
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Изменяет язык"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(Item, KeyboardMixin):
    """Создаем класс Keyboard для товара 'клавиатура'"""
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        KeyboardMixin.__init__(self)
