from src.functions.operational_functions import create_product
from src.functions.list_functions import *
from unittest.mock import Mock, patch
import unittest

uuid_generator_mock = Mock()
string_with_cancel_mock = Mock()
float_input_mock = Mock()
update_mock = Mock()


class Testing(unittest.TestCase):

    # Test create function to ensure it adds items to specified list
    @patch("src.functions.operational_functions.uuid_generator", uuid_generator_mock)
    @patch(
        "src.functions.operational_functions.string_with_cancel",
        string_with_cancel_mock,
    )
    @patch("src.functions.operational_functions.float_input", float_input_mock)
    @patch("src.functions.operational_functions.update", update_mock)
    def test_create_product(
        self,
    ):
        product_list = []
        uuid_generator_mock.return_value = "0123"
        string_with_cancel_mock.return_value = "Apple"
        float_input_mock.return_value = 2.50
        update_mock = ""

        test_product = [{"id": "0123", "name": "Apple", "price": 2.50}]

        expected = test_product
        actual = create_product(product_list)
        assert expected == actual


if __name__ == "__main__":
    unittest.main()
