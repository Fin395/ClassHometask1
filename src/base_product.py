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
        """Метод для инициализации экземпляра класса"""
        pass

    @abstractmethod
    def __str__(self, *args, **kwargs) -> str:
        """Метод для строкового отображения экземпляра класса"""
        pass

    @abstractmethod
    def __add__(self, *args, **kwargs) -> Any:
        """Метод, позволяющий складывать стоимость товаров"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs) -> Any:
        """Класс-метод для получения экземпляра на основе параметров товара из входного словаря"""
        pass

    @property
    @abstractmethod
    def price(self, *args, **kwargs) -> float:
        """Геттер для получения значения цены как приватного атрибута "self.__price" """
        pass

    @price.setter
    @abstractmethod
    def price(self, *args, **kwargs) -> None:
        """Сеттер для установки нового значения приватного атрибута "self.__price" """
        pass
