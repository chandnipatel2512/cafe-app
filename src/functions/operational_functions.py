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


# Create new courier and save to database
def create_courier(list_name=[]):
    new_courier = {}
    new_courier["id"] = uuid_generator()
    user_input = string_with_cancel(list_name, "name", "name")
    if user_input != "0":
        new_courier["name"] = user_input
        new_courier["phone"] = string_input(list_name, "number")
        sql = sql_add("courier", new_courier)
        update(new_courier, sql)
        list_name.append(new_courier)
    return list_name


# Update a product
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
            "Name: Please enter any key to update the name, or press enter to continue."
        )
        if user_input != "":
            updated_name = string_input(list_name, "name", "name")
            update_product["name"] = updated_name
            list_name[index - 1]["name"] = updated_name
        user_input = input(
            "Price: Please enter any key to update the price, or press enter to continue."
        )
        if user_input != "":
            updated_price = float_input(list_name, "price")
            update_product["price"] = updated_price
            list_name[index - 1]["price"] = updated_price
        sql = sql_update("product", update_product)
        update(update_product, sql)
    return list_name


# Add products to basket
def create_basket(list_name=[], transaction_id=""):
    new_basket = {}
    new_basket["id"] = uuid_generator()
    new_basket["transaction_id"] = transaction_id
    user_input = 1
    user_input, product_name = select_product(product)
    while user_input != 0:
        new_basket["product_id"] = user_input
        new_basket["product_name"] = product_name
        sql = sql_add("basket", new_basket)
        update(new_basket, sql)
        list_name.append(new_basket)
        user_input, product_name = select_product(product)
    return list_name


# Create new order
def create_order(list_name=[]):
    new_transaction = {}
    id = uuid_generator()
    new_transaction["id"] = id
    user_input = string_with_cancel(list_name, "customer_name", "customer name")
    if user_input != "0":
        new_transaction["customer_name"] = user_input
        new_transaction["customer_address"] = string_input(
            list_name, "customer_address", "customer address"
        )
        new_transaction["customer_phone"] = string_input(
            list_name, "customer_phone number", "customer phone number"
        )
        new_transaction["courier_id"] = select_item(courier)
        new_transaction["order_status"] = order_status()
        sql = sql_add("transaction", new_transaction)
        update(new_transaction, sql)
        list_name.append(new_transaction)
        create_basket(basket, id)
    return list_name