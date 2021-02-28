import uuid
from tabulate import tabulate

# Print list without id numbers
def print_list(
    list_name=[],
    hidden_fields=["id", "courier_id", "transaction_id", "basket_id", "product_id"],
):
    print("\n")
    list_without_id = [
        {k: v for k, v in d.items() if k not in hidden_fields} for d in list_name
    ]  # Creates new list without id fields
    print(tabulate(list_without_id, headers="keys", showindex=True, tablefmt="grid"))
    print("\n")


# Generate UUID
def uuid_generator():
    return uuid.uuid4()


# List key names:
def key_names(list_name=[]):
    return list(list_name[0].keys())


# Product list of all data in list_name with specific id
def list_for_id(id="", list_name=[]):
    list = []
    for item in list_name:
        if id in item.values():
            list.append(item)
    return list


# List of all values in list of dictionaries for specific key
def list_values(list_name=[], key_name=""):
    return [d[key_name] for d in list_name]


# Function for a string input with cancellation option
def string_with_cancel(list_name=[], key_name="", input_name=""):
    existing_items = list_values(list_name, key_name)
    while True:
        user_input = input(
            f"\nPlease enter the {input_name}. Alternatively, press enter to cancel.\n"
        )
        if user_input in existing_items:
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
def integer_input(input_name=""):
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
def float_input(input_name=""):
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


# Function for selecting an item from a list (used for orders and couriers)
def select_item(item_list=[], item_name=""):
    options = print_list(item_list)
    uuid = list_values(item_list, "id")
    print(uuid)
    try:
        name = list_values(item_list, "name")
        print(name)
    except:
        name = uuid
    while True:
        try:
            index = input(
                f"\nPlease select the number of the {item_name}. Alternatively, press enter to cancel.\n"
            )
            if index == "":
                return 0, 0
            index = int(index)
            list_item = item_list[index]
            if index < 0:
                raise ValueError
        except (ValueError, IndexError, TypeError):
            print(f"\nInvalid input")
        else:
            break
    return uuid[index], name[index]


# Function for selecting an item from the product list with cancellation option
def select_product(product_list=[]):
    options = print_list(product_list)
    uuid = list_values(product_list, "id")
    product_name = list_values(product_list, "name")
    while True:
        try:
            user_input = input(
                f"\nPlease enter the number of the product you would like to add to this order, or press enter to return to the previous menu.\n"
            )
            if user_input == "":
                return "0", "0"
            user_input = int(user_input)
            list_item = product_list[user_input]
            if user_input < 0:
                raise ValueError
        except (ValueError, IndexError):
            print(f"\nInvalid input")
        else:
            break
    return uuid[user_input], product_name[user_input]


# Function for order status
def order_status():
    status_options = [
        {"Status": "Order placed"},
        {"Status": "Preparing"},
        {"Status": "Being delivered"},
        {"Status": "Delivered"},
    ]
    print_list(status_options)
    while True:
        try:
            user_input = int(input("\nPlease select the current order status.\n"))
            current_status = status_options[user_input]["Status"]
            if user_input == "" or user_input < 0:
                raise ValueError
        except (ValueError, IndexError):
            print(f"\nInvalid input")
        else:
            break
    return current_status