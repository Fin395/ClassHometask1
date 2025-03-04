from src.main import Category, Product


def test_init_first_product(first_product: Product) -> None:
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_init_second_product(second_product: Product) -> None:
    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_init_third_product(third_product: Product) -> None:
    assert third_product.name == "Xiaomi Redmi Note 11"
    assert third_product.description == "1024GB, Синий"
    assert third_product.price == 31000.0
    assert third_product.quantity == 14


def test_init_forth_product(forth_product: Product) -> None:
    assert forth_product.name == '55" QLED 4K'
    assert forth_product.description == "Фоновая подсветка"
    assert forth_product.price == 123000.0
    assert forth_product.quantity == 7


def test_init_category(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(first_category.products) == 3
    assert second_category.name == "Телевизоры"
    assert (
        second_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(second_category.products) == 1
    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert first_category.product_count == 4
    assert second_category.product_count == 4
