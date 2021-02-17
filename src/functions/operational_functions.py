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
        update_product = list_name[index - 1]
        user_input = input(
            "\nName: Please enter any key to update the name, or press enter to continue.\n"
        )
        if user_input != "":
            update_product["name"] = list_name[index - 1]["name"] = string_input(
                list_name, "name", "name"
            )
        user_input = input(
            "\nPrice: Please enter any key to update the price, or press enter to continue.\n"
        )
        if user_input != "":
            update_product["price"] = list_name[index - 1]["price"] = float_input(
                list_name, "price"
            )
        sql = sql_update("product", update_product)
        update(update_product, sql)
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


# Add products to basket and save to database
def create_basket(transaction_id="", basket_list=[], product_list=[]):
    new_basket = {}
    new_basket["id"] = uuid_generator()
    new_basket["transaction_id"] = transaction_id
    user_input = 1
    user_input, product_name = select_product(product_list)
    while user_input != 0:
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
        create_basket(id, basket_list, product_list)
    return order_list