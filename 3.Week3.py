from List_Functions import number_items, create, update, delete
from File_Functions import load_txt_data, save_txt_data, load_csv_data

# Load products and couriers data
products = load_txt_data("Products.txt")
couriers = load_txt_data("Couriers.txt")
orders = load_csv_data("Orders.csv")
print(orders, type(orders))

# Open main menu
def main_menu():
    options = ["Exit app", "Show products menu", "Show couriers menu"]
    print("\nPlease select from the below:")
    print(number_items(options))
    y = int(input())

    if y == 1:
        print("\nThank you for using this app, goodbye")
        return save_txt_data("Products.txt", products), save_txt_data("Couriers.txt", couriers)

    elif y == 2:
        print("\nThe current products are as follows:")
        number_items(products)
        return operations_menu("product", products)

    elif y == 3:
        print("\nThe current couriers are as follows:")
        number_items(couriers)
        return operations_menu("courier", couriers)

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
    print(number_items(options))
    y = int(input())

    if y == 1:
        return main_menu()

    elif y == 2:
        number_items(list)
        return operations_menu(item, list)

    elif y == 3:
        return create(item, list), operations_menu(item, list)

    elif y == 4:
        number_items(list)
        return update(item, list), operations_menu(item, list)

    elif y == 5:
        number_items(list)
        return delete(item, list), operations_menu(item, list)

    elif y == 6:
        return post_updates_menu(item, list)

    else:
        print("\nPlease select a valid option ")
        return operations_menu(item, list)


# View updated menu
def post_updates_menu(item="", list=[]):
    options = [
        f"Show updated {item} menu",
        f"Make another update to the {item} menu",
        "Return to main menu",
        "Exit app",
    ]
    print("\nPlease select from the below:")
    print(number_items(options))
    y = int(input())

    if y == 1:
        print("\n Updated menu:")
        number_items(list)
        return post_updates_menu(item, list)

    elif y == 2:
        return operations_menu(item, list)

    elif y == 3:
        return main_menu()

    elif y == 4:
        print("\nThank you for using this app, goodbye")
        return save_txt_data("Products.txt", products), save_txt_data("Couriers.txt", couriers)

    else:
        print("\nPlease select a valid option ")
        return post_updates_menu(item, list)


main_menu()
