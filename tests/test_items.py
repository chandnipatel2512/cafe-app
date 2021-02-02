from src.functions.list_functions import number_items, create, update, delete

# Test create function to ensure it adds items to specified list
def test_create():
    test_items = ["Apple", "Banana", "Cherries"]

    def mock_input(msg):
        return "Mango"

    expected = ["Apple", "Banana", "Cherries", "Mango"]
    actual = create("product", test_items, mock_input)
    assert expected == actual
    print("test_create = PASS")


test_create()

# Test create function to ensure it cancels and returns "" when user want to cancel and return to operations menu
def test_create_cancel():
    test_items = ["Apple", "Banana", "Cherries"]

    def mock_input(msg):
        return "0"

    expected = ""
    actual = create("product", test_items, mock_input)
    assert expected == actual
    print("test_create_cancel = PASS")


test_create_cancel()

# Test update function to ensure it returns "" when user want to cancel and return to operations menu
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
    print("test_update_item: PASSED")


test_update()

# Test update function to ensure it returns "" when user want to cancel and return to operations menu
def test_update_cancel():
    test_items = ["Apple", "Banana", "Cherries"]

    def mock_input(msg):
        return "0"

    expected = ["Apple", "Banana", "Cherries"]
    actual = update("product", test_items, mock_input)
    assert actual == expected
    print("test_update_cancel: PASSED")


test_update_cancel()