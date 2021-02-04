# Number items in list:
def number_items(list, index=1):
    for item in list:
        print(index, item)
        index += 1
    return


# Create new item in list
def create(item="", list=[], input=input):
    new_item = input(
        f"\nPlease provide the name of the {item} you would like to add to the menu, alternatively, please enter 0 to cancel.\n"
    )
    if new_item != "0":
        list.append(new_item)
    return list


# Update item in list
def update(item="", list=[], input=input):
    number_items(list)
    z = input(
        f"\nPlease provide the number of the {item} you would like to update, alternatively, please enter 0 to cancel.\n"
    )
    if z != "0":
        updated_item = input(f"\nPlease provide the updated {item} name.")
        list[int(z) - 1] = updated_item
    return list


# Delete item in list
def delete(item="", list=[], input=input):
    z = input(
        f"\nPlease provide the number of the {item} you would like to delete, alternatively, please enter 0 to cancel."
    )
    return "" if z == "0" else list.remove(list[int(z) - 1])


# Add new order
def new_order(couriers=[], orders=[], input=input):
    name = input(
        "Please provide the customer name, alternatively, please enter 0 to cancel."
    )
    if name == "0":
        return
    address = input("Please provide the customer address.")
    phone_number = input("Please provide the customer phone number.")
    number_items(couriers)
    courier = couriers[int(input("Please select the courier for this order.") - 1)]
    order = {
        "customer_name": name,
        "customer_address": address,
        "customer_phone": phone_number,
        "courier": courier,
        "status": "preparing",
    }
    return orders.append(dict(order))


# Update order status
def update_order_status(orders=[], input=input):
    number_items(orders)
    number = int(
        input(
            "Please provide the order number for which you would like to update the status, alternatively, please enter 0 to cancel."
        )
    )
    if number == 0:
        return ""
    else:
        updated_status = input("Please provide the latest order status.")
        orders[number - 1]["status"] = updated_status
    return orders


# Update order
def update_order(orders=[], couriers=[], input=input):
    number_items(orders)
    number = int(
        input(
            "Please provide the order number you would like to update, alternatively, please enter 0 to cancel."
        )
    )
    if number == 0:
        return ""
    else:
        keys = orders[0].keys()
        number_items(keys)
        option = int(input("What would you like to update?"))
        if option == 1:
            name = input("Please provide the updated customer name.")
            orders[number - 1]["customer_name"] = name
        if option == 2:
            address = input("Please provide the updated customer address.")
            orders[number - 1]["customer_address"] = address
        if option == 3:
            phone = input("Please provide the updated contact number.")
            orders[number - 1]["customer_phone"] = phone
        if option == 4:
            number_items(couriers)
            courier = couriers[
                int(input("Please select the new courier for this order.")) - 1
            ]
            orders[number - 1]["courier"] = courier
        if option == 5:
            updated_status = input("Please provide the latest order status.")
            orders[number - 1]["status"] = updated_status


# Delete order
def delete_order(orders=[], input=input):
    number_items(orders)
    number = int(
        input(
            "Please provide the order number you would like to delete, alternatively, please enter 0 to cancel."
        )
    )
    if number == 0:
        return ""
    else:
        orders.remove(orders[number - 1])
    print(orders)
