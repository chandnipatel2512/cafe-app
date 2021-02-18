from src.db.core import connection, get_data, update
from src.functions.list_functions import *
from src.functions.sql_functions import *
import uuid

# Create new product and save to database
def create_product(list_name=[]):
    new_product = {}
    new_product["id"] = uuid_generator()
    user_input = string_with_cancel(list_name, "name", "name")
    if user_input != "0":
        new_product["name"] = user_input
        new_product["price"] = float_input(list_name, "price")
        sql = sql_add("product", new_product)
        update(new_product, sql)
        list_name.append(new_product)
    return list_name


# Update a product and save to database
def update_product(list_name=[]):
    print_list(list_name)
    index = int(
        input(
            "Please enter the number of the product you would like to update, alternatively, enter 0 to cancel.\n"
        )
    )
    if index != 0:
        updated_product = list_name[index - 1]
        user_input = input(
            "\nName: Please enter any key to update the name, or press enter to continue.\n"
        )
        if user_input != "":
            updated_product["name"] = list_name[index - 1]["name"] = string_input(
                list_name, "name", "name"
            )
        user_input = input(
            "\nPrice: Please enter any key to update the price, or press enter to continue.\n"
        )
        if user_input != "":
            updated_product["price"] = list_name[index - 1]["price"] = float_input(
                list_name, "price"
            )
        sql = sql_update("product", updated_product)
        update(updated_product, sql)
    return list_name


# Delete a product and update database
def delete_product(list_name):
    print_list(list_name)
    index = int(
        input(
            "Please enter the number of the product you would like to delete, alternatively, enter 0 to cancel.\n"
        )
    )
    deleted_product = list_name[index - 1]
    id = list_name[index - 1]["id"]
    if index != 0:
        del list_name[index - 1]
        sql = sql_delete("product", id)
        update(deleted_product, sql)
    return list_name


# Create new courier and save to database
def create_courier(list_name=[]):
    new_courier = {}
    new_courier["id"] = uuid_generator()
    user_input = string_with_cancel(list_name, "name", "name")
    if user_input != "0":
        new_courier["name"] = user_input
        new_courier["phone"] = string_input(list_name, "phone", "phone number")
        sql = sql_add("courier", new_courier)
        update(new_courier, sql)
        list_name.append(new_courier)
    return list_name


# Update a courier and save to database
def update_courier(list_name=[]):
    print_list(list_name)
    index = int(
        input(
            "Please enter the number of the courier you would like to update, alternatively, enter 0 to cancel.\n"
        )
    )
    if index != 0:
        update_courier = list_name[index - 1]
        user_input = input(
            "\nName: Please enter any key to update the name, or press enter to continue.\n"
        )
        if user_input != "":
            update_courier["name"] = list_name[index - 1]["name"] = string_input(
                list_name, "name", "name"
            )
        user_input = input(
            "\nPhone number: Please enter any key to update the phone number, or press enter to continue.\n"
        )
        if user_input != "":
            update_courier["phone"] = list_name[index - 1]["phone"] = string_input(
                list_name, "phone"
            )
        sql = sql_update("courier", update_courier)
        update(update_courier, sql)
    return list_name


# Delete a courier and update database
def delete_courier(list_name):
    print_list(list_name)
    index = int(
        input(
            "Please enter the number of the courier you would like to delete, alternatively, enter 0 to cancel.\n"
        )
    )
    deleted_courier = list_name[index - 1]
    id = list_name[index - 1]["id"]
    if index != 0:
        del list_name[index - 1]
        sql = sql_delete("courier", id)
        update(deleted_courier, sql)
    return list_name


# Add products to basket and save to database
def create_basket(transaction_id="", basket_list=[], product_list=[]):
    new_basket = {}
    new_basket["transaction_id"] = transaction_id
    user_input = 1
    user_input, product_name = select_product(product_list)
    while user_input != 0:
        new_basket["id"] = uuid_generator()
        new_basket["product_id"] = user_input
        new_basket["product_name"] = product_name
        sql = sql_add("basket", new_basket)
        update(new_basket, sql)
        basket_list.append(new_basket)
        user_input, product_name = select_product(product_list)
    return basket_list


# Create new order and save to database
def create_order(order_list=[], courier_list=[], basket_list=[], product_list=[]):
    new_transaction = {}
    id = uuid_generator()
    new_transaction["id"] = id
    user_input = string_with_cancel(order_list, "customer_name", "customer name")
    if user_input != "0":
        new_transaction["customer_name"] = user_input
        new_transaction["customer_address"] = string_input(
            order_list, "customer_address", "customer address"
        )
        new_transaction["customer_phone"] = string_input(
            order_list, "customer_phone", "customer phone number"
        )
        new_transaction["courier_id"] = select_item(courier_list)
        new_transaction["order_status"] = order_status()
        sql = sql_add("transaction", new_transaction)
        update(new_transaction, sql)
        order_list.append(new_transaction)
        basket_list = create_basket(id, basket_list, product_list)
    return basket_list, order_list


# Update products in basket and save to database
def update_basket(transaction_id="", basket_list=[], product_list=[]):
    user_input = "1"
    while user_input == "1" or user_input == "2":
        order_list = list_for_id(transaction_id, "transaction_id", basket_list)
        products = list_values(order_list, "product_name")
        number_items(products)
        index = int(
            input(
                "\nPlease select the number of the basket you would like to update.\n"
            )
        )
        user_input = input(
            "\nEnter 1 to update or 2 to delete, alternatively, enter anything else to cancel.\n"
        )
        selected_basket = order_list[index - 1]
        basket_list_index = basket_list.index(selected_basket)
        if user_input == "1":
            product_id, product_name = select_product(product_list)
            selected_basket["product_id"] = basket_list[basket_list_index][
                "product_id"
            ] = product_id
            selected_basket["product_name"] = basket_list[basket_list_index][
                "product_name"
            ] = product_name
            sql = sql_update("basket", selected_basket)
            update(selected_basket, sql)
        elif user_input == "2":
            id = order_list[index - 1]["id"]
            del basket_list[basket_list_index]
            sql = sql_delete("basket", id)
            update(selected_basket, sql)
    return basket_list


# Update order and save to database
def update_order(order_list=[], courier_list=[], basket_list=[], product_list=[]):
    print_list(order_list)
    index = int(
        input(
            "Please enter the number of the order you would like to update, alternatively, enter 0 to cancel.\n"
        )
    )
    if index != 0:
        updated_order = order_list[index - 1]
        user_input = input(
            "\nCustomer name: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            updated_order["customer_name"] = order_list[index - 1][
                "customer_name"
            ] = string_input(order_list, "customer_name", "customer_name")
        user_input = input(
            "\nCustomer adress: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            updated_order["customer_address"] = order_list[index - 1][
                "customer_address"
            ] = string_input(order_list, "customer_address", "customer_address")
        user_input = input(
            "\nCustomer phone number: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            updated_order["customer_phone"] = order_list[index - 1][
                "customer_phone"
            ] = string_input(order_list, "customer_phone", "customer_phone")
        user_input = input(
            "\nCourier: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            updated_order["courier_id"] = order_list[index - 1][
                "courier_id"
            ] = select_item(courier_list)
        user_input = input(
            "\nOrdered items: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            id = order_list[index - 1]["id"]
            basket_list = update_basket(id, basket_list, product_list)
    sql = sql_update("transaction", updated_order)
    update(updated_order, sql)
    return basket_list, order_list