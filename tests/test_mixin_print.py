from typing import Any
import pytest
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_mixin_print_product(capsys: pytest.CaptureFixture) -> None:
    """Проверяем, что миксин выводит в консоль информацию о создаваемом экземпляре класса Product"""
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 5, 180000.0)"


def test_mixin_print_smartphone(capsys: pytest.CaptureFixture) -> None:
    """Проверяем, что миксин выводит в консоль информацию о создаваемом экземпляре дочернего класса Smartphone"""
    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone('Iphone 15', '512GB, Gray space', 8, 210000.0)"


def test_mixin_print_lawngrass(capsys: pytest.CaptureFixture) -> None:
    """Проверяем, что миксин выводит в консоль информацию о создаваемом экземпляре дочернего класса LawnGrass"""
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass('Газонная трава', 'Элитная трава для газона', 20, 500.0)"
