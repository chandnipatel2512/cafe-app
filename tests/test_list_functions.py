from src.functions.list_functions import *
from unittest.mock import Mock, patch
import unittest


mock_input = Mock()
list_values_mock = Mock()
print_list_mock = Mock()


@patch("builtins.input", mock_input)
class Testing(unittest.TestCase):
    def setUp(self):
        mock_input.reset_mock()

    # Test cancel option when string_with_cancel function is called
    @patch("src.functions.list_functions.list_values", list_values_mock)
    def test_string_with_cancel1(self):
        empty = []
        list_values_mock.return_value = []
        mock_input.side_effect = [""]
        expected = ""
        actual = string_with_cancel(empty, "name", "product name")
        assert expected == actual

    # Test string_with_cancel function when item entered already exists in list
    @patch("src.functions.list_functions.list_values", list_values_mock)
    def test_string_with_cancel2(self):
        empty = []
        list_values_mock.return_value = ["apple", "banana"]
        mock_input.side_effect = ["apple", "banana", "cherries"]
        expected = "cherries"
        actual = string_with_cancel(empty, "name", "product name")
        assert expected == actual

    # Test string_input function when user enters nothing
    @patch("src.functions.list_functions.list_values", list_values_mock)
    def test_string_input1(self):
        empty = []
        list_values_mock.return_value = []
        mock_input.side_effect = ["", "apple"]
        expected = "apple"
        actual = string_input(empty, "name", "product name")
        assert expected == actual

    # Test string_input function when item entered already exists in list
    @patch("src.functions.list_functions.list_values", list_values_mock)
    def test_string_input2(self):
        empty = []
        list_values_mock.return_value = ["apple", "banana"]
        mock_input.side_effect = ["apple", "banana", "mangoes"]
        expected = "mangoes"
        actual = string_input(empty, "name", "product name")
        assert expected == actual

    # Test float_input function, error cases tested - string input and empty input
    def test_float_input(self):
        mock_input.side_effect = ["Should generate type error", "", 2.50]
        expected = 2.50
        actual = float_input("price")
        assert expected == actual

    # Test integer_input function, error cases tested - string input and empty input
    def test_integer_input(self):
        mock_input.side_effect = ["Should generate type error", "", 4]
        expected = 4
        actual = integer_input("price")
        assert expected == actual

    # Test function for selecting an item from a list when cancel option is called
    @patch("src.functions.list_functions.list_values", print_list_mock)
    @patch("src.functions.list_functions.list_values", list_values_mock)
    def test_select_item1(self):
        list = [
            {"id": "0123", "name": "Americano", "price": 1.5},
            {"id": "01234", "name": "Decaf", "price": 2.5},
        ]
        print_list_mock.return_value = []
        list_values_mock.return_value = ["Americano", "Decaf"]
        mock_input.side_effect = [""]
        expected = 0, 0
        actual = select_item(list, "name")
        assert expected == actual

    # Test function for selecting an item from a list when there is an IndexError and TypeError
    @patch("src.functions.list_functions.print_list", print_list_mock)
    @patch("src.functions.list_functions.list_values", list_values_mock)
    def test_select_item2(self):
        list = [
            {"id": "0123", "name": "Americano", "price": 1.5},
            {"id": "01234", "name": "Decaf", "price": 2.5},
        ]
        print_list_mock.return_value = []
        list_values_mock.return_value = ["Americano", "Decaf"]
        mock_input.side_effect = [2, "Should generate TypeError", 1]
        expected = ("Decaf", "Decaf")
        actual = select_item(list, "name")
        assert expected == actual