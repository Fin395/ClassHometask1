from src.category import Category


def test_init_category(first_category: Category, second_category: Category) -> None:
    """Проверяем корректность инициализации экземпляров класса Category (первой и второй категории)"""
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
#    assert len(first_category.products) == 3
    assert second_category.name == "Телевизоры"
    assert (
        second_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
#    assert len(second_category.products) == 1
    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert first_category.product_count == 4
    assert second_category.product_count == 4