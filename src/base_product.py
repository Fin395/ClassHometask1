from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Создаем базовый абстрактный класс, который является родительским для класса продуктов"""

    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Метод для инициализации экземпляра класса"""
        pass

    @abstractmethod
    def __str__(self, *args: Any, **kwargs: Any) -> str:
        """Метод для строкового отображения экземпляра класса"""
        pass

    @abstractmethod
    def __add__(self, *args: Any, **kwargs: Any) -> Any:
        """Метод, позволяющий складывать стоимость товаров"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        """Класс-метод для получения экземпляра на основе параметров товара из входного словаря"""
        pass

    @property
    @abstractmethod
    def price(self, *args: Any, **kwargs: Any) -> float:
        """Геттер для получения значения цены как приватного атрибута "self.__price" """
        pass

    @price.setter
    @abstractmethod
    def price(self, *args: Any, **kwargs: Any) -> None:
        """Сеттер для установки нового значения приватного атрибута "self.__price" """
        pass
