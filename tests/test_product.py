from src.main import Product


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