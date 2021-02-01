from src.functions.list_functions import number_items, create, update, delete

# Test create function to ensure it adds items to specified list
def test_create():
    test_items = ["Apple", "Banana", "Cherries"]

    def mock_input(msg):
        return "Mango"

    expected = ["Apple", "Banana", "Cherries", "Mango"]
    actual = create(mock_input, "product", test_items)
    assert expected == actual
    print("test_create = PASS")


test_create()

# Test create function to ensure it cancels and returns "" when user want to cancel and return to operations menu
def test_create_cancel():
    test_items = ["Apple", "Banana", "Cherries"]

    def mock_input(msg):
        return "0"

    expected = ""
    actual = create(mock_input, "product", test_items)
    print(expected, actual)
    assert expected == actual
    print("test_create_cancel = PASS")


test_create_cancel()

# Test update function to ensure it returns "" when user want to cancel and return to operations menu
def test_update():
    test_items = ["Apple", "Banana", "Cherries"]

    # def mock_number_items(test_items):
    #     pass

    def mock_input(msg, item="product"):
        return "0", "Pear"
        if (
            msg
            == "Please provide the number of the product you would like to update, alternatively, please enter 0 to cancel."
        ):
            print("1")
            return "1"
        elif msg == "Please provide the updated product name.":
            return "Pear"

    expected = ["Pear", "Banana", "Cherries"]
    actual = update(mock_input, "product", test_items)
    assert actual == expected
    print("test_update_item: PASSED")


test_update()

# Test update function to ensure it returns "" when user want to cancel and return to operations menu
def test_update_cancel():
    test_items = ["Apple", "Banana", "Cherries"]

    def mock_input(msg):
        return "0"

    expected = ""
    actual = update(mock_input, "product", test_items)
    assert actual == expected
    print("test_update_cancel: PASSED")


test_update_cancel()