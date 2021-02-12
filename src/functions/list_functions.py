# Number items in list:
def number_items(list, index=1):
    for item in list:
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
def list_values(list_name=[], key_name=""):
    return [d[key_name] for d in list_name]


# Function for a string input with cancellation option
# Return to be updated
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


# Function for selecting an item from a list
def select_item(list_name=[], external_list=[], key_name=""):
    external_items = list_values(external_list, key_name)
    print(number_items(external_items))
    while True:
        try:
            user_input = int(input(f"\nPlease select an id number.\n"))
            list_item = external_items[user_input - 1]
            if not user_input or user_input <= 0:
                raise ValueError
        except (ValueError, IndexError):
            print(f"\nInvalid input")
        else:
            break
    return list_item


# Function for order status
def order_status():
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
