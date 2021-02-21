from src.functions.list_functions import *
from src.functions.operational_functions import *
from src.db.load_data import *

# Open main menu
def main_menu():
    options = [
        {"Option": "Exit app"},
        {"Option": "Show products menu"},
        {"Option": "Show couriers menu"},
        {"Option": "Show orders menu"},
    ]
    print_list(options)
    y = int(input("\nPlease select an option from the above menu.\n"))

    if y == 0:
        print("\nThank you for using this app, goodbye")
        os.system("clear")

    elif y == 1:
        return os.system("clear"), product_menu(product)

    elif y == 2:
        return os.system("clear"), courier_menu(courier)

    elif y == 3:
        return os.system("clear"), order_menu(order, courier, basket, product)

    else:
        print("\nPlease select a valid option ")
        return main_menu()


# View product menu
def product_menu(product_list=[]):
    options = [
        {"Option": "Return to main menu"},
        {"Option": "Show products"},
        {"Option": "Create new product"},
        {"Option": "Update product"},
        {"Option": "Delete product"},
    ]
    print_list(options)
    y = int(input("\nPlease select an option from the above menu.\n"))

    if y == 0:
        return main_menu()

    elif y == 1:
        os.system("clear")
        print_list(product_list)
        return product_menu(product_list)

    elif y == 2:
        os.system("clear")
        product_list = create_product(product_list)
        return product_menu(product_list)

    elif y == 3:
        os.system("clear")
        product_list = update_product(product_list)
        return product_menu(product_list)

    elif y == 4:
        os.system("clear")
        product_list = delete_product(product_list)
        return product_menu(product_list)

    else:
        print("\nPlease select a valid option ")
        return product_menu(product_list)


# View courier menu
def courier_menu(courier_list=[]):
    options = [
        {"Option": "Return to main menu"},
        {"Option": "Show couriers"},
        {"Option": "Create new courier"},
        {"Option": "Update courier"},
        {"Option": "Delete courier"},
    ]
    print_list(options)
    y = int(input("\nPlease select an option from the above menu.\n"))

    if y == 0:
        return main_menu()

    elif y == 1:
        os.system("clear")
        print_list(courier_list)
        return courier_menu(courier_list)

    elif y == 2:
        os.system("clear")
        courier_list = create_courier(courier_list)
        return courier_menu(courier_list)

    elif y == 3:
        os.system("clear")
        courier_list = update_courier(courier_list)
        return courier_menu(courier_list)

    elif y == 4:
        os.system("clear")
        courier_list = delete_courier(courier_list)
        return courier_menu(courier_list)

    else:
        print("\nPlease select a valid option ")
        return courier_menu(courier_list)


# View order menu
def order_menu(order_list=[], courier_list=[], basket_list=[], product_list=[]):
    options = [
        {"Option": "Return to main menu"},
        {"Option": "Show orders"},
        {"Option": "Create new order"},
        {"Option": "Update order status"},
        {"Option": "Update order"},
        {"Option": "Update basket"},
        {"Option": "Delete order"},
    ]
    print_list(options)
    y = int(input("\nPlease select an option from the above menu.\n"))

    if y == 0:
        return main_menu()

    if y == 1:
        os.system("clear")
        print_list(order_list)
        return order_menu(order_list, courier_list, basket_list, product_list)

    if y == 2:
        os.system("clear")
        basket, order = create_order(
            order_list, courier_list, basket_list, product_list
        )
        return order_menu(order_list, courier_list, basket_list, product_list)

    if y == 3:
        os.system("clear")
        order = update_order_status(order_list)
        return order_menu(order_list, courier_list, basket_list, product_list)

    if y == 4:
        os.system("clear")
        basket, order = update_order(
            order_list, courier_list, basket_list, product_list
        )
        return order_menu(order_list, courier_list, basket_list, product_list)

    if y == 5:
        os.system("clear")
        basket = update_basket(order_list)
        return order_menu(
            order_list=[], courier_list=[], basket_list=[], product_list=[]
        )

    if y == 6:
        os.system("clear")
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