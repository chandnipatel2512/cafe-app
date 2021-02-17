import uuid

# Number items in list:
def number_items(list, index=1):
    for item in list:
        print(index, item)
        index += 1
    return ""


# Print list without id number
def print_list(list_name=[]):
    list_without_id = [{k: v for k, v in d.items() if k != "id"} for d in list_name]
    print(number_items(list_without_id))
    return


# Generate UUID
def uuid_generator():
    return uuid.uuid4()


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
def string_with_cancel(list_name=[], key_name="", input_name=""):
    existing_items = list_values(list_name, key_name)
    while True:
        user_input = input(
            f"\nPlease enter the {input_name}. Alternatively, enter 0 to cancel.\n"
        )
        if not user_input:
            print(f"\nPlease enter a valid {input_name}")
        elif user_input in existing_items:
            print(f"\nThis {input_name} already exists.")
        else:
            break
    return user_input


# Function for a string input
def string_input(list_name=[], key_name="", input_name=""):
    existing_items = list_values(list_name, key_name)
    while True:
        user_input = input(f"\nPlease enter the {input_name}.\n")
        if not user_input:
            print(f"\nInvalid input")
        elif user_input in existing_items:
            print(f"\nThis {input_name} already exists.")
        else:
            break
    return user_input


# Function for an integer input
def integer_input(list_name=[], input_name=""):
    while True:
        try:
            user_input = int(input(f"\nPlease enter the {input_name}.\n"))
            if not user_input or user_input < 0:
                raise ValueError
        except (ValueError, IndexError):
            print(f"\nInvalid input")
        else:
            break
    return user_input


# Function for a float input
def float_input(list_name=[], input_name=""):
    while True:
        try:
            user_input = float(input(f"\nPlease enter the {input_name}.\n"))
            if not user_input or user_input < 0:
                raise ValueError
        except (ValueError, IndexError):
            print(f"\nInvalid input")
        else:
            break
    return user_input


# Function for selecting an item from a list - may change to just courier
def select_item(external_list=[]):
    options = print_list(external_list)
    uuid = list_values(external_list, "id")
    while True:
        try:
            user_input = int(input(f"\nPlease select the relevant number.\n"))
            list_item = external_list[user_input - 1]
            if not user_input or user_input <= 0:
                raise ValueError
        except (ValueError, IndexError):
            print(f"\nInvalid input")
        else:
            break
    return uuid[user_input - 1]


# Function for selecting an item from the product list with cancellation option
def select_product(product_list=[]):
    options = print_list(product_list)
    uuid = list_values(product_list, "id")
    product_name = list_values(product_list, "name")
    while True:
        try:
            user_input = int(
                input(
                    f"\nPlease enter the number of the product you would like to add to this order, enter 0 once complete.\n"
                )
            )
            list_item = product_list[user_input - 1]
            if user_input == 0:
                return 0, 0
            elif not user_input or user_input < 0:
                raise ValueError
        except (ValueError, IndexError):
            print(f"\nInvalid input")
        else:
            break
    return uuid[user_input - 1], product_name[user_input - 1]



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