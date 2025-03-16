from src.smartphone import Smartphone


def test_init_first_smartphone(first_smartphone: Smartphone, second_smartphone: Smartphone) -> None:
    """Проверяем корректность инициализации объектов класса Smartphone """
    assert first_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert first_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert first_smartphone.price == 180000.0
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == 95.5
    assert first_smartphone.model == "S23 Ultra"
    assert first_smartphone.memory == 256
    assert first_smartphone.color == "Серый"
    assert second_smartphone.name == "Iphone 15"
    assert second_smartphone.description == "512GB, Gray space"
    assert second_smartphone.price == 210000.0
    assert second_smartphone.quantity == 8
    assert second_smartphone.efficiency == 98.2
    assert second_smartphone.model == "15"
    assert second_smartphone.memory == 512
    assert second_smartphone.color == "Gray space"


def test_add_smartphones(first_smartphone: Smartphone, second_smartphone: Smartphone) -> None:
    """Проверяем корректность сложения объектов класса Smartphone"""
    assert first_smartphone + second_smartphone == 2580000.0


def test_add_smartphones_error(first_smartphone: Smartphone, second_smartphone: Smartphone) -> None:
    """Проверяем возбуждение ошибки TypeError при сложении объектов разных классов"""

