"""
Протестируйте классы из модуля homework/models.py
"""


import pytest

from homework8.models import Product
from homework8.models import Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(10) is True  # Проверка на True
        assert product.check_quantity(1001) is False  # Проверка на False

    def test_product_buy(self, product):
        product.buy(10)  # Покупка 10 продуктов
        assert product.quantity == 990  # Проверка остатка

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(1001)  # Попытка купить больше, чем есть в наличии, ожидаем ValueError

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product, 5)
        assert cart.products == {product: 5}

    def test_remove_product(self, product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product, 2)
        assert cart.products == {product: 3}

    def test_remove_product_full(self, product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product)
        assert cart.products == {}

    def test_remove_product_invalid(self, product, cart):
        with pytest.raises(KeyError):
            cart.remove_product(product)

    def test_get_total_price(self, product, cart):
        cart.add_product(product, 5)
        total_price = cart.get_total_price()
        assert total_price == (5 * 100.0)

    def test_buy(self, product, cart):
        cart.add_product(product, 5)
        cart.buy()
        assert product.quantity == 995
        assert cart.products == {}

    def test_buy_insufficient_quantity(self, product, cart):
        cart.add_product(product, 1001)  # Попытка купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            cart.buy()