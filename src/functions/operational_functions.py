from src.functions.list_functions import *

# Create new item in list
def create_item(list_name=[], external_list=[]):
    keys = key_names(list_name)
    value_type = value_types(list_name)
    new_item = {}
    index = 0
    for key in keys:
        if key == "id":
            continue
        elif index == 0:
            input1 = string_with_cancel(list_name, key)
            if input1 == 0:
                return
            else:
                new_item[key] = input1
        elif key == "courier":
            print("\nCourier options:")
            courier_id, list_item = select_item(external_list, "name")
            new_item[key] = courier_id
        elif key == "order status":
            new_item[key] = order_status()
        elif value_type[index] == int:
            new_item[key] = integer_input(list_name, key)
        elif value_type[index] == float:
            new_item[key] = float_input(list_name, key)
        else:
            new_item[key] = string_input(list_name, key)
        index += 1
    return list_name.append(new_item)


# Update item in list
def update_item(list_name=[], external_list=[], name_of_list=""):
    list_item = ""
    update = input(
        "\nYou have opted to update an item, please enter 0 to cancel. Alternatively, enter anything else to continue.\n"
    )
    if update != "0":
        id, list_item = select_item(list_name, "name")
        keys = key_names(list_name)
        value_type = value_types(list_name)
        update = "1"
        while update == "1":
            print(number_items(keys))
            index = (
                integer_input(keys, "number of the item you would like to update")
            ) - 1
            key = keys[index]
            if key == "id":
                print(
                    "The id is a system generated number, this cannot be updated manually."
                )
                continue
            elif key == "courier":
                print("\nCourier options:")
                courier_id, list_item = select_item(external_list, "name")
                list_item[key] = courier_id
            elif key == "order status":
                list_item[key] = order_status()
            elif value_type[index] == int:
                list_item[key] = integer_input(list_name, key)
            elif value_type[index] == float:
                list_item[key] = float_input(list_name, key)
            else:
                list_item[key] = string_input(list_name, key)
            update = input(
                "\nPlease enter 1 if you would like to make another update to this item. Alternatively, enter anything else to return to the main menu.\n"
            )
    return list_item


# Delete item in list


# Update order status


# Update order


# Delete order
