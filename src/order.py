from src.base_order_category import OrderCategory
from src.product import Product


class Order(OrderCategory):
    """Описываем дочерний класс от базового абстрактного класса OrderCategory"""

    product_name: str
    quantity: int
    amount: float

    product_count = 0
    ID = 1

    def __init__(self, product, quantity):
        """Конструктор инициализации экземпляра класса Order"""
        self.product = product
        self.quantity = quantity
        self.id = self.ID
        Order.ID += 1

    def get_order_id(self) -> int:
        """Метод, возвращающий значение порядкового номера заказа"""
        return self.id

    def __str__(self) -> str:
        """Создаем метод для строкового отображения экземпляра класса с подсчетом стоимости заказа"""
        if isinstance(self.product, Product):
            self.amount = self.quantity * self.product.price
            if self.quantity > self.product.quantity:
                return f"Заказ № {self.get_order_id()}: На складе отсутствует необходимое количество товара. Максимальное количество: {self.product.quantity} шт."
            else:
                return f"Заказ № {self.get_order_id()}: {self.product.name}, {self.quantity} шт., {self.amount} руб."
        else:
            raise TypeError("Попробуйте выбрать другой товар")

if __name__ == "__main__":

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    order1 = Order(product1, 3)
    order2 = Order(product1, 8)
    order3 = Order(product2, 9)
    order4 = Order(product2, 4)
    print(order1)
    print(order2)
    print(order3)
    print(order4)
