import pytest

from src.main import Product, Category


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
        name="Телевизор", description="Посмотреть вечерком", products=["product_one"]
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
