# Number items in list:
def number_items(list_name=[], index=1):
    print("\n")
    for item in list_name:
        print(index, item)
        index += 1
    return ""


# List key names:
def key_names(list_name=[]):
    return list(list_name[0].keys())


# List value types:
def value_types(list_name=[]):
    return [type(v) for v in list_name[0].values()]


# List of all values in list of dictionaries for specific key
def list_values(list_name=[], key_name="name"):
    return [d[key_name] for d in list_name]


# Function for a string input with cancellation option
def string_with_cancel(list_name=[], key_name=""):
    existing_items = list_values(list_name, key_name)
    while True:
        user_input = input(
            f"\nPlease enter the {key_name}. Alternatively, please enter 0 to cancel.\n"
        )
        if not user_input:
            print(f"\nPlease enter a valid {key_name}")
        elif user_input in existing_items:
            print(f"\nThis {key_name} already exists.")
        else:
            break
    return user_input


# Function for a string input
def string_input(list_name=[], key_name=""):
    existing_items = list_values(list_name, key_name)
    while True:
        user_input = input(f"\nPlease enter the {key_name}.\n")
        if not user_input:
            print(f"\nInvalid input")
        elif user_input in existing_items:
            print(f"\nThis {key_name} already exists.")
        else:
            break
    return user_input


# Function for an integer input
def integer_input(list_name=[], key_name=""):
    while True:
        try:
            user_input = int(input(f"\nPlease enter the {key_name}.\n"))
            list_item = list_name[user_input - 1]
            if not user_input or user_input < 0:
                raise ValueError
        except (ValueError, IndexError):
            print(f"\nInvalid input")
        else:
            break
    return user_input


# Function for a float input
def float_input(list_name=[], key_name=""):
    while True:
        try:
            user_input = float(input(f"\nPlease enter the {key_name}.\n"))
            if not user_input or user_input < 0:
                raise ValueError
        except (ValueError, IndexError):
            print(f"\nInvalid input")
        else:
            break
    return user_input


# Function for selecting an item from an external list
def select_item(external_list=[], key_name=""):
    print(*external_list, sep="\n")
    external_items = list_values(external_list, key_name)
    while True:
        try:
            user_input = int(input(f"\nPlease select an id number.\n"))
            list_item = next(item for item in external_list if item["id"] == user_input)
            if not user_input or user_input <= 0:
                raise ValueError
        except (ValueError, IndexError, StopIteration):
            print(f"\nInvalid input")
        else:
            break
    return user_input, list_item


# Function for order status
def order_status():
    print("\nThe order status options are as follows:")
    status_options = ["Order placed", "Preparing", "Being delivered", "Delivered"]
    number_items(status_options)
    while True:
        try:
            user_input = int(input(f"\nPlease select the current order status.\n"))
            current_status = status_options[user_input - 1]
            if not user_input or user_input <= 0:
                raise ValueError
        except (ValueError, IndexError):
            print(f"\nInvalid input")
        else:
            break
    return status_options[user_input - 1]