from src.product import Product


class Smartphone(Product):
    """Создаем класс Smartphone с атрибутами"""
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: float, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color




