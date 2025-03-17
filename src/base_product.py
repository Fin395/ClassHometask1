from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Создаем базовый абстрактный класс, который является родительским для класса продуктов"""

    name: str
    description: str
    __price: float
    quantity: int

    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        """Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра"""
        pass

    @abstractmethod
    def __str__(self, *args, **kwargs) -> str:
        """Создаем метод для строкового отображения экземпляра класса"""
        pass

    @abstractmethod
    def __add__(self, *args, **kwargs) -> Any:
        """Создаем метод, позволяющий складывать стоимость товаров"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs) -> Any:
        """Создаем класс-метод для получения экземпляра на основе параметров товара из входного словаря"""
        pass

    @property
    @abstractmethod
    def price(self, *args, **kwargs) -> float:
        """Создаем геттер для получения значения цены как приватного атрибута "self.__price" """
        pass

    @price.setter
    @abstractmethod
    def price(self, *args, **kwargs) -> None:
        """Создаем сеттер для установки нового значения приватного атрибута "self.__price" """
        pass