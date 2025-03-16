import pytest

from src.lawngrass import LawnGrass


def test_init_first_grass(first_grass: LawnGrass, second_grass: LawnGrass) -> None:
    """Проверяем корректность инициализации объектов класса LawnGrass"""
    assert first_grass.name == "Газонная трава"
    assert first_grass.description == "Элитная трава для газона"
    assert first_grass.price == 500.0
    assert first_grass.quantity == 20
    assert first_grass.country == "Россия"
    assert first_grass.germination_period == "7 дней"
    assert first_grass.color == "Зеленый"
    assert second_grass.name == "Газонная трава 2"
    assert second_grass.description == "Выносливая трава"
    assert second_grass.price == 450.0
    assert second_grass.quantity == 15
    assert second_grass.country == "США"
    assert second_grass.germination_period == "5 дней"
    assert second_grass.color == "Темно-зеленый"


def test_add_grass(first_grass: LawnGrass, second_grass: LawnGrass) -> None:
    """Проверяем корректность сложения объектов класса LawnGrass"""
    assert first_grass + second_grass == 16750.0


def test_add_smartphones_error(first_grass: LawnGrass) -> None:
    """Проверяем возбуждение ошибки TypeError при сложении объектов разных классов"""
    with pytest.raises(TypeError):
        first_grass + 1
