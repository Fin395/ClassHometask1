class ZeroQuantityProduct(Exception):
    """Создаем пользовательский класс исключения"""

    def __init__(self, *args: list, **kwargs: dict) -> None:
        """Инициализация экземпляра класса"""
        if args:
            self.message = args[0]
        else:
            self.message = "Товар с нулевым количеством не может быть добавлен"

    def __str__(self) -> str:
        """Магический метод, который возвращает текст ошибки"""
        return self.message
