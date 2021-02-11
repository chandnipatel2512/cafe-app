# List key names:
def key_names(list_name=[]):
    return list(list_name[0].keys())


# List value types:
def value_types(list_name=[]):
    return [type(v) for v in list_name[0].values()]


# Function for string input with cancellation option
# Return to be updated
def string_with_cancel(key_name=""):
    while True:
        user_input = input(
            f"\nPlease enter the {key_name}. Alternatively, please enter 0 to cancel.\n"
        )
        if not user_input:
            print(f"\nPlease enter a valid {key_name}")
        else:
            break

    if user_input != "0":
        return user_input
    else:
        return "main_menu"