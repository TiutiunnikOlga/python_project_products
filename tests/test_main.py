from src.main import Product, Category

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
    category2 = Category("К2", "Описание", [Product("P2", "Desc", 200.0, 8), Product("P3", "Desc", 300.0, 10)])

    assert Category.category_count == 2
    assert Category.product_count == 3

def test_category_empty():
    category = Category("Пустая категория", "Описание", [])
    assert len(category.products) == 0
    assert category.product_count == 3

