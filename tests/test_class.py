from src.main import Product
import unittest


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError("Нельзя складывать смартфоны с другими типами")


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if isinstance(other, LawnGrass):
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError("Нельзя складывать газонную траву с другими типами")


class TestProductHierarchy(unittest.TestCase):
    def setUp(self):
        self.smartphone1 = Smartphone(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5,
            95.5,
            "S23 Ultra",
            256,
            "Серый",
        )
        self.smartphone2 = Smartphone(
            "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
        )
        self.grass1 = LawnGrass(
            "Газонная трава",
            "Элитная трава для газона",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый",
        )
        self.grass2 = LawnGrass(
            "Газонная трава 2",
            "Выносливая трава",
            450.0,
            15,
            "США",
            "5 дней",
            "Темно-зеленый",
        )

    def test_smartphone_attributes(self):
        self.assertEqual(self.smartphone1.name, "Samsung Galaxy S23 Ultra")
        self.assertEqual(self.smartphone1.memory, 256)
        self.assertEqual(self.smartphone1.efficiency, 95.5)

    def test_lawn_grass_attributes(self):
        self.assertEqual(self.grass1.name, "Газонная трава")
        self.assertEqual(self.grass1.country, "Россия")
        self.assertEqual(self.grass1.germination_period, "7 дней")

    def test_add_smartphones(self):
        result = self.smartphone1 + self.smartphone2
        self.assertEqual(result, 2580000.0)

    def test_add_lawn_grass(self):
        result = self.grass1 + self.grass2
        self.assertEqual(result, 16750.0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.smartphone1 + self.grass1

    def test_inheritance(self):
        self.assertTrue(isinstance(self.smartphone1, Product))
        self.assertTrue(isinstance(self.grass1, Product))

        self.assertTrue(issubclass(Smartphone, Product))
        self.assertTrue(issubclass(LawnGrass, Product))

    def test_str_method(self):
        expected_smartphone = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
        self.assertEqual(str(self.smartphone1), expected_smartphone)

        expected_grass = "Газонная трава, 500.0 руб. Остаток: 20 шт."
        self.assertEqual(str(self.grass1), expected_grass)
