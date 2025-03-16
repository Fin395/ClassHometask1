import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def first_product() -> Product:
    """Создаем фикстуру для тестирования первого продукта"""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def second_product() -> Product:
    """Создаем фикстуру для тестирования второго продукта"""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def third_product() -> Product:
    """Создаем фикстуру для тестирования третьего продукта"""
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def forth_product() -> Product:
    """Создаем фикстуру для тестирования четвертого продукта"""
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def first_category() -> Category:
    """Создаем фикстуру для тестирования первой категории"""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def second_category() -> Category:
    """Создаем фикстуру для тестирования второй категории"""
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def product_with_amount1() -> Product:
    """Фикстура продукта1 для проверки метода '__add__'"""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_with_amount2() -> Product:
    """Фикстура продукта2 для проверки метода '__add__'"""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_iterator(first_category: Category) -> ProductIterator:
    """Фикстура товара для проверки работы итератора"""
    return ProductIterator(first_category)
