from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Создаем базовый абстрактный класс, который является родительским для класса продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        """Абстрактный метод, который должен быть переопределен в дочерних классаъ"""
        pass
