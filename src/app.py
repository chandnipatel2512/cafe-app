from src.db.core import connection, get_data
from .functions.file_functions import load_data, save_data
from .functions.list_functions import (
    number_items,
    create,
    update,
    delete,
    new_order,
    update_order_status,
    update_order,
    delete_order,
)


select_all_products = "SELECT * FROM product"
select_all_couriers = "SELECT * FROM courier"

products = get_data("product")

print(products)
# Load data
products, couriers, orders = load_data()

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
        return save_data(products, couriers, orders)

    elif y == 1:
        return operations_menu("product", "price", products)

    elif y == 2:
        return operations_menu("courier", "phone", couriers)

    elif y == 3:
        return orders_menu()

    else:
        print("\nPlease select a valid option ")
        return main_menu()


# View operations menu
def operations_menu(item="", detail="", list=[]):
    options = [
        "Return to main menu",
        f"Show {item}s",
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
        return operations_menu(item, detail, list)

    elif y == 2:
        return create(item, detail, list), operations_menu(item, detail, list)

    elif y == 3:
        return update(item, detail, list), operations_menu(item, detail, list)

    elif y == 4:
        number_items(list)
        return delete(item, list), operations_menu(item, detail, list)

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
        return new_order(couriers, orders), orders_menu()

    if y == 3:
        return update_order_status(orders), orders_menu()

    if y == 4:
        return update_order(orders, couriers), orders_menu()

    if y == 5:
        return delete_order(orders), orders_menu()

    else:
        print("\nPlease select a valid option ")
        return orders_menu()


main_menu()
