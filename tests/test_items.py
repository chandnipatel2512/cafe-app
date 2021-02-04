from src.functions.list_functions import number_items, create, update, delete
from unittest.mock import Mock

# Test create function to ensure it adds items to specified list
def test_create():
    test_items = ["Apple", "Banana", "Cherries"]

    def mock_input(msg):
        return "Mango"

    expected = ["Apple", "Banana", "Cherries", "Mango"]
    actual = create("product", test_items, mock_input)
    assert expected == actual


# Test create function to ensure it cancels and returns "" when user want to cancel and return to operations menu
def test_create_cancel():
    test_items = ["Apple", "Banana", "Cherries"]

    def mock_input(msg):
        return "0"

    expected = ["Apple", "Banana", "Cherries"]
    actual = create("product", test_items, mock_input)
    assert expected == actual


# Test update function to ensure it returns updated list when user want to cancel and return to operations menu
def test_update():
    test_items = ["Apple", "Banana", "Cherries"]

    item = "product"

    def mock_input(msg):
        if (
            msg
            == f"\nPlease provide the number of the {item} you would like to update, alternatively, please enter 0 to cancel.\n"
        ):
            return "1"
        else:
            return "Pear"

    expected = ["Pear", "Banana", "Cherries"]
    actual = update(item, test_items, mock_input)


# Test update function to ensure it returns unedited list when user want to cancel and return to operations menu
def test_update_cancel():
    test_items = ["Apple", "Banana", "Cherries"]

    def mock_input(msg):
        return "0"

    expected = ["Apple", "Banana", "Cherries"]
    actual = update("product", test_items, mock_input)
    assert actual == expected
