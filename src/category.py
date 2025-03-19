from typing import Optional, Any
from src.base_order_category import OrderCategory
from src.exception import ZeroQuantityProduct
from src.product import Product


class Category(OrderCategory):
    """Создаем класс Category с атрибутами"""

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[list] = None) -> None:
        """Метод для инициализации экземпляра класса Category. Задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        """Создаем метод для строкового отображения экземпляра класса с подсчетом общего количества товара"""
        total_amount = 0
        for product in self.__products:
            total_amount += product.quantity
        return f"{self.name}, количество продуктов: {total_amount} шт."

    def add_product(self, product: Product) -> None:
        """Метод, который добавляет новый продукт в категорию"""
        if isinstance(product, Product):
            if product.quantity == 0:
                raise ZeroQuantityProduct("Товар с нулевым количеством не может быть добавлен")
            try:
                self.__products.append(product)
            except ZeroQuantityProduct as e:
                print(f"Ошибка при добавлении товара: {e}")
            else:
                Category.product_count += 1
                print("Товар добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError("Объект не является продуктом")

    @property
    def products(self) -> list[str]:
        """Создаем геттер для атрибута "self.__products", который будет выводить список товаров в виде списка строк"""
        product_list = []
        for product in self.__products:
            product = f"{str(product)}"
            product_list.append(product)
        return product_list

    #    Переопределил данный метод (теперь товар выводится списком строк) для корректного подсчета
    #    количества наименований товара в категории (len(category1.products), len(category2.products) в соответствии
    #    с кодом main.py
    #    @property
    #    def products(self) -> str:
    #        """Создаем геттер для атрибута "self.__products", который будет выводить список товаров в виде строк"""
    #        product_str = ""
    #        for product in self.__products:
    #            product_str += f"{str(product)}\n"
    #        return product_str

    @property
    def products_in_list(self) -> list:
        """
        Создаем геттер для атрибута "self.__products" для получения информации о количества товара в списке при
        инициализации экземпляров класса "Category" """
        return self.__products

    def middle_price(self) -> Any:
        """Метод подсчета среднего ценника товаров с обработкой ошибки, если список товаров пустой"""
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
