from typing import Any

from src.base_product import BaseProduct
from src.mixin_print import MixinPrint


class Product(MixinPrint, BaseProduct):
    """Создаем класс Product из базового абстрактного класса BaseProduct"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """Создаем метод для строкового отображения экземпляра класса"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> Any:
        """Создаем метод, позволяющий складывать стоимость товаров"""
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, one_more_product: dict) -> Any:
        """Создаем класс-метод для получения экземпляра на основе параметров товара из входного словаря"""
        try:
            return cls(**one_more_product)
        except Exception:
            raise Exception("Ошибка: Проверьте корректность описания товара")

    @property
    def price(self) -> float:
        """Создаем геттер для получения значения цены как приватного атрибута "self.__price" """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Создаем сеттер для установки нового значения приватного атрибута "self.__price" """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            if new_price < self.__price:
                user_input = input("Вы уверены, что хотите понизить цену?\nY/N\n")
                if user_input == "N":
                    self.__price = self.__price
                else:
                    self.__price = new_price
