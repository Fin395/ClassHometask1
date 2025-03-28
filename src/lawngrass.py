from src.product import Product


class LawnGrass(Product):
    """Создаем дочерний класс LawnGrass от класса Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализируем экземпляр дочернего класса LawnGrass с использованием super()"""

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
