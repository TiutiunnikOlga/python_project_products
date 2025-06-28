from src.main import Product, Category
import unittest


def test_main(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.quantity == 5
    assert product.price == 180000.0


def test_main_category(category):
    assert category.name == "Телевизор"
    assert category.description == "Посмотреть вечерком"
    assert category.products == "Продукт"


def test_main_category_count(category_one):
    assert category_one.name == "Телевизор"
    assert category_one.description == "Посмотреть вечерком"


def test_main_count(category_two):
    assert category_two.product_count == 10
    assert category_two.category_count == 3


def test_empty_category(empty_category):
    print(f"Список продуктов: {empty_category}")
    assert empty_category.product_count == 10


def test_category_count():
    Category.category_count = 0  # Сброс счетчика
    Category.product_count = 0

    category1 = Category("К1", "Описание", [Product("P1", "Desc", 100.0, 5)])
    category2 = Category(
        "К2",
        "Описание",
        [Product("P2", "Desc", 200.0, 8), Product("P3", "Desc", 300.0, 10)],
    )

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_empty():
    category = Category("Пустая категория", "Описание", [])
    assert len(category.products) == 0
    assert category.product_count == 3


class TestProduct(unittest.TestCase):
    def setUp(self):
        # Создаем тестовый продукт
        self.product = Product(
            "Test Product", "Описание тестового продукта", 1000.0, 10
        )

    def tearDown(self):
        # Очистка после каждого теста
        Category.category_count = 0
        Category.product_count = 0

    def test_init(self):
        # Проверяем корректность инициализации
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "Описание тестового продукта")
        self.assertEqual(self.product.price, 1000.0)
        self.assertEqual(self.product.quantity, 10)

    def test_new_product(self):
        # Проверка создания продукта через класс
        product_dict = {
            "name": "Новый продукт",
            "description": "Описание",
            "price": 2000.0,
            "quantity": 5,
        }
        new_product = Product.new_product(product_dict)

        self.assertEqual(new_product.name, "Новый продукт")
        self.assertEqual(new_product.price, 2000.0)
        self.assertEqual(new_product.quantity, 5)


class TestCategory(unittest.TestCase):
    def setUp(self):
        # Создаем тестовые продукты
        self.product1 = Product("P1", "Описание", 1000, 5)
        self.product2 = Product("P2", "Описание", 2000, 3)

        # Создаем категорию
        self.category = Category(
            "Тестовая категория", "Описание категории", [self.product1, self.product2]
        )

    def test_init(self):
        # Проверка инициализации категории
        self.assertEqual(self.category.name, "Тестовая категория")
        self.assertEqual(len(self.category.products), 2)
        self.assertEqual(Category.category_count, 1)
        self.assertEqual(Category.product_count, 2)

    def test_products_property(self):
        # Проверка работы свойства products
        products = self.category.products
        self.assertEqual(len(products), 2)
        self.assertIsInstance(products, list)

    def test_set_products(self):
        # Проверка установки нового списка продуктов
        new_products = [Product("P4", "Описание", 4000, 1)]
        self.category.products = new_products

        self.assertEqual(len(self.category.products), 1)
        self.assertEqual(Category.product_count, 1)


def test_str_representation(category_three):
    assert str(category_three) == "Смартфоны, количество продуктов: 5 шт."


def test_multiple_products():
    product1 = Product("Samsung", "Описание", 10000, 5)
    product2 = Product("Apple", "Описание", 20000, 3)
    category = Category("Смартфоны", "Описание", [product1, product2])
    assert str(category) == "Смартфоны, количество продуктов: 8 шт."
