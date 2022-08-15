import unittest


class TransactionTest(unittest.TestCase):
    def setup(self):
        self.fixture = self._Fixture()

    def test_add_lineitem_in_transaction(self):
        self.fixture.given_lineitem(LineItem())
        self.fixture.when_add_lineitem_operation_is_called()
        self.fixture.then_status_should_be_this(True)

    def test_get_list_of_lineitems_in_trasaction(self):
        self.fixture.given_get_lineitems(LineItem())
        self.fixture.when_get_lineitems_operation_is_called()
        self.fixture.then_status_should_be_this(True)

    def test_display_total_of_transaction(self):
        self.fixture.given_display_total(2500)
        self.fixture.when_get_lineitems_operation_is_called()
        self.fixture.then_status_should_be_this(True)

    def test_display_void_iten_with_regular_item(self):
        self.fixture.given_void_item_with_regular_item(LineItem.itemlist)
        self.fixture.when_void_item_with_regular_item_operation_is_called()
        self.fixture.then_status_should_be_this(True)

    class _Fixture(unittest.TestCase):
        def __init__(self):
            self.transaction = Transaction()

        def given_lineitem(self, obj):
            self.obj = obj

        def given_get_lineitems(self, obj):
            self.list_obj = []
            self.list_obj.append(obj)

        def given_display_total(self, total):
            self.total = total

        def given_void_item_with_regular_item(self, itemlist):
            self.itemlist = itemlist

        def when_get_lineitems_operation_is_called(self):
            self.status = self.transaction.get_lineitems(self.total)

        def when_add_lineitem_operation_is_called(self):
            self.status = self.transaction.add_lineitem(self.obj)

        def when_void_item_with_regular_item_operation_is_called(self):
            self.status = self.transaction.display_all_item(self.itemlist)

        def then_status_should_be_this(self, expected_status):
            self.assertTrue(self.status, expected_status)


if __name__ == "__main__":
    unittest.main()
