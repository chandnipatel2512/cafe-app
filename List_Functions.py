# Number items in list:
def number_items(list, index=1):
    for item in list:
        print(index, item)
        index += 1
    return ""


# Create new item in list
def create(item="", list=[]):
    print(
        f"\nPlease provide the name of the {item} you would like to add to the menu, alternatively, please enter 0 to cancel."
    )
    new_item = input()
    return "" if new_item == "0" else list.append(new_item)


# Update item in list
def update(item="", list=[]):
    print(
        f"\nPlease provide the number of the {item} you would like to update, alternatively, please enter 0 to cancel."
    )
    z = int(input())
    if z == 0:
        return ""
    else:
        print(f"\nPlease provide the updated {item} name ")
        updated_item = input()
        list[z - 1] = updated_item


# Delete item in list
def delete(item="", list=[]):
    print(
        f"\nPlease provide the number of the {item} you would like to delete, alternatively, please enter 0 to cancel."
    )
    z = int(input())
    return "" if z == 0 else list.remove(list[z - 1])


# Add new order
def new_order(list):
    global new_order
    order = {
        "customer_name": "",
        "customer_address": "",
        "customer_phone": "",
        "courier": "",
        "status": "preparing",
    }
    print("Please provide the customer name, alternatively, please enter 0 to cancel")
    name = input()
    if name == "0":
        return ""
    else:
        order.update({"customer_name": name})
    print("Please provide the customer address.")
    address = input()
    order.update({"customer_address": address})
    print("Please provide the customer phone number.")
    phone_number = input()
    order.update({"customer_phone": phone_number})
    print("Please select the courier for this order.")
    number_items(list)
    courier = int(input())
    order.update({"courier": list[courier - 1]})
    print(order)
    return list.append(dict(order))
    print(list.append(dict(order)))