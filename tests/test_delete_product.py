from src.functions.operational_functions import delete_product
from src.functions.list_functions import *
from unittest.mock import Mock, patch
import unittest

select_item_mock = Mock()
update_mock = Mock()


class Testing(unittest.TestCase):

    # Test delete product function to ensure it deletes item from specified list
    @patch("src.functions.operational_functions.select_item", select_item_mock)
    @patch("src.functions.operational_functions.update", update_mock)
    def test_delete_product1(
        self,
    ):
        product_list = [
            {"id": "0123", "name": "Apple", "price": 2.50},
            {"id": "4567", "name": "Banana", "price": 1.25},
        ]

        select_item_mock.return_value = "0123", "0123"
        update_mock = ""

        test_delete_product = [{"id": "4567", "name": "Banana", "price": 1.25}]

        expected = test_delete_product
        actual = delete_product(product_list)
        assert expected == actual
