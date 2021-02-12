from src.functions.list_functions import (
    number_items,
    key_names,
    value_types,
    string_with_cancel,
    string_input,
    integer_input,
    float_input,
    select_item,
    order_status,
)

# Create new item in list
def create(list=[], external_list=[]):
    keys = key_names(list)
    value_type = value_types(list)
    new_item = {}
    index = 0
    for key in keys:
        if index == 0:
            input = string_with_cancel(list, key)
            if input == 0:
                return
            else:
                new_item[key] = input
        elif key == "courier":
            new_item[key] = select_item(list, external_list, "name")
        elif key == "order status":
            new_item[key] = order_status()
        elif value_type[index] == int:
            new_item[key] = integer_input(list, key)
        elif value_type[index] == float:
            new_item[key] = float_input(list, key)
        else:
            new_item[key] = string_input(list, key)
        index += 1
    return list.append(new_item)


# Update item in list


# Delete item in list


# Update order status


# Update order


# Delete order
