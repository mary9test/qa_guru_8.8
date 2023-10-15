"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        pass

    def test_product_check_quantity_true(self, product):
        assert product.check_quantity(999) is True

    def test_product_check_quantity_false(self, product):
        assert product.check_quantity(1001) is False

    def test_product_check_quantity_equal(self, product):
        assert product.check_quantity(1000) is True


    def test_product_buy(self, product):
        product.buy(999)
        assert product.quantity == 1


    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    @pytest.fixture
    def cart(self):
        return Cart()

    def test_add_product(self, cart):
        cart.add_product(product, 10)
        assert product in cart.products
        assert cart.products[product] == 10