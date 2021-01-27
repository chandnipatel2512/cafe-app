from File_Functions import load_txt_data, save_txt_data, load_csv_data
from List_Functions import number_items, create, update, delete, new_order

# Load products and couriers data
products = load_txt_data("Products.txt")
couriers = load_txt_data("Couriers.txt")
orders = load_csv_data("Orders.csv")
print(orders, type(orders))

# Open main menu
def main_menu():
    options = [
        "Exit app",
        "Show products menu",
        "Show couriers menu",
        "Show orders menu",
    ]
    print("\nPlease select from the below:")
    print(number_items(options, 0))
    y = int(input())

    if y == 0:
        print("\nThank you for using this app, goodbye")
        return save_txt_data("Products.txt", products), save_txt_data(
            "Couriers.txt", couriers
        )

    elif y == 1:
        print("\nThe current products are as follows:")
        number_items(products)
        return operations_menu("product", products)

    elif y == 2:
        print("\nThe current couriers are as follows:")
        number_items(couriers)
        return operations_menu("courier", couriers)

    elif y == 3:
        return orders_menu()

    else:
        print("\nPlease select a valid option ")
        return main_menu()


# View operations menu
def operations_menu(item="", list=[]):
    options = [
        "Return to main menu",
        f"Show {item} menu",
        f"Create new {item}",
        f"Update {item}",
        f"Delete {item}",
        f"View updated menu",
    ]
    print("\nPlease select from the below:")
    print(number_items(options, 0))
    y = int(input())

    if y == 0:
        return main_menu()

    elif y == 1:
        number_items(list)
        return operations_menu(item, list)

    elif y == 2:
        return create(item, list), operations_menu(item, list)

    elif y == 3:
        number_items(list)
        return update(item, list), operations_menu(item, list)

    elif y == 4:
        number_items(list)
        return delete(item, list), operations_menu(item, list)

    elif y == 5:
        return operations_menu(item, list)

    else:
        print("\nPlease select a valid option ")
        return operations_menu(item, list)


# View orders menu
def orders_menu():
    options = [
        "Return to main menu",
        "Print orders to screen",
        "Create new order",
        "Update order status",
        "Update order",
        "Delete order",
    ]
    print("\nPlease select from the below:")
    print(number_items(options, 0))
    y = int(input())

    if y == 0:
        return main_menu()

    if y == 1:
        number_items(orders)
        return orders_menu()

    if y == 2:
        return new_order(couriers), orders_menu()

    if y == 3:
        return orders_menu()

    if y == 4:
        return orders_menu()

    if y == 5:
        return orders_menu()

    else:
        print("\nPlease select a valid option ")
        return orders_menu()


main_menu()
