from typing import Any

from src.category import Category


class ProductIterator:
    """Создаем итератор, с помощью которого можно перебирать товары одной категории"""

    def __init__(self, category_obj: Category):
        """Инициализируем итератор"""
        self.category_obj = category_obj
        self.index = 0

    def __iter__(self) -> "ProductIterator":
        """Возвращает итератор"""
        self.index = 0
        return self

    def __next__(self) -> Any:
        """Возвращает следующий товар в списке"""
        if self.index < len(self.category_obj.products_in_list):
            product = self.category_obj.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
