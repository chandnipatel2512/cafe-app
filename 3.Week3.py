from List_Functions import number_items, create, update, delete
from File_Functions import load_data

# Load products and couriers data
load_data("Products.txt")
products = list1

load_data("Couriers.txt")
couriers = list1

# Open main menu
def main_menu():
    options = ["Exit app", "Show product menu", "Show couriers menu"]
    print("\nPlease select from the below:")
    print(number_items(options))
    y = int(input())

    if y == 1:
        print("\nThank you for using this app, goodbye")
        return close_file()

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
        f"View updated {item} menu"
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

    elif y==6:
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
        return close_file()

    else:
        print("\nPlease select a valid option ")
        return post_updates_menu(item, list)


# Save updated product list, this overwrites the original file
def close_file():
    updated_products = "\n".join(str(x) for x in products)
    file = open("Products.txt", "w+")
    file.write(updated_products)
    file.close()

    updated_couriers = "\n".join(str(x) for x in couriers)
    file = open("Couriers.txt", "w+")
    file.write(updated_couriers)
    file.close()


main_menu()
