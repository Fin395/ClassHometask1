from src.main import Product
import pytest

def test_init_first_product(first_product: Product) -> None:
    """Проверяем корректность инициализации экземпляра класса Product (первый продукт)"""
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_init_second_product(second_product: Product) -> None:
    """Проверяем корректность инициализации экземпляра класса Product (второй продукт)"""
    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_init_third_product(third_product: Product) -> None:
    """Проверяем корректность инициализации экземпляра класса Product (третий продукт)"""
    assert third_product.name == "Xiaomi Redmi Note 11"
    assert third_product.description == "1024GB, Синий"
    assert third_product.price == 31000.0
    assert third_product.quantity == 14


def test_init_forth_product(forth_product: Product) -> None:
    """Проверяем корректность инициализации экземпляра класса Product (четвертый продукт)"""
    assert forth_product.name == '55" QLED 4K'
    assert forth_product.description == "Фоновая подсветка"
    assert forth_product.price == 123000.0
    assert forth_product.quantity == 7


def test_new_product_creation() -> None:
    """ Проверяем корректность создания нового продукта на основе данных из словаря """
    product_data = (
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    new_product = Product.new_product(product_data)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_new_product_creation_invalid_data() -> None:
    """ Проверяем вызов исключения, если в словаре некорректные данные """
    product_data = (
        {
            "price": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "name": 180000.0,
            "quantity": 5,
        }
    )
    with pytest.raises(Exception) as exc_info:
        Product.new_product(product_data)
    assert str(exc_info.value) == "Ошибка: Проверьте корректность описания товара"


def test_price_update_if_below_zero(capsys, forth_product):
    forth_product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_price_update_if_zero(capsys, forth_product):
    forth_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_price_update_if_above_zero(forth_product):
    forth_product.price = 200
    assert forth_product.price == 200


