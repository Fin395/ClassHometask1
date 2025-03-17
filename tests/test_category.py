import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone


def test_init_category(first_category: Category, second_category: Category) -> None:
    """Проверяем корректность инициализации экземпляров класса Category (первой и второй категории)"""
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(first_category.products_in_list) == 3
    assert second_category.name == "Телевизоры"
    assert (
        second_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(second_category.products_in_list) == 1
    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_products_property(first_category: Category) -> None:
    """Проверяем корректность добавления нового товара в категорию"""
    assert first_category.products == [
        'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.',
        'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
        'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.'
    ]


def test_add_product(first_category: Category, forth_product: Product) -> None:
    """Проверяем корректность добавления нового товара в список"""
    assert len(first_category.products_in_list) == 3
    first_category.add_product(forth_product)
    assert len(first_category.products_in_list) == 4


def test_add_product_error(first_category: Category) -> None:
    """Проверяем возбуждение ошибки при попытке добавить в категорию посторонний объект"""
    with pytest.raises(TypeError):
        first_category.add_product("Not a product")
    assert len(first_category.products_in_list) == 3


def test_add_product_smartphone(first_category: Category, first_smartphone: Smartphone) -> None:
    """Проверяем корректность добавления нового смартфона в список"""
    assert len(first_category.products_in_list) == 3
    first_category.add_product(first_smartphone)
    assert len(first_category.products_in_list) == 4
    assert first_category.products_in_list[-1].name == "Samsung Galaxy S23 Ultra"


def test_category_str(first_category: Category) -> None:
    """Проверяем корректность строкового вывода экземпляра категории"""
    assert str(first_category) == "Смартфоны, количество продуктов: 27 шт."
