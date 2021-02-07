from src.functions.list_functions import number_items, create, update, delete
from unittest.mock import Mock
import unittest

# Test create function to ensure it adds items to specified list
class Testing(unittest.TestCase):
    def test_create(self):
        empty = []
        mock_input = Mock()
        mock_input.side_effect = ["Apple", "Should generate ValueError", 2.50]

        test_product = [{"name": "Apple", "price": 2.50}]

        expected = test_product
        actual = create("product", "price", empty, mock_input)
        assert expected == actual


if __name__ == "__main__":
    unittest.main()

# Test create function to ensure it cancels and returns "" when user want to cancel and return to operations menu

# Test update function to ensure it returns updated list when user want to cancel and return to operations menu

# Test update function to ensure it returns unedited list when user want to cancel and return to operations menu
