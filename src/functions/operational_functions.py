from src.db.core import *
from src.functions.list_functions import *
from src.functions.sql_functions import *
import uuid

# Create new product and save to database
def create_product(product_list=[]):
    new_product = {}
    new_product["id"] = uuid_generator()
    user_input = string_with_cancel(product_list, "name", "name")
    if user_input != "":
        new_product["name"] = user_input
        new_product["price"] = float_input(product_list, "price")
        sql = sql_add("product", new_product)
        update(new_product, sql)
        product_list.append(new_product)
    return product_list


# Update a product and save to database
def update_product(product_list=[]):
    print_list(product_list)
    index = int(
        input(
            "Please enter the number of the product you would like to update, alternatively, press enter to cancel.\n"
        )
    )
    if index != "":
        updated_product = product_list[index]
        user_input = input(
            "\nName: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            updated_product["name"] = product_list[index]["name"] = string_input(
                product_list, "name", "name"
            )
        user_input = input(
            "\nPrice: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            updated_product["price"] = product_list[index]["price"] = float_input(
                product_list, "price"
            )
        sql = sql_update("product", updated_product)
        update(updated_product, sql)
    return product_list


# Delete a product and update database
def delete_product(product_list):
    print_list(product_list)
    index = int(
        input(
            "\nPlease enter the number of the product you would like to delete, alternatively, press enter to cancel.\n"
        )
    )
    deleted_product = product_list[index]
    id = product_list[index]["id"]
    if index != "":
        del product_list[index]
        sql = sql_delete("product", id)
        update(deleted_product, sql)
    return product_list


# Create new courier and save to database
def create_courier(courier_list=[]):
    new_courier = {}
    new_courier["id"] = uuid_generator()
    user_input = string_with_cancel(courier_list, "name", "name")
    if user_input != "0":
        new_courier["name"] = user_input
        new_courier["phone"] = string_input(courier_list, "phone", "phone number")
        sql = sql_add("courier", new_courier)
        update(new_courier, sql)
        courier_list.append(new_courier)
    return courier_list


# Update a courier and save to database
def update_courier(courier_list=[]):
    print_list(courier_list)
    index = int(
        input(
            "Please enter the number of the courier you would like to update, alternatively, enter 0 to cancel.\n"
        )
    )
    if index != 0:
        update_courier = courier_list[index]
        user_input = input(
            "\nName: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            update_courier["name"] = courier_list[index]["name"] = string_input(
                courier_list, "name", "name"
            )
        user_input = input(
            "\nPhone number: Enter any key to update, or press enter to continue.\n\n"
        )
        if user_input != "":
            update_courier["phone"] = courier_list[index]["phone"] = string_input(
                courier_list, "phone"
            )
        sql = sql_update("courier", update_courier)
        update(update_courier, sql)
    return courier_list


# Delete a courier and update database
def delete_courier(courier_list):
    print_list(courier_list)
    index = int(
        input(
            "\nPlease enter the number of the courier you would like to delete, alternatively, enter 0 to cancel.\n"
        )
    )
    deleted_courier = courier_list[index]
    id = courier_list[index]["id"]
    if index != 0:
        del courier_list[index]
        sql = sql_delete("courier", id)
        update(deleted_courier, sql)
    return courier_list


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
    if user_input != "":
        new_transaction["customer_name"] = user_input
        new_transaction["customer_address"] = string_input(
            order_list, "customer_address", "customer address"
        )
        new_transaction["customer_phone"] = string_input(
            order_list, "customer_phone", "customer phone number"
        )
        new_transaction["courier_id"] = select_courier(courier_list)
        new_transaction["order_status"] = order_status()
        sql = sql_add("transaction", new_transaction)
        update(new_transaction, sql)
        order_list.append(new_transaction)
        basket_list = create_basket(id, basket_list, product_list)
    return basket_list, order_list


# Update order status and save to database
def update_order_status(order_list=[]):
    print_list(order_list)
    index = int(
        input(
            "Please enter the order number of the status you would like to update, alternatively, enter 0 to cancel.\n"
        )
    )
    if index != 0:
        updated_order_status = order_list[index]
        updated_order_status["order_status"] = order_list[index][
            "order_status"
        ] = order_status()
        sql = sql_update("transaction", updated_order_status)
        update(updated_order_status, sql)
    return order_list


# Update products in basket and save to database
def update_basket(transaction_id="", basket_list=[], product_list=[]):
    user_input = "1"
    while user_input == "1" or user_input == "2":
        order_list = list_for_id(transaction_id, "transaction_id", basket_list)
        products = list_values(order_list, "product_name")
        print_list(products)
        index = int(
            input("Please select the number of the basket you would like to update.\n")
        )
        user_input = input(
            "\nEnter 1 to update or 2 to delete, alternatively, enter anything else to cancel.\n"
        )
        selected_basket = order_list[index]
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
            id = order_list[index]["id"]
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
        updated_order = order_list[index]
        user_input = input(
            "\nCustomer name: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            updated_order["customer_name"] = order_list[index][
                "customer_name"
            ] = string_input(order_list, "customer_name", "customer_name")
        user_input = input(
            "\nCustomer adress: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            updated_order["customer_address"] = order_list[index][
                "customer_address"
            ] = string_input(order_list, "customer_address", "customer_address")
        user_input = input(
            "\nCustomer phone number: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            updated_order["customer_phone"] = order_list[index][
                "customer_phone"
            ] = string_input(order_list, "customer_phone", "customer_phone")
        user_input = input(
            "\nCourier: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            updated_order["courier_id"] = order_list[index][
                "courier_id"
            ] = select_courier(courier_list)
        user_input = input(
            "\nOrdered items: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            id = order_list[index]["id"]
            basket_list = update_basket(id, basket_list, product_list)
    sql = sql_update("transaction", updated_order)
    update(updated_order, sql)
    return basket_list, order_list


# Delete an order and update database
def delete_order(order_list=[]):
    print_list(order_list)
    index = int(
        input(
            "Please enter the number of the order you would like to delete, alternatively, enter 0 to cancel.\n"
        )
    )
    deleted_order = order_list[index]
    id = order_list[index]["id"]
    if index != 0:
        del order_list[index]
        sql = sql_delete("transaction", id)
        update(deleted_order, sql)
    return order_list