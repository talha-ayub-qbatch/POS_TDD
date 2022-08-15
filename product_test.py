import unittest


class ProductTest(unittest.TestCase):
    def setup(self):
        self.fixture = self._Fixture()

    def test_add_the_product(self):
        self.fixture.given_add_the_product(code=1, name="egg", price=200)
        self.fixture.when_add_the_product_operation_is_called()
        self.fixture.then_status_should_be(True)

    def test_update_the_product_name_with_valid_id(self):
        self.fixture.given_update_the_product_name(1, "Bread")
        self.fixture.when_update_the_product_name_operation_is_called()
        self.fixture.then_status_should_be(True)

    def test_update_the_product_name_with_invalid_id(self):
        self.fixture.given_update_the_product_name("id", "Bread")
        self.fixture.when_update_the_product_name_operation_is_called()
        self.fixture.then_status_should_be(False)

    def test_update_the_product_price_with_valid_id(self):
        self.fixture.given_update_the_product_price(1, 300)
        self.fixture.when_update_the_product_price_operation_is_called()
        self.fixture.then_status_should_be(True)

    def test_update_the_product_price_with_invalid_id(self):
        self.fixture.given_update_the_product_price("id", 300)
        self.fixture.when_update_the_product_price_operation_is_called()
        self.fixture.then_status_should_be(False)

    class _Fixture(unittest.TestCase):
        def __init__(self):
            self.product = Product()

        def given_add_the_product(self, code, name, price):
            self.code = code
            self.name = name
            self.price = price

        def given_update_the_product_name(self, code, name):
            self.code = code
            self.name = name

        def given_update_the_product_price(self, code, price):
            self.code = code
            self.price = price

        def when_add_the_product_operation_is_called(self):
            self.status = self.product.update_product(
                self.code, self.name, self.price)

        def when_update_the_product_name_operation_is_called(self):
            self.status = self.product.add_product(self.code, self.name)

        def when_update_the_product_price_operation_is_called(self):
            self.status = self.product.add_product(self.code, self.name)

        def then_status_should_be(self, expected_result):
            self.assertTrue(self.status, expected_result)


if __name__ == "__main__":
    unittest.main()
