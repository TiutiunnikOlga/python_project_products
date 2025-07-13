import pytest

from src.main import Category, Product


@pytest.fixture
def product_one():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


def product_two():
    return Product(
        name="Прекрасный телефон",
        description="10GB, Красный цвет, нет камеры",
        price=1000.0,
        quantity=1,
    )


@pytest.fixture
def product():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def category_one():
    return Category(
        name="Телевизор", description="Посмотреть вечерком", products=[product_one]
    )


@pytest.fixture
def category_two():
    return Category(
        name="Прекрасный телефон",
        description="10GB, Красный цвет, нет камеры",
        products=["product1", "product3"],
    )


@pytest.fixture
def category():
    return Category("Телевизор", "Посмотреть вечерком", "Продукт")


@pytest.fixture
def empty_category():
    return Category(name="Пустая категория", description="Без продуктов", products=[])


@pytest.fixture
def product_5():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def category_2(product):
    return Category("Смартфоны", "Описание категории", [product])


@pytest.fixture
def empty_category_2():
    return Category("Пустая категория", "Описание пустой категории", [])


@pytest.fixture
def category_three(product_one):
    return Category(
        name="Смартфоны",
        description="Смартфоны как средство коммуникации",
        products=[product_one],
    )


@pytest.fixture
def category_four(product_one, product_two):
    return Category(
        name="Телефоны",
        description="Мобильные устройства",
        products=[product_one, product_two],
    )


@pytest.fixture
def product_three():
    return Product(
        name="Прекрасный телефон",
        description="10GB, Красный цвет, нет камеры",
        price=1000.0,
        quantity=1,
    )
