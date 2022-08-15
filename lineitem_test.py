import unittest


class LineItemTest(unittest.TestCase):
    def setup(self):
        self.fixture = self._Fixture()

    def test_add_quantity_of_an_item(self):
        self.fixture.given_add_quantity(Product.code, 1)
        self.fixture.when_add_quantity_operation_is_called()
        self.fixture.then_status_should_be(True)

    def test_update_quantity_of_an_item(self):
        self.fixture.given_update_quantity(2, listitem=[])
        self.fixture.when_update_quantity_operation_is_called()
        self.fixture.then_status_should_be(True)

    def test_void_an_lineitem(self):
        self.fixture.given_void_lineitem(1, voiditem=True)
        self.fixture.when_void_item_operation_is_called()
        self.fixture.then_status_should_be(True)

    class _Fixture(unittest.TestCase):
        def __init__(self):
            self.lineitem = LineItem()

        def given_add_quantity(self, code, quantity):
            self.code = code
            self.quantity = quantity

        def given_update_quantity(self, quantity, item):
            self.quantity = quantity
            self.item = item

        def given_void_lineitem(self, code, void):
            self.code = code
            self.void = void

        def when_void_item_operation_is_called(self):
            self.status = self.lineitem.void_lineitem(self.code, self.void)

        def when_update_quantity_operation_is_called(self):
            self.status = self.lineitem.update_quantity(
                self.quantity, self.item)

        def when_add_quantity_operation_is_called(self):
            self.status = self.lineitem.add_quantity(self.code, self.quantity)

        def then_status_should_be(self, expected_result):
            self.assertTrue(self.status, expected_result)


if __name__ == "__main__":
    unittest.main()
