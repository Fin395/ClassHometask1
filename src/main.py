from typing import Optional


class Product:
    """Создаем класс Product с атрибутами"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Создаем класс Category с атрибутами"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[list] = None):
        """Метод для инициализации экземпляра класса Category. Задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
