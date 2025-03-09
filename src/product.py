class Product:
    """Создаем класс Product с атрибутами"""

    name: str
    description: str
    price: float
    quantity: int

    @classmethod
    def new_product(cls, one_more_product: dict):
        """Создаем класс-метод для получения экземпляра на основе параметров товара из входного словаря"""
        name, description, price, quantity = one_more_product.values()
#        for product in product_str:
#            if one_more_product["name"] == product.name:
#                product.quantity += one_more_product["quantity"]
#                if product.price > one_more_product["price"]:
#                    product.price = product.price
#                else:
#                    product.price = one_more_product["price"]
#            else:
        return cls(name, description, price, quantity)

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
