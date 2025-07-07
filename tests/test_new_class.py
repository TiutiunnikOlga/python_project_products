from src.main import Product


def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    print(message)
    assert message.out.strip() == (
        "<class 'src.main.Product'>(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, "
        "200MP камера, 180000.0, 5)"
    )
