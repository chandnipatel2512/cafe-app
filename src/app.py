from src.functions.list_functions import *
from src.functions.operational_functions import *
from src.db.load_data import *

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
        os.system("clear")
    elif y == 1:
        return product_menu(product)

    elif y == 2:
        return courier_menu(courier)

    elif y == 3:
        return order_menu(order, courier, basket, product)

    else:
        print("\nPlease select a valid option ")
        return main_menu()


# View product menu
def product_menu(product_list=[]):
    options = [
        "Return to main menu",
        "Show products",
        "Create new product",
        "Update product",
        "Delete product",
    ]
    print("\nPlease select from the below:")
    print(number_items(options, 0))
    y = int(input())

    if y == 0:
        return main_menu()

    elif y == 1:
        print_list(product_list)
        return product_menu(product_list)

    elif y == 2:
        product_list = create_product(product_list)
        return product_menu(product_list)

    elif y == 3:
        product_list = update_product(product_list)
        return product_menu(product_list)

    elif y == 4:
        product_list = delete_product(product_list)
        return product_menu(product_list)

    else:
        print("\nPlease select a valid option ")
        return product_menu(product_list)


# View courier menu
def courier_menu(courier_list=[]):
    options = [
        "Return to main menu",
        "Show couriers",
        "Create new courier",
        "Update courier",
        "Delete courier",
    ]
    print("\nPlease select from the below:")
    print(number_items(options, 0))
    y = int(input())

    if y == 0:
        return main_menu()

    elif y == 1:
        print_list(courier_list)
        return courier_menu(courier_list)

    elif y == 2:
        courier_list = create_courier(courier_list)
        return courier_menu(courier_list)

    elif y == 3:
        courier_list = update_courier(courier_list)
        return courier_menu(courier_list)

    elif y == 4:
        courier_list = delete_courier(courier_list)
        return courier_menu(courier_list)

    else:
        print("\nPlease select a valid option ")
        return courier_menu(courier_list)


# View order menu
def order_menu(order_list=[], courier_list=[], basket_list=[], product_list=[]):
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
        print_list(order_list)
        return order_menu(order_list, courier_list, basket_list, product_list)

    if y == 2:
        basket, order = create_order(
            order_list, courier_list, basket_list, product_list
        )
        return order_menu(order_list, courier_list, basket_list, product_list)

    if y == 3:
        order = update_order_status(order_list)
        return order_menu(order_list, courier_list, basket_list, product_list)

    if y == 4:
        basket, order = update_order(
            order_list, courier_list, basket_list, product_list
        )
        return order_menu(order_list, courier_list, basket_list, product_list)

    if y == 5:
        order = delete_order(order_list)
        return order_menu(
            order_list=[], courier_list=[], basket_list=[], product_list=[]
        )

    else:
        print("\nPlease select a valid option ")
        return order_menu(
            order_list=[], courier_list=[], basket_list=[], product_list=[]
        )


# Run app
main_menu()