from File_Functions import load_txt_data, save_txt_data, load_csv_data
from List_Functions import (
    number_items,
    create,
    update,
    delete,
    new_order,
    update_order_status,
    update_order,
    delete_order,
)

# # Load products and couriers data
# products = load_txt_data("Products.txt")
couriers = load_txt_data("Couriers.txt")
orders = load_csv_data("Orders.csv")

# new_order(couriers, orders)
# print(orders)
delete_order(orders)