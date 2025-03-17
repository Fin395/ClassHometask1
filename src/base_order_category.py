from abc import ABC, abstractmethod
from typing import Any


class OrderCategory(ABC):
    """Создаем базовый абстрактный класс, который является родительским для классов Order и Category"""

    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Метод для инициализации экземпляра класса"""
        pass

    @abstractmethod
    def __str__(self, *args: Any, **kwargs: Any) -> str:
        """Метод для строкового отображения экземпляра класса"""
        pass
