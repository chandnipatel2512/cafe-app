# Number items in list:
def number_items(list, index=1):
    for item in list:
        print(index, item)
        index += 1
    return ""


# Create new item in list
def create(item="", list=[], input=input):
    new_item = input(
        f"\nPlease provide the name of the {item} you would like to add to the menu, alternatively, please enter 0 to cancel.\n"
    )
    if new_item == "0":
        return ""
    else:
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
    print(
        f"\nPlease provide the number of the {item} you would like to delete, alternatively, please enter 0 to cancel."
    )
    z = int(input())
    return "" if z == 0 else list.remove(list[z - 1])


# Add new order
def new_order(couriers=[], orders=[], input=input):
    print("Please provide the customer name, alternatively, please enter 0 to cancel.")
    name = input()
    if name == "0":
        return ""
    print("Please provide the customer address.")
    address = input()
    print("Please provide the customer phone number.")
    phone_number = input()
    print("Please select the courier for this order.")
    number_items(couriers)
    courier = couriers[int(input()) - 1]
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
    print(
        "Please provide the order number for which you would like to update the status, alternatively, please enter 0 to cancel."
    )
    number_items(orders)
    number = int(input())
    if number == 0:
        return ""
    else:
        print("Please provide the latest order status.")
        updated_status = input()
        orders[number - 1]["status"] = updated_status
    print(orders)


# Update order
def update_order(orders=[], couriers=[], input=input):
    print(
        "Please provide the order number you would like to update, alternatively, please enter 0 to cancel."
    )
    number_items(orders)
    number = int(input())
    if number == 0:
        return ""
    else:
        print("What would you like to update?")
        keys = orders[0].keys()
        number_items(keys)
        option = int(input())
        if option == 1:
            print("Please provide the updated customer name.")
            name = input()
            orders[number - 1]["customer_name"] = name
        if option == 2:
            print("Please provide the updated customer address.")
            address = input()
            orders[number - 1]["customer_address"] = address
        if option == 3:
            print("Please provide the updated contact number.")
            phone = input()
            orders[number - 1]["customer_phone"] = phone
        if option == 4:
            print("Please select the new courier for this order.")
            number_items(couriers)
            courier = couriers[int(input()) - 1]
            orders[number - 1]["courier"] = courier
        if option == 5:
            print("Please provide the latest order status.")
            updated_status = input()
            orders[number - 1]["status"] = updated_status


# Delete order
def delete_order(orders=[], input=input):
    print(
        "Please provide the order number you would like to delete, alternatively, please enter 0 to cancel."
    )
    number_items(orders)
    number = int(input())
    if number == 0:
        return ""
    else:
        orders.remove(orders[number - 1])
    print(orders)
