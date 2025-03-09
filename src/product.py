from typing import Any


class Product:
    """Создаем класс Product с атрибутами"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, one_more_product: dict) -> Any:
        """Создаем класс-метод для получения экземпляра на основе параметров товара из входного словаря"""
        keys_list = []
        new_attributes = one_more_product.keys()
        for attribute in new_attributes:
            keys_list.append(attribute)
        if (
            keys_list[0] == "name"
            and keys_list[1] == "description"
            and keys_list[2] == "price"
            and keys_list[3] == "quantity"
        ):
            name, description, price, quantity = one_more_product.values()
        else:
            raise Exception("Ошибка: Проверьте корректность описания товара")
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Создаем геттер для получения значения цены как приватного атрибута "self.__price" """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Создаем сеттер для установки нового значения приватного атрибута "self.__price" """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            if new_price < self.__price:
                user_input = input("Вы уверены, что хотите понизить цену?\nY/N\n")
                if user_input == "N":
                    self.__price = self.__price
                else:
                    self.__price = new_price
