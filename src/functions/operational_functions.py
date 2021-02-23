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
    os.system("clear")
    return product_list


# Update a product and save to database
def update_product(product_list=[]):
    id, unused = select_item(product_list, "the product you would like to update")
    if id != 0:
        index = next(
            (index for (index, d) in enumerate(product_list) if d["id"] == id), None
        )
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
        os.system("clear")
    return product_list


# Delete a product and update database
def delete_product(product_list):
    id, unused = select_item(product_list, "the product you would like to delete")
    if id != 0:
        index = next(
            (index for (index, d) in enumerate(product_list) if d["id"] == id), None
        )
        deleted_product = product_list[index]
        id = product_list[index]["id"]
        if index != "":
            del product_list[index]
            sql = sql_delete("product", id)
            update(deleted_product, sql)
        os.system("clear")
    return product_list


# Create new courier and save to database
def create_courier(courier_list=[]):
    new_courier = {}
    new_courier["id"] = uuid_generator()
    user_input = string_with_cancel(courier_list, "name", "name")
    if user_input != "":
        new_courier["name"] = user_input
        new_courier["phone"] = string_input(courier_list, "phone", "phone number")
        sql = sql_add("courier", new_courier)
        update(new_courier, sql)
        courier_list.append(new_courier)
    os.system("clear")
    return courier_list


# Update a courier and save to database
def update_courier(courier_list=[]):
    id, unused = select_item(courier_list, "the courier you would like to update")
    if id != 0:
        index = next(
            (index for (index, d) in enumerate(courier_list) if d["id"] == id), None
        )
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
        os.system("clear")
    return courier_list


# Delete a courier and update database
def delete_courier(courier_list):
    id, unused = select_item(courier_list, "the courier you would like to delete")
    if id != 0:
        index = next(
            (index for (index, d) in enumerate(courier_list) if d["id"] == id), None
        )
        deleted_courier = courier_list[index]
        id = courier_list[index]["id"]
        if index != 0:
            del courier_list[index]
            sql = sql_delete("courier", id)
            update(deleted_courier, sql)
        os.system("clear")
    return courier_list


# Add products to basket and save to database
def create_basket(transaction_id="", basket_list=[], product_list=[]):
    new_basket = {}
    new_basket["transaction_id"] = transaction_id
    user_input = 1
    product_id, product_name = select_product(product_list)
    while product_id != "0":
        new_basket["id"] = uuid_generator()
        new_basket["product_id"] = product_id
        new_basket["product_name"] = product_name
        sql = sql_add("basket", new_basket)
        update(new_basket, sql)
        basket_list.append(new_basket.copy())
        product_id, product_name = select_product(product_list)
    os.system("clear")
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
        courier_id, courier_name = select_item(courier_list, "courier")
        new_transaction["courier_id"] = courier_id
        new_transaction["courier_name"] = courier_name
        new_transaction["order_status"] = order_status()
        sql = sql_add("transaction", new_transaction)
        update(new_transaction, sql)
        order_list.append(new_transaction)
        basket_list = create_basket(id, basket_list, product_list)
    os.system("clear")
    return basket_list, order_list


# Update order status and save to database
def update_order_status(order_list=[]):
    id, unused = select_item(order_list, "the status you would like to update")
    if id != 0:
        index = next(
            (index for (index, d) in enumerate(order_list) if d["id"] == id), None
        )
        updated_order_status = order_list[index]
        updated_order_status["order_status"] = order_list[index][
            "order_status"
        ] = order_status()
        sql = sql_update("transaction", updated_order_status)
        update(updated_order_status, sql)
        os.system("clear")
    return order_list


# Update products in basket and save to database
def update_basket(transaction_id="", basket_list=[], product_list=[]):
    user_input = "1"
    options = ["1", "2", "3"]
    while user_input in options:
        order_list = list_for_id(
            transaction_id, basket_list
        )  # List of all items ordered in specified transaction
        user_input = input(
            "\nEnter 1 to add a product, 2 to update a product, or 3 to delete a product. Alternatively, enter anything else once complete.\n"
        )
        os.system("clear")
        if user_input == "1":
            basket_list = create_basket(transaction_id, basket_list, product_list)
        elif user_input == "2":
            if order_list == []:
                print("There are no items in this basket.")
                return update_basket(transaction_id, basket_list, product_list)
            id, unused = select_item(order_list, "basket you would like to update")
            if id != 0:
                product_id, product_name = select_product(product_list)
                if product_id != "0":
                    basket_list_index = next(
                        (
                            index
                            for (index, d) in enumerate(basket_list)
                            if d["id"] == id
                        ),
                        None,
                    )
                    selected_basket = basket_list[
                        basket_list_index
                    ]  # Extract dictionary for chosen id
                    selected_basket["product_id"] = basket_list[basket_list_index][
                        "product_id"
                    ] = product_id
                    selected_basket["product_name"] = basket_list[basket_list_index][
                        "product_name"
                    ] = product_name
                    sql = sql_update("basket", selected_basket)
                    update(selected_basket, sql)

        elif user_input == "3":
            if order_list == []:
                print("There are no items in this basket.")
                return update_basket(transaction_id, basket_list, product_list)
            id, unused = select_item(order_list, "basket you would like to delete")
            if id != 0:
                basket_list_index = next(
                    (index for (index, d) in enumerate(basket_list) if d["id"] == id),
                    None,
                )
                selected_basket = basket_list[basket_list_index]
                del basket_list[basket_list_index]
                sql = sql_delete("basket", id)
                update(selected_basket, sql)
    os.system("clear")
    return basket_list


# Update order and save to database
def update_order(order_list=[], courier_list=[], basket_list=[], product_list=[]):
    id, unused = select_item(order_list, "the order you would like to update")
    if id != 0:
        index = next(
            (index for (index, d) in enumerate(order_list) if d["id"] == id), None
        )
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
            courier_id, courier_name = select_item(courier_list, "courier")
            updated_order["courier_id"] = order_list[index]["courier_id"] = courier_id
            updated_order["courier_name"] = order_list[index][
                "courier_name"
            ] = courier_name
        sql = sql_update("transaction", updated_order)
        update(updated_order, sql)
        user_input = input(
            "\nOrdered items: Enter any key to update, or press enter to continue.\n"
        )
        if user_input != "":
            id = order_list[index]["id"]
            basket_list = update_basket(id, basket_list, product_list)
    os.system("clear")
    return basket_list, order_list


# Delete an order and update database
def delete_order(order_list=[]):
    id, unused = select_item(order_list, "the order you would like to delete")
    if id != 0:
        index = next(
            (index for (index, d) in enumerate(order_list) if d["id"] == id), None
        )
        deleted_order = order_list[index]
        id = order_list[index]["id"]
        del order_list[index]
        sql = sql_delete("transaction", id)
        update(deleted_order, sql)
    os.system("clear")
    return order_list