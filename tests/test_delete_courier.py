from src.functions.operational_functions import delete_courier
from src.functions.list_functions import *
from unittest.mock import Mock, patch
import unittest

select_item_mock = Mock()
update_mock = Mock()


class Testing(unittest.TestCase):

    # Test delete courier function to ensure it deletes item from specified list
    @patch("src.functions.operational_functions.select_item", select_item_mock)
    @patch("src.functions.operational_functions.update", update_mock)
    def test_delete_courier1(
        self,
    ):
        courier_list = [
            {"id": "0123", "name": "DHL", "phone": "07874567266"},
            {"id": "4567", "name": "Royal Mail", "phone": "07874567277"},
        ]
        select_item_mock.return_value = "4567", "Royal Mail"
        update_mock = ""

        test_delete_courier = [{"id": "0123", "name": "DHL", "phone": "07874567266"}]

        expected = test_delete_courier
        actual = delete_courier(courier_list)
        assert expected == actual
