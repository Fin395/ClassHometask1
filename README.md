# Проект 

Проект **ClassHometask1** - подготовительный этап для формирования ядра для интернет-магазина. 
В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.

# Описание проекта

На данном этапе в проекте реализовано описание основных сущностей и инициализации объектов.

Созданы два класса и инициализированы экземпляры каждого класса.

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/Fin395/ClassHometask1.git 
   ```
2. Перейдите в директорию проекта:
   ```
   cd ClassHometask1
   ```
3. Установите необходимые зависимости:
   ```
   pip install -r requirements.txt
   ```

## Использование

В модуле **"main.py"** реализована логика создания классов и инициализации экземпляров.

```
# Пример использования
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
category1 = Category(
"Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
[product1, product2, product3])
```

В проекте реализован функционал наследования классов.
Кроме того, проработан функционал, который добавляет продукт в категорию таким образом,
чтобы не было возможности добавить вместо продукта или его наследников любой другой объект.

Создан базовый абстрактный класс BaseProduct, который является родительским для класса продуктов,
а также базовый абстрактный класс OrderCategory, являющийся родительским для классов категорий и заказов.

Реализован класс-миксин, который при создании объекта печатает в консоль информацию о том, 
от какого класса и с какими параметрами создан объект.

```
# Пример использования

class Product(MixinPrint, BaseProduct):
   <тело кода>
   
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

>>> 
Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 5, 180000.0)
Product('Iphone 15', '512GB, Gray space', 8, 210000.0)
Product('Xiaomi Redmi Note 11', '1024GB, Синий', 14, 31000.0)
```

## Тестирование

В проекте для тестирования используются фикстуры.
Для запуска теста с оценкой покрытия воспользуйтесь командой:

```
   pytest --cov
```

Также проект предусматривает наличие файла с отчетом о покрытии кода тестами. 

## Вклад

Если вы хотите внести свой вклад, пожалуйста, создайте форк репозитория и отправьте пул-реквест.