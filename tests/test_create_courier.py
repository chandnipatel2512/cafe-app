from src.functions.operational_functions import create_courier
from src.functions.list_functions import *
from unittest.mock import Mock, patch
import unittest

uuid_generator_mock = Mock()
string_with_cancel_mock = Mock()
string_input_mock = Mock()
update_mock = Mock()


class Testing(unittest.TestCase):

    # Test create function to ensure it adds items to specified list
    @patch("src.functions.operational_functions.uuid_generator", uuid_generator_mock)
    @patch(
        "src.functions.operational_functions.string_with_cancel",
        string_with_cancel_mock,
    )
    @patch("src.functions.operational_functions.string_input", string_input_mock)
    @patch("src.functions.operational_functions.update", update_mock)
    def test_create_courier1(
        self,
    ):
        courier_list = []
        uuid_generator_mock.return_value = "0123"
        string_with_cancel_mock.return_value = "DHL"
        string_input_mock.return_value = "07874567266"
        update_mock = ""

        test_courier = [{"id": "0123", "name": "DHL", "phone": "07874567266"}]

        expected = test_courier
        actual = create_courier(courier_list)
        assert expected == actual

    # Test create function to ensure it cancels if user enters empty input
    @patch("src.functions.operational_functions.uuid_generator", uuid_generator_mock)
    @patch(
        "src.functions.operational_functions.string_with_cancel",
        string_with_cancel_mock,
    )
    @patch("src.functions.operational_functions.update", update_mock)
    def test_create_courier2(
        self,
    ):
        courier_list = []
        uuid_generator_mock.return_value = "0123"
        string_with_cancel_mock.return_value = ""
        update_mock = ""

        test_courier = []

        expected = test_courier
        actual = create_courier(courier_list)
        assert expected == actual