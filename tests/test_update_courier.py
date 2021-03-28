from src.functions.operational_functions import update_courier
from src.functions.list_functions import *
from unittest.mock import Mock, patch
import unittest

mock_input = Mock()
select_item_mock = Mock()
update_mock = Mock()


@patch("builtins.input", mock_input)
class Testing(unittest.TestCase):
    def setUp(self):
        mock_input.reset_mock()

    # Test update courier function to ensure it updates item from specified list
    @patch("src.functions.operational_functions.select_item", select_item_mock)
    @patch("src.functions.operational_functions.update", update_mock)
    def test_update_courier1(
        self,
    ):
        courier_list = [
            {"id": "0123", "name": "DHL", "phone": "07874567266"},
            {"id": "4567", "name": "Royal Mail", "phone": "07874567277"},
        ]
        select_item_mock.return_value = ["4567", "Royal Mail"]
        mock_input.side_effect = ["a", "Parcel Force", ""]
        update_mock = ""

        test_update_courier = [
            {"id": "0123", "name": "DHL", "phone": "07874567266"},
            {"id": "4567", "name": "Parcel Force", "phone": "07874567277"},
        ]

        expected = test_update_courier
        actual = update_courier(courier_list)
        assert expected == actual
