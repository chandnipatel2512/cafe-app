from src.functions.list_functions import *
from unittest.mock import Mock, patch
import unittest


class Testing(unittest.TestCase):
    def test_float_input(self):
        empty = []
        mock_input = Mock()
        mock_input.side_effect = ["Should generate type error", "", 2.50]

        expected = 2.50
        actual = float_input(empty, "price", mock_input)
        assert expected == actual


if __name__ == "__main__":
    unittest.main()