class ZeroQuantityProduct(Exception):
    def __init__(self, *args, **kwargs):
        if args:
            self.message = args[0]
        else:
            self.message = "Товар с нулевым количеством не может быть добавлен"

    def __str__(self):
        return self.message
