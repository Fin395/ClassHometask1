from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        """Создаем базовый абстрактный класс, который является родительским для класса продуктов"""
        pass
