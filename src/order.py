from src.base_order_category import OrderCategory
from src.exception import ZeroQuantityProduct
from src.product import Product


class Order(OrderCategory):
    """Описываем дочерний класс от базового абстрактного класса OrderCategory"""

    product_name: str
    quantity: int
    total_amount: float

    product_count = 0
    ID = 1

    def __init__(self, product: Product, quantity: int) -> None:
        """Конструктор инициализации экземпляра класса Order"""
        self.product = product
        self.id = self.ID
        Order.ID += 1
        try:
            if quantity == 0:
                raise ZeroQuantityProduct
            elif quantity > self.product.quantity:
                raise Exception
        except ZeroQuantityProduct as e:
            print(f"Заказ № {self.id}: Ошибка при добавлении товара в заказ: {e}")
        except Exception:
            print(
                f""
                f"Заказ № {self.id}:На складе отсутствует необходимое количество товара. "
                f"Максимальное количество: {self.product.quantity} шт."
            )
        else:
            self.quantity = quantity
            self.total_amount = self.get_total_amount()
            print("Товар добавлен")
        finally:
            print("Обработка добавления товара завершена")

    def get_total_amount(self) -> float:
        """Рассчитываем общую стоимость товара"""
        self.total_amount = self.quantity * self.product.price
        return self.total_amount

    def __str__(self) -> str:
        """Создаем метод для строкового отображения заказа"""
        return f"Заказ № {self.id}: {self.product.name}, {self.quantity} шт., {self.total_amount} руб."


if __name__ == "__main__":

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 18)
    order1 = Order(product1, 8)
    order2 = Order(product1, 4)
    print(order2)
    order3 = Order(product1, 0)
