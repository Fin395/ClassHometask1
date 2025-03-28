import pytest

from src.product_iterator import ProductIterator


def test_product_iterator(product_iterator: ProductIterator) -> None:
    """Проверяем корректность работы итератора"""
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator)
