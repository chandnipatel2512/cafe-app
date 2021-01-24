## START APP
## SHOW LIST OF OPTIONS TO USER AND ACCEPT NUMERICAL INPUT
## IF USER ENTERS 0 THEN EXIT APP
## IF USER ENTERS 1 THEN SHOW PRODUCT MENU
# IF USER ENTERS 0 RETURN TO MAIN MENU
# IF USER ENTERS 1 PRINT OUT PRODUCTS TO SCREEN
# IF USER ENTER 2 CREATE NEW PRODUCT
# ASK USER FOR THE NAME OF THE PRODUCT
# APPEND THIS TO THE LIST OF PRODUCTS
# STRETCH IF USER ENTERS 3 UPDATE PRODUCT
# ASK USER TO SELECT A PRODUCT TO UPDATE
# ASK USER FOR NEW NAME OF PRODUCT
# REPLACE PRODUCT AT SELECTED IDX WITH NEW NAME
# STRETCH IF USER ENTERS 4 DELETE PRODUCT
# ASK USER TO SELECT A PRODUCT TO DELETE
# REMOVE THIS ITEM FROM THE PRODUCT LIST

## Functions menu:
# number_items(list): To return a numbered list (used when showing the products and for menu options)
# main_menu(): To go to options when opening the app
# operations_menu(): To make changes to the menu
# create_product(): To create a new product
# updated_product(): To update a product
# delete_product(): To delete product

# Start app
products = [
    "Spinach, banana and peanut butter smoothie",
    "Grapefruit and orange juice",
    "Apple and kale smoothie",
]

# Number items in list:
def number_items(list):
    index = 0
    for item in list:
        print(index, item)
        index += 1
    return ""


def main_menu():
    options = ["Exit app", "Show product menu"]
    print("\nPlease select from the below:")
    print(number_items(options))
    y = int(input())

    if y == 0:
        print("\nThank you for using this app, goodbye")

    elif y == 1:
        print("\nThe current products are as follows:")
        number_items(products)
        return operations_menu()

    else:
        print("\nPlease select a valid option ")
        return main_menu()


# View operations menu
def operations_menu():
    options = [
        "Return to main menu",
        "Show product menu",
        "Create new product",
        "Update product",
        "Delete product",
    ]
    print("\nPlease select from the below:")
    print(number_items(options))
    y = int(input())

    if y == 0:
        return main_menu()

    elif y == 1:
        number_items(products)
        return operations_menu()

    elif y == 2:
        return create_product()

    elif y == 3:
        return updated_product()

    elif y == 4:
        return delete_product()

    else:
        print("\nPlease select a valid option ")
        return operations_menu()


# Create product
def create_product():
    print("\nPlease provide the name of the product you would like to add to the menu")
    new_product = input()
    products.append(new_product)
    return post_updates_menu()


# Update product
def updated_product():
    number_items(products)
    print("\nPlease provide the number of the product you would like to update ")
    z = int(input())
    print("\nPlease provide the updated product name ")
    updated_product = input()
    products[z] = updated_product
    return post_updates_menu()


# Delete product
def delete_product():
    number_items(products)
    print("\nPlease provide the number of the product you would like to delete ")
    z = int(input())
    products.remove(products[z])
    return post_updates_menu()


# View updated menu
def post_updates_menu():
    options = [
        "Show updated menu",
        "Make another update to the menu",
        "Return to main menu",
        "Exit app",
    ]
    print("\nPlease select from the below:")
    print(number_items(options))
    y = int(input())

    if y == 0:
        print("\n Updated menu:")
        number_items(products)
        return post_updates_menu()

    elif y == 1:
        return operations_menu()

    elif y == 2:
        return main_menu()

    elif y == 3:
        print("\nThank you for using this app, goodbye")

    else:
        print("\nPlease select a valid option ")
        return post_updates_menu()


main_menu()