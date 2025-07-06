class Product:
    name: str
    description: str
    __price: float
    quantity: int
    color: str

    def __init__(self, name, description, price: float, quantity, color="Не указан"):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return f"{self.quantity * self.price + other.quantity * other.price}"
        raise TypeError

    @classmethod
    def new_product(cls, new_product: dict):
        name = new_product.get("name", "")
        description = new_product.get("description", "")
        price = new_product.get("price")
        quantity = new_product.get("quantity")
        color = new_product.get("color")
        return cls(name, description, price, quantity, color)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        new_price = float(new_price)
        if not isinstance(new_price, (int, float)):
            print("Ошибка: цена должна быть числом")
            return
        if new_price <= 0:
            print("Цена не должна быть нулевой или отрицательной")
            return

        # Если новая цена ниже текущей, запрашиваем подтверждение
        if new_price < self.__price:
            confirm = input(
                f"Текущая цена: {self.__price}. "
                f"Новая цена: {new_price}. "
                "Вы уверены, что хотите установить цену ниже? (y/n): "
            )
            if confirm.lower() != "y":
                print("Цена не изменена")
                return

        # Присваиваем новую цену
        self.__price = new_price
        print(f"Цена успешно изменена на {self.__price}")


class Category:
    name: str
    description: str
    _products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {sum(product.quantity for product in self.__products)} шт."

    @property
    def products(self) -> list:
        return self.__products

    @products.setter
    def products(self, value: list):
        self.__products = value
        Category.product_count = len(self.__products)

    def add_product(self, product: Product):
        """Метод для добавления одного продукта, проверяем принадлежность к классу Product"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)

    print(new_product)
    print(category1)
    print(product1 + product2)
