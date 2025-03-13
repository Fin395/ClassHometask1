from typing import Optional

from src.product import Product


class Category:
    """Создаем класс Category с атрибутами"""

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[list] = None):
        """Метод для инициализации экземпляра класса Category. Задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product) -> None:
        """Метод, который добавляет новый продукт в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Создаем геттер для атрибута "self.__products", который будет выводить список товаров в виде строк"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def products_in_list(self) -> list:
        """
        Создаем геттер для атрибута "self.__products" для получения информации о количества товара в списке при
        инициализации экземпляров класса "Category" """
        return self.__products
